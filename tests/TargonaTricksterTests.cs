using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Targona, Trickster (Writer/handoffs/trickster/targona.md): spend it again, unnoticed (F16). Lariel's light, the part of his
// sword that entered the Commander in Kenabres, used without being spent: the blow that kills her in Areelu's laboratory
// lands with nothing left to spend (killed_in_lab), or the infirmary's last wand never runs down (freed_in_heaven).
// One block per spec rules test (Trk_Targona_*), plus the hooks, the presence, the night, the epilogues and the reactions.
internal static class TargonaTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Unit = "81297c673b63b60448ef88a10db6bc78";
    private const string Quartermaster = "15f754455d1d87c42a4e14df456d5415"; // F9 ordinary capital smith
    private const string LabList = "2a75fbc8e86fd514e82117c99fc9e528";
    private const string P = "targona.trickster.";
    private const string Committed = "targona.committed";
    private const string Closed = "targona.closed";

    private static Snapshot World(Story story, int chapter, params string[] flags) => World(story, chapter, true, flags);

    // contact false: the runtime's view before her copy has spawned (Sol quality pass: the contact is produced by the presence).
    private static Snapshot World(Story story, int chapter, bool contact, params string[] flags)
    {
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        if (contact && (chapter == 3 || chapter == 5)) state.AvailableContacts.Add(Unit);
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
        var setup = S(P + "dead.setup_sleep");       // Q6: the scroll primers (dead.setup, dead.setup_open) are retired by gating
        var retiredSetup = S(P + "dead.setup");
        var longSleep = S(P + "dead.long_sleep");
        var lateLight = S(P + "dead.late_light");
        var oneSoul = S(P + "dead.one_soul");
        var furlough = S(P + "dead.furlough");
        var second = S(P + "dead.second_asking");
        var spent = S(P + "free.spent_light");
        var freeFurlough = S(P + "free.furlough");
        var ward = S(P + "after.ward");
        var quiet = S(P + "after.quiet_ward");
        var epCommit = S(P + "epilogue.commit");
        var epDeclined = S(P + "epilogue.declined");
        var epFurlough = S(P + "epilogue.furlough");
        Snapshot After(Scene scene, Snapshot w, string node, int choice)
        {
            // Edge-exact (Sol quality pass, HOW): reach the node, then take exactly this choice from the state held there.
            var target = scene.Nodes.Single(n => n.Id == node).Choices[choice];
            Snapshot? at = null;
            Program.Walk(scene, w, (page, st) => { if (at == null && page == node && Rules.Match(target.Requires, target.Forbids, st)) at = Program.Copy(st); });
            check(at != null, "Node not reached with its choice open: " + scene.Id + "/" + node + "/" + choice);
            if (at == null) return w;
            var edge = new Scene { Id = scene.Id, Relationship = scene.Relationship, Owner = scene.Owner,
                                   Nodes = new[] { new Node { Id = "__edge", Choices = new List<Choice> { target } } }.Concat(scene.Nodes).ToList() };
            var hit = Program.Walk(edge, at).FirstOrDefault();
            check(hit != null && target.Set.All(hit.Has), "No outcome through " + scene.Id + "/" + node + "/" + choice);
            return hit ?? w;
        }
        bool Reaches(Snapshot w, string flag, int depth = 6)
        {
            if (w.Has(flag)) return true;
            if (depth == 0) return false;
            var later = Later(story, w, 100);
            foreach (var s in story.Scenes.Where(s => s.Relationship == "targona" && !s.Reaction
                                                   && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                                                   && Rules.Available(story, s, later)))
                foreach (var outcome in Program.Walk(s, later))
                    if (Reaches(outcome, flag, depth - 1)) return true;
            return false;
        }

        // Hooks, relationship patch and the presence.
        check(setup.AnswerLists.SequenceEqual(new[] { LabList }) && setup.NativeReturnCue == null && setup.MinChapter == 3
              && setup.MaxChapter == 3 && setup.EntryMythic == "PlayerIsTrickster" && setup.Forbids.Contains("targona.dead_lab")
              && setup.Forbids.Contains("targona.free") && setup.Forbids.Contains("targona.condemned"),
            "The laboratory primer left her list, became inline, or no longer comes before the blow.");
        foreach (var s in new[] { furlough, second, freeFurlough, ward, quiet })
            check(s.InteractionHub == "targona.presence" && s.ContactUnit == Unit && Rules.IsPresenceHubScene(s)
                  && s.Chapters.SequenceEqual(new[] { 3, 5 }) && !Rules.IsRemote(s), "An in-person beat left the infirmary: " + s.Id);
        foreach (var s in new[] { lateLight, oneSoul, spent })
            check(Rules.IsRemote(s), "A letter is physical: " + s.Id);
        check(oneSoul.Chapters.SequenceEqual(new[] { 3 }) && oneSoul.DelayHours == 72 && longSleep.Chapters.SequenceEqual(new[] { 5 })
              && Rules.IsRemote(longSleep), "The ring payoff (Chapter 3, three nights) or its Abyss variant (Chapter 5) has the wrong window.");
        foreach (var s in new[] { oneSoul, longSleep, lateLight })
            check(!s.TricksterDevice, "A retired killed-state scene is still advertised as a device: " + s.Id);
        var rel = story.Relationships["targona"];
        check(rel.UnavailableOverrides["targona.dead_lab"] == P + "returned" && rel.TricksterAccess.Count == 1
              && !rel.TricksterAccess.ContainsKey("targona.dead_lab")
              && rel.TricksterAccess["freed_in_heaven"].Device == P + "free.spent_light"
              && rel.CommittedFlag == Committed && rel.ClosedFlag == Closed, "Targona's relationship patch is wrong.");
        check(story.Presences.TryGetValue("targona.presence", out var presence) && presence.Unit == Unit && presence.Mode == "spawn-copy"
              && presence.At?.NearUnit == Quartermaster && presence.At.Offset != null && presence.At.Offset[0] == -3f && presence.At.Offset[1] == -6f && presence.Dialog == "hub"
              && presence.Forbids.Contains(Closed) && presence.MinChapter == 3 && presence.MaxChapter == 5
              && presence.Requires.Contains(P + "in_drezen"), "Her presence among the cots is missing or malformed.");
        check(!story.Presences.Any(p => p.Key != "targona.presence" && p.Value.At?.NearUnit == Quartermaster && p.Value.At.Side == "behind"),
            "Targona's copy would stand where another presence stands behind the quartermaster.");

        // Trk_Targona_Setup (quality pass Q6 r3): the killed state has no device. Native [Attack] starts a real, lethal fight;
        // no primer can survive it without a raise (Irabeth's is the campaign's one) or an interception of native combat. The
        // attack is the Commander's own choice against a non-partner, so canon stands (11-ROSTER-PLAN-2 section 5 ruling #2).
        // Every primer and payoff keeps its id and is unreachable; her Trickster route is the freed state.
        check(story.InventoryItems["targona.abyss_key_held"] == "b5b0214f3ce3ded42a62094b87a434dd", "The Suture's key is not read natively.");
        var labWorlds = new[] { World(story, 3, "trickster", "trickster.ever", "targona.abyss_key_held"),
                                World(story, 3, "trickster", "trickster.ever", "trickster.umd_tier2", "targona.abyss_key_held"),
                                World(story, 3, "trickster", "trickster.ever") };
        foreach (var id in new[] { "dead.setup", "dead.setup_open", "dead.setup_sleep", "dead.late_light", "dead.late_crypt", "dead.one_soul", "dead.long_sleep" })
            foreach (var w in labWorlds.Concat(new[] { World(story, 3, "trickster", "trickster.ever", "targona.dead_lab", "targona.abyss_key_held"),
                                                      World(story, 5, "trickster", "trickster.ever", "targona.dead_lab", "targona.abyss_key_held") }))
                check(!Rules.Available(story, S(P + id), w), "A retired killed-state scene is still reachable: " + id);
        check(!story.Scenes.Where(s => s.Relationship == "targona" && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal))
                  .Where(s => labWorlds.Any(w => Rules.Available(story, s, w)))
                  .SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Any(c => c.Set.Contains(P + "primed") || c.Set.Contains(P + "cost.her_sleep")),
            "A laboratory primer still sets the killed-state flags.");
        // The late romance ending stages its own threshold (Directive 12) for a met-only or washed history that never played the ward.

        // Trk_Targona_KilledUnprimed (Q6): an [Attack] is the Commander's own choice of a non-partner's death and stands
        // (11-ROSTER-PLAN-2 section 5 ruling #2). No device, no raise; the no-kill branch ([Destroy the barrier]) stays open until then.
        foreach (var ch in new[] { 3, 5 })
        {
            var unprimed = World(story, ch, "trickster", "trickster.ever", "targona.dead_lab", "targona.abyss_key_held");
            check(!story.Scenes.Any(s => s.Relationship == "targona" && !s.Reaction && s.TricksterDevice && Rules.Available(story, s, unprimed))
                  && !Reaches(unprimed, Committed), "A laboratory kill is reversed after all (chapter " + ch + ").");
        }
        check(Rules.Available(story, spent, World(story, 3, "trickster", "trickster.ever", "targona.free", "targona.abyss_key_held")),
            "The freed state does not open after [Destroy the barrier].");

        // Trk_Targona_Furlough: the return beat never commits; the truth forgives, the joke and the lie do not.
        var back = World(story, 5, "trickster", "trickster.ever", "targona.dead_lab", P + "returned", P + "cost.struck_down");
        check(Rules.Available(story, furlough, back), "Trk_Targona_Furlough: unavailable.");
        var forgiven = After(furlough, back, "truth", 0);
        check(forgiven.Has(P + "forgiven") && !forgiven.Has(Committed), "Trk_Targona_Furlough: flags.");
        check(!furlough.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed)), "The return beat commits.");
        // Sol quality pass (BEL): forgiveness alone no longer opens the vigil; she first asks the Commander's hands to wash a
        // dead soldier with her (after.the_washing), and the ward waits four days on that.
        var washing = S(P + "after.the_washing");
        check(!Rules.Available(story, ward, Later(story, forgiven, 500)) && !Rules.Available(story, washing, Later(story, forgiven, 47))
              && Rules.Available(story, washing, Later(story, forgiven, 48)), "Trk_Targona_Furlough: the washing does not follow forgiveness.");
        check(washing.InteractionHub == "targona.presence" && washing.ContactUnit == Unit && Rules.IsPresenceHubScene(washing),
            "The washing left the ward.");
        var shirked = Program.Walk(washing, Later(story, forgiven, 48)).Where(o => !o.Has(P + "washed_the_dead")).ToList();
        check(shirked.Count > 0 && shirked.All(o => !o.Has(washing.Id) && !o.Has(Closed)), "Sending for a chaplain closes the washing for good.");
        var washed = After(washing, Later(story, forgiven, 48), "after", 0);
        check(Rules.Available(story, ward, Later(story, washed, 96)) && !Rules.Available(story, ward, Later(story, washed, 95)),
            "Trk_Targona_Furlough: the ward ignores its four days.");
        check(!Rules.Available(story, washing, World(story, 5, "trickster", "trickster.ever", "targona.free", P + "met")),
            "The freed state is asked to wash a body it never struck.");
        var joked = After(furlough, back, "joke", 0);
        check(joked.Has(P + "cost.unforgiven") && !Rules.Available(story, ward, Later(story, joked, 200))
              && Rules.Available(story, second, Later(story, joked, 96)), "The glib answer does not lead to the second asking.");
        var lied = After(furlough, back, "lie", 0);
        check(lied.Has(P + "cost.unforgiven") && lied.Has(P + "cost.lied"), "The lie is not recorded.");
        var sorry = After(second, Later(story, joked, 96), "sorry", 0);
        check(sorry.Has(P + "forgiven") && Reaches(sorry, Committed), "The apology does not reopen the ward.");
        var sent = After(second, Later(story, joked, 96), "start", 1);
        check(sent.Has(Closed) && !sent.Has("seelah.closed") && !sent.Has("sosiel.closed"), "Sending her away closes the wrong thing.");

        // Trk_Targona_Commit: the named producer, then the night.
        var ready = World(story, 5, "trickster", "trickster.ever", "targona.dead_lab", P + "returned", P + "forgiven", P + "washed_the_dead");
        check(Rules.Available(story, ward, ready) && !Rules.Available(story, quiet, ready), "Trk_Targona_Commit: availability.");
        var committed = After(ward, ready, "dawn", 0);
        check(committed.Has(Committed), "Trk_Targona_Commit: flags.");
        var nightPages = new HashSet<string>();
        Program.Walk(ward, ready, (page, _) => nightPages.Add(page));
        check(nightPages.Contains("threshold") && nightPages.Contains("morning")
              && Program.Walk(ward, ready).Any(o => o.Has(Committed) && o.Has(P + "night_kept")),
            "The commit has no night (Directive 12).");
        check(ward.Nodes.Single(n => n.Id == "threshold").Choices.All(c => c.Next == "morning"),
            "The threshold does not cut to the morning.");
        var left = Program.Walk(ward, ready).Where(o => o.Has(P + "cost.left_the_ward")).ToList();
        check(left.Count > 0 && left.All(o => o.Has(Closed) && !o.Has(Committed)), "Leaving before dawn does not close her route.");

        // Trk_Targona_Declined: her soft no, and the priced second ask.
        var metOnly = World(story, 5, "trickster", "trickster.ever", "targona.free", P + "met", P + "cost.wand_unspent", P + "primed", P + "free.spark");
        // Polish r4 (BEL): the freed-state vigil waits on the stove's earned attraction; answering it as colleagues keeps friendship.
        var stove = S(P + "free.the_stove");
        var metNoSpark = World(story, 5, "trickster", "trickster.ever", "targona.free", P + "met", P + "cost.wand_unspent", P + "primed");
        check(!Rules.Available(story, ward, metNoSpark) && Rules.Available(story, stove, metNoSpark), "The vigil opens without the stove.");
        var stoveOut = Program.Walk(stove, metNoSpark).ToList();
        check(stoveOut.Any(o => o.Has(P + "free.spark")) && stoveOut.Any(o => o.Has(P + "free.colleagues") && !o.Has(P + "free.spark"))
              && stoveOut.All(o => !o.Has(Committed) && !o.Has(Closed)), "The stove forces or forbids the attraction.");
        foreach (var answer in new[] { "truth", "lie", "hers" })
        {
            var stovePages = new HashSet<string>();
            Program.Walk(stove, metNoSpark, (page, _) => stovePages.Add(page));
            check(stovePages.Contains(answer), "The stove loses an answer: " + answer);
        }
        check(stoveOut.Where(o => o.Has(P + "free.colleagues")).All(o => !Rules.Available(story, ward, Later(story, o, 200))),
            "Colleagues at the stove still reach the vigil.");
        // r5: both orders stay open (the letters move to the ward after the meeting; see TargonaOpeningTests), and an angel
        // already writing from the wayhouse greets the Commander as her correspondent, not as a stranger from Heaven.
        check(Rules.Available(story, S("targona.unasked_question"), World(story, 5, "trickster", "trickster.ever", "targona.free",
                  "targona.ran_treatment_completed", "targona.ran_final_seen", "targona.ran_none", P + "met"))
              && Rules.Available(story, spent, World(story, 5, "trickster", "trickster.ever", "targona.free", "targona.correspondence_opened")),
            "One order of letters and ward closes the other.");
        var wayhousePages = new HashSet<string>();
        var wayhouseNight = World(story, 5, "trickster", "trickster.ever", "targona.free", P + "cost.wand_unspent", "targona.ran_treatment_completed",
            "targona.correspondence_opened");
        Program.Walk(freeFurlough, wayhouseNight, (page, _) => wayhousePages.Add(page));
        check(wayhousePages.Contains("greet_wayhouse") && !wayhousePages.Contains("greet_treated") && !wayhousePages.Contains("greet"),
            "The wayhouse correspondent arrives as if from Heaven.");
        check(Rules.Available(story, ward, metOnly), "Trk_Targona_Declined: the ward is closed to the freed state.");
        var declined = After(ward, metOnly, "refused", 0);
        check(declined.Has(P + "declined") && !declined.Has(Committed) && !declined.Has(Closed), "Trk_Targona_Declined: flags.");
        check(!Rules.Available(story, ward, Later(story, declined, 200)) && Rules.Available(story, quiet, Later(story, declined, 72))
              && !Rules.Available(story, quiet, Later(story, declined, 71)), "Trk_Targona_Declined: the quiet ward does not follow.");
        var sealedYes = After(quiet, Later(story, declined, 72), "start", 0);
        check(sealedYes.Has(Committed) && sealedYes.Has(P + "cost.light_sealed")
              && Program.Walk(quiet, Later(story, declined, 72)).Any(o => o.Has(P + "night_kept")), "Her price is not paid, or no night follows.");
        var refused = After(quiet, Later(story, declined, 72), "start", 1);
        check(refused.Has(Closed) && !refused.Has(Committed), "Refusing her price does not close her route.");
        // Polish r3 (INT/HOW): both live freed-state commitments, with their full flag histories, reach the right ending.
        var firstYes = After(ward, metOnly, "dawn", 2);
        foreach (var history in new[] { firstYes, sealedYes })
        {
            check(history.Has(Committed), "A freed-state commitment did not commit.");
            var died = World(story, 6, history.Flags.Concat(new[] { "sacrifice" }).ToArray());
            var cameBack = World(story, 6, history.Flags.Concat(new[] { "sacrifice", "ending.trickster" }).ToArray());
            var lived = World(story, 6, history.Flags.ToArray());
            check(Rules.Available(story, S(P + "epilogue.sacrifice"), died) && !Rules.Available(story, epFurlough, died),
                "An unsurvived sacrifice after a live commitment has no mourning page.");
            check(Rules.Available(story, epFurlough, cameBack) && !Rules.Available(story, S(P + "epilogue.sacrifice"), cameBack)
                  && Rules.Available(story, epFurlough, lived) && !Rules.Available(story, epDeclined, lived),
                "A surviving committed Commander gets the wrong page.");
        }
        // Polish r3: the captives memory is delivered after their departure cue, so it never stages the cellar door.

        // Trk_Targona_Free: the wand that does not run down.
        var free = World(story, 5, "trickster", "trickster.ever", "targona.free", "trickster.umd_tier2");
        check(Rules.Available(story, spent, free) && !Rules.Available(story, oneSoul, free) && !Rules.Available(story, lateLight, free),
            "Trk_Targona_Free: availability.");
        var wand = spent.Nodes.Single(n => n.Id == "start").Choices[0];
        check(wand.Crusade?.Resource == "Favors" && wand.Crusade.Amount == -300 && wand.Mythic == "PlayerIsTrickster", "The wand night lost its joke or its cost.");
        var night = After(spent, free, "night", 0);
        check(night.Has(P + "primed") && night.Has(P + "cost.wand_unspent"), "Trk_Targona_Free: flags.");
        check(Rules.Available(story, freeFurlough, night), "Trk_Targona_Free: she does not come.");
        var freeNoTrick = World(story, 5, "trickster", "trickster.ever", "targona.free");
        var spentAll = After(spent, freeNoTrick, "night_spent", 0);
        check(spent.Nodes.Single(n => n.Id == "start").Choices.Single(c => c.Next == "night_spent").Crusade?.Resource == "Finances"
              && spentAll.Has(P + "cost.charges_spent") && Rules.Available(story, freeFurlough, spentAll) && !Program.Walk(spent, freeNoTrick)
                  .Any(o => o.Has(P + "cost.wand_unspent") && !o.Has(P + "cost.charges_spent")),
            "Without the trick, the wand night is free or claims an unspent wand.");
        var met = After(freeFurlough, night, "why", 0);
        check(met.Has(P + "met") && met.Has("targona.started") && Reaches(met, Committed), "Trk_Targona_Free: the commit is unreachable.");
        var labPages = new HashSet<string>();
        var toldFree = Program.Copy(night); toldFree.Flags.Add(P + "told_in_lab");
        Program.Walk(freeFurlough, toldFree, (page, _) => labPages.Add(page));
        check(labPages.Contains("greet_lab") && !labPages.Contains("greet"), "She forgets the barrier.");

        // PP7 (Chapter 4): Latverk's freed captives sent to the camp (Latverk_Final Cue_0039); the memory, then her answer at
        // the cots in Chapter 5.
        var birds = S(P + "free.little_birds");
        var names = S(P + "free.the_names");
        string[] nameVariants = { P + "free.names_asked", P + "free.names_tended", P + "free.names_unasked" };
        string[] nameAnswers = { "list", "tended", "unasked" };
        check(birds.Remote && birds.Kind == "memory" && birds.Chapters.SequenceEqual(new[] { 4 }) && birds.MinChapter == 4 && birds.MaxChapter == 4
              && birds.Relationship == "targona" && new[] { "trickster.ever", P + "met", "targona.aasimar_sent.latched" }.All(birds.Requires.Contains)
              && story.Latches["targona.aasimar_sent.latched"].SequenceEqual(new[] { "targona.aasimar_sent" })
              && birds.Forbids.Contains(Closed) && story.SeenCues["targona.aasimar_sent"].SequenceEqual(new[] { "a3ca33a66c286b24493176d00a9a7527" })
              && !names.Remote && names.Chapters.SequenceEqual(new[] { 5 }) && names.ContactUnit == Unit && names.InteractionHub == "targona.presence"
              && names.Relationship == "targona" && names.Forbids.Contains(Closed),
            "Heaven's blood lost its shape (a Chapter 4 memory after the captives are sent; her answer in person in Chapter 5).");
        // In the Abyss, not Drezen: a remote memory must carry no area restriction (Story.Available applies it).
        var abyssMet = Program.Copy(met); abyssMet.Chapter = 4; abyssMet.AvailableContacts.Clear(); abyssMet.Area = "abyss-camp";
        abyssMet = Later(story, abyssMet, 24);
        check(!Rules.Available(story, birds, abyssMet), "Heaven's blood opens before the captives are sent.");
        var seen = Program.Copy(abyssMet); seen.Flags.Add("targona.aasimar_sent"); Rules.Complete(story, seen);
        seen.Times["targona.aasimar_sent.latched"] = seen.Hour;   // Main.RecordLatches stamps the hour it first sees the cue
        check(seen.Has("targona.aasimar_sent.latched") && !Rules.Available(story, birds, seen)
              && !Rules.Available(story, birds, Later(story, seen, birds.DelayHours - 1)),
            "Heaven's blood opens before its hours have passed since the captives left (the older ward meeting must not count).");
        var sentOff = Later(story, seen, birds.DelayHours);
        check(Rules.Available(story, birds, sentOff), "Heaven's blood does not follow the captives.");
        var neverMet = Program.Copy(sentOff); neverMet.Flags.Remove(P + "met");
        check(!Rules.Available(story, birds, neverMet), "Heaven's blood opens for an angel the Commander has not met in the ward.");
        foreach (var chapter in new[] { 3, 5 })
        {
            var wrong = Program.Copy(sentOff); wrong.Chapter = chapter;
            check(!Rules.Available(story, birds, wrong), "Heaven's blood leaks into chapter " + chapter);
        }
        var birdPages = new HashSet<string>();
        var namePages = new HashSet<string>();
        var memories = Program.Walk(birds, sentOff, (page, _) => birdPages.Add(page)).Where(r => r.Has(birds.Id)).ToList();
        check(memories.Count == 3 && memories.All(r => r.Has(P + "free.names_kept") && nameVariants.Count(r.Has) == 1 && !Rules.Available(story, birds, r)),
            "Heaven's blood loses a variant, overlaps, or replays.");
        foreach (var r in memories)
        {
            var home = Program.Copy(r); home.Chapter = 5; home.Area = Drezen; home.AvailableContacts.Add(Unit);
            home = Later(story, home, names.DelayHours + 1);
            check(Rules.Available(story, names, home), "Her answer does not follow the Abyss memory.");
            var gone = Program.Copy(home); gone.AvailableContacts.Clear();
            check(!Rules.Available(story, names, gone), "Her answer opens without her at the cots.");
            var heard = Program.Walk(names, home, (page, _) =>
            {
                namePages.Add(page);
                int i = Array.IndexOf(nameAnswers, page);
                if (i >= 0) check(r.Has(nameVariants[i]), "She answers a memory the Commander does not have: " + page);
            }).Where(o => o.Has(names.Id)).ToList();
            check(heard.Count == 1 && heard.All(o => o.Has(P + "free.names_heard") && !Rules.Available(story, names, o)), "Her answer does not complete once.");
        }
        var unremembered = Later(story, met, 48);
        check(!Rules.Available(story, names, unremembered), "Her answer opens with no Abyss memory.");
        check(birdPages.SetEquals(birds.Nodes.Select(n => n.Id)) && namePages.SetEquals(names.Nodes.Select(n => n.Id)),
            "Unreached page of Heaven's blood or of her answer.");

        presence = story.Presences["targona.presence"];
        // Sol quality pass (INT 58): the freed state reaches her with no contact supplied by the fixture. The wand night
        // alone must make her copy wanted and spawnable; only then does the contact exist, and the hub walks to the commit.
        foreach (var trick in new[] { true, false })
        {
            var bare = trick ? World(story, 5, false, "trickster", "trickster.ever", "targona.free", "trickster.umd_tier2")
                             : World(story, 5, false, "trickster", "trickster.ever", "targona.free");
            check(!bare.AvailableContacts.Contains(Unit) && !Rules.PresenceWanted(presence, bare),
                "Freed state: her copy stands in the ward before the wand night.");
            var wandNight = Program.Copy(After(spent, bare, trick ? "night" : "night_spent", 0));
            Rules.Complete(story, wandNight);
            check(Rules.PresenceWanted(presence, wandNight), "Freed state: the wand night does not bring her copy to the cots.");
            check(Rules.PlanPresence(presence, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = true })
                      .SequenceEqual(new[] { PresenceStep.Spawn }), "Freed state: the wanted copy is not spawned at Wilcer's anchor.");
            check(!Rules.Available(story, freeFurlough, wandNight), "Freed state: the arrival opens without her copy.");
            var spawned = Program.Copy(wandNight);
            spawned.AvailableContacts.Add(Unit);
            Rules.Complete(story, spawned);
            check(Rules.Available(story, freeFurlough, spawned)
                  && story.Scenes.Any(s => s.InteractionHub == "targona.presence" && Rules.Available(story, s, spawned)),
                "Freed state: the spawned copy's hub offers no arrival (Main.CanOpenPresenceHub would refuse the click).");
            var arrived = Program.Copy(After(freeFurlough, spawned, "why", 0));
            Rules.Complete(story, arrived);
            check(arrived.Has(P + "met") && Rules.PresenceWanted(presence, arrived), "Freed state: the arrival does not keep her at the cots.");
            // Polish r4: the stove comes between the arrival and the vigil.
            check(!Rules.Available(story, ward, Later(story, arrived, 200)) && Rules.Available(story, S(P + "free.the_stove"), Later(story, arrived, 48)),
                "Freed state: the vigil skips the stove.");
            var sparked = After(S(P + "free.the_stove"), Later(story, arrived, 48), "stove", 0);
            Rules.Complete(story, sparked);
            var wardNight = Later(story, sparked, 96);
            check(sparked.Has(P + "free.spark") && Rules.Available(story, ward, wardNight), "Freed state: the ward does not follow the stove.");
            var freePages = new HashSet<string>();
            Program.Walk(ward, wardNight, (page, _) => freePages.Add(page));
            check(freePages.Contains("yes_free") && !freePages.Contains("yes") && freePages.Contains("refused_dawn"),
                "Freed state: the ward's yes remembers the death branch, or the dawn question has no answer of its own.");
            check(Program.Walk(ward, wardNight).Any(o => o.Has(Committed) && o.Has(P + "night_kept")), "Freed state: no commit and night.");
        }
        var deathPages = new HashSet<string>();
        Program.Walk(ward, ready, (page, _) => deathPages.Add(page));
        check(deathPages.Contains("yes") && !deathPages.Contains("yes_free"), "Death branch: the freed yes plays after a raise.");
        var wardNodes = ward.Nodes.ToDictionary(n => n.Id);
        check(wardNodes["dawn"].Choices[1].Next == "refused_dawn" && wardNodes["start"].Choices[1].Next == "refused",
            "The dawn question's refusal contradicts the sleeping sergeant.");
        // The Chapter 3 laboratory memory holds nothing from a later chapter or another mythic path (the Angel Nexus).

        // Q6 r4 (TRK/BEL): the late romance needs her to have stayed because the Commander asked; a charitable welcome is a colleague.
        var epColleague = S(P + "epilogue.colleague");
        // Play every stove answer through both exits, then read the colleague ending's conditional history.
        const string PikemanLie = P + "free.pikeman_lied";
        var stoveNight = After(spent, free, "night", 0);
        var stoveArrival = After(freeFurlough, stoveNight, "why", 0);
        var stoveReady = Later(story, stoveArrival, stove.DelayHours);
        check(Rules.Available(story, stove, stoveReady), "The played wand night and arrival cannot reach the stove.");
        foreach (int answer in new[] { 0, 1, 2 })
        {
            var outcomes = Program.WalkVia(stove, stoveReady, "start", answer);
            check(outcomes.Count == 2 && outcomes.All(o => o.Has(PikemanLie) == (answer == 1)),
                "The stove fails to record only the pikeman lie, on both exits.");
            foreach (var colleague in outcomes.Where(o => o.Has(P + "free.colleagues")))
            {
                var ending = World(story, 6, colleague.Flags.ToArray());
                check(Rules.Available(story, epColleague, ending), "The played stove colleague history loses its ending.");
                var paragraphs = Rules.VisibleParagraphs(epColleague.Nodes[0], ending);
                check(paragraphs.Any(p => SurfaceIds.Has(SurfaceIds.Of(story, p), "[targona.trickster.epilogue.colleague/end/paragraph/2]")) == (answer == 1),
                    "The colleague ending erases or invents the disagreement over the dying pikeman.");
            }
        }
        var welcomed6 = World(story, 6, "trickster", "trickster.ever", "targona.free", P + "met", P + "cost.wand_unspent");
        var drawn6 = World(story, 6, "trickster", "trickster.ever", "targona.free", P + "met", P + "drawn", P + "free.spark", P + "cost.wand_unspent");
        var drawnOnly6 = World(story, 6, "trickster", "trickster.ever", "targona.free", P + "met", P + "drawn", P + "cost.wand_unspent");
        check(!drawnOnly6.Has(P + "late_committed") && Rules.Available(story, epColleague, drawnOnly6) && !Rules.Available(story, epCommit, drawnOnly6),
            "An asked-for stay without the stove's attraction becomes a romance at the war's end.");
        check(!welcomed6.Has(P + "late_committed") && !Rules.Available(story, epCommit, welcomed6) && !Rules.Available(story, epFurlough, welcomed6)
              && Rules.Available(story, epColleague, welcomed6)
              && drawn6.Has(P + "late_committed") && Rules.Available(story, epCommit, drawn6) && !Rules.Available(story, epColleague, drawn6),
            "A charitable welcome becomes a romance at the war's end, or the asked-for stay does not.");
        var greetNode = freeFurlough.Nodes.Single(n => n.Id == "why").Choices;
        check(greetNode.Count == 2 && greetNode[0].Set.Contains(P + "met") && !greetNode[0].Set.Contains(P + "drawn") && greetNode[1].Set.Contains(P + "drawn"),
            "The arrival's romantic answer is not an appended, recorded choice.");
        check(spent.Nodes.Single(n => n.Id == "night_spent").Choices[0].Forbids.Contains("herald.killed") && spent.Nodes.Single(n => n.Id == "night_spent").Choices[1].Requires.Contains("herald.killed") && story.Etudes["herald.killed"] == "348dfb40784b436cbe21347f8e0f08ce",
            "The ordinary wands reach Heaven by no named road, or by the Hand after HeraldKilled.");
        var heraldDead = World(story, 5, "trickster", "trickster.ever", "targona.free", "herald.killed");
        var hp = new HashSet<string>(); Program.Walk(spent, heraldDead, (page, _) => hp.Add(page));
        check(hp.Contains("report_chapel") && !hp.Contains("report_hand")
              && Program.Walk(spent, heraldDead).Any(o => o.Has(P + "cost.charges_spent")), "The dead Hand still reads the report.");

        // Q6 r6 (BEL/CAN): the freed ward has a reactor; the correspondence names no Hand (captive or dead in many histories).
        check(Rules.Available(story, S(P + "react.seelah_ward_free"), World(story, 5, "trickster", "trickster.ever", "targona.free", P + "met", P + "night_kept"))
              && !Rules.Available(story, S(P + "react.seelah_ward_free"), World(story, 5, "trickster", "trickster.ever", "targona.free", P + "met")),
            "The freed ward's night has no companion response.");

        // Trk_Targona_TreatmentDone: a treatment that ended as RanRomance's romance runs the parent route instead. A friendship-only
        // treatment history (Sol quality pass, INT) can still be courted: walk it from the parent's own flags, no injected romance.
        var treatedRomance = World(story, 5, "trickster", "trickster.ever", "targona.free", "targona.ran_treatment_completed", "targona.ran_romance");
        check(treatedRomance.Has(P + "parent_romanced") && !Rules.Available(story, spent, treatedRomance)
              && !Rules.Available(story, lateLight, treatedRomance), "Trk_Targona_TreatmentDone.");
        var treatedFriend = World(story, 5, false, "trickster", "trickster.ever", "targona.free", "targona.ran_treatment_completed",
                                  "trickster.umd_tier2");
        check(!treatedFriend.Has(P + "parent_romanced") && Rules.Available(story, spent, treatedFriend),
            "A friendship-only treatment history has no Trickster courtship.");
        var friendNight = Program.Copy(After(spent, treatedFriend, "night", 0));
        friendNight.AvailableContacts.Add(Unit);
        Rules.Complete(story, friendNight);
        var friendPages = new HashSet<string>();
        Program.Walk(freeFurlough, friendNight, (page, _) => friendPages.Add(page));
        check(Rules.Available(story, freeFurlough, friendNight) && friendPages.Contains("greet_treated") && !friendPages.Contains("greet"),
            "The treated angel greets her physician as a stranger.");
        check(Reaches(After(freeFurlough, friendNight, "why", 0), Committed), "A friendship-only treatment history cannot commit.");

        // RanRomance's own romance (parent treatment completed as a romance) reaches the Last Call coda and the household.
        var lcTargona = S("targona.lastcall.page");
        check(lcTargona.RequiresAnyGroups.Length == 1 && lcTargona.RequiresAnyGroups[0].Contains("targona.committed")
              && lcTargona.RequiresAnyGroups[0].Contains(P + "parent_romanced") && treatedRomance.Has(P + "parent_romanced"),
            "The parent romance never reaches Targona's coda.");
        check(lcTargona.RequiresAnyGroups[0].Contains(P + "late_committed"), "The late commitment (met, or washed) never reaches Targona's coda.");
        var lcParas = lcTargona.Nodes[0].Paragraphs;
        check(lcParas.Single(q => q.Requires.Contains(P + "cost.unforgiven") && !q.Requires.Contains(P + "forgiven")).Forbids.Contains(P + "forgiven")
              && lcParas.Any(q => q.Requires.Contains(P + "cost.unforgiven") && q.Requires.Contains(P + "forgiven")),
            "A forgiven Targona is still at the far end of every room.");
        var eligibleGroups = story.Derived["targona.harem.eligible"];
        check(eligibleGroups.Any(g => g.Length == 1 && g[0] == P + "parent_romanced"), "The parent romance is not a household partner.");
        // The laboratory death: TargonaIsWasKilledInAreeluLab starts at the [Attack] cue, and the native game itself reads it as her
        // death (Epilogues/Cue_0531, ThresholdCamp_Scripts03). The fight it begins has no surrender and no exit, so a world with
        // the etude and a living angel is not a native state; no fixture pretends otherwise.

        // Trk_Targona_Epilogue_Late and the siblings.
        // Sol quality pass (BEL): on the killed branch the late commitment needs the washing, as the vigil does; forgiveness
        // alone is an ally's ending.
        var late6 = World(story, 6, "trickster", "trickster.ever", P + "forgiven", P + "washed_the_dead");
        check(Rules.Available(story, epCommit, late6) && !Rules.Available(story, epDeclined, late6), "Trk_Targona_Epilogue_Late.");
        check(Rules.Available(story, epFurlough, late6), "The late commit has no furlough page.");
        var epAlly = S(P + "epilogue.ally");
        var forgivenOnly6 = World(story, 6, "trickster", "trickster.ever", P + "forgiven");
        check(!forgivenOnly6.Has(P + "late_committed") && !Rules.Available(story, epCommit, forgivenOnly6)
              && !Rules.Available(story, epFurlough, forgivenOnly6) && Rules.Available(story, epAlly, forgivenOnly6)
              && !Rules.Available(story, epAlly, late6), "Forgiveness without the washing is a romance ending.");
        // Unprepared returns never recall a promise made at the barrier.
        var furloughPages = new HashSet<string>();
        Program.Walk(furlough, World(story, 5, "trickster", "trickster.ever", "targona.dead_lab", P + "returned", P + "cost.struck_down", P + "cost.raised_the_hard_way"),
            (page, _) => furloughPages.Add(page));
        check(furloughPages.Contains("pikeman_late") && !furloughPages.Contains("pikeman"),
            "An unprepared return recalls a promise she never made.");
        var toldPages = new HashSet<string>();
        Program.Walk(furlough, World(story, 5, "trickster", "trickster.ever", "targona.dead_lab", P + "returned", P + "cost.struck_down", P + "cost.she_told_heaven"),
            (page, _) => toldPages.Add(page));
        check(toldPages.Contains("pikeman") && !toldPages.Contains("pikeman_late"), "The promised report is lost.");
        // The wand stays the Commander's gift; the promise's paragraph follows what Last Call recorded.
        var furloughParas = epFurlough.Nodes[0].Paragraphs;
        check(furloughParas.Single(q => q.Requires.Contains(P + "cost.light_sealed") && !q.Requires.Contains("targona.lastcall.called")).Forbids.Contains("targona.lastcall.called") && furloughParas.Any(q => q.Requires.Contains(P + "cost.light_sealed") && q.Requires.Contains("targona.lastcall.called")),
            "The kept-promise paragraph survives a recorded breach, or the wand runs on without the Commander.");
        var wed6 = World(story, 6, "trickster", "trickster.ever", P + "forgiven", Committed);
        check(!Rules.Available(story, epCommit, wed6) && Rules.Available(story, epFurlough, wed6), "A committed Targona gets the late page.");
        var no6 = World(story, 6, "trickster", "trickster.ever", P + "met", P + "declined");
        check(Rules.Available(story, epDeclined, no6) && !Rules.Available(story, epCommit, no6) && !Rules.Available(story, epFurlough, no6),
            "The declined page is wrong.");
        var shut6 = World(story, 6, "trickster", "trickster.ever", P + "forgiven", Closed);
        check(!Rules.Available(story, epCommit, shut6) && !Rules.Available(story, epFurlough, shut6), "A closed route gets a page.");
        // The Commander's sacrifice: no reunion unless the Commander came back (trickster.commander_back); otherwise her own page.
        var epSacrifice = S(P + "epilogue.sacrifice");
        var lost6 = World(story, 6, "trickster", "trickster.ever", P + "forgiven", Committed, "sacrifice");
        check(!Rules.Available(story, epFurlough, lost6) && !Rules.Available(story, epCommit, World(story, 6, "trickster", "trickster.ever", P + "forgiven", "sacrifice"))
              && Rules.Available(story, epSacrifice, lost6), "An unsurvived sacrifice still gets the reunion.");
        var back6 = World(story, 6, "trickster", "trickster.ever", P + "forgiven", Committed, "sacrifice", "ending.trickster");
        check(back6.Has("trickster.commander_back") && Rules.Available(story, epFurlough, back6) && !Rules.Available(story, epSacrifice, back6),
            "A Commander who came back is mourned.");
        check(!Rules.Available(story, epSacrifice, wed6), "The sacrifice page plays without a sacrifice.");
        // Polish: an unsurvived sacrifice gets no living-recipient letter; a refused promise is not a postponement.
        var epColleague2 = S(P + "epilogue.colleague");
        var epColleagueLost = S(P + "epilogue.colleague_lost");
        var epRefused = S(P + "epilogue.refused_promise");
        var metLost6 = World(story, 6, "trickster", "trickster.ever", P + "met", "sacrifice");
        check(!Rules.Available(story, epColleague2, metLost6) && Rules.Available(story, epColleagueLost, metLost6),
            "The colleague's invitation reaches a Commander who died at the Threshold.");
        var metBack6 = World(story, 6, "trickster", "trickster.ever", P + "met", "sacrifice", "ending.trickster");
        check(Rules.Available(story, epColleague2, metBack6) && !Rules.Available(story, epColleagueLost, metBack6),
            "A Commander who came back loses the colleague's letter.");
        check(!Rules.Available(story, epAlly, World(story, 6, "trickster", "trickster.ever", P + "forgiven", "sacrifice")), "The ally page ignores the sacrifice.");
        var refusedHistory = After(quiet, Later(story, declined, 72), "start", 1);
        var refused6 = World(story, 6, refusedHistory.Flags.ToArray());
        check(refusedHistory.Has(Closed) && !Rules.Available(story, epDeclined, refused6) && Rules.Available(story, epRefused, refused6)
              && !Rules.Available(story, epRefused, no6), "A refused promise reads as an open question, or the open question reads as refused.");
        foreach (var page in new[] { epCommit, epDeclined, epFurlough, epSacrifice, epColleague2, epColleagueLost, epAlly, epRefused })
            check(page.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0), "An epilogue page has effects: " + page.Id);

        // Reactions: exactly Seelah, Sosiel and Ember; guarded; never touching another relationship.
        var reactions = story.Scenes.Where(s => s.Relationship == "targona" && s.Reaction).ToList();
        check(reactions.Select(s => s.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Ember", "Seelah", "Sosiel" }),
            "Targona's reactors are not exactly Seelah, Sosiel and Ember.");
        // Ember reports only the history the player made: the unspent wand, the three emptied wands, or the raised angel's bandages.
        var eWand = S(P + "react.ember_wand"); var eEmpty = S(P + "react.ember_empty_wands"); var eBandage = S(P + "react.ember_bandages");
        var quietWand = World(story, 5, "trickster", "trickster.ever", "targona.free", P + "cost.wand_unspent");
        var emptied = World(story, 5, "trickster", "trickster.ever", "targona.free", P + "cost.wand_unspent", P + "cost.charges_spent");
        var raisedAngel = World(story, 5, "trickster", "trickster.ever", "targona.dead_lab", P + "returned");
        check(Rules.Available(story, eWand, quietWand) && !Rules.Available(story, eEmpty, quietWand) && !Rules.Available(story, eBandage, quietWand)
              && !Rules.Available(story, eWand, emptied) && Rules.Available(story, eEmpty, emptied) && !Rules.Available(story, eBandage, emptied)
              && !Rules.Available(story, eWand, raisedAngel) && !Rules.Available(story, eEmpty, raisedAngel) && Rules.Available(story, eBandage, raisedAngel),
            "Ember reports a wand history the player never made.");
        foreach (var e in new[] { eWand, eEmpty, eBandage })
            check(e.Forbids.Contains("ember_dead") && e.Forbids.Contains("ember_gone"),
                "Ember's reaction is unguarded or romantic: " + e.Id);
        check(S(P + "react.seelah_furlough").Forbids.Contains("seelah_dead") && S(P + "react.seelah_furlough").Forbids.Contains("seelah_gone")
              && S(P + "react.sosiel_forgiven").Forbids.Contains("sosiel.dead") && S(P + "react.sosiel_forgiven").Forbids.Contains("sosiel.kicked_out")
              && S(P + "react.ember_wand").Forbids.Contains("ember_dead") && S(P + "react.ember_wand").Forbids.Contains("ember_gone"),
            "A reaction is not guarded against its reactor's absence.");
        check(Rules.Available(story, S(P + "react.seelah_furlough"), back) && !Rules.Available(story, S(P + "react.seelah_furlough"),
              World(story, 5, "trickster", "trickster.ever", P + "returned", "seelah_dead")), "Seelah's reaction is wrong.");
        // G6(b): Seelah back on her own Trickster route lifts her death or departure for this bark.
        check(Rules.Available(story, S(P + "react.seelah_furlough"), World(story, 5, "trickster", "trickster.ever", P + "returned", "seelah_dead", "seelah.trickster.returned"))
              && Rules.Available(story, S(P + "react.seelah_furlough"), World(story, 5, "trickster", "trickster.ever", P + "returned", "seelah_gone", "seelah.trickster.returned")),
            "Seelah's reaction ignores her Trickster return.");
        check(!reactions.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(),
            "A reaction sets state.");
        var ember = S(P + "react.ember_wand").Nodes[0].Text;
        check(!new[] { "kiss", "love", "beautiful", "darling" }.Any(w => ember.Contains(w, StringComparison.OrdinalIgnoreCase)),
            "Ember's reaction has romantic framing.");

        // Coexistence: no Targona scene requires another romanceable character's death, departure or closure.
        foreach (var s in story.Scenes.Where(s => s.Id.StartsWith(P, StringComparison.Ordinal)))
            check(!s.Requires.Any(f => f.EndsWith(".closed", StringComparison.Ordinal) && f != Closed
                                   || f.EndsWith("_dead", StringComparison.Ordinal) || f.EndsWith("_gone", StringComparison.Ordinal)),
                "A Targona scene requires another character's loss: " + s.Id);
        Console.WriteLine("PASS: Targona Trickster (Trk_Targona_*): the lab primer, the late light, one soul, the furlough, the ward and the wand.");
    }
}
