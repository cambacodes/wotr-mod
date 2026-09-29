using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Shamira, Trickster (Writer/handoffs/11-ROSTER-PLAN-2.md §2, "Dreams for a body", as revised by the coordinator on
// 2026-09-29: the flask capture is dropped; spec trickster/shamira.md for hooks). One block per rules test (Trk_Shamira_*):
// the Chapter 4 seeds on her own audience list, the earning (a native answer that let her in, or the Commander's open mind),
// the door left open at Socothbenoth's briefing (or opened blind), her first words at his closet and their letter twin, the
// late road (she drowns in the Commander's head), the nights behind the Commander's eyes, the theft, the fuel (her evil
// demand), the waking and its cost (never dreaming alone), the game lost on purpose and its two no's, Nocticula's court scene,
// the reactions, the pages, and Areelu's flask left untouched for Last Call in one all-romance run.
internal static class ShamiraTricksterTests
{
    private const string P = "shamira.trickster.";
    private const string Hub4 = "d138954fd7cdb2d4e90bb28cbd76235e";
    private const string Hub4Return = "64fdd0fed0509db42b073f8ef7503d45";
    private const string Briefing = "5266a3d8bc5b0714eaaf77dfa5c20695";
    private const string BriefingReturn = "2f4be0bde527a7d4cb7c73131ab551db";
    private const string Closet = "db7f69fa013c7ec49b651e7ad26c67de";
    private const string ClosetReturn = "e52a1d81a098a2843aa5f1f35481ddc1";
    private const string Audience = "2729c49e2bf20c64caa4f54b352e03f6";
    private const string Reported = "84df3b227f54e3e44888b5bb8585089d";
    private const string SoulJar = "f0641f67501a4084897d9bcbc00ddc99";
    private const string Killed = "shamira.killed";
    private const string Primed = P + "primed";
    private const string Heard = P + "heard";
    private const string Returned = P + "returned";
    private const string Embodied = P + "embodied";
    private const string NeverAlone = P + "cost.never_alone";
    private const string Committed = "shamira.committed";
    private const string Closed = "shamira.closed";
    private const string LcPrimed = "trickster.lastcall.primed.bottle";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later);
        foreach (var flag in later.Flags.Where(f => !later.Times.ContainsKey(f)).ToList()) later.Times[flag] = state.Hour;
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Avail(Scene s, Snapshot w) => Rules.Available(story, s, w);
        Choice Ch(Scene s, string node, int index) => s.Nodes.Single(n => n.Id == node).Choices[index];
        // Every outcome that passed through the given choice (its flags set, and the scene completed or aborted there).
        List<Snapshot> Through(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Ch(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        var mine = story.Scenes.Where(s => s.Relationship == "shamira").ToArray();
        var own = mine.Where(s => !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = mine.Where(s => s.Owner == "ShamiraEpilogue").ToArray();
        var reactions = mine.Where(s => s.Reaction).ToArray();
        // Plays every available Shamira scene forward and reports whether a flag is reachable.
        bool Reaches(Snapshot start, string flag, int chapter = 5)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 24 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    if (from.Has(flag)) return true;
                    var w = Later(story, from, 200, chapter);
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

        // Shape and hooks.
        var rel = story.Relationships["shamira"];
        check(rel.StartedFlag == "shamira.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { Killed }) && rel.UnavailableOverrides[Killed] == Returned
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "cold", "killed" })
              && rel.TricksterAccess["killed"].Device == P + "killed.voice" && rel.TricksterAccess["cold"].Device == P + "killed.drowning"
              && rel.TricksterAccess.Values.All(a => a.Returned == Returned),
            "Shamira's relationship does not match the revised 11 §2 (killed, the voice behind the eyes, returned).");
        check(!story.Presences.Keys.Any(k => k.StartsWith("shamira", StringComparison.Ordinal)),
            "Shamira spawns a presence; no Shamira unit carries a dialog, and Chapter 5 never walks Alushinyrra on this path.");
        check(story.SelectedAnswers["shamira.let_in.mine"] == "c64d3f7e4a58fad43bd2bf135ab2b29e"
              && story.SelectedAnswers["shamira.let_in.submitted"] == "d5c0eb028f41da648bfbdd5a1ac2dc97"
              && story.Derived[P + "let_in"].Length == 5,
            "The earning is not bound to her native mind-reading answers (Answer_0008, 0031, 0044, 0178) and the open mind.");
        var read = S(P + "ch4.read");
        var bird = S(P + "ch4.bird");
        foreach (var s in new[] { read, bird })
            check(s.AnswerLists.SequenceEqual(new[] { Hub4 }) && s.NativeReturnCue == Hub4Return && s.Chapters.SequenceEqual(new[] { 4 })
                  && s.Forbids.Contains(Killed) && s.Forbids.Contains("shamira.no_more_ch4") && !Rules.IsRemote(s),
                "A Chapter 4 beat is not on her own audience list, behind her death and the closed audience: " + s.Id);
        var setup = S(P + "killed.setup");
        check(setup.AnswerLists.SequenceEqual(new[] { Briefing }) && setup.NativeReturnCue == BriefingReturn
              && setup.EntryMythic == "PlayerIsTrickster" && setup.Requires.Contains("shamira.plan_known") && setup.Forbids.Contains(Killed),
            "The setup is not the Trickster's question at Socothbenoth's briefing, before the kill.");
        var voice = S(P + "killed.voice");
        var twin = S(P + "killed.voice_letter");
        var drowning = S(P + "killed.drowning");
        check(voice.AnswerLists.SequenceEqual(new[] { Closet }) && voice.NativeReturnCue == ClosetReturn && voice.TricksterDevice
              && voice.TricksterState == "killed" && twin.TricksterDevice && Rules.IsRemote(twin) && drowning.TricksterDevice
              && drowning.TricksterState == "cold" && Rules.IsRemote(drowning),
            "Her first words are not physical at Socothbenoth's closet (with a letter twin), or the late road is not a device.");

        // Trk_Shamira_FlaskUntouched: Areelu's flask is Last Call's alone.
        foreach (var s in mine.Concat(new[] { S("nocticula.trickster.court.shamira") }))
        {
            var keys = s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                .Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids).Concat(c.Set)));
            check(!keys.Any(k => k.StartsWith("lastcall.", StringComparison.Ordinal) || k.StartsWith("trickster.lastcall.", StringComparison.Ordinal))
                  && s.Nodes.SelectMany(n => n.Choices).All(c => c.RemoveItem != SoulJar),
                "Trk_Shamira_FlaskUntouched: a Shamira scene reads, fills or removes Areelu's flask: " + s.Id);
        }
        foreach (var id in new[] { "trickster.lastcall.bottle.king", "trickster.lastcall.bottle.alone", "trickster.lastcall.threshold" })
            check(!S(id).Forbids.Concat(S(id).Requires).Any(k => k.StartsWith("shamira", StringComparison.Ordinal)),
                "Trk_Shamira_FlaskUntouched: Last Call's bottle waits on Shamira: " + id);

        // Trk_Shamira_Seed: her audience in Chapter 4.
        var ch4 = World(story, 4, "trickster", "trickster.ever");
        check(Avail(read, ch4) && !Avail(bird, ch4), "Trk_Shamira_Seed: the open mind does not come first.");
        var hid = Through(read, ch4, "game", 2).First();
        check(hid.Has(P + "hid") && hid.Has(P + "read") && hid.Has("shamira.started") && Ch(read, "game", 2).Mythic == "PlayerIsTrickster",
            "Trk_Shamira_Seed: hiding under the barley is not the Trickster's answer.");
        check(Avail(bird, Later(story, hid, 9)), "Trk_Shamira_Seed: the bird does not follow the open mind.");
        var taste = S(P + "ch4.first_taste");
        check(Avail(taste, Later(story, Through(bird, Later(story, hid, 9), "chair", 0).First(), 13))
              && Avail(taste, Later(story, Through(bird, Later(story, hid, 9), "chair", 1).First(), 13)),
            "Trk_Shamira_Seed: she does not walk the dream, invited or not.");
        check(!Avail(read, World(story, 4, "trickster", "trickster.ever", "shamira.no_more_ch4")),
            "Trk_Shamira_Seed: her audience is offered after it closed natively.");

        // Trk_Shamira_Door: the door she knows, left open (earned natively or by the open mind), or opened blind.
        var known = World(story, 5, "trickster", "trickster.ever", "shamira.plan_known", "shamira.let_in.submitted");
        check(known.Has(P + "let_in") && Avail(setup, known), "Trk_Shamira_Door: submitting to her in her Harem does not count as letting her in.");
        var primed = Through(setup, known, "her_words", 0).First();
        check(primed.Has(Primed) && !primed.Has(P + "cost.opened_blind") && !primed.Has(Returned), "Trk_Shamira_Door: the known door is not left open.");
        check(Ch(setup, "her_words", 1).Abort && Ch(setup, "never_in", 1).Abort, "Trk_Shamira_Door: the question cannot be let go.");
        var never = World(story, 5, "trickster", "trickster.ever", "shamira.plan_known", "shamira.threw_out");
        var blind = Through(setup, never, "never_in", 0).First();
        check(blind.Has(Primed) && blind.Has(P + "cost.opened_blind"), "Trk_Shamira_Blind: a Commander who never let her in cannot open the door blind.");
        check(Program.Walk(setup, known).Any(r => r.Has(P + "veil")), "Trk_Shamira_Door: Socothbenoth's veil cannot be asked for.");

        // Trk_Shamira_Voice: the kill lands; she speaks behind the Commander's eyes at his closet.
        var dead = World(story, 5, "trickster", "trickster.ever", Killed, Primed, "shamira.started");
        check(Avail(voice, dead) && !Avail(twin, dead) && !Avail(drowning, dead), "Trk_Shamira_Voice: the closet is shut, or a twin opens beside it.");
        check(!own.Where(s => !s.TricksterDevice).Any(s => Avail(s, dead)), "Trk_Shamira_Voice: a courtship beat opens before she is heard.");
        var heard = Through(voice, dead, "choose", 0).First();
        check(heard.Has(Returned) && heard.Has(Heard) && heard.Has(P + "told_honest") && !heard.Has(Committed), "Trk_Shamira_Voice: the honest answer does not return her.");
        check(Through(voice, dead, "choose", 1).First().Has(P + "bargain"), "Trk_Shamira_Voice: the bargain is not recorded.");
        var kept = Through(voice, dead, "choose", 2).First();
        check(kept.Has(P + "cost.kept_captive") && kept.Has(Closed) && Ch(voice, "choose", 2).Alignment?.Direction == "Evil"
              && !Reaches(kept, Committed), "Trk_Shamira_Captive: locking her in the back of the head is not an evil hard no.");
        check(Program.Walk(voice, World(story, 5, "trickster", "trickster.ever", Killed, Primed, P + "cost.opened_blind")).All(r => r.Has(P + "cost.read_all")),
            "Trk_Shamira_Blind: coming in through a door opened blind does not tear through the Commander's head.");
        check(Reaches(heard, Committed), "Trk_Shamira_Voice: no road from her first words to the commit.");
        var handed = World(story, 5, "trickster", "trickster.ever", Killed, Primed, "shamira.cauldron_shown.latched");
        check(Avail(twin, Later(story, handed, 13)) && Program.Walk(twin, Later(story, handed, 13)).Any(r => r.Has(Heard)),
            "Trk_Shamira_SkipTwin: handing over the cauldron without listening has no letter.");
        check(!Avail(twin, Later(story, heard, 13)), "Trk_Shamira_SkipTwin: the twin repeats the closet.");

        // Trk_Shamira_Cold: killed with no door open; she drowns in the Commander's head.
        var cold = World(story, 5, "trickster", "trickster.ever", Killed);
        check(Avail(drowning, cold) && !Avail(voice, cold) && !Avail(setup, cold), "Trk_Shamira_Cold: the late road is shut, or the primed road opens.");
        var room = Through(drowning, cold, "choose", 0).First();
        check(room.Has(Returned) && room.Has(P + "made_room") && room.Has(P + "cost.late") && room.Has(P + "cost.read_all"),
            "Trk_Shamira_Cold: making room does not carry the late costs.");
        check(Reaches(room, Committed), "Trk_Shamira_Cold: no road from the late road to the commit.");
        var drowned = Through(drowning, cold, "choose", 1).First();
        check(drowned.Has(Closed) && drowned.Has(P + "declined") && !drowned.Has(Returned), "Trk_Shamira_Cold: letting her go under is not a hard no.");
        check(!Avail(drowning, World(story, 5, "trickster.ever", "trickster.failed", Killed)), "Trk_Shamira_AfterFailure: a lost Trickster saves her.");

        // Trk_Shamira_Court: Nocticula smells her in the Commander (Nocticula's scene; only Nocticula's flags).
        var court = S("nocticula.trickster.court.shamira");
        check(court.Relationship == "nocticula" && court.AnswerLists.SequenceEqual(new[] { Audience }) && court.Requires.Contains(Killed)
              && court.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).All(f => f.StartsWith("nocticula.", StringComparison.Ordinal))
              && court.Nodes.SelectMany(n => n.Choices).Where(c => c.NativeNext != null).All(c => c.NativeNext == Reported),
            "Nocticula's court scene is not hers, on her audience list after the kill, ending in her canon thanks.");

        // The nights, the theft, the fuel, the waking.
        var night = S(P + "mind.first_night");
        var heist = S(P + "mind.heist");
        var heistAlone = S(P + "mind.heist_alone");
        var dream = S(P + "mind.dream");
        var fuel = S(P + "mind.fuel");
        var waking = S(P + "mind.waking");
        check(Avail(night, Later(story, heard, 13)) && !Avail(heist, Later(story, heard, 13)), "The first night does not come first.");
        var n1 = Through(night, Later(story, heard, 13), "want", 0).First();
        check(n1.Has(P + "first_night") && n1.Has(P + "want.steward"), "The first night does not ask what she was kept for.");
        check(Avail(heist, Later(story, n1, 25)) && Avail(dream, Later(story, n1, 25)), "The theft or the second night does not follow the first.");
        var checks = heist.Nodes.SelectMany(n => n.Choices).Where(c => c.Check != null).Select(c => c.Check!).ToArray();
        check(checks.Count(k => k.Skill == "SkillStealth") == 3 && checks.Count(k => k.Skill == "SkillThievery") == 1
              && checks.Count(k => k.Skill == "CheckBluff") == 1
              && checks.Where(k => k.Skill == "SkillStealth").Select(k => k.DC).OrderBy(d => d).SequenceEqual(new[] { 22, 26, 32 }),
            "The theft is not Stealth (22 veiled, 26 with the Trickster's shadow, 32 bare) and Thievery, with a bluff when caught.");
        var street = heist.Nodes.Single(n => n.Id == "street").Choices;
        check(street[0].Requires.Contains(P + "veil") && street[1].Requires.Contains("trickster.stealth_tier1") && street[2].Forbids.Contains("trickster.stealth_tier1"),
            "The theft's easier roads are not gated on the veil and the chosen Stealth trick.");
        var stolen = Program.Walk(heist, Later(story, n1, 25)).ToList();
        check(stolen.All(r => r.Has(P + "shell")) && stolen.Any(r => r.Has(P + "cost.shell_torn")) && stolen.Any(r => r.Has(P + "cost.ramisa_story"))
              && stolen.Any(r => r.Has(P + "ramisa_fooled")), "Every road through the vats does not end with a shell, or a cost is missing.");
        var alone = World(story, 5, "trickster", "trickster.ever", Primed, P + "veil");
        check(Avail(heistAlone, Later(story, alone, 13)) && heistAlone.Forbids.Contains(Killed) && heistAlone.Kind == "event",
            "Trk_Shamira_Prepared: the body cannot be stolen before the kill, on Socothbenoth's veil.");
        var d2 = Through(dream, Later(story, n1, 25), "choice", 0).First();
        check(d2.Has(P + "dreamed") && d2.Has(P + "dream_burned") && Through(dream, Later(story, n1, 25), "choice", 1).First().Has(P + "dream_kept"),
            "The second night's choice (let the dream burn, or keep the reins) is not recorded.");
        var withShell = Later(story, d2, 25);
        withShell.Flags.Add(P + "shell");
        withShell.Times[P + "shell"] = d2.Hour;
        check(Avail(fuel, Later(story, withShell, 25)) && !Avail(fuel, Later(story, d2, 25)), "The fuel does not wait for the body.");
        var fw = Later(story, withShell, 25);
        var mineOnly = Through(fuel, fw, "choose", 0).First();
        var barracks = Through(fuel, fw, "choose", 1).First();
        check(mineOnly.Has(P + "fuel_set") && mineOnly.Has(P + "refused_barracks") && !mineOnly.Has(P + "cost.barracks"),
            "Trk_Shamira_Fuel: her dreams only is not recorded.");
        check(barracks.Has(P + "cost.barracks") && barracks.Has("trickster.secret.shamira_barracks") && Ch(fuel, "choose", 1).Alignment?.Direction == "Evil",
            "Trk_Shamira_Barracks: meeting her evil demand is not evil, or keeps no secret.");
        var refusals = Program.Walk(fuel, fw).ToList();
        check(refusals.Any(r => r.Has(P + "cast_out") && r.Has(Closed)) && refusals.Any(r => r.Has(P + "cost.kept_captive") && r.Has(Closed)),
            "Trk_Shamira_Fuel: refusing her the dreams has no captive-or-cast-out ending.");
        check(Avail(waking, Later(story, mineOnly, 25)), "The waking does not follow the fuel.");
        var woke = Program.Walk(waking, Later(story, mineOnly, 25)).ToList();
        check(woke.All(r => r.Has(Embodied) && r.Has(NeverAlone)) && woke.Any(r => r.Has(P + "last_dream.her")),
            "Trk_Shamira_Waking: the waking does not leave the Commander never dreaming alone.");
        check(own.Where(s => s.Id != waking.Id).SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => !c.Set.Contains(NeverAlone)),
            "Something other than the waking sets the cost.");

        // Trk_Shamira_Commit: the game in her Harem.
        var harem = S(P + "harem");
        var company = S(P + "after.first_company");
        var visit = S(P + "after.visit");
        var city = S(P + "after.city");
        var embodied = Later(story, woke.First(), 1);
        check(Avail(company, Later(story, embodied, 13)) && Avail(city, Later(story, embodied, 49)) && !Avail(harem, Later(story, embodied, 49)),
            "Her company and her city do not come before the game.");
        var cityDone = Program.Walk(city, Later(story, embodied, 49)).First();
        check(Avail(visit, Later(story, cityDone, 49)), "Her visit does not follow her city.");
        var proposed = Program.Walk(visit, Later(story, cityDone, 49)).First();
        check(proposed.Has(P + "game_proposed") && !proposed.Has(Committed), "She does not propose the game.");
        var hw = Later(story, proposed, 25);
        check(Avail(harem, hw), "Trk_Shamira_Commit: the game is not offered after her proposal.");
        var search = harem.Nodes.Single(n => n.Id == "search").Choices;
        check(search.All(c => c.Text.StartsWith("[", StringComparison.Ordinal) && !c.Text.Contains('"')),
            "Trk_Shamira_Commit: something is spoken in the game.");
        check(Through(harem, hw, "search", 0).All(r => r.Has(Committed) && r.Has(P + "lost_on_purpose")), "Trk_Shamira_Commit: losing on purpose does not commit.");
        check(Through(harem, hw, "search", 1).All(r => r.Has(P + "ally") && !r.Has(Committed) && !r.Has(Closed)), "Trk_Shamira_Won: winning is not the soft no.");
        check(Through(harem, hw, "search", 2).All(r => r.Has(Closed) && !r.Has(Committed)), "Trk_Shamira_Thrown: throwing her out is not the hard no.");
        var committers = own.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed))).Select(s => s.Id).ToArray();
        check(committers.SequenceEqual(new[] { P + "harem" }), "Something other than the game commits her.");
        check(harem.Nodes.Single(n => n.Id == "cut").Choices.Count == 1 && harem.Nodes.Any(n => n.Id == "morning"),
            "The intimacy has no cut and morning after.");
        var committed = Through(harem, hw, "search", 0).First();
        check(Avail(S(P + "after.throne"), Later(story, committed, 73)), "The throne does not follow the commit.");
        var throned = Program.Walk(S(P + "after.throne"), Later(story, committed, 73)).First();
        check(Avail(S(P + "after.night_alone"), Later(story, throned, 73)), "The night alone does not follow the throne.");
        check(Avail(S(P + "after.favour"), Later(story, Through(harem, hw, "search", 1).First(), 73)), "The ally never pays a favour.");
        check(story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "game_proposed" })
              && story.Derived["shamira.harem.eligible"].Length == 2 && story.Derived.ContainsKey("shamira.harem.voice.keeps_a_harem"),
            "The late commit or the household eligibility is not declared.");

        // Trk_Shamira_AllRomance: Shamira's whole road and Last Call's bottle in one Chapter 5, in either order.
        var bottleAlone = S("trickster.lastcall.bottle.alone");
        var threshold = S("trickster.lastcall.threshold");
        var lc = new[] { "trickster", "trickster.ever", "lastcall.flask_taken", "lastcall.flask_held", "shamira.plan_known", "shamira.let_in.thought" };
        var run = Through(setup, World(story, 5, lc), "her_words", 0).First();
        check(Avail(bottleAlone, Later(story, run, 1)), "Trk_Shamira_AllRomance: Last Call's bottle is shut by the door left open.");
        run.Flags.Add(Killed); run.Times[Killed] = run.Hour;
        run = Through(voice, Later(story, run, 1), "choose", 0).First();
        run = Program.Walk(night, Later(story, run, 13)).First(r => r.Has(P + "first_night"));
        check(Avail(bottleAlone, Later(story, run, 1)), "Trk_Shamira_AllRomance: Last Call's bottle is shut while she is behind the Commander's eyes.");
        var bottledEarly = Program.Walk(bottleAlone, Later(story, run, 1)).First(r => r.Has(LcPrimed));
        check(Reaches(bottledEarly, Committed), "Trk_Shamira_AllRomance: filling the bottle mid-route loses her commit.");
        run = Program.Walk(heist, Later(story, run, 25)).First(r => r.Has(P + "shell"));
        run = Program.Walk(dream, Later(story, run, 25)).First(r => r.Has(P + "dreamed"));
        run = Through(fuel, Later(story, run, 25), "choose", 0).First();
        run = Program.Walk(waking, Later(story, run, 25)).First();
        check(run.Has(Embodied) && Avail(bottleAlone, Later(story, run, 1)), "Trk_Shamira_AllRomance: Last Call's bottle is shut after the waking.");
        var bottled = Program.Walk(bottleAlone, Later(story, run, 1)).First(r => r.Has(LcPrimed));
        check(Avail(threshold, World(story, 6, bottled.Flags.ToArray())), "Trk_Shamira_AllRomance: last orders cannot be called after both roads.");
        check(Reaches(bottled, Committed), "Trk_Shamira_AllRomance: the commit is lost once the bottle is filled.");
        var lcFirst = World(story, 5, lc.Concat(new[] { LcPrimed }).ToArray());
        check(Avail(setup, lcFirst), "Trk_Shamira_LastCallFirst: a bottled death shuts the door.");

        // Coexistence, reactions and pages.
        foreach (var s in mine)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".closed", StringComparison.Ordinal) && key != Closed) && !key.EndsWith("_dead", StringComparison.Ordinal)
                      && !(key.EndsWith(".dead", StringComparison.Ordinal)) && !key.StartsWith("noct.", StringComparison.Ordinal),
                    "Shamira needs someone else dead, closed or Nocticula's state: " + s.Id + " " + key);
        var produced = new HashSet<string>(story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set));
        foreach (var s in mine)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)).Where(k => k.StartsWith(P, StringComparison.Ordinal)))
                check(produced.Contains(key) || story.Derived.ContainsKey(key), "A Shamira gate has no producer: " + s.Id + " requires " + key);
        check(reactions.Length == 6 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Arueshalae", "Daeran", "Regill", "Shyka", "Woljif" }),
            "The reactions are not Shyka, Arueshalae (twice), Daeran, Regill and Woljif.");
        check(pages.Length == 10 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null && c.Alignment == null))),
            "The epilogue pages carry effects or are missing.");
        foreach (var s in own.Where(x => Rules.IsRemote(x) && !x.TricksterDevice && x.Id != P + "mind.heist_alone"))
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray();
            var w = World(story, s.Chapters[0], new[] { "trickster", "trickster.ever", Returned, "shamira.started", Heard }.Concat(needs).ToArray());
            check(Avail(s, Later(story, w, s.DelayHours + 1)), "A Shamira page never opens: " + s.Id);
        }
        Console.WriteLine("PASS: Shamira Trickster (Trk_Shamira_*): the door left open or opened blind, the drowning, the vats, " + own.Count(s => !s.TricksterDevice)
            + " courtship beats, the fuel and the waking, the game and its no's, Nocticula's court, Areelu's flask left to Last Call in one run, "
            + reactions.Length + " reactions and " + pages.Length + " pages.");
    }
}
