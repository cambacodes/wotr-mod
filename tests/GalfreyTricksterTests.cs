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
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = chapter == 5 ? Drezen : "" };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Disguised);
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
        var hub = own.Where(s => s.InteractionHub != null).ToArray();
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
              && story.Etudes["galfrey.final"] == "e9205b9f9e8ecd04c92852d72d09ca86" && story.Etudes["iz.left_early"] == "a583e4ab47544f5e928fc5b6b7c41e48",
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
        check(own.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed))).All(s => s.Id.StartsWith(P + "commit", StringComparison.Ordinal)),
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

        // Trk_Galfrey_Kitrane: planted, read at the bed, framed for her; the return at +48 h; the oath refused.
        var bed = World(story, 5, "trickster", "trickster.ever", "galfrey.dying_seen", "galfrey.early.kitrane.mooted");
        check(Rules.Available(story, offer, bed) && !Rules.Available(story, offer, World(story, 5, "trickster.ever", "galfrey.dying_seen")),
            "Trk_Galfrey_Kitrane: the offer is shut at the bed, or opens without the live Trickster.");
        var watch = offer.Nodes.Single(n => n.Id == "watch").Choices.Where(c => c.Check != null).ToList();
        check(watch.Count == 2 && watch.All(c => c.Check!.Skill == "SkillPerception") && watch.Single(c => c.Check!.DC == 18).Requires.Contains(P + "kitrane_planted")
              && watch.Single(c => c.Check!.DC == 22).Forbids.Contains(P + "kitrane_planted"),
            "Trk_Galfrey_Kitrane: the watch is not Perception 22, 18 when planted.");
        var taken = One(offer, bed, new[] { Taken, P + "sorcery_read", "galfrey.started" }, P + "cost.rent_scar");
        var takenBlind = One(offer, bed, new[] { Taken, P + "blind", P + "cost.rent_scar" });
        var died = Died(taken);
        check(Rules.Available(story, road, Later(story, died, 12)) && Rules.Available(story, eulogy, Later(story, died, 40)),
            "Trk_Galfrey_Kitrane: the road or the eulogy does not follow the taken offer.");
        var roaded = One(road, Later(story, died, 12), new[] { P + "cost.coffin" });
        var eulogised = One(eulogy, Later(story, roaded, 40), new[] { P + "cost.eulogy", "trickster.secret.galfrey_eulogy" });
        var crowned = Later(story, eulogised, 10, null, "coronation.after", "coronation.seen");
        check(!Rules.Available(story, ret, Later(story, crowned, 20)) && Rules.Available(story, ret, Later(story, crowned, 50))
              && !Rules.Available(story, retScarred, Later(story, crowned, 200)),
            "Trk_Galfrey_Kitrane: the return is not 48 hours after the Coronation, or the scarred twin plays in the read world.");
        var back = One(ret, Later(story, crowned, 50), new[] { Returned });
        check(Rules.PresenceWanted(stall, back) && !Rules.PresenceWanted(fb, back), "Trk_Galfrey_Kitrane: her presence does not stand in the market.");
        var morning = One(first, Later(story, back, 10), new[] { P + "first_morning" });
        check(!Rules.Available(story, oath, Later(story, morning, 20)) && Rules.Available(story, oath, Later(story, morning, 50)),
            "Trk_Galfrey_Kitrane: the oath is not 48 hours after her first morning.");
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
        check(!Rules.Available(story, ret, Later(story, diedBlind, 50)) && !Rules.Available(story, retScarred, Later(story, diedBlind, 50))
              && Rules.Available(story, retScarred, Later(story, diedBlind, 100)),
            "Trk_Galfrey_RefusedThenYes: the blind return is not 96 hours after the Coronation.");
        var letDie = One(offer, bed, new[] { P + "let_die", Closed }, Taken);
        check(!Rules.Available(story, ret, Later(story, Died(letDie, "coronation.after", "coronation.seen"), 200))
              && Rules.Available(story, S(P + "epilogue.queen"), World(story, 6, letDie.Flags.Concat(new[] { "trickster.ever", Dead }).ToArray())),
            "Trk_Galfrey_RefusedThenYes: letting her die as the Queen does not close her route and give her page.");

        // Trk_Galfrey_Offscreen: the Commander never came; planted, she writes; unplanted, canon stands.
        var offscreen = World(story, 5, "trickster", "trickster.ever", "iz.left_early", Dead, P + "crows_mooted");
        var wrote = One(alone, offscreen, new[] { Taken, P + "cost.rent_scar", P + "cost.alone", P + "cost.coffin" });
        check(Rules.Available(story, retScarred, Later(story, Later(story, wrote, 10, null, "coronation.after", "coronation.seen"), 100))
              && !Rules.Available(story, road, Later(story, wrote, 20)),
            "Trk_Galfrey_Offscreen: the letter does not lead to the scarred return, or the road plays without the bed.");
        var unplanted = World(story, 5, "trickster", "trickster.ever", "iz.left_early", Dead, "coronation.after", "coronation.seen");
        check(!own.Where(s => s.TricksterDevice).Any(s => Rules.Available(story, s, Later(story, unplanted, 200))),
            "Trk_Galfrey_Offscreen: without the seed a Galfrey device opens.");
        check(!own.Where(s => s.TricksterDevice).Any(s => Rules.Available(story, s,
                  World(story, 5, "trickster", "trickster.ever", Dead, "galfrey.killed_by_commander", P + "crows_mooted", "iz.left_early"))),
            "Trk_Galfrey_Killed: a device serves a kill the Commander chose.");

        // Trk_Galfrey_Sworn: the oath accepted; the release 48 hours later; she chooses.
        var sworn = One(oath, Later(story, morning, 50), new[] { P + "sworn" }, Committed);
        check(!Rules.Available(story, release, Later(story, sworn, 20)) && Rules.Available(story, release, Later(story, sworn, 50)),
            "Trk_Galfrey_Sworn: the release is not 48 hours after the oath.");
        One(release, Later(story, sworn, 50), new[] { Committed });
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
        One(ford, Later(story, crowsOrder, 30), new[] { P + "ride.refused_order", P + "ride.hanged" });
        One(ford, Later(story, crowsOrder, 30), new[] { P + "ride.trial" }, P + "ride.refused_order");

        // Trk_Galfrey_NativeFirst: she lived, the native romance ran to the end: no device, one page, a partner.
        var native = World(story, 6, "trickster.ever", "iz.fought_with_galfrey", "galfrey.romance_active", "galfrey.final");
        check(!own.Where(s => s.TricksterDevice || s.MinChapter == 5).Any(s => Rules.Available(story, s, World(story, 5, "trickster", "trickster.ever",
                  "iz.fought_with_galfrey", "galfrey.romance_active", "galfrey.final", "coronation.after", "coronation.seen"))),
            "Trk_Galfrey_NativeFirst: a Chapter 5 Galfrey scene opens where she lives.");
        check(native.Has(P + "partner") && native.Has("galfrey.harem.eligible")
              && pages.Count(s => Rules.Available(story, s, native)) == 1 && Rules.Available(story, S(P + "epilogue.native"), native),
            "Trk_Galfrey_NativeFirst: the native world does not count her once, with exactly one page.");
        check(!World(story, 6, "trickster.ever", "galfrey.romance_active", Dead).Has(P + "partner"),
            "Trk_Galfrey_NativeFirst: a dead Queen counts as a partner through the native romance.");
        foreach (var w in new[] { night, sworn, letDie })
        {
            var epi = World(story, 6, w.Flags.Concat(new[] { "trickster.ever", Dead }).ToArray());
            check(pages.Count(s => Rules.Available(story, s, epi)) == 1, "Trk_Galfrey_Pages: a world reaches more or fewer than one Galfrey page.");
        }

        // Reactions and pages.
        check(reactions.Length == 8 && reactions.All(s => s.Nodes.Count == 1)
              && new[] { "Irabeth", "Seelah", "Hulrun", "Daeran", "Thaberdine" }.All(o => reactions.Any(s => s.Owner == o))
              && reactions.Where(s => s.Owner == "Irabeth").All(s => s.Forbids.Contains("irabeth_dead")
                  && s.ForbidOverrides.TryGetValue("irabeth_dead", out var r) && r == "irabeth.trickster.returned"),
            "Galfrey's reactors are not Irabeth (three), Seelah, Hulrun (two), Daeran and the King, or Irabeth's are unguarded.");
        check(pages.Length == 5 && pages.All(s => s.MinChapter == 6 && s.MaxChapter == 6 && s.Requires.Contains("trickster.ever")
                  && s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0)),
            "Her epilogue pages are not five read-only Trickster Chapter 6 pages.");

        Console.WriteLine("PASS: Galfrey Trickster (Trk_Galfrey_*): the Kitrane question in Chapters 2-4 on every path, the offer at the bed "
            + "read or blind, for Mendev refused and for her taken, the road, the eulogy, the letter from the rubble, the return, the oath refused "
            + "or sworn and released, the tent and the drill, Sir Anselm's name and her last choice, the native world, " + reactions.Length
            + " reactions and " + pages.Length + " pages.");
    }
}
