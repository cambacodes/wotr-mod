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
        // eng8-q8f: funded positive predicate fixtures; negatives explicitly remove funds.
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = Drezen,
            CrusadeResources = new Dictionary<string, int> { ["Favors"] = 100, ["Finances"] = 150 } };
        // end eng8-q8f
        state.AvailableContacts.Add(Unit);
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        // Native ending/Last Call checkpoint flags expand to their actual sources.
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    // Round 2 authority pages consume the completed con and report receipts.
    // Keep transaction and unpaid-closure fixtures on World, without these inputs.
    private static Snapshot PaidWorld(Story story, int chapter, params string[] flags) =>
        World(story, chapter, new[] { Primed, Ear, Returned }.Concat(flags).ToArray());

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
        // Take: the scene must be available, and the outcome must have traversed exactly that choice.
        List<Snapshot> Through(Scene scene, Snapshot w, string node, int index)
        {
            check(Avail(scene, w), "Not available before taking " + scene.Id + "/" + node + "[" + index + "]");
            // eng8-q8f: shared production affordability, debit, entry and abort processing.
            var hits = Program.WalkVia(scene, w, node, index);
            // end eng8-q8f
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
        var reactions = story.Scenes.Where(s => s.Id.StartsWith(P + "react.", StringComparison.Ordinal) && s.Reaction).ToArray();
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
              && rel.UnavailableFlags.SequenceEqual(new[] { Dead, P + "left_free" }) && rel.UnavailableOverrides.Count == 0
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
              && story.SeenCues["baphomet.spawn_told"].SequenceEqual(new[] { "0cdc1a24d29c77f4490900d3a9418afc" })
              && story.SeenCues["horzalah.seals_seen"].SequenceEqual(new[] { "fc1030e8724b086479d7ec2a52aae2a5" })
              && story.SeenCues["horzalah.rescue_refused_told"].SequenceEqual(new[] { "fc5119d8d4a54e047b07338764beb346" })
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
        check(Avail(scar, ch4) && scar.AnswerLists.SequenceEqual(new[] { YozzList }) && scar.ReturnToList && scar.NativeReturnCue == null
              && Take(scar, ch4, "who", 0, P + "scar_noted").Has(P + "scar_noted") && Ch(scar, "look", 2).Abort,
            "The Chapter 4 scar beat is not inline on YozzDying's list, returning to the list (not replaying Cue_0049), with a silent abort.");
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

        // H01/H03: carry the real guard closures forward; neither start state earns Started.
        check(!ng.Has(Started), "H03: fresh unmet fixture already has Started.");
        var failedCombat = Take(unmet, ng, "outmatched", 0, Closed, P + "guard_called");
        check(failedCombat.Has(Started) && Avail(S(P + "epilogue.closed"), Later(story, failedCombat, 72, 6)),
            "H01/H03: fresh failed combat does not earn the doubled-watch Chapter 6 page.");

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
        check(!dismissed.Has(Started), "H03: native dismissal fixture already has Started.");
        var dismissedGuard = Take(late, Later(story, dismissed, 24), "guard", 0, Closed, P + "guard_called");
        check(dismissedGuard.Has(Started) && Avail(S(P + "epilogue.closed"), Later(story, dismissedGuard, 72, 6)),
            "H01/H03: native dismissal then guard does not earn the doubled-watch Chapter 6 page.");
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
        // eng7-l13: new commitments on fallback visits require current power.
        var nf = World(story, 5, "trickster", "trickster.ever", Primed, Returned, Wants, Failed);
        nf.AvailableContacts.Clear();
        check(!Avail(gift, Later(story, nf, 48)) && Avail(giftNight, Later(story, nf, 48)) && Rules.IsRemote(giftNight) && giftNight.Kind == "visit",
            "The presence failed and the gift has no night twin.");
        var nfTested = Take(giftNight, Later(story, nf, 48), "decline_end", 0, Tested);
        check(Avail(collarNight, Later(story, nfTested, 24)) && Take(collarNight, Later(story, nfTested, 24), "word3", 0, Committed).Has(Committed)
              && Avail(moveNight, Later(story, World(story, 5, "trickster.ever", Wants, Tested, Declined, Failed), 48)),
            "The presence failed and the collar or her move has no night twin.");

        // Pages.
        var pg = pages.ToDictionary(s => s.Id.Substring(P.Length));
        check(pages.Length == 9 && pages.All(s => s.MinChapter == 6 && s.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.RemoveItem == null && c.Crusade == null))),
            "Horzalah's pages are not nine effect-free Chapter 6 pages.");
        check(Avail(pg["epilogue.together"], PaidWorld(story, 6, "trickster.ever", Committed, Ear))
              && Avail(pg["epilogue.commit"], PaidWorld(story, 6, "trickster", "trickster.ever", Wants, Tested)) && !Avail(pg["epilogue.commit"], PaidWorld(story, 6, "trickster.ever", Wants, Tested, Committed))
              && !Avail(pg["epilogue.commit"], PaidWorld(story, 6, "trickster.ever", Wants)) && Avail(pg["epilogue.unanswered"], PaidWorld(story, 6, "trickster.ever", Wants))
              && !Avail(pg["epilogue.unanswered"], PaidWorld(story, 6, "trickster.ever", Wants, Tested))
              && Avail(pg["epilogue.decided"], PaidWorld(story, 6, "trickster.ever", Wants, Declined)) && !Avail(pg["epilogue.commit"], PaidWorld(story, 6, "trickster.ever", Wants, Declined))
              && Avail(pg["epilogue.left_free"], PaidWorld(story, 6, "trickster.ever", LeftFree))
              && Avail(pg["epilogue.ally"], PaidWorld(story, 6, "trickster.ever", Ally))
              && Avail(pg["epilogue.scarred"], PaidWorld(story, 6, "trickster.ever", P + "threatened", Closed))
              && Avail(pg["epilogue.closed"], PaidWorld(story, 6, "trickster.ever", Started, Closed, P + "guard_called"))
              && !Avail(pg["epilogue.closed"], PaidWorld(story, 6, "trickster.ever", Started, Closed, P + "threatened")),
            "Horzalah's pages do not follow the states (together, the late commit, her decision, free, ally, scarred, closed).");
        check(story.Derived[P + "late_committed"].Any(g => g.Contains(Tested)) && story.Derived["horzalah.harem.eligible"].Any(g => g.Length == 1 && g[0] == P + "late_committed"),
            "The late commit is not the R2-6 late_committed key, or eligibility ignores it.");

        // Reactors: Greybor (whose contract she held) and Wenduag, on their own hubs.
        check(reactions.Length == 10 && reactions.Select(s => s.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Greybor", "Wenduag" })
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

        // Chronologically: a Commander who read her first letter and then accepted her gift gets no invoice on top of it.
        var readFirst = Take(first, Later(story, World(story, 5, "trickster", "trickster.ever", Primed, Ear, Returned, Wants), 72), "vials", 0, P + "letter.first_read");
        var boughtAfter = Take(gift, Later(story, readFirst, 48), "accept2", 0, Ally);
        check(!Avail(invoice, Later(story, boughtAfter, 96)) && Avail(invoice, Later(story, World(story, 5, "trickster.ever", Wants, Ally), 96)),
            "A Commander who read her first letter and then bought her gift also gets the invoice (three letters).");

        // The late page keeps the gift's history: offered only if it never was; the freed hatter and the declined gift remembered.
        var latePage = pages.Single(s => s.Id == P + "epilogue.commit").Nodes[0];
        int Shown(Snapshot st, string fragment) => latePage.Paragraphs.Count(q => Rules.ParagraphVisible(q, st) && SurfaceIds.Has(SurfaceIds.Of(story, q), fragment));
        var neverTested = World(story, 6, "trickster.ever", Wants, Tested);
        var freedLate = World(story, 6, "trickster.ever", Wants, Tested, P + "cost.gift_freed");
        // A Commander who stayed dead gets the mourning page, never a page that assumes a long life; one brought back keeps them.
        var dead = new[] { "trickster.ever", Started, "sacrifice" };
        var back = new[] { "trickster.ever", Started, "sacrifice", "trickster.lastcall.taken", "ending.wound_closed", "trickster.lastcall.pillar.bottle" };
        foreach (var (id, flags) in new[] { ("epilogue.left_free", new[] { LeftFree }), ("epilogue.ally", new[] { Ally }),
                                            ("epilogue.scarred", new[] { P + "threatened", Closed }), ("epilogue.closed", new[] { Closed, P + "guard_called" }),
                                            ("epilogue.together", new[] { Committed }) })
            check(!Avail(pg[id], PaidWorld(story, 6, dead.Concat(flags).ToArray())) && Avail(pg[id], PaidWorld(story, 6, back.Concat(flags).ToArray()))
                  && Avail(pg["epilogue.mourned"], PaidWorld(story, 6, dead.Concat(flags).ToArray())) == !flags.Contains(LeftFree)
                  && !Avail(pg["epilogue.mourned"], PaidWorld(story, 6, back.Concat(flags).ToArray())),
                "A living-Commander page plays after a permanent sacrifice, or the mourning page does not: " + id);
        var declinedLate = World(story, 6, "trickster.ever", Wants, Tested);
        check(Shown(freedLate, "[horzalah.trickster.epilogue.commit/page/paragraph/0]") == 1 && Shown(declinedLate, "[horzalah.trickster.epilogue.commit/page/paragraph/0]") == 0 && Shown(declinedLate, "[horzalah.trickster.epilogue.commit/page/paragraph/1]") == 1 && Shown(freedLate, "[horzalah.trickster.epilogue.commit/page/paragraph/1]") == 0,
            "The late page offers the gift again, or forgets how it went.");
        // The dwarf's three mistakes are remembered only where he told them (Horzalah_Mercy/Cue_0011).
        var dwarfStart = beats.Single(s => s.Id == P + "beat.dwarf").Nodes.Single(n => n.Id == "start").Choices;
        check(dwarfStart.Single(c => c.Next == "betrayed").Requires.Contains("horzalah.greybor_explained")
              && dwarfStart.Single(c => c.Next == "betrayed_plain").Forbids.Contains("horzalah.greybor_explained")
              && story.SeenCues["horzalah.greybor_explained"].SequenceEqual(new[] { "ae22177b1bc76fc42a9d08dba83cccdc" }),
            "The dwarf's lecture is remembered in a world where he never gave it.");

        // Trk_Horzalah_Chapter6: the Greybor-less night after Q3 lapsed at Chapter 6 ends on the pages (the one-rest Chapter 6
        // budget): no presence, no room twins; her gift left unanswered is the open page. The Last Call coda needs the commit.
        var c6 = World(story, 6, "trickster", "trickster.ever", "iz.done", "coronation.after", "greybor.q2_done", "chapter.six");
        var c6a = Take(unmet, c6, "eng8.guild.decline_end_6", 0, Primed, Ear, Wants, Tested, Returned);
        // Q12 (Sol COX/HOW): in Chapter 6 the gift comes with her to the same visit, so the romantic page is reachable with
        // no extra delivery: the Chapter 5 "wants" answer is shut, "wants6" leads into the room version of the gift.
        var pivotChoices = kept.Nodes.Single(n => n.Id == "pivot").Choices;
        check(pivotChoices.Single(ch => ch.Next == "wants").Forbids.Contains("chapter.six") && pivotChoices.Last().Next == "wants6"
              && pivotChoices.Last().Requires.Contains("chapter.six") && !Rules.Match(pivotChoices[0].Requires, pivotChoices[0].Forbids, Later(story, c6a, 48)),
            "Trk_Horzalah_Chapter6: the Chapter 5 answer (no gift) plays in Chapter 6, or the Chapter 6 answer was not appended.");
        var c6b = Take(unmet, c6, "eng8.guild.decline_end_6", 0, Wants, Tested, Returned);
        var c6free = Take(unmet, c6, "eng8.guild.free2_6", 0, Wants, Tested, P + "cost.gift_freed");
        var c6ally = Take(unmet, c6, "eng8.guild.accept2_6", 0, Wants, Ally);
        check(!Avail(gift, Later(story, c6b, 48)) && !Avail(giftNight, Later(story, c6b, 48))
              && !Avail(giftNight, Later(story, World(story, 6, "trickster.ever", Wants, "horzalah.presence.failed"), 48))
              && Avail(pg["epilogue.commit"], World(story, 6, c6b.Flags.ToArray())) && Avail(pg["epilogue.commit"], World(story, 6, c6free.Flags.ToArray()))
              && Avail(pg["epilogue.ally"], World(story, 6, c6ally.Flags.ToArray())) && !Avail(pg["epilogue.unanswered"], World(story, 6, c6b.Flags.ToArray()))
              && story.Scenes.Single(s => s.Id == "horzalah.lastcall.page").Requires.Contains(Committed),
            "Trk_Horzalah_Chapter6: a presence scene plays in Chapter 6, or the Chapter 6 road cannot reach her romantic page.");
        // Chapter 5 keeps its road: the plain answer, no gift on the spot.
        var ch5Kept = Later(story, World(story, 5, "trickster", "trickster.ever", Primed, Ear), 48);
        check(Through(kept, ch5Kept, "wants", 0).Any() && !Rules.Match(pivotChoices.Last().Requires, pivotChoices.Last().Forbids, ch5Kept),
            "Trk_Horzalah_Chapter6: the Chapter 6 gift leaks into Chapter 5.");
        // Q12 (Sol INT): a Wenduag back on her own Trickster route speaks from her presence by the south gate.
        var street = story.Scenes.Where(s => s.Id.StartsWith(P + "react.wenduag_", StringComparison.Ordinal) && s.Id.EndsWith("_street", StringComparison.Ordinal)).ToArray();
        check(street.Length == 4 && street.All(s => s.Relationship == "wenduag" && s.InteractionHub == "wenduag.presence"
                  && s.Requires.Contains("wenduag.trickster.returned") && s.Forbids.Contains("wenduag.in_party")
                  && !s.Forbids.Contains("wenduag.killed") && !s.Forbids.Contains("wenduag.kicked_out")),
            "Trk_Horzalah_Wenduag: a returned Wenduag has no word on Horzalah.");
        // H2 (Last Call's bottle brings the Commander back with sacrifice held) keeps her romantic pages, as the native endings do.
        var h2 = PaidWorld(story, 6, "trickster.ever", Committed, Ear, "sacrifice", "trickster.lastcall.taken", "ending.wound_closed", "trickster.lastcall.pillar.bottle");
        check(h2.Has("trickster.commander_back") && Avail(pg["epilogue.together"], h2)
              && Avail(pg["epilogue.commit"], PaidWorld(story, 6, "trickster", "trickster.ever", Wants, Tested, "sacrifice", "trickster.lastcall.taken", "ending.wound_closed", "trickster.lastcall.pillar.bottle"))
              && !Avail(pg["epilogue.together"], PaidWorld(story, 6, "trickster.ever", Committed, "sacrifice")),
            "H2 survival suppresses her pages, or a Commander who stayed dead still gets them.");
        // Reactors speak only while with the Commander: Wenduag and Greybor need their in-party states.
        check(reactions.Where(s => s.Owner == "Wenduag").All(s => s.Requires.Contains("wenduag.in_party") && s.Forbids.Contains("wenduag.killed"))
              && reactions.Where(s => s.Owner == "Greybor").All(s => s.Requires.Contains("greybor.in_party") && s.Forbids.Contains("greybor.dead")),
            "A reactor speaks without being with the Commander, or after a native death.");

        // Choices in the courtship leave traces: the board's names, the poisoned cup, the touch before and after her yes.
        var namesBeat = beats.Single(s => s.Id == P + "beat.names");
        var warned = World(story, 5, "trickster.ever", Wants, P + "beat.board_heard", P + "beat.board_warned");
        var left = World(story, 5, "trickster.ever", Wants, P + "beat.board_heard", P + "beat.board_left");
        check(Take(namesBeat, Later(story, warned, 72), "lord", 0, P + "beat.names_known").Has(P + "beat.board_warned")
              && Take(namesBeat, Later(story, left, 72), "left", 0, P + "beat.names_known").Has(P + "beat.board_left")
              && !Avail(namesBeat, Later(story, World(story, 5, "trickster.ever", Wants, P + "beat.board_heard"), 72)),
            "The names on her board lead nowhere, or lead to the same place whatever the Commander did.");
        var question = beats.Single(s => s.Id == P + "beat.question");
        check(Through(question, Later(story, World(story, 5, "trickster.ever", Wants, Tested, P + "beat.cup_drunk", P + "beat.cup_sick"), 48), "opening", 0).Any()
              && Through(question, Later(story, World(story, 5, "trickster.ever", Wants, Tested, P + "beat.cup_drunk", P + "beat.cup_dreams"), 48), "opening", 1).Any(),
            "The poisoned cup is forgotten the next time she speaks to the Commander.");
        var hunger = beats.Single(s => s.Id == P + "beat.hunger").Nodes.Single(n => n.Id == "eat").Choices;
        check(hunger.Single(c => c.Next == "thumb").Requires.Contains(Committed) && hunger.Single(c => c.Next == "thumb_early").Forbids.Contains(Committed),
            "Her remark about being taught to wait comes before she taught it.");

        // Reviewed polish: exact native receipts decide biography, never romance eligibility.
        check(story.SelectedAnswers["horzalah.yozz_killed"] == "da63ff8f158beaf42825a5d821128a96"
              && story.SelectedAnswers["horzalah.yozz_knives"] == "0d313dee79e05da4994b7bfe481cb973"
              && story.SelectedAnswers["horzalah.yozz_tortured"] == "ae3a61bbbc053484eb3117840d9455c0"
              && story.SelectedAnswers["horzalah.yozz_released"] == "5e6e4baafff6a5d4da795553928f07a5"
              && story.SeenCues["horzalah.yozz_confession_heard"].SequenceEqual(new[] { "1a302027ad5c3e94ebbd2313cb3f1e6e" }),
            "Horzalah polish: Yozz's outcomes or optional confession are bound to the wrong native producer.");
        var yozzBeat = S(P + "beat.yozz");
        foreach (var (receipt, expected) in new[] {
            ("horzalah.yozz_killed", "leash_dead"), ("horzalah.yozz_knives", "leash"),
            ("horzalah.yozz_tortured", "leash"), ("horzalah.yozz_released", "leash"), ("", "leash_unvisited") })
        foreach (bool freed in new[] { false, true })
        {
            var facts = new List<string> { "trickster", "trickster.ever", Wants, Tested };
            if (receipt.Length > 0) facts.Add(receipt);
            if (freed) facts.Add(P + "cost.gift_freed");
            var world = Later(story, World(story, 5, facts.ToArray()), 24);
            foreach (string source in new[] { "start", "own" })
            {
                var shown = yozzBeat.Nodes.Single(n => n.Id == source).Choices
                    .Where(c => c.Next != null && c.Next.StartsWith("leash", StringComparison.Ordinal)
                                && Rules.ChoiceAvailable(c, world)).ToArray();
                check(shown.Length == 1 && shown[0].Next == expected, "Horzalah polish: Yozz history conflated at " + source);
            }
            check(Through(yozzBeat, world, expected, 0).Any(r => r.Has(P + "beat.yozz_heard"))
                  && Through(yozzBeat, world, expected, 1).Any(r => r.Has(P + "beat.yozz_heard")),
                "Horzalah polish: a biography variant has no selectable conclusion.");
        }
        var killedAndSpared = World(story, 5, "trickster", "trickster.ever", Wants, Tested,
            "horzalah.yozz_killed", "horzalah.yozz_knives");
        check(yozzBeat.Nodes.Single(n => n.Id == "start").Choices.Where(c => c.Next != null
                  && c.Next.StartsWith("leash", StringComparison.Ordinal) && Rules.ChoiceAvailable(c, killedAndSpared))
                  .Single().Next == "leash_dead", "Horzalah polish: Yozz's death loses to a historical survivor receipt.");
        var confession = S(P + "beat.used");
        var firstAdmission = S(P + "beat.used_first");
        foreach (bool heard in new[] { false, true })
        {
            var world = World(story, 5, "trickster", "trickster.ever", Wants, Tested, P + "beat.yozz_heard");
            if (heard) world.Flags.Add("horzalah.yozz_confession_heard");
            check(Avail(confession, world) == heard && Avail(firstAdmission, world) != heard,
                "Horzalah polish: optional confession memory and first admission overlap or both disappear.");
            var consumed = Take(heard ? confession : firstAdmission, world, "little", 0, P + "beat.used_heard");
            check(!Avail(confession, consumed) && !Avail(firstAdmission, consumed),
                "Horzalah polish: both versions of the admission can be consumed.");
        }
        var cheekReaction = S(P + "react.wenduag_cheek");
        check(cheekReaction.Relationship == "wenduag"
              && Avail(cheekReaction, World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", P + "threatened", Closed)),
            "Horzalah polish: closing Horzalah suppresses Wenduag's historical judgment.");
        foreach (string loss in new[] { "wenduag.killed", "wenduag.kicked_out" })
            check(!Avail(cheekReaction, World(story, 5, "trickster", "trickster.ever", "wenduag.in_party", P + "threatened", Closed, loss)),
                "Horzalah polish: unavailable Wenduag materializes for the cheek reaction.");
        foreach (string kill in Kills)
        {
            var world = World(story, 6, "trickster", "trickster.ever", Started, Returned, Tested, Committed, Closed, "sacrifice", kill);
            check(pages.All(s => !Avail(s, world)), "Horzalah polish: dead Horzalah receives a living or mourning page.");
        }

        // Courtship: every beat and letter is reachable on some road.
        check(beats.Length == 29 && letters.Length == 2 && letters.All(s => Rules.IsRemote(s) && s.Kind == "letter" && s.Chapters.SequenceEqual(new[] { 5 }))
              && beats.All(s => s.ContactUnit == Unit && s.InteractionHub == "horzalah.presence" && s.Optional),
            "Horzalah's courtship is not twenty-eight beats and their confession variant on her presence and two Chapter 5 letters.");
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
        // What the Commander claims to have seen or heard rests on the cue that shows it: the seals (HorzalahFirst/Cue_0001),
        // her father's boast of spawning thousands (Cue_0121, not Cue_0122), her own account of the unanswered rescue (Cue_0051).
        var fatherBeat = beats.Single(s => s.Id == P + "beat.father");
        var seals = fatherBeat.Nodes.Single(n => n.Id == "start").Choices;
        var spawn = beats.Single(s => s.Id == P + "beat.thousands").Nodes.Single(n => n.Id == "start").Choices.Single(c => c.Next == "hundreds");
        check(seals.Where(c => c.Next == "count" || c.Next == "count_plain").All(c => c.Requires.Contains("horzalah.seals_seen"))
              && seals.Single(c => c.Next == "never").Forbids.Contains("horzalah.seals_seen")
              && spawn.Requires.SequenceEqual(new[] { "baphomet.spawn_told" })
              && mercy.Nodes.Single(n => n.Id == "guess").Choices.Where(c => c.Next == "called").Any(c => c.Requires.Contains("horzalah.rescue_refused_told")),
            "A recollection is offered without the cue that shows it.");
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
            "horzalah.gift_delivered", "hepzamirah.trickster.returned", "horzalah.met_q2", "horzalah.yozz_confession_heard", P + "scar_noted", P + "cost.late", P + "beat.board_warned");
        Play(road, 5, 20, Ally, LeftFree, Declined, P + "threatened");
        Play(World(story, 5, "trickster", "trickster.ever", Primed, Ear, Returned, Wants, Tested, P + "beat.yozz_heard"), 5, 2, Ally, LeftFree, Declined);
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
