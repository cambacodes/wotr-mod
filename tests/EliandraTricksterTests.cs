using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Eliandra, Trickster (Writer/handoffs/11-ROSTER-PLAN-2.md §2, R4 build sheet): "A sacrifice in her place".
// One block per rules test (Trk_Eliandra_*): the hooks and bindings, the leave (the lights taken), the counteroffer (gold
// refused, her reward returned), the refusals and her own offering, the commit and the road letter, the star-heart, the
// King's list and the presence, the path-fit tags, the reactors and the pages.
internal static class EliandraTricksterTests
{
    private const string E = "eliandra.trickster.";
    private const string Unit = "e349079a648cb15448a27f9049344bf1";
    private const string Hub = "6073e28cab0691542b85a24436ed919c";
    private const string Ret = "cb48db9773f775b428f0a5f20757145e";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string KingC5 = "6dccfd39947ef4242a8afbe36b21a46c";
    private const string KingReturn = "7b050ba0745bf144e815632e39b34853";
    private const string FoolKing = "cc50a88bbd8dd3e4da066d33d14fdfc8";
    private const string Fye = "0f12118177d102f428a3b30b15b132eb";
    private const string Wilcer = "a380d926e92f70e429681eb9654478f9";
    private const string Smith = "15f754455d1d87c42a4e14df456d5415";
    private const string Committed = "eliandra.committed";
    private const string Closed = "eliandra.closed";
    private const string Started = "eliandra.started";
    private const string Met = "eliandra.met_ch5";
    private const string ShrineLeft = "eliandra.shrine_left";
    private const string Leave = E + "leave_granted";
    private const string NoLeave = E + "no_leave";
    private const string Lights = E + "cost.lights_given";
    private const string Reward = E + "cost.reward_returned";
    private static readonly string[] Unfit = { "demon", "devil", "lich", "swarm", "angel" };

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = chapter == 5 ? Drezen : "" };
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
        state.AvailableContacts.Add(Unit);
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

    private sealed class SeqEq : IEqualityComparer<string[]>
    {
        public bool Equals(string[]? a, string[]? b) => a != null && b != null && a.SequenceEqual(b);
        public int GetHashCode(string[] a) => a.Length;
    }

    private static (float X, float Z) Spot(Presence p)
    {
        var d = p.At!.Distance;
        return p.At.Side switch { "left" => (-d, 0f), "right" => (d, 0f), "front" => (0f, d), "behind" => (0f, -d), _ => (0f, 0f) };
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var firstWords = S(E + "ch5.first_words");
        var terms = S(E + "ch5.terms");
        var observe = S(E + "ch5.observe");
        var rite = S(E + "ch5.last_rite");
        var self = S(E + "ch5.self_offering");
        var mile = S(E + "ch5.first_mile");
        var letter = S(E + "ch5.road_letter");
        var heart = S(E + "visit.star_heart");
        var chiefs = S(E + "ch3.chiefs_ground");
        var redSky = S(E + "ch4.red_sky");
        var own = story.Scenes.Where(s => s.Relationship == "eliandra" && !s.Reaction).ToArray();
        var shrine = own.Where(s => s.AnswerLists.SequenceEqual(new[] { Hub })).ToArray();
        var presenceBeats = own.Where(s => s.InteractionHub != null).ToArray();
        var pages = own.Where(s => s.Owner == "EliandraEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "eliandra" && s.Reaction).ToArray();

        Snapshot One(Scene scene, Snapshot w, string[] with, params string[] without)
        {
            check(Rules.Available(story, scene, w), "Not available: " + scene.Id);
            var hit = Program.Walk(scene, w).FirstOrDefault(r => with.All(r.Has) && !without.Any(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " with [" + string.Join(",", with) + "] and none of [" + string.Join(",", without) + "]");
            return hit!;
        }

        // Trk_Eliandra_Bindings: the relationship, the hub and its clean return, the corrected sanctuary key, the path tags.
        var rel = story.Relationships["eliandra"];
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { "eliandra.dead", "eliandra.attacked" })
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "no_leave", "vow" })
              && rel.TricksterAccess["vow"].Device == rite.Id && rel.TricksterAccess["vow"].Detect.SequenceEqual(new[] { Met }) && rel.TricksterAccess["no_leave"].Device == self.Id,
            "Trk_Eliandra_Bindings: the relationship does not match the build sheet.");
        check(shrine.Length >= 12 && shrine.All(s => (s.NativeReturnCue == Ret) != s.ReturnToList && s.Chapters.SequenceEqual(new[] { 5 })
                  && (s.NativeReturnCue == null) == !s.Nodes.SelectMany(n => n.Choices).Any(c => c.Check != null)
                  && s.Requires.Contains(Met) && s.Forbids.Contains(Closed) && s.Forbids.Contains("eliandra.dead") && s.ContactUnit == null),
            "Trk_Eliandra_Bindings: a shrine beat is not inline on her Ch5 hub with its clean return.");
        check(story.SeenCues[ShrineLeft].Contains("7ca8fc49de894e94db63142f153a172a") && story.SeenCues[ShrineLeft].Contains("28e3b35d52e24fb4da16778f68b2b1c2"),
            "Trk_Eliandra_Bindings: the sanctuary key misses Katair's Cue_0029 or her own Cue_0030 (the one a Trickster hears).");
        check(!story.Scenes.Where(s => s.Relationship == "eliandra").SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Any(c => c.Revive != null)
              && !story.Scenes.Where(s => s.Relationship == "eliandra").SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set)
                  .Any(f => f.Contains("year") || f.Contains("century")),
            "Trk_Eliandra_Bindings: something raises, or a lapsing-years flag survives (the century premise is withdrawn).");
        check(!story.Scenes.Any(s => s.Requires.Contains("eliandra.rite_seen") || s.RequiresAnyGroups.Any(g => g.Contains("eliandra.rite_seen"))),
            "Trk_Eliandra_Bindings: a scene reads the Angel-only rite key.");

        // Path fit (v1): N-fit build-up has no Trickster gate and is shut on the unfit paths; T scenes need the Trickster.
        var nfit = shrine.Where(s => !s.Requires.Contains("trickster")).ToArray();
        check(nfit.Length >= 10 && nfit.All(s => !s.Requires.Contains("trickster.ever") && Unfit.All(s.Forbids.Contains)),
            "Path fit: an N-fit shrine beat carries a Trickster gate, or opens on a path that does not fit her.");
        check(own.Except(nfit).All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever")),
            "Path fit: a T scene opens without the Trickster.");
        check(Rules.Available(story, firstWords, World(story, 5, "azata", Met)) && !Rules.Available(story, firstWords, World(story, 5, "demon", Met))
              && !Rules.Available(story, terms, World(story, 5, "azata", Met, E + "dead_named")),
            "Path fit: the first words are shut on Azata or open on Demon, or the device opens off the Trickster path.");
        check(!own.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Where(c => c.Set.Contains(Committed))
                  .Any(c => !own.Where(s => s.Requires.Contains("trickster.ever") || s.Requires.Contains("trickster"))
                      .SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Contains(c)),
            "Path fit: a non-Trickster commit exists (v2 only).");

        // Pacing: the chiefs' ground in Ch3 (the tablet trip) and the red sky in Ch4.
        var tripped = World(story, 3, "trickster", "trickster.ever", "fool_king.tablet_brought");
        check(Rules.Available(story, chiefs, tripped) && !Rules.Available(story, chiefs, World(story, 3, "trickster")),
            "Trk_Eliandra_Pacing: the chiefs' ground page is shut after the tablet trip, or open without it.");
        var seen = One(chiefs, tripped, new[] { E + "lights_seen", E + "wine_left" });
        check(!Rules.Available(story, redSky, World(story, 4, "trickster", E + "lights_seen")) == false
              && Rules.Available(story, redSky, Later(story, World(story, 4, "trickster", E + "lights_seen"), 60)),
            "Trk_Eliandra_Pacing: the red sky never comes after the lights were seen.");

        // Trk_Eliandra_Leave: the first words, the terms read, the rite, the lights taken, the first mile, the yes.
        var arrived = World(story, 5, "trickster", "trickster.ever", Met, ShrineLeft, "fool_king.tablet_brought", E + "lights_seen");
        var named = One(firstWords, arrived, new[] { E + "dead_named", E + "lights_told" });
        check(!Rules.Available(story, rite, named), "Trk_Eliandra_Leave: the rite opens with neither the terms nor an observation.");
        var read = One(terms, named, new[] { E + "terms_read", Started });
        check(Rules.Available(story, rite, read), "Trk_Eliandra_Leave: the terms read do not open the rite.");
        // The sanctuary question (Cue_0029/0030) is not a gate: a Commander who never asks it still reaches the rite and its yes.
        var unasked = World(story, 5, "trickster", "trickster.ever", Met);
        var unaskedRead = One(terms, One(firstWords, unasked, new[] { E + "dead_named" }), new[] { E + "terms_read" });
        check(!rite.Requires.Contains(ShrineLeft) && Rules.Available(story, rite, unaskedRead)
              && Program.Walk(rite, unaskedRead).Any(r => r.Has(Leave)), "Trk_Eliandra_Leave: the rite waits on the sanctuary question.");
        var lightsOffer = rite.Nodes.Single(n => n.Id == "name").Choices.Where(c => c.Check != null).ToList();
        check(rite.Nodes.Single(n => n.Id == "name_again").Choices.Where(c => c.Check != null).Select(c => c.Check!.DC).OrderBy(d => d).SequenceEqual(new[] { 18, 24 }),
            "Trk_Eliandra_Leave: after the refusal the lights are not offered at 24, or 18 with the terms.");
        check(lightsOffer.Count == 2 && lightsOffer.All(c => c.Check!.Skill == "SkillLoreReligion" && c.Check.Success == "taken" && c.Check.Failure == "counter")
              && lightsOffer.Single(c => c.Check!.DC == 18).Requires.Contains(E + "terms_read")
              && lightsOffer.Single(c => c.Check!.DC == 24).Forbids.Contains(E + "terms_read")
              && terms.Nodes.Single(n => n.Id == "start").Choices[0].Check is { Skill: "SkillLoreReligion", DC: 20 },
            "Trk_Eliandra_Leave: the checks are not the terms at 20 and the lights at 24, or 18 with the terms.");
        var granted = One(rite, read, new[] { Leave, Lights }, Reward, NoLeave);
        check(rite.TricksterDevice && rite.TricksterState == "vow" && !granted.Has(Committed), "Trk_Eliandra_Leave: the rite commits, or is not the device.");
        // Her question needs a personal exchange first (audit r6): the shrine build-up, or the evening on the crates in Drezen.
        var eveningScene = S(E + "ch5.evening");
        Snapshot Evening(Snapshot w) => One(eveningScene, Later(story, w, 10), new[] { E + "drezen.evening" });
        check(!Rules.Available(story, mile, Later(story, granted, 30)), "Trk_Eliandra_Leave: she asks with no personal exchange behind the offering.");
        granted = Evening(granted);
        check(!Rules.Available(story, mile, Later(story, granted, 4)) && Rules.Available(story, mile, Later(story, granted, 30)),
            "Trk_Eliandra_Leave: the first mile is not 24 hours after the leave.");
        var yes = One(mile, Later(story, granted, 30), new[] { Committed }, E + "declined", Closed);
        check(mile.Nodes.Single(n => n.Id == "ask").Choices[0].Set.Contains(Committed)
              && mile.Nodes.Single(n => n.Id == "ask").Choices[1].Set.Contains(E + "declined")
              && mile.Nodes.Single(n => n.Id == "ask").Choices[2].Set.Contains(Closed),
            "Trk_Eliandra_Leave: the first mile is not 0 yes, 1 the soft no, 2 the farewell.");

        // Trk_Eliandra_Counter: gold first with the terms guessed, refused, and the lights still on offer; the counteroffer taken.
        var guessedWorld = One(terms, named, new[] { E + "terms_guessed" }, E + "terms_read");
        check(!Rules.Available(story, rite, guessedWorld), "Trk_Eliandra_Counter: the guessed terms alone open the rite.");
        var watched = One(observe, guessedWorld, new[] { E + "observed" });
        check(Rules.Available(story, rite, watched), "Trk_Eliandra_Counter: the observation does not open the rite.");
        var nameNode = rite.Nodes.Single(n => n.Id == "name");
        check(nameNode.Choices[0].Next == "gold" && nameNode.Choices[0].Forbids.Contains(E + "offer_refused")
              && rite.Nodes.Single(n => n.Id == "gold").Choices.Single().Next == "name_again"
              && rite.Nodes.Single(n => n.Id == "gold").Choices.Single().Set.Contains(E + "offer_refused"),
            "Trk_Eliandra_Counter: gold is not first, or is not refused back into the rite.");
        var refusedGold = Program.Copy(watched); refusedGold.Flags.Add(E + "offer_refused");
        var shown = rite.Nodes.Single(n => n.Id == "name_again").Choices.Where(c => Rules.Match(c.Requires, c.Forbids, refusedGold)).ToList();
        check(shown.All(c => c.Next != "gold") && shown.Any(c => c.Check != null), "Trk_Eliandra_Counter: after the refusal the lights are gone, or gold is back.");
        var both = One(rite, watched, new[] { Leave, Lights, Reward, E + "offer_refused" });
        check(!both.Has(NoLeave), "Trk_Eliandra_Counter: the counteroffer taken still leaves her bound.");
        One(rite, watched, new[] { NoLeave, E + "refused_for_her" }, Leave);
        One(rite, watched, new[] { NoLeave, E + "cost.tried_to_cheat" }, Leave);
        check(rite.Nodes.SelectMany(n => n.Choices).Where(c => c.Next == "cheat").All(c => c.Mythic == "PlayerIsTrickster"),
            "Trk_Eliandra_Counter: the hand behind the back is not the Trickster's.");

        // Trk_Eliandra_NoLeaveAndKingList: walked away, her own offering, the soft no, the road letter; the King's list.
        var walked = One(rite, read, new[] { NoLeave }, Leave, E + "refused_for_her", E + "cost.tried_to_cheat");
        check(!Rules.Available(story, self, Later(story, walked, 10)) && Rules.Available(story, self, Later(story, walked, 60)),
            "Trk_Eliandra_NoLeaveAndKingList: her own offering is not 48 hours after the refusal.");
        var hers = One(self, Later(story, walked, 60), new[] { Leave, Reward }, Lights);
        check(self.TricksterDevice && self.TricksterState == "no_leave", "Trk_Eliandra_NoLeaveAndKingList: her offering is not the no_leave device.");
        check(!Rules.Available(story, mile, Later(story, hers, 30)), "Trk_Eliandra_NoLeaveAndKingList: after the walk-away she asks with no exchange behind it.");
        hers = Evening(hers);
        var no = One(mile, Later(story, hers, 30), new[] { E + "declined" }, Committed, Closed);
        check(!Rules.Available(story, letter, Later(story, no, 10)) && Rules.Available(story, letter, Later(story, no, 60)),
            "Trk_Eliandra_NoLeaveAndKingList: the road letter is not 48 hours after the soft no.");
        var answered = One(letter, Later(story, no, 60), new[] { Committed, E + "letter_answered" });
        check(Rules.Available(story, heart, Later(story, answered, 20)), "Trk_Eliandra_NoLeaveAndKingList: the letter's yes does not lead to the star-heart.");
        // The King's Ch5 list is shared with the Table and Last Call (13 §7 (a)): every prior entry keeps its order; hers comes
        // after every route's entry; the frameworks' entries (Last Call's bottle, the Table's offer) follow all routes by
        // construction, and the Table's native opener is inserted after every scene entry (Main.cs), so it is never displaced.
        var kingList = story.Scenes.Where(s => s.AnswerLists.Contains(KingC5)).Select(s => s.Id).ToList();
        var mine = kingList.Where(id => id.StartsWith(E, StringComparison.Ordinal)).ToList();
        var prior = new[] { "jerribeth.trickster.never_met.toast_king", "aranka.trickster.verse.kings_tavern_c5", "aranka.trickster.failure.mocking_verse_c5",
                            "jannah.trickster.react.king_gaol", "jannah.trickster.react.king_muster", "trickster.lastcall.bottle.king", "household.table.offered_c5" };
        var others = kingList.Where(id => !mine.Contains(id)).ToList();
        var routes = new[] { "jerribeth.", "aranka.", "jannah." };
        check(mine.Count == 1 && prior.All(others.Contains) && prior.Select(id => others.IndexOf(id)).SequenceEqual(prior.Select(id => others.IndexOf(id)).OrderBy(i => i))
              && kingList.Where(id => routes.Any(r => id.StartsWith(r, StringComparison.Ordinal))).All(id => kingList.IndexOf(id) < kingList.IndexOf(mine[0]))
              && story.Openers.Any(o => o.AnswerList == KingC5)
              && story.Scenes.Single(s => s.Id == mine[0]).NativeReturnCue == KingReturn
              && story.Scenes.Single(s => s.Id == mine[0]).Forbids.Contains("fool_king.gone"),
            "Trk_Eliandra_NoLeaveAndKingList: her one King entry does not keep the prior entries in order after every route's: " + string.Join(",", kingList));
        var tavern = story.Presences["eliandra.presence"];
        var mark = story.Presences["eliandra.presence.mark"];
        check(tavern.At!.NearUnit == "253cdb8f434e5a6469b75e18428316e3" && tavern.At.Side == "front" && Math.Abs(tavern.At.Distance - 8f) < 0.01f
              && tavern.Unit == Unit && tavern.Area == Drezen && tavern.Mode == "spawn-copy" && tavern.Dialog == "hub"
              && tavern.Forbids.Contains("fool_king.gone") && tavern.Forbids.Contains("eliandra.presence.failed")
              && mark.At!.NearUnit == "bc1093231b1577a4485a730c29595195" && mark.At.Offset!.SequenceEqual(new[] { -5.2f, 3.2f }) && mark.RequiresAnyGroups.Any(g => g.Contains("eliandra.presence.failed") && g.Contains("fool_king.gone")),
            "Trk_Eliandra_NoLeaveAndKingList: the presence is not in front of the persistent tailor, with the jeweller street as fallback.");
        foreach (var pair in story.Presences.Where(p => p.Key != "eliandra.presence" && p.Value.At?.NearUnit == tavern.At!.NearUnit))
        {
            var a = Spot(tavern); var b = Spot(pair.Value);
            check(Math.Sqrt((a.X - b.X) * (a.X - b.X) + (a.Z - b.Z) * (a.Z - b.Z)) >= 4.0, "Trk_Eliandra_NoLeaveAndKingList: " + pair.Key + " stands within 4 m of her.");
        }
        check(story.Presences.Values.Where(p => p.Unit == Unit).All(p => p.At?.NearUnit != Fye && p.At?.NearUnit != Wilcer && p.At?.NearUnit != Smith),
            "Trk_Eliandra_NoLeaveAndKingList: a presence of hers stands at Fye, the yard or the smith.");
        check(presenceBeats.All(s => s.ContactUnit == Unit && s.Areas.SequenceEqual(new[] { Drezen })
                                     && (s.InteractionHub == "eliandra.presence" || s.InteractionHub == "eliandra.presence.mark"))
              && presenceBeats.Where(s => s.Id.StartsWith(E + "drezen.", StringComparison.Ordinal)).All(s => s.Requires.Contains(E + "heart_seen")),
            "Trk_Eliandra_NoLeaveAndKingList: a Drezen beat is not on her presence, or a courtship beat comes before the star-heart.");
        // Native lifecycle (audit r4): her shrine unit is in the captive pool that Pulura_Chapter05_Mechanics destroys once
        // C5_MutasafenFall_quest completes (her greeting completes it). The delayed beats never wait on the shrine: her own
        // offering, the first mile and the star-heart are hosted on her Drezen presence, which stands from the meeting on, and
        // the terms and the rite have Drezen twins for a Commander who left the shrine before asking.
        var metOnly = World(story, 5, "trickster", "trickster.ever", Met);
        check(Rules.PresenceWanted(tavern, metOnly) && tavern.Requires.SequenceEqual(new[] { "trickster.ever", Met, "eliandra.presence.route_open", "eliandra.present_now" }),
            "Lifecycle: her presence does not stand in Drezen from the meeting on.");
        check(new[] { self, mile, heart }.All(s => s.InteractionHub == "eliandra.presence" && s.AnswerLists.Length == 0 && s.NativeReturnCue == null)
              && shrine.All(s => s.DelayHours == 0),
            "Lifecycle: a delayed beat waits on the shrine, whose unit is destroyed after the quest.");
        var riteTwin = S(E + "ch5.last_rite_drezen");
        var termsTwin = S(E + "ch5.terms_drezen");
        check(riteTwin.InteractionHub == "eliandra.presence" && riteTwin.TricksterDevice && riteTwin.Forbids.Contains(rite.Id) && rite.Forbids.Contains(riteTwin.Id)
              && Rules.Available(story, termsTwin, metOnly)
              && Program.Walk(riteTwin, One(termsTwin, metOnly, new[] { E + "terms_read" })).Any(r => r.Has(Leave)),
            "Lifecycle: a Commander who left the shrine before asking cannot reach the terms and the rite in Drezen.");
        foreach (var s in presenceBeats.Where(s => s.InteractionHub == "eliandra.presence.mark"))
            check(s.Id.EndsWith("_mark", StringComparison.Ordinal) && s.Forbids.Contains(s.Id.Substring(0, s.Id.Length - 5))
                  && S(s.Id.Substring(0, s.Id.Length - 5)).Forbids.Contains(s.Id), "A mark twin does not shut its tavern twin: " + s.Id);

        // Trk_Eliandra_StarHeart (Directive 12): desire, the threshold, the cut, the morning with Katair.
        var night = One(heart, Later(story, yes, 20), new[] { E + "heart_seen", E + "charts" });
        check(new[] { "want", "robes", "wrist", "charts", "morning", "katair", "wrong" }.All(id => heart.Nodes.Any(n => n.Id == id))
              && heart.Nodes.Single(n => n.Id == "charts").Choices.All(c => c.Next == "morning"),
            "Trk_Eliandra_StarHeart: the night is not staged to the cut and carried into the morning.");
        check(Rules.PresenceWanted(tavern, night) && !Rules.PresenceWanted(mark, night), "Trk_Eliandra_StarHeart: she does not come to the King's tavern after.");
        var ulbrig = reactions.Where(s => s.Owner == "Ulbrig").ToArray();
        check(ulbrig.Length == 2 && ulbrig.All(s => s.Requires.Contains(E + "heart_seen") && s.Forbids.Contains("ulbrig.dead") && s.Forbids.Contains("ulbrig.kicked_out")),
            "Trk_Eliandra_StarHeart: Ulbrig does not speak after the star-heart, or is unguarded.");

        // Coexistence: nothing gates on another woman's death, departure or refusal.
        var allowed = new HashSet<string> { "eliandra.dead", "ulbrig.dead", "lann.dead", "daeran.dead", "fool_king.gone", "sacrifice" };
        foreach (var s in story.Scenes.Where(s => s.Relationship == "eliandra"))
            foreach (var key in s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(allowed.Contains(key) || !(key.EndsWith(".closed", StringComparison.Ordinal) && key != Closed)
                      && !key.EndsWith("_dead", StringComparison.Ordinal) && !key.EndsWith(".dead", StringComparison.Ordinal)
                      && !key.EndsWith("_gone", StringComparison.Ordinal) && !key.EndsWith(".gone", StringComparison.Ordinal),
                    "Coexistence: " + s.Id + " gates on " + key);
        var produced = new HashSet<string>(story.Scenes.Where(s => s.Relationship == "eliandra").SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set));
        foreach (var s in story.Scenes.Where(s => s.Relationship == "eliandra"))
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)).Where(k => k.StartsWith(E, StringComparison.Ordinal)))
                check(produced.Contains(key) || story.Derived.ContainsKey(key) || story.Scenes.Any(o => o.Id == key), "A gate has no producer: " + s.Id + " requires " + key);

        // Reactions and pages.
        check(reactions.Length == 3 && reactions.All(s => s.Nodes.Count == 1)
              && reactions.Select(s => s.Owner).Distinct().OrderBy(o => o).SequenceEqual(new[] { "Thaberdine", "Ulbrig" }),
            "Eliandra's reactors are not exactly the allocated King Thaberdine and Ulbrig (twice) (ledger 05 §3.1 row 13).");
        var swords = S(E + "ch5.regnard");
        check(swords.Nodes.Single(n => n.Id == "hands").Choices.Single().Set.Contains(E + "regnard_swords_home")
              && swords.Nodes.Single(n => n.Id == "keep").Choices.Single().Set.Contains(E + "regnard_sword_kept")
              && S(E + "epilogue.together").Nodes.Single().Paragraphs.Count(p => p.Requires.Contains(E + "regnard_sword_kept") || p.Requires.Contains(E + "regnard_swords_home")) == 2,
            "Regnard's swords do not end as the player chose.");
        check(!story.Scenes.Any(s => s.Id == E + "ch5.inventory") && terms.Nodes.Any(n => n.Id == "decide")
              && terms.Nodes.Single(n => n.Id == "decide").Choices.Single().Set.Contains(E + "planned"),
            "The planning is not the player's choice inside the terms.");
        check(pages.Length == 8 && pages.All(s => s.MinChapter == 6 && s.MaxChapter == 6 && s.Nodes.SelectMany(n => n.Choices).All(c => c.Set.Length == 0)),
            "Her epilogue pages are not eight read-only Chapter 6 pages.");
        check(Rules.Available(story, S(E + "epilogue.together"), World(story, 6, night.Flags.ToArray()))
              && !Rules.Available(story, S(E + "epilogue.late"), World(story, 6, night.Flags.ToArray())),
            "The committed page is not the only page of a committed route.");
        // The soft no alone is no romance: the late page needs the road letter kept with its answer promised (R2-6).
        check(!Rules.Available(story, S(E + "epilogue.late"), World(story, 6, no.Flags.ToArray()))
              && Rules.Available(story, S(E + "epilogue.declined"), World(story, 6, no.Flags.ToArray())),
            "The soft no alone unlocks the late romance page, or has no ending of its own.");
        var kept = One(letter, Later(story, no, 60), new[] { E + "letter_kept" }, Committed);
        check(Rules.Available(story, S(E + "epilogue.late"), World(story, 6, kept.Flags.ToArray()))
              && !Rules.Available(story, S(E + "epilogue.declined"), World(story, 6, kept.Flags.ToArray()))
        // eng7-l13: preparation also requires the live outcome contract.
              && story.Derived[E + "late_committed"].SequenceEqual(new[] { new[] { "trickster.ever", E + "letter_kept", "eliandra.outcome.route_open" } }, new SeqEq()),
            "The kept letter does not carry the R2-6 late yes.");
        // A committed Commander who survived the finale by the bottle keeps her page (ledger row 16: commander_back).
        var survived = World(story, 6, night.Flags.Concat(new[] { "sacrifice", "ending.trickster" }).ToArray());
        check(survived.Has("trickster.commander_back") && Rules.Available(story, S(E + "epilogue.together"), survived),
            "A committed Commander back from the sacrifice loses her page.");
        // The hand behind the back is answered on the road: the truth leads to her question, a second lie to the soft no.
        var cheated = One(rite, watched, new[] { NoLeave, E + "cost.tried_to_cheat" }, Leave);
        var paidAfterCheat = One(self, Later(story, cheated, 60), new[] { Leave, Reward });
        var road = Later(story, Evening(paidAfterCheat), 30);
        One(mile, road, new[] { Committed }, E + "lied_about_hand");
        var liedAgain = One(mile, road, new[] { E + "declined", E + "lied_about_hand" }, Committed);
        check(Program.Walk(letter, Later(story, liedAgain, 60)).Any(r => r.Has(Committed)),
            "The second lie leaves no reachable yes from the road.");
        // What she misses follows the cost: only a woman who gave her strength back mourns it.
        var miss = S(E + "drezen.questions").Nodes.Single(n => n.Id == "miss").Choices;
        check(miss.Count == 2 && miss.Single(c => c.Next == "miss_slow").Requires.Contains(Reward)
              && miss.Single(c => c.Next == "miss_strong").Forbids.Contains(Reward),
            "Her answer about her strength does not follow the cost.");
        // What the rendered outcomes say (audit r3): a withheld promise is not a promise; the soft no after the lights alone keeps her
        // strength on the page; her own offering is hers at the morning after.
        var roadScene = S(E + "drezen.road");
        check(roadScene.Nodes.Single(n => n.Id == "war").Choices.All(c => !c.Set.Contains(E + "drezen.road_promised") && c.Set.Contains(E + "drezen.road_open"))
              && roadScene.Nodes.Where(n => n.Id != "war").SelectMany(n => n.Choices).Where(c => c.Set.Length > 0).All(c => c.Set.Contains(E + "drezen.road_promised")),
            "A refused first spring still promises the road.");
        var together = S(E + "epilogue.together").Nodes.Single().Paragraphs;
        check(together.Single(p => p.Requires.Contains(E + "drezen.road_promised")).Forbids.Length == 0
              && together.Single(p => p.Requires.Contains(E + "drezen.road_open")).Forbids.Contains(E + "drezen.road_promised"),
            "The first spring's paragraphs do not follow the answer given.");
        var declinedParas = S(E + "epilogue.declined").Nodes.Single().Paragraphs;
        var lightsOnlyNo = World(story, 6, One(mile, Later(story, granted, 30), new[] { E + "declined" }).Flags.ToArray());
        bool Shown(Paragraph p, Snapshot w) => p.Requires.All(w.Has) && !p.Forbids.Any(w.Has);
        check(declinedParas.Where(p => Shown(p, lightsOnlyNo)).All(p => !SurfaceIds.Has(SurfaceIds.Of(story, p), "[eliandra.trickster.epilogue.declined/page/paragraph/2]") && !SurfaceIds.Has(SurfaceIds.Of(story, p), "[eliandra.trickster.epilogue.declined/page/paragraph/0]"))
              && declinedParas.Any(p => Shown(p, lightsOnlyNo) && SurfaceIds.Has(SurfaceIds.Of(story, p), "[eliandra.trickster.epilogue.declined/page/paragraph/3]")),
            "The soft no after the lights alone tells of a strength she never gave, or of a letter never read.");
        var selfNight = Later(story, answered, 20);
        var answerNode = heart.Nodes.Single(n => n.Id == "answer").Choices;
        check(!selfNight.Has(Lights) && answerNode.Single(c => c.Next == "answer_self").Forbids.Contains(Lights)
              && answerNode.Single(c => c.Next == "answer_given").Requires.Contains(Lights)
              && Program.Walk(heart, selfNight).Count > 0,
            "The morning after credits the Commander with her own offering.");
        check(chiefs.Chapters.SequenceEqual(new[] { 3 }), "The chiefs' ground page can arrive in the Abyss with its Drezen frame.");
        // R2-6 (audit r7): released and courted but out of Chapter 5 before her question: a definite late yes on the page;
        // released with no exchange at all: no romance.
        var courtedLate = World(story, 6, granted.Flags.Concat(new[] { E + "flirted" }).ToArray());
        var bareLate = World(story, 6, One(rite, read, new[] { Leave, Lights }, Reward, NoLeave).Flags.ToArray());
        check(Rules.Available(story, S(E + "epilogue.unasked"), courtedLate) && !Rules.Available(story, S(E + "epilogue.released"), courtedLate)
              && Rules.Available(story, S(E + "epilogue.released"), bareLate) && !Rules.Available(story, S(E + "epilogue.unasked"), bareLate),
            "The late pages do not follow whether she was courted before the war ran out.");
        check(story.SelectedAnswers["eliandra.northern_lights_awakened"] == "984d9d1432ea89044a6515be61a22125",
            "The Threshold lights paragraph does not read the artifact actually awakened.");
        // Last Call (R2-6): her coda plays for the commit or the kept letter, and not for the soft no alone.
        var coda = S("eliandra.lastcall.page");
        check(coda.RequiresAnyGroups.Length == 1 && coda.RequiresAnyGroups[0].Contains(Committed) && coda.RequiresAnyGroups[0].Contains(E + "late_committed")
              && Rules.Available(story, coda, World(story, 6, kept.Flags.Concat(new[] { "lastcall.active" }).ToArray()))
              && !Rules.Available(story, coda, World(story, 6, no.Flags.Concat(new[] { "lastcall.active" }).ToArray())),
            "Her Last Call coda does not follow the kept letter, or plays for the soft no alone.");
        // The stranded Drezen state (audit r9): the shrine unit gone, the terms misheard on either presence; the wall observation
        // opens the rite there, and the yes is still reachable, with the King present or gone.
        foreach (var (twinId, gone) in new[] { (E + "ch5.terms_drezen", false), (E + "ch5.terms_drezen_mark", true) })
        {
            var start = gone ? World(story, 5, "trickster", "trickster.ever", Met, "fool_king.gone") : World(story, 5, "trickster", "trickster.ever", Met);
            var misheard = One(S(twinId), start, new[] { E + "terms_guessed" }, E + "terms_read");
            var suffix = gone ? "_mark" : "";
            check(!Rules.Available(story, S(E + "ch5.last_rite_drezen" + suffix), misheard), "Stranded: the rite opens on misheard terms alone.");
            var watchedWall = One(S(E + "ch5.observe_drezen" + suffix), misheard, new[] { E + "observed" });
            var releasedThere = One(S(E + "ch5.last_rite_drezen" + suffix), watchedWall, new[] { Leave });
            var eve = One(S(E + "ch5.evening" + suffix), Later(story, releasedThere, 10), new[] { E + "drezen.evening" });
            One(S(E + "ch5.first_mile" + suffix), Later(story, eve, 30), new[] { Committed });
        }
        // The late yes is a romance only when the player chose one.
        var friendLate = World(story, 6, One(rite, watched, new[] { Leave, Lights, Reward }).Flags.Where(f => f != E + "flirted").ToArray());
        check(!friendLate.Has(E + "flirted") && Rules.Available(story, S(E + "epilogue.released"), friendLate)
              && !Rules.Available(story, S(E + "epilogue.unasked"), friendLate),
            "A friend who never showed interest is given a romance on the late page.");
        // Rest-delivered pages in Chapter 5: the planning page, and the road letter on the soft no only.
        var remote5 = own.Where(s => Rules.IsRemote(s) && s.Chapters.Contains(5) && s.Owner != "EliandraEpilogue").Select(s => s.Id).ToList();
        check(remote5.SequenceEqual(new[] { E + "ch5.road_letter" }),
            "Chapter 5 delivers more than the one soft-no letter by rest (ledger §4.2): " + string.Join(",", remote5));
        var farewell = One(mile, Later(story, granted, 30), new[] { Closed });
        check(Rules.Available(story, S(E + "epilogue.closed"), World(story, 6, farewell.Flags.ToArray()))
              && !Rules.Available(story, S(E + "epilogue.together"), World(story, 6, farewell.Flags.ToArray())),
            "The farewell does not end on her own road.");

        Console.WriteLine("PASS: Eliandra Trickster (Trk_Eliandra_*): the chiefs' ground and the red sky, " + nfit.Length + " N-fit shrine beats, "
            + "the terms, the rite (gold refused, the lights taken, the counteroffer, the hand behind the back, the walk), her own offering, "
            + "the first mile and the road letter, the star-heart, " + presenceBeats.Length + " Drezen beats, the King's list, "
            + reactions.Length + " reactions and " + pages.Length + " pages.");
    }
}
