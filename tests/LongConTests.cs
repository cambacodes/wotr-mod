using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// The Long Con (Writer/handoffs/15-LONG-CON-OPENING.md, PP8): doc 15 section 8 at rules level (Tier 1).
// The entry twins at Chaleb's pyre, the prisoner pages, the citadel offer (one DC per provenance), Nurah's big joke, the
// Areelu crossing and its lens memory, the Ch3 talk in both voices (hub or sergeant, never both), the hanging, the summons,
// the enacted consequences, Minagho's Ch5 variant nodes, the Ledger lines and the reader lint.
internal static class LongConTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Irabeth = "280d4712dceb37f4a88e98f1f4c6e64f";
    private const string Hub = "871af36f2ab2b1f40b5de77976c54276";
    private const string P = "longcon.";
    private const string Begun = P + "begun", Loud = P + "legend_loud", Quiet = P + "legend_quiet";
    private const string Confirmed = P + "rumour_confirmed", Seen = P + "prisoner_seen";
    private const string Hanged = P + "prisoner_hanged", Killed = P + "prisoner_killed", Clerk = P + "clerk_recorded", Fed = P + "legend_fed";
    private const string OfferHeard = P + "offer_heard", Knew = P + "minagho_knew", Witnessed = P + "citadel_witnessed", CitadelDone = P + "citadel_done";
    private const string TalkDone = P + "talk_done", Stands = P + "talk_stands", Wary = P + "irabeth_wary";
    private const string Minder = P + "minder", MinderSeen = P + "minder_seen";
    private const string Proposed = P + "sting_proposed", Owed = P + "sting_owed", ViaIrabeth = P + "sting_via_irabeth", ViaWatch = P + "sting_via_watch";
    private const string StingDone = P + "sting_done", Refused = P + "sting_refused", Exposed = P + "sting_exposed", Scar = P + "sting_scar", AgentLost = P + "agent_lost";
    private const string Deceived = P + "watch_deceived", ColdSeen = P + "irabeth_cold_seen", Offpath = P + "offpath_note";
    private const string Lied = "irabeth.longcon_lied";
    private const string Owned = P + "hanging_owned", Noted = P + "hanging_noted", Accounted = P + "hanging_accounted";
    private const string AfterSeen = P + "irabeth_after_hanging.seen";
    private const string Mask = "areelu.early.mask_counted", Courtesy = "areelu.early.courtesy_done";
    private const string Silent = "areelu.early.read_silent", Offered = "areelu.early.read_offered";
    private const string BothKilled = "pyre.both_killed", OneKilled = "pyre.one_killed";
    private const string Ch3 = P + "reached_ch3";
    private const string M = "minagho_chivarro.trickster.";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = Drezen };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Irabeth);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 500;
        return state;
    }

    private static bool Shown(Paragraph line, Snapshot s) =>
        line.Requires.All(s.Has) && !line.Forbids.Any(s.Has) && line.AnyGroups.All(g => g.Any(s.Has));

    private static IEnumerable<string> Reads(Scene s) =>
        s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)).Concat(s.ForbidOverrides.Keys).Concat(s.ForbidOverrides.Values)
            .Concat(s.Nodes.SelectMany(n => n.Choices.SelectMany(c => c.Requires.Concat(c.Forbids))))
            .Concat(s.Nodes.SelectMany(n => n.Paragraphs.SelectMany(p => p.Requires.Concat(p.Forbids))));

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Choice C(Scene scene, string node, int i) => scene.Nodes.Single(n => n.Id == node).Choices[i];
        Node N(Scene scene, string node) => scene.Nodes.Single(n => n.Id == node);
        bool Avail(Scene scene, Snapshot w) => Rules.Available(story, scene, w);
        var ours = story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal) || s.Id.StartsWith("areelu.early.", StringComparison.Ordinal)).ToList();

        // ---- Section 7: the framework relationship, never closed; every scene explicit. ----
        var rel = story.Relationships["longcon"];
        check(rel.StartedFlag == Begun && rel.ClosedFlag == P + "abandoned" && rel.CommittedFlag == TalkDone && rel.UnavailableFlags.Length == 0,
            "Long Con: the relationship's flags differ from doc 15 section 7.");
        check(!story.Scenes.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Contains(P + "abandoned")))),
            "Long Con: a choice sets longcon.abandoned (the relationship must never close in v1).");
        check(ours.Count == 20 && ours.All(s => s.Relationship == (s.Id.StartsWith("areelu.", StringComparison.Ordinal) ? "areelu" : "longcon")),
            "Long Con: a scene has the wrong or a defaulted Relationship.");
        check(ours.All(s => s.Nodes.All(n => n.Choices.All(c => c.StartEtude == null))), "Long Con: a scene starts a native etude.");

        // ---- Section 2: the entry twins (S1, S3, S4, S8, S10, S11). ----
        var tell = S(P + "tell_them");
        var tellB = S(P + "tell_them_b");
        check(tell.AnswerLists.SequenceEqual(new[] { "99e167bfcc0f3a74ca25cdec4dbe4e39" }) && tellB.AnswerLists.SequenceEqual(new[] { "91fbd759907af9a43ba284ca8845ee45" })
              && new[] { tell, tellB }.All(s => s.ReturnToList && s.EntryMythic == "TricksterUnlocked" && s.Chapters.SequenceEqual(new[] { 1 })
                  && s.Requires.SequenceEqual(new[] { "CalebFooled" }) && s.Forbids.SequenceEqual(new[] { Begun })
                  && (s.ReturnText ?? "").Split(' ').Length <= 25 && s.Nodes.Where(n => n.Id != "start" || true).All(n => n.Speaker == "conversant")),
            "S1/S8: the entry twins are not ReturnToList, EntryMythic TricksterUnlocked, CalebFooled, Ch1, Chaleb as conversant.");
        check(Avail(tell, World(story, 1, "CalebFooled")) && !Avail(tell, World(story, 1)) && !Avail(tell, World(story, 1, "CalebFooled", Begun))
              && !Avail(tell, World(story, 2, "CalebFooled")),
            "S3/S4: the entry ignores CalebFooled, begun or the chapter.");
        foreach (var (flags, node) in new[] { (new string[0], "start"), (new[] { BothKilled }, "both_dead"), (new[] { OneKilled }, "one_dead"),
                                              (new[] { OneKilled, BothKilled }, "both_dead") })
            foreach (var entry in new[] { tell, tellB })
            {
                var visited = new HashSet<string>();
                var outs = Program.Walk(entry, World(story, 1, flags.Append("CalebFooled").ToArray()), (id, _) => visited.Add(id));
                check(outs.Count == 2 && outs.All(r => r.Has(Begun) && new[] { Loud, Quiet }.Count(r.Has) == 1 && r.Has(entry.Id))
                      && (node == "start" ? !visited.Contains("both_dead") && !visited.Contains("one_dead") : visited.Contains(node))
                      && visited.Contains("both_dead") == flags.Contains(BothKilled) && !outs.Any(r => Avail(tell, r) || Avail(tellB, r)),
                    "S1/S8/S11: the entry variant or its outcomes are wrong for " + string.Join(",", flags) + " on " + entry.Id);
            }
        check(new[] { tell, tellB }.All(s => s.Nodes.SelectMany(n => n.Choices).Where(c => c.Set.Contains(Begun)).All(c => c.Alignment?.Direction == "Chaotic" && c.Alignment.Value == 1)),
            "S1: the callous choice is not Chaotic 1.");

        // ---- Section 2b: the prisoner pages (S1, S2, S11, S12). ----
        var pLoud = S(P + "prisoner_loud");
        var pQuiet = S(P + "prisoner_quiet");
        check(new[] { pLoud, pQuiet }.All(s => Rules.IsRemote(s) && s.Chapters.SequenceEqual(new[] { 2 }) && s.Forbids.Contains(Seen) && s.Kind == "event")
              && pLoud.DelayHours == 48 && pQuiet.DelayHours == 168 && pLoud.Requires.Contains(Loud) && pQuiet.Requires.Contains(Quiet),
            "2b: the prisoner twins are not Ch2 remote pages at 48 h / 168 h.");
        var ch2 = World(story, 2, Begun, Loud, "longcon.kc_appointed");
        ch2.Times[Loud] = ch2.Hour - 47;
        check(!Avail(pLoud, ch2), "2b: the loud page comes before 48 h.");
        ch2.Times[Loud] = ch2.Hour - 48;
        check(Avail(pLoud, ch2) && !Avail(pQuiet, ch2) && !Avail(pLoud, World(story, 2, Begun, Loud)) && !Avail(pLoud, World(story, 3, Begun, Loud, "longcon.kc_appointed")),
            "2b: the loud page ignores its legend, the Knight Commander's appointment or Chapter 2.");
        foreach (var both in new[] { false, true })
        {
            var visited = new HashSet<string>();
            var w = both ? World(story, 2, Begun, Loud, "longcon.kc_appointed", BothKilled) : World(story, 2, Begun, Loud, "longcon.kc_appointed");
            var outs = Program.Walk(pLoud, w, (id, _) => visited.Add(id));
            check(outs.Count == 4 && outs.All(r => r.Has(Seen) && r.Has(Confirmed) && new[] { Hanged, Clerk, Fed, Killed }.Count(r.Has) == 1)
                  && visited.Contains("singular") == both && visited.Contains("plural") == !both,
                "2b/S11: the loud page (both mates dead " + both + ") does not end in exactly one provenance flag.");
        }
        check(C(pLoud, "plural", 2).Check?.Skill == "CheckBluff" && C(pLoud, "plural", 2).Check!.DC == 15 && C(pLoud, "plural", 0).Alignment?.Direction == "Evil",
            "2b: the release is not Bluff DC 15, or the hanging is not Evil 1.");
        check(!N(pQuiet, "quiet").Text.Contains("bragged") && !N(pQuiet, "quiet").Text.Contains("whole Garrison"), "2b: the quiet page claims shouting.");

        // ---- Section 3: the citadel offer (S16). ----
        var cit = S(P + "citadel_offer");
        check(cit.AnswerLists.SequenceEqual(new[] { "41dff710486d05d49bbb663f729ddabd" }) && cit.NativeReturnCue == "7be28a1118c8af24ebf757789b9cfa4c"
              && cit.Chapters.SequenceEqual(new[] { 2 }) && cit.Requires.SequenceEqual(new[] { Begun }) && cit.Forbids.SequenceEqual(new[] { CitadelDone })
              && N(cit, "heard").Speaker == "conversant" && N(cit, "heard_blind").Speaker == "conversant",
            "3: the citadel offer is not inline on Minagho's list returning to Cue_0016, with her as the conversant.");
        foreach (var (flags, dc) in new[] { (new[] { Begun, Confirmed, Fed }, 14), (new[] { Begun, Confirmed }, 16), (new[] { Begun }, 20) })
        {
            var w = World(story, 2, flags);
            var shown = N(cit, "start").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, w)).ToList();
            check(shown.Count == 1 && shown[0].Check?.Skill == "CheckBluff" && shown[0].Check!.DC == dc && shown[0].Set.Contains(Witnessed) && shown[0].Set.Contains(CitadelDone),
                "S16: the citadel offer does not show exactly one twin at DC " + dc);
            var outs = Program.Walk(cit, w);
            check(outs.Count == 2 && outs.All(r => r.Has(Witnessed) && r.Has(CitadelDone))
                  && outs.Count(r => r.Has(OfferHeard)) == 1 && outs.Count(r => r.Has(Knew)) == (dc == 20 ? 0 : 1),
                "S16: the citadel outcomes (heard / heard_blind / lost) set the wrong flags at DC " + dc);
        }

        // ---- Nurah's big joke (S6). ----
        var joke = S(P + "big_joke");
        check(joke.ReturnToList && joke.AnswerLists.SequenceEqual(new[] { "2ce412d70ca0f40468252bec95ab2881" })
              && Avail(joke, World(story, 2, Begun, "nurah.asked_what_she_wants", "nurah.trickster_recruited"))
              && !Avail(joke, World(story, 2, Begun, "nurah.asked_what_she_wants")) && !Avail(joke, World(story, 2, Begun, "nurah.trickster_recruited"))
              && Program.Walk(joke, World(story, 2, Begun, "nurah.asked_what_she_wants", "nurah.trickster_recruited")).All(r => r.Has(P + "big_joke.seen") && !Avail(joke, r)),
            "S6: the big joke ignores the pact or the native answer, or plays twice.");

        // ---- Section 4a: Areelu's two masks and the courtesy twins (S7, S22). ----
        var masks = S("areelu.early.two_masks");
        check(masks.AnswerLists.SequenceEqual(new[] { "e47ef9ec640a1b4488ffb0c6a9983348" }) && masks.NativeReturnCue == "38bb928a4aa04e64ea2bd3b665d16985"
              && masks.EntryMythic == "TricksterUnlocked" && Avail(masks, World(story, 2, Begun)) && !Avail(masks, World(story, 2))
              && new[] { "yaniel.freed_answer", "yaniel.refused_0006", "yaniel.refused_0036" }.All(f => !Avail(masks, World(story, 2, Begun, f)))
              && Program.Walk(masks, World(story, 2, Begun)).All(r => r.Has(Mask)),
            "4a: two masks is not offered exactly before the prisoner's fate, or does not count the mask.");
        var freedTwin = S("areelu.early.courtesy_freed");
        var refusedTwin = S("areelu.early.courtesy_refused");
        check(new[] { freedTwin, refusedTwin }.All(s => s.ReturnToList && s.NativeReturnCue == null && s.AnswerLists.SequenceEqual(new[] { "4ab7a78f96a994446a56a9bc27ac2bfb" })
                  && s.Nodes.All(n => n.Speaker == "conversant")),
            "S22: the courtesy twins are not ReturnToList on her unmasked list with her as the conversant.");
        foreach (var (native, twin, other) in new[] { ("yaniel.freed_answer", freedTwin, refusedTwin), ("yaniel.refused_0006", refusedTwin, freedTwin),
                                                     ("yaniel.refused_0036", refusedTwin, freedTwin) })
        {
            var w = World(story, 2, Begun, Mask, native);
            check(Avail(twin, w) && !Avail(other, w) && !Avail(twin, World(story, 2, Begun, native)), "S7: the wrong courtesy twin for " + native);
            var outs = Program.Walk(twin, w);
            check(outs.Count == 2 && outs.All(r => r.Has(Courtesy) && new[] { Silent, Offered }.Count(r.Has) == 1 && !Avail(twin, r) && !Avail(other, r)),
                "S22: a courtesy path does not set read_* exactly once: " + native);
        }
        check(!Avail(refusedTwin, World(story, 2, Begun, Mask, "yaniel.refused_0006", "yaniel.freed_answer")), "S7: the refused twin plays after a free.");
        var lens = S("areelu.trickster.rivalry.lens");
        check(C(lens, "reply", 0).Next == "terms" && C(lens, "reply", 1).Next == "drezen_memory"
              && C(lens, "reply", 1).Requires.SequenceEqual(new[] { "trickster", Mask }),
            "4a: the lens memory is not appended at reply [1] behind trickster + mask_counted.");
        foreach (var (flags, node) in new[] { (new[] { Mask, Silent }, "drezen_silent"), (new[] { Mask, Offered }, "drezen_offered"), (new[] { Mask }, "drezen_counted") })
        {
            var visited = new HashSet<string>();
            Program.Walk(lens, World(story, 5, flags.Concat(new[] { "trickster", "areelu.met" }).ToArray()), (id, _) => visited.Add(id));
            check(visited.Contains(node) && new[] { "drezen_silent", "drezen_offered", "drezen_counted" }.Count(visited.Contains) == 1,
                "4a: the lens memory shows the wrong conclusion for " + string.Join(",", flags));
        }
        var noMask = new HashSet<string>();
        Program.Walk(lens, World(story, 5, "trickster", "areelu.met"), (id, _) => noMask.Add(id));
        check(!noMask.Contains("drezen_memory"), "4a: the lens memory plays without the crossing.");

        // ---- Section 5: the talk, hub or sergeant, never both (S5, S5b, S15, S21). ----
        var talk = S(P + "the_talk");
        var sgt = S(P + "the_talk_sergeant");
        var summons = S(P + "the_summons");
        var summonsWatch = S(P + "the_summons_watch");
        check(talk.AnswerLists.SequenceEqual(new[] { Hub }) && talk.ContactUnit == Irabeth && talk.Chapters.SequenceEqual(new[] { 3, 5 })
              && Rules.IsRemote(sgt) && sgt.Chapters.SequenceEqual(new[] { 3 }) && sgt.DelayHours == 72
              && summons.DelayHours == 96 && summonsWatch.DelayHours == 96 && summons.Chapters.SequenceEqual(new[] { 3, 5 }),
            "5.1: the talk's placements or windows differ from doc 15.");
        var absences = new[] { "irabeth_dead", "irabeth_gone", "irabeth_away" };
        foreach (var chapter in new[] { 3, 5 })
        {
            var present = World(story, chapter, Begun, Ch3);
            check(Avail(talk, present) && !Avail(sgt, present) && Avail(summons, present) && !Avail(summonsWatch, present),
                "S5: with Irabeth present the hub and her summons are not the only versions (Ch" + chapter + ").");
            foreach (var gone in absences)
            {
                var w = World(story, chapter, Begun, Ch3, gone);
                check(!Avail(talk, w) && Avail(sgt, w) == (chapter == 3) && Avail(summonsWatch, w) && !Avail(summons, w),
                    "S5: with " + gone + " the sergeant / Watch summons are not the only versions (Ch" + chapter + ").");
                var back = World(story, chapter, Begun, Ch3, gone, "irabeth.trickster.returned");
                check(Avail(talk, back) && !Avail(sgt, back) && Avail(summons, back) && !Avail(summonsWatch, back),
                    "S5b: a returned Irabeth does not get the hub version for " + gone);
            }
        }
        var early = World(story, 3, Begun, Ch3);
        early.Times[Ch3] = early.Hour - 95;
        check(!Avail(summons, early), "S18: the summons comes before 96 h in Chapter 3.");
        early.Times[Ch3] = early.Hour - 96;
        check(Avail(summons, early), "S18: the summons does not come at 96 h.");
        foreach (var (scene, irabethVoice) in new[] { (talk, true), (summons, true), (sgt, false), (summonsWatch, false) })
        {
            var start = irabethVoice ? World(story, 3, Begun, Ch3) : World(story, 3, Begun, Ch3, "irabeth_dead");
            var outs = Program.Walk(scene, start);
            check(outs.All(r => r.Has(TalkDone)) && outs.Count == 5, "S15: a talk path does not end in talk_done: " + scene.Id);
            var coin = Program.WalkVia(scene, start, "ask", 0).Single();
            var stand = Program.WalkVia(scene, start, "ask", 1).Single();
            var propose = Program.WalkVia(scene, start, "ask", 2).Single();
            var lie = Program.WalkVia(scene, start, "ask", 3);
            var lieOk = lie.Single(r => r.Has(Owed));
            var lieBad = lie.Single(r => !r.Has(Owed));
            string[] New(Snapshot r) => r.Flags.Except(start.Flags).Where(f => f != scene.Id && f != Confirmed).OrderBy(f => f, StringComparer.Ordinal).ToArray();
            string[] Sorted(params string[] f) => f.OrderBy(x => x, StringComparer.Ordinal).ToArray();
            if (irabethVoice)
                check(New(coin).SequenceEqual(Sorted(TalkDone, Wary)) && New(stand).SequenceEqual(Sorted(TalkDone, Stands, Wary))
                      && New(propose).SequenceEqual(Sorted(TalkDone, Proposed, Owed, ViaIrabeth)) && New(lieOk).SequenceEqual(Sorted(TalkDone, Lied, Owed, ViaIrabeth))
                      && New(lieBad).SequenceEqual(Sorted(TalkDone, Stands, Wary)),
                    "S15: an Irabeth-voice cell sets the wrong flags: " + scene.Id);
            else
                check(New(coin).SequenceEqual(Sorted(TalkDone, Minder)) && New(stand).SequenceEqual(Sorted(TalkDone, Stands, Minder))
                      && New(propose).SequenceEqual(Sorted(TalkDone, Proposed, Owed, ViaWatch)) && New(lieOk).SequenceEqual(Sorted(TalkDone, Deceived, Owed, ViaWatch))
                      && New(lieBad).SequenceEqual(Sorted(TalkDone, Stands, Minder)),
                    "S15: a Watch-voice cell sets the wrong flags: " + scene.Id);
            var ask = N(scene, "ask");
            check(ask.Choices[0].Crusade?.Resource == "Favors" && ask.Choices[0].Crusade!.Amount == -100 && ask.Choices[0].Forbids.Contains(Hanged)
                  && ask.Choices[3].Check?.Skill == "CheckBluff" && ask.Choices[3].Check!.DC == 20 && ask.Choices[3].Alignment?.Direction == "Chaotic",
                "S15: Coin (-100 Favors, not after a hanging) or the Lie (Bluff DC 20, Chaotic 1) differ: " + scene.Id);
            // S21: the hanging prelude, Coin absent, the voice's own flags in every branch.
            var hangedStart = irabethVoice ? World(story, 3, Begun, Ch3, Hanged, Seen, Confirmed) : World(story, 3, Begun, Ch3, "irabeth_dead", Hanged, Seen, Confirmed);
            var visited = new HashSet<string>();
            var hangedOuts = Program.Walk(scene, hangedStart, (id, _) => visited.Add(id));
            check(visited.Contains("hanging") && Program.WalkVia(scene, hangedStart, "ask", 0).Count == 0
                  && hangedOuts.All(r => r.Has(TalkDone) && (irabethVoice ? r.Has(Owned) && r.Has(Wary) && !r.Has(Minder) : r.Has(Noted) && r.Has(Minder) && !r.Has(Owned))),
                "S21: the hanging prelude, the absent Coin or the voice's hanging flags are wrong: " + scene.Id);
            // Section 5.2: the opening clauses. Each prisoner outcome gives its own clause; the skip case confirms the rumour.
            foreach (var (flags, clause) in new[] { (new[] { Clerk, Loud }, "clerk_plural"), (new[] { Clerk, Loud, BothKilled }, "clerk_singular"),
                                                    (new[] { Clerk, Quiet }, "clerk_quiet"), (new[] { Fed }, "fed"), (new[] { Killed }, "killed"),
                                                    (new[] { Witnessed }, "citadel"), (new string[0], "skip") })
            {
                var w = irabethVoice ? World(story, 3, flags.Concat(new[] { Begun, Ch3 }).ToArray()) : World(story, 3, flags.Concat(new[] { Begun, Ch3, "irabeth_dead" }).ToArray());
                var seen = new HashSet<string>();
                var o = Program.Walk(scene, w, (id, _) => seen.Add(id));
                var clauses = new[] { "clerk_plural", "clerk_singular", "clerk_quiet", "fed", "hanged", "killed", "citadel", "skip" };
                check(seen.Contains(clause) && clauses.Count(seen.Contains) == 1 && o.All(r => r.Has(Confirmed) == (clause == "skip" || w.Has(Confirmed))),
                    "S12/S13: the opening shows the wrong clause for " + string.Join(",", flags) + " on " + scene.Id);
            }
            var both = irabethVoice ? World(story, 3, Begun, Ch3, Clerk, Quiet, Witnessed) : World(story, 3, Begun, Ch3, Clerk, Quiet, Witnessed, "irabeth_dead");
            var seenBoth = new HashSet<string>();
            Program.Walk(scene, both, (id, _) => seenBoth.Add(id));
            check(seenBoth.Contains("clerk_quiet") && seenBoth.Contains("citadel") && !N(scene, "clerk_quiet").Text.Contains("shouting"),
                "S1/S15: the clerk and citadel clauses do not both show, or the quiet clerk claims shouting: " + scene.Id);
        }

        // ---- Section 5.2b: after the hanging; the inquiry. ----
        var after = S(P + "irabeth_after_hanging");
        var account = S(P + "hanging_account");
        var hangW = World(story, 3, Begun, Owned, TalkDone, Wary);
        hangW.Times[TalkDone] = hangW.Hour - 23;
        check(!Avail(after, hangW), "S5h: Irabeth's personal scene comes before 24 h.");
        hangW.Times[TalkDone] = hangW.Hour - 24;
        check(Avail(after, hangW) && !Avail(account, hangW) && Program.Walk(after, hangW).All(r => r.Has(AfterSeen) && Avail(account, r)),
            "S5h: the personal scene is not offered at 24 h, or does not open the inquiry.");
        var accOuts = Program.Walk(account, World(story, 3, Begun, Owned, TalkDone, AfterSeen));
        check(accOuts.Count == 2 && accOuts.Count(r => r.Has(Accounted)) == 1 && accOuts.All(r => r.Has(P + "hanging_account.seen") && !Avail(account, r))
              && C(account, "start", 1).Abort,
            "5.2b: the inquiry (submit / not now) does not end once, with the account only on submission.");

        // ---- Section 5.4: the enacted consequences (S14, S5, S1). ----
        var cold = S(P + "irabeth_cold");
        check(cold.Requires.SequenceEqual(new[] { Wary }) && cold.DelayHours == 72 && !cold.Forbids.Contains(TalkDone)
              && cold.ForbidOverrides.Count == 3 && Program.Walk(cold, World(story, 3, Wary)).All(r => r.Has(ColdSeen) && !Avail(cold, r)),
            "S1: irabeth_cold does not require exactly irabeth_wary, or plays twice.");
        var minder = S(P + "the_minder");
        var sting = S(P + "the_sting");
        var away = World(story, 3, Minder, Owed, ViaIrabeth);
        away.Area = "somewhere_else";
        check(minder.Areas.SequenceEqual(new[] { Drezen }) && sting.Areas.SequenceEqual(new[] { Drezen }) && !Avail(minder, away) && !Avail(sting, away)
              && Avail(minder, World(story, 3, Minder)) && Avail(sting, World(story, 3, Owed, ViaIrabeth)),
            "S5/S14: the minder or the sting plays outside Drezen.");
        var noted = new HashSet<string>();
        Program.Walk(minder, World(story, 3, Minder, Noted), (id, _) => noted.Add(id));
        check(noted.Contains("prisoners"), "5.2b: the minder does not carry the prisoners order after a hanging.");
        string[] SetOf(Snapshot r, Snapshot s0) => r.Flags.Except(s0.Flags).Where(f => f != sting.Id).OrderBy(f => f, StringComparer.Ordinal).ToArray();
        foreach (var (prov, lied) in new[] { (ViaIrabeth, false), (ViaIrabeth, true), (ViaWatch, false) })
        {
            var w = lied ? World(story, 3, Owed, prov, Lied) : World(story, 3, Owed, prov);
            var outs = Program.Walk(sting, w).Select(r => string.Join(",", SetOf(r, w))).OrderBy(x => x, StringComparer.Ordinal).ToList();
            var refuse = prov == ViaIrabeth ? string.Join(",", new[] { Refused, Wary }.OrderBy(x => x, StringComparer.Ordinal))
                                            : string.Join(",", new[] { Minder, Refused }.OrderBy(x => x, StringComparer.Ordinal));
            var expected = new[] {
                string.Join(",", new[] { StingDone, Exposed }.OrderBy(x => x, StringComparer.Ordinal)),
                string.Join(",", new[] { StingDone, Exposed, Scar }.OrderBy(x => x, StringComparer.Ordinal)),
                string.Join(",", new[] { StingDone, Exposed, AgentLost }.OrderBy(x => x, StringComparer.Ordinal)),
                string.Join(",", new[] { StingDone, Exposed, Scar, AgentLost }.OrderBy(x => x, StringComparer.Ordinal)),
                refuse }.OrderBy(x => x, StringComparer.Ordinal).ToList();
            check(outs.SequenceEqual(expected), "S14: the sting's exact sets differ for " + prov + (lied ? " (lied)" : "") + ": " + string.Join(" | ", outs));
        }
        check(C(sting, "start", 0).Check!.DC == 22 && C(sting, "start", 1).Check!.DC == 16, "S14: the sting DCs differ (close 22, back 16).");
        var off = S(P + "offpath_note");
        check(Avail(off, World(story, 3, Begun)) && !Avail(off, World(story, 3, Begun, "trickster")) && !Avail(off, World(story, 3, Begun, "trickster.was"))
              && !Avail(off, World(story, 4, Begun)) && off.Areas.SequenceEqual(new[] { Drezen }) && Program.Walk(off, World(story, 3, Begun)).All(r => r.Has(Offpath)),
            "S2: the off-path note plays on Trickster, in Ch4, or more than once.");

        // ---- S17: Minagho's Ch5 variant nodes on both deliveries (offer_heard + the live Trickster). ----
        foreach (var id in new[] { M + "spared.brand", M + "spared.brand_letter" })
        {
            var scene = S(id);
            foreach (var (flags, node, cellars) in new[] {
                (new[] { "trickster", "trickster.ever", "minagho.spared.latched", OfferHeard }, "longcon_run", false),
                (new[] { "trickster", "trickster.ever", "minagho.spared.latched", OfferHeard, M + "primed" }, "longcon_palm", false),
                (new[] { "trickster", "trickster.ever", "minagho.spared.latched", OfferHeard, Exposed }, "longcon_run", true),
                (new[] { "trickster.ever", "minagho.spared.latched", OfferHeard, M + "primed" }, null, false),
                (new[] { "trickster", "trickster.ever", "minagho.spared.latched" }, null, false) })
            {
                var w = World(story, 5, flags);
                var visited = new HashSet<string>();
                var outs = Program.Walk(scene, w, (n, _) => visited.Add(n));
                check((node == null ? !visited.Any(v => v.StartsWith("longcon_", StringComparison.Ordinal)) : visited.Contains(node))
                      && visited.Contains("longcon_cellars") == cellars && outs.Count > 0,
                    "S17: " + id + " shows the wrong opening for " + string.Join(",", flags));
            }
            check(N(scene, "start").Choices.Count >= 4, "S17: the Minagho variant moved an existing choice: " + id);
        }

        // ---- The Ledger (section 5.4; prospective and retrospective lines). ----
        var page = story.Books["trickster.ledger"].Entries.Single(e => e.Id == "early.longcon");
        check(page.Section == "Secrets" && page.Requires.SequenceEqual(new[] { "trickster.secret.longcon" })
              && World(story, 5, Begun, "trickster").Has("trickster.secret.longcon") && !World(story, 5, Begun).Has("trickster.secret.longcon"),
            "Ledger: the Long Con page is not a Secrets page on a Trickster run that began the con.");
        bool Has(string text, params string[] f) { var s = new Snapshot(); s.Flags.UnionWith(f); return page.Lines.Any(l => Shown(l, s) && l.Text.Contains(text)); }
        check(Has("never answered for", Begun) && !Has("never answered for", Begun, TalkDone)
              && Has("still owe the Watch", Owed) && !Has("still owe the Watch", Owed, StingDone)
              && Has("Everyone came home", StingDone) && !Has("Everyone came home", StingDone, AgentLost) && Has("didn't come home", StingDone, AgentLost)
              && Has("posted a guard", Minder) && !Has("posted a guard", Minder, MinderSeen) && Has("slept across", MinderSeen)
              && Has("She believed you", Lied) && !Has("She believed you", Lied, Wary)
              && Has("never answered for it", Owned) && Has("answered for it, in front", Owned, Accounted) && !Has("never answered for it", Owned, Accounted),
            "S18/S19: a Ledger line is not prospective before, retrospective after.");

        // ---- Section 8: the reader lint (exhaustive permitted readers). ----
        var permitted = new Dictionary<string, string[]> {
            [OfferHeard] = new string[0],
            [Exposed] = new[] { M + "spared.brand", M + "spared.brand_letter" },
            [Owned] = new[] { P + "irabeth_after_hanging", P + "irabeth_after_hanging_letter", P + "hanging_account" },
            [Accounted] = new[] { P + "hanging_account" },
            [Mask] = new[] { "areelu.trickster.rivalry.lens", "areelu.early.two_masks", "areelu.early.courtesy_freed", "areelu.early.courtesy_refused" },
            [Silent] = new[] { "areelu.trickster.rivalry.lens" }, [Offered] = new[] { "areelu.trickster.rivalry.lens" },
            [Lied] = new[] { P + "the_sting" }, [Wary] = new[] { P + "irabeth_cold" },
            ["longcon.minagho_reads"] = new[] { M + "spared.brand", M + "spared.brand_letter" } };
        foreach (var pair in permitted)
            foreach (var s in story.Scenes.Where(s => Reads(s).Contains(pair.Key)))
                check(pair.Value.Contains(s.Id), "Reader lint: " + s.Id + " reads " + pair.Key);
        foreach (var s in story.Scenes.Where(s => !ours.Contains(s)))
            foreach (var key in Reads(s).Where(k => k.StartsWith(P, StringComparison.Ordinal)))
                check(key == "longcon.minagho_reads" || key == Exposed && permitted[Exposed].Contains(s.Id),
                    "Reader lint: a scene outside the Long Con reads " + key + ": " + s.Id);
        var derived = story.Derived["longcon.minagho_reads"];
        check(derived.Length == 1 && derived[0].OrderBy(x => x, StringComparer.Ordinal).SequenceEqual(new[] { OfferHeard, "trickster" }),
            "S17: Minagho's read is not offer_heard + the current Trickster.");

        // Coexistence: no Long Con scene reads a partner's committed, closed or harem state, and none closes a route.
        foreach (var s in ours)
            check(!Reads(s).Any(f => f.EndsWith(".committed", StringComparison.Ordinal) || f.EndsWith(".closed", StringComparison.Ordinal) || f.Contains(".harem."))
                  && !s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => story.Relationships.Values.Any(r => r.ClosedFlag == f)))),
                "Coexistence: a Long Con scene reads or sets a partner state: " + s.Id);
        Console.WriteLine("PASS: the Long Con (doc 15): entry twins, prisoner pages, citadel twins, Areelu crossing, the talk in both voices, consequences, Minagho's variant, Ledger and readers.");
    }
}
