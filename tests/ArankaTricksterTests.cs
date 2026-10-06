using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Aranka, Trickster (Writer/handoffs/trickster/aranka.md): the boast made true (F05) in the Fool King's tavern, the verse
// where the Commander loses (parent-mod failure) and the court poet billed before she was asked (parent romance done).
// One block per spec rules test (Trk_Aranka_*), plus hooks, the presences, the yard copies for a Fye-less capital, the night, epilogues and
// reactions.
internal static class ArankaTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Unit = "430cba7801b149b4e8494ace6baf4f7c";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string Market = "bad9f602b81a80047ac470b01ebe65a9"; // ExoticCapitalTrader (polish 2026-09-28: off Fye's counter)
    private const string YardUnit = "bd0c4fe722aeef94b8495ac284b96bc8";
    private const string Quartermaster = "15f754455d1d87c42a4e14df456d5415"; // F9 ordinary capital smith
    private const string FyeGone = "aranka.presence.failed";
    private const string KingC3 = "1a17d8053a3be7f47a7908eb6706f2fe";
    private const string KingC3Return = "814dd1a078a1c2849aefc85e2e15b2d2";
    private const string KingC5 = "6dccfd39947ef4242a8afbe36b21a46c";
    private const string KingC5Return = "7b050ba0745bf144e815632e39b34853";
    private const string P = "aranka.trickster.";
    private const string Kept = "aranka.extension_kept";
    private const string Closed = "aranka.extension_closed";

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
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        if (chapter == 3 || chapter == 5) state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    // Polish (item 6): a Chapter 5 snapshot of native facts only: no Aranka contact, no presence observation, no route flag.
    private static Snapshot Native(Story story, int chapter, params string[] flags)
    {
        // eng-final: native facts do not imply an empty crusade treasury.
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000 } };
        state.Flags.UnionWith(flags);
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.Flags.Add("chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    // An ending snapshot (Chapter 6) of a played state, for the epilogue pages (R2-6).
    private static Snapshot Ending(Story story, Snapshot state)
    {
        var end = Program.Copy(state);
        end.Chapter = 6;
        end.Flags.ExceptWith(story.Derived.Keys);
        Rules.Complete(story, end);
        return end;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        later.Flags.ExceptWith(story.Derived.Keys);
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var tavern = S(P + "verse.kings_tavern");
        var tavern5 = S(P + "verse.kings_tavern_c5");
        var anyTavern = S(P + "verse.any_tavern");
        var herLetter = S(P + "verse.her_letter");
        var duet = S(P + "verse.duet");
        var encore = S(P + "verse.encore");
        var third = S(P + "verse.third_verse");
        var mocking = S(P + "failure.mocking_verse");
        var mockingAny = S(P + "failure.mocking_verse_any");
        var mocking5 = S(P + "failure.mocking_verse_c5");
        var secondVerse = S(P + "failure.second_verse");
        var boast = S(P + "touring.boast");
        var arrives = S(P + "touring.arrives");
        var epCommit = S(P + "epilogue.commit");
        var epDeclined = S(P + "epilogue.declined");
        var epVerse = S(P + "epilogue.verse");
        var epNerosyan = S(P + "epilogue.nerosyan");
        // Polish (item 2): the Chapter 3 beats close at Chapter 3; their Chapter 5 twins run on a 24-hour clock.
        Scene L(Scene s) => S(s.Id + "_late");
        var herLetterL = L(herLetter);
        var duetL = L(duet);
        var encoreL = L(encore);
        var thirdL = L(third);
        var secondVerseL = L(secondVerse);
        var arrivesL = L(arrives);
        var reckoning = S(P + "failure.reckoning");
        var reckoningYard = S(P + "failure.reckoning_yard");
        const string Repaired = P + "moral_repaired";
        var setups = new[] { tavern, tavern5, anyTavern, mocking, mocking5, mockingAny, boast };
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w);
        Snapshot After(Scene scene, Snapshot w, string node, int choice)
        {
            var target = scene.Nodes.Single(n => n.Id == node).Choices[choice];
            var hit = Program.Walk(scene, w).FirstOrDefault(o => target.Set.All(o.Has));
            check(hit != null && target.Set.Length > 0, "No outcome through " + scene.Id + "/" + node + "/" + choice);
            return hit ?? w;
        }
        bool Reaches(Snapshot w, string flag, int depth = 6)
        {
            if (w.Has(flag)) return true;
            if (depth == 0) return false;
            var later = Later(story, w, 100);
            foreach (var s in story.Scenes.Where(s => s.Relationship == "aranka" && !s.Reaction
                                                   && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                                                   && Rules.Available(story, s, later)))
                foreach (var outcome in Play(s, later))
                    if (Reaches(outcome, flag, depth - 1)) return true;
            return false;
        }

        // Hooks, relationship patch and the presence.
        check(tavern.AnswerLists.SequenceEqual(new[] { KingC3 }) && tavern.NativeReturnCue == KingC3Return
              && tavern.MinChapter == 3 && tavern.MaxChapter == 3
              && tavern5.AnswerLists.SequenceEqual(new[] { KingC5 }) && tavern5.NativeReturnCue == KingC5Return
              && tavern5.MinChapter == 5 && tavern5.Requires.Contains("fool_king.crowned") && tavern5.Forbids.Contains("fool_king.gone")
              && mocking.AnswerLists.SequenceEqual(new[] { KingC3 }) && mocking.NativeReturnCue == KingC3Return,
            "The King's tavern hooks moved.");
        foreach (var s in new[] { tavern, tavern5, mocking })
            check(s.Nodes.Where(n => n.Speaker != "Narrator").All(n => n.Speaker == "conversant"),
                "An inline tavern node would borrow the King's voice for Aranka: " + s.Id);
        foreach (var s in new[] { duet, encore, third, arrives })
            check(s.InteractionHub == "aranka.presence" && s.ContactUnit == Unit && Rules.IsPresenceHubScene(s)
                  && s.Chapters.SequenceEqual(new[] { 3 }) && s.MinChapter == 3 && s.MaxChapter == 3
                  && L(s).InteractionHub == "aranka.presence" && L(s).ContactUnit == Unit && Rules.IsPresenceHubScene(L(s)),
                "An in-person beat left her place in the market: " + s.Id);
        // Polish (item 2): every Chapter 5 twin is a deep copy on a 24-hour clock that never replays its original.
        foreach (var s in new[] { herLetter, duet, S(duet.Id + "_yard"), encore, S(encore.Id + "_yard"), third, S(third.Id + "_yard"),
                                  secondVerse, arrives, S(arrives.Id + "_yard") })
        {
            var t = L(s);
            check(s.Chapters.SequenceEqual(new[] { 3 }) && s.MinChapter == 3 && s.MaxChapter == 3
                  && t.Chapters.SequenceEqual(new[] { 5 }) && t.MinChapter == 5 && t.MaxChapter == 5 && t.DelayHours == 24
                  && t.Relationship == s.Relationship && t.Requires.SequenceEqual(s.Requires)
                  && t.Forbids.SequenceEqual(s.Forbids.Append(s.Id)) && t.TricksterDevice == s.TricksterDevice
                  && t.TricksterState == s.TricksterState && t.InteractionHub == s.InteractionHub && t.ContactUnit == s.ContactUnit
                  && t.Remote == s.Remote && t.Nodes.Select(n => n.Id).SequenceEqual(s.Nodes.Select(n => n.Id))
                  && t.Nodes.SelectMany(n => n.Choices).Select(c => c.Text + "|" + c.Next + "|" + string.Join(",", c.Set))
                      .SequenceEqual(s.Nodes.SelectMany(n => n.Choices).Select(c => c.Text + "|" + c.Next + "|" + string.Join(",", c.Set)))
                  && !ReferenceEquals(t.Nodes[0], s.Nodes[0]) && !t.Nodes.Any(n => n.Text.Contains('@')),
                "A Chapter 5 twin drifted from its Chapter 3 beat: " + t.Id);
            check(story.Scenes.Count(x => x.Id == t.Id) == 1, "A Chapter 5 twin is duplicated: " + t.Id);
        }
        check(!encoreL.Nodes.Single(n => n.Id == "offer").Text.Contains("these last few nights")
              && !arrivesL.Nodes[0].Text.Contains("two days") && !S(arrives.Id + "_yard_late").Nodes[0].Text.Contains("market")
              && herLetterL.Nodes.Where(n => n.Id == "known" || n.Id == "unknown").All(n => n.Text.Contains("first ford")),
            "A Chapter 5 twin keeps a journey that a day cannot carry.");
        foreach (var s in new[] { anyTavern, herLetter, mockingAny, secondVerse, boast, herLetterL, secondVerseL })
            check(Rules.IsRemote(s), "A letter is physical: " + s.Id);
        check(!story.Scenes.Any(s => s.Id == P + "verse.her_letter_twin"), "The retired letter twin came back.");
        foreach (var s in new[] { duet, encore, third, arrives })
        {
            var y = S(s.Id + "_yard");
            check(y.InteractionHub == "aranka.presence.yard" && y.ContactUnit == YardUnit && Rules.IsPresenceHubScene(y)
                  && y.Requires.Contains(FyeGone) && y.Requires.Except(new[] { FyeGone }).SequenceEqual(s.Requires)
                  && y.Forbids.SequenceEqual(s.Forbids) && y.DelayHours == s.DelayHours && y.Chapters.SequenceEqual(s.Chapters)
                  && y.Nodes.Select(n => n.Id).SequenceEqual(s.Nodes.Select(n => n.Id))
                  && y.Nodes.SelectMany(n => n.Choices).Select(c => string.Join(",", c.Set)).SequenceEqual(s.Nodes.SelectMany(n => n.Choices).Select(c => string.Join(",", c.Set)))
                  && !y.Nodes.Any(n => n.Text.Contains("spice trader") || n.Text.Contains("above the market") || n.Text.Contains('@')),
                "The yard copy drifted from its counter scene: " + y.Id);
        }
        var rel = story.Relationships["aranka"];
        check(rel.UnavailableOverrides["aranka.ran_failure"] == Repaired && rel.TricksterAccess.Count == 3
              && rel.TricksterAccess["aranka.ran_failure"].Returned == Repaired
              && rel.TricksterAccess["aranka.ran_failure"].Detect.SequenceEqual(new[] { "aranka.ran_failure" })
              && rel.CommittedFlag == Kept && rel.ClosedFlag == Closed, "Aranka's relationship patch is wrong.");
        foreach (var s in new[] { mocking, mocking5, mockingAny, secondVerse, secondVerseL, reckoning, reckoningYard })
            check(s.TricksterDevice && s.TricksterState == "aranka.ran_failure", "A failure-state scene is not an ER-2 device: " + s.Id);
        check(story.Presences.TryGetValue("aranka.presence", out var presence) && presence.Unit == Unit && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == Market && presence.Dialog == "hub" && presence.Forbids.Contains(Closed)
              && presence.MinChapter == 3 && presence.MaxChapter == 5 && presence.Requires.Contains("aranka.trickster.in_drezen"),
            "Her presence in the market is missing or malformed.");
        presence = story.Presences["aranka.presence"];
        check(story.Presences.TryGetValue("aranka.presence.yard", out var yard) && yard.Unit == YardUnit && yard.Unit != presence.Unit
              && yard.At?.NearUnit == Quartermaster && yard.At.Offset != null && yard.At.Offset[0] == 5f && yard.At.Offset[1] == -7f && yard.Dialog == "hub" && yard.Requires.Contains(FyeGone)
              && yard.Forbids.Contains(Closed) && yard.MinChapter == 3 && yard.MaxChapter == 5,
            "The yard presence for a Fye-less capital is missing or malformed.");
        yard = story.Presences["aranka.presence.yard"];
        // 11-ROSTER-PLAN-2 §2 (Nenio's build sheet): a second copy may stand at the stall on the far side (behind, 5 m away).
        check(!story.Presences.Any(p => p.Key != "aranka.presence" && p.Value.At?.NearUnit == Market && p.Value.At?.Side == presence.At?.Side),
            "Another presence shares Aranka's side of the market stall.");
        check(!story.Presences.Any(p => p.Key == "aranka.presence" && p.Value.At?.NearUnit == Fye),
            "Aranka is back on Fye's crowded counter.");

        // Trk_Aranka_NeverEntered: the King's round; her letter three days on.
        var fresh = World(story, 3, "trickster", "trickster.ever");
        check(Rules.Available(story, tavern, fresh) && !Rules.Available(story, mocking, fresh) && !Rules.Available(story, boast, fresh)
              && !Rules.Available(story, anyTavern, fresh), "Trk_Aranka_NeverEntered: availability.");
        var joke = tavern.Nodes.Single(n => n.Id == "known").Choices[0];
        check(joke.Mythic == "PlayerIsTrickster" && joke.Crusade?.Resource == "Finances" && joke.Crusade.Amount == -100
              && joke.Text.StartsWith("[Follow your instincts]", StringComparison.Ordinal), "The King's round lost its joke or its cost.");
        var sung = After(tavern, fresh, "uncrowned", 0);
        check(sung.Has(P + "primed") && sung.Has(P + "cost.round_bought"), "Trk_Aranka_NeverEntered: flags.");
        check(!Rules.Available(story, herLetter, Later(story, sung, 71)) && Rules.Available(story, herLetter, Later(story, sung, 72)),
            "Trk_Aranka_NeverEntered: her letter ignores its three days.");
        check(Reaches(sung, Kept), "Trk_Aranka_NeverEntered: the commit is unreachable.");
        var crownedPages = new HashSet<string>();
        var crowned = World(story, 3, "trickster", "trickster.ever", "fool_king.crowned");
        Program.Walk(tavern, crowned, (page, _) => crownedPages.Add(page));
        check(crownedPages.Contains("crowned") && !crownedPages.Contains("uncrowned"), "The King weeps into a crown he has not got yet.");
        var met = World(story, 3, "trickster", "trickster.ever", "aranka.gave_song");
        var metPages = new HashSet<string>();
        Program.Walk(tavern, met, (page, _) => metPages.Add(page));
        check(metPages.Contains("known") && !metPages.Contains("unknown"), "The Kenabres gift is not remembered.");
        check(metPages.Contains("sheet") && metPages.Contains("pilgrim") && !metPages.Contains("stone"),
            "The rewrite is not shown on the King's song-sheet, or nobody in the room refuses it.");
        var tablet = World(story, 3, "trickster", "trickster.ever", "fool_king.tablet_true");
        var tabletPages = new HashSet<string>();
        Program.Walk(tavern, tablet, (page, _) => tabletPages.Add(page));
        check(tabletPages.Contains("stone"), "The song-sheet does not recall the stone from Pulura's Fall.");

        // Chapter 5: the crowned King's hub, and not once he is gone.
        var c5 = World(story, 5, "trickster", "trickster.ever", "fool_king.crowned");
        check(Rules.Available(story, tavern5, c5) && !Rules.Available(story, tavern, c5), "The Chapter 5 King's round is missing.");
        var gone = World(story, 5, "trickster", "trickster.ever", "fool_king.crowned", "fool_king.gone");
        check(!Rules.Available(story, tavern5, gone), "The King's round outlives the King.");
        // Audit round 5 (INT/COX): after the Coronation, a crowned King who is still here keeps the only entry; the
        // fallback ("There is no King left to sing to") opens only when he is gone, or was never crowned.
        var crownedAfter = World(story, 5, "trickster", "trickster.ever", "fool_king.crowned", "coronation.after");
        check(Rules.Available(story, tavern5, crownedAfter) && !Rules.Available(story, anyTavern, crownedAfter),
            "The no-King fallback opens beside a living, crowned King.");
        var neverCrowned = World(story, 5, "trickster", "trickster.ever", "coronation.after");
        check(Rules.Available(story, anyTavern, neverCrowned) && !Rules.Available(story, tavern5, neverCrowned),
            "A Commander whose King was never crowned has no Chapter 5 entry.");
        var failedCrowned = World(story, 5, "trickster", "trickster.ever", "aranka.ran_failure", "fool_king.crowned", "coronation.after");
        check(Rules.Available(story, mocking5, failedCrowned) && !Rules.Available(story, mockingAny, failedCrowned),
            "The failure state in Chapter 5 has no entry beside a crowned King, or two.");
        check(mocking5.AnswerLists.SequenceEqual(new[] { KingC5 }) && mocking5.NativeReturnCue == KingC5Return,
            "The Chapter 5 failure verse left the King's list.");

        // Trk_Aranka_NoKing: the late fallback, dearer, with her reply folded in.
        check(Rules.Available(story, anyTavern, gone) && anyTavern.Nodes[0].Choices[0].Crusade?.Amount == -150
              && anyTavern.Nodes[0].Choices[0].Mythic == "PlayerIsTrickster", "Trk_Aranka_NoKing: the fallback is missing or cheap.");
        var late = After(anyTavern, gone, "reply_unknown", 0);
        check(late.Has(P + "primed") && late.Has(P + "cost.late") && late.Has(P + "answered"), "Trk_Aranka_NoKing: flags.");
        check(!Rules.Available(story, herLetter, Later(story, late, 100)) && !Rules.Available(story, herLetterL, Later(story, late, 100))
              && !Rules.Available(story, duetL, Later(story, late, 23)) && Rules.Available(story, duetL, Later(story, late, 24))
              && !Rules.Available(story, duet, Later(story, late, 72)),
            "Trk_Aranka_NoKing: a second letter follows the fallback, or the Chapter 5 duet does not follow a day later.");
        check(!Rules.Available(story, anyTavern, World(story, 3, "trickster", "trickster.ever")),
            "The fallback opens while the King is still singing.");
        // Audit pol2 (BEL/INT, R2-2): the fallbacks stage the opportunity only; the paid act is narrated after its answer,
        // and walking away costs and records nothing.
        foreach (var fallback in new[] { anyTavern, mockingAny })
        {
            var leave = fallback.Nodes[0].Choices[1];
            check(fallback.Nodes[0].Choices.Count == 2 && leave.Abort && leave.Crusade == null && leave.Set.Length == 0
                  && !fallback.Nodes[0].Text.Contains("every mug") && fallback.Nodes.Single(n => n.Id == "reply").Text.Contains("every mug"),
                "A fallback narrates the paid act before the Commander chooses it: " + fallback.Id);
        }
        var herLetterSet = herLetter.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).ToHashSet();
        check(!herLetterSet.Contains(P + "cost.late") && !herLetterSet.Contains(P + "primed"), "Her ordinary letter records the late cost.");

        // Trk_Aranka_Duet: the billing, both ways; every opening variant is exclusive.
        var answered = World(story, 3, "trickster", "trickster.ever", P + "answered", "aranka.extension_started", P + "cost.credited");
        check(Rules.Available(story, duet, answered), "Trk_Aranka_Duet: unavailable.");
        var signed = After(duet, answered, "signed", 0);
        check(signed.Has(P + "duet_sung") && Play(duet, answered).Any(r => r.Has(P + "cost.vain")), "Trk_Aranka_Duet: flags.");
        check(!Rules.Available(story, encore, Later(story, signed, 71)) && Rules.Available(story, encore, Later(story, signed, 72)),
            "Trk_Aranka_Duet: the encore ignores its three days.");
        foreach (var variant in new[] { P + "cost.denied", P + "cost.mocking_verse", P + "cost.announced" })
        {
            var w = Program.Copy(answered); w.Flags.Add(variant);
            var pages = new HashSet<string>();
            Program.Walk(duet, w, (page, _) => pages.Add(page));
            check(new[] { "vandal", "denied", "mocking", "posters" }.Count(pages.Contains) == 1, "Two duet openings play at once: " + variant);
        }

        // Audit pol3 (VOI): the bard who won the Count's contest (DesnaAdept2/Cue_15) duets as a rival, never as a pupil.
        foreach (var opening in new[] { (string?)null, P + "cost.denied", P + "cost.mocking_verse", P + "cost.announced" })
        {
            var w = Program.Copy(answered); w.Flags.Add("aranka.kenabres_contest_won");
            if (opening != null) w.Flags.Add(opening);
            var pages = new HashSet<string>();
            var outs = Program.Walk(duet, w, (page, _) => pages.Add(page));
            check(pages.Contains("duet_rival") && !pages.Contains("duet") && outs.Any(r => r.Has(P + "duet_sung")),
                "The contest winner is taught to sing: " + (opening ?? "vandal"));
        }
        var plainPages = new HashSet<string>();
        Program.Walk(duet, answered, (page, _) => plainPages.Add(page));
        check(plainPages.Contains("duet") && !plainPages.Contains("duet_rival"), "The rivals' duet plays without the won contest.");

        // Trk_Aranka_Commit / Declined / Nerosyan, and the night after the yes.
        var ready = World(story, 5, "trickster", "trickster.ever", P + "duet_sung", "aranka.extension_started", P + "answered");
        check(Rules.Available(story, encoreL, ready) && !Rules.Available(story, encore, ready), "Trk_Aranka_Commit: the encore is unavailable.");
        var stay = encore.Nodes.Single(n => n.Id == "choice").Choices[0];
        check(stay.Set.SequenceEqual(new[] { Kept }) && encoreL.Nodes.Single(n => n.Id == "choice").Choices[0].Set.SequenceEqual(new[] { Kept }),
            "The named producer is not encore/choice/0.");
        var encorePages = new HashSet<string>();
        var outcomes = Program.Walk(encoreL, ready, (page, _) => encorePages.Add(page));
        var committed = outcomes.First(r => r.Has(Kept));
        check(encorePages.Contains("threshold") && encorePages.Contains("morning") && committed.Has(P + "night_kept"),
            "Trk_Aranka_Commit: the yes has no night.");
        var declined = After(encoreL, ready, "not_yet", 0);
        check(declined.Has(P + "declined") && !declined.Has(Kept), "Trk_Aranka_Declined: her soft no.");
        check(!Rules.Available(story, thirdL, Later(story, declined, 23)) && Rules.Available(story, thirdL, Later(story, declined, 24))
              && !Rules.Available(story, encoreL, Later(story, declined, 24)),
            "Trk_Aranka_Declined: the third verse does not replace the encore.");
        var thirdOut = Play(thirdL, Later(story, declined, 24));
        check(thirdOut.Any(r => r.Has(Kept) && r.Has(P + "cost.sang_alone") && r.Has(P + "night_kept"))
              && thirdOut.Any(r => r.Has(Closed) && !r.Has(Kept)), "Trk_Aranka_Declined: her proposal verse, or the rhyme left hanging, is missing.");
        var sungAlone = third.Nodes[0].Choices[0];
        // Polish 2026-09-28: the answer's cost is personal (singing alone, badly, in public), never a crusade fee.
        check(sungAlone.Crusade == null && sungAlone.Set.Contains(P + "cost.sang_alone"), "Finishing her verse is a crusade fee, not a personal cost.");
        check(!third.Nodes.SelectMany(n => n.Choices).Any(c => c.Text.Contains("[Sign") || c.Text.Contains("terms")) && !third.Nodes.Any(n => n.Text.Contains("sign it")),
            "The third verse went back to a priced, signed ask.");
        var released = outcomes.First(r => r.Has(P + "gone_to_nerosyan"));
        check(released.Has(Closed) && !released.Has(Kept) && !Rules.Available(story, duetL, Later(story, released, 500))
              && !Rules.Available(story, thirdL, Later(story, released, 500)), "The Nerosyan stage is not a kind ending.");

        // Trk_Aranka_ParentFailure: the verse where the Commander loses, an ER-2 device; the letter, then the duet.
        var failed = World(story, 3, "trickster", "trickster.ever", "aranka.ran_failure");
        check(Rules.Available(story, mocking, failed) && !Rules.Available(story, tavern, failed) && !Rules.Available(story, anyTavern, failed),
            "Trk_Aranka_ParentFailure: availability.");
        var led = After(mocking, failed, "after", 0);
        check(led.Has(P + "primed") && led.Has(P + "cost.mocking_verse"), "Trk_Aranka_ParentFailure: flags.");
        check(Rules.Available(story, secondVerse, Later(story, led, 72)), "Trk_Aranka_ParentFailure: her letter is missing.");
        var invited = After(secondVerse, Later(story, led, 72), "start", 0);
        // Coordinator ruling 2026-10-02 (item 1): the song only brings her to Drezen; her moral objection is answered in person.
        check(invited.Has(P + "returned") && invited.Has(P + "answered") && !invited.Has(Repaired)
              && !Rules.Available(story, duet, Later(story, invited, 72)) && Rules.Available(story, reckoning, invited)
              && !Rules.Available(story, secondVerse, Later(story, invited, 72)) && !Rules.Available(story, secondVerseL, Later(story, invited, 72)),
            "Trk_Aranka_ParentFailure: the song alone lifts the failure, or the reckoning is missing.");
        var buy = reckoning.Nodes[0].Choices[0];
        check(buy.Crusade?.Resource == "Finances" && buy.Crusade.Amount == -200 && buy.Next == "bought"
              && reckoning.Nodes.Single(n => n.Id == "bought").Choices[0].Set.SequenceEqual(new[] { P + "returned", Repaired, P + "cost.provisions_bought" })
              && reckoning.Nodes.Single(n => n.Id == "unchanged").Choices[0].Set.SequenceEqual(new[] { Closed }) && reckoning.Nodes[0].Choices[2].Abort,
            "The reckoning lost its price, its repair or its refusal.");
        var forgiven = After(reckoning, invited, "bought", 0);
        check(forgiven.Has(Repaired) && Rules.Available(story, duet, Later(story, forgiven, 72)) && Reaches(forgiven, Kept)
              && !Rules.Available(story, reckoning, forgiven), "Trk_Aranka_ParentFailure: the reckoning does not lift the failure.");
        var unchanged = After(reckoning, invited, "unchanged", 0);
        check(unchanged.Has(Closed) && !Rules.Available(story, duet, Later(story, unchanged, 500)) && !Reaches(unchanged, Kept),
            "An unchanged justification does not close her route.");
        var deferred = Play(reckoning, invited).First(r => !r.Has(Repaired) && !r.Has(Closed));
        check(Rules.Available(story, reckoning, Later(story, deferred, 24)), "Deferring the reckoning closes it.");
        // Old saves (approved policy): the legacy returned flag, alone or with an earned yes, waits for the reckoning.
        foreach (var legacy in new[] { new[] { P + "returned" }, new[] { P + "returned", Kept, P + "duet_sung" } })
        {
            var old = World(story, 3, new[] { "trickster", "trickster.ever", "aranka.ran_failure", P + "primed", P + "cost.mocking_verse",
                P + "answered", "aranka.extension_started" }.Concat(legacy).ToArray());
            check(Rules.Available(story, reckoning, old) && !Rules.Available(story, duet, old) && !Rules.Available(story, encore, old)
                  && !Rules.Available(story, epVerse, Ending(story, old)) && !Rules.Available(story, epCommit, Ending(story, old)),
                "A legacy returned save resumes courtship without the reckoning: " + string.Join("+", legacy));
            var mended = After(reckoning, old, "bought", 0);
            check(legacy.Contains(Kept) ? Rules.Available(story, epVerse, Ending(story, mended)) : Rules.Available(story, duet, Later(story, mended, 72)),
                "The reckoning does not restore a legacy save: " + string.Join("+", legacy));
        }
        var failedLate = World(story, 5, "trickster", "trickster.ever", "aranka.ran_failure", "coronation.after");
        check(Rules.Available(story, mockingAny, failedLate) && mockingAny.Nodes[0].Choices[0].Crusade?.Amount == -150,
            "The failure fallback is missing after the Coronation.");

        // Trk_Aranka_ParentDone: the posters; she arrives furious; the duet on the same counter.
        var done = World(story, 5, "trickster", "trickster.ever", "aranka.ran_romance", "aranka.ran_quest_complete");
        check(Rules.Available(story, boast, done) && !Rules.Available(story, tavern5, done) && !Rules.Available(story, anyTavern, done),
            "Trk_Aranka_ParentDone: availability.");
        var billed = After(boast, done, "posters", 0);
        check(billed.Has(P + "primed") && billed.Has(P + "cost.announced") && boast.Nodes[0].Choices[0].Crusade?.Amount == -100,
            "Trk_Aranka_ParentDone: flags or cost.");
        check(!Rules.Available(story, arrivesL, Later(story, billed, 23)) && Rules.Available(story, arrivesL, Later(story, billed, 24))
              && !Rules.Available(story, arrives, Later(story, billed, 48)),
            "Trk_Aranka_ParentDone: the arrival ignores its hours.");
        var arrived = Play(arrivesL, Later(story, billed, 24)).First();
        check(arrived.Has(P + "answered") && Rules.Available(story, duetL, Later(story, arrived, 24)) && Reaches(arrived, Kept),
            "Trk_Aranka_ParentDone: the arrival does not lead to the duet.");
        check(!Rules.Available(story, boast, World(story, 5, "trickster", "trickster.ever", "aranka.ran_romance", "aranka.ran_quest_complete", "azata")),
            "The posters go up on an Azata run.");

        // Every setup excludes the others in each world (COX).
        foreach (var w in new[] { fresh, c5, gone, failed, failedLate, done, crownedAfter, neverCrowned, failedCrowned })
            check(setups.Count(s => Rules.Available(story, s, w)) <= 1, "Two Aranka setups open at once.");

        // Fye has left the capital (Chapter 3 or 5): every in-person beat plays in the quartermaster's yard instead, through
        // the commit, her soft no, the priced second ask and the stage (audit round 3, INT/HOW).
        Snapshot Yard(int chapter, params string[] flags)
        {
            var w = World(story, chapter, flags.Concat(new[] { FyeGone }).ToArray());
            w.AvailableContacts.Remove(Unit); w.AvailableContacts.Add(YardUnit);
            return w;
        }
        foreach (var chapter in new[] { 3, 5 })
        {
            Scene Y(Scene s) => S(s.Id + "_yard" + (chapter == 5 ? "_late" : ""));
            Scene M(Scene s) => chapter == 5 ? L(s) : s;
            int day = chapter == 5 ? 24 : 72, posted = chapter == 5 ? 24 : 48;
            // eng7-l13: the positive encore creates a new Trickster commitment.
            var yAnswered = Yard(chapter, "trickster", "trickster.ever", P + "answered", "aranka.extension_started", P + "cost.credited");
            check(Rules.Available(story, Y(duet), yAnswered) && !Rules.Available(story, M(duet), yAnswered),
                "Fye-less duet: the yard copy is missing, or the counter scene still opens (chapter " + chapter + ").");
            var ySung = Play(Y(duet), yAnswered).First(r => r.Has(P + "duet_sung"));
            var yEncore = Later(story, ySung, day);
            check(Rules.Available(story, Y(encore), yEncore), "Fye-less encore unavailable (chapter " + chapter + ").");
            var yPages = new HashSet<string>();
            var yOut = Program.Walk(Y(encore), yEncore, (page, _) => yPages.Add(page));
            check(yOut.Any(r => r.Has(Kept) && r.Has(P + "night_kept")) && yPages.Contains("threshold") && yPages.Contains("morning"),
                "Fye-less commit: no yes, or no night (chapter " + chapter + ").");
            check(yOut.Any(r => r.Has(P + "gone_to_nerosyan") && r.Has(Closed)), "Fye-less stage ending missing (chapter " + chapter + ").");
            var yNo = yOut.First(r => r.Has(P + "declined"));
            var yThird = Later(story, yNo, day);
            check(Rules.Available(story, Y(third), yThird) && !Rules.Available(story, M(third), yThird), "Fye-less third verse unavailable.");
            var yThirdOut = Play(Y(third), yThird);
            check(yThirdOut.Any(r => r.Has(Kept) && r.Has(P + "cost.sang_alone")) && yThirdOut.Any(r => r.Has(Closed) && !r.Has(Kept)),
                "Stall-less proposal verse or hard no missing (chapter " + chapter + ").");
            var yBilled = Yard(chapter, "trickster", "trickster.ever", "aranka.ran_romance", "aranka.ran_quest_complete", P + "primed", P + "cost.announced");
            check(Rules.Available(story, Y(arrives), Later(story, yBilled, posted)) && !Rules.Available(story, M(arrives), Later(story, yBilled, posted)),
                "Fye-less touring arrival missing (chapter " + chapter + ").");
        }
        check(!Rules.Available(story, S(duet.Id + "_yard"), answered), "The yard copy opens while Fye is serving.");

        // Epilogue pages (R2-6): the late commit, her no, the credit, the stage.
        var lateWorld = World(story, 6, "trickster", "trickster.ever", P + "duet_sung", P + "answered", P + "cost.credited");
        check(lateWorld.Has(P + "late_committed") && Rules.Available(story, epCommit, lateWorld) && Rules.Available(story, epVerse, lateWorld)
              && !Rules.Available(story, epCommit, Ending(story, committed)) && Rules.Available(story, epVerse, Ending(story, committed)),
            "The late commit or the credit page is missing.");
        check(Rules.Available(story, epDeclined, Ending(story, declined)) && !Rules.Available(story, epVerse, Ending(story, declined))
              && !Rules.Available(story, epDeclined, Ending(story, thirdOut.First(r => r.Has(Kept)))), "Her no is not remembered, or outlives her yes.");
        // Polish (item 5, R2-6): the five pages are Chapter 6 only, whatever flags a Chapter 1-5 state already holds.
        foreach (var pg in new[] { epCommit, epDeclined, S(P + "epilogue.unanswered"), epVerse, epNerosyan })
        {
            check(pg.MinChapter == 6 && pg.MaxChapter == 6 && pg.Chapters.SequenceEqual(new[] { 6 }), "An epilogue page leaves Chapter 6: " + pg.Id);
            foreach (var chapter in new[] { 1, 2, 3, 4, 5 })
            {
                var early = World(story, chapter, "trickster", "trickster.ever", P + "duet_sung", P + "answered", P + "declined", Kept, Closed,
                    P + "gone_to_nerosyan", P + "cost.credited");
                check(!Rules.Available(story, pg, early), "An epilogue page plays before the ending: " + pg.Id + " in chapter " + chapter);
            }
        }
        // Q8 (Sol TRK): a Commander who attacked the adepts in Kenabres killed her; no tavern, letter, presence or page follows.
        var murdered = World(story, 3, "trickster", "trickster.ever", "aranka.kenabres_attacked");
        check(!Rules.Available(story, tavern, murdered) && !Rules.Available(story, anyTavern, World(story, 5, "trickster", "trickster.ever", "aranka.kenabres_attacked", "coronation.after"))
              && !Rules.Available(story, epVerse, World(story, 6, "trickster", "trickster.ever", Kept, "aranka.kenabres_attacked"))
              && story.SelectedAnswers["aranka.kenabres_attacked"] == "3259064c6a1ac284c80ecc7d3fad6135",
            "A living Aranka follows her death in Kenabres.");
        // Q8 (Sol BEL): the third verse sung and its rhyme left hanging has its own page, never "never written".
        var hardNo = thirdOut.First(r => r.Has(Closed) && !r.Has(Kept));
        check(!Rules.Available(story, epDeclined, Ending(story, hardNo)) && Rules.Available(story, S(P + "epilogue.unanswered"), Ending(story, hardNo))
              && !Rules.Available(story, S(P + "epilogue.unanswered"), Ending(story, declined)), "The hard no after the third verse reads as never written.");
        // Q8 (Sol BEL/CAN): the touring and mocking primers never hear the tambourine verse.
        check(!Rules.Available(story, S(P + "react.anevia_verse"), World(story, 3, "trickster", "trickster.ever", P + "primed", P + "cost.announced"))
              && !Rules.Available(story, S(P + "react.lann_verse"), World(story, 3, "trickster", "trickster.ever", P + "answered", P + "cost.mocking_verse", P + "cost.credited")),
            "A reaction sings a verse the Commander never wrote.");
        var sheet = tavern.Nodes.Single(n => n.Id == "sheet").Text;
        check(!sheet.Contains("crown"), "The King swears on a crown he may not have.");
        check(Rules.Available(story, epNerosyan, Ending(story, released)) && !Rules.Available(story, epVerse, Ending(story, released))
              && !Rules.Available(story, epCommit, Ending(story, released)), "The stage page is missing, or the Commander is credited as her lover.");

        // Coordinator ruling 2026-10-02 (item 3): her Last Call coda takes the late yes too, in Chapter 6, with explicit guards.
        var coda = S("aranka.lastcall.page");
        var lateCall = World(story, 6, "trickster", "trickster.ever", "lastcall.active", P + "duet_sung", P + "answered");
        check(coda.MinChapter == 6 && coda.MaxChapter == 6 && Rules.Available(story, coda, lateCall) && !lateCall.Has(Kept)
              && !Rules.Available(story, coda, World(story, 5, "trickster", "trickster.ever", "lastcall.active", P + "duet_sung", P + "answered")),
            "The late yes loses her Last Call coda, or the coda plays before the ending.");
        foreach (var (block, lift) in new[] { (P + "declined", Kept), (Closed, (string?)null), ("aranka.kenabres_attacked", null),
                                              ("sacrifice", "trickster.commander_back"), ("aranka.ran_failure", Repaired) })
        {
            var w = World(story, 6, "trickster", "trickster.ever", "lastcall.active", P + "duet_sung", P + "answered", block);
            if (block == "sacrifice") { w.Flags.ExceptWith(new[] { "ending.trickster", "ending.wound_closed", "trickster.lastcall.pillar.bottle" }); Rules.Complete(story, w); }
            check(!Rules.Available(story, coda, w), "Her coda ignores " + block);
            if (lift != null)
                check(Rules.Available(story, coda, World(story, 6, "trickster", "trickster.ever", "lastcall.active", P + "duet_sung", P + "answered", block, lift)),
                    "Her coda stays shut after " + lift);
        }
        check(!Rules.Available(story, coda, World(story, 6, "trickster", "trickster.ever", "lastcall.active", P + "duet_sung", P + "answered", Kept, Closed)),
            "A closed route keeps her coda through a kept flag.");

        // Polish (item 6): the post-Coronation chain from real choices, with derived placement and a 168-hour deadline.
        // Native facts only; contacts are granted only after the presence plan spawns her copy; every beat is the named choice.
        var market = story.Presences["aranka.presence"];
        Snapshot Place(Snapshot w, bool marketAnchor, bool yardAnchor)
        {
            var at = Program.Copy(w);
            at.AvailableContacts.Clear();
            at.Flags.Remove(FyeGone);
            at.Flags.ExceptWith(story.Derived.Keys);
            Rules.Complete(story, at);
            bool wanted = Rules.PresenceWanted(market, at);
            var plan = Rules.PlanPresence(market, wanted, new PresenceObservation { AreaLoaded = true, AnchorResolved = marketAnchor });
            if (!wanted) { check(plan.Length == 0, "Her market copy is planned while she is not wanted."); return at; }
            if (marketAnchor)
            {
                check(plan.SequenceEqual(new[] { PresenceStep.Spawn }), "Her market copy is not spawned beside a live stall.");
                at.AvailableContacts.Add(Unit);
                return at;
            }
            check(plan.SequenceEqual(new[] { PresenceStep.Blocked }), "Her market copy is spawned without its stall.");
            at.Flags.Add(FyeGone);   // the runtime's observation of the blocked anchor (never stamped)
            Rules.Complete(story, at);
            var yardPlan = Rules.PlanPresence(yard, Rules.PresenceWanted(yard, at), new PresenceObservation { AreaLoaded = true, AnchorResolved = yardAnchor });
            check(yardPlan.SequenceEqual(new[] { yardAnchor ? PresenceStep.Spawn : PresenceStep.Blocked }), "The yard copy ignores its anchor.");
            if (yardAnchor) at.AvailableContacts.Add(YardUnit);
            return at;
        }
        Snapshot Pick(Scene scene, Snapshot w, string node, int choice)
        {
            check(Rules.Available(story, scene, w), "Walk: " + scene.Id + " is unavailable when its beat is due.");
            var hit = Program.WalkVia(scene, w, node, choice).FirstOrDefault();
            check(hit != null, "Walk: no path through " + scene.Id + "/" + node + "/" + choice);
            if (hit == null) return w;
            // Main observes a fresh snapshot each tick; Derived flags are computed, never saved.
            hit.Flags.ExceptWith(story.Derived.Keys);
            Rules.Complete(story, hit);
            return hit;
        }
        Scene Venue(Scene s, Snapshot w) => w.Has(FyeGone) ? S(s.Id + "_yard_late") : L(s);
        void Chain(string label, Snapshot answeredAt, int t0, bool marketAnchor)
        {
            check(Rules.PresenceWanted(market, answeredAt), label + ": her presence is not wanted after her answer.");
            if (answeredAt.Has("aranka.ran_failure"))
            {
                var rel = story.Relationships["aranka"];
                check(answeredAt.Has(P + "answered") && answeredAt.Has(P + "returned")
                    && answeredAt.Has(P + "cost.mocking_verse") && !answeredAt.Has(Repaired)
                    && !Rules.RouteOpen(rel, answeredAt), label + ": her paid reply bypasses moral repair.");
                Snapshot Fresh(params string[] added) => Native(story, answeredAt.Chapter,
                    answeredAt.Flags.Where(k => !story.Derived.ContainsKey(k)).Concat(added).ToArray());
                check(!Fresh(Kept).Has("aranka.harem.eligible"),
                    label + ": presence during repair opens household eligibility.");
                foreach (var blocked in rel.UnavailableFlags.Where(f => f != "aranka.ran_failure").Append(Closed))
                {
                    var lost = Fresh(blocked);
                    var lostYard = Fresh(blocked, FyeGone);
                    check(!Rules.PresenceWanted(market, lost) && !Rules.PresenceWanted(yard!, lostYard),
                        label + ": paid reply lifts another closure: " + blocked);
                }
                var unmended = Place(Later(story, answeredAt, 24), marketAnchor, true);
                check(!Rules.Available(story, Venue(duet, unmended), unmended), label + ": the duet opens before the reckoning.");
                var facing = Place(answeredAt, marketAnchor, true);
                var encounter = facing.Has(FyeGone) ? reckoningYard : reckoning;
                var deferred = Pick(encounter, facing, "start", 2);
                check(!deferred.Has(Repaired) && Rules.PresenceWanted(market, deferred)
                    && !Rules.RouteOpen(rel, deferred), label + ": deferring changes the repair requirements.");
                var refused = Pick(encounter, facing, "unchanged", 0);
                var refusedFresh = Native(story, refused.Chapter,
                    refused.Flags.Where(k => !story.Derived.ContainsKey(k)).ToArray());
                check(refusedFresh.Has(Closed) && !Rules.PresenceWanted(market, refusedFresh),
                    label + ": refusing the reckoning leaves her physical presence.");
                answeredAt = Pick(encounter, facing, "bought", 0);
                check(answeredAt.Has(Repaired) && answeredAt.Has(P + "cost.provisions_bought")
                    && Rules.RouteOpen(rel, answeredAt) && !Fresh(Kept).Has("aranka.harem.eligible"),
                    label + ": the paid reckoning does not reopen the full route.");
            }
            var tooEarly = Place(Later(story, answeredAt, 23), marketAnchor, true);
            check(!Rules.Available(story, Venue(duet, tooEarly), tooEarly), label + ": the duet comes before its day.");
            var duetAt = Place(Later(story, answeredAt, 24), marketAnchor, true);
            var sung = Pick(Venue(duet, duetAt), duetAt, "signed", 0);
            var encoreAt = Place(Later(story, sung, 24), marketAnchor, true);
            var stayed = Pick(Venue(encore, encoreAt), encoreAt, "choice", 0);
            check(stayed.Has(Kept) && stayed.Hour - t0 <= 168, label + ": her yes misses the week (" + (stayed.Hour - t0) + " h).");
            var notYet = Pick(Venue(encore, encoreAt), encoreAt, "not_yet", 0);
            var thirdAt = Place(Later(story, notYet, 24), marketAnchor, true);
            var asked = Pick(Venue(third, thirdAt), thirdAt, "start", 0);
            check(asked.Has(Kept) && asked.Hour - t0 <= 168, label + ": the second ask misses the week (" + (asked.Hour - t0) + " h).");
            var left = Pick(Venue(encore, encoreAt), encoreAt, "choice", 2);
            check(!Rules.PresenceWanted(market, left) && Rules.PlanPresence(market, false,
                    new PresenceObservation { AreaLoaded = true, CopyFound = true, CopyAlive = true }).SequenceEqual(new[] { PresenceStep.Remove }),
                label + ": her copy stays after she takes the stage.");
        }
        foreach (var anchor in new[] { true, false })
        {
            var venueLabel = anchor ? " (market)" : " (yard)";
            // King, fresh: his round, her letter at the next day's rest, then the presence.
            var kingWorld = Native(story, 5, "trickster", "trickster.ever", "fool_king.crowned", "coronation.after");
            int t0 = kingWorld.Hour;
            var primed = Pick(tavern5, kingWorld, "crowned", 0);
            check(!Rules.PresenceWanted(market, primed) && !Rules.Available(story, duetL, Place(Later(story, primed, 100), anchor, true)),
                "Walk: she is in Drezen before she has answered.");
            check(!Rules.MailbagArrivals(story, Later(story, primed, 23)).Contains(herLetterL)
                  && Rules.MailbagArrivals(story, Later(story, primed, 24)).Contains(herLetterL), "Walk: her Chapter 5 letter misses its day.");
            Chain("King, fresh" + venueLabel, Pick(herLetterL, Later(story, primed, 24), "unknown", 0), t0, anchor);
            // King, failure: the verse where the Commander loses, then her letter a day later.
            var failWorld = Native(story, 5, "trickster", "trickster.ever", "aranka.ran_failure", "fool_king.crowned", "coronation.after");
            check(!Rules.PresenceWanted(market, failWorld) && !Rules.PresenceWanted(yard!, failWorld)
                && !Rules.Available(story, reckoning, Place(failWorld, anchor, true)),
                "King, unpaid failure" + venueLabel + ": she returns before the paid verse.");
            var led5 = Pick(mocking5, failWorld, "after", 0);
            var awaitingReply = Later(story, led5, 24);
            check(led5.Has(P + "cost.mocking_verse") && !awaitingReply.Has(P + "answered")
                && !Rules.PresenceWanted(market, awaitingReply)
                && !Rules.Available(story, reckoning, Place(awaitingReply, anchor, true)),
                "King, unanswered failure" + venueLabel + ": the primer alone brings her back.");
            check(Rules.MailbagArrivals(story, Later(story, led5, 24)).Contains(secondVerseL), "Walk: her failure letter misses its day.");
            Chain("King, failure" + venueLabel, Pick(secondVerseL, Later(story, led5, 24), "start", 0), failWorld.Hour, anchor);
            // No King: the reply is folded into the fallback.
            var noKing = Native(story, 5, "trickster", "trickster.ever", "coronation.after");
            Chain("No King, fresh" + venueLabel, Pick(anyTavern, noKing, "reply_unknown", 0), noKing.Hour, anchor);
            var noKingFail = Native(story, 5, "trickster", "trickster.ever", "aranka.ran_failure", "coronation.after");
            Chain("No King, failure" + venueLabel, Pick(mockingAny, noKingFail, "her_reply", 0), noKingFail.Hour, anchor);
            // Touring: the posters, the courier, her arrival a day later.
            var tour = Native(story, 5, "trickster", "trickster.ever", "aranka.ran_romance", "aranka.ran_quest_complete", "coronation.after");
            var posted = Pick(boast, tour, "posters", 0);
            var arriveAt = Place(Later(story, posted, 24), anchor, true);
            check(!Rules.Available(story, Venue(arrives, arriveAt), Place(Later(story, posted, 23), anchor, true)), "Walk: the touring arrival comes early.");
            Chain("Touring" + venueLabel, Pick(Venue(arrives, arriveAt), arriveAt, "shout", 0), tour.Hour, anchor);
        }
        // Neither anchor resolves: no in-person beat is playable.
        var stranded = Place(Later(story, Native(story, 5, "trickster", "trickster.ever", P + "answered", "aranka.extension_started"), 24), false, false);
        check(!Rules.Available(story, duetL, stranded) && !Rules.Available(story, S(duet.Id + "_yard_late"), stranded),
            "Walk: a duet plays with no copy of her placed.");
        // A save that finished the original duet in Chapter 5 before the split: no replay; the encore twin follows.
        var oldSave = World(story, 5, "trickster", "trickster.ever", P + "answered", "aranka.extension_started", P + "duet_sung", duet.Id);
        check(!Rules.Available(story, duetL, oldSave) && Rules.Available(story, encoreL, oldSave), "An old Chapter 5 duet replays, or strands the encore.");

        // Reactions: exactly Anevia, Woljif and Lann (ledger 05 3.1), with their guards.
        var reactions = story.Scenes.Where(s => s.Relationship == "aranka" && s.Reaction).ToArray();
        check(reactions.Select(s => s.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Anevia", "Lann", "Woljif" }),
            "Aranka's reactors changed.");
        var anevia = S(P + "react.anevia_verse");
        var aneviaAlone = S(P + "react.anevia_verse_alone");
        var widowed = World(story, 3, "trickster", "trickster.ever", P + "primed", P + "cost.round_bought", "irabeth_dead");
        check(!Rules.Available(story, anevia, widowed) && Rules.Available(story, aneviaAlone, widowed)
              && Rules.Available(story, anevia, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "cost.round_bought")), "Anevia's Beth line plays over Irabeth's grave.");
        var returnedBeth = World(story, 3, "trickster", "trickster.ever", P + "primed", P + "cost.round_bought", "irabeth_dead", "irabeth.trickster.returned");
        check(Rules.Available(story, anevia, returnedBeth) && !Rules.Available(story, aneviaAlone, returnedBeth),
            "Anevia still mourns a returned Irabeth.");
        check(!Rules.Available(story, S(P + "react.woljif_billing"), World(story, 3, "trickster", "trickster.ever", P + "duet_sung", "woljif.dead")),
            "A dead Woljif sells the fine print.");
        // Audit polr4 (BEL, Directive 12): Woljif answers the night itself, after either intimate commitment, never the duet alone.
        var roof = S(P + "react.woljif_roof");
        check(roof.Requires.SequenceEqual(new[] { P + "night_kept", "aranka.present_now" }) && roof.Forbids.SequenceEqual(new[] { "woljif.dead", "woljif.kicked_out" })
              && !Rules.Available(story, roof, World(story, 3, "trickster", "trickster.ever", P + "duet_sung", P + "answered"))
              && Rules.Available(story, roof, committed) && Rules.Available(story, roof, thirdOut.First(r => r.Has(Kept)))
              && !Rules.Available(story, roof, World(story, 5, "trickster", "trickster.ever", P + "night_kept", "woljif.kicked_out")),
            "Nobody in the camp answers her night, or Woljif answers it from the grave.");
        // Audit polr4 (VOI): the proposal is sung, and the Commander's answer is the rhyme.
        foreach (var s in new[] { third, S(third.Id + "_yard"), thirdL, S(third.Id + "_yard_late") })
            check(s.Nodes[0].Text.Contains("sing me a reason, or sing me away") && s.Nodes[0].Choices[0].Text.Contains("every day"),
                "The third verse is summarized, not sung: " + s.Id);

        // G5: no Aranka Trickster beat gates on another romance.
        var others = story.Relationships.Where(p => p.Key != "aranka")
            .SelectMany(p => new[] { p.Value.ClosedFlag, p.Value.CommittedFlag, p.Value.StartedFlag }.Concat(p.Value.UnavailableFlags))
            .Except(new[] { "trickster.failed", "inhuman", "swarm", "true_lich", "sacrifice", "ascended", "loss", "demon", "devil", "lich" }).ToHashSet();
        foreach (var s in story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal) && !s.Reaction))
            check(!s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)).Any(others.Contains),
                "G5: an Aranka Trickster scene gates on another romance: " + s.Id);
    }
}
