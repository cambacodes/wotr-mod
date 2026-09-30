using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Horzalah, Trickster (Writer/handoffs/trickster/horzalah.md; binding plan 11-ROSTER-PLAN-2 §2, Horzalah block and build sheet,
// R4): "The ear in the gift box". One block per rules test (Trk_Horzalah_*): the mercy node (the guess, the story, the
// Diplomacy twins, her knife, her native farewell), the Greybor-less night, the Guild circling (refused or dismissed), the
// Guild kept and its pivot, her gift, the collar and her own move, the chamber, the kill that stands, the pages, the
// reactors, the presence and its night twins, and the courtship on her presence.
internal static class HorzalahTricksterTests
{
    private const string P = "horzalah.trickster.";
    private const string Committed = "horzalah.committed";
    private const string Closed = "horzalah.closed";
    private const string Started = "horzalah.started";
    private const string Dead = "horzalah.dead";
    private const string Unit = "38f0acf8ba7c3b64b87369d478014fda";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string MercyList = "8373a8ede2c5483e9a734dfea046fe2d";
    private const string MercyReturn = "4a3f22ae70e441d9b27ce67974f632d5";
    private const string Farewell = "c12bda4e0a95464db71e9f9f79e765de";
    private const string YozzList = "9652bd6d33d394a498bb7a1c28693cc6";
    private const string ScarCue = "7dce8fddc72c85d49a9520a9bc1ac85f";
    private const string Primed = P + "primed";
    private const string Ear = P + "cost.ear";
    private const string Late = P + "cost.late";
    private const string Refused = P + "refused";
    private const string Wants = P + "wants_heard";
    private const string Returned = P + "returned";
    private const string LeftFree = P + "left_free";
    private const string Tested = P + "tested";
    private const string Ally = P + "ally";
    private const string Declined = P + "declined";
    private const string Chamber = P + "chamber_seen";
    private const string Morning = P + "morning_seen";
    private const string Failed = "horzalah.presence.failed";
    private static readonly string[] Kills = { "horzalah.killed", "horzalah.killed_b", P + "killed_unmet" };

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = Drezen };
        state.AvailableContacts.Add(Unit);
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
        // Every outcome of a scene with the exact edges taken to reach it: (node, choice index) pairs, walked the way the
        // engine offers them (only choices whose Requires/Forbids hold at that point; a check branches to both outcomes).
        List<(Snapshot state, List<(string node, int index)> path)> Paths(Scene scene, Snapshot initial)
        {
            var outcomes = new List<(Snapshot, List<(string, int)>)>();
            void Visit(string id, Snapshot state, List<(string, int)> path)
            {
                var node = scene.Nodes.Single(n => n.Id == id);
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    if (!Rules.Match(choice.Requires, choice.Forbids, state)) continue;
                    var next = Program.Copy(state);
                    foreach (var effect in choice.Set)
                        if (next.Flags.Add(effect)) next.Times[effect] = next.Hour;
                    var edge = new List<(string, int)>(path) { (id, i) };
                    if (choice.Next != null || choice.Check != null)
                        foreach (var target in Rules.NextNodes(choice)) Visit(target, Program.Copy(next), edge);
                    else
                    {
                        if (!choice.Abort) { next.Flags.Add(scene.Id); next.Times[scene.Id] = next.Hour; }
                        outcomes.Add((next, edge));
                    }
                }
            }
            Visit(scene.Nodes[0].Id, initial, new List<(string, int)>());
            return outcomes;
        }
        // Take: the scene must be available, and the outcome must have traversed exactly that choice.
        List<Snapshot> Through(Scene scene, Snapshot w, string node, int index)
        {
            check(Avail(scene, w), "Not available before taking " + scene.Id + "/" + node + "[" + index + "]");
            var hits = Paths(scene, w).Where(o => o.path.Contains((node, index))).Select(o => o.state).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            var hit = Through(scene, w, node, index).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            return hit ?? w;
        }
        bool NoKill(Snapshot s) => !Kills.Any(s.Has) && !s.Has(Dead);

        var rel = story.Relationships["horzalah"];
        var own = story.Scenes.Where(s => s.Relationship == "horzalah" && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = story.Scenes.Where(s => s.Relationship == "horzalah" && s.Owner == "HorzalahEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "horzalah" && s.Reaction).ToArray();
        var scar = S(P + "ch4.scar");
        var box5 = S(P + "ch5.nothing");
        var mercy = S(P + "mercy.gift");
        var unmet = S(P + "unmet.knife");
        var late = S(P + "late.at_night");
        var kept = S(P + "guild.kept");
        var gift = S(P + "test.the_gift");
        var giftNight = S(P + "test.the_gift_night");
        var collar = S(P + "commit.collar");
        var collarNight = S(P + "commit.collar_night");
        var move = S(P + "commit.her_move");
        var moveNight = S(P + "commit.her_move_night");
        var chamber = S(P + "visit.chamber");
        var beats = own.Where(s => s.Id.StartsWith(P + "beat.", StringComparison.Ordinal)).ToArray();
        var letters = own.Where(s => s.Id.StartsWith(P + "letter.", StringComparison.Ordinal)).ToArray();

        // Shape and hooks (Trk_Horzalah_Bindings: the build sheet's keys are bound as listed; tools/verify-game-bindings.py
        // resolves every GUID against blueprints.zip).
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { Dead }) && rel.UnavailableOverrides.Count == 0
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "late", "mercy", "unmet" }),
            "Horzalah's relationship does not match the plan (her death stands; mercy, unmet and late access).");
        check(story.SelectedAnswers["horzalah.killed"] == "5de3ea4370854d229e047d95980006c9"
              && story.SelectedAnswers["horzalah.killed_b"] == "717a2f84c7dbfd24dbb474abd26211b3"
              && story.Latches["horzalah.dismissed.latched"].OrderBy(k => k).SequenceEqual(new[] { "horzalah.dismissed", "horzalah.dismissed_b" })
              && story.SelectedAnswers["horzalah.dismissed"] == "86e984232083404ebb61832b0cd5778c"
              && story.SelectedAnswers["horzalah.dismissed_b"] == "a4e7f54ec0c0ccd42ba50cf216a1457c"
              && story.SeenCues["horzalah.met_q3_a"].SequenceEqual(new[] { "65b730aabc12f344fb3fc779a8e8c53b" })
              && story.SeenCues["horzalah.met_q3_b"].SequenceEqual(new[] { "bc0174e40cf066444a69785514bc6901" })
              && story.SeenCues["horzalah.scar_seen"].SequenceEqual(new[] { ScarCue })
              && story.SeenCues["baphomet.named_horzalah"].SequenceEqual(new[] { "039978569cf79814899362d3f1b5b45b" })
              && story.CompletedQuests["greybor.q2_done"] == "6377e00508d4c9243a7b89d743d7914c"
              && story.CompletedQuests["iz.done"] == "95ff7d975689fcf44b085d10907e711d"
              && story.Etudes["greybor.dead"] == "10320ad437121a44eb629d5fa9a79c75"
              && story.Etudes["greybor.kicked_out"] == "dd138e723bf3dd94caddc127a23788ad"
              && story.Etudes["greybor.away"] == "00715f05d727921438971fa32c02ceaf"
              && story.Etudes["chapter.six"] == "41bf413e0fa2ea34b937d4445edd5f89"
              && story.SeenCues["greybor.q3_failed"].SequenceEqual(new[] { "e60797a42f8d33c4581cfe3bb37b5d2f" }),
            "Trk_Horzalah_Bindings: a native key is not bound as the build sheet lists it.");
        check(story.Derived[Dead].Select(g => string.Join("+", g)).OrderBy(g => g).SequenceEqual(new[] { "horzalah.killed", "horzalah.killed_b", P + "killed_unmet" })
              && story.Derived["horzalah.q3_lapsed"].Select(g => string.Join("+", g)).OrderBy(g => g)
                    .SequenceEqual(new[] { "chapter.six", "greybor.away", "greybor.dead", "greybor.kicked_out", "greybor.q3_failed" }),
            "Trk_Horzalah_Bindings: horzalah.dead or horzalah.q3_lapsed does not extend the merged keys as the build sheet says.");
        var presence = story.Presences["horzalah.presence"];
        check(presence.Unit == Unit && presence.Area == Drezen && presence.Mode == "spawn-copy" && presence.Dialog == "hub"
              && presence.At?.NearUnit == "da4c28dd01413694f82b08b728a8c6e5" && presence.At?.Side == "left" && presence.At?.Distance == 2.0f
              && presence.MinChapter == 5 && presence.MaxChapter == 5
              && presence.Requires.Contains(Wants) && presence.Forbids.Contains(Closed) && presence.Forbids.Contains(LeftFree),
            "Her presence is not the spawn-copy left of the Storyteller (Vellexia stands right), Chapter 5, after she said what she wants.");
        check(!own.Any(s => s.AnswerLists.Contains("0f12118177d102f428a3b30b15b132eb") || s.AnswerLists.Contains("a380d926e92f70e429681eb9654478f9")
                            || s.AnswerLists.Contains("15f754455d1d87c42a4e14df456d5415")),
            "A Horzalah scene hangs on a crowded hub (Fye, the yard, the smith).");
        check(story.Scenes.Where(s => s.Relationship == "horzalah").All(s => !s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                  .Any(f => f.StartsWith("hepzamirah.", StringComparison.Ordinal))),
            "A Horzalah scene gates on Hepzamirah (node variants only).");
        check(!own.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal))))),
            "Horzalah's device spends a Word Made True (the budget is full: a con, not a word made true).");
        // Path fit (v1): the two Chapter 4 build-up beats carry no Trickster gate; everything after the device does.
        var buildUp = new[] { scar, box5 };
        check(buildUp.All(b => !b.Requires.Any(f => f.StartsWith("trickster", StringComparison.Ordinal)))
              && own.Concat(reactions).Concat(pages).Where(s => !buildUp.Contains(s)).All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever")),
            "Path fit: a build-up beat is Trickster-gated, or a device-side scene is not.");

        // Chapter 4 (N-all): the scar in Yozz's hall and the box after Colyphyr.
        var ch4 = World(story, 4, "horzalah.scar_seen");
        check(Avail(scar, ch4) && scar.AnswerLists.SequenceEqual(new[] { YozzList }) && scar.NativeReturnCue == ScarCue
              && Take(scar, ch4, "who", 0, P + "scar_noted").Has(P + "scar_noted") && Ch(scar, "look", 2).Abort,
            "The Chapter 4 scar beat is not inline on YozzDying's list, returning to Cue_0049, with a silent abort.");
        check(Avail(box5, World(story, 5, "horzalah.met_q2")) && Rules.IsRemote(box5) && box5.Kind == "letter" && box5.MinChapter == 5
              && !Avail(box5, World(story, 5, "horzalah.met_q2", "horzalah.met_q3_a")) && !Avail(box5, World(story, 5, "horzalah.met_q2", Primed))
              && !story.Scenes.Any(s => s.Relationship == "horzalah" && Rules.IsRemote(s) && s.MinChapter <= 4),
            "The empty box does not arrive at the start of Chapter 5, once, before the ambush, or a Horzalah page arrives in Chapter 4.");

        // Trk_Horzalah_Mercy: the guess, the story, her knife; the Guild kept; her gift; the collar; the chamber.
        var m = World(story, 5, "trickster", "trickster.ever");
        check(Avail(mercy, m) && mercy.TricksterDevice && mercy.TricksterState == "mercy" && mercy.EntryMythic == "PlayerIsTrickster"
              && mercy.AnswerLists.SequenceEqual(new[] { MercyList }) && mercy.NativeReturnCue == MercyReturn,
            "Trk_Horzalah_Mercy: the story is not offered inline at her mercy (AnswersList_0001, back to Cue_4), on the live path.");
        var pitch = mercy.Nodes.Single(n => n.Id == "guild").Choices.Where(c => c.Check != null).ToList();
        check(pitch.Count == 3 && pitch.All(c => c.Check!.Skill == "CheckDiplomacy" && c.Check.Success == "ear" && c.Check.Failure == "refused")
              && pitch[0].Check!.DC == 22 && pitch[0].Requires.Contains("baphomet.named_horzalah")
              && pitch[1].Check!.DC == 24 && pitch[1].Requires.Contains(P + "scar_noted") && pitch[1].Forbids.Contains("baphomet.named_horzalah")
              && pitch[2].Check!.DC == 26,
            "Trk_Horzalah_Mercy: the story is not Diplomacy DC 26 (24 after the scar, 22 with her father's words).");
        check(mercy.Nodes.SelectMany(n => n.Choices).Where(c => c.Next == null && c.Check == null && !c.Abort).All(c => c.NativeNext == Farewell)
              && !Program.Walk(mercy, m).Any(r => r.Has("horzalah.killed") || r.Has("horzalah.dismissed")),
            "Trk_Horzalah_Mercy: an ending does not play her own farewell, or the story records a kill or a dismissal.");
        var gave = Take(mercy, m, "exit", 0, Primed, Ear, Started);
        check(!Avail(kept, Later(story, gave, 24)) && Avail(kept, Later(story, gave, 48)), "Trk_Horzalah_Mercy: the Guild is not kept two days on.");
        var wants = Take(kept, Later(story, gave, 48), "wants", 0, Returned, Wants);
        check(!Avail(gift, Later(story, wants, 24)) && Avail(gift, Later(story, wants, 48)) && !Avail(giftNight, Later(story, wants, 48)),
            "Trk_Horzalah_Mercy: her gift does not wait two days at her presence.");
        var decline = Take(gift, Later(story, wants, 48), "decline_end", 0, Tested);
        check(Ch(gift, "gift", 1).Alignment?.Direction == "Good" && Ch(gift, "gift", 2).Alignment?.Direction == "Evil"
              && Take(gift, Later(story, wants, 48), "free2", 0, Tested, P + "cost.gift_freed").Has(Tested)
              && Take(gift, Later(story, wants, 48), "accept2", 0, Ally).Has(Ally) && !Program.Walk(gift, Later(story, wants, 48)).Any(r => r.Has(Ally) && r.Has(Tested)),
            "Trk_Horzalah_Mercy: her gift is not the pivot (decline; free him, Good; accept him, Evil, a business ally only).");
        check(!Avail(collar, Later(story, World(story, 5, "trickster.ever", Primed, Returned, Wants, Ally), 72)),
            "Trk_Horzalah_Mercy: an owner of people still reaches the collar.");
        var yes = Take(collar, Later(story, decline, 24), "word3", 0, Committed);
        check(Ch(collar, "look", 0).Next == "word" && Ch(collar, "look", 1).Next == "buyer" && Ch(collar, "look", 2).Next == "brand"
              && collar.Nodes.Where(n => n.Id.StartsWith("word", StringComparison.Ordinal)).SelectMany(n => n.Choices).All(c => c.Check == null && c.Crusade == null),
            "Trk_Horzalah_Mercy: the collar is not wait / reach / ask, or her yes carries a test or a price.");
        check(!Avail(chamber, Later(story, yes, 12)) && Avail(chamber, Later(story, yes, 24)), "Trk_Horzalah_Mercy: the chamber does not follow the collar.");
        var morning = Take(chamber, Later(story, yes, 24), "morning2", 0, Chamber, Morning);
        check(morning.Has(Committed) && NoKill(morning), "Trk_Horzalah_Mercy: the chamber does not end in the morning her assassins see.");

        // Trk_Horzalah_NoGreybor: she comes herself when Greybor's third quest cannot happen.
        var ng = World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after");
        check(Avail(unmet, ng) && unmet.TricksterDevice && unmet.TricksterState == "unmet" && Rules.IsRemote(unmet),
            "Trk_Horzalah_NoGreybor: she does not come herself when Greybor never finished his second quest.");
        check(!Avail(unmet, World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done"))
              && Avail(unmet, World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "greybor.q3_failed"))
              && Avail(unmet, World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "greybor.dead"))
              && Avail(unmet, World(story, 6, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "chapter.six")),
            "Trk_Horzalah_NoGreybor: the night does not wait for Greybor's third quest, or does not come once it lapses.");
        var killed = Take(unmet, ng, "kill", 0, P + "killed_unmet", Closed);
        check(Later(story, killed, 0).Has(Dead) && !own.Any(s => Avail(s, Later(story, killed, 72))),
            "Trk_Horzalah_NoGreybor: a kill in the night is not her death, or something still plays after it.");
        var unmetYes = Take(unmet, ng, "exit", 0, Primed, Ear, P + "came_herself");
        check(Avail(kept, Later(story, unmetYes, 48)), "Trk_Horzalah_NoGreybor: the story told on the floor of the room does not reach the Guild kept.");

        // Trk_Horzalah_FirstSight: met at the ambush, the mercy dialog decides; the night never duplicates it.
        var sight = World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "greybor.dead", "horzalah.met_q3_a");
        check(!Avail(unmet, sight) && Avail(mercy, sight) && !Avail(unmet, World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "horzalah.met_q3_b")),
            "Trk_Horzalah_FirstSight: the night fires in a world where the ambush already met her.");

        // Trk_Horzalah_KillStands: a player-chosen kill closes the route; canon stands (user ruling §5 #2).
        foreach (var kill in new[] { "horzalah.killed", "horzalah.killed_b" })
        {
            var k = World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "horzalah.met_q3_a", kill);
            check(k.Has(Dead) && !own.Any(s => Avail(s, Later(story, k, 72))) && !pages.Any(s => Avail(s, World(story, 6, "trickster.ever", kill))),
                "Trk_Horzalah_KillStands: a scene or page plays after " + kill + ".");
        }

        // Trk_Horzalah_RefusedLate: her refusal, the Guild circling, the ear taken at night.
        var refused = Take(mercy, m, "refused", 0, Refused, Started);
        check(!Avail(late, Later(story, refused, 12)) && Avail(late, Later(story, refused, 24)) && late.TricksterDevice,
            "Trk_Horzalah_RefusedLate: the Guild does not circle a day after her refusal.");
        var lateYes = Take(late, Later(story, refused, 24), "no_priest", 0, Primed, Ear, Late);
        check(Ch(late, "no_priest", 0).Crusade?.Resource == "Favors" && Ch(late, "no_priest", 0).Crusade?.Amount == -100
              && Ch(late, "head", 0).Requires.Contains(Refused) && Ch(late, "head", 1).Forbids.Contains(Refused)
              && Take(late, Later(story, refused, 24), "guard", 0, Closed).Has(P + "guard_called"),
            "Trk_Horzalah_RefusedLate: the night costs no Favors, or the guard does not close.");
        var dismissed = World(story, 5, "trickster", "trickster.ever", "horzalah.met_q3_b", "horzalah.dismissed_b");
        check(dismissed.Has("horzalah.dismissed.latched") && Avail(late, Later(story, dismissed, 24)),
            "Trk_Horzalah_RefusedLate: the native dismissal does not reach the night.");
        var declined = Take(collar, Later(story, Take(gift, Later(story, Take(kept, Later(story, lateYes, 48), "wants", 0, Wants), 48), "decline_end", 0, Tested), 24), "buyer", 0, Declined);
        check(!declined.Has(Committed) && !Avail(move, Later(story, declined, 12)) && Avail(move, Later(story, declined, 24)),
            "Trk_Horzalah_RefusedLate: her soft no does not hold a day before she moves.");
        check(Take(move, Later(story, declined, 48), "yes", 0, Committed).Has(Committed) && Take(move, Later(story, declined, 48), "go", 0, LeftFree).Has(LeftFree)
              && Take(collar, Later(story, Take(gift, Later(story, wants, 48), "decline_end", 0, Tested), 24), "brand", 0, Declined).Has(Declined),
            "Trk_Horzalah_RefusedLate: asking whose mark it is is not her soft no, or her own move is not the yes.");

        // Trk_Horzalah_PathFailed: nothing new opens off the path.
        var lost = World(story, 5, "trickster.ever", "trickster.was", "trickster.failed", "iz.done", "coronation.after", "horzalah.dismissed");
        check(!Avail(mercy, lost) && !Avail(unmet, lost) && !Avail(late, Later(story, lost, 24)),
            "Trk_Horzalah_PathFailed: a device fires after the path is lost.");

        // Trk_Horzalah_AllRomanceWalk: every contact state reaches the commit without a kill.
        var roads = new List<(string name, Snapshot start, Scene entry, string node)>
        {
            ("mercy", World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "horzalah.met_q3_a"), mercy, "exit"),
            ("unmet", ng, unmet, "exit"),
            ("lapsed", World(story, 5, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "greybor.q3_failed"), unmet, "exit"),
        };
        foreach (var (name, start, entry, node) in roads)
        {
            var s0 = Take(entry, start, node, 0, Primed);
            var s1 = Take(kept, Later(story, s0, 48), "wants", 0, Wants);
            var s2 = Take(gift, Later(story, s1, 48), "free2", 0, Tested);
            var s3 = Take(collar, Later(story, s2, 24), "word3", 1, Committed);
            check(s3.Has(Committed) && NoKill(s3), "Trk_Horzalah_AllRomanceWalk_" + name + ": no clean road to the commit.");
        }

        // The presence failed: the night twins carry the test and both commits.
        var nf = World(story, 5, "trickster.ever", Primed, Returned, Wants, Failed);
        nf.AvailableContacts.Clear();
        check(!Avail(gift, Later(story, nf, 48)) && Avail(giftNight, Later(story, nf, 48)) && Rules.IsRemote(giftNight) && giftNight.Kind == "visit",
            "The presence failed and the gift has no night twin.");
        var nfTested = Take(giftNight, Later(story, nf, 48), "decline_end", 0, Tested);
        check(Avail(collarNight, Later(story, nfTested, 24)) && Take(collarNight, Later(story, nfTested, 24), "word3", 0, Committed).Has(Committed)
              && Avail(moveNight, Later(story, World(story, 5, "trickster.ever", Wants, Tested, Declined, Failed), 48)),
            "The presence failed and the collar or her move has no night twin.");

        // Pages.
        var pg = pages.ToDictionary(s => s.Id.Substring(P.Length));
        check(pages.Length == 7 && pages.All(s => s.MinChapter == 6 && s.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.RemoveItem == null && c.Crusade == null))),
            "Horzalah's pages are not seven effect-free Chapter 6 pages.");
        check(Avail(pg["epilogue.together"], World(story, 6, "trickster.ever", Committed, Ear))
              && Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Wants)) && !Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Wants, Committed))
              && Avail(pg["epilogue.decided"], World(story, 6, "trickster.ever", Wants, Declined)) && !Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Wants, Declined))
              && Avail(pg["epilogue.left_free"], World(story, 6, "trickster.ever", LeftFree))
              && Avail(pg["epilogue.ally"], World(story, 6, "trickster.ever", Ally))
              && Avail(pg["epilogue.scarred"], World(story, 6, "trickster.ever", P + "threatened", Closed))
              && Avail(pg["epilogue.closed"], World(story, 6, "trickster.ever", Started, Closed, P + "guard_called"))
              && !Avail(pg["epilogue.closed"], World(story, 6, "trickster.ever", Started, Closed, P + "threatened")),
            "Horzalah's pages do not follow the states (together, the late commit, her decision, free, ally, scarred, closed).");
        check(story.Derived[P + "late_committed"].Any(g => g.Contains(Wants)) && story.Derived["horzalah.harem.eligible"].Any(g => g.Length == 1 && g[0] == P + "late_committed"),
            "The late commit is not the R2-6 late_committed key, or eligibility ignores it.");

        // Reactors: Greybor (whose contract she held) and Wenduag, on their own hubs.
        check(reactions.Length == 8 && reactions.Select(s => s.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Greybor", "Wenduag" })
              && reactions.All(s => s.AnswerLists.Length == 1 && s.Forbids.Length > 0),
            "Horzalah's reactions are not Greybor and Wenduag on their hubs, each with its guard.");

        // Rest budget (spec §10: two Chapter 5 letters on the worst branch, none in Chapter 6). Every rest-delivered page
        // presented as a letter counts, whatever its id: the Chapter 5 box, her first letter and the Guild's invoice. The first
        // letter and the invoice are exclusive (an ally gets only the invoice), so no branch reads more than two.
        var mail = story.Scenes.Where(s => s.Relationship == "horzalah" && Rules.IsRemote(s) && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)
                                           && Rules.KindOf(s) == "letter").ToArray();
        var ch5Mail = mail.Where(s => s.MinChapter <= 5 && s.MaxChapter >= 5).Select(s => s.Id).OrderBy(x => x).ToArray();
        var first = mail.Single(s => s.Id == P + "letter.first");
        var invoice = mail.Single(s => s.Id == P + "letter.invoice");
        check(ch5Mail.SequenceEqual(new[] { P + "ch5.nothing", P + "letter.first", P + "letter.invoice" })
              && first.Forbids.Contains(Ally) && invoice.Requires.Contains(Ally) && !mail.Any(s => s.MaxChapter >= 6),
            "Horzalah's letters exceed two on the worst Chapter 5 branch, or one arrives in Chapter 6: " + string.Join(",", ch5Mail));

        // Trk_Horzalah_Chapter6: the Greybor-less night after Q3 lapsed at Chapter 6 still carries her test, her yes, the
        // chamber and her Last Call coda (the room twins stand in for her presence, which is Chapter 5 only).
        var c6 = World(story, 6, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "chapter.six");
        var c6a = Take(unmet, c6, "exit", 0, Primed, Ear);
        var c6b = Take(kept, Later(story, c6a, 48), "wants", 0, Wants);
        check(!Avail(gift, Later(story, c6b, 48)), "Trk_Horzalah_Chapter6: her Chapter 5 presence opens in Chapter 6.");
        var c6c = Take(giftNight, Later(story, c6b, 48), "decline_end", 0, Tested);
        var c6d = Take(collarNight, Later(story, c6c, 24), "word3", 0, Committed);
        var c6e = Take(chamber, Later(story, c6d, 24), "morning2", 0, Chamber, Morning);
        var coda = story.Scenes.Single(s => s.Id == "horzalah.lastcall.page");
        check(c6e.Has(Committed) && NoKill(c6e) && coda.Requires.Contains(Committed),
            "Trk_Horzalah_Chapter6: the Chapter 6 road loses her test, her yes, the chamber or her Last Call coda.");
        // H2 (Last Call's bottle brings the Commander back with sacrifice held) keeps her romantic pages, as the native endings do.
        var h2 = World(story, 6, "trickster.ever", Committed, Ear, "sacrifice", "trickster.lastcall.taken", "ending.wound_closed", "trickster.lastcall.pillar.bottle");
        check(h2.Has("trickster.commander_back") && Avail(pg["epilogue.together"], h2)
              && Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Wants, "sacrifice", "trickster.lastcall.taken", "ending.wound_closed", "trickster.lastcall.pillar.bottle"))
              && !Avail(pg["epilogue.together"], World(story, 6, "trickster.ever", Committed, "sacrifice")),
            "H2 survival suppresses her pages, or a Commander who stayed dead still gets them.");
        // Reactors speak only while with the Commander: Wenduag and Greybor need their in-party states.
        check(reactions.Where(s => s.Owner == "Wenduag").All(s => s.Requires.Contains("wenduag.in_party") && s.Forbids.Contains("wenduag.killed"))
              && reactions.Where(s => s.Owner == "Greybor").All(s => s.Requires.Contains("greybor.in_party") && s.Forbids.Contains("greybor.dead")),
            "A reactor speaks without being with the Commander, or after a native death.");

        // Courtship: every beat and letter is reachable on some road.
        check(beats.Length == 27 && letters.Length == 2 && letters.All(s => Rules.IsRemote(s) && s.Kind == "letter" && s.Chapters.SequenceEqual(new[] { 5 }))
              && beats.All(s => s.ContactUnit == Unit && s.InteractionHub == "horzalah.presence" && s.Optional),
            "Horzalah's courtship is not twenty-seven beats on her presence and two Chapter 5 letters.");
        var reachedIds = new HashSet<string>();
        void Play(Snapshot start, int chapter, int rounds, params string[] avoid)
        {
            var state = start;
            for (int i = 0; i < rounds; i++)
            {
                state = Later(story, state, 48, chapter);
                foreach (var scene in own.Where(s => Avail(s, state)).ToList())
                {
                    if (!Avail(scene, state)) continue;
                    var outcome = Program.Walk(scene, state).FirstOrDefault(r => r.Has(scene.Id) && !r.Has(Closed) && !avoid.Any(r.Has));
                    if (outcome == null) continue;
                    reachedIds.Add(scene.Id);
                    state = outcome;
                }
            }
        }
        // Her cell in the Ivory Labyrinth is talked of only with a Commander who has been in her father's prison.
        var labyrinth = beats.Single(s => s.Id == P + "beat.labyrinth");
        check(labyrinth.Requires.Contains("baphomet.parley.latched")
              && !Avail(labyrinth, Later(story, World(story, 5, "trickster.ever", Wants, P + "beat.father_heard", P + "beat.sister_heard"), 48)),
            "The Labyrinth beat plays for a Commander who never walked the Labyrinth.");
        // The longest road after the coronation (dismissed or refused, the Guild circling, her gift, the soft no, her move)
        // reaches the commit within 168 hours.
        check(late.DelayHours + kept.DelayHours + gift.DelayHours + collar.DelayHours + move.DelayHours <= 168
              && giftNight.DelayHours == gift.DelayHours && moveNight.DelayHours == move.DelayHours && collarNight.DelayHours == collar.DelayHours,
            "The refusal road to her commit is longer than 168 hours.");
        var road = World(story, 5, "trickster", "trickster.ever", "greybor.in_party", "horzalah.met_q3_a", "baphomet.named_horzalah", "baphomet.parley",
            "horzalah.gift_delivered", "hepzamirah.trickster.returned", "horzalah.met_q2", P + "scar_noted", P + "cost.late");
        Play(road, 5, 20, Ally, LeftFree, Declined, P + "threatened");
        Play(World(story, 5, "trickster", "trickster.ever", Primed, Ear, Returned, Wants, Ally), 5, 6);
        Play(World(story, 6, "trickster", "trickster.ever", Primed, Ear, Returned, Wants, Tested, Committed, Chamber), 6, 2);
        Play(World(story, 6, "trickster", "trickster.ever", Primed, Ear, Returned, Wants), 6, 2);
        Play(World(story, 5, "trickster", "trickster.ever", Primed, Ear, Returned, Wants, Tested, Declined), 5, 2, Committed, LeftFree);
        foreach (var scene in beats.Concat(letters))
            check(reachedIds.Contains(scene.Id), "Horzalah: the beat " + scene.Id + " is never reachable.");
        Console.WriteLine("PASS: Horzalah Trickster (Trk_Horzalah_*): the scar and the box, the mercy node and its twins, the Greybor-less night, "
                          + "the Guild circling, the Guild kept, her gift, the collar and her move, the chamber, the kill that stands, the night twins, "
                          + "the pages, the reactors, " + beats.Length + " beats and " + letters.Length + " letters.");
    }
}
