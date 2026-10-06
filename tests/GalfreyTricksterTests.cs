using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Galfrey, Trickster (Writer/handoffs/11-ROSTER-PLAN-2.md §2, R4 build sheet): "The Queen dies; Kitrane walks out".
// One block per rules test (Trk_Galfrey_*): the hooks, the Kitrane question planted in Chapters 2-4 (path-neutral), the offer
// at the deathbed read or blind, framed for Mendev (refused) or for her (taken), the offscreen letter, the return, the oath
// refused or accepted and released, the tent, her last choice, the native-romance world, the reactors and the pages.
internal static class GalfreyTricksterTests
{
    private const string P = "galfrey.trickster.";
    private const string EdgeList = "13487ef288faa30459888cdcce979b51";
    private const string EdgeBack = "a316738673dc6524eaeeb3feda0e9fe7";
    private const string Farewell = "a5e30e29364069446926ff78a73a026d";
    private const string IncognitoList = "f1225677b6e455a4db45f2ce77533816";
    private const string IncognitoBack = "d5133deffe0362548bd2563ee5291eef";
    private const string ArrivesList = "44704bddb6223b84989dd26bcf20b601";
    private const string ArrivesBack = "21467e29a21d22b438eac99a34d8c09b";
    private const string Disguised = "a8b7f6fd39ff2974f8b5fbf944a7f735";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Curio = "bad9f602b81a80047ac470b01ebe65a9";
    private const string Tiefling = "23eabf5b6364d4a4e86202dc5d27600b";
    private const string Hulrun = "35733470f7fc4ae2bd1c874cd58118a4";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string Wilcer = "a380d926e92f70e429681eb9654478f9";
    private const string Smith = "15f754455d1d87c42a4e14df456d5415";
    private const string Returned = P + "returned";
    private const string Taken = P + "kitrane_taken";
    private const string Committed = "galfrey.committed";
    private const string Closed = "galfrey.closed";
    private const string Dead = "galfrey.dead";

