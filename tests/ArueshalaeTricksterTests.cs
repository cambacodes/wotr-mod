using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Arueshalae, Trickster (Writer/handoffs/trickster/arueshalae.md; F18): "Treatment".
// One block per spec rules test (Trk_Arueshalae_*), the shape of each hook, the living courtship (arueshalae_treatment:
// she proposes; the second ask has no price), the rulebook placements (the arcade and the awning on two bodies), and the
// device redesign of 2026-10-01 ("Prevention, not resurrection"): the Scroll of Death Ward the engine spends per
// protected touch, the retired returns (nothing in the route returns her from death), the lair kill that closes her
// route, Nocticula's retired court.arueshalae, and no living coda on the dead branches.
internal static class ArueshalaeTricksterTests
{
    private const string Unit = "a352873d37ec6c54c9fa8f6da3a6b3e1";
    private const string Hub = "03ebad9587cbea0438d901a0f8df44f1";
    private const string EvilUnit = "e3bc95db7e2181d41847b3a1d858258d";
    private const string EvilNpc = "2c8caedd0a558524ca0ed1ab3132fae1";
    private const string Lair = "fe9eaf819cf03424a9108aa8b777694d";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Jeweler = "bc1093231b1577a4485a730c29595195";
    private const string Tailor = "253cdb8f434e5a6469b75e18428316e3";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string Wilcer = "a380d926e92f70e429681eb9654478f9";
    private const string MeetEvilList = "3ef227bb0ba84104387fd9b4865a4ce0";
    private const string TasteCue = "480082b0c04099540be2ed84be7c9536";
    private const string OfferCue = "68cfcd112d6060141a492949392692aa";
    private const string Scroll = "89e10c3f21fa50c4b8719e004c7628d3";
    private const string Ward = "arueshalae.ward_held";
    private const string P = "arueshalae.trickster.";
    private const string T = "arueshalae.treatment.";

