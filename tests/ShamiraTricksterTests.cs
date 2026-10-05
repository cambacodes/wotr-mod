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
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Unit = "66e12264eaf6bf74196e20a9d7619cd2";
    private const string FoolKing = "cc50a88bbd8dd3e4da066d33d14fdfc8";
    private const string Tailor = "253cdb8f434e5a6469b75e18428316e3";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Hour = 5000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    private static Snapshot AtHerTable(Story story, Snapshot state)
    {
        var there = Program.Copy(state);
        there.Area = Drezen;
        there.AvailableContacts.Add(Unit);
        return there;
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
                    var w = AtHerTable(story, Later(story, from, 200, chapter));
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
        // F10: the ordinary jeweller replaces the transient Fool King as the primary anchor.
        // The existing King-gone/failure gates still select the tailor fallback.
        var table = story.Presences["shamira.presence"];
        var awning = story.Presences["shamira.presence.awning"];
        check(story.Presences.Keys.Count(k => k.StartsWith("shamira", StringComparison.Ordinal)) == 2
              && new[] { table, awning }.All(pr => pr.Unit == Unit && pr.Area == Drezen && pr.Mode == "spawn-copy" && pr.Dialog == "hub"
                  && pr.MinChapter == 5 && pr.MaxChapter == 5 && pr.Requires.Contains(Embodied) && pr.At!.Distance >= 2f
                  && new[] { Closed, P + "cost.kept_captive", P + "cast_out", P + "ally" }.All(pr.Forbids.Contains))
              && table.At!.NearUnit == Tailor && table.At.Side == "right" && table.At.Distance == 10f && table.Forbids.Contains("shamira.presence.failed")
              && table.Forbids.Contains("fool_king.gone") && awning.At!.NearUnit == "15f754455d1d87c42a4e14df456d5415" && awning.At.Side == "left" && awning.At.Distance == 6.5f
              && awning.RequiresAnyGroups.Length == 1 && awning.RequiresAnyGroups[0].Contains("shamira.presence.failed")
              && awning.RequiresAnyGroups[0].Contains("fool_king.gone"),
            "Trk_Shamira_Presence: her presence is not at the tailor with the independent smith-yard fallback.");
        var hubScenes = own.Where(s => s.InteractionHub == "shamira.presence").ToArray();
        check(hubScenes.Select(s => s.Id).OrderBy(x => x).SequenceEqual(new[] { P + "after.city", P + "after.night_alone", P + "after.throne", P + "after.visit", P + "harem", P + "mind.barracks_after" }.OrderBy(x => x))
              && hubScenes.All(s => !Rules.IsRemote(s) && s.Entry.Length > 0 && s.ContactUnit == Unit && s.Areas.SequenceEqual(new[] { Drezen })),
            "Trk_Shamira_Presence: the courtship after the waking is not played at her table.");
        foreach (var s in hubScenes)
        {
            var twinScene = S(s.Id + "_awning");
            check(twinScene.InteractionHub == "shamira.presence.awning" && s.Forbids.Contains(twinScene.Id) && twinScene.Forbids.Contains(s.Id)
                  && twinScene.RequiresAnyGroups.Any(g => g.Contains("shamira.presence.failed")), "Trk_Shamira_Presence: no awning twin for " + s.Id);
        }
        check(story.SelectedAnswers["shamira.let_in.mine"] == "c64d3f7e4a58fad43bd2bf135ab2b29e"
              && story.SelectedAnswers["shamira.let_in.submitted"] == "d5c0eb028f41da648bfbdd5a1ac2dc97"
              && story.Derived[P + "let_in"].Length == 5,
            "The earning is not bound to her native mind-reading answers (Answer_0008, 0031, 0044, 0178) and the open mind.");
        var read = S(P + "ch4.read");
        var bird = S(P + "ch4.bird");
        foreach (var s in new[] { read, bird })
            check(s.AnswerLists.SequenceEqual(new[] { Hub4 }) && (s == bird ? s.ReturnToList && s.NativeReturnCue == null : s.NativeReturnCue == Hub4Return) && s.Chapters.SequenceEqual(new[] { 4 })
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
            check(!keys.Any(k => k != "lastcall.active" && k.StartsWith("lastcall.", StringComparison.Ordinal) || k.StartsWith("trickster.lastcall.", StringComparison.Ordinal))
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
        check(Through(bird, Later(story, hid, 9), "chair", 0).All(r => r.Has(P + "tasted")) && Through(bird, Later(story, hid, 9), "chair", 1).All(r => r.Has(P + "tasted"))
              && !Avail(taste, Later(story, Through(bird, Later(story, hid, 9), "chair", 0).First(), 13)) && !Rules.IsRemote(bird),
            "Trk_Shamira_Seed: she does not walk the dream, invited or not.");
        check(!Avail(read, World(story, 4, "trickster", "trickster.ever", "shamira.no_more_ch4")),
            "Trk_Shamira_Seed: her audience is offered after it closed natively.");

        // Trk_Shamira_Door: the door she knows, left open (earned natively or by the open mind), or opened blind.
        var known = World(story, 5, "trickster", "trickster.ever", "shamira.plan_known", "shamira.let_in.submitted");
        check(known.Has(P + "let_in") && Avail(setup, known), "Trk_Shamira_Door: submitting to her in her Harem does not count as letting her in.");
        var primed = Through(setup, known, "her_native", 0).First();
        // Sol CAN: only the authored open mind heard her explain the Abyss's mouth; native let-ins guess it.
        var seenNative = new HashSet<string>(); Program.Walk(setup, known, (id, _) => seenNative.Add(id));
        var seenRead = new HashSet<string>(); Program.Walk(setup, World(story, 5, "trickster", "trickster.ever", "shamira.plan_known", P + "read"), (id, _) => seenRead.Add(id));
        check(seenNative.Contains("her_native") && !seenNative.Contains("her_words") && seenRead.Contains("her_words") && !seenRead.Contains("her_native"),
            "Trk_Shamira_Door: a native let-in recalls the open mind's lesson, or the open mind does not.");
        check(primed.Has(Primed) && !primed.Has(P + "cost.opened_blind") && !primed.Has(Returned), "Trk_Shamira_Door: the known door is not left open.");
        check(Ch(setup, "her_words", 1).Abort && Ch(setup, "never_in", 1).Abort && Ch(setup, "her_native", 1).Abort, "Trk_Shamira_Door: the question cannot be let go.");
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
        check(night.Nodes.Any(n => n.Id == "wt_start") && night.Nodes.Any(n => n.Id == "h_start"), "The war council and the theft are not folded into the first night's page.");
        var n1 = Through(night, Later(story, heard, 13), "want", 0).First();
        check(n1.Has(P + "first_night") && n1.Has(P + "want.steward"), "The first night does not ask what she was kept for.");
        check(n1.Has(P + "shell") && !Avail(heist, Later(story, n1, 25)) && !Avail(S(P + "mind.war_table"), Later(story, n1, 25)) && Avail(dream, Later(story, n1, 25)),
            "The theft is not on the first night's page, or the second night does not follow.");
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
        Snapshot With(Snapshot s, string f) { var t = Program.Copy(s); t.Flags.Add(f); return t; }
        var planned = World(story, 5, "trickster", "trickster.ever", "shamira.plan_known", "shamira.let_in.submitted");
        var alonePaths = Program.WalkVia(setup, planned, "veil", 1);
        check(!Avail(heistAlone, Later(story, With(alone, "shamira.plan_known"), 13)) && !Avail(heistAlone, Later(story, planned, 13)) && alonePaths.Count > 0
              && alonePaths.All(r => r.Has(P + "shell") && r.Has(P + "veil")) && alonePaths.Any(r => r.Has(P + "shell_chosen_alone")),
            "Trk_Shamira_Prepared: the body cannot be stolen before the kill, on Socothbenoth's veil.");
        var d2 = Through(dream, Later(story, n1, 25), "choice", 0).First();
        check(d2.Has(P + "dreamed") && d2.Has(P + "dream_burned") && Through(dream, Later(story, n1, 25), "choice", 1).First().Has(P + "dream_kept"),
            "The second night's choice (let the dream burn, or keep the reins) is not recorded.");
        var withShell = Later(story, d2, 25);
        withShell.Flags.Add(P + "shell");
        withShell.Times[P + "shell"] = d2.Hour;
        check(d2.Has(P + "almost") && d2.Has(P + "fuel_set") && d2.Has(Embodied) && d2.Has(P + "first_company") && !Avail(fuel, Later(story, d2, 25))
              && !Avail(S(P + "mind.almost"), Later(story, d2, 25)), "The third night, the fuel and the waking are not folded into the dreams' page.");
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
        // 05 §4.2 folds: the waking follows the fuel on its page, and her first night of company follows the waking.
        var woke = Through(fuel, fw, "choose", 0).ToList();
        check(woke.All(r => r.Has(Embodied) && r.Has(NeverAlone) && r.Has(P + "first_company"))
              && Program.Walk(fuel, fw).Any(r => r.Has(P + "last_dream.her")) && Program.Walk(fuel, fw).Any(r => r.Has(P + "terms.edge")),
            "Trk_Shamira_Waking: the waking does not leave the Commander never dreaming alone.");
        check(barracks.Has(Embodied) && !Avail(waking, Later(story, mineOnly, 25)) && !Avail(S(P + "after.first_company"), Later(story, mineOnly, 25)),
            "Trk_Shamira_Waking: the folded pages are still delivered after the fuel page.");
        check(own.Where(s => s.Id != waking.Id && s.Id != fuel.Id && s.Id != dream.Id).SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => !c.Set.Contains(NeverAlone)),
            "Something other than the waking sets the cost.");

        // Trk_Shamira_Commit: the game in her Harem.
        var harem = S(P + "harem");
        var visit = S(P + "after.visit");
        var city = S(P + "after.city");
        var embodied = AtHerTable(story, Later(story, woke.First(), 1));
        check(Avail(city, Later(story, embodied, 49)) && !Avail(harem, Later(story, embodied, 49))
              && !Avail(city, Later(story, Later(story, woke.First(), 1), 49)),
            "Her city does not come before the game, at her table only.");
        var cityDone = Program.Walk(city, Later(story, embodied, 49)).First();
        check(Avail(visit, Later(story, cityDone, 49)), "Her visit does not follow her city.");
        var proposed = Program.Walk(visit, Later(story, cityDone, 49)).First();
        check(proposed.Has(P + "game_proposed") && !proposed.Has(Committed), "She does not propose the game.");
        // Sol INT: Arueshalae as she is: redeemed and here, corrupted and here, or gone.
        foreach (var (flags, node) in new (string[], string)[] {
            (new string[0], "aru_redeemed"), (new[] { "arueshalae.evil_recruited" }, "aru_evil"),
            (new[] { "arueshalae_dead" }, "aru_gone"), (new[] { "arueshalae.kicked_out" }, "aru_gone"),
            (new[] { "arueshalae.failed" }, "aru_gone"), (new[] { "arueshalae.evil_recruited", "arueshalae.evil_dead" }, "aru_gone"),
            (new[] { "arueshalae_dead", "arueshalae.trickster.returned" }, "aru_redeemed") })
        {
            var at = Program.Copy(Later(story, cityDone, 49));
            foreach (var f in flags) at.Flags.Add(f);
            var seenNodes = new HashSet<string>();
            Program.Walk(visit, at, (id, _) => seenNodes.Add(id));
            check(seenNodes.Contains(node) && seenNodes.Count(x => x.StartsWith("aru_", StringComparison.Ordinal)) == 1,
                "Trk_Shamira_Visit: Arueshalae's state [" + string.Join(",", flags) + "] does not read as " + node + ".");
        }
        var hw = Later(story, proposed, 25);
        check(Avail(harem, hw), "Trk_Shamira_Commit: the game is not offered after her proposal.");
        var search = harem.Nodes.Single(n => n.Id == "search").Choices;
        check(search.All(c => c.Text.StartsWith("[", StringComparison.Ordinal) && !c.Text.Contains('"')),
            "Trk_Shamira_Commit: something is spoken in the game.");
        check(Through(harem, hw, "search", 0).All(r => r.Has(Committed) && r.Has(P + "lost_on_purpose")), "Trk_Shamira_Commit: losing on purpose does not commit.");
        check(Through(harem, hw, "search", 1).All(r => r.Has(P + "ally") && !r.Has(Committed) && !r.Has(Closed)), "Trk_Shamira_Won: winning is not the soft no.");
        check(Through(harem, hw, "search", 2).All(r => r.Has(Closed) && !r.Has(Committed)), "Trk_Shamira_Thrown: throwing her out is not the hard no.");
        var committers = own.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed))).Select(s => s.Id).ToArray();
        check(committers.OrderBy(x => x).SequenceEqual(new[] { P + "harem", P + "harem_awning" }), "Something other than the game (at her table, or its awning twin) commits her.");
        check(harem.Nodes.Single(n => n.Id == "cut").Choices.Count == 1 && harem.Nodes.Any(n => n.Id == "morning")
              && harem.Nodes.Single(n => n.Id == "cut").Text.Contains("astride"),
            "The intimacy has no staged threshold, cut and morning after.");
        var committed = Through(harem, hw, "search", 0).First();
        check(Avail(S(P + "after.throne"), Later(story, committed, 73)), "The throne does not follow the commit.");
        var throned = Program.Walk(S(P + "after.throne"), Later(story, committed, 73)).First();
        check(Avail(S(P + "after.night_alone"), Later(story, throned, 73)), "The night alone does not follow the throne.");
        check(Through(harem, hw, "search", 1).All(r => r.Has(P + "ally.favour")) && !Avail(S(P + "after.favour"), Later(story, Through(harem, hw, "search", 1).First(), 73)), "The ally never pays a favour, or it comes again as a page.");
        // eng7-l13: preparation also requires the live outcome contract.
        check(story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "game_proposed", "shamira.outcome.route_open" })
              && story.Derived["shamira.harem.eligible"].Length == 2 && story.Derived.ContainsKey("shamira.harem.voice.keeps_a_harem"),
            "The late commit or the household eligibility is not declared.");

        // Trk_Shamira_AllRomance: Shamira's whole road and Last Call's bottle in one Chapter 5, in either order.
        var bottleAlone = S("trickster.lastcall.bottle.alone");
        var threshold = S("trickster.lastcall.threshold");
        var lc = new[] { "trickster", "trickster.ever", "lastcall.flask_taken", "lastcall.flask_held", "shamira.plan_known", "shamira.let_in.thought" };
        var run = Through(setup, World(story, 5, lc), "her_native", 0).First();
        check(Avail(bottleAlone, Later(story, run, 1)), "Trk_Shamira_AllRomance: Last Call's bottle is shut by the door left open.");
        run.Flags.Add(Killed); run.Times[Killed] = run.Hour;
        run = Through(voice, Later(story, run, 1), "choose", 0).First();
        run = Program.Walk(night, Later(story, run, 13)).First(r => r.Has(P + "first_night"));
        check(run.Has(P + "asked_lady") && !run.Has(P + "council_heard"), "Trk_Shamira_FirstNight: her lady's words are not folded into the first night, or a Council never attended is recalled.");
        check(Avail(bottleAlone, Later(story, run, 1)), "Trk_Shamira_AllRomance: Last Call's bottle is shut while she is behind the Commander's eyes.");
        var bottledEarly = Program.Walk(bottleAlone, Later(story, run, 1)).First(r => r.Has(LcPrimed));
        check(Reaches(bottledEarly, Committed), "Trk_Shamira_AllRomance: filling the bottle mid-route loses her commit.");
        run = Program.Walk(heist, Later(story, run, 25)).First(r => r.Has(P + "shell"));
        run = Program.Walk(dream, Later(story, run, 25)).First(r => r.Has(P + "dreamed"));
        run = Through(fuel, Later(story, run, 25), "choose", 0).First();
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
        // 05 §3.1 row 37: exactly Shyka, Socothbenoth (inside the setup and the first words) and Arueshalae. The Daeran, Regill
        // and Woljif reactions of the first build are retired by gating: none is ever available beside the flag that triggers it.
        var retiredReactions = reactions.Where(r => r.Owner == "Daeran" || r.Owner == "Regill" || r.Owner == "Woljif").ToArray();
        check(reactions.Length == 7 && reactions.All(r => r.Nodes.Count == 1) && retiredReactions.Length == 3
              && retiredReactions.All(r => !Avail(r, World(story, 5, new[] { "trickster", "trickster.ever", Returned, Heard, Embodied, NeverAlone, P + "fuel_set", P + "cost.barracks" })))
              && retiredReactions.All(r => !Avail(r, World(story, 5, new[] { "trickster", "trickster.ever", Returned, Heard })))
              && reactions.Except(retiredReactions).Select(r => r.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Arueshalae", "Shyka" }),
            "The live reactions are not Shyka and Arueshalae, or a retired reactor still speaks.");
        check(pages.Length == 11 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null && c.Alignment == null))),
            "The epilogue pages carry effects or are missing.");
        // The pages folded into others (05 §4.2) are never delivered on a new road; every other page opens.
        var folded = new[] { P + "mind.council", P + "mind.her_lady", P + "mind.almost", P + "mind.waking", P + "after.first_company", P + "after.eve",
                             P + "mind.heist", P + "mind.war_table", P + "mind.fuel", P + "ch4.first_taste", P + "after.favour" };
        foreach (var s in own.Where(x => Rules.IsRemote(x) && !x.TricksterDevice && x.Id != P + "mind.heist_alone" && !folded.Contains(x.Id)))
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray();
            var w = World(story, s.Chapters[0], new[] { "trickster", "trickster.ever", Returned, "shamira.started", Heard }.Concat(needs).ToArray());
            check(Avail(s, Later(story, w, s.DelayHours + 1)), "A Shamira page never opens: " + s.Id);
        }
        // Sol INT/COX: through actual rest delivery, the first post-Council rest brings the first night with the Council in it,
        // and the whole primed road reaches the commit with at most four required Chapter 5 pages (the folds) before her
        // presence takes over; the folded pages never arrive.

        // eng7-l08: delivery accounting follows the woman after refusal too,
        // including consequence relationships; a rotation alias is no exemption.
        var refusalRuns = new HashSet<string>();
        bool ShamiraDelivery(Scene s) => s.Relationship == "shamira" || s.Relationship == "shamira_barracks"
            || s.Owner == "Shamira";
        void RefusalDeliveries(Snapshot beforeGame, IEnumerable<string> alreadyDelivered, string roadName)
        {
            if (!beforeGame.Has(P + "cost.barracks")) return;
            foreach (string placement in new[] { P + "harem", P + "harem_awning" })
            foreach (int refusal in new[] { 1, 2 })
            {
                var at = Program.Copy(beforeGame);
                if (placement.EndsWith("_awning", StringComparison.Ordinal))
                    at.Flags.Add("fool_king.gone"); // explicit native gone world; no fabricated placement-failure flag
                Rules.Complete(story, at);
                var game = S(placement);
                if (!Avail(game, at)) continue; // the alternate placement is tested only in its own valid native world
                foreach (var refused in Through(game, at, "search", refusal))
                {
                    refusalRuns.Add(roadName + "/" + placement + "/" + refusal);
                    var after = Program.Copy(refused);
                    var deliveries = alreadyDelivered.ToList();
                    for (int rest = 0; rest < 8; rest++)
                    {
                        after = Later(story, after, 26);
                        foreach (var page in Rules.MailbagArrivals(story, after).Where(ShamiraDelivery).ToList())
                        {
                            // Closure is retained: the consequence may belong to a separate relationship.
                            var outcome = Program.Walk(page, after).FirstOrDefault(s => s.Has(page.Id));
                            if (outcome != null) { deliveries.Add(page.Id); after = outcome; Rules.Complete(story, after); }
                        }
                    }
                    Program.Eng7L08Allocation(story, check, roadName + "/" + placement + "/refusal " + refusal,
                        "Shamira", 5, after, deliveries, false);
                    check(deliveries.Count <= 2, "05-ROUND2-LEDGER-AND-RULES §4.2 Shamira tier B: "
                        + roadName + "/" + placement + "/refusal " + refusal + ": " + string.Join(",", deliveries));
                    check(!after.Has(Committed), "Refused Shamira gained an unearned commitment during later rests");
                }
            }
        }
        // end eng7-l08
        var deliveredIds = new List<string>();
        var road = World(story, 5, "trickster", "trickster.ever", Killed, Primed, "shamira.started", "shamira.cauldron_shown.latched");
        road = Through(voice, road, "choose", 0).First();
        for (int rest = 0; rest < 30 && !road.Has(Committed); rest++)
        {
            road = AtHerTable(story, Later(story, road, 26));
            var bag = Rules.MailbagArrivals(story, road).Where(ShamiraDelivery).ToList();
            foreach (var letter in bag)
            {
                var outcome = Program.Walk(letter, road).Where(r => r.Has(letter.Id) && !r.Has(Closed)).OrderByDescending(r => r.Flags.Count).FirstOrDefault();
                if (outcome == null) continue;
                deliveredIds.Add(letter.Id); road = AtHerTable(story, outcome);
            }
            // eng7-l08: continue both refusal histories beyond this game.
            RefusalDeliveries(road, deliveredIds, "primed");
            foreach (var beat in own.Where(s => s.InteractionHub == "shamira.presence" && Avail(s, road)).ToList())
            {
                var outcome = Program.Walk(beat, road).Where(r => r.Has(beat.Id) && !r.Has(Closed) && !r.Has(P + "ally")).OrderByDescending(r => r.Has(Committed)).FirstOrDefault();
                if (outcome != null) road = AtHerTable(story, outcome);
            }
        }
        check(road.Has(Committed), "Trk_Shamira_Delivery: the primed road does not reach the commit through actual delivery (" + string.Join(",", deliveredIds) + ").");
        check(deliveredIds.Count > 0 && deliveredIds[0] == P + "mind.first_night" && road.Has(P + "council_heard")
              && !deliveredIds.Intersect(folded).Any() && !deliveredIds.Contains(P + "mind.council"),
            "Trk_Shamira_Delivery: the Council beat is lost to delivery order, or a folded page arrives (" + string.Join(",", deliveredIds) + ").");
        check(deliveredIds.Count <= 2, "Trk_Shamira_Delivery: more than two Chapter 5 pages on the way to the commit (" + string.Join(",", deliveredIds) + ").");
        // eng7-l08: every promised refusal case must actually execute.
        check(refusalRuns.Count(x => x.StartsWith("primed/", StringComparison.Ordinal)) == 4, "Primed Shamira refusal histories were not executed");
        // The same cap on the letter road (her first words by letter) and the late road (she drowns), all pages counted.
        foreach (var (roadName, startFlags, entry) in new (string, string[], string)[] {
            ("letter", new[] { "trickster", "trickster.ever", Killed, Primed, "shamira.started", "shamira.cauldron_shown.latched" }, P + "killed.voice_letter"),
            ("late", new[] { "trickster", "trickster.ever", Killed }, P + "killed.drowning"),
            // eng7-l08: the actual pre-kill, body-chosen-alone road; not a seeded shell.
            ("unextracted", new[] { "trickster", "trickster.ever", "shamira.plan_known", "shamira.let_in.submitted" }, P + "mind.first_night") })
        {
            var r0 = World(story, 5, startFlags);
            // eng7-l08: play the prepared theft before the native kill/cauldron observation.
            if (roadName == "unextracted")
            {
                r0 = Program.WalkVia(setup, r0, "veil", 1).First(r => r.Has(P + "shell_chosen_alone"));
                r0.Flags.Add(Killed); r0.Times[Killed] = r0.Hour;
                r0.Flags.Add("shamira.cauldron_shown"); r0.Times["shamira.cauldron_shown"] = r0.Hour;
                Rules.Complete(story, r0);
                r0 = Through(voice, r0, "choose", 0).First();
            }
            // end eng7-l08
            var got = new List<string>();
            for (int rest = 0; rest < 30 && !r0.Has(Committed); rest++)
            {
                r0 = AtHerTable(story, Later(story, r0, 26));
                foreach (var letter in Rules.MailbagArrivals(story, r0).Where(ShamiraDelivery).ToList())
                {
                    var outcome = Program.Walk(letter, r0).Where(r => r.Has(letter.Id) && !r.Has(Closed)).OrderByDescending(r => r.Flags.Count).FirstOrDefault();
                    if (outcome == null) continue;
                    got.Add(letter.Id); r0 = AtHerTable(story, outcome);
                }
                // eng7-l08: count post-refusal consequence deliveries too.
                RefusalDeliveries(r0, got, roadName);
                foreach (var beat in own.Where(s => s.InteractionHub == "shamira.presence" && Avail(s, r0)).ToList())
                {
                    var outcome = Program.Walk(beat, r0).Where(r => r.Has(beat.Id) && !r.Has(Closed) && !r.Has(P + "ally")).OrderByDescending(r => r.Has(Committed)).FirstOrDefault();
                    if (outcome != null) r0 = AtHerTable(story, outcome);
                }
            }
            check(r0.Has(Committed) && got.Count <= 2 && got.FirstOrDefault() == entry,
                "Trk_Shamira_Delivery_" + roadName + ": " + string.Join(",", got) + (r0.Has(Committed) ? "" : " (no commit)"));
            // eng7-l08: both placements and both refusals must execute on this road.
            check(refusalRuns.Count(x => x.StartsWith(roadName + "/", StringComparison.Ordinal)) == 4, roadName + " Shamira refusal histories were not executed");
        }

        // Sol CAN/HOW: the diamond as the Council actually left it: Nirvana only, the Council's essences, or Shyka's taking.
        foreach (var (extra, want, not) in new (string[], string, string)[] {
            (new string[0], "c_nirvana", "c_full"), (new[] { "shamira.council_donated" }, "c_full", "c_shyka"),
            (new[] { "shamira.council_donated", "shamira.shyka_offer_seen" }, "c_shyka", "c_nirvana") })
        {
            var cw = World(story, 5, new[] { "trickster", "trickster.ever", Killed, Primed, "shamira.started", "shamira.cauldron_shown.latched", Returned, Heard }.Concat(extra).ToArray());
            var cn = new HashSet<string>(); Program.Walk(night, cw, (id, _) => cn.Add(id));
            check(cn.Contains(want) && !cn.Contains(not), "Trk_Shamira_Council: the diamond's contents are misremembered (" + string.Join(",", extra) + ").");
        }
        // Sol INT/CAN (r5): the bird's taste follows what the Commander actually thought; demons are read, not eaten asleep.
        var birdScene = S(P + "ch4.bird");
        foreach (var (thought, want) in new[] { (P + "hid", "eat_barley"), (P + "thought_war", "eat_war"), (P + "thought_her", "eat_her") })
        {
            var bn = new HashSet<string>(); Program.Walk(birdScene, World(story, 4, "trickster", P + "read", thought), (id, _) => bn.Add(id));
            check(bn.Contains(want) && new[] { "eat_barley", "eat_war", "eat_her" }.Count(bn.Contains) == 1, "Trk_Shamira_Bird: the taste of " + thought + " is misremembered.");
        }
        check(!birdScene.Nodes.Any(n => n.Text.Contains("dream of my throne")), "Trk_Shamira_Bird: her courtiers dream (demons do not).");
        // Sol INT (r5): the game's lost node never credits the barracks; the masked courtier is known only after the bird.
        foreach (var hs in story.Scenes.Where(s => s.Id.StartsWith(P + "harem", StringComparison.Ordinal)))
        {
            check(!hs.Nodes.Any(n => n.Id == "lost" && n.Text.Contains("barracks")), "Trk_Shamira_Harem: the lost game credits a refused barracks: " + hs.Id);
            var be = hs.Nodes.FirstOrDefault(n => n.Id == "bell_end");
            check(be == null || (be.Choices.Count == 2 && be.Choices[0].Next == "mask_known" && be.Choices[0].Requires.Contains(P + "bird")
                                 && be.Choices[1].Next == "mask_stranger" && be.Choices[1].Forbids.Contains(P + "bird")),
                "Trk_Shamira_Harem: the masked courtier is recognised without the bird: " + hs.Id);
        }
        // Sol CAN/INT (r6): a native invitation (Answer_0008 etc.) is remembered as one; the night alone never removes her presence.
        foreach (var hs in story.Scenes.Where(s => s.Id.StartsWith(P + "harem", StringComparison.Ordinal)))
        {
            var sits = hs.Nodes.Single(n => n.Id == "sits");
            check(sits.Choices.Count == 6 && sits.Choices[4].Forbids.Contains(P + "let_in") && sits.Choices[5].Next == "where_invited"
                  && sits.Choices[5].Requires.Contains(P + "let_in"), "Trk_Shamira_Harem: an invited Commander is told she never went in: " + hs.Id);
        }
        check(new[] { table, awning }.All(pr => !pr.Forbids.Contains(P + "night_alone.asked")), "Trk_Shamira_Presence: the night alone removes her from the table.");
        // Sol INT (G6(b)): an Arueshalae who died and came back on her own road reacts again; a dead one does not.
        var walking = S(P + "react.arueshalae_walking");
        var aw = World(story, 5, "trickster", "trickster.ever", Embodied, "arueshalae_dead");
        check(!Avail(walking, aw) && Avail(walking, World(story, 5, "trickster", "trickster.ever", Embodied, "arueshalae_dead", "arueshalae.trickster.returned")),
            "Trk_Shamira_Reactions: a returned Arueshalae is still treated as dead.");
        // Sol INT: the pages of a life after the war play only for a Commander who has one.
        var keptPage = S(P + "epilogue.kept");
        var mourned = S(P + "epilogue.mourned");
        var livingEnd = new[] { "trickster.ever", Embodied, Committed };
        check(Avail(keptPage, World(story, 6, livingEnd)) && !Avail(keptPage, World(story, 6, livingEnd.Concat(new[] { "sacrifice" }).ToArray()))
              && Avail(keptPage, World(story, 6, livingEnd.Concat(new[] { "sacrifice", "trickster.commander_back" }).ToArray()))
              && Avail(mourned, World(story, 6, livingEnd.Concat(new[] { "sacrifice" }).ToArray()))
              && !Avail(mourned, World(story, 6, livingEnd.Concat(new[] { "sacrifice", "trickster.commander_back" }).ToArray())),
            "Trk_Shamira_Survival: the surviving pages play over a death, or the dead Commander has no page.");

        // Sol INT: the Harem remembers the crystals only where she took them; the awning twins stage no absent King.
        var whereSeen = new HashSet<string>();
        Program.Walk(harem, World(story, 5, "trickster", "trickster.ever", Embodied, P + "visited", P + "game_proposed"), (id, _) => whereSeen.Add(id));
        check(whereSeen.Contains("where_first") && !whereSeen.Contains("where_crystals"), "Trk_Shamira_Harem: a crystal interrogation is recalled that never happened.");
        foreach (var twinScene in own.Where(s => s.InteractionHub == "shamira.presence.awning"))
            check(!twinScene.Nodes.Any(n => n.Text.Contains("King's") || n.Text.Contains("tavern table") || n.Text.Contains("back door")),
                "Trk_Shamira_Awning: the fallback stages the King's tavern: " + twinScene.Id);
        Console.WriteLine("PASS: Shamira Trickster (Trk_Shamira_*): the door left open or opened blind, the drowning, the vats, " + own.Count(s => !s.TricksterDevice)
            + " courtship beats, the fuel and the waking, the game and its no's, Nocticula's court, Areelu's flask left to Last Call in one run, "
            + reactions.Length + " reactions and " + pages.Length + " pages.");
    }
}
