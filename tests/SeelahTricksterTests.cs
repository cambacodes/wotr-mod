using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Seelah, Trickster (Writer/handoffs/trickster/seelah.md): rob the thief (F07). One block per spec rules test
// (Trk_Seelah_*), plus the registered-route integration (G6 overrides, the retired revive, the presence, Irabeth's barks).
internal static class SeelahTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Npc = "90481a29cc75f424b9891a55c6dcbb53";
    private const string Diamond = "6a7cdeb14fc6ef44580cf639c5cdc113";
    private const string Returned = "seelah.trickster.returned";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.AvailableContacts.Add(Npc);
        Rules.Complete(story, state);
        foreach (var latch in story.Latches.Keys.Where(state.Has)) state.Times[latch] = state.Hour - 48;
        return state;
    }

    // The world after a walk, observed later: the native death etude ends once the retained unit stands up.
    private static Snapshot After(Story story, Snapshot outcome, int hours, params string[] drop)
    {
        var later = Program.Copy(outcome);
        later.Hour += hours;
        foreach (var flag in drop) later.Flags.Remove(flag);
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var lesson = S("seelah.trickster.in_party.lift_lesson");
        var pick = S("seelah.trickster.dead.pickpocket");
        var wakes = S("seelah.trickster.dead.wakes");
        var effects = S("seelah.trickster.dead.pickpocket_effects");
        var setup = S("seelah.trickster.dismissed.setup");
        var late = S("seelah.trickster.dismissed.late");
        var papers = S("seelah.trickster.dismissed.back_for_the_papers");
        var papersLetter = S("seelah.trickster.dismissed.back_for_the_papers_letter");
        var stay = S("seelah.trickster.after.stay_or_go");
        var commit = S("seelah.trickster.dismissed.commit");
        var second = S("seelah.trickster.dismissed.second_ask");
        var devices = new[] { pick, effects, late, papers, papersLetter };
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        IEnumerable<Choice> Choices(Scene s) => s.Nodes.SelectMany(n => n.Choices);

        // Hooks and data.
        check(setup.AnswerLists.SequenceEqual(new[] { "64cfedbb85f36a44cb45f568f18152f7" })
              && setup.NativeReturnCue == "3a2c9f56a58b5c1478746c3ebc456986" && setup.EntryMythic == "PlayerIsTrickster"
              && setup.TricksterState == "dismissed", "Dismissal setup left the native dismissal list.");
        var joke = setup.Nodes.Single().Choices.Single();
        check(joke.NativeNext == "6b81c330ca8b1324186cb02bdc8d9c54" && joke.Set.Contains("seelah.trickster.primed")
              && joke.Set.Contains("seelah.trickster.pockets_picked"), "Dismissal joke lost its native farewell or its flags.");
        check(new[] { lesson, wakes }.All(s => s.AnswerLists.SequenceEqual(new[] { "417fa384f3250634bb71859fbc913453" })),
            "Lift lesson or waking left her companion hub.");
        check(new[] { papers, stay, commit, second }.All(s => s.ContactUnit == Npc && s.InteractionHub == "seelah.presence"),
            "Tavern scenes left the presence.");
        check(pick.Remote && pick.Recovery == "seelah" && effects.Remote && late.Remote && papersLetter.Remote,
            "Remote devices mislabelled.");
        check(pick.TricksterState == "dead" && effects.TricksterState == "dead_no_unit" && late.TricksterState == "dismissed"
              && papers.TricksterState == "dismissed", "Device states mislabelled.");
        var rel = story.Relationships["seelah"];
        check(rel.UnavailableOverrides["seelah_dead"] == Returned && rel.UnavailableOverrides["seelah_gone"] == Returned
              && rel.TricksterAccess.Count == 3, "Seelah relationship patch missing.");
        check(story.Presences.TryGetValue("seelah.presence", out var presence) && presence.Unit == Npc && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == "0f12118177d102f428a3b30b15b132eb", "Seelah presence missing or on the companion unit.");
        check(story.RemovableItems.Contains(Diamond) && story.InventoryItems["seelah.diamond_held"] == Diamond, "Diamond not whitelisted.");

        // Trk_Seelah_InParty: the lesson is planted while she is in the party; no device opens.
        var party = World(story, 3, "trickster", "trickster.ever");
        check(Rules.Available(story, lesson, party) && !Any(party, devices), "Trk_Seelah_InParty failed.");
        var lessons = Program.Walk(lesson, party);
        check(lessons.Count == 2 && lessons.All(r => r.Has("seelah.trickster.lift_lesson")),
            "Trk_Seelah_InParty: both check results must record that she taught the lift.");
        check(Choices(lesson).Single(c => c.Check != null).Check!.Skill == "SkillThievery", "The lesson is not a Thievery check.");

        // Trk_Seelah_Dead: retained unit, a diamond in the coat.
        var dead = World(story, 3, "trickster", "trickster.ever", "seelah_dead", "revive.seelah.available", "seelah.diamond_held");
        check(dead.Has("seelah.finally_dead"), "seelah.finally_dead is not derived from the retained dead unit.");
        check(Rules.Available(story, pick, dead) && !Any(dead, effects, papers, late), "Trk_Seelah_Dead: wrong device set.");
        check(!Rules.Available(story, S("seelah.fate_life"), dead), "The retired revive still opens beside the pickpocket.");
        var joker = Choices(pick).Single(c => c.Mythic == "PlayerIsTrickster");
        check(joker.Alignment?.Direction == "Chaotic" && joker.Alignment.Value == 1, "The pickpocket lost its alignment price.");
        var paid = Choices(pick).Where(c => c.Revive == "seelah").ToList();
        check(paid.Count == 2 && paid.Count(c => c.RemoveItem == Diamond) == 1
              && paid.Count(c => c.Crusade?.Resource == "Favors" && c.Crusade.Amount == -100) == 1, "The rite's two prices are wrong.");
        // Polish b9c: the bowl is filled by a lift on the relic-seller (her list's last line); the lift or the caught lift
        // both fill it, and only the caught one leaves him knowing the Commander's face.
        var raised = Program.Walk(pick, dead).Where(r => r.Has(Returned)).ToList();
        check(raised.Count == 2 && raised.All(r => r.Has("seelah.revived") && r.Has("seelah.trickster.cost.holds_her_death")
              && !r.Has("seelah.trickster.cost.chaplains_word")) && raised.Count(r => r.Has("seelah.trickster.cost.broker_knows")) == 1,
            "Trk_Seelah_Dead: the diamond rite sets the wrong flags, or a failed lift closes the road.");
        var liftDcs = Choices(pick).Where(c => c.Check != null).Select(c => (c.Check!.DC, lessoned: c.Requires.Contains("seelah.trickster.lift_lesson"))).ToList();
        check(liftDcs.Count == 2 && liftDcs.Single(d => d.lessoned).DC == 15 && liftDcs.Single(d => !d.lessoned).DC == 25
              && Choices(pick).Where(c => c.Check != null).All(c => c.Check!.Skill == "SkillThievery" && c.Mythic == null),
            "The relic-seller lift is not her lesson's Thievery check, or a mythic power does it.");
        var standing = After(story, raised[0], 1, "seelah_dead", "revive.seelah.available");
        check(Rules.Available(story, wakes, standing) && !Rules.Available(story, S("seelah.fate_return"), standing),
            "Trk_Seelah_Dead: she does not wake into her own scene.");
        check(!Rules.Available(story, wakes, After(story, raised[0], 1)), "She wakes while the death etude still holds.");
        check(!Any(standing, devices), "A second device opened after the rite.");

        // Trk_Seelah_Dead_NoDiamond: the chapel's reserve, on the Commander's word.
        var poor = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "revive.seelah.available");
        var owed = Program.Walk(pick, poor).Where(r => r.Has(Returned)).ToList();
        check(Rules.Available(story, pick, poor) && owed.Count == 2 && owed.All(r => r.Has("seelah.trickster.cost.chaplains_word")),
            "Trk_Seelah_Dead_NoDiamond failed.");

        // Trk_Seelah_Wakes: her price for getting up.
        var woke = Program.Walk(wakes, standing);
        check(woke.Any(r => r.Has("seelah.trickster.death_returned")) && woke.Any(r => r.Has("seelah.trickster.cost.keeps_it"))
              && woke.All(r => r.Has("seelah.trickster.woke")), "Trk_Seelah_Wakes failed.");

        // Trk_Seelah_Dead_NoBody: no retained unit; the rite by rider, and she comes to Drezen.
        var nobody = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "seelah.diamond_held");
        check(Rules.Available(story, effects, nobody) && !Any(nobody, pick, late, papers), "Trk_Seelah_Dead_NoBody: wrong device set.");
        var ridden = Program.Walk(effects, nobody).Where(r => r.Has(Returned)).ToList();
        check(ridden.Count == 2 && ridden.All(r => r.Has("seelah.trickster.correspondent") && r.Has("seelah.trickster.cost.holds_her_death"))
              && Choices(effects).Count(c => c.RemoveItem == Diamond) == 1, "Trk_Seelah_Dead_NoBody: the rider rite sets the wrong flags.");
        var inTown = After(story, ridden[0], 30);
        check(inTown.Has("seelah.trickster.in_drezen") && Rules.Available(story, stay, inTown) && !Rules.Available(story, wakes, inTown),
            "Trk_Seelah_Dead_NoBody: she never comes to Drezen, or wakes into a party she is not in.");

        // Trk_Seelah_Dismissed: the papers, primed at the dismissal, come back in person.
        var herded = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.primed");
        check(Rules.Available(story, papers, herded) && !Any(herded, late, papersLetter, pick, effects), "Trk_Seelah_Dismissed: wrong device set.");
        var back = Program.Walk(papers, herded);
        check(back.Count == 2 && back.All(r => r.Has(Returned) && r.Has("seelah.trickster.cost.herded")) && back.Count(r => r.Has("seelah.trickster.dared")) == 1,
            "Trk_Seelah_Dismissed: the papers do not return her.");
        check(Rules.Available(story, stay, After(story, back[0], 30)), "Trk_Seelah_Dismissed: no decision after the papers.");
        var failed = Program.Copy(herded); failed.Flags.Add("seelah.presence.failed"); failed.Hour += 200;
        check(Rules.Available(story, papersLetter, failed), "The papers letter twin does not open when the presence fails.");
        var caught = Program.Copy(herded); caught.Flags.Add("seelah.trickster.cost.caught");
        var caughtPages = new HashSet<string>();
        check(Program.Walk(papers, caught, (page, _) => caughtPages.Add(page)).Count == 2 && caughtPages.Contains("papers_caught"),
            "The caught variant blocks the papers or goes unsaid.");

        // Trk_Seelah_Dismissed_Late: the lift, now, at a worse price.
        var unprimed = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.lift_lesson");
        check(Rules.Available(story, late, unprimed) && !Rules.Available(story, papers, unprimed), "Trk_Seelah_Dismissed_Late: wrong device set.");
        var lifts = Program.Walk(late, unprimed);
        check(lifts.Any(r => r.Has("seelah.trickster.primed") && r.Has("seelah.trickster.cost.late") && !r.Has("seelah.trickster.cost.caught"))
              && lifts.Any(r => r.Has("seelah.trickster.cost.caught")) && lifts.Any(r => r.Has("seelah.trickster.declined")),
            "Trk_Seelah_Dismissed_Late: lifted, caught or let go is missing.");
        var dcs = Choices(late).Where(c => c.Check != null).Select(c => (c.Check!.DC, lessoned: c.Requires.Contains("seelah.trickster.lift_lesson"))).ToList();
        check(dcs.Single(d => d.lessoned).DC == 15 && dcs.Single(d => !d.lessoned).DC == 25, "The lesson does not make the lift easier.");
        var letGo = lifts.Single(r => r.Has("seelah.trickster.declined"));
        check(!Any(After(story, letGo, 500), devices), "A return survives her being let go.");

        // Trk_Seelah_Commit: a romance, then her choice; the threshold, the cut, the morning.
        var courted = World(story, 5, "trickster.ever", "seelah_gone", Returned, "seelah.trickster.stay_decided",
            "seelah.trickster.stays_near", "seelah.started", "seelah.kissed");
        check(courted.Has("seelah.romance") && Rules.Available(story, commit, courted) && !Rules.Available(story, second, courted),
            "Trk_Seelah_Commit: commit unavailable, or a second ask before any no.");
        var pages = new HashSet<string>();
        var kept = Program.Walk(commit, courted, (page, _) => pages.Add(page));
        check(kept.Count(r => r.Has("seelah.committed")) == 2 && pages.Contains("threshold") && pages.Contains("morning_near")
              && !pages.Contains("morning_far"), "Trk_Seelah_Commit: the committing branches or the morning are wrong.");

        // Trk_Seelah_Refusal: without a romance she offers friendship or the door; her no opens one priced ask.
        var friends = World(story, 5, "trickster.ever", "seelah_gone", Returned, "seelah.trickster.stay_decided", "seelah.trickster.goes_far",
            "seelah.trickster.courted");
        var answers = Program.Walk(commit, friends);
        check(Rules.Available(story, commit, friends) && answers.All(r => !r.Has("seelah.committed"))
              && answers.Any(r => r.Has("seelah.trickster.friends")), "Trk_Seelah_Refusal: a romantic commit without a romance.");
        var no = answers.Single(r => r.Has("seelah.trickster.declined"));
        check(!no.Has("kiana.closed") && !no.Has("jannah.closed") && !Rules.Available(story, commit, After(story, no, 100)),
            "Trk_Seelah_Refusal: her no touched another route, or the commit reopens.");
        check(!Rules.Available(story, second, After(story, no, 100)), "A second ask without a romance.");
        var loved = After(story, no, 100); loved.Flags.Add("seelah.lovers"); Rules.Complete(story, loved);
        var asked = Program.Walk(second, loved);
        check(Rules.Available(story, second, loved) && asked.Any(r => r.Has("seelah.committed") && r.Has("seelah.trickster.cost.robbed_back"))
              && asked.Any(r => r.Has("seelah.closed")), "Trk_Seelah_Refusal: the priced second ask is wrong.");
        var death = World(story, 5, "trickster.ever", "seelah_dead", Returned, "seelah.trickster.correspondent",
            "seelah.trickster.cost.holds_her_death", "seelah.trickster.stay_decided", "seelah.trickster.courted");
        var noPages = new HashSet<string>();
        Program.Walk(commit, death, (page, _) => noPages.Add(page));
        check(noPages.Contains("no_death") && !noPages.Contains("no"), "Her no does not name the death in the Commander's pocket.");

        // Q10 (Sol INT/HOW): a fresh return has no kiss behind it. Walk the actual presence scenes from the native dismissal
        // and from the no-unit death, with no authored romance, to a reachable commit; then the same with Fye's anchor failed
        // and no contact at all, through the visit twins.
        var courtship = S("seelah.trickster.after.courtship");
        check(new[] { courtship }.All(s => s.ContactUnit == Npc && s.InteractionHub == "seelah.presence" && s.AnswerLists.Length == 0),
            "The courtship left the presence hub.");
        Snapshot? Pick(List<Snapshot> outcomes, string flag) => outcomes.FirstOrDefault(r => r.Has(flag));
        void FreshReturnReachesCommit(string name, Snapshot returned, Scene stayScene, Scene courtScene, Scene commitScene)
        {
            check(!returned.Has("seelah.romance") && Rules.Available(story, stayScene, returned), name + ": no decision after the return.");
            var decided = Program.Walk(stayScene, returned).First(r => r.Has("seelah.trickster.stay_decided"));
            var waiting = After(story, decided, 60);
            check(!Rules.Available(story, commitScene, waiting) && Rules.Available(story, courtScene, waiting),
                name + ": the commit opens before any courtship, or the courtship never opens.");
            var courted = Program.Walk(courtScene, waiting);
            check(courted.All(r => r.Has("seelah.trickster.courted")) && courted.Any(r => r.Has("seelah.trickster.tavern_kissed"))
                  && courted.Any(r => !r.Has("seelah.trickster.tavern_kissed")), name + ": the courtship lacks the kiss or the friend.");
            var kissed = After(story, Pick(courted, "seelah.trickster.tavern_kissed")!, 60);
            check(kissed.Has("seelah.romance") && Rules.Available(story, commitScene, kissed)
                  && Program.Walk(commitScene, kissed).Any(r => r.Has("seelah.committed")), name + ": no commit after the kiss.");
            var friendly = After(story, courted.First(r => !r.Has("seelah.trickster.tavern_kissed")), 60);
            var answers = Program.Walk(commitScene, friendly);
            check(Rules.Available(story, commitScene, friendly) && answers.All(r => !r.Has("seelah.committed"))
                  && answers.Any(r => r.Has("seelah.trickster.friends")), name + ": the friend road commits, or is closed.");
        }
        var freshHerded = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.primed");
        FreshReturnReachesCommit("Dismissal walk", After(story, Program.Walk(papers, freshHerded)[0], 30), stay, courtship, commit);
        var freshNobody = World(story, 5, "trickster", "trickster.ever", "seelah_dead", "seelah.diamond_held");
        FreshReturnReachesCommit("No-unit walk", After(story, Program.Walk(effects, freshNobody).First(r => r.Has(Returned)), 30),
            stay, courtship, commit);

        var stayVisit = S("seelah.trickster.after.stay_or_go_visit");
        var courtVisit = S("seelah.trickster.after.courtship_visit");
        var commitVisit = S("seelah.trickster.dismissed.commit_visit");
        var secondVisit = S("seelah.trickster.dismissed.second_ask_visit");
        check(new[] { stayVisit, courtVisit, commitVisit, secondVisit }.All(s => s.Remote && s.ContactUnit == null && s.Kind == "visit"
              && s.Requires.Contains("seelah.presence.failed")), "The failed-anchor visit twins are not remote visits.");
        var noContact = World(story, 5, "trickster", "trickster.ever", "seelah_gone", "seelah.trickster.primed", "seelah.presence.failed");
        noContact.AvailableContacts.Clear();
        noContact.Hour += 200;
        Rules.Complete(story, noContact);
        check(!Any(noContact, papers, stay, courtship, commit, second) && Rules.Available(story, papersLetter, noContact),
            "Failed anchor: a presence scene opens without a contact, or the papers letter does not.");
        var mailed = After(story, Program.Walk(papersLetter, noContact).Single(), 30);
        check(mailed.AvailableContacts.Count == 0, "The failed-anchor walk gained a contact.");
        FreshReturnReachesCommit("Failed-anchor walk", mailed, stayVisit, courtVisit, commitVisit);
        var spurned = Program.Walk(commitVisit, After(story, Pick(Program.Walk(courtVisit, After(story,
            Program.Walk(stayVisit, mailed).First(), 30)), "seelah.trickster.tavern_kissed")!, 60)).Single(r => r.Has("seelah.trickster.declined"));
        var secondAsked = Program.Walk(secondVisit, After(story, spurned, 100));
        check(Rules.Available(story, secondVisit, After(story, spurned, 100)) && secondAsked.Any(r => r.Has("seelah.committed"))
              && secondAsked.Any(r => r.Has("seelah.closed")), "Failed anchor: the second ask is unreachable, or lacks its yes or its no.");

        // Trk_Seelah_PathFailed: canon fate stands after the path fails.
        var failedPath = World(story, 5, "trickster.was", "trickster.ever", "trickster.failed", "seelah_dead", "revive.seelah.available");
        check(!Any(failedPath, pick, effects, late), "Trk_Seelah_PathFailed: a device opened after the path failed.");

        // Registered route: G6(b) overrides; letters lift only for a Seelah back in the party; the retired revive.
        foreach (var s in story.Scenes.Where(s => s.Relationship == "seelah" && !s.Id.StartsWith("seelah.trickster.", StringComparison.Ordinal)))
            foreach (var flag in new[] { "seelah_dead", "seelah_gone" }.Where(s.Forbids.Contains))
                check(s.ForbidOverrides.TryGetValue(flag, out var value)
                      && value == (s.Remote ? "seelah.trickster.rejoined" : Returned), "G6(b) override missing: " + s.Id + "/" + flag);
        check(S("seelah.fate_life").Forbids.Contains("trickster.ever") && S("seelah.fate_return").Forbids.Contains(Returned),
            "The old Trickster revive is not retired.");
        foreach (var id in new[] { "irabeth.trickster.dead.react_seelah", "irabeth.trickster.killed.react_seelah" })
            if (story.Scenes.Any(s => s.Id == id))
                check(S(id).ForbidOverrides.TryGetValue("seelah_dead", out var d) && d == Returned
                      && S(id).ForbidOverrides.TryGetValue("seelah_gone", out var g) && g == Returned, "Irabeth's Seelah bark lacks G6(b): " + id);
        var together = World(story, 5, "seelah.committed", "seelah.souls_returned", "seelah_gone", Returned);
        check(Rules.Available(story, S("seelah.ending_together"), together), "A returned Seelah loses her registered ending.");
        check(story.Scenes.Where(s => s.Relationship == "seelah" && s.Reaction).All(s => Choices(s).All(c => !c.Set.Contains("seelah.closed"))),
            "A reaction closes her route.");
    }
}