    private static readonly string[] NativeEtudes = { "galfrey.romance_active", "galfrey.dead", "galfrey.killed_by_commander", "galfrey.final" };

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        // eng7-l12: Chapter 3 standing orders are delivered in the Drezen camp.
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = chapter == 3 || chapter == 5 ? Drezen : "",
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000, ["Materials"] = 10000 } };
        state.Flags.UnionWith(flags);
        // These positive predicate fixtures represent an already accepted route.
        // Coarse-key negatives are independent in PayoffDepartureRulesTests.
        foreach (var rel in story.Relationships)
            if (flags.Contains(rel.Value.CommittedFlag) && story.Derived.ContainsKey(rel.Key + ".payoff.ordinary"))
                HouseholdTests.Earn(story, state, rel.Key + ".payoff.ordinary");
        // Native ending/Last Call checkpoint flags expand to their actual sources.
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Disguised);
        state.AvailableContacts.Add("8a23e71893cf8ab428e7ebd64b10ad27"); // eng8-q8d: the Crows sergeant
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null, params string[] add)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        foreach (var flag in add) { later.Flags.Add(flag); later.Times[flag] = later.Hour; }
        if (chapter != null)
        {
            later.Chapter = chapter.Value;
            later.Area = chapter.Value == 5 ? Drezen : "";
        }
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var early = S("galfrey.early.kitrane");
        var crows = S(P + "ch3.crows");
        var crowd = S(P + "ch4.crowd");
        var letter = S(P + "ch4.letter");
        var offer = S(P + "iz.offer");
        var road = S(P + "iz.road");
        var eulogy = S(P + "iz.eulogy");
        var alone = S(P + "iz.alone");
        var ret = S(P + "return.kitrane");
        var retScarred = S(P + "return.kitrane_scarred");
        var first = S(P + "after.first_morning");
        var coffin = S(P + "kitrane.coffin");
        var oath = S(P + "commit.oath");
        var release = S(P + "commit.release");
        var tent = S(P + "visit.tent");
        var crown = S(P + "kitrane.crown");
        var ford = S(P + "kitrane.ford");
        var own = story.Scenes.Where(s => s.Relationship == "galfrey" && !s.Reaction).ToArray();
        var hub = own.Where(s => s.InteractionHub == "galfrey.presence" || s.InteractionHub == "galfrey.presence.stall").ToArray();
        var pages = own.Where(s => s.Owner == "GalfreyEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "galfrey" && s.Reaction).ToArray();

        List<Snapshot> Play(Scene scene, Snapshot w, string[] with, params string[] without)
        {
            check(Rules.Available(story, scene, w), "Not available: " + scene.Id);
            var hits = Program.Walk(scene, w).Where(r => with.All(r.Has) && !without.Any(r.Has)).ToList();
            check(hits.Count > 0, "No outcome of " + scene.Id + " with [" + string.Join(",", with) + "]");
            return hits;
        }
        Snapshot One(Scene scene, Snapshot w, string[] with, params string[] without) => Play(scene, w, with, without)[0];
        // The canon death after the offer: GalfreyDead plays, the Coronation comes.
        Snapshot Died(Snapshot w, params string[] add) => Later(story, w, 12, null, new[] { Dead }.Concat(add).ToArray());

        // Trk_Galfrey_Bindings: the relationship and every hook of the build sheet.
        var rel = story.Relationships["galfrey"];
        check(rel.StartedFlag == "galfrey.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.OrderBy(f => f).SequenceEqual(new[] { Dead, "galfrey.killed_by_commander" })
              && rel.UnavailableOverrides.Count == 1 && rel.UnavailableOverrides[Dead] == Returned
              && rel.TricksterAccess.Keys.SequenceEqual(new[] { "dead" }) && rel.TricksterAccess["dead"].Device == ret.Id
              && rel.TricksterAccess["dead"].Returned == Returned,
            "Trk_Galfrey_Bindings: the relationship does not match the build sheet.");
        check(story.SeenCues["galfrey.dying_seen"].SequenceEqual(new[] { "963c942bae94eed4b8928d65cf56bad5" })
              && story.SeenCues["galfrey.incognito_met"].SequenceEqual(new[] { "19d217c3503c0304db4bec29c9882bc9" })
              && story.SeenCues["galfrey.seelah_at_bed"].SequenceEqual(new[] { "95037d694c52c964a8bf7b121b309caa" })
              && story.SeenCues["galfrey.farewell_found"].SequenceEqual(new[] { "c0cf7ea6c8f13434fa36671b3b81a2ab" })
              && story.Etudes["galfrey.dead"] == "a4f20ae9f6a6c3d4ba204721589470a2" && story.Etudes["galfrey.romance_active"] == "c9358d866e0b3844b8d72536ca60e4b4"
              && story.Etudes["galfrey.final"] == "e9205b9f9e8ecd04c92852d72d09ca86" && story.Etudes["iz.left_early.live"] == "a583e4ab47544f5e928fc5b6b7c41e48",
            "Trk_Galfrey_Bindings: a native key is bound to the wrong blueprint.");
        check(early.AnswerLists.SequenceEqual(new[] { IncognitoList }) && early.NativeReturnCue == IncognitoBack
              && crows.AnswerLists.SequenceEqual(new[] { ArrivesList }) && crows.NativeReturnCue == ArrivesBack
              && offer.AnswerLists.SequenceEqual(new[] { EdgeList }) && offer.NativeReturnCue == EdgeBack,
            "Trk_Galfrey_Bindings: an inline scene is not on its native list with its clean return cue.");
        check(offer.Nodes.SelectMany(n => n.Choices).Where(c => c.Next == null && !c.Abort && c.Check == null).All(c => c.NativeNext == Farewell),
            "Trk_Galfrey_Bindings: an ending of the offer skips her native farewell (Cue_0053 -> GalfreyDead).");
        // Never touch a native romance etude: nothing sets a native key.
        check(!story.Scenes.Where(s => s.Relationship == "galfrey").SelectMany(s => s.Nodes).SelectMany(n => n.Choices)
                  .SelectMany(c => c.Set).Any(f => NativeEtudes.Contains(f) || story.Etudes.ContainsKey(f)),
            "Trk_Galfrey_NativeFirst: a Galfrey choice sets a native key.");
        check(!story.Scenes.Where(s => s.Relationship == "galfrey").SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Any(c => c.Revive != null),
            "Trk_Galfrey: something in her route is a raise.");

        // Path fit (v1): the Chapter 2-4 build-up is on every path; everything from the offer on is Trickster-only.
        foreach (var s in new[] { early, crows, crowd, letter })
            check(!s.Requires.Any(k => k.StartsWith("trickster", StringComparison.Ordinal)), "Path fit: a build-up beat is Trickster-gated: " + s.Id);
        foreach (var s in own.Where(s => s.MinChapter >= 5))
            check(s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever"), "Path fit: a Chapter 5+ scene is not Trickster-only: " + s.Id);

        // Presences: the curio stall, the tiefling fallback; never Hulrun (PretendUnit), Fye, Wilcer or the smith.
        var stall = story.Presences["galfrey.presence"];
        var fb = story.Presences["galfrey.presence.stall"];
        foreach (var pr in new[] { stall, fb })
            check(pr.Unit == Disguised && pr.Area == Drezen && pr.Mode == "spawn-copy" && pr.Dialog == "hub" && pr.MinChapter == 5 && pr.MaxChapter == 5
                  && pr.Requires.Contains(Returned) && pr.Forbids.Contains(Closed) && pr.At!.Distance >= 2f
                  && new[] { Fye, Wilcer, Smith, Hulrun }.All(u => pr.At.NearUnit != u),
                "Trk_Galfrey_Presence: a presence of hers is misplaced or at a crowded anchor.");
        check(stall.At!.NearUnit == Curio && stall.At.Side == "left" && fb.At!.NearUnit == Tiefling && fb.At.Side == "right"
              && stall.Forbids.Contains("galfrey.presence.failed") && fb.Requires.Contains("galfrey.presence.failed"),
            "Trk_Galfrey_Presence: her presence is not left of the curio trader with the tiefling's stall as fallback.");
        foreach (var s in hub.Where(s => !s.Id.EndsWith("_stall", StringComparison.Ordinal)))
        {
            var twin = S(s.Id + "_stall");
            check(s.Forbids.Contains(twin.Id) && twin.Forbids.Contains(s.Id) && twin.Requires.Contains("galfrey.presence.failed")
                  && s.ContactUnit == Disguised && s.Areas.SequenceEqual(new[] { Drezen }), "Trk_Galfrey_Presence: a beat has no stall twin: " + s.Id);
        }
        // Coexistence: no Galfrey scene gates on another woman's death, departure, return or refusal.
        foreach (var s in own)
            foreach (var key in s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".closed", StringComparison.Ordinal) && key != Closed) && !key.StartsWith("irabeth", StringComparison.Ordinal)
                      && !key.StartsWith("terendelev", StringComparison.Ordinal) && !key.StartsWith("seelah", StringComparison.Ordinal)
                      && !key.StartsWith("anevia", StringComparison.Ordinal),
                    "Trk_Galfrey_Coexistence: Galfrey's route gates on someone else: " + s.Id + " " + key);
        var produced = new HashSet<string>(story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set));
        foreach (var s in own)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)).Where(k => k.StartsWith(P, StringComparison.Ordinal)))
                check(produced.Contains(key) || story.Derived.ContainsKey(key) || own.Any(o => o.Id == key), "A gate has no producer: " + s.Id + " requires " + key);
        check(own.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed))).All(s => s.Id.StartsWith(P + "commit", StringComparison.Ordinal) || s.Id == P + "alive.oath"),
            "Something other than the oath or its release commits her.");

        // Trk_Galfrey_Pacing: a beat in Chapters 2, 3 and 4 on every path.
        var ch2 = World(story, 2, "galfrey.incognito_met");
        var mooted = One(early, ch2, new[] { "galfrey.early.kitrane.mooted" });
        One(early, ch2, new[] { "galfrey.early.kitrane.refused" });
        check(Rules.Available(story, crows, World(story, 3)) && Rules.Available(story, crowd, World(story, 4)),
            "Trk_Galfrey_Pacing: the Chapter 3 or 4 beat is shut on a path without the Trickster.");
        var pressed = One(crows, World(story, 3), new[] { P + "crows_refused", P + "crows_pressed" });
        check(Rules.Available(story, letter, Later(story, pressed, 30, 4)) && !Rules.Available(story, letter, World(story, 4)),
            "Trk_Galfrey_Pacing: her pre-Fane letter is not the answer to a pressed question.");
        One(letter, Later(story, pressed, 30, 4), new[] { P + "letter_mooted" });
        var general = One(crows, World(story, 3), new[] { P + "crows_pressed_general" });
        check(Program.Walk(letter, Later(story, general, 30, 4)).All(r => r.Has(P + "letter_refused") && !r.Has(P + "letter_mooted")),
            "Trk_Galfrey_Pacing: asked as her general, the letter still moots it.");
        check(World(story, 2, mooted.Flags.ToArray()).Has(P + "kitrane_planted"), "Trk_Galfrey_Pacing: a moot in Chapter 2 does not plant Kitrane.");

        // Trk_Galfrey_Kitrane: planted, read at the bed, framed for her; the return at +24 h; the oath refused.
        var bed = World(story, 5, "trickster", "trickster.ever", "galfrey.dying_seen", "galfrey.early.kitrane.mooted");
        check(Rules.Available(story, offer, bed) && !Rules.Available(story, offer, World(story, 5, "trickster.ever", "trickster.failed", "galfrey.dying_seen")),
            "Trk_Galfrey_Kitrane: the offer is shut at the bed, or opens without the live Trickster.");
        var watch = offer.Nodes.Single(n => n.Id == "watch").Choices.Where(c => c.Check != null).ToList();
        check(watch.Count == 2 && watch.All(c => c.Check!.Skill == "SkillPerception") && watch.Single(c => c.Check!.DC == 18).Requires.Contains(P + "kitrane_planted")
              && watch.Single(c => c.Check!.DC == 22).Forbids.Contains(P + "kitrane_planted"),
            "Trk_Galfrey_Kitrane: the watch is not Perception 22, 18 when planted.");
        var taken = One(offer, bed, new[] { Taken, P + "sorcery_read", "galfrey.started" }, P + "cost.rent_scar");
        var takenBlind = One(offer, bed, new[] { Taken, P + "blind", P + "cost.rent_scar" });
        var died = Died(taken);
        // The manuscripts branch (the priestess, Cue_0072): no way back to the dragon's Cue_0073 once she is knelt to.
        check(Program.Walk(offer, Later(story, bed, 0, null, "iz.manuscripts")).All(r => r.Has(Taken) || r.Has(P + "let_die")),
            "Trk_Galfrey_Kitrane: the manuscripts deathbed can fall back to the dragon's return cue.");
        check(Program.Walk(offer, Later(story, bed, 0, null, "galfrey.kc_after_fane")).Where(r => r.Has(Taken)).All(r => r.Has(P + "carried.crows") && !r.Has(P + "carried.irabeth")),
            "Trk_Galfrey_Kitrane: Irabeth carries the order while she was left in Drezen (the title kept after the Fane).");
        var awayRest = Later(story, died, 40); awayRest.Area = "";
        check(!Rules.Available(story, eulogy, awayRest), "Trk_Galfrey_Kitrane: the Drezen vigil plays at a rest outside Drezen.");
        check(Rules.Available(story, road, Later(story, died, 12)) && Rules.Available(story, eulogy, Later(story, died, 40)),
            "Trk_Galfrey_Kitrane: the road or the eulogy does not follow the taken offer.");
        var roaded = One(road, Later(story, died, 12), new[] { P + "cost.coffin" });
        var eulogised = One(eulogy, Later(story, roaded, 40), new[] { P + "cost.eulogy", "trickster.secret.galfrey_eulogy" });
        var crowned = Later(story, eulogised, 10, null, "coronation.after", "coronation.seen");
        check(!Rules.Available(story, ret, Later(story, crowned, 20)) && Rules.Available(story, ret, Later(story, crowned, 50))
              && !Rules.Available(story, retScarred, Later(story, crowned, 200)),
            "Trk_Galfrey_Kitrane: the return is not 24 hours after the Coronation, or the scarred twin plays in the read world.");
        var back = One(ret, Later(story, crowned, 50), new[] { Returned });
        check(Rules.PresenceWanted(stall, back) && !Rules.PresenceWanted(fb, back), "Trk_Galfrey_Kitrane: her presence does not stand in the market.");
        var met = One(first, Later(story, back, 10), new[] { P + "first_morning" });
        check(!Rules.Available(story, oath, Later(story, met, 60)), "Trk_Galfrey_Kitrane: the oath comes without a shared act and a real exchange.");
        var morning = Later(story, met, 0, null, P + "kitrane.reel", P + "kitrane.elixir_told");
        check(!Rules.Available(story, oath, Later(story, morning, 10)) && Rules.Available(story, oath, Later(story, morning, 12)),
            "Trk_Galfrey_Kitrane: the oath has not reserved the earlier 12-hour courtship wait.");
        var yes = One(oath, Later(story, morning, 50), new[] { Committed }, P + "sworn");
        check(oath.Nodes.Single(n => n.Id == "crowd").Choices.Any(c => c.Text.StartsWith("[Refuse her oath", StringComparison.Ordinal) && c.Next == "refuse"),
            "Trk_Galfrey_Kitrane: the commit is not the Commander refusing her oath.");
        var night = One(tent, Later(story, yes, 10), new[] { P + "tent_seen", P + "morning_drill" });
        var beats = new[] { "armour", "buckles", "mail", "want", "bed", "cut", "after", "morning", "drill" };
        check(beats.All(b => tent.Nodes.Any(n => n.Id == b)) && tent.Nodes.Single(n => n.Id == "cut").Choices.All(c => c.Next == "after"),
            "Trk_Galfrey_Kitrane: the tent is not staged up to the cut and carried into the morning drill.");
        check(Rules.Available(story, S(P + "epilogue.kitrane"), World(story, 6, night.Flags.ToArray())),
            "Trk_Galfrey_Kitrane: the Kitrane page does not play for a committed Kitrane.");

        // Trk_Galfrey_RefusedThenYes: blind; framed for Mendev she refuses and names her condition; framed for her she takes it.
        var refused = Program.Walk(offer, bed).Where(r => r.Has(P + "offer_refused") && r.Has(Taken) && r.Has(P + "blind")).ToList();
        check(refused.Count > 0 && refused.All(r => r.Has(P + "cost.rent_scar")), "Trk_Galfrey_RefusedThenYes: refused for Mendev, no later yes at the bed.");
        check(!Program.Walk(offer, bed).Any(r => r.Has(P + "offer_refused") && !r.Has(Taken) && !r.Has(P + "let_die")),
            "Trk_Galfrey_RefusedThenYes: her refusal ends the scene without a yes or the Commander's own choice.");
        var diedBlind = Later(story, Died(takenBlind), 60, null, "coronation.after", "coronation.seen");
        check(!Rules.Available(story, retScarred, Later(story, diedBlind, 200)),
            "Trk_Galfrey_RefusedThenYes: a blind offer is released without the proclamation (the eulogy).");
        var proclaimed = Later(story, One(eulogy, Later(story, diedBlind, 1), new[] { P + "cost.eulogy" }), 1);
        check(!Rules.Available(story, ret, Later(story, proclaimed, 50)) && !Rules.Available(story, retScarred, Later(story, proclaimed, 34))
              && Rules.Available(story, retScarred, Later(story, proclaimed, 100)),
            "Trk_Galfrey_RefusedThenYes: the blind return is not 36 hours after the Coronation and the eulogy.");
        var letDie = One(offer, bed, new[] { P + "let_die", Closed }, Taken);
        check(!Rules.Available(story, ret, Later(story, Died(letDie, "coronation.after", "coronation.seen"), 200))
              && Rules.Available(story, S(P + "epilogue.queen"), World(story, 6, letDie.Flags.Concat(new[] { "trickster", "trickster.ever", Dead }).ToArray())),
            "Trk_Galfrey_RefusedThenYes: letting her die as the Queen does not close her route and give her page.");

        // Trk_Galfrey_Offscreen: the Commander never came; planted and briefed, she writes; otherwise the cortege at Drezen.
        var offscreen = World(story, 5, "trickster", "trickster.ever", "iz.left_early", Dead, P + "crows_mooted", P + "crows_briefed");
        check(!Rules.Available(story, alone, World(story, 5, "trickster", "trickster.ever", "iz.left_early", Dead, P + "crows_mooted")),
            "Trk_Galfrey_Offscreen: her letter comes without the Commander's standing orders to the Crows.");
        check(Rules.Available(story, S(P + "ch3.standing_orders"), World(story, 3, "trickster", P + "crows_mooted"))
              && !Rules.Available(story, S(P + "ch3.standing_orders"), World(story, 3, P + "crows_mooted")),
            "Trk_Galfrey_Offscreen: the standing orders are not a Trickster preparation in Chapter 3.");
        var wrote = One(alone, offscreen, new[] { Taken, P + "cost.rent_scar", P + "cost.alone", P + "cost.coffin" });
        check(!Rules.Available(story, retScarred, Later(story, Later(story, wrote, 10, null, "coronation.after", "coronation.seen"), 100))
              && Rules.Available(story, retScarred, Later(story, One(eulogy, Later(story, wrote, 40, null, "coronation.after", "coronation.seen"), new[] { P + "cost.eulogy" }), 100))
              && !Rules.Available(story, road, Later(story, wrote, 20)),
            "Trk_Galfrey_Offscreen: the letter does not lead to the scarred return, or the road plays without the bed.");
        // Trk_Galfrey_Cortege (the late recovery): no seed, no orders; the lid not yet sealed at Drezen. Dearer, and hers to refuse.
        var cortege = S(P + "iz.cortege");
        var unplanted = World(story, 5, "trickster", "trickster.ever", "iz.left_early", Dead);
        check(!Rules.Available(story, cortege, Later(story, unplanted, -150)) && Rules.Available(story, cortege, Later(story, unplanted, 0))
              && !Rules.Available(story, cortege, World(story, 5, "trickster.ever", "trickster.failed", "iz.left_early", Dead))
              && !cortege.Requires.Contains(P + "kitrane_planted") && !cortege.Requires.Contains(P + "crows_briefed")
              && cortege.Areas.SequenceEqual(new[] { Drezen }),
            "Trk_Galfrey_Cortege: the unprepared offscreen death has no late recovery in Drezen, or one an ex-Trickster can start.");
        var found = One(cortege, unplanted, new[] { Taken, P + "cost.rent_scar", P + "cost.alone", P + "cost.found_late", P + "cost.coffin" });
        check(Program.Walk(cortege, unplanted).Any(r => r.Has(P + "let_die") && r.Has(Closed) && !r.Has(Taken)),
            "Trk_Galfrey_Cortege: she cannot refuse the name on the bier.");
        check(!Rules.Available(story, cortege, found) && !Rules.Available(story, cortege, Later(story, wrote, 100)),
            "Trk_Galfrey_Cortege: the cortege plays after she has already taken the name.");
        var foundProclaimed = One(eulogy, Later(story, found, 40), new[] { P + "cost.eulogy" });
        var foundBack = Later(story, Later(story, foundProclaimed, 1, null, "coronation.after", "coronation.seen"), 100);
        check(Rules.Available(story, retScarred, foundBack), "Trk_Galfrey_Cortege: the late recovery does not lead to her return.");
        var recalled = new List<string>();
        Program.Walk(retScarred, foundBack, (id, _) => recalled.Add(id));
        check((recalled.Contains("alone_found") || recalled.Contains("alone_found_talked")) && !recalled.Contains("alone") && !recalled.Contains("alone_silent"),
            "Trk_Galfrey_Cortege: the return invents a letter for the woman found on the bier.");
        // Q12: the return remembers how the Commander got past the sergeant (paid, or talked), and the name came from
        // the Commander's own war-camp meeting or, failing that, from the sergeant at the door.
        foreach (var paid in new[] { true, false })
        {
            var f = paid ? One(cortege, unplanted, new[] { Taken, P + "cost.found_late", P + "cortege.paid" })
                         : One(cortege, unplanted, new[] { Taken, P + "cost.found_late" }, P + "cortege.paid");
            var fBack = Later(story, Later(story, One(eulogy, Later(story, f, 40), new[] { P + "cost.eulogy" }), 1, null, "coronation.after", "coronation.seen"), 100);
            var fSeen = new List<string>();
            Program.Walk(retScarred, fBack, (id, _) => fSeen.Add(id));
            check(fSeen.Contains(paid ? "alone_found" : "alone_found_talked") && !fSeen.Contains(paid ? "alone_found_talked" : "alone_found"),
                "Trk_Galfrey_Cortege: the return remembers a bribe that was never paid, or forgets one that was.");
        }
        var bierNodes = new List<string>();
        Program.Walk(cortege, unplanted, (id, _) => bierNodes.Add(id));
        var metNodes = new List<string>();
        Program.Walk(cortege, Later(story, unplanted, 0, null, "galfrey.incognito_met"), (id, _) => metNodes.Add(id));
        check(bierNodes.Contains("flare_told") && !bierNodes.Contains("flare") && metNodes.Contains("flare") && !metNodes.Contains("flare_told"),
            "Trk_Galfrey_Cortege: the Commander remembers a war-camp meeting that never happened.");
        var bierRefused = Program.Walk(cortege, unplanted).First(r => r.Has(P + "let_die"));
        var bierEpi = World(story, 6, bierRefused.Flags.Concat(new[] { "trickster", "trickster.ever" }).ToArray());
        check(Rules.Available(story, S(P + "epilogue.queen_bier"), bierEpi) && !Rules.Available(story, S(P + "epilogue.queen"), bierEpi),
            "Trk_Galfrey_Cortege: her refusal on the bier gets the deathbed page.");
        check(!own.Where(s => s.TricksterDevice).Any(s => Rules.Available(story, s,
                  World(story, 5, "trickster", "trickster.ever", Dead, "galfrey.killed_by_commander", P + "crows_mooted", "iz.left_early"))),
            "Trk_Galfrey_Killed: a device serves a kill the Commander chose.");

        // Trk_Galfrey_Postponed: her own two days on the direct oath, then her answer.
        var postponed = One(oath, Later(story, morning, 50), new[] { P + "oath_postponed" }, Committed, P + "sworn");
        var answer = S(P + "commit.answer");
        check(!Rules.Available(story, oath, Later(story, postponed, 60)) && !Rules.Available(story, answer, Later(story, postponed, 20))
              && Rules.Available(story, answer, Later(story, postponed, 50)),
            "Trk_Galfrey_Postponed: her answer is not two days after her postponement.");
        One(answer, Later(story, postponed, 50), new[] { Committed });

        // Trk_Galfrey_Sworn: the oath accepted; the release 48 hours later; she chooses.
        var sworn = One(oath, Later(story, morning, 50), new[] { P + "sworn" }, Committed);
        check(!Rules.Available(story, release, Later(story, sworn, 20)) && Rules.Available(story, release, Later(story, sworn, 50)),
            "Trk_Galfrey_Sworn: the release is not 48 hours after the oath.");
        One(release, Later(story, sworn, 50), new[] { Committed });
        var swornHanged = Later(story, sworn, 1, null, P + "ride.hanged", P + "ride.refused_order");
        check(!Rules.Available(story, release, Later(story, swornHanged, 60))
              && Rules.Available(story, release, Later(story, swornHanged, 60, null, P + "ride.answered")),
            "Trk_Galfrey_Sworn: the release ignores an unanswered hanging, or stays shut after the terms are kept.");
        check(Program.Walk(release, Later(story, sworn, 50)).Any(r => !r.Has(Committed)),
            "Trk_Galfrey_Sworn: the release has no refusal of hers (an order dressed as a release).");
        check(Rules.Available(story, S(P + "epilogue.sworn"), World(story, 6, sworn.Flags.ToArray())),
            "Trk_Galfrey_Sworn: a sworn knight has no page.");

        // Trk_Galfrey_Cost: her last choice follows what the Commander said of Sir Anselm.
        var named = One(coffin, Later(story, morning, 20), new[] { P + "coffin.named" });
        check(Program.Walk(crown, Later(story, named, 60)).All(r => r.Has(P + "crown_reclaimed") && !r.Has(P + "kitrane_forever")),
            "Trk_Galfrey_Cost: named, she does not reclaim the crown.");
        var kept = One(coffin, Later(story, morning, 20), new[] { P + "coffin.kept" });
        check(Program.Walk(crown, Later(story, kept, 60)).All(r => r.Has(P + "kitrane_forever") && !r.Has(P + "crown_reclaimed")),
            "Trk_Galfrey_Cost: kept, she does not stay Kitrane.");
        // The ford: an order she refuses (Evil), or a trial.
        var crowsOrder = Later(story, morning, 30, null, P + "kitrane.squire_sworn");
        var hanged = One(ford, Later(story, crowsOrder, 30), new[] { P + "ride.refused_order", P + "ride.hanged" });
        check(!Rules.Available(story, oath, Later(story, hanged, 60)), "Trk_Galfrey_Ford: the oath is offered over six unanswered ropes.");
        check(Program.Walk(S(P + "kitrane.ford_after"), Later(story, hanged, 30)).Any(r => !r.Has(P + "ride.answered")),
            "Trk_Galfrey_Ford: refusing her terms is not a way out of the scene.");
        var answered = One(S(P + "kitrane.ford_after"), Later(story, hanged, 30), new[] { P + "ride.answered" });
        check(Rules.Available(story, oath, Later(story, answered, 60)), "Trk_Galfrey_Ford: her terms met, the oath stays shut.");
        var hangedAfter = Later(story, yes, 1, null, P + "ride.hanged", P + "ride.refused_order");
        check(!Rules.Available(story, tent, Later(story, hangedAfter, 20)), "Trk_Galfrey_Ford: the tent opens over an unanswered hanging after the commit.");
        One(ford, Later(story, crowsOrder, 30), new[] { P + "ride.trial" }, P + "ride.refused_order");

        // Trk_Galfrey_NativeFirst: she lived, the native romance ran to the end: no device, one page, a partner.
        var native = World(story, 6, "trickster", "trickster.ever", "iz.fought_with_galfrey", "galfrey.romance_active", "galfrey.romance_finished", "galfrey.final");
        check(!World(story, 6, "trickster", "trickster.ever", "iz.fought_with_galfrey", "galfrey.romance_active", "galfrey.final").Has(P + "partner"),
            "Trk_Galfrey_NativeFirst: an unfinished native courtship counts as a partner.");
        check(!own.Where(s => s.TricksterDevice).Any(s => Rules.Available(story, s, World(story, 5, "trickster", "trickster.ever",
                  "iz.fought_with_galfrey", "galfrey.romance_active", "galfrey.final", "coronation.after", "coronation.seen"))),
            "Trk_Galfrey_NativeFirst: a Kitrane device opens where she lives.");
        // Trk_Galfrey_Living: on the Trickster path her own Chapter 5 answer is "friendship is all I can offer you" (Cue_0041);
        // the living courtship answers it as Kitrane, earned by one plan told and kept, and commits by the refused oath.
        var living = World(story, 5, "trickster", "trickster.ever", "iz.fought_with_galfrey", "galfrey.final", "galfrey.native_refused",
                           "coronation.after", "coronation.seen");
        var livingKitrane = S(P + "alive.kitrane");
        check(Rules.Available(story, livingKitrane, living) && livingKitrane.AnswerLists.SequenceEqual(new[] { "fed166af2f1d509478d18ea63a40339f" })
              && livingKitrane.NativeReturnCue == "344bc63f6bbace64fab2a3e6c69561fe"
              && !Rules.Available(story, livingKitrane, World(story, 5, "trickster", "trickster.ever", "galfrey.final", "galfrey.romance_active")),
            "Trk_Galfrey_Living: the living courtship is shut after her native refusal, or opens while her native romance is active.");
        var evening = One(livingKitrane, living, new[] { P + "alive.evening" });
        var plan = S(P + "alive.plan");
        check(Program.Walk(plan, Later(story, evening, 50)).Any(r => !r.Has(P + "alive.plan_kept")), "Trk_Galfrey_Living: a half-told plan still earns her.");
        var planKept = One(plan, Later(story, evening, 50), new[] { P + "alive.plan_kept" });
        // Q12: one kept plan is a beginning; the next one is a decision she objects to, and her objection must be answered.
        var trial = S(P + "alive.trial");
        check(!Rules.Available(story, S(P + "alive.oath"), Later(story, planKept, 50)) && Rules.Available(story, trial, Later(story, planKept, 50)),
            "Trk_Galfrey_Living: one kept plan opens her bed without the next test.");
        check(Program.Walk(trial, Later(story, planKept, 50)).Any(r => !r.Has(P + "alive.trial_kept"))
              && Program.Walk(trial, Later(story, planKept, 50)).Where(r => r.Has(P + "alive.trial_priced")).All(r => !r.Has(P + "alive.trial_kept")),
            "Trk_Galfrey_Living: the test has no failure, or a cultist turned loose unwatched still earns her.");
        var trialKept = One(trial, Later(story, planKept, 50), new[] { P + "alive.trial_kept" });
        var livingYes = One(S(P + "alive.oath"), Later(story, trialKept, 50), new[] { Committed });
        check(Rules.Available(story, S(P + "react.irabeth.queen_night"), Later(story, livingYes, 20)),
            "Trk_Galfrey_Living: the living Queen's night has no companion reaction.");
        check(Program.Walk(S(P + "alive.oath"), Later(story, trialKept, 50)).Any(r => !r.Has(Committed))
              && Rules.Available(story, S(P + "epilogue.alive"), World(story, 6, livingYes.Flags.ToArray()))
              && World(story, 6, livingYes.Flags.ToArray()).Has(P + "partner"),
            "Trk_Galfrey_Living: the living commit has no no of hers, or no page, or no Last Call seat.");
        check(!Rules.Available(story, tent, Later(story, livingYes, 30)) && !Rules.Available(story, S(P + "kitrane.grey"), Later(story, livingYes, 30)),
            "Trk_Galfrey_Living: the living Queen is sent to the returned knight's tent.");
        check(Program.Walk(plan, Later(story, evening, 50)).Where(r => r.Has(P + "alive.plan_kept")).All(r => r.Has(P + "alive.plan_told")),
            "Trk_Galfrey_Living: a plan is kept that was never told.");
        // The manuscripts deathbed with Terendelev returned: no recollection of her claw.
        var manuIz = World(story, 5, back.Flags.Concat(new[] { "iz.manuscripts", "terendelev.trickster.returned", P + "first_morning" }).ToArray());
        manuIz.Hour += 100;
        var seen = new List<string>();
        Program.Walk(S(P + "kitrane.iz"), manuIz, (id, _) => seen.Add(id));
        check(seen.Contains("priestess") && !seen.Contains("dragon") && !seen.Contains("hate") && seen.Contains("hate_manu"),
            "Trk_Galfrey_Manuscripts: the priestess's branch recalls the dragon's claw.");
        // A returned Seelah is in Drezen: the pie is hers, and her reaction plays.
        var seelahBack = World(story, 5, back.Flags.Concat(new[] { "galfrey.seelah_at_bed", "seelah_dead", "seelah.trickster.returned", P + "first_morning" }).ToArray());
        seelahBack.Hour += 100;
        var pie = new List<string>();
        Program.Walk(S(P + "kitrane.seelah"), seelahBack, (id, _) => pie.Add(id));
        check(pie.Contains("seelah") && !pie.Contains("stranger") && !pie.Contains("stranger_absent")
              && Rules.Available(story, S(P + "react.seelah.majesty"), seelahBack),
            "Trk_Galfrey_Coexistence: a returned Seelah is written as absent.");
        check(native.Has(P + "partner") && native.Has("galfrey.harem.eligible")
              && pages.Count(s => Rules.Available(story, s, native)) == 1 && Rules.Available(story, S(P + "epilogue.native"), native),
            "Trk_Galfrey_NativeFirst: the native world does not count her once, with exactly one page.");
        check(!World(story, 6, "trickster", "trickster.ever", "galfrey.romance_active", Dead).Has(P + "partner"),
            "Trk_Galfrey_NativeFirst: a dead Queen counts as a partner through the native romance.");
        // The bottle world: the Commander died at Threshold and came back (trickster.commander_back): the shared life, not the loss.
        var bottle = World(story, 6, night.Flags.Concat(new[] { "trickster", "trickster.ever", Dead, "sacrifice", "trickster.commander_back" }).ToArray());
        check(Rules.Available(story, S(P + "epilogue.kitrane"), bottle) && !Rules.Available(story, S(P + "epilogue.widow"), bottle)
              && pages.Count(s => Rules.Available(story, s, bottle)) == 1,
            "Trk_Galfrey_Pages: the bottle-survival world does not get exactly the shared-life page.");
        // Carriers: Irabeth's firsthand accounts only where she carried the order; the Crows' version where they did.
        var byIrabeth = World(story, 5, back.Flags.Concat(new[] { P + "carried.irabeth" }).Where(f => f != P + "carried.crows").ToArray());
        var byCrows = World(story, 5, back.Flags.Concat(new[] { P + "carried.crows", P + "carried.crows_drezen" }).Where(f => f != P + "carried.irabeth").ToArray());
        byIrabeth.Hour += 100; byCrows.Hour += 100;
        check(Rules.Available(story, S(P + "react.irabeth.carried"), byIrabeth) && !Rules.Available(story, S(P + "react.irabeth.carried"), byCrows)
              && Rules.Available(story, S(P + "react.irabeth.learned"), byCrows) && !Rules.Available(story, S(P + "react.irabeth.learned"), byIrabeth),
            "Trk_Galfrey_Reactions: Irabeth's account does not follow who carried the order.");
        var drilled = World(story, 5, night.Flags.ToArray()); drilled.Hour += 100;
        var drilledSquire = World(story, 5, night.Flags.Concat(new[] { P + "kitrane.squire_sworn" }).ToArray()); drilledSquire.Hour += 100;
        check(Rules.Available(story, S(P + "react.irabeth.drill_alone"), drilled) && !Rules.Available(story, S(P + "react.irabeth.drill"), drilled)
              && Rules.Available(story, S(P + "react.irabeth.drill"), drilledSquire) && !Rules.Available(story, S(P + "react.irabeth.drill_alone"), drilledSquire),
            "Trk_Galfrey_Reactions: Irabeth's drill does not follow whether there was a squire.");
        // Hulrun absent: the vigil's line reaches no Inquisitor.
        foreach (var gone in new[] { "hulrun.dead", "hulrun.away_c5" })
        {
            var visited = new List<string>();
            Program.Walk(eulogy, Later(story, roaded, 40, null, gone), (id, _) => visited.Add(id));
            check(!visited.Contains("hulrun") && !visited.Contains("sign_hulrun") && visited.Contains("chaplain"),
                "Trk_Galfrey_Vigil: Hulrun is in the chapel although " + gone + ".");
        }
        var lost = World(story, 6, night.Flags.Concat(new[] { "trickster", "trickster.ever", Dead, "sacrifice" }).ToArray());
        check(Rules.Available(story, S(P + "epilogue.widow"), lost) && !Rules.Available(story, S(P + "epilogue.kitrane"), lost),
            "Trk_Galfrey_Pages: a Commander lost at Threshold still gets the shared-life page.");
        foreach (var w in new[] { night, sworn, letDie })
        {
            var epi = World(story, 6, w.Flags.Concat(new[] { "trickster", "trickster.ever", Dead }).ToArray());
            check(pages.Count(s => Rules.Available(story, s, epi)) == 1, "Trk_Galfrey_Pages: a world reaches more or fewer than one Galfrey page.");
        }

        // Reactions and pages.
        check(reactions.Length == 13 && reactions.All(s => s.Nodes.Count == 1)
              && new[] { "Irabeth", "Seelah", "Hulrun" }.All(o => reactions.Any(s => s.Owner == o && !s.Forbids.Contains("trickster.ever")))
              && reactions.Where(s => s.Owner == "Daeran" || s.Owner == "Thaberdine").All(s => s.Forbids.Contains("trickster.ever"))
              && reactions.Where(s => s.Owner == "Irabeth").All(s => s.Forbids.Contains("irabeth_dead")
                  && s.ForbidOverrides.TryGetValue("irabeth_dead", out var r) && r == "irabeth.trickster.returned"),
            "Galfrey's reactors are not Irabeth (seven), Seelah, Hulrun (two), Daeran and the King, or Irabeth's are unguarded.");
        // 9 since R6: alive_buried, the sibling of "alive" in the world where the Commander lives buried (iomedae_trickster).
        check(pages.Length == 9 && pages.All(s => s.MinChapter == 6 && s.MaxChapter == 6 && s.Requires.Contains("trickster.ever")
                  && s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0)),
            "Her epilogue pages are not nine read-only Trickster Chapter 6 pages.");

        Console.WriteLine("PASS: Galfrey Trickster (Trk_Galfrey_*): the Kitrane question in Chapters 2-4 on every path, the offer at the bed "
            + "read or blind, for Mendev refused and for her taken, the road, the eulogy, the letter from the rubble, the return, the oath refused "
            + "or sworn and released, the tent and the drill, Sir Anselm's name and her last choice, the native world, " + reactions.Length
            + " reactions and " + pages.Length + " pages.");
    }
}
