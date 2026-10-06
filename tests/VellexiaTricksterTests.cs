using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Vellexia, Trickster (Writer/handoffs/trickster/vellexia.md): the joke told backwards (F08, mirrored), the unfinished
// likeness (F08, killed by the sword) and the invitation to a party she has not yet decided to throw (F11, never
// visited). One block per spec rules test (Trk_Vellexia_*), plus the registered-route edits and TT-05.
internal static class VellexiaTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Nexus = "7847c3e3537104f4694167af0b9fcd0e";
    private const string Unit = "a32a07903e428d34cb0e98a804d40569";
    private const string Storyteller = "da4c28dd01413694f82b08b728a8c6e5";
    private const string StHub = "2f5b7e0b76d3c5a42a431e1e33a8db09";
    private const string StReturn = "34a0d078b4ac51547a8f5e0e1c8e1e2c";
    private const string QmHub = "3c58e83a970a0f643a88e15f2323c805";
    private const string P = "vellexia.trickster.";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = chapter == 4 ? Nexus : Drezen, Hour = 5000,
            // eng-final / E-Q8-10: fund these positive histories; the walker enforces every debit.
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        if (chapter == 5) state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null && chapter != later.Chapter)
        {
            later.Chapter = chapter.Value;
            later.Area = later.Chapter == 4 ? Nexus : Drezen;
            if (later.Chapter == 5) later.AvailableContacts.Add(Unit);
        }
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var speaks = S(P + "mirrored.speaks");
        var fetch = S(P + "mirrored.fetch");
        var unmirror = S(P + "mirrored.unmirror");
        var unmirrorStores = S(P + "mirrored.unmirror_stores");
        var portrait = S(P + "sword.portrait");
        var latePortrait = S(P + "sword.late_portrait");
        var likeness = S(P + "sword.likeness");
        var likenessStores = S(P + "sword.likeness_stores");
        var invitation = S(P + "never_visited.invitation");
        var visit = S(P + "after.visit");
        var visitQuarters = S(P + "after.visit_quarters");
        var voice = S(P + "after.voice");
        var glass = S(P + "glass.uncovered");
        var night = S(P + "after.night");
        var epCommit = S(P + "epilogue.commit");
        var evening = S("vellexia.two_unremarkable_pleasures");
        var cover = S("vellexia.the_cover_before_the_battle");
        var registeredVoice = S("vellexia.the_voice_after_the_abyss");
        var returns = new[] { unmirror, unmirrorStores, likeness, likenessStores, invitation };
        var setups = new[] { speaks, fetch, portrait, latePortrait, invitation };
        var own = story.Scenes.Where(s => s.Relationship == "vellexia" && !s.Reaction
                                          && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w).Where(r => r.Has(scene.Id)).ToList();
        Scene Ending(string name) => S("vellexia.ending_" + name);

        // Plays every available Vellexia scene forward (Chapter 4 into 5) and reports whether a flag is ever held.
        bool Reaches(Snapshot start, string flag)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 14 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    foreach (int chapter in from.Chapter == 4 ? new[] { 4, 5 } : new[] { from.Chapter })
                    {
                        var w = Later(story, from, 100, chapter);
                        foreach (var scene in own.Where(s => Rules.Available(story, s, w)))
                            foreach (var r in Program.Walk(scene, w))
                            {
                                if (r.Has(flag)) return true;
                                if (seen.Add(r.Chapter + "|" + string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                            }
                    }
                }
                frontier = next;
            }
            return false;
        }

        // Shape and hooks.
        check(speaks.Remote && portrait.Remote && speaks.Chapters.SequenceEqual(new[] { 4 }) && portrait.Chapters.SequenceEqual(new[] { 4 })
              && speaks.Areas.SequenceEqual(new[] { Nexus }) && portrait.Areas.SequenceEqual(new[] { Nexus }),
            "The Chapter 4 pages are not the Abyss letters of the night itself.");
        // Q11 (COX): the late acquisitions, the failed-anchor visit and the night are physical (the quartermaster's hub);
        // the never-met boast stays a letter.
        foreach (var s in new[] { fetch, latePortrait, visitQuarters, night })
            check(!s.Remote && s.AnswerLists.SequenceEqual(new[] { QmHub }) && s.Chapters.SequenceEqual(new[] { 5 }),
                "Q11: a Chapter 5 Trickster beat is a letter again: " + s.Id);
        check(invitation.Remote && invitation.Chapters.SequenceEqual(new[] { 5 }), "The never-met boast lost its letter shape.");
        foreach (var s in new[] { unmirror, likeness })
            check(s.AnswerLists.SequenceEqual(new[] { StHub }) && s.NativeReturnCue == StReturn && s.ContactUnit == null && !s.Remote,
                "The Storyteller does not read the object inline on his own hub: " + s.Id);
        foreach (var s in new[] { unmirrorStores, likenessStores })
            check(s.AnswerLists.SequenceEqual(new[] { QmHub }) && s.NativeReturnCue == null && !s.Remote && s.TricksterDevice,
                "The quartermaster's stores do not host the Storyteller-dead twin: " + s.Id);
        check(speaks.TricksterDevice && speaks.TricksterState == "vellexia.mirrored" && fetch.TricksterState == "vellexia.mirrored"
              && unmirror.TricksterState == "vellexia.mirrored" && unmirrorStores.TricksterState == "vellexia.mirrored",
            "Mirrored device states mislabelled.");
        check(portrait.TricksterDevice && portrait.TricksterState == "vellexia.dead" && latePortrait.TricksterState == "vellexia.dead"
              && likeness.TricksterState == "vellexia.dead" && likenessStores.TricksterState == "vellexia.dead",
            "Sword device states mislabelled.");
        var rel = story.Relationships["vellexia"];
        check(rel.UnavailableOverrides["vellexia.dead"] == P + "returned" && rel.UnavailableOverrides["vellexia.early_fight"] == P + "returned"
              && rel.UnavailableOverrides["vellexia.final_fight"] == "vellexia.fight_survived"
              && rel.UnavailableFlags.SequenceEqual(new[] { "vellexia.dead", "vellexia.early_fight", "vellexia.final_fight" }),
            "Vellexia's overrides or registered unavailable flags changed.");
        check(rel.TricksterAccess.Count == 2 && rel.TricksterAccess["vellexia.mirrored"].Detect.Contains("vellexia.final_fight")
              && rel.TricksterAccess["vellexia.dead"].Detect.Contains("vellexia.early_fight"), "Vellexia access map missing a detect key.");
        check(story.Derived["vellexia.fight_survived"].Length == 2, "fight_survived is not spared OR returned.");
        check(story.Presences.TryGetValue("vellexia.presence", out var presence) && presence.Unit == Unit && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == Storyteller && presence.Dialog == "hub" && presence.Forbids.Contains(P + "kept_as_mirror"),
            "Her presence beside the Storyteller is missing or talks while she is glass.");
        check(visit.InteractionHub == "vellexia.presence" && visit.ContactUnit == Unit && Rules.IsPresenceHubScene(visit),
            "The test in person is not on her presence hub.");
        var glassNode = unmirror.Nodes.Single(n => n.Id == "glass").Choices;
        check(unmirror.Nodes.Single(n => n.Id == "undone").SpeakerUnit == Unit && likeness.Nodes.Single(n => n.Id == "wake").SpeakerUnit == Unit,
            "Inline, Vellexia would speak with the Storyteller's portrait.");

        // Trk_Vellexia_Mirrored: the page of the night itself.
        var mirrored = World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.mirrored", "vellexia.dead",
                             "vellexia.native_finished");
        check(Rules.Available(story, speaks, mirrored) && !Any(mirrored, portrait, latePortrait, invitation, unmirror, fetch),
            "Trk_Vellexia_Mirrored: the wrong setups open on the night of the prank.");
        var spoken = Play(speaks, mirrored);
        check(spoken.Any(r => r.Has(P + "primed") && !r.Has(P + "declined")) && spoken.Any(r => r.Has(P + "declined") && !r.Has(P + "primed")),
            "Trk_Vellexia_Mirrored: crate and sheet do not decide.");
        check(Reaches(mirrored, "vellexia.committed"), "Trk_Vellexia_Mirrored: no road to the commit.");
        var finneanPages = new HashSet<string>();
        var objected = Program.Copy(mirrored); objected.Flags.Add("finnean.objected");
        Program.Walk(speaks, objected, (page, _) => finneanPages.Add(page));
        check(finneanPages.Contains("finnean"), "Finnean's objection is forgotten in the Nexus.");

        // Trk_Vellexia_Unmirror: the Storyteller reads it forwards; the Commander tells it backwards.
        var primed = World(story, 5, "trickster", "trickster.ever", "vellexia.mirrored", "vellexia.dead", P + "primed");
        check(Rules.Available(story, unmirror, primed) && !Any(primed, unmirrorStores, fetch, speaks),
            "Trk_Vellexia_Unmirror: the payoff is unavailable or its twins open beside it.");
        var told = Play(unmirror, primed);
        var nice = told.Single(r => r.Has(P + "unmirrored"));
        check(new[] { "returned", "unmirrored", "cost.bare_walls", "presumed_dead" }.All(f => nice.Has(P + f)) && nice.Has("vellexia.prediction_known")
              && !nice.Has(P + "kept_as_mirror"), "Trk_Vellexia_Unmirror: the nice trick sets the wrong flags.");
        check(Rules.Available(story, visit, Later(story, nice, 24)) && !Rules.Available(story, visit, Later(story, nice, 23)),
            "Trk_Vellexia_Unmirror: the test in person ignores its day.");
        check(!Rules.Available(story, voice, Later(story, nice, 200)), "The first call comes before she has been tested in person.");
        check(!Rules.Available(story, registeredVoice, Later(story, nice, 200)), "The registered return call opens for a Commander she never gave a shell.");
        check(Reaches(nice, "vellexia.committed"), "Trk_Vellexia_Unmirror: no road from the unmirroring to the commit.");

        // Trk_Vellexia_MirroredKept: the cruel trick; she stays glass and never commits.
        var kept = told.Single(r => r.Has(P + "kept_as_mirror"));
        check(new[] { "returned", "cost.watched", "presumed_dead" }.All(f => kept.Has(P + f)) && !kept.Has(P + "unmirrored"),
            "Trk_Vellexia_MirroredKept: the cruel trick sets the wrong flags.");
        var keptLater = Later(story, kept, 48);
        check(!Rules.Available(story, visit, keptLater) && !Rules.Available(story, voice, keptLater) && Rules.Available(story, glass, keptLater),
            "Trk_Vellexia_MirroredKept: the glass visits, or is never uncovered.");
        check(!Reaches(kept, "vellexia.committed"), "Trk_Vellexia_MirroredKept: the glass commits.");
        var covered = Play(glass, keptLater).Single();
        check(Rules.Available(story, Ending("mirror"), covered) && !new[] { "lovers", "friends", "slow", "interrupted", "closed" }
                  .Any(e => Rules.Available(story, Ending(e), covered)) && !Rules.Available(story, epCommit, covered),
            "Trk_Vellexia_MirroredKept: the glass ends anywhere but the mirror.");

        // Trk_Vellexia_PostFightMirror: the guards were called, Jerribeth betrayed her, the fight was lost, then the mirror.
        var postFight = World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.guards_called",
                              "jerribeth.betrays_vellexia", "vellexia.final_fight", "vellexia.mirrored", "vellexia.dead");
        check(Rules.Available(story, speaks, postFight), "Trk_Vellexia_PostFightMirror: final_fight blocks the mirror page.");

        // Trk_Vellexia_MirroredFetch: Chapter 4 ended without the page; Vask brings it out, dearer.
        var unfetched = World(story, 5, "trickster", "trickster.ever", "vellexia.mirrored", "vellexia.dead");
        check(Rules.Available(story, fetch, unfetched) && !Rules.Available(story, speaks, unfetched), "Trk_Vellexia_MirroredFetch: no fetch.");
        var fetched = Play(fetch, unfetched);
        var paid = fetched.Single(r => r.Has(P + "primed"));
        check(paid.Has(P + "cost.late") && fetch.Nodes[0].Choices[0].Crusade?.Resource == "Finances" && fetch.Nodes[0].Choices[0].Crusade?.Amount == -200,
            "Trk_Vellexia_MirroredFetch: the haulers are free.");
        check(Rules.Available(story, unmirror, Later(story, paid, 24)), "Trk_Vellexia_MirroredFetch: the fetched mirror cannot be read.");

        // Trk_Vellexia_UnmirrorStorytellerDead: the quartermaster's stores, and the Commander tells it alone.
        var noReader = World(story, 5, "trickster", "trickster.ever", "vellexia.mirrored", "vellexia.dead", P + "primed", "storyteller.dead_main");
        check(Rules.Available(story, unmirrorStores, noReader) && !Rules.Available(story, unmirror, noReader),
            "Trk_Vellexia_UnmirrorStorytellerDead: the dead Storyteller still reads.");
        check(Play(unmirrorStores, noReader).Any(r => r.Has(P + "unmirrored") && r.Has(P + "cost.bare_walls")),
            "Trk_Vellexia_UnmirrorStorytellerDead: the stores twin cannot unmirror her.");

        // Trk_Vellexia_Declined: canon fate stands by the Commander's own choice.
        var declined = World(story, 5, "trickster", "trickster.ever", "vellexia.mirrored", "vellexia.dead", P + "declined");
        check(!Any(declined, speaks, fetch, unmirror, unmirrorStores), "Trk_Vellexia_Declined: a declined mirror is still offered.");
        check(!Reaches(declined, "vellexia.committed"), "Trk_Vellexia_Declined: a declined mirror still commits.");

        // ENGINE-Q5: fetching and unmaking the mirror complete devices and require the live path.
        var failed = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "vellexia.mirrored", "vellexia.dead");
        check(!Rules.Available(story, fetch, failed), "Trk_Vellexia_PathFailed: a fetch completes after the lost path.");
        var failedPrimed = Program.Copy(failed); failedPrimed.Flags.Add(P + "primed");
        var failedReady = Later(story, failedPrimed, 24);
        check(!Rules.Available(story, unmirror, failedReady), "Trk_Vellexia_PathFailed: unmirroring completes after the lost path.");
        var failedGlass = unmirror.Nodes.Single(n => n.Id == "glass").Choices.Where(ch => Rules.Match(ch.Requires, ch.Forbids, failedReady)).ToList();
        check(failedGlass.All(ch => ch.Mythic == null) && failedGlass.Count(ch => !ch.Abort) == 2,
            "Trk_Vellexia_PathFailedUnmirror: a lost Trickster still sees the mythic bracket, or loses the twins.");
        var failedPages = new HashSet<string>();
        check(Program.Walk(unmirror, failedReady, (page, _) => failedPages.Add(page)).Any(r => r.Has(P + "unmirrored"))
              && failedPages.Contains("no_sparks"), "Trk_Vellexia_PathFailedUnmirror: no sparkless telling.");

        // Trk_Vellexia_NoPowerUnmaking (polish batch 9): no Trickster sparks or backwards spell does the unmaking or wakes the
        // canvas; the Commander pays (the house through Vask, the painter's sitting) and she pays (bare walls, her hands).
        foreach (var s in new[] { unmirror, unmirrorStores, likeness, likenessStores })
        check(unmirror.Nodes.Single(n => n.Id == "glass").Choices.Where(ch => ch.Next == "nice" || ch.Next == "no_sparks")
                  .All(ch => ch.Crusade?.Resource == "Finances" && ch.Crusade?.Amount < 0),
            "Trk_Vellexia_NoPowerUnmaking: the house is not bought.");
        check(likeness.Nodes.Single(n => n.Id == "spell").Choices.All(ch => ch.Set.Contains(P + "cost.sat_for_painter")),
            "Trk_Vellexia_NoPowerUnmaking: the painter's sitting costs the Commander nothing.");
        // The native sequence can free her guests first and then mirror her (Cue_0095, then Answer_0091): no furniture is left
        // to prove she holds the knot, so the reading and the lever change (the stripped house bought back), same flags.
        var freedMirror = Program.Copy(primed); freedMirror.Flags.Add("vellexia.slaves_freed");
        var freedPages = new HashSet<string>();
        var freedOut = Program.Walk(unmirror, freedMirror, (page, _) => freedPages.Add(page));
        check(freedOut.Any(r => r.Has(P + "unmirrored") && r.Has(P + "cost.bare_walls")) && freedPages.Contains("reading_freed")
              && freedPages.Contains("nice_freed") && !freedPages.Contains("reading") && !freedPages.Contains("nice"),
            "Trk_Vellexia_FreedThenMirrored: the freed house still reads as full of furniture.");

        // Trk_Vellexia_Sword: the portrait marked in the gallery, taken the night she died.
        var sword = World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.final_fight", "vellexia.dead",
                          "vellexia.slaves_freed", P + "portrait_marked");
        check(Rules.Available(story, portrait, sword) && !Any(sword, speaks, invitation, latePortrait, likeness),
            "Trk_Vellexia_Sword: the wrong setups open the night she died.");
        var swordPages = new HashSet<string>();
        var taken = Program.Walk(portrait, sword, (page, _) => swordPages.Add(page)).Where(r => r.Has(portrait.Id)).ToList();
        check(taken.Any(r => r.Has(P + "primed")) && taken.Any(r => r.Has(P + "declined")) && swordPages.Contains("freed"),
            "Trk_Vellexia_Sword: the portrait page does not decide, or forgets her freed victims.");
        check(!Rules.Available(story, portrait, World(story, 4, "trickster", "trickster.ever", "vellexia.dead")),
            "The portrait page opens without the mark from the gallery.");
        check(Reaches(sword, "vellexia.committed"), "Trk_Vellexia_Sword: no road to the commit.");
        var boughtBack = Program.Copy(sword); boughtBack.Flags.Remove("vellexia.slaves_freed"); boughtBack.Flags.Add("vellexia.returned_picture");
        var boughtPages = new HashSet<string>();
        Program.Walk(portrait, boughtBack, (page, _) => boughtPages.Add(page));
        check(boughtPages.Contains("bought_back") && !boughtPages.Contains("gallery"), "The returned picture is still in her gallery.");

        // Trk_Vellexia_EarlyFight: never reached the gallery; Vask sells her by the yard.
        var early = World(story, 5, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.early_fight", "vellexia.dead");
        check(Rules.Available(story, latePortrait, early) && !Rules.Available(story, portrait, early), "Trk_Vellexia_EarlyFight: no late portrait.");
        var earlyPages = new HashSet<string>();
        var bought = Program.Walk(latePortrait, early, (page, _) => earlyPages.Add(page)).Single(r => r.Has(P + "primed"));
        var price = latePortrait.Nodes.Single(n => n.Id == "price").Choices[0].Crusade;
        check(bought.Has(P + "cost.late") && price?.Resource == "Finances" && price.Amount == -200 && earlyPages.Contains("unmarked")
              && !earlyPages.Contains("marked"), "Trk_Vellexia_EarlyFight: Vask's canvas is free or already marked.");
        check(Rules.Available(story, likeness, Later(story, bought, 24)), "Trk_Vellexia_EarlyFight: the bought canvas cannot be read.");

        // Trk_Vellexia_Likeness: unfinished; the Storyteller's guess, her own words as foresight.
        var canvas = World(story, 5, "trickster", "trickster.ever", "vellexia.final_fight", "vellexia.dead", P + "primed");
        check(Rules.Available(story, likeness, canvas) && !Rules.Available(story, likenessStores, canvas), "Trk_Vellexia_Likeness: unavailable.");
        var woken = Play(likeness, canvas);
        check(woken.Count > 0 && woken.All(r => new[] { "returned", "cost.diminished", "presumed_dead" }.All(f => r.Has(P + f))
                                                 && r.Has("vellexia.prediction_known")), "Trk_Vellexia_Likeness: the wrong flags.");
        check(Rules.Available(story, visit, Later(story, woken[0], 24)), "Trk_Vellexia_Likeness: she is never tested in person.");
        check(Reaches(woken[0], "vellexia.committed"), "Trk_Vellexia_Likeness: no road to the commit.");
        var plain = new HashSet<string>(); Program.Walk(likeness, canvas, (page, _) => plain.Add(page));
        var told136 = Program.Copy(canvas); told136.Flags.Add("vellexia.bungler_explained");
        var foresight = new HashSet<string>(); Program.Walk(likeness, told136, (page, _) => foresight.Add(page));
        check(!plain.Contains("foresight") && foresight.Contains("foresight"), "The Cue_0136 foresight is not gated on hearing it.");

        // Trk_Vellexia_LikenessStorytellerDead.
        var dlcDead = World(story, 5, "trickster", "trickster.ever", "vellexia.final_fight", "vellexia.dead", P + "primed", "storyteller.dead_dlc");
        check(Rules.Available(story, likenessStores, dlcDead) && !Rules.Available(story, likeness, dlcDead),
            "Trk_Vellexia_LikenessStorytellerDead: the dead Storyteller still reads.");

        // Trk_Vellexia_SwordLateNeedsLiveTrickster (R2-2): an unprimed sword kill on a lost path stays dead.
        var lostSword = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "vellexia.dead");
        check(!Any(lostSword, latePortrait, portrait), "Trk_Vellexia_SwordLateNeedsLiveTrickster: the late portrait needs no live Trickster.");

        // Trk_Vellexia_Spared: no device; the registered final_fight block lifts through fight_survived.
        var spared = World(story, 5, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.final_fight", "vellexia.spared",
                           "vellexia.native_finished", "vellexia.dismissed_native", "vellexia.prediction_known", "vellexia.departure_kept");
        check(spared.Has("vellexia.fight_survived") && Rules.Available(story, registeredVoice, spared),
            "Trk_Vellexia_Spared: the spared world stays blocked by her fight.");
        check(!story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal) && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                  .Any(s => Rules.Available(story, s, spared)), "Trk_Vellexia_Spared: a Trickster scene opens for a spared Vellexia.");
        check(!Rules.Available(story, Ending("hostility"), spared), "A spared Vellexia gets the hostility ending.");

        // Q11 Trk_Vellexia_MercyContinues / _FarewellContinues: every native ending of the affair (the bored dismissal, the
        // mercy Cue_0098, the passionate farewell Cue_0106) opens the correspondence to a commitment and a night, with no
        // injected dismissal; the opening of the second invitation is true to the ending that actually happened.
        Snapshot? Step(Scene scene, Snapshot? from, string flag, int hours = 100, int? chapter = null)
        {
            if (from == null) return null;
            var w = Later(story, from, hours, chapter);
            if (!Rules.Available(story, scene, w)) return null;
            return Program.Walk(scene, w).FirstOrDefault(r => r.Has(flag));
        }
        var secondInvitation = S("vellexia.the_second_invitation");
        Snapshot? Correspond(Snapshot start, string page)
        {
            var pages = new HashSet<string>();
            if (!Rules.Available(story, secondInvitation, Later(story, start, 100))) return null;
            var opened = Program.Walk(secondInvitation, Later(story, start, 100), (pg, _) => pages.Add(pg)).FirstOrDefault(r => r.Has("vellexia.case_opened"));
            check(pages.Contains(page) && !pages.Contains("dismissed"), "Q11: the second invitation misremembers the ending: " + page);
            var read = Step(S("vellexia.the_claim_before_the_event"), opened, "vellexia.account_read", 100, 5);
            var heard = Step(S("vellexia.the_clerks_own_price"), read, "vellexia.witness_heard");
            var chosen = Step(S("vellexia.an_hour_that_counts"), Step(S("vellexia.the_wager_with_an_edge"), heard, "vellexia.wager_chosen"),
                              "vellexia.verdict_kept");
            return Step(S("vellexia.the_question_after_business"), chosen, "vellexia.committed");
        }
        var mercy = World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.final_fight", "vellexia.spared",
                          "vellexia.native_finished", "vellexia.prediction_known");
        var mercyCommitted = Correspond(mercy, "spared");
        check(mercyCommitted != null && !mercyCommitted.Has("vellexia.dismissed_native"),
            "Trk_Vellexia_MercyContinues: the spared Vellexia never reaches a commitment without an injected dismissal.");
        var parted = World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.farewell", "vellexia.native_finished",
                           "vellexia.prediction_known");
        var partedCommitted = Correspond(parted, "farewell");
        check(partedCommitted != null && !partedCommitted.Has("vellexia.dismissed_native"),
            "Trk_Vellexia_FarewellContinues: the passionate farewell never reaches a commitment.");
        check(!Rules.Available(story, secondInvitation, World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.native_finished",
                  "vellexia.prediction_known")), "Q11: the correspondence opens with no native ending of the affair.");

        // Q11 Trk_Vellexia_PeacefulNight: the peaceful lovers invite her to Drezen, and the night follows the commit.
        var calledBack = Step(registeredVoice, mercyCommitted, "vellexia.return_kept", 100, 5);
        var invitedHome = Step(evening, calledBack, "vellexia.invited");
        var parting = Step(cover, invitedHome, "vellexia.farewell_lovers");
        check(parting != null && Rules.Available(story, night, Later(story, parting, 12)),
            "Trk_Vellexia_PeacefulNight: the peaceful commit never reaches the night.");
        var peacefulNight = parting == null ? null : Program.Walk(night, Later(story, parting, 12)).SingleOrDefault();
        check(peacefulNight != null && peacefulNight.Has(P + "night_kept"), "Trk_Vellexia_PeacefulNight: the night has no threshold.");
        var uninvited = Program.Copy(mercyCommitted ?? mercy); uninvited.Flags.Remove("vellexia.invited");
        check(!Rules.Available(story, night, Later(story, uninvited, 100, 5)), "Q11: she arrives in the Commander's room uninvited and unmet.");

        // Q11 Trk_Vellexia_LoversEndingVariants: the lovers' ending follows what happened in the flesh.
        var loversNode = Ending("lovers").Nodes[0];
        int Shown(Snapshot w) => loversNode.Paragraphs.Count(pp => Rules.Match(pp.Requires, pp.Forbids, w)
                                                                 && (SurfaceIds.Has(SurfaceIds.Of(story, pp), "[vellexia.ending_lovers/start/paragraph/0]") || SurfaceIds.Has(SurfaceIds.Of(story, pp), "[vellexia.ending_lovers/start/paragraph/1]")
                                                                     || SurfaceIds.Has(SurfaceIds.Of(story, pp), "[vellexia.ending_lovers/start/paragraph/2]")));
        bool Says(Snapshot w, string text) => loversNode.Paragraphs.Any(pp => Rules.Match(pp.Requires, pp.Forbids, w) && SurfaceIds.Has(SurfaceIds.Of(story, pp), text));
        if (peacefulNight != null)
        {
            var lovers = Program.Copy(peacefulNight); Rules.Complete(story, lovers);
            check(Rules.Available(story, Ending("lovers"), lovers) && Shown(lovers) == 1 && Says(lovers, "[vellexia.ending_lovers/start/paragraph/2]"),
                "Trk_Vellexia_LoversEndingVariants: the night is not remembered in the lovers' ending.");
        }
        var letters = Program.Copy(partedCommitted ?? parted); letters.Flags.Add("vellexia.farewell_lovers");
        check(Shown(letters) == 1 && Says(letters, "[vellexia.ending_lovers/start/paragraph/0]"), "Trk_Vellexia_LoversEndingVariants: correspondence-only lovers get the wrong account.");
        var visitedOnly = Program.Copy(letters); visitedOnly.Flags.Add(P + "visited");
        check(Shown(visitedOnly) == 1 && Says(visitedOnly, "[vellexia.ending_lovers/start/paragraph/1][vellexia.trickster.mirrored.unmirror/reading_freed][vellexia.trickster.mirrored.unmirror_stores/reading_freed][trickster.lastcall.page.collectors/page/paragraph/11]"), "Trk_Vellexia_LoversEndingVariants: the earlier visit is forgotten.");

        // Q11: a Commander who came back is not mourned and keeps the ordinary ending.
        var back = Program.Copy(letters); back.Flags.Add("sacrifice"); back.Flags.Add("trickster.commander_back"); Rules.Complete(story, back);
        check(Rules.Available(story, Ending("lovers"), back) && !Rules.Available(story, Ending("sacrifice"), back),
            "Q11: the surviving Commander is mourned, or loses the lovers' ending.");
        var gone = Program.Copy(letters); gone.Flags.Add("sacrifice"); Rules.Complete(story, gone);
        check(!Rules.Available(story, Ending("lovers"), gone) && Rules.Available(story, Ending("sacrifice"), gone),
            "Q11: a genuine sacrifice keeps the lovers' ending, or loses its mourning.");

        // Q11 Trk_Vellexia_LateLastCall: the late commit reaches its Last Call coda; friendship and the slow answer do not.
        var lastCall = S("vellexia.lastcall.page");
        var lateCall = World(story, 5, "trickster", "trickster.ever", "lastcall.active", P + "returned", P + "courting", "vellexia.return_kept");
        check(lateCall.Has(P + "late_committed") && Rules.Available(story, lastCall, lateCall),
            "Trk_Vellexia_LateLastCall: the late commit has no Last Call page.");
        foreach (var refusal in new[] { "vellexia.farewell_slow", "vellexia.farewell_friends", P + "kept_as_mirror" })
        {
            var refused = Program.Copy(lateCall); refused.Flags.Add(refusal);
            check(!Rules.Available(story, lastCall, refused), "Trk_Vellexia_LateLastCall: a refused romance gets the coda: " + refusal);
        }
        check(!Rules.Available(story, lastCall, World(story, 5, "trickster", "trickster.ever", "lastcall.active", P + "returned", "vellexia.renewed_company")),
            "Trk_Vellexia_LateLastCall: friendship gets the lovers' coda.");

        // Q11 COX: Chapter 4 carries one of her shell calls, the second invitation (R2-5 allowance); the rest wait for Drezen.
        check(story.Scenes.Count(s => s.Relationship == "vellexia" && s.Remote && s.Owner == "Memory" && s.Chapters.Contains(4)) == 1,
            "Q11: the peaceful correspondence exceeds the Chapter 4 allowance.");

        // Q11 Trk_Vellexia_SecondInvitationDrezen: missing the one Chapter 4 call does not strand the correspondence; the
        // Drezen twin keeps the three native openings, opens the same account, and never plays beside the original.
        var twin = S("vellexia.the_second_invitation_drezen");
        var missedNexus = Later(story, mercy, 100, 5);
        check(Rules.Available(story, twin, missedNexus) && !Rules.Available(story, secondInvitation, missedNexus),
            "Trk_Vellexia_SecondInvitationDrezen: no Chapter 5 entry after the Nexus call was missed.");
        var twinPages = new HashSet<string>();
        var twinOpened = Program.Walk(twin, missedNexus, (pg, _) => twinPages.Add(pg)).FirstOrDefault(r => r.Has("vellexia.case_opened"));
        check(twinOpened != null && twinPages.Contains("spared") && !twinPages.Contains("dismissed"),
            "Trk_Vellexia_SecondInvitationDrezen: the twin does not open the account, or misremembers the ending.");
        var twinCommitted = Step(S("vellexia.the_question_after_business"),
            Step(S("vellexia.an_hour_that_counts"), Step(S("vellexia.the_wager_with_an_edge"),
                Step(S("vellexia.the_clerks_own_price"), Step(S("vellexia.the_claim_before_the_event"), twinOpened, "vellexia.account_read"),
                    "vellexia.witness_heard"), "vellexia.wager_chosen"), "vellexia.verdict_kept"), "vellexia.committed");
        check(twinCommitted != null, "Trk_Vellexia_SecondInvitationDrezen: the twin's chain never reaches a commitment.");
        var answeredInNexus = Program.Copy(missedNexus); answeredInNexus.Flags.Add("vellexia.the_second_invitation");
        check(!Rules.Available(story, twin, answeredInNexus), "Trk_Vellexia_SecondInvitationDrezen: both invitations play.");

        // Q11 Trk_Vellexia_Provocation: a greeted, living Vellexia with no continuation (affair unfinished, or finished without
        // the shell) is reached by a live Trickster's insult; she answers in person, gives the shell, and can be committed to.
        var provocation = S(P + "reacquire.provocation");
        foreach (var history in new[] {
            new[] { "trickster", "trickster.ever", "vellexia.greeted" },
            new[] { "trickster", "trickster.ever", "vellexia.greeted", "vellexia.native_finished", "vellexia.dismissed_native" } })
        {
            var stranded = World(story, 5, history);
            check(Rules.Available(story, provocation, stranded) && !Rules.Available(story, invitation, stranded),
                "Trk_Vellexia_Provocation: a stranded living history has no road back: " + string.Join(",", history));
            var provoked = Play(provocation, stranded).Single(r => r.Has(P + "provoked"));
            check(provoked.Has("vellexia.prediction_known") && !provoked.Has("vellexia.seal_agreed"), "Trk_Vellexia_Provocation: the shell arrives before she answers.");
            var arrives = Later(story, provoked, 24);
            check(arrives.Has(P + "in_person") && Rules.Available(story, visit, arrives), "Trk_Vellexia_Provocation: she never comes to answer it.");
            var provPages = new HashSet<string>();
            var answered = Program.Walk(visit, arrives, (pg, _) => provPages.Add(pg)).Where(r => r.Has(visit.Id)).ToList();
            check(provPages.Contains("provoked") && provPages.Contains("shell_prov") && !provPages.Contains("shell") && !provPages.Contains("entry"),
                "Trk_Vellexia_Provocation: the visit calls a living guest dead or a prophet.");
            check(Reaches(answered.First(r => r.Has(P + "courting")), "vellexia.committed"), "Trk_Vellexia_Provocation: no road to the commit.");
        }
        check(!Rules.Available(story, provocation, World(story, 5, "trickster.ever", "trickster.failed", "vellexia.greeted")),
            "Trk_Vellexia_Provocation: the insult is carried without a live Trickster.");
        // Q11 r5 Trk_Vellexia_Unpaid: the shell taken and the seller's claim read in the manor (seal_agreed, prediction_known),
        // then the native dates abandoned: she bills the walked-out evening through the shell she gave, and comes to collect.
        var unpaid = S(P + "reacquire.unpaid");
        var abandoned = World(story, 5, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.seal_agreed", "vellexia.prediction_known");
        check(!Rules.Available(story, provocation, abandoned) && Rules.Available(story, unpaid, abandoned),
            "Trk_Vellexia_Unpaid: the abandoned affair is stranded, or insulted instead of billed.");
        var billed = Play(unpaid, abandoned).Single(r => r.Has(P + "unpaid"));
        var collecting = Later(story, billed, 24);
        var unpaidPages = new HashSet<string>();
        var paidUp = Program.Walk(visit, collecting, (pg, _) => unpaidPages.Add(pg)).Where(r => r.Has(visit.Id)).ToList();
        check(Rules.Available(story, visit, collecting) && unpaidPages.Contains("unpaid") && unpaidPages.Contains("shell_unpaid")
              && !unpaidPages.Contains("shell_held") && !unpaidPages.Contains("provoked"), "Trk_Vellexia_Unpaid: she does not come to collect, or comes as someone else.");
        check(Reaches(paidUp.First(r => r.Has(P + "courting")), "vellexia.committed"), "Trk_Vellexia_Unpaid: no road to the commit.");
        foreach (var opened in new[] { new[] { "vellexia.native_finished", "vellexia.dismissed_native" }, new[] { "vellexia.case_opened" } })
        {
            var continuing = Program.Copy(abandoned); continuing.Flags.UnionWith(opened);
            check(!Rules.Available(story, unpaid, continuing), "Trk_Vellexia_Unpaid: the bill opens beside a living continuation: " + string.Join(",", opened));
        }

        // Q11 Trk_Vellexia_LateCommitThreshold: the late commit stages its own threshold and morning.
        var lateText = SurfaceIds.Of(story, epCommit.Nodes[0]) + string.Concat(epCommit.Nodes[0].Paragraphs.Select(pp => SurfaceIds.Of(story, pp)));
        check(SurfaceIds.Has(lateText, "[vellexia.trickster.epilogue.commit/start/paragraph/2]") && SurfaceIds.Has(lateText, "[vellexia.trickster.epilogue.commit/start/paragraph/2]") && SurfaceIds.Has(lateText, "[vellexia.trickster.epilogue.commit/start/paragraph/3][vellexia.trickster.epilogue.commit/start/paragraph/4]"), "Trk_Vellexia_LateCommitThreshold: the late commit fades before the threshold.");

        // Q11 r3 Trk_Vellexia_LateCommitSacrifice: a genuine sacrifice is mourned and nothing else; a Commander who came back
        // keeps the late romance; and the room follows what became of her collection.
        var lateCourted = World(story, 5, "trickster", "trickster.ever", P + "returned", P + "courting", "vellexia.return_kept", "vellexia.prediction_known",
                                P + "unmirrored", P + "cost.bare_walls");
        var lateDied = Program.Copy(lateCourted); lateDied.Flags.Add("sacrifice"); Rules.Complete(story, lateDied);
        check(!Rules.Available(story, epCommit, lateDied) && Rules.Available(story, Ending("sacrifice"), lateDied),
            "Trk_Vellexia_LateCommitSacrifice: a dead Commander is mourned and bedded at once.");
        var lateBack = Program.Copy(lateDied); lateBack.Flags.Add("trickster.commander_back"); Rules.Complete(story, lateBack);
        check(Rules.Available(story, epCommit, lateBack) && !Rules.Available(story, Ending("sacrifice"), lateBack),
            "Trk_Vellexia_LateCommitSacrifice: the surviving Commander loses the late romance, or is mourned.");
        var lateInhuman = Program.Copy(lateCourted); lateInhuman.Flags.Add("inhuman");
        check(!Rules.Available(story, epCommit, lateInhuman), "Trk_Vellexia_LateCommitSacrifice: the late romance plays for an inhuman Commander.");
        string RoomShown(Snapshot w) => string.Concat(epCommit.Nodes[0].Paragraphs.Where(pp => Rules.ParagraphVisible(pp, w)).Select(pp => SurfaceIds.Of(story, pp)));
        check(SurfaceIds.Has(RoomShown(lateCourted), "[vellexia.trickster.epilogue.commit/start/paragraph/1]") && !SurfaceIds.Has(RoomShown(lateCourted), "[vellexia.trickster.epilogue.commit/start/paragraph/0]"),
            "Trk_Vellexia_LateCommitSacrifice: the furniture she let go of is still watching.");
        var lateFull = Program.Copy(lateCourted); lateFull.Flags.Remove(P + "cost.bare_walls");
        check(SurfaceIds.Has(RoomShown(lateFull), "[vellexia.trickster.epilogue.commit/start/paragraph/0]") && !SurfaceIds.Has(RoomShown(lateFull), "[vellexia.trickster.epilogue.commit/start/paragraph/1]"),
            "Trk_Vellexia_LateCommitSacrifice: the kept collection is gone from the room.");

        // Q11 r5: an ascended Commander's late courtship is told once, on the ascent page.
        var lateAscended = Program.Copy(lateCourted); lateAscended.Flags.Add("ascended"); Rules.Complete(story, lateAscended);
        check(!Rules.Available(story, epCommit, lateAscended) && Rules.Available(story, Ending("ascent"), lateAscended)
              && Ending("ascent").Nodes[0].Paragraphs.Any(pp => Rules.ParagraphVisible(pp, lateAscended) && SurfaceIds.Has(SurfaceIds.Of(story, pp), "[vellexia.ending_ascent/start/paragraph/0]")),
            "Q11 r5: the ascended late courtship plays twice, or not at all.");

        // Q11 r3: the freed house and the picture she sent back and bought back.
        var freedBought = World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.final_fight", "vellexia.dead",
                                "vellexia.slaves_freed", "vellexia.returned_picture", P + "portrait_marked");
        var freedBoughtPages = new HashSet<string>();
        check(Program.Walk(portrait, freedBought, (pg, _) => freedBoughtPages.Add(pg)).Any(r => r.Has(P + "primed"))
              && freedBoughtPages.Contains("freed_bought_back") && !freedBoughtPages.Contains("freed") && !freedBoughtPages.Contains("bought_back"),
            "Q11: the freed gallery forgets the picture she bought back.");

        // Q11 r3: the claim opens on her clerk's acceptance, whichever invitation opened it; no absence is invented.

        // Q11 r4: an ended correspondence never gets the Last Call romance; the glove ritual never outlives the relationship;
        // the Last Call bill names what was done to her; a first meeting introduces the love thesis rather than recalling it.
        var lcPage = S("vellexia.lastcall.page");
        var brokeUp = Step(cover, invitedHome, "vellexia.closed");
        check(brokeUp != null && brokeUp.Has("vellexia.parted"), "Q11 r4: the cover's breakup does not record the parting.");
        if (brokeUp != null)
        {
            var brokeUpLc = Program.Copy(brokeUp); brokeUpLc.Flags.Add("lastcall.active"); Rules.Complete(story, brokeUpLc);
            check(!Rules.Available(story, lcPage, brokeUpLc), "Q11 r4: Last Call restores a romance the cover ended.");
        }
        var collected = Play(visit, Later(story, nice, 24)).First(r => r.Has("vellexia.closed"));
        check(collected.Has("vellexia.parted"), "Q11 r4: her no at the visit does not record the parting.");
        string Visible(Scene sc, Snapshot w) => string.Concat(sc.Nodes[0].Paragraphs.Where(pp => Rules.ParagraphVisible(pp, w)).Select(pp => SurfaceIds.Of(story, pp)));
        foreach (var ended in new[] { "vellexia.closed", "sacrifice", "inhuman" })
        {
            var w = World(story, 6, "trickster", "trickster.ever", P + "returned", P + "cost.diminished", "vellexia.prediction_known", ended);
            check(!SurfaceIds.Has(Visible(Ending("closed"), w), "[vellexia.ending_closed/start/paragraph/3]") && !SurfaceIds.Has(Visible(Ending("sacrifice"), w), "[vellexia.ending_sacrifice/start/paragraph/3]")
                  && !SurfaceIds.Has(Visible(Ending("changed"), w), "[vellexia.ending_changed/start/paragraph/3]") && SurfaceIds.Has(Visible(Ending("closed"), w), "[vellexia.ending_closed/start/paragraph/2]"),
                "Q11 r4: the glove ritual outlives the relationship (" + ended + "), or the unfinished hands are forgotten.");
        }
        var gloved = World(story, 6, "trickster", "trickster.ever", P + "returned", P + "cost.diminished", "vellexia.prediction_known", "vellexia.farewell_lovers");
        check(SurfaceIds.Has(Visible(Ending("lovers"), gloved), "[vellexia.ending_lovers/start/paragraph/6]"), "Q11 r4: the lovers lose the glove ritual.");
        foreach (var (history, bill, notBill) in new[] {
            (P + "unmirrored", 0, 1), (P + "cost.diminished", 1, 0),
            (P + "cost.predicted", 2, 0), (P + "provoked", 3, 0) })
        {
            var w = World(story, 6, "trickster", "trickster.ever", "lastcall.active", "vellexia.committed", "vellexia.lastcall.called", history);
            check(Rules.ParagraphVisible(lcPage.Nodes[0].Paragraphs[bill], w) && !Rules.ParagraphVisible(lcPage.Nodes[0].Paragraphs[notBill], w),
                "Q11 r4: the Last Call bill narrates another history: " + history);
        }
        var lcCall = story.Scenes.Single(s => s.Id == "vellexia.lastcall.call");
        var giftedFinished = World(story, 5, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.native_finished", "vellexia.spared",
                                   "vellexia.final_fight", "vellexia.coin_given", "vellexia.seal_agreed");
        var giftedPages = new HashSet<string>();
        check(Rules.Available(story, provocation, giftedFinished)
              && Program.Walk(provocation, giftedFinished, (pg, _) => giftedPages.Add(pg)).Any(r => r.Has(P + "provoked"))
              && giftedPages.Contains("finished"),
            "Q11 r4: the finished affair denies the coin and the shell she gave.");

        // Q11 Trk_Vellexia_Ch5LetterCap (ledger: one Trickster-layer Chapter 5 letter): the only remote Trickster scenes in
        // Chapter 5 sit on mutually exclusive branches, and the old first call never follows the in-person visit.
        var ch5Letters = story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal) && s.Remote && !s.Reaction
                                                 && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && s.Chapters.Contains(5))
            .Select(s => s.Id).OrderBy(id => id).ToArray();
        check(ch5Letters.SequenceEqual(new[] { P + "after.voice", P + "glass.uncovered", P + "never_visited.invitation", P + "reacquire.provocation", P + "reacquire.unpaid" }),
            "Trk_Vellexia_Ch5LetterCap: an unexpected Chapter 5 letter: " + string.Join(", ", ch5Letters));
        check(invitation.Forbids.Contains("vellexia.greeted") && provocation.Requires.Contains("vellexia.greeted")
              && S(P + "glass.uncovered").Requires.Contains(P + "kept_as_mirror") && invitation.Forbids.Contains("vellexia.dead")
              && provocation.Forbids.Contains("vellexia.mirrored") && voice.Forbids.Contains("vellexia.return_kept")
              && provocation.Forbids.Contains("vellexia.prediction_known") && unpaid.Requires.Contains("vellexia.prediction_known")
              && unpaid.Forbids.Contains("vellexia.mirrored") && unpaid.Requires.Contains("vellexia.greeted"),
            "Trk_Vellexia_Ch5LetterCap: two Chapter 5 letters can share a branch.");

        // Trk_Vellexia_Farewell: her own farewell; nothing to defy.
        var farewell = World(story, 4, "trickster", "trickster.ever", "vellexia.greeted", "vellexia.farewell", "vellexia.native_finished",
                             "vellexia.prediction_known");
        check(!Any(farewell, setups), "Trk_Vellexia_Farewell: a Trickster setup opens after her farewell.");

        // Trk_Vellexia_NeverVisited / _Ch4Silent: the boast, carried word for word by a named carrier.
        var never = World(story, 5, "trickster", "trickster.ever");
        check(Rules.Available(story, invitation, never) && !Rules.Available(story, invitation, World(story, 4, "trickster")),
            "Trk_Vellexia_NeverVisited: the boast is unavailable, or speaks while her manor is still open.");
        check(!Rules.Available(story, invitation, World(story, 5, "trickster", "trickster.ever", "vellexia.greeted")),
            "Trk_Vellexia_NeverVisited: a Commander she has met boasts of a stranger.");
        var boast = invitation.Nodes[0].Choices[0];
        check(boast.Mythic == "PlayerIsTrickster" && boast.Crusade?.Resource == "Finances" && boast.Crusade?.Amount == -100,
            "The wine-factor is not paid.");
        var invited = Play(invitation, never).Single(r => r.Has(P + "entry"));
        check(new[] { "primed", "cost.predicted" }.All(f => invited.Has(P + f)) && invited.Has("vellexia.prediction_known"),
            "Trk_Vellexia_NeverVisited: the card sets the wrong flags.");
        check(Rules.Available(story, visit, Later(story, invited, 24)), "Trk_Vellexia_NeverVisited: she never comes to see the prophet.");
        check(Reaches(invited, "vellexia.committed"), "Trk_Vellexia_NeverVisited: no road to the commit.");
        check(Play(invitation, never).Any(r => r.Has(P + "declined")), "The subject cannot be changed.");

        // Trk_Vellexia_Visit: the test in person, and the shell she leaves.
        var guest = Later(story, invited, 24);
        var tested = Play(visit, guest);
        var kept1 = tested.First(r => r.Has(P + "cost.trick_kept") && r.Has("vellexia.return_kept"));
        check(kept1.Has(P + "visited") && tested.Any(r => r.Has(P + "lesson_given")) && !Rules.Available(story, visit, kept1),
            "Trk_Vellexia_Visit: the test does not record the trick, or repeats.");
        check(!Rules.Available(story, visitQuarters, guest), "The quarters twin opens while the presence stands.");
        var anchorless = Program.Copy(guest); anchorless.Flags.Add("vellexia.presence.failed"); anchorless.Hour += 48;
        var visitedAnchorless = Later(story, kept1, 48); visitedAnchorless.Flags.Add("vellexia.presence.failed");
        check(Rules.Available(story, visitQuarters, anchorless) && !Rules.Available(story, visitQuarters, visitedAnchorless),
            "The quarters twin does not replace a failed presence, or repeats the visit.");
        var shellPages = new HashSet<string>();
        var shelled = Program.Copy(guest); shelled.Flags.Add("vellexia.seal_agreed");
        Program.Walk(visit, shelled, (page, _) => shellPages.Add(page));
        check(shellPages.Contains("shell_entry_held") && !shellPages.Contains("shell_entry") && !shellPages.Contains("shell")
              && !shellPages.Contains("shell_held"), "She gives a second shell to a Commander who kept hers, or tells a living guest she is dead.");

        // The first question, asked in person at the end of the visit (Q11: the old remote first call is folded in): her
        // price spoken; her no; the registered evenings; the commit; the night.
        var calls = tested;
        check(calls.All(r => r.Has("vellexia.return_kept") || r.Has("vellexia.closed")) && !calls.Any(r => Rules.Available(story, voice, Later(story, r, 100))),
            "Q11: the old remote first call still follows the visit.");
        var no = Play(visit, Later(story, nice, 24)).First(r => r.Has("vellexia.closed"));
        check(!no.Has("vellexia.return_kept") && !Reaches(no, "vellexia.committed"), "Her no is not final.");
        var courting = calls.First(r => r.Has(P + "courting") && !r.Has(P + "cost.bored_once"));
        check(calls.Any(r => r.Has(P + "cost.bored_once")) && calls.All(r => !r.Has(P + "cost.bored_once") || r.Has(P + "cost.predicted")),
            "The dull answer is free, or asked of a Commander who never predicted her.");
        check(courting.Has("vellexia.return_kept") && courting.Has("vellexia.renewed_slow"), "The courting answer does not open the evenings.");
        check(calls.Any(r => r.Has("vellexia.renewed_company") && !r.Has(P + "courting")), "Friendship is not on offer.");
        var eveningReady = Later(story, courting, 24);
        check(Rules.Available(story, evening, eveningReady), "The registered evening does not follow a Trickster return.");
        var privateKept = Play(evening, eveningReady).First(r => r.Has("vellexia.private_kept"));
        var coverReady = Later(story, privateKept, 24);
        check(Rules.Available(story, cover, coverReady), "The registered commit does not follow a Trickster return.");
        var farewells = Play(cover, coverReady);
        var committed = farewells.FirstOrDefault(r => r.Has("vellexia.committed"));
        check(committed != null && farewells.Any(r => r.Has("vellexia.farewell_friends")), "The cover cannot commit, or cannot stay friends.");
        check(!Rules.Available(story, night, Later(story, committed!, 11)) && Rules.Available(story, night, Later(story, committed!, 12)),
            "The night of less glass ignores its hours.");
        var nightPages = new HashSet<string>();
        var nightOut = Program.Walk(night, Later(story, committed!, 12), (page, _) => nightPages.Add(page)).Single();
        check(nightPages.Contains("threshold") && nightPages.Contains("morning") && nightOut.Has(P + "night_kept"), "The night has no threshold.");
        check(Rules.Available(story, Ending("lovers"), nightOut) && !Rules.Available(story, Ending("dead"), nightOut)
              && !Rules.Available(story, epCommit, nightOut), "The lovers' ending does not follow a Trickster commit.");
        check(!Rules.Available(story, night, Later(story, courting, 100)), "The night comes before the commit.");

        // Endings after a return: grief and the mirror only while she stays dead or glass.
        var unmirroredEnd = Program.Copy(nice); unmirroredEnd.Flags.Add("vellexia.closed"); Rules.Complete(story, unmirroredEnd);
        check(!Rules.Available(story, Ending("dead"), unmirroredEnd) && !Rules.Available(story, Ending("mirror"), unmirroredEnd)
              && Rules.Available(story, Ending("closed"), unmirroredEnd), "An unmirrored Vellexia is mourned, or kept as glass.");
        var swordEnd = Program.Copy(woken[0]); swordEnd.Flags.Add("vellexia.farewell_friends"); Rules.Complete(story, swordEnd);
        check(!Rules.Available(story, Ending("hostility"), swordEnd) && !Rules.Available(story, Ending("dead"), swordEnd)
              && Rules.Available(story, Ending("friends"), swordEnd), "A painted-back Vellexia ends in hostility or grief.");
        var mirrorStands = World(story, 5, "trickster", "trickster.ever", "vellexia.mirrored", "vellexia.dead", "vellexia.prediction_known", P + "declined");
        check(Rules.Available(story, Ending("mirror"), mirrorStands) && !Rules.Available(story, Ending("dead"), mirrorStands),
            "A declined mirror loses its canon ending.");

        // Trk_Vellexia_EpilogueCommit / ...Kept (R2-6).
        var late = World(story, 5, "trickster", "trickster.ever", P + "returned", P + "courting", "vellexia.return_kept", "vellexia.prediction_known");
        check(late.Has(P + "late_committed") && Rules.Available(story, epCommit, late) && !Rules.Available(story, Ending("interrupted"), late),
            "Trk_Vellexia_EpilogueCommit: the late commit is missing, or the interrupted ending also plays.");
        var lateKept = Program.Copy(late); lateKept.Flags.Add(P + "kept_as_mirror");
        check(!Rules.Available(story, epCommit, lateKept), "Trk_Vellexia_EpilogueCommitKept: the glass commits in the epilogue.");
        var lateChose = Program.Copy(late); lateChose.Flags.Add("vellexia.farewell_kept"); lateChose.Flags.Add("vellexia.farewell_slow");
        check(!Rules.Available(story, epCommit, lateChose), "The late commit overrides the answer she was given at the cover.");

        // Registered primer: appended, Trickster-only, recorded on the scene's terminal answers.
        var gallery = S("vellexia.unfinished_likeness");
        var changed = gallery.Nodes.Single(n => n.Id == "picture_changed").Choices;
        check(changed.Count == 3 && changed[2].Next == "hands" && changed[2].Mythic == "PlayerIsTrickster" && changed[2].Set.Length == 0
              && changed[2].Requires.Contains("trickster"), "The gallery primer is not an appended Trickster answer.");
        var manor = new Snapshot { Chapter = 4, Hour = 1000, Area = gallery.Areas.Single() };
        manor.AvailableContacts.Add(Unit); manor.Flags.Add("vellexia.greeted");
        var plainGallery = Program.Walk(gallery, manor);
        var trickGallery = Program.Walk(gallery, Later(story, manor, 0).Also(s => s.Flags.Add("trickster")));
        check(plainGallery.All(r => !r.Has(P + "portrait_marked")) && trickGallery.Any(r => r.Has(P + "portrait_marked") && r.Has("vellexia.gallery_invited")),
            "The mark on the portrait is not a Trickster outcome of the gallery visit.");


        // Reviewed polish P1/C1-C6: render both hosts and body/room histories without changing their entitlement.
        string PlayedText(Scene sc, Snapshot w)
        {
            var pages = new List<string>();
            Program.Walk(sc, w, (id, state) =>
            {
                var node = sc.Nodes.Single(nd => nd.Id == id);
                pages.Add(SurfaceIds.Of(story, node) + string.Concat(node.Paragraphs.Where(pp => Rules.ParagraphVisible(pp, state)).Select(pp => SurfaceIds.Of(story, pp))));
            });
            return string.Join("\n", pages);
        }
        var refusedCrate = fetched.Single(r => r.Has(P + "declined"));
        check(!refusedCrate.Has(P + "primed") && !refusedCrate.Has(P + "returned") && !Any(refusedCrate, unmirror, unmirrorStores),
            "Polish P1: refusing the camp crate relocates it or primes the return.");
        foreach (var (host, ready) in new[] { (unmirror, primed), (unmirrorStores, noReader) })
        {
            var captiveText = PlayedText(host, ready);
            check(SurfaceIds.Has(captiveText, "[vellexia.trickster.mirrored.unmirror/reading][vellexia.trickster.mirrored.unmirror_stores/reading]") && SurfaceIds.Has(captiveText, "[vellexia.trickster.mirrored.unmirror/nice][vellexia.trickster.mirrored.unmirror_stores/nice]"),
                "Polish C6: the observed collateral is missing or never released: " + host.Id);
            var alreadyFreed = Program.Copy(ready); alreadyFreed.Flags.Add("vellexia.slaves_freed");
            var freeText = PlayedText(host, alreadyFreed);
            check(!SurfaceIds.Has(freeText, "[vellexia.trickster.mirrored.unmirror/reading][vellexia.trickster.mirrored.unmirror_stores/reading]") && !SurfaceIds.Has(freeText, "[vellexia.trickster.mirrored.unmirror/nice][vellexia.trickster.mirrored.unmirror_stores/nice]"),
                "Polish C6: already freed victims become bargaining furniture again: " + host.Id);
            var imprisoned = Play(host, ready).Single(r => r.Has(P + "kept_as_mirror"));
            var threat = PlayedText(glass, Later(story, imprisoned, 48));
            check(SurfaceIds.Has(threat, "[vellexia.trickster.glass.uncovered/speaks]"),
                "Polish C1/C3: the captive remembers an unplayed host or invented march: " + host.Id);
        }
        foreach (var (host, ready) in new[] { (likeness, canvas), (likenessStores, dlcDead) })
        {
            var readingText = PlayedText(host, ready);
            check(SurfaceIds.Has(readingText, "[vellexia.trickster.sword.likeness/spell][vellexia.trickster.sword.likeness_stores/spell]") && SurfaceIds.Has(readingText, "[vellexia.trickster.sword.likeness/spell][vellexia.trickster.sword.likeness_stores/spell]"),
                "Polish C5: the portrait promises a universal resurrection or opens the wrong notch: " + host.Id);
        }
        var recalled = Program.Copy(canvas); recalled.Flags.Add("vellexia.bungler_explained");
        check(SurfaceIds.Has(PlayedText(likeness, recalled), "[vellexia.trickster.sword.likeness/foresight]")
              && !SurfaceIds.Has(PlayedText(likeness, canvas), "[vellexia.trickster.sword.likeness/foresight]"),
            "Polish C5: the native diagnosis is misattributed or recalled without witnessing it.");
        foreach (var body in new[] { "unmirrored", "cost.diminished", "provoked", "entry" })
        {
            var intimate = World(story, 5, "trickster", "trickster.ever", "vellexia.committed", "vellexia.farewell_lovers",
                                 "vellexia.invited", P + body);
            var renderedNight = PlayedText(night, intimate);
            if (body == "cost.diminished")
                check(SurfaceIds.Has(renderedNight, "[vellexia.trickster.after.night/hands]"),
                    "Polish C2: diminished hands either immobilize her or recover their magic.");
        }
        foreach (var roomFlag in new[] { "", P + "cost.bare_walls", "vellexia.slaves_freed" })
        foreach (var party in new[] { false, true })
        {
            var atParty = Program.Copy(lateFull);
            atParty.Flags.UnionWith(new[] { P + "cost.diminished", P + "presumed_dead" });
            if (roomFlag != "") atParty.Flags.Add(roomFlag);
            if (party) atParty.Flags.Add("lastcall.active");
            var shown = RoomShown(atParty);
            check(SurfaceIds.Has(shown, "[vellexia.trickster.epilogue.commit/start/paragraph/0]") == (roomFlag == "") && SurfaceIds.Has(shown, "[vellexia.trickster.mirrored.unmirror_stores/reading][vellexia.trickster.after.voice/bare][vellexia.trickster.epilogue.commit/start/paragraph/1]") == (roomFlag != ""),
                "Polish C2: room paragraphs duplicate each other or revive freed furniture.");
            var absentDaeran = Program.Copy(atParty); absentDaeran.Flags.Add("daeran.dead");
            check(!SurfaceIds.Has(RoomShown(absentDaeran), "[vellexia.trickster.epilogue.commit/start/paragraph/4]"), "Polish C2: a dead Daeran attends breakfast.");
        }

        // TT-05: one return scene per third-date branch; no cross-relationship gate.
        foreach (var branch in new[] { mirrored, postFight, unfetched, primed, sword, early, canvas, never, spared, farewell })
        {
            var ready = Later(story, branch, 0);
            check(returns.Count(s => Rules.Available(story, s, ready)) <= 1, "TT-05: two Vellexia returns open at once.");
        }
        var others = story.Relationships.Where(p => p.Key != "vellexia")
            .SelectMany(p => new[] { p.Value.ClosedFlag, p.Value.CommittedFlag, p.Value.StartedFlag }.Concat(p.Value.UnavailableFlags))
            .Except(new[] { "trickster.failed", "inhuman", "swarm", "true_lich", "sacrifice", "ascended", "loss" }).ToHashSet();
        foreach (var s in story.Scenes.Where(s => s.Relationship == "vellexia" && s.Id.StartsWith(P, StringComparison.Ordinal)))
            check(!s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)).Any(others.Contains),
                "TT-05/G5: a Vellexia Trickster scene gates on another romance: " + s.Id);
    }

    private static T Also<T>(this T value, Action<T> action) { action(value); return value; }
}