    private static Snapshot World(Story story, int chapter, string area, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = area, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        state.AvailableContacts.Add(EvilUnit);
        state.AvailableContacts.Add(EvilNpc);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Choice Ch(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Ch(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))
                                                          && chosen.Forbids.All(f => !r.Has(f) || chosen.Set.Contains(f))).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot First(Scene scene, Snapshot w, string node, int index) => After(scene, w, node, index).FirstOrDefault() ?? w;
        bool Avail(Scene scene, Snapshot w) => Rules.Available(story, scene, w);
        var own = story.Scenes.Where(s => s.Relationship == "arueshalae" && !s.Reaction && s.Owner == "Arueshalae").ToArray();
        // Plays every available Arueshalae scene forward (in the given area) and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag, int chapter, string area)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 24 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 100, chapter);
                    w.Area = area;
                    foreach (var scene in own.Where(s => Avail(s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            if (r.Has(flag)) return true;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(300).ToList();
            }
            return false;
        }

        // --- Shape: relationship, revival, presences (06-ROUTE-REGISTRY placements) --------------------------------
        var rel = story.Relationships["arueshalae"];
        check(rel.StartedFlag == "arueshalae.started" && rel.ClosedFlag == "arueshalae.closed" && rel.CommittedFlag == "arueshalae.committed"
              && rel.UnavailableFlags.SequenceEqual(new[] { "arueshalae_dead", "arueshalae.evil_dead", "arueshalae.kicked_out", "arueshalae.kicked_out_evil" })
              && rel.UnavailableOverrides["arueshalae_dead"] == P + "returned" && rel.UnavailableOverrides["arueshalae.evil_dead"] == P + "returned"
              && !rel.UnavailableOverrides.ContainsKey("arueshalae.kicked_out")
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "dead", "evil_dead", "failed" }),
            "Arueshalae's relationship does not match the spec (kick-out is closure, never overridden).");
        check(story.Revivals["arueshalae"].Unit == Unit && story.Revivals["arueshalae"].DeathFlag == "arueshalae_dead",
            "Her revival is not her companion unit behind her death etude.");
        var arcade = story.Presences["arueshalae.presence.evil_drezen"];
        var awning = story.Presences["arueshalae.presence.evil_awning"];
        var lairPresence = story.Presences["arueshalae.presence.evil"];
        check(arcade.At?.NearUnit == Jeweler && awning.At?.NearUnit == Tailor && arcade.Unit == EvilUnit && awning.Unit == EvilNpc
              && awning.Requires.Contains("arueshalae.presence.evil_drezen.failed") && arcade.Dialog == "hub" && awning.Dialog == "hub",
            "The evil Drezen beats are not at the jeweller with the tailor's awning as a second-body fallback.");
        foreach (var pr in new[] { arcade, awning, lairPresence })
            check(pr.At?.NearUnit != Fye && pr.At?.NearUnit != Wilcer, "A presence sits at a crowded anchor (Fye or Wilcer Garms).");
        check(lairPresence.At?.Locator == "8b58ebe0-42a8-4be6-96dc-75926e191cb6" && lairPresence.Area == Lair,
            "The lair presence is not at her own native locator.");
        foreach (var s in own.Where(s => !Rules.IsRemote(s) && s.InteractionHub == null && s.AnswerLists.Contains(Hub)))
            check(s.ContactUnit == Unit, "A hub scene is not hers: " + s.Id);
        foreach (var s in story.Scenes.Where(s => s.Relationship == "arueshalae" && s.Id.EndsWith("_yard")))
            check(s.ContactUnit == EvilNpc && s.InteractionHub == "arueshalae.presence.evil_awning"
                  && s.Requires.Contains("arueshalae.presence.evil_drezen.failed"),
                "An awning twin is not on the second body behind the arcade's failure: " + s.Id);

        // --- Device redesign (2026-10-01): nothing in the route returns her from death ----------------------------
        // Dead in the party, the crusade's own Raise Dead / Resurrection serve; the old return and its insurance are
        // retired by gating (ids, nodes and choice indices kept); every revive or return answer sits in a retired scene.
        var starving = S(P + "dead.starving");
        bool Retired(Scene sc) => sc.Forbids.Contains("chapter_later") && sc.MinChapter >= 2;   // the runtime holds chapter_later from Chapter 2 on
        check(starving.TricksterDevice && starving.TricksterState == "dead" && Retired(starving) && Retired(S(P + "insurance"))
              && starving.Recovery == null && starving.Nodes.SelectMany(n => n.Choices).All(ch => ch.Revive == null)
              && starving.Nodes.Select(n => n.Id).SequenceEqual(new[] { "start", "treat", "wake", "rite_holds", "rite_fails", "work", "thread", "claimed", "plea", "vow" })
              && starving.Nodes.Single(n => n.Id == "start").Choices.Count == 4 && starving.Nodes.Single(n => n.Id == "plea").Choices.Count == 3,
            "Trk_Arueshalae_Retired: the old return is not retired by gating with its ids and choice indices kept.");
        foreach (var sc in story.Scenes.Where(sc => sc.Relationship == "arueshalae" || sc.Id.StartsWith("arueshalae.", StringComparison.Ordinal)))
            foreach (var ch in sc.Nodes.SelectMany(n => n.Choices))
                if (ch.Revive != null || ch.Set.Contains(P + "returned"))
                    check(Retired(sc), "Trk_Arueshalae_NoReturn: a live answer still returns her from death: " + sc.Id);
        var dead = Later(story, World(story, 3, Drezen, "trickster", "trickster.ever", P + "gift_held", "trickster.religion_tier1",
                                      "arueshalae_dead", "arueshalae_dead.latched", "revive.arueshalae.available"), 30);
        check(!Avail(starving, dead) && !Avail(S(P + "insurance"), Later(story, World(story, 3, Drezen, "trickster", "trickster.ever"), 30)),
            "Trk_Arueshalae_NoReturn: the retired diagnosis or insurance still opens.");
        check(!own.Any(sc => Avail(sc, Later(story, dead, 100, 5))),
            "Trk_Arueshalae_DeadUnraised: a scene of hers plays while she lies dead and unraised.");
        // Ruling 3: the native rites work on her; the route never says otherwise.
        foreach (var sc in story.Scenes.Where(sc => sc.Relationship == "arueshalae"))
            foreach (var text in sc.Nodes.SelectMany(n => n.Paragraphs.Select(pp => pp.Text).Prepend(n.Text)).Append(sc.Entry))
                check(!System.Text.RegularExpressions.Regex.IsMatch(text, @"(won't|will not|wouldn't|would not) raise (a|me|her|a succubus|a demon)"),
                    "Trk_Arueshalae_RaiseDead: the route claims the crusade will not raise her: " + sc.Id);
        var lostPage = S("arueshalae.lastcall.page");
        var lost = story.Books["trickster.ledger"].Entries.Single(e => e.Id == "lost.arueshalae");
        var lair = story.Books["trickster.ledger"].Entries.Single(e => e.Id == "lost.arueshalae_lair");
        check(lostPage.Forbids.Contains("arueshalae_dead") && lostPage.ForbidOverrides["arueshalae_dead"] == P + "returned"
              && lost.Requires.Contains("arueshalae_dead") && lost.Forbids.SequenceEqual(new[] { P + "returned" }) && !lost.Text.Contains("will not raise")
              && lair.Requires.Contains("arueshalae.evil_dead") && lair.Forbids.Contains(P + "returned"),
            "Trk_Arueshalae_Ledger: an unraised death keeps a living coda, or the Ledger does not state the loss truthfully.");

        // --- Legacy (saves that already hold the old return): Aftertaste / Terms / TermsRefusal / TermsAgain ------
        var aftertaste = S(P + "returned.aftertaste");
        var returned3 = Later(story, World(story, 3, Drezen, "trickster.ever", P + "returned", P + "cost.fed_on_you"), 30);
        check(Avail(aftertaste, returned3), "Trk_Arueshalae_Aftertaste: not available after the return.");
        var tasted = First(aftertaste, returned3, "test", 0);
        check(tasted.Has(P + "aftertaste") && tasted.Has(P + "said_every_time"), "Trk_Arueshalae_Aftertaste: the test does not record her answer.");
        var terms = S(P + "terms");
        check(!Avail(terms, Later(story, tasted, 100)), "Trk_Arueshalae_Aftertaste: the commit opens in Chapter 3.");
        var ch5Returned = Later(story, World(story, 5, Drezen, "trickster.ever", P + "returned", P + "aftertaste"), 100);
        check(Avail(terms, ch5Returned), "Trk_Arueshalae_TermsCommit: terms not available in Chapter 5.");
        check(First(terms, ch5Returned, "question", 0).Has("arueshalae.committed"), "Trk_Arueshalae_TermsCommit: 'Both' does not commit.");
        var notYet = First(terms, ch5Returned, "question", 2);
        check(notYet.Has(P + "declined") && !notYet.Has("arueshalae.committed"), "Trk_Arueshalae_TermsRefusal: not a soft no.");
        var again = S(P + "terms_again");
        check(Avail(again, Later(story, notYet, 170)), "Trk_Arueshalae_TermsRefusal: the second ask does not open.");
        var sworn = First(again, Later(story, notYet, 170), "start", 0);
        check(sworn.Has("arueshalae.committed") && sworn.Has(P + "cost.no_second_joke"), "Trk_Arueshalae_TermsAgain: the promise does not commit.");
        check(!Avail(again, Later(story, notYet, 100)), "Trk_Arueshalae_TermsAgain: the week is shorter than seven days.");

        // --- Evil at the lair: the house call into the native recruitment; the kill closes the route (ruling 4) -------
        var home = S(P + "evil.home_visit");
        check(home.AnswerLists.SequenceEqual(new[] { MeetEvilList }) && home.ContactUnit == null && home.EntryMythic == "PlayerIsTrickster"
              && home.Nodes.Single().Choices.Count == 1 && Ch(home, "start", 0).NativeNext == OfferCue && !home.TricksterDevice,
            "Trk_Arueshalae_EvilHome: the house call is not one terminal answer into the native offer (Cue_0011).");
        var lairWorld = World(story, 5, Lair, "trickster", "trickster.ever");
        check(Avail(home, lairWorld) && !Avail(home, World(story, 5, Lair, "trickster", "trickster.ever", "arueshalae.evil_dead"))
              && !Avail(home, World(story, 5, Lair, "trickster", "trickster.ever", "arueshalae.evil_recruited")),
            "Trk_Arueshalae_EvilHome: the house call is offered after the kill or the recruitment, or not at all.");
        foreach (var id in new[] { "evil.diagnosis", "evil.late_referral", "evil.second_opinion", "evil.wager", "evil.wager_yard" })
            check(Retired(S(P + id)), "Trk_Arueshalae_Retired: " + id + " is not retired by gating.");
        var killed = Later(story, World(story, 5, Drezen, "trickster", "trickster.ever", "arueshalae.evil_dead", "arueshalae.evil_dead.latched",
                                        P + "primed", T + "intake", T + "studied"), 100);
        check(!own.Any(sc => Avail(sc, killed)) && !Reaches(killed, "arueshalae.committed", 5, Drezen)
              && !Reaches(killed, P + "returned", 5, Lair),
            "Trk_Arueshalae_EvilKilled: the lair kill does not close her route (a scene, a return or a commit still opens).");
        var deadCommitted = Later(story, World(story, 6, Drezen, "trickster.ever", "arueshalae.evil_dead", "arueshalae.committed", "lastcall.active"), 10);
        check(!Avail(lostPage, deadCommitted) && !Avail(lostPage, Later(story, World(story, 6, Drezen, "trickster.ever", "arueshalae_dead",
                  "arueshalae.committed", "lastcall.active"), 10)),
            "Trk_Arueshalae_NoLivingCoda: a dead branch still gets her living Last Call coda.");

        // --- Legacy (saves that already hold the queen's return): Reunion / Letter / Terms / Refusal / the night ------
        var reunion = S(P + "evil.reunion");
        check(reunion.InteractionHub == "arueshalae.presence.evil" && reunion.ContactUnit == EvilUnit && reunion.Areas.SequenceEqual(new[] { Lair }),
            "The reunion is not on the lair presence.");
        var back = Later(story, World(story, 5, Lair, "trickster.ever", "arueshalae.evil_dead", P + "returned", P + "cost.nocticula_debt"), 30);
        check(Avail(reunion, back), "Trk_Arueshalae_EvilReunion: not available.");
        check(Ch(reunion, "price", 2).Set.Contains(P + "cost.fed_on_demon") && Ch(reunion, "price", 2).Requires.Contains(P + "cost.late")
              && Ch(reunion, "price", 4).Set.Contains(P + "cost.fed_on_demon") && Ch(reunion, "price", 4).Forbids.Contains(P + "cost.late")
              && Ch(reunion, "price", 2).Alignment == null && Ch(reunion, "price", 4).Alignment == null,
            "The reunion's third way does not match the path (the vrock only after the late referral; the babau otherwise).");
        check(First(reunion, back, "price", 4).Has(P + "cost.fed_on_demon"), "The primed path's third way (the babau) is not playable.");
        var hungry = First(reunion, back, "price", 3);
        check(hungry.Has(P + "reunited") && hungry.Has(P + "cost.sent_away_hungry"), "Trk_Arueshalae_EvilReunion: refusing does not reunite, hungry.");
        var letterTwin = S(P + "evil.reunion_letter");
        var lairFailed = Program.Copy(back); lairFailed.Flags.Add("arueshalae.presence.evil.failed");
        // PP2 (Sol COX): a failed lair moves the reunion to Drezen in person; the note is left only when every anchor fails.
        check(!Avail(letterTwin, Later(story, lairFailed, 130)), "Trk_Arueshalae_EvilReunionLetter: a letter while Drezen can still host her.");
        var allFailed = Program.Copy(lairFailed);
        allFailed.Flags.Add("arueshalae.presence.evil_drezen.failed"); allFailed.Flags.Add("arueshalae.presence.evil_awning.failed");
        check(Avail(letterTwin, Later(story, allFailed, 130)), "Trk_Arueshalae_EvilReunionLetter: no letter when every anchor fails.");
        var evilTerms = S(P + "evil.terms");
        var reunitedW = Later(story, World(story, 5, Drezen, "trickster.ever", "arueshalae.evil_dead", P + "returned", P + "reunited", P + "cost.nocticula_debt"), 60);
        check(Avail(evilTerms, reunitedW) && evilTerms.InteractionHub == "arueshalae.presence.evil_drezen", "Trk_Arueshalae_EvilTermsCommit: not available at the arcade.");
        var open = First(evilTerms, reunitedW, "ask", 0);
        check(open.Has("arueshalae.committed") && open.Has(P + "cost.open_door"), "Trk_Arueshalae_EvilTermsCommit: the open door does not commit.");
        var stay = First(evilTerms, reunitedW, "ask", 1);
        check(stay.Has(P + "ally") && !stay.Has("arueshalae.committed"), "Trk_Arueshalae_EvilTermsRefusal: 'stay' is not her refusal.");
        var window = S(P + "evil.window");
        check(Avail(window, Later(story, open, 30)), "The fallen's night does not follow the open door.");

        // --- Failed: the chaplain -------------------------------------------------------------------------------
        var chaplain = S(P + "failed.chaplain");
        var failed = Later(story, World(story, 3, Drezen, "trickster", "trickster.ever", "arueshalae.failed"), 5);
        check(Avail(chaplain, failed) && chaplain.EntryMythic == "PlayerIsTrickster" && chaplain.TricksterState == "failed",
            "Trk_Arueshalae_Failed: the appointment is not available.");
        var appointed = First(chaplain, failed, "sword", 0);
        check(appointed.Has(P + "cost.chaplain") && appointed.Has("arueshalae.started"), "Trk_Arueshalae_Failed: the job does not stick.");
        var ch5Chaplain = Later(story, World(story, 5, Drezen, "trickster.ever", P + "cost.chaplain"), 100);
        check(First(terms, ch5Chaplain, "question", 3).Has("arueshalae.closed"), "Trk_Arueshalae_FailedTermsNeither: 'Neither' does not close.");
        check(!First(terms, ch5Chaplain, "question", 1).Has("arueshalae.committed") && First(terms, ch5Chaplain, "question", 1).Has(P + "declined"),
            "Trk_Arueshalae_FailedTermsCommit: 'only the good days' commits her to an answer she refuses (R2-1).");

        // --- The treatment: the living courtship -----------------------------------------------------------------
        var intake = S(T + "intake");
        var study = S(T + "studied");
        var reader = World(story, 3, Drezen, "trickster", "trickster.ever");
        check(Avail(study, reader) && !Avail(intake, reader), "The intake opens before the Commander has done the reading.");
        check(study.Nodes.Single(n => n.Id == "why").Choices.Any(c => c.Check?.Skill == "SkillLoreReligion" && c.Forbids.Contains("trickster.religion_tier1")),
            "The reading has no Lore (Religion) check for a Commander without the trick.");
        var alive = World(story, 3, Drezen, "trickster", "trickster.ever", T + "studied");
        check(Avail(intake, alive) && intake.EntryMythic == "PlayerIsTrickster", "The treatment's intake is not open after the reading.");
        check(!Avail(intake, World(story, 3, Drezen, "trickster.ever")), "The intake opens without the live Trickster path.");
        var patient = First(intake, alive, "her", 0);
        check(patient.Has(T + "intake") && patient.Has("arueshalae.started"), "The intake does not start the relationship.");
        var warded = Program.Copy(patient); warded.Flags.Add(Ward);
        check(Reaches(warded, T + "relapse_two", 5, Drezen), "The treatment cannot reach its second relapse with a scroll in hand.");
        check(!Reaches(warded, T + "touched", 5, Lair), "Trk_Arueshalae_Drezen: the chapel procedure plays away from Drezen.");
        check(!Reaches(patient, T + "touched", 5, ""), "Trk_Arueshalae_NoScrollNoTouch: the procedure touches her without a scroll.");
        // --- The Death Ward cost (ruling 2): the engine removes one Scroll of Death Ward per protected touch ------------
        var touch = S(T + "touched");
        check(story.InventoryItems[Ward] == Scroll && story.RemovableItems.Contains(Scroll),
            "Trk_Arueshalae_DeathWard: the Scroll of Death Ward is not the bound, removable item.");
        foreach (var sc in story.Scenes.Where(sc => sc.Relationship == "arueshalae"))
            foreach (var ch in sc.Nodes.SelectMany(n => n.Choices).Where(ch => ch.RemoveItem != null))
                check(ch.RemoveItem == Scroll && (ch.Requires.Contains(Ward) || sc.Requires.Contains(Ward)),
                    "Trk_Arueshalae_DeathWard: a removal that is not the scroll, or not gated on holding one: " + sc.Id);
        check(new[] { 0, 1 }.All(i => Ch(touch, "explain", i).Requires.Intersect(Ch(touch, "explain", i).Forbids).Any())
              && Ch(touch, "explain", 3).RemoveItem == Scroll && Ch(touch, "explain", 3).Requires.Contains(Ward)
              && Ch(touch, "explain", 4).Forbids.Contains(Ward),
            "Trk_Arueshalae_DeathWard: the procedure still offers the candle or the lore, or the scroll answer is not appended.");
        var touchW = Later(story, World(story, 3, Drezen, "trickster", "trickster.ever", T + "intake", T + "relapse", Ward), 60);
        var wardedTouch = Program.WalkVia(touch, touchW, "explain", 3);
        check(wardedTouch.Count > 0 && wardedTouch.All(r => r.Has(T + "touched") && r.Has(T + "cure_works") && !r.Has(Ward)),
            "Trk_Arueshalae_DeathWard: the protected touch does not spend the scroll.");
        var bare = Program.Copy(touchW); bare.Flags.Remove(Ward);
        check(Program.Walk(touch, bare).All(r => !r.Has(T + "touched")) && Program.WalkVia(touch, bare, "explain", 4).Count > 0
              && Program.WalkVia(touch, bare, "explain", 4).All(r => !r.Has(touch.Id) && !r.Has(T + "touched")),
            "Trk_Arueshalae_NoScrollNoTouch: without a scroll the procedure still touches, or does not stay replayable.");
        // The Trickster's lore lowers the reading's DC and protects nothing (no live answer outside the reading reads it).
        foreach (var sc in story.Scenes.Where(sc => sc.Relationship == "arueshalae" && sc.Id != T + "studied"))
            foreach (var ch in sc.Nodes.SelectMany(n => n.Choices).Where(ch => !ch.Requires.Intersect(ch.Forbids).Any()))
                check(!ch.Requires.Contains("trickster.religion_tier1") && !ch.Forbids.Contains("trickster.religion_tier1") || Retired(sc),
                    "Trk_Arueshalae_NoLoreShield: a live answer still selects on the Trickster's lore: " + sc.Id);
        var readingChoices = S(T + "studied").Nodes.Single(n => n.Id == "why").Choices;
        check(readingChoices[0].Check!.DC < readingChoices[1].Check!.DC && readingChoices[1].Check!.DC == 15, "The lore does not merely lower the reading's DC.");
        var slip = S(T + "rite_slipped");
        var slipW = Later(story, World(story, 5, Drezen, "trickster.ever", T + "intake", T + "touched", T + "kitchen"), 60);
        check(Avail(slip, slipW) && slip.Nodes.Single(n => n.Id == "distance").Choices.All(c => c.Set.Contains("arueshalae.trickster.cost.drained")),
            "The missed rite is not a priced, visible cost with her distance to answer.");
        check(S(T + "relapse_two").Requires.Contains(T + "rite_slipped"), "The second relapse does not follow the missed rite.");
        var proposal = S(T + "prescription");
        var ask = proposal.Nodes.Single(n => n.Id == "ask");
        check(ask.Choices.Count == 4 && ask.Choices.All(c => c.Crusade == null && c.Alignment == null),
            "The proposal is not hers alone (yes / the saint / not yet / no, no price).");
        var ready = Later(story, World(story, 5, Drezen, "trickster.ever", T + "intake", T + "relapse_two", T + "her_call"), 100);
        check(Avail(proposal, ready), "The proposal is not available after the second relapse.");
        var yes = First(proposal, ready, "ask", 0);
        check(yes.Has("arueshalae.committed"), "Her proposal does not commit on yes.");
        var later = First(proposal, ready, "ask", 2);
        var again2 = S(T + "prescription_again");
        check(Avail(again2, Later(story, later, 60)) && again2.Nodes.SelectMany(n => n.Choices).All(c => c.Crusade == null && c.Alignment == null),
            "The second ask is missing, or priced.");
        check(First(again2, Later(story, later, 60), "roof", 0).Has("arueshalae.committed"), "The Commander's ask does not commit.");
        var night = S(T + "night");
        check(night.Requires.Contains("arueshalae.committed") && !Avail(night, Later(story, ready, 50)), "The night opens before any yes.");
        var yesHere = Later(story, yes, 30); yesHere.Area = Drezen;   // PP2: the tower is above Drezen's citadel
        var yesAway = Later(story, yes, 30); yesAway.Area = Lair;
        check(Avail(night, yesHere) && !Avail(night, yesAway), "The night does not follow the yes in Drezen (or plays outside it).");
        // No scroll, no night (it aborts and stays replayable); with one, the ward is read on the tower and spent.
        check(Program.Walk(night, yesHere).All(r => !r.Has(T + "night")), "Trk_Arueshalae_NightWard: the tower night plays with no ward.");
        var yesWarded = Program.Copy(yesHere); yesWarded.Flags.Add(Ward);
        var nightWarded = Program.Walk(night, yesWarded);
        check(nightWarded.Count > 0 && nightWarded.All(r => r.Has(T + "night") && !r.Has(Ward)) && Ch(night, "start", 0).RemoveItem == Scroll,
            "Trk_Arueshalae_NightWard: the warded night does not spend its scroll.");
        var released = Program.Copy(yesHere); released.Flags.Add("arueshalae.back_to_reality");
        check(Program.Walk(night, Later(story, released, 0)).Any(r => r.Has(T + "night")),
            "Trk_Arueshalae_NightWard: after her release from the Abyss the night still demands a ward.");
        foreach (var n in night.Nodes)
            check(!n.Text.Contains(" cot") && !n.Text.Contains("narrow bed"), "The night is staged on a cot: " + n.Id);

        // --- Nocticula's court.arueshalae: retired by gating (ruling 5; nothing produces the favour any more) --------
        var court = S("nocticula.trickster.court.arueshalae");
        var owed = Later(story, World(story, 5, Drezen, "trickster.ever", "arueshalae.started", P + "returned", P + "cost.nocticula_favour", "noct.started"), 30);
        check(Rules.IsRemote(court) && court.Relationship == "nocticula" && Retired(court) && !Avail(court, owed),
            "Trk_Nocticula_CourtArueshalae_Retired: the court still collects a favour nothing produces.");
        check(court.Nodes.Select(n => n.Id).SequenceEqual(new[] { "seal", "letter", "her_side", "chose", "night", "raised" }),
            "Trk_Nocticula_CourtArueshalae_Retired: its nodes were not kept.");

        // --- Reactions: exactly Sosiel and Lann, each behind its reactor's guard ---------------------------------
        var reactions = story.Scenes.Where(s => s.Relationship == "arueshalae" && s.Reaction).ToArray();
        check(reactions.Length > 0 && reactions.All(r => r.Owner == "Sosiel" || r.Owner == "Lann"), "A reactor beyond Sosiel and Lann.");
        foreach (var r in reactions)
            check(r.Forbids.Contains(r.Owner == "Sosiel" ? "sosiel.dead" : "lann.dead")
                  && r.Forbids.Contains(r.Owner == "Sosiel" ? "sosiel.kicked_out" : "lann.kicked_out"),
                "A reaction without its reactor's guard: " + r.Id);

        // --- The Abyss night and the old name are told in Drezen, after the crossing (Chapter 5 only) ----------------
        foreach (var id in new[] { T + "abyss_dose", T + "old_name" })
        {
            var scene = S(id);
            var ch4 = Later(story, World(story, 4, Drezen, "trickster.ever", T + "intake", T + "touched"), 100);
            var ch5 = Later(story, World(story, 5, Drezen, "trickster.ever", T + "intake", T + "touched"), 100);
            check(!Avail(scene, ch4), "A physical Abyss-memory scene is offered in Chapter 4, where the hub cannot play it: " + id);
            check(Avail(scene, ch5), "The Abyss-memory scene is not available in Chapter 5, where it is told: " + id);
        }

        // --- Never another route's state; never a key token; never a crusade fee as the device's price --------------
        foreach (var s in story.Scenes.Where(s => s.Relationship == "arueshalae"))
        {
            foreach (var flag in s.Requires.Concat(s.Forbids).Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids))))
                check(!flag.EndsWith(".closed") || flag == "arueshalae.closed", "An Arueshalae scene reads another route's closure: " + s.Id);
            check(s.Nodes.SelectMany(n => n.Choices).All(c => c.Crusade == null), "A crusade fee in her route: " + s.Id);
        }

        // Q11 witnesses: a failed reading can be retried; the living, recruited fallen Arueshalae has a romance; the
        // Elysium morning drains nothing; elapsed-time claims are enforced; the torn gift costs something the game counts.
        var studied = S(T + "studied");
        var reading = World(story, 3, Drezen, "trickster", "trickster.ever");
        var failedReading = Program.WalkVia(studied, reading, "not_yet", 0);
        check(failedReading.Count > 0 && failedReading.All(r => !r.Has(T + "studied"))
              && Rules.Available(story, studied, Later(story, failedReading[0], 24))
              && !Rules.Available(story, S(T + "intake"), Later(story, failedReading[0], 24)),
            "A failed night reading records the rite as learned, or forbids the promised retry.");
        var learned = Program.WalkVia(studied, reading, "fit", 0);
        check(learned.Count > 0 && learned.All(r => r.Has(T + "studied")) && Rules.Available(story, S(T + "intake"), Later(story, learned[0], 24)),
            "A successful night reading does not open the intake.");
        var houseCall = S(P + "fallen.house_call");
        var recruited = World(story, 5, Drezen, "trickster", "trickster.ever", "arueshalae.evil_recruited");
        check(Rules.Available(story, houseCall, recruited) && !recruited.Has("arueshalae.evil_dead")
              && !Rules.Available(story, houseCall, World(story, 5, Drezen, "trickster", "trickster.ever")),
            "The living recruited fallen Arueshalae has no courtship, or it opens without her recruitment.");
        var doorOpen = Program.WalkVia(houseCall, recruited, "ask", 0);
        check(doorOpen.Count > 0 && doorOpen.All(r => r.Has("arueshalae.committed") && r.Has(P + "cost.open_door")),
            "The recruited fallen commit does not commit.");
        var roof = S(P + "fallen.roof");
        var roofW = Later(story, doorOpen[0], 30);
        var roofWarded = Program.Copy(roofW); roofWarded.Flags.Add(Ward);
        check(Rules.Available(story, roof, roofW)
              && Program.WalkVia(roof, roofWarded, "start", 0).Count > 0
              && Program.WalkVia(roof, roofWarded, "start", 0).All(r => r.Has(P + "evil.dawn") && !r.Has(Ward))
              && Program.Walk(roof, roofW).All(r => !r.Has(P + "evil.dawn")),
            "Trk_Arueshalae_FallenWard: the recruited roof night is unreachable with a ward, or plays unwarded (no scroll, no night).");
        var house = S(P + "fallen.house_call");
        check(Ch(house, "price", 0).Requires.Intersect(Ch(house, "price", 0).Forbids).Any() && Ch(house, "price", 3).RemoveItem == Scroll
              && Ch(house, "price", 3).Requires.Contains(Ward),
            "Trk_Arueshalae_FallenWard: the fallen still feeds on the Commander's bare wrist, or the warded fee does not spend a scroll.");
        var notTonight = Program.WalkVia(houseCall, recruited, "ask", 1);
        check(notTonight.Count > 0 && Rules.Available(story, S(P + "fallen.lock"), Later(story, notTonight[0], 80))
              && !Rules.Available(story, S(P + "fallen.lock"), Later(story, notTonight[0], 10)),
            "'Not tonight' does not keep a reachable yes.");
        check(Rules.Available(story, S(P + "epilogue.fallen"), Later(story, doorOpen[0], 100, 6))
              && !Rules.Available(story, S(T + "epilogue.together"), Later(story, World(story, 6, Drezen, "trickster.ever", "arueshalae.committed", T + "intake", "arueshalae.evil_recruited"), 1)),
            "The recruited fallen commit has no ending, or reads the redeemed daybook ending.");
        var morning = S(T + "morning");
        var elysium = Later(story, World(story, 5, Drezen, "trickster", "trickster.ever", "arueshalae.committed", T + "night", "arueshalae.elysium"), 10);
        check(Rules.Available(story, morning, elysium) && Program.WalkVia(morning, elysium, "start", 0).Count == 0
              && Program.WalkVia(morning, elysium, "start", 1).Count > 0,
            "After the native Elysium ending, the morning still counts a drain.");
        check(S(T + "prescription").DelayHours >= 168, "The proposal opens before the fast's seven days have passed.");
        // Ledger row 2: native Nocticula keys reach her route only through Derived aliases, never a choice or scene gate.
        foreach (var s in story.Scenes.Where(s => s.Relationship == "arueshalae"))
            check(s.Requires.Concat(s.Forbids).Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)))
                      .All(k => !k.StartsWith("noct.", StringComparison.Ordinal)),
                "An Arueshalae scene gates on a native Nocticula key: " + s.Id);
        // A soft 'not yet' at the proposal, then the native Elysium ending: the discharge still offers the yes.
        var deferred = World(story, 5, Drezen, "trickster", "trickster.ever", T + "intake", P + "declined", "arueshalae.elysium");
        check(Rules.Available(story, S(T + "discharged"), deferred) && !Rules.Available(story, S(T + "prescription_again"), deferred)
              && Program.WalkVia(S(T + "discharged"), deferred, "ask", 0).All(r => r.Has("arueshalae.committed")),
            "A deferred proposal followed by Elysium locks the treatment out of every commit.");
        // The failed-lair reunion serves the late referral as well: in person at the arcade (PP2), the letter only when every
        // anchor fails.
        var lateLair = Later(story, World(story, 5, Drezen, "trickster", "trickster.ever", P + "returned",
                  "arueshalae.evil_dead", P + "cost.late", P + "cost.nocticula_debt", "arueshalae.presence.evil.failed"), 130);
        lateLair.AvailableContacts.Add(EvilUnit);
        check(Rules.Available(story, S(P + "evil.reunion_city"), lateLair) && !Rules.Available(story, S(P + "evil.reunion_letter"), lateLair),
            "The late referral has no in-person reunion when the lair presence fails.");
        // HOW (Sol r4): chronological witnesses. The proposal waits the fast's 168 hours from the hour the relapse was earned
        // (not from a backdated fixture); a closed chaplain gets no Last Call continuation.
        var earned = World(story, 5, Drezen, "trickster.ever", T + "intake", T + "relapse_two", T + "her_call");
        earned.Times[T + "relapse_two"] = earned.Hour; earned.Times[T + "her_call"] = earned.Hour;
        check(!Avail(proposal, Later(story, earned, 167)) && Avail(proposal, Later(story, earned, 168)),
            "Trk_Arueshalae_Chronology: the proposal does not open exactly at the fast's seventh day.");
        var chapW = Later(story, World(story, 5, Drezen, "trickster.ever", P + "cost.chaplain"), 100);
        var refusedTerms = Program.WalkVia(terms, chapW, "question", 3);
        var againChap = S(P + "terms_again_chaplain");
        var deferredChap = Program.WalkVia(terms, chapW, "question", 2);
        var refusedAgain = deferredChap.SelectMany(d => Program.WalkVia(againChap, Later(story, d, 170), "start", 1)).ToList();
        foreach (var closedW in refusedTerms.Concat(refusedAgain))
        {
            var atEnd = Later(story, closedW, 50, 6); atEnd.Flags.Add("lastcall.active");
            check(closedW.Has("arueshalae.closed") && closedW.Has(P + "terms_refused") && closedW.Has(P + "late_committed")
                  && !Avail(lostPage, atEnd), "Trk_Arueshalae_LastCallClosed: a refused chaplain still gets her Last Call coda.");
        }
        check(refusedAgain.Count > 0, "Trk_Arueshalae_LastCallClosed: the chaplain's second refusal is unreachable.");
        // CAN (Sol r4): after her release the chaplain's yes is about the appointment, not a hunger she fights.
        var chapReleased = Later(story, World(story, 5, Drezen, "trickster.ever", P + "cost.chaplain", P + "declined", "arueshalae.back_to_reality"), 200);
        var yesPages = new HashSet<string>();
        Program.Walk(againChap, chapReleased, (page, _) => yesPages.Add(page));
        check(Avail(againChap, chapReleased) && yesPages.Contains("yes_e") && !yesPages.Contains("yes"),
            "Trk_Arueshalae_ChaplainReleased: the released chaplain still accepts on her hunger.");
        Console.WriteLine("PASS: Arueshalae Trickster (Trk_Arueshalae_*): the Death Ward, the retired returns, the lair kill's closure, the chaplain, the treatment and her proposal, the arcade, and the retired court.");
    }
}
