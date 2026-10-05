using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Terendelev, Trickster (Writer/handoffs/11-ROSTER-PLAN-2.md §2, R3 build sheet): "Restitution in the Wound's blood".
// One block per rules test (Trk_Terendelev_*): the shape of each hook, the bones on Galfrey's list and on Irabeth's, the
// late page, the refusals (claimed, let rest, the search failed), the first night and its debt, the commit, the release,
// the guardian's hard no, the north turret, the keepsakes, the reactors and the pages.
internal static class TerendelevTricksterTests
{
    private const string P = "terendelev.trickster.";
    private const string GalfreyList = "c132e5e4fabc68d49aad76af3f447eb6";
    private const string GalfreyReturn = "4323895e05091eb40a206bcfb1394b6f";
    private const string IrabethList = "d0905746a5a015949ac39891ab4e5339";
    private const string IrabethReturn = "2a2a1beb1f22986499798b8e094d46f6";
    private const string Human = "9e8401e7703907e4d94189d5992dd13e";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Tiefling = "23eabf5b6364d4a4e86202dc5d27600b";
    private const string Tailor = "253cdb8f434e5a6469b75e18428316e3";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string Wilcer = "a380d926e92f70e429681eb9654478f9";
    private const string Smith = "15f754455d1d87c42a4e14df456d5415";
    private const string Scale = "816f244523b5455a85ae06db452d4330";
    private const string Claw = "66afc74ef27c7244eac8f8d376cd7947";
    private const string Returned = P + "returned";
    private const string Committed = "terendelev.committed";
    private const string Closed = "terendelev.closed";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = chapter == 5 || chapter == 3 ? Drezen : "" };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Human);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
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
        var square = S(P + "memory.square");
        var where = S(P + "voice.where");
        var weeps = S(P + "wound.weeps");
        var bones = S(P + "bones.restitution");
        var bonesIrabeth = S(P + "bones.restitution_irabeth");
        var late = S(P + "late.the_wound_calls");
        var firstNight = S(P + "after.first_night");
        var commit = S(P + "commit");
        var release = S(P + "commit.release");
        var night = S(P + "night.watch");
        var keepsakes = S(P + "watch.keepsakes");
        var road = S(P + "watch.road");
        var own = story.Scenes.Where(s => s.Relationship == "terendelev" && !s.Reaction && !s.Id.StartsWith(P + "react.", StringComparison.Ordinal) && !s.Id.StartsWith("terendelev.continuation", StringComparison.Ordinal)).ToArray();
        var hub = own.Where(s => s.InteractionHub != null).ToArray();
        var pages = own.Where(s => s.Id.StartsWith(P + "epilogue.", StringComparison.Ordinal)).ToArray(); // eng7-f6d: native dialogue text records have their own suite.
        // eng8-q8f: count the royal-letter reactor once, delivered as a physical handover.
        var reactions = story.Scenes.Where(s => s.Relationship == "terendelev"
            && (s.Reaction || s.Id == P + "react.galfrey.letter")).ToArray();
        // end eng8-q8f

        // Plays one scene and returns the outcomes holding every flag in `with` and none in `without`.
        List<Snapshot> Play(Scene scene, Snapshot w, string[] with, params string[] without)
        {
            check(Rules.Available(story, scene, w), "Not available: " + scene.Id);
            var hits = Program.Walk(scene, w).Where(r => with.All(r.Has) && !without.Any(r.Has)).ToList();
            check(hits.Count > 0, "No outcome of " + scene.Id + " with [" + string.Join(",", with) + "]");
            return hits;
        }
        Snapshot One(Scene scene, Snapshot w, string[] with, params string[] without) => Play(scene, w, with, without)[0];

        // Shape and hooks.
        var rel = story.Relationships["terendelev"];
        check(rel.StartedFlag == "terendelev.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { "terendelev.aeon_spared" }) && rel.UnavailableOverrides.Count == 0
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "bones", "late" })
              && rel.TricksterAccess["bones"].Device == bones.Id && rel.TricksterAccess["late"].Device == late.Id,
            "Terendelev's relationship does not match the build sheet.");
        check(bones.AnswerLists.SequenceEqual(new[] { GalfreyList }) && bones.NativeReturnCue == GalfreyReturn
              && bonesIrabeth.AnswerLists.SequenceEqual(new[] { IrabethList }) && bonesIrabeth.NativeReturnCue == IrabethReturn
              && bones.Forbids.Contains(bonesIrabeth.Id) && bonesIrabeth.Forbids.Contains(bones.Id)
              && new[] { bones, bonesIrabeth }.All(s => s.TricksterDevice && s.TricksterState == "bones" && s.Requires.Contains("trickster")
                  && s.Requires.Contains("iz.terendelev_battle") && s.Forbids.Contains("terendelev.aeon_spared") && s.ContactUnit == null
                  && s.Chapters.SequenceEqual(new[] { 5 })),
            "The bones are not inline on the Queen's and the knight's post-battle lists.");
        check(late.TricksterDevice && late.TricksterState == "late" && Rules.IsRemote(late) && late.DelayHours == 24
              && late.Requires.Contains("iz.monster_dead") && late.Requires.Contains("iz.monster_dead.latched"),
            "The late page is not the late device.");
        check(new[] { bones, bonesIrabeth, late }.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Where(c => c.Set.Contains(Returned))
                  .All(c => c.Set.Contains(P + "cost.wound_open") && c.Set.Contains(P + "grounded")),
            "A return does not open the wound and ground her.");
        check(new[] { bones, bonesIrabeth, late }.All(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Mythic == "PlayerIsTrickster"
                  && c.Text.StartsWith("[Open the wound", StringComparison.Ordinal))),
            "Opening the wound is not the Trickster's act.");
        check(story.Scenes.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).All(c => c.RemoveItem != Scale),
            "Something consumes her scale; it is never spent here.");
        check(!story.Scenes.Where(s => s.Relationship == "terendelev").SelectMany(s => s.Nodes).SelectMany(n => n.Choices)
                  .Any(c => c.Revive != null), "Something in her route is a raise.");
        var perception = bones.Nodes.Single(n => n.Id == "host").Choices.Where(c => c.Check != null).ToList();
        check(perception.Count == 3 && perception.All(c => c.Check!.Skill == "SkillPerception")
              && perception.Select(c => c.Check!.DC).OrderBy(d => d).SequenceEqual(new[] { 20, 24, 30 })
              && perception.Single(c => c.Check!.DC == 20).Requires.Contains(P + "eyes")
              && perception.Single(c => c.Check!.DC == 24).Requires.Contains("terendelev.voice_heard"),
            "The search is not Perception 30, 24 with the vision, 20 with the claw story or the sight.");
        check(story.Derived[P + "eyes"].Any(g => g.SequenceEqual(new[] { "terendelev.claw_story" }))
              && story.Derived[P + "eyes"].Any(g => g.SequenceEqual(new[] { "trickster.perception_tier1" })),
            "The DC 20 search does not follow the claw story or the Trickster's sight.");
        check(hub.All(s => s.ContactUnit == Human && s.Areas.SequenceEqual(new[] { Drezen }) && s.Chapters.SequenceEqual(new[] { 5 })
                          && (s.InteractionHub == "terendelev.presence" || s.InteractionHub == "terendelev.presence.awning")
                          && s.Forbids.Contains(Closed) && s.Requires.Contains(Returned)),
            "A Chapter 5 beat is not on her presence in Drezen.");
        foreach (var s in hub.Where(s => !s.Id.EndsWith("_awning", StringComparison.Ordinal)))
        {
            var twin = S(s.Id + "_awning");
            check(s.Forbids.Contains(twin.Id) && twin.Forbids.Contains(s.Id) && twin.Requires.Contains("terendelev.presence.failed")
                  && twin.InteractionHub == "terendelev.presence.awning", "A beat has no awning twin: " + s.Id);
        }
        var stall = story.Presences["terendelev.presence"];
        var awning = story.Presences["terendelev.presence.awning"];
        foreach (var pr in new[] { stall, awning })
            check(pr.Unit == Human && pr.Area == Drezen && pr.Mode == "spawn-copy" && pr.Dialog == "hub" && pr.MinChapter == 5 && pr.MaxChapter == 5
                  && pr.Requires.Contains(Returned) && pr.Forbids.Contains(Closed)
                  && pr.At?.NearUnit != Fye && pr.At?.NearUnit != Wilcer && pr.At?.NearUnit != Smith && pr.At!.Distance >= 2f,
                "A presence of hers is misplaced or at a crowded anchor.");
        check(stall.At!.NearUnit == Tiefling && stall.At.Side == "front" && awning.At!.NearUnit == Tailor && awning.At.Side == "right"
              && stall.Forbids.Contains("terendelev.presence.failed") && awning.Requires.Contains("terendelev.presence.failed"),
            "Her presence is not in front of the tiefling trader with the tailor's awning as fallback.");
        // Coexistence: no scene needs, or is shut by, another woman's death, departure or refusal.
        foreach (var s in own)
            foreach (var key in s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".closed", StringComparison.Ordinal) && key != Closed)
                      && !((key.EndsWith("_dead", StringComparison.Ordinal) || key.EndsWith(".dead", StringComparison.Ordinal) || key.EndsWith("_gone", StringComparison.Ordinal))
                           && key != "storyteller.dead" && !key.StartsWith("iz.", StringComparison.Ordinal)),
                    "Terendelev's route gates on someone else: " + s.Id + " " + key);
        var produced = new HashSet<string>(story.Scenes.Where(s => s.Relationship == "terendelev").SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set));
        foreach (var s in own)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)).Where(k => k.StartsWith(P, StringComparison.Ordinal)))
                check(produced.Contains(key) || story.Derived.ContainsKey(key) || own.Any(o => o.Id == key), "A gate has no producer: " + s.Id + " requires " + key);
        check(own.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Where(c => c.Set.Contains(Committed)).All(c => c.Set.Contains(P + "dressing"))
              && own.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed)))
                    .All(s => s.Id.StartsWith(P + "commit", StringComparison.Ordinal)),
            "Something other than her watch commits, or the commit leaves the wound undressed.");

        // Pacing: at least one beat in Chapters 3 and 4 before she returns.
        check(Rules.Available(story, square, World(story, 3, "trickster")) && Rules.Available(story, weeps, World(story, 4, "trickster"))
              && Rules.Available(story, where, World(story, 3, "trickster", "terendelev.voice_heard"))
              && !Rules.Available(story, where, World(story, 3, "trickster")),
            "Trk_Terendelev_Pacing: the Chapter 3 and 4 beats are shut.");
        check(!Rules.Available(story, square, World(story, 4, "trickster")), "The Drezen memory plays in the Abyss (Q6 r2).");
        var tested = One(weeps, World(story, 4, "trickster", "terendelev.scale_held"), new[] { P + "blood_tested", P + "scale_warmed" });
        check(tested.Has(P + "blood_tested"), "Trk_Terendelev_Pacing: the blood is never tested in the Abyss.");

        // Trk_Terendelev_Bones: the Queen's list; the found search, the gamble, the wound.
        var battle = World(story, 5, "trickster", "trickster.ever", "iz.terendelev_battle");
        check(Rules.Available(story, bones, battle) && Rules.Available(story, bonesIrabeth, battle),
            "Trk_Terendelev_Bones: the bones are shut after the battle.");
        check(!Rules.Available(story, bones, World(story, 5, "trickster", "trickster.ever", "iz.terendelev_battle", "terendelev.aeon_spared")),
            "Trk_Terendelev_Bones: the Aeon world reaches the bones.");
        check(!Rules.Available(story, bones, World(story, 5, "trickster.ever", "iz.terendelev_battle")),
            "Trk_Terendelev_Bones: the bones open without the live Trickster.");
        var back = One(bones, battle, new[] { Returned, P + "cost.wound_open", P + "grounded", "terendelev.started" }, P + "saw_the_queen_fall");
        check(!back.Has(Committed) && !back.Has(P + "cost.late"), "Trk_Terendelev_Bones: the return commits, or costs the late price.");
        One(bones, battle, new[] { Returned, P + "cost.bled_white" });
        var prepared = World(story, 5, "trickster", "trickster.ever", "iz.terendelev_battle", P + "blood_tested");
        check(!Program.Walk(bones, prepared).Any(r => r.Has(P + "cost.bled_white")) && Program.Walk(bones, prepared).Any(r => r.Has(Returned)),
            "Trk_Terendelev_Bones: the Abyss test does not spare the Commander the unmeasured bleeding.");
        check(Rules.PresenceWanted(stall, back) && !Rules.PresenceWanted(awning, back), "Trk_Terendelev_Bones: her presence does not stand in Drezen.");
        check(!Rules.Available(story, late, Later(story, World(story, 5, "trickster", "trickster.ever", "iz.monster_dead.live", Returned), 48)),
            "Trk_Terendelev_Bones: the late page follows a return.");
        check(Rules.Available(story, road, Later(story, World(story, 5, "trickster.ever", Returned, "iz.done"), 8)), "Trk_Terendelev_Bones: the road out of Iz never comes.");
        var failed = One(bones, battle, new[] { P + "search_failed" }, Returned);
        var claimed = One(bones, battle, new[] { P + "refused_claim" }, Returned);
        var flinched = One(bones, battle, new[] { P + "flinched" }, Returned, P + "search_failed");
        var rested = One(bones, battle, new[] { P + "rested", Closed }, Returned);
        foreach (var w in new[] { failed, claimed, flinched })
            check(!Rules.Available(story, bones, w) && !Rules.Available(story, bonesIrabeth, w), "Trk_Terendelev_Bones: the bones reopen after " + w.Flags.First(f => f.StartsWith(P)));

        // Trk_Terendelev_ParentReturn: the parent romance has already brought her back (its returned finale, or the Lich
        // binding): no Trickster return anywhere. Met or courted on the parent route only: the Trickster return stands.
        foreach (var parent in new[] { "terendelev.continuation.returned_finale_seen", "terendelev.parent_lich_bind" })
        {
            var already = World(story, 5, "trickster", "trickster.ever", "iz.terendelev_battle", parent);
            check(!Rules.Available(story, bones, already) && !Rules.Available(story, bonesIrabeth, already)
                  && !Rules.Available(story, late, World(story, 5, "trickster", "trickster.ever", "iz.monster_dead.live", "iz.left_early", parent))
                  && !Rules.Available(story, commit, World(story, 5, "trickster", "trickster.ever", Returned, P + "first_night_seen", parent))
                  && !Rules.PresenceWanted(stall, World(story, 5, "trickster", "trickster.ever", Returned, parent)),
                "Trk_Terendelev_ParentReturn: a Trickster return opens after the parent romance has returned her (" + parent + ").");
        }
        foreach (var met in new[] { "terendelev.parent_romance", "terendelev.parent_oath" })
        {
            var courted = World(story, 5, "trickster", "trickster.ever", "iz.terendelev_battle", met);
            check(Rules.Available(story, bones, courted) && Program.Walk(bones, courted).Any(r => r.Has(Returned)),
                "Trk_Terendelev_ParentReturn: meeting her on the parent route (" + met + ") shuts the Trickster return.");
        }

        // Trk_Terendelev_IrabethHost: the same on the knight's list when the Queen has fallen.
        var queenDead = World(story, 5, "trickster", "trickster.ever", "iz.terendelev_battle", "galfrey.dead");
        var backIrabeth = One(bonesIrabeth, queenDead, new[] { Returned, P + "cost.wound_open", P + "grounded", P + "saw_the_queen_fall" });
        check(backIrabeth.Has("terendelev.started") && !backIrabeth.Has(Committed), "Trk_Terendelev_IrabethHost: the flags differ from the Queen's list.");

        // Trk_Terendelev_LateAndDecline: the Queen fought it alone; the late page, the debt, the release.
        var alone = World(story, 5, "trickster", "trickster.ever", "iz.monster_dead.live", "iz.left_early");   // the kill observed in Iz
        check(!Rules.Available(story, bones, alone), "Trk_Terendelev_LateAndDecline: the bones open without the battle.");
        check(Rules.Available(story, late, alone) && !Rules.Available(story, late, World(story, 5, "trickster", "trickster.ever"))
              && !Rules.Available(story, late, World(story, 5, "trickster.ever", "iz.monster_dead.live")),
            "Trk_Terendelev_LateAndDecline: the late page is shut, or comes without the kill or the live path.");
        var lateBack = One(late, alone, new[] { Returned, P + "cost.late", P + "cost.wound_open", P + "grounded" });
        var lateRest = One(late, alone, new[] { P + "rested", Closed }, Returned);
        Snapshot Killed(Snapshot w)
        {
            var after = Program.Copy(w);
            after.Flags.Add("iz.monster_dead.live");
            Rules.Complete(story, after);
            foreach (var flag in after.Flags.ToList()) after.Times[flag] = after.Hour - 200;
            return after;
        }
        foreach (var w in new[] { failed, claimed, flinched })
            check(Rules.Available(story, late, Killed(w)), "Trk_Terendelev_LateAndDecline: no late yes after " + string.Join(",", w.Flags.Where(f => f.StartsWith(P))));
        check(!Rules.Available(story, late, Killed(rested)), "Trk_Terendelev_LateAndDecline: the late page reopens a rest the Commander granted.");
        var night1 = Later(story, lateBack, 30);
        check(Rules.Available(story, firstNight, night1), "Trk_Terendelev_LateAndDecline: her first night never comes.");
        var owed = One(firstNight, night1, new[] { P + "first_night_seen", P + "owed" });
        var askedOwed = Later(story, owed, 60);
        var declined = One(commit, askedOwed, new[] { P + "declined" }, Committed);
        check(!Program.Walk(commit, askedOwed).Any(r => r.Has(Committed)), "Trk_Terendelev_LateAndDecline: a held debt still commits.");
        check(!Rules.Available(story, release, Later(story, declined, 10)) && Rules.Available(story, release, Later(story, declined, 60)),
            "Trk_Terendelev_LateAndDecline: the release is not 48 hours after the debt is held.");
        var released = One(release, Later(story, declined, 60), new[] { Committed, P + "dressing" });
        check(Rules.Available(story, night, Later(story, released, 10)), "Trk_Terendelev_LateAndDecline: the release does not lead to the turret.");

        // Trk_Terendelev_Commit: nothing owed; she asks to guard the wound; the turret; the morning.
        var night2 = Later(story, back, 30);
        var square1 = One(firstNight, night2, new[] { P + "first_night_seen" }, P + "owed");
        check(!Rules.Available(story, commit, Later(story, square1, 20)) && Rules.Available(story, commit, Later(story, square1, 50)),
            "Trk_Terendelev_Commit: her ask is not 48 hours after her first night.");
        var sworn = One(commit, Later(story, square1, 50), new[] { Committed, P + "dressing" }, Closed);
        var turret = One(night, Later(story, sworn, 10), new[] { P + "night.seen" });
        check(turret.Has(Committed) && !turret.Has(Closed), "Trk_Terendelev_Commit: the turret closes her.");
        var beats = new[] { "want", "wound", "hoard", "throat", "cloak", "cut", "grey", "morning" };
        check(beats.All(b => night.Nodes.Any(n => n.Id == b))
              && night.Nodes.Single(n => n.Id == "cut").Choices.All(c => c.Next == "grey")
              && night.Nodes.Single(n => n.Id == "grey").Choices.All(c => c.Next == "morning"),
            "Trk_Terendelev_Commit: the night is not staged up to the cut and carried into the morning.");
        var seelah = reactions.Single(s => s.Id == P + "react.seelah.watch");
        check(seelah.Requires.Contains(P + "night.seen") && seelah.AnswerLists.SequenceEqual(new[] { "417fa384f3250634bb71859fbc913453" }),
            "Trk_Terendelev_Commit: Seelah's word does not follow the turret.");
        var irabeth = reactions.Single(s => s.Id == P + "react.irabeth.dressing");
        check(irabeth.Requires.Contains(P + "dressing") && irabeth.Forbids.Contains("irabeth_dead")
              && irabeth.ForbidOverrides.TryGetValue("irabeth_dead", out var ret) && ret == "irabeth.trickster.returned",
            "Trk_Terendelev_Commit: Irabeth's word does not read the dressing, or is not guarded by her return.");

        // Trk_Terendelev_Guardian: her hard no is going home to Kenabres; the page follows.
        var home = One(commit, Later(story, square1, 50), new[] { Closed, P + "guardian" }, Committed);
        check(!hub.Any(s => Rules.Available(story, s, Later(story, home, 100))), "Trk_Terendelev_Guardian: a beat plays after she has gone home.");
        var epiHome = World(story, 6, home.Flags.ToArray());
        check(pages.Count(s => Rules.Available(story, s, epiHome)) >= 1 && Rules.Available(story, S(P + "epilogue.guardian"), epiHome)
              && !Rules.Available(story, S(P + "epilogue.watch"), epiHome), "Trk_Terendelev_Guardian: the guardian page does not play.");

        // Trk_Terendelev_Keepsakes: her claw handed back (removed), her scale refused (kept).
        var withBoth = Later(story, square1, 20);
        withBoth.Flags.Add("terendelev.scale_held"); withBoth.Flags.Add("terendelev.claw_held");
        foreach (var flag in withBoth.Flags.ToList()) if (!withBoth.Times.ContainsKey(flag)) withBoth.Times[flag] = withBoth.Hour - 200;
        check(Rules.Available(story, keepsakes, withBoth) && !Rules.Available(story, keepsakes, Later(story, square1, 20)),
            "Trk_Terendelev_Keepsakes: the keepsakes open without a keepsake, or not with one.");
        var give = keepsakes.Nodes.SelectMany(n => n.Choices).Single(c => c.RemoveItem != null);
        check(give.RemoveItem == Claw && give.Requires.Contains("terendelev.claw_held") && give.Set.Contains(P + "watch.claw_returned")
              && story.RemovableItems.Contains(Claw),
            "Trk_Terendelev_Keepsakes: the claw is not handed back as hers.");

        // Reactions and pages.
        check(reactions.Length == 8 && reactions.All(s => s.Nodes.Count == 1)
              && new[] { "Seelah", "Irabeth", "Anevia", "Storyteller", "Galfrey" }.All(o => reactions.Any(s => s.Owner == o))
              && reactions.Where(s => s.Owner == "Daeran" || s.Owner == "Regill").All(s => s.Forbids.Contains("chapter_later")),
            "Terendelev's reactors are not Seelah (twice), Irabeth, Anevia, the Storyteller, Galfrey, Daeran and Regill.");
        check(pages.Length == 6 && pages.All(s => s.MinChapter == 6 && s.MaxChapter == 6 && s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0)),
            "Her epilogue pages are not six read-only Chapter 6 pages.");
        var epiWatch = World(story, 6, turret.Flags.ToArray());
        check(Rules.Available(story, S(P + "epilogue.watch"), epiWatch) && !Rules.Available(story, S(P + "epilogue.late"), epiWatch)
              && !Rules.Available(story, S(P + "epilogue.debt"), epiWatch), "Her committed page is not the only page of a committed watch.");
        var epiLate = World(story, 6, square1.Flags.ToArray());
        check(Rules.Available(story, S(P + "epilogue.late"), epiLate), "The R2-6 late page does not carry an unanswered first night.");
        check(Rules.Available(story, S(P + "epilogue.rest"), World(story, 6, rested.Flags.ToArray())), "The rest page does not follow the rest granted.");

        // Quality pass Q6.
        HashSet<string> PagesOf(Scene scene, Snapshot w) { var seen = new HashSet<string>(); Program.Walk(scene, w, (page, _) => seen.Add(page)); return seen; }
        // CAN: she remembers the Commander at the second death only when the Commander fought there.
        var withQueen = World(story, 5, "trickster.ever", Returned, "terendelev.started");
        var leftEarly = World(story, 5, "trickster.ever", Returned, "terendelev.started", "iz.left_early");
        check(PagesOf(firstNight, withQueen).Contains("iz") && !PagesOf(firstNight, withQueen).Contains("iz_queen")
              && PagesOf(firstNight, leftEarly).Contains("iz_queen") && !PagesOf(firstNight, leftEarly).Contains("iz"),
            "She remembers the Commander at a battle the Commander left.");
        // COX: a Queen brought back on her own route is alive in Terendelev's chapel talk, and still writes.
        var galScene = S(P + "watch.galfrey");
        var queenBack = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "galfrey.dead", "galfrey.trickster.returned");
        var queenGone = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "galfrey.dead");
        check(PagesOf(galScene, queenBack).Contains("queen_back") && !PagesOf(galScene, queenBack).Contains("dead_late") && !PagesOf(galScene, queenBack).Contains("carry")
              && PagesOf(galScene, queenGone).Contains("dead_unknown") && !PagesOf(galScene, queenGone).Contains("queen_back")
              && !PagesOf(galScene, queenGone).Contains("dead_late"),
            "A returned Queen is mourned as permanently dead.");
        // Q6 r2 (CAN/COX): the Queen's death by its recorded cause.
        var qEarly = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "galfrey.dead", "iz.left_early");
        var qPriestess = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "galfrey.dead", "iz.manuscripts.live");
        var qBackPriestess = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "galfrey.dead", "iz.manuscripts.live", "galfrey.trickster.returned");
        check(PagesOf(galScene, qEarly).Contains("dead_late") && PagesOf(galScene, qPriestess).Contains("dead_priestess") && !PagesOf(galScene, qPriestess).Contains("dead_late")
              && PagesOf(galScene, qBackPriestess).Contains("queen_back_priestess") && !PagesOf(galScene, qBackPriestess).Contains("queen_back"),
            "Terendelev claims a killing the record gives to the priestess.");
        // Q6 r3 (CAN/COX): the Commander's own kill survives the Queen's return; the Lord of Locusts' death needs its record.
        var qBackByYou = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "galfrey.killed_by_commander", "galfrey.trickster.returned");
        var qByYou = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "galfrey.killed_by_commander");
        check(PagesOf(galScene, qBackByYou).Contains("queen_back_by_you") && !PagesOf(galScene, qBackByYou).Contains("queen_back")
              && !PagesOf(galScene, qBackByYou).Contains("queen_back_priestess") && PagesOf(galScene, qByYou).Contains("dead_by_you")
              && !PagesOf(galScene, qByYou).Contains("dead") && !PagesOf(galScene, qByYou).Contains("alive"),
            "Terendelev claims the Queen's death when the Commander killed her.");
        var deskari = S(P + "watch.deskari");
        var dBase = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen");
        var dKilled = World(story, 5, "trickster.ever", Returned, "terendelev.started", P + "first_night_seen", "iz.deskari_killed.live");
        check(story.Etudes["iz.deskari_killed.live"] == "047d71e3e928d454bbd168497ee7c17f" && dKilled.Has("iz.deskari_killed")
              && !Rules.Available(story, deskari, Later(story, dBase, 30)) && Rules.Available(story, deskari, Later(story, dKilled, 30)),
            "The barracks confirm Deskari's death without DeskariKilledInIz.");
        // Q6 r3 (INT): no living-Commander page after an unsurvived sacrifice; her own page instead.
        var lost = World(story, 6, "trickster.ever", Returned, Committed, "sacrifice");
        check(!Rules.Available(story, S(P + "epilogue.watch"), lost) && Rules.Available(story, S(P + "epilogue.sacrifice"), lost)
              && !Rules.Available(story, S(P + "epilogue.sacrifice"), World(story, 6, "trickster.ever", Returned, Committed, "sacrifice", "ending.trickster")),
            "An unsurvived sacrifice still gets the watch, or a returned Commander is mourned.");
        var galLetter = S(P + "react.galfrey.letter");
        check(galLetter.ForbidOverrides.TryGetValue("galfrey.dead", out var gback) && gback == "galfrey.trickster.returned"
              && Rules.Available(story, galLetter, Later(story, World(story, 5, "trickster.ever", Returned, "galfrey.dead", "galfrey.trickster.returned"), 60)),
            "The Queen's letter ignores her return.");
        // CAN: Seelah's orphan years were in Solku; nothing puts her childhood in Kenabres.
        foreach (var s in story.Scenes.Where(x => x.Relationship == "terendelev"))
            foreach (var node in s.Nodes)
                check(!node.Text.Contains("street kid in Kenabres", StringComparison.Ordinal) && !node.Text.Contains("night before", StringComparison.Ordinal),
                    "Invented history or the wrong prologue chronology: " + s.Id + "/" + node.Id);
        // eng8-q8f: extras open at placed contacts; manual UI is no delivery witness.
        foreach (var id in new[] { "letter.watch_report", "letter.second_report", "watch.at_the_gate", "watch.road", "watch.third_bell" })
            check(!S(P + id).ManualOnly && !Rules.IsMailbagLetter(S(P + id))
                  && S(P + id).ContactUnit == Human && S(P + id).InteractionHub == "terendelev.presence",
                "A Chapter 5 extra lacks gameplay contact: " + id);
        // end eng8-q8f

        Console.WriteLine("PASS: Terendelev Trickster (Trk_Terendelev_*): the square and the Abyss, the bones on the Queen's list and the knight's, "
            + "the search and the gamble, the late page, the claim, the rest and the flinch, the first night and its debt, the release, "
            + "the watch and the turret, the road home to Kenabres, the keepsakes, " + reactions.Length + " reactions and " + pages.Length + " pages.");
    }
}
