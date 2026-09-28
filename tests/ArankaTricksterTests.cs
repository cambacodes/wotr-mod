using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Aranka, Trickster (Writer/handoffs/trickster/aranka.md): the boast made true (F05) in the Fool King's tavern, the verse
// where the Commander loses (parent-mod failure) and the court poet billed before she was asked (parent romance done).
// One block per spec rules test (Trk_Aranka_*), plus hooks, the presence, the letter twin, the night, epilogues and
// reactions.
internal static class ArankaTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Unit = "430cba7801b149b4e8494ace6baf4f7c";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string KingC3 = "1a17d8053a3be7f47a7908eb6706f2fe";
    private const string KingC3Return = "814dd1a078a1c2849aefc85e2e15b2d2";
    private const string KingC5 = "6dccfd39947ef4242a8afbe36b21a46c";
    private const string KingC5Return = "7b050ba0745bf144e815632e39b34853";
    private const string P = "aranka.trickster.";
    private const string Kept = "aranka.extension_kept";
    private const string Closed = "aranka.extension_closed";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        if (chapter == 3 || chapter == 5) state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
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
        var twin = S(P + "verse.her_letter_twin");
        var encore = S(P + "verse.encore");
        var third = S(P + "verse.third_verse");
        var mocking = S(P + "failure.mocking_verse");
        var mockingAny = S(P + "failure.mocking_verse_any");
        var secondVerse = S(P + "failure.second_verse");
        var boast = S(P + "touring.boast");
        var arrives = S(P + "touring.arrives");
        var epCommit = S(P + "epilogue.commit");
        var epDeclined = S(P + "epilogue.declined");
        var epVerse = S(P + "epilogue.verse");
        var epNerosyan = S(P + "epilogue.nerosyan");
        var setups = new[] { tavern, tavern5, anyTavern, mocking, mockingAny, boast };
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
                  && s.Chapters.SequenceEqual(new[] { 3, 5 }), "An in-person beat left her place at Fye's counter: " + s.Id);
        foreach (var s in new[] { anyTavern, herLetter, twin, mockingAny, secondVerse, boast })
            check(Rules.IsRemote(s), "A letter is physical: " + s.Id);
        check(twin.Chapters.SequenceEqual(new[] { 3 }), "The letter twin reaches past Chapter 3.");
        var rel = story.Relationships["aranka"];
        check(rel.UnavailableOverrides["aranka.ran_failure"] == P + "returned" && rel.TricksterAccess.Count == 3
              && rel.TricksterAccess["aranka.ran_failure"].Detect.SequenceEqual(new[] { "aranka.ran_failure" })
              && rel.CommittedFlag == Kept && rel.ClosedFlag == Closed, "Aranka's relationship patch is wrong.");
        foreach (var s in new[] { mocking, mockingAny, secondVerse })
            check(s.TricksterDevice && s.TricksterState == "aranka.ran_failure", "A failure-state scene is not an ER-2 device: " + s.Id);
        check(story.Presences.TryGetValue("aranka.presence", out var presence) && presence.Unit == Unit && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == Fye && presence.Dialog == "hub" && presence.Forbids.Contains(Closed)
              && presence.MinChapter == 3 && presence.MaxChapter == 5 && presence.Requires.Contains("aranka.trickster.in_drezen"),
            "Her presence at Fye's counter is missing or malformed.");
        check(!story.Presences.Any(p => p.Key != "aranka.presence" && p.Value.At?.NearUnit == Fye && p.Value.At.Side == presence.At!.Side),
            "Aranka's copy would stand on another presence's side of Fye.");

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

        // Chapter 5: the crowned King's hub, and not once he is gone.
        var c5 = World(story, 5, "trickster", "trickster.ever", "fool_king.crowned");
        check(Rules.Available(story, tavern5, c5) && !Rules.Available(story, tavern, c5), "The Chapter 5 King's round is missing.");
        var gone = World(story, 5, "trickster", "trickster.ever", "fool_king.crowned", "fool_king.gone");
        check(!Rules.Available(story, tavern5, gone), "The King's round outlives the King.");

        // Trk_Aranka_NoKing: the late fallback, dearer, with her reply folded in.
        check(Rules.Available(story, anyTavern, gone) && anyTavern.Nodes[0].Choices[0].Crusade?.Amount == -150
              && anyTavern.Nodes[0].Choices[0].Mythic == "PlayerIsTrickster", "Trk_Aranka_NoKing: the fallback is missing or cheap.");
        var late = After(anyTavern, gone, "reply_unknown", 0);
        check(late.Has(P + "primed") && late.Has(P + "cost.late") && late.Has(P + "answered"), "Trk_Aranka_NoKing: flags.");
        check(!Rules.Available(story, herLetter, Later(story, late, 100)) && Rules.Available(story, duet, Later(story, late, 72)),
            "Trk_Aranka_NoKing: a second letter follows the fallback, or the duet does not.");
        check(!Rules.Available(story, anyTavern, World(story, 3, "trickster", "trickster.ever")),
            "The fallback opens while the King is still singing.");
        var herLetterSet = herLetter.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).ToHashSet();
        check(!herLetterSet.Contains(P + "cost.late") && !herLetterSet.Contains(P + "primed"), "Her ordinary letter records the late cost.");

        // Trk_Aranka_Duet: the billing, both ways; every opening variant is exclusive.
        var answered = World(story, 3, "trickster.ever", P + "answered", "aranka.extension_started", P + "cost.credited");
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

        // Trk_Aranka_Commit / Declined / Nerosyan, and the night after the yes.
        var ready = World(story, 5, "trickster.ever", P + "duet_sung", "aranka.extension_started", P + "answered");
        check(Rules.Available(story, encore, ready), "Trk_Aranka_Commit: the encore is unavailable.");
        var stay = encore.Nodes.Single(n => n.Id == "choice").Choices[0];
        check(stay.Set.SequenceEqual(new[] { Kept }), "The named producer is not encore/choice/0.");
        var encorePages = new HashSet<string>();
        var outcomes = Program.Walk(encore, ready, (page, _) => encorePages.Add(page));
        var committed = outcomes.First(r => r.Has(Kept));
        check(encorePages.Contains("threshold") && encorePages.Contains("morning") && committed.Has(P + "night_kept"),
            "Trk_Aranka_Commit: the yes has no night.");
        var declined = After(encore, ready, "not_yet", 0);
        check(declined.Has(P + "declined") && !declined.Has(Kept), "Trk_Aranka_Declined: her soft no.");
        check(Rules.Available(story, third, Later(story, declined, 72)) && !Rules.Available(story, encore, Later(story, declined, 72)),
            "Trk_Aranka_Declined: the third verse does not replace the encore.");
        var thirdOut = Play(third, Later(story, declined, 72));
        check(thirdOut.Any(r => r.Has(Kept) && r.Has(P + "cost.sang_alone") && r.Has(P + "night_kept"))
              && thirdOut.Any(r => r.Has(Closed) && !r.Has(Kept)), "Trk_Aranka_Declined: the priced second ask or her hard no is missing.");
        var sungAlone = third.Nodes[0].Choices[0];
        check(sungAlone.Crusade?.Resource == "Favors" && sungAlone.Crusade.Amount == -100, "Singing alone costs nothing.");
        var released = outcomes.First(r => r.Has(P + "gone_to_nerosyan"));
        check(released.Has(Closed) && !released.Has(Kept) && !Rules.Available(story, duet, Later(story, released, 500))
              && !Rules.Available(story, third, Later(story, released, 500)), "The Nerosyan stage is not a kind ending.");

        // Trk_Aranka_ParentFailure: the verse where the Commander loses, an ER-2 device; the letter, then the duet.
        var failed = World(story, 3, "trickster", "trickster.ever", "aranka.ran_failure");
        check(Rules.Available(story, mocking, failed) && !Rules.Available(story, tavern, failed) && !Rules.Available(story, anyTavern, failed),
            "Trk_Aranka_ParentFailure: availability.");
        var led = After(mocking, failed, "after", 0);
        check(led.Has(P + "primed") && led.Has(P + "cost.mocking_verse"), "Trk_Aranka_ParentFailure: flags.");
        check(Rules.Available(story, secondVerse, Later(story, led, 72)), "Trk_Aranka_ParentFailure: her letter is missing.");
        var forgiven = After(secondVerse, Later(story, led, 72), "start", 0);
        check(forgiven.Has(P + "returned") && Rules.Available(story, duet, Later(story, forgiven, 72)) && Reaches(forgiven, Kept),
            "Trk_Aranka_ParentFailure: the return does not lift the failure.");
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
        check(!Rules.Available(story, arrives, Later(story, billed, 47)) && Rules.Available(story, arrives, Later(story, billed, 48)),
            "Trk_Aranka_ParentDone: the arrival ignores its hours.");
        var arrived = Play(arrives, Later(story, billed, 48)).First();
        check(arrived.Has(P + "answered") && Rules.Available(story, duet, Later(story, arrived, 72)) && Reaches(arrived, Kept),
            "Trk_Aranka_ParentDone: the arrival does not lead to the duet.");
        check(!Rules.Available(story, boast, World(story, 5, "trickster", "trickster.ever", "aranka.ran_romance", "aranka.ran_quest_complete", "azata")),
            "The posters go up on an Azata run.");

        // Every setup excludes the others in each world (COX).
        foreach (var w in new[] { fresh, c5, gone, failed, failedLate, done })
            check(setups.Count(s => Rules.Available(story, s, w)) <= 1, "Two Aranka setups open at once.");

        // The anchor fails: the Chapter 3 letter twin, for the verse and the touring arrival alike.
        var anchorless = Later(story, answered, 96); anchorless.Flags.Add("aranka.presence.failed");
        check(Rules.Available(story, twin, anchorless) && !Rules.Available(story, twin, Later(story, answered, 96)),
            "The letter twin does not replace a failed presence, or opens while it stands.");
        var billedAnchorless = World(story, 3, "trickster.ever", "aranka.ran_romance", "aranka.ran_quest_complete", P + "primed",
                                     P + "cost.announced", "aranka.presence.failed");
        check(Rules.Available(story, twin, Later(story, billedAnchorless, 96)), "A billed Aranka cannot reach a failed anchor.");
        var twinOut = Play(twin, anchorless).Single();
        check(twinOut.Has(P + "duet_sung") && !Rules.Available(story, duet, Later(story, twinOut, 72)), "The twin plays beside the duet.");

        // Epilogue pages (R2-6): the late commit, her no, the credit, the stage.
        var lateWorld = World(story, 5, "trickster.ever", P + "duet_sung", P + "answered", P + "cost.credited");
        check(lateWorld.Has(P + "late_committed") && Rules.Available(story, epCommit, lateWorld) && Rules.Available(story, epVerse, lateWorld)
              && !Rules.Available(story, epCommit, committed) && Rules.Available(story, epVerse, committed),
            "The late commit or the credit page is missing.");
        check(Rules.Available(story, epDeclined, declined) && !Rules.Available(story, epVerse, declined)
              && !Rules.Available(story, epDeclined, thirdOut.First(r => r.Has(Kept))), "Her no is not remembered, or outlives her yes.");
        check(Rules.Available(story, epNerosyan, released) && !Rules.Available(story, epVerse, released)
              && !Rules.Available(story, epCommit, released), "The stage page is missing, or the Commander is credited as her lover.");

        // Reactions: exactly Anevia, Woljif and Lann (ledger 05 3.1), with their guards.
        var reactions = story.Scenes.Where(s => s.Relationship == "aranka" && s.Reaction).ToArray();
        check(reactions.Select(s => s.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Anevia", "Lann", "Woljif" }),
            "Aranka's reactors changed.");
        var anevia = S(P + "react.anevia_verse");
        var aneviaAlone = S(P + "react.anevia_verse_alone");
        var widowed = World(story, 3, "trickster.ever", P + "primed", "irabeth_dead");
        check(!Rules.Available(story, anevia, widowed) && Rules.Available(story, aneviaAlone, widowed)
              && Rules.Available(story, anevia, World(story, 3, "trickster.ever", P + "primed")), "Anevia's Beth line plays over Irabeth's grave.");
        var returnedBeth = World(story, 3, "trickster.ever", P + "primed", "irabeth_dead", "irabeth.trickster.returned");
        check(Rules.Available(story, anevia, returnedBeth) && !Rules.Available(story, aneviaAlone, returnedBeth),
            "Anevia still mourns a returned Irabeth.");
        check(!Rules.Available(story, S(P + "react.woljif_billing"), World(story, 3, "trickster.ever", P + "duet_sung", "woljif.dead")),
            "A dead Woljif sells the fine print.");

        // G5: no Aranka Trickster beat gates on another romance.
        var others = story.Relationships.Where(p => p.Key != "aranka")
            .SelectMany(p => new[] { p.Value.ClosedFlag, p.Value.CommittedFlag, p.Value.StartedFlag }.Concat(p.Value.UnavailableFlags))
            .Except(new[] { "inhuman", "swarm", "true_lich", "sacrifice", "ascended", "loss", "demon", "devil", "lich" }).ToHashSet();
        foreach (var s in story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal) && !s.Reaction))
            check(!s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)).Any(others.Contains),
                "G5: an Aranka Trickster scene gates on another romance: " + s.Id);
    }
}
