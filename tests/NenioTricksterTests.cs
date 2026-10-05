using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Nenio, Trickster (Writer/handoffs/trickster/nenio.md; binding plan 11-ROSTER-PLAN-2 §2 and its build sheet, after the Astra
// design review r3): "A name for a name". One block per rules test (Trk_Nenio_*): the riddle in the Enigma (the stake, the
// told answer, the failed telling rebuilt once, the dissolution), her hypothesis and her own test (clean, tampered, dictated,
// replicated, denied), the loss worlds (the Sphinx's servant for a dead or a Ch1-killed Nenio; the field report and the
// probation for a sent-away or kicked-out one), the dictation spine, the night and the morning, the pages, the two reactors,
// the presence, and the Areelu G6(b) overrides.
internal static class NenioTricksterTests
{
    private const string Unit = "1b893f7cf2b150e4f8bc2b3c389ba71d";
    private const string CopyUnit = "49e6676f68337114985a22bd548a8a4d";
    private const string Hub = "1ab909cc3a6194840b1475b99547c263";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string FoxList = "d0eed6e4ca8dd5f478810c3ee59228de";
    private const string FoxReturn = "cfae2454cb77dc8479ff0b044158e067";
    private const string FoxOne = "357224f06cf28804294c737124e66c29";
    private const string FoxTwo = "e7831690d3ccf5f4594e842cb7b8af9e";
    private const string P = "nenio.trickster.";
    private const string F = "nenio.folio.";
    private const string Started = "nenio.started";
    private const string Committed = "nenio.committed";
    private const string Closed = "nenio.closed";
    private const string Returned = P + "returned";
    private const string Scribe = P + "scribe";
    private const string Test = P + "test_running";
    private const string Tampered = P + "tampered";
    private const string Declined = P + "declined";
    private const string NameFiled = P + "cost.name_filed";
    private const string NameStaked = P + "name_staked";
    private const string Owes = P + "cost.owes_an_answer";
    private const string FoxFarewell = "c214b2d290676f344a9227a2711393a6";   // FoxMyself/Cue_0032: she thanks the Commander by name

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        state.AvailableContacts.Add(CopyUnit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    private static Snapshot With(Snapshot state, params string[] flags)
    {
        var next = Program.Copy(state);
        foreach (var flag in flags) if (next.Flags.Add(flag)) next.Times[flag] = next.Hour - 300;
        return next;
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
        List<Snapshot> Through(Scene scene, Snapshot w, string node, int index)
        {
            // eng8-q8f: prove the edge, including empty/shared Set arrays.
            var hits = Program.WalkVia(scene, w, node, index);
            // end eng8-q8f
            foreach (var r in hits)
            {
                // eng8-q8a: observe the native resurrection after this recovery's paid answer.
                if (scene.Recovery == "nenio" && r.Flags.Contains(Returned) && !w.Flags.Contains(Returned))
                {
                    r.Flags.Remove("nenio.dead");
                    r.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
                    Rules.Complete(story, r);
                }
                // end eng8-q8a
            }
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            var hit = Through(scene, w, node, index).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            return hit ?? w;
        }
        var own = story.Scenes.Where(s => s.Relationship == "nenio" && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        using var reachability = new ReachabilityCache();
        bool Reaches(Snapshot start, string flag, int chapter = 5, Func<Snapshot, bool>? keep = null)
            => keep == null
                ? reachability.Reaches(start, flag, chapter, () => Explore(Program.Copy(start), chapter, null))
                : Explore(Program.Copy(start), chapter, keep).Any(s => s.Has(flag));
        IEnumerable<Snapshot> Explore(Snapshot start, int chapter, Func<Snapshot, bool>? keep)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 24 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    yield return from;
                    var w = Later(story, from, 160, chapter);
                    foreach (var scene in own.Where(s => Avail(s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            yield return r;
                            if (keep != null && !keep(r)) continue;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next.Take(300).ToList();
            }
        }

        var rel = story.Relationships["nenio"];
        var riddle = S(P + "taken.riddle");
        var hyp = S(P + "commit.hypothesis");
        var hypVisitor = S(P + "commit.hypothesis_visitor");
        var result = S(P + "commit.result");
        var replication = S(P + "commit.replication");
        var night = S(P + "night");
        var morning = S(P + "morning");
        var price = S(P + "dead.the_price");
        var priceRecreated = S(P + "dead.the_price_recreated");
        var recreated = S(P + "killed.recreated");
        var fieldReport = S(P + "away.field_report");
        var correction = S(P + "away.correction_visitor");
        var first = S(F + "dictation");
        var demons = S(F + "demons");
        // eng8-q8e: E14 replacement text is not an additional authored route page.
        var pages = story.Scenes.Where(s => s.Relationship == "nenio" && s.Owner == "NenioEpilogue" && !Rules.IsNativeReplacement(story, s)).ToArray();

        // Shape and hooks.
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.OrderBy(f => f).SequenceEqual(new[] { "nenio.dead", "nenio.dissolved", "nenio.kicked_out", "nenio.killed_by_commander", "nenio.life.unavailable", "nenio.sent_away" }) // eng8-q8a
              && !rel.UnavailableOverrides.ContainsKey("nenio.dissolved") && rel.UnavailableOverrides.Count == 4
              // eng8-q8a: a bodily return cannot answer a later loss or a different departure.
              && rel.UnavailableOverrides["nenio.dead"] == "nenio.life.recreated"
              && rel.UnavailableOverrides["nenio.killed_by_commander"] == "nenio.life.unremembered"
              && rel.UnavailableOverrides["nenio.sent_away"] == "nenio.life.probation"
              && rel.UnavailableOverrides["nenio.kicked_out"] == "nenio.life.probation"
              // end eng8-q8a
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "enigma", "nenio.away", "nenio.dead", "nenio.killed_by_commander" }),
            "Nenio's relationship does not match the build sheet (four loss overrides to the return, none for the dissolution).");
        check(riddle.AnswerLists.SequenceEqual(new[] { FoxList }) && riddle.NativeReturnCue == FoxReturn && riddle.EntryMythic == "PlayerIsTrickster"
              && riddle.Chapters.SequenceEqual(new[] { 5 }) && riddle.Requires.SequenceEqual(new[] { "trickster", "nenio.asked_to_leave" })
              && riddle.Forbids.Contains("nenio.dissolved") && riddle.TricksterDevice && riddle.TricksterState == "enigma",
            "The riddle is not the inline Trickster device on FoxMyself/AnswersList_0004, returning to Cue_0002.");
        check(Ch(riddle, "start", 0).Check?.Skill == "SkillKnowledgeWorld" && Ch(riddle, "start", 0).Check?.DC == 32
              && Ch(riddle, "start", 1).Check?.DC == 26 && Ch(riddle, "start", 1).Requires.SequenceEqual(new[] { "nenio.asked_forgetting" })
              && Ch(riddle, "start", 2).Check?.DC == 26 && Ch(riddle, "start", 2).Requires.SequenceEqual(new[] { "nenio.asked_gift" })
              && Ch(riddle, "tangled_her", 0).Check?.Skill == "SkillLoreReligion" && Ch(riddle, "tangled_her", 0).Check?.DC == 24,
            "The riddle's checks are not Knowledge (World) 32/26 (after she explained her forgetting or her gift), with one Lore (Religion) rebuild.");
        check(Ch(riddle, "filed", 0).NativeNext == FoxOne && Ch(riddle, "filed", 0).Forbids.Contains("nenio.fox_argued")
              && Ch(riddle, "filed", 1).NativeNext == FoxTwo && Ch(riddle, "filed", 1).Requires.Contains("nenio.fox_argued")
              && riddle.Nodes.Single(n => n.Id == "filed").Choices.All(c => c.Set.Contains(P + "riddle_done") && c.Set.Contains(Started) && c.Set.Contains(NameStaked)),
            "The answered riddle is not one of her two native arguments (Cue_0019 first, Cue_0020 second) with the name staked.");
        // Sol INT: both native arguments can reach her farewell by name (FoxMyself/Cue_0032). The stake is filed only once that
        // farewell has been seen: cost.name_filed is Derived [riddle_done, enigma_resolved], and no choice sets it.
        check(!riddle.Nodes.Any(n => n.Choices.Any(c => c.Set.Contains(NameFiled)))
              && story.Scenes.Where(s => s.Relationship == "nenio").Where(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Contains(NameFiled)))).All(s => s.Id.StartsWith(P + "after_enigma", StringComparison.Ordinal))
              && story.Derived[P + "name_gone"].Length == 2 && story.Derived[P + "name_gone"][1].OrderBy(f => f).SequenceEqual(new[] { "nenio.enigma_resolved", P + "riddle_done" })
              && story.SeenCues["nenio.enigma_resolved"].SequenceEqual(new[] { FoxFarewell }),
            "The name is filed before her native farewell, which still says it.");
        check(!story.Scenes.Where(s => s.Relationship == "nenio").Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal))))),
            "Nenio's device spends a Word Made True (the budget is full).");

        // Trk_Nenio_Riddle: the stake, the told answer, a failure that costs only this wager, and the dissolution.
        var fox = World(story, 5, "trickster", "trickster.ever", "nenio.asked_to_leave");
        check(Avail(riddle, fox) && !Avail(riddle, World(story, 5, "trickster", "trickster.ever", "nenio.asked_to_leave", "nenio.dissolved"))
              && !Avail(riddle, World(story, 5, "trickster.ever", "trickster.failed", "nenio.asked_to_leave")),
            "Trk_Nenio_Riddle: the riddle is closed in the Enigma, or open after the dissolution or the lost path.");
        var staked = Take(riddle, fox, "filed", 0, P + "riddle_done", NameStaked, Started);
        check(!Avail(riddle, staked) && !staked.Has(NameFiled), "Trk_Nenio_Riddle: the wager can be made twice, or files the name at once.");
        check(!story.Scenes.Any(s => s.Id == P + "taken.filing"), "A rest delivery files the name (Sol r1 COX: no extra Chapter 5 delivery).");
        var afterEnigma = S(P + "after_enigma");
        var agedStake = Later(story, staked, 200);
        var farewellSeen = Later(story, With(staked, "nenio.enigma_resolved"), 13);
        check(!agedStake.Has(P + "name_gone") && !Avail(afterEnigma, agedStake) && farewellSeen.Has(P + "name_gone") && Avail(afterEnigma, farewellSeen)
              && Program.Walk(afterEnigma, farewellSeen).Where(r => r.Has(afterEnigma.Id)).All(r => r.Has(NameFiled)),
            "The name is filed without her farewell, or the talk after the Enigma does not follow it.");
        var told = Take(riddle, fox, "told", 0, P + "riddle_declined");
        check(!told.Has(Started) && !told.Has(Closed) && !told.Has(Declined), "Trk_Nenio_Riddle: the told answer closes more than the wager.");
        var failed = Take(riddle, fox, "lost", 0, P + "riddle_declined");
        check(!failed.Has(Closed) && Reaches(Later(story, failed, 1), Committed), "Trk_Nenio_Riddle: a failed telling locks the romance (review r3 HOW).");
        check(Program.Walk(riddle, fox).Any(r => r.Has(P + "riddle_done")) && riddle.Nodes.Single(n => n.Id == "rebuilt").Choices.Single().Next == "stake",
            "Trk_Nenio_Riddle: the rebuilt riddle does not lead back to the stake.");
        check(Reaches(staked, Committed), "Trk_Nenio_Riddle: no road from the stake to the commit.");

        // Trk_Nenio_Dictated: in the party, the dictation entry leaves the space; a stated fact aborts; the hypothesis commits.
        var party = World(story, 3, "trickster", "trickster.ever", "nenio.friendship_concluded");
        check(Avail(first, party) && !Avail(hyp, party), "Trk_Nenio_Dictated: the dictation is not the entry, or the question comes before any session.");
        var scribed = Take(first, party, "go_on", 0, Scribe, Started);
        check(Avail(demons, Later(story, scribed, 24)) && !Avail(hyp, Later(story, scribed, 24)), "Trk_Nenio_Dictated: the second session does not follow, or the question comes too soon.");
        var margin = Take(demons, Later(story, scribed, 24), "hand", 0);
        var asked = Later(story, margin, 24);
        check(Avail(hyp, asked) && Avail(hyp, Later(story, margin, 24, 5)) && !Avail(hyp, Later(story, margin, 24, 4)),
            "Trk_Nenio_Dictated: the hypothesis is not open in Chapters 3 and 5 after the second session.");
        check(Ch(hyp, "dictated", 0).Abort && Ch(hyp, "unmeant", 1).Next == "dictated" && Ch(hyp, "dodge", 2).Abort,
            "Trk_Nenio_Dictated: a stated fact does not stop her (and leave the hypothesis open).");
        var running = Take(hyp, asked, "conditions", 0, Test, Started);
        check(!running.Has(Tampered) && !Avail(result, Later(story, running, 12)) && Avail(result, Later(story, running, 24)),
            "Trk_Nenio_Dictated: the result does not come the morning after the clean night.");
        var yes = Take(result, Later(story, running, 24), "variable", 0, Committed, P + "first_night");
        check(!Program.Walk(result, Later(story, running, 24)).Any(r => r.Has(Declined)),
            "Trk_Nenio_Dictated: a clean night can end in her void ruling.");
        var no = Take(result, Later(story, running, 24), "variable", 2, P + "refused_her", Closed);
        check(!no.Has(Committed), "Trk_Nenio_Dictated: the Commander's no still commits.");

        // Trk_Nenio_Tampered: the reminders void it; a confession replicates it; a denial closes it.
        var tampering = Take(hyp, asked, "conditions", 1, Test, Tampered);
        var voided = Take(result, Later(story, tampering, 24), "void_her", 0, Declined);
        check(!voided.Has(Committed) && !voided.Has(Closed) && !Avail(replication, Later(story, voided, 48)) && Avail(replication, Later(story, voided, 72)),
            "Trk_Nenio_Tampered: the contaminated night does not void the result, or the replication does not wait three days.");
        check(Take(replication, Later(story, voided, 72), "morning", 0, Committed, P + "confessed", P + "replicated", P + "first_night").Has(Committed),
            "Trk_Nenio_Tampered: the confession does not earn a clean replication and her yes.");
        check(Take(replication, Later(story, voided, 72), "denied", 0, Closed).Has(Closed), "Trk_Nenio_Tampered: the denial does not close it.");
        check(Avail(S(F + "void_days"), Later(story, voided, 24)), "Trk_Nenio_Tampered: she does not work on the evidence between the ruling and the question.");

        // Trk_Nenio_Night: the threshold and the morning, the reactors, and the study after.
        var nightWorld = Later(story, yes, 4);
        check(Avail(night, nightWorld) && !Rules.IsRemote(night) && !night.Optional, "Trk_Nenio_Night: the night does not follow her yes.");
        var slept = Take(night, nightWorld, "watch", 0, P + "night");
        check(Avail(morning, Later(story, slept, 6)), "Trk_Nenio_Night: the morning does not follow.");
        var after = Take(morning, Later(story, slept, 6), "war", 0, P + "morning_after");
        check(Avail(S(F + "longitudinal"), Later(story, after, 48)), "Trk_Nenio_Night: the study does not continue after the morning.");
        check(night.Nodes.Single(n => n.Id == "count").Choices.Any(c => c.Requires.Contains("nenio.fox_revealed"))
              && night.Nodes.Single(n => n.Id == "count").Choices.Any(c => c.Forbids.Contains("nenio.fox_revealed")),
            "Trk_Nenio_Night: her tail is not gated on the kitsune reveal.");
        var sosiel = S(P + "react.sosiel_point_five");
        check(sosiel.Reaction && sosiel.AnswerLists.SequenceEqual(new[] { "129b55b8b5d50974f84f7c607d894fd0" }) && sosiel.Requires.Contains(P + "night") && !sosiel.Requires.Contains(P + "first_night")
              && sosiel.Forbids.Contains("sosiel.dead") && sosiel.Forbids.Contains("sosiel.kicked_out"),
            "Trk_Nenio_Night: Sosiel's reaction is not on his hub after the first night.");

        // Trk_Nenio_LossEntries: dead (revived for the notes, or recreated), killed (recreated, unremembered), away (probation).
        var dead = World(story, 3, "trickster", "trickster.ever", "nenio.dead", "revive.nenio.available");
        check(Avail(price, dead) && !Avail(priceRecreated, dead) && price.Recovery == "nenio" && price.TricksterDevice,
            "Trk_Nenio_LossEntries: the Sphinx's claim does not come for a retained body (or the recreated twin does too).");
        // Sol CAN: the chapel scene is staged in Drezen; never in Chapter 4, when the campaign is in the Abyss.
        check(price.Chapters.SequenceEqual(new[] { 3, 5 }) && price.Areas.SequenceEqual(new[] { Drezen })
              && !Avail(price, World(story, 4, "trickster", "trickster.ever", "nenio.dead", "revive.nenio.available"))
              && Avail(price, World(story, 5, "trickster", "trickster.ever", "nenio.dead", "revive.nenio.available")),
            "The Drezen chapel scene can play in the Abyss.");
        var revived = Take(price, dead, "terms", 0, Returned, Started, P + "cost.manuscript_surrendered", P + "cost.owes_an_answer");
        check(Ch(price, "raised", 0).Revive == "nenio" && Reaches(Later(story, revived, 1), Committed), "Trk_Nenio_Dead: no revive, or no road to the commit.");
        check(Take(price, dead, "terms", 1, P + "let_rest").Has(P + "let_rest") && !Avail(price, Take(price, dead, "terms", 1, P + "let_rest")),
            "Trk_Nenio_Dead: refusing the price does not let her rest.");
        var noBody = World(story, 5, "trickster", "trickster.ever", "nenio.dead");
        check(!Avail(price, noBody) && Avail(priceRecreated, noBody), "Trk_Nenio_Dead: with no body the new vessel is not offered.");
        check(!Avail(priceRecreated, World(story, 4, "trickster", "trickster.ever", "nenio.dead")) && priceRecreated.Chapters.SequenceEqual(new[] { 3, 5 }),
            "Sol r3 COX: the new vessel is delivered in the Abyss (R2-5).");
        var remade = Take(priceRecreated, noBody, "terms", 0, Returned, P + "cost.recreated");
        check(Later(story, remade, 1).Has(P + "visitor") && Reaches(Later(story, remade, 1), Committed), "Trk_Nenio_Recreated: she is not a visitor, or cannot be reached.");
        var killed = World(story, 3, "trickster", "trickster.ever", "nenio.killed_by_commander");
        check(Avail(recreated, killed) && recreated.TricksterDevice && Ch(recreated, "purpose", 0).Check?.Skill == "SkillKnowledgeArcana",
            "Trk_Nenio_Killed: the servant does not come to the Kenabres report.");
        var stranger = Take(recreated, killed, "terms", 0, Returned, Started, P + "cost.unremembered", P + "cost.owes_an_answer");
        check(Later(story, stranger, 1).Has(P + "visitor") && Avail(S(P + "killed.stranger_visitor"), Later(story, stranger, 48)),
            "Trk_Nenio_Killed: she does not come to the market, remembering nothing.");
        check(Reaches(Later(story, stranger, 1), Committed), "Trk_Nenio_Killed: no road from the recreation to the commit.");
        var kicked = World(story, 3, "trickster", "trickster.ever", "nenio.kicked_out");
        check(Avail(fieldReport, kicked) && Avail(fieldReport, World(story, 5, "trickster", "trickster.ever", "nenio.sent_away")),
            "Trk_Nenio_Away: the field report is not the device for both departures.");
        var primed = Take(fieldReport, kicked, "reply", 0, P + "primed_away");
        check(!primed.Has(Returned) && Avail(correction, Later(story, primed, 48)),
            "Trk_Nenio_Away: the probation is not offered at the market after the reply.");
        var probation = Take(correction, Later(story, primed, 48), "record", 0, Returned, Started, P + "cost.demoted", Scribe);
        check(Take(correction, Later(story, primed, 48), "record", 1, Closed).Has(Closed) && Reaches(Later(story, probation, 1), Committed),
            "Trk_Nenio_Away: the probation has no refusal, or no road to the commit.");
        check(Avail(hypVisitor, Later(story, Take(S(F + "demons_visitor"), Later(story, probation, 24), "hand", 0), 24)),
            "Trk_Nenio_Away: the question does not come to the market.");
        check(!own.Any(s => Avail(s, World(story, 5, "trickster.ever", "trickster.failed", "nenio.dead"))) && !Avail(price, World(story, 5, "trickster.ever", "trickster.failed", "nenio.dead", "revive.nenio.available")),
            "Trk_Nenio_PathFailed: a loss device opens after the path is lost.");
        check(!own.Any(s => Avail(s, World(story, 5, "trickster", "trickster.ever", "nenio.dissolved", "nenio.asked_to_leave"))),
            "Trk_Nenio_Dissolved: a scene opens after 'Farewell, Nenio.'.");

        // Coexistence: no state closes or reads another relationship; no crowded hub; the presence is off Fye, the yard and the smith.
        var others = story.Relationships.Where(r => r.Key != "nenio").SelectMany(r => new[] { r.Value.StartedFlag, r.Value.ClosedFlag, r.Value.CommittedFlag }).ToHashSet();
        check(story.Scenes.Where(s => s.Relationship == "nenio").All(s => s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g)).All(f => !others.Contains(f))
              && s.Nodes.All(n => n.Choices.All(c => c.Set.All(f => f.StartsWith("nenio.", StringComparison.Ordinal) || f == "trickster.secret.nenio_kenabres")))),
            "A Nenio scene reads or writes another relationship's state.");
        check(!own.Any(s => s.AnswerLists.Contains("0f12118177d102f428a3b30b15b132eb") || s.AnswerLists.Contains("9b15b09c244076047b02f317e55ef5e3")
                            || s.AnswerLists.Contains("a380d926e92f70e429681eb9654478f9") || s.AnswerLists.Contains("15f754455d1d87c42a4e14df456d5415")),
            "A Nenio scene hangs on a crowded hub (Fye, the yard, the smith).");
        var presence = story.Presences["nenio.presence"];
        var arcade = story.Presences["nenio.presence.arcade"];
        check(presence.Unit == CopyUnit && presence.At?.NearUnit == "bad9f602b81a80047ac470b01ebe65a9" && presence.At?.Side == "behind"
              && presence.Requires.Contains(P + "visitor") && presence.Forbids.Contains(Closed) && presence.Dialog == "hub"
              && arcade.At?.NearUnit == "bc1093231b1577a4485a730c29595195" && arcade.Requires.Contains("nenio.presence.failed"),
            "Her presence is not the copy behind the exotic trader (5 m from Aranka), with the jeweller's arcade as the fallback.");
        foreach (var hub in own.Where(s => s.InteractionHub != null))
            check(hub.ContactUnit == CopyUnit && hub.Areas.SequenceEqual(new[] { Drezen }) && hub.Requires.Contains(P + "visitor") && hub.Forbids.Contains(Closed),
                "A market scene is not a visitor scene at her copy: " + hub.Id);
        foreach (var inParty in own.Where(s => s.AnswerLists.Contains(Hub)))
            check(inParty.ContactUnit == Unit && inParty.Forbids.Contains(P + "visitor"), "A hub scene plays for a visitor: " + inParty.Id);

        // Pacing (Sol r1 COX, ledger R2-5): in the Abyss she travels with the company, so her Chapter 4 beats are in person on
        // her hub; the Drezen report is handed over in person after the return; no Nenio rest delivery plays in Chapter 4.
        check(own.Count(s => s.Chapters.SequenceEqual(new[] { 4 }) && !Rules.IsRemote(s) && s.AnswerLists.Contains(Hub) && s.Forbids.Contains(P + "visitor")) >= 3
              && !own.Any(s => s.Id.StartsWith(F, StringComparison.Ordinal) && Rules.IsRemote(s) && s.Chapters.Contains(4) && !s.Forbids.Contains("trickster.ever"))
              && S(F + "drezen.handed_visitor").Chapters.SequenceEqual(new[] { 5 }) && S(F + "drezen.report").Forbids.Contains("trickster.ever"),
            "Pacing: Chapter 4 beats are not in person, or a Chapter 4 rest delivery remains.");
        // Sol r1 INT/BEL: history-bound callbacks.
        HashSet<string> Visited(Scene sc, Snapshot w) { var seen = new HashSet<string>(); Program.Walk(sc, w, (node, _) => seen.Add(node)); return seen; }
        var lamp = S(F + "abyss.lamp");
        check(lamp.Nodes.All(n => !n.Text.Contains("audience hall")), "The lamp remembers an audience the Commander may not have had.");
        check(!Avail(S(F + "who_are_you"), World(story, 5, "trickster", "trickster.ever", Scribe, Started, "nenio.fox_revealed", "nenio.enigma_resolved")),
            "Nenio promises to find the masks after the Enigma was resolved natively.");
        var strangerWorld = World(story, 5, "trickster", "trickster.ever", Returned, P + "cost.unremembered", Scribe, Started);
        check(!Avail(S(F + "kenabres_box_visitor"), Later(story, strangerWorld, 80)) && Avail(S(F + "kenabres_box_visitor"), Later(story, With(strangerWorld, F + "stranger.kenabres_said"), 80)),
            "The box quotes a Kenabres confession that was never made.");
        var nightLost = Visited(night, World(story, 5, "trickster", "trickster.ever", P + "first_night", P + "cost.unremembered"));
        var nightKept = Visited(night, World(story, 5, "trickster", "trickster.ever", P + "first_night"));
        check(nightLost.Contains("bare") && !nightLost.Contains("shelves") && nightKept.Contains("shelves") && !nightKept.Contains("bare")
              && !night.Nodes[0].Text.Contains("ninety-nine"), "The night shows notes she no longer has.");

        // Pages: the article, the late yes, the void, and the closed page; none writes anything.
        check(pages.Select(s => s.Id).OrderBy(i => i).SequenceEqual(new[] { P + "epilogue.article", P + "epilogue.closed", P + "epilogue.commit", P + "epilogue.void", P + "epilogue.scholar" }.OrderBy(i => i))
              && pages.All(s => s.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0))),
            "Nenio's pages are not the article, the late yes, the void and the closed page.");
        var ch6 = World(story, 6, "trickster", "trickster.ever", Started, Committed, NameFiled);
        check(Avail(S(P + "epilogue.article"), ch6) && !Avail(S(P + "epilogue.commit"), ch6), "Pages: the committed page is not the article.");
        // eng8-q8h: ordinary employment cannot grant the romantic conclusion.
        check(!Avail(S(P + "epilogue.commit"), World(story, 6, "trickster", "trickster.ever", Started)), "Employment grants late yes.");
        // Sol COX: the Last Call H2 survival (the bottle, the Wound closed) keeps her romance pages (ledger row 16).
        var h2 = new[] { "sacrifice", "ending.wound_closed", "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle" };
        var h2Committed = World(story, 6, new[] { "trickster", "trickster.ever", Started, Committed }.Concat(h2).ToArray());
        var h2Late = World(story, 6, new[] { "trickster", "trickster.ever", Started, P + "test_running" }.Concat(h2).ToArray());
        check(h2Committed.Has("trickster.commander_back") && !h2Committed.Has("trickster.cheated_death")
              && Avail(S(P + "epilogue.article"), h2Committed) && Avail(S(P + "epilogue.commit"), h2Late),
            "The Last Call H2 survival loses Nenio's romance pages.");
        check(!Avail(S(P + "epilogue.article"), World(story, 6, "trickster", "trickster.ever", Started, Committed, "sacrifice", "ending.wound_closed")),
            "A Commander who burned closing the Wound still gets the article.");

        // Sol TRK: the Sphinx's servant collects in person in Chapter 5, in front of her: paid, paid in the Sphinx's own coin
        // (prepared: the Sphinx's axiom bargained into the terms, Sol r3), or defaulted. No rest delivery; after night one.
        var debt = S(P + "debt.collected");
        check(!Avail(debt, Later(story, World(story, 5, "trickster", "trickster.ever", Returned, Owes, Started, Scribe), 49)),
            "Sol r3 BEL: the Sphinx can collect (and take volume one) before night one.");
        var owing = World(story, 5, "trickster", "trickster.ever", Returned, Owes, Started, Scribe, P + "night");
        check(!Rules.IsRemote(debt) && debt.AnswerLists.Contains(Hub) && Avail(debt, Later(story, owing, 49)) && !Avail(debt, World(story, 6, "trickster", "trickster.ever", Returned, Owes, Started, Scribe, P + "night")),
            "The Sphinx does not come to collect in person in Chapter 5.");
        var debts = Program.Walk(debt, owing).Where(r => r.Has(debt.Id)).ToList();
        check(debts.Any(r => r.Has(P + "debt.paid")) && debts.Any(r => r.Has(P + "debt.defaulted")) && !debts.Any(r => r.Has(P + "debt.evaded")),
            "The collection offers the Sphinx's coin without the prepared silence, or lacks payment or default.");
        check(Program.Walk(debt, With(owing, P + "cost.silence_clause")).Any(r => r.Has(P + "debt.evaded"))
              && !Program.Walk(debt, With(owing, F + "who_are_you.silent", "nenio.fox_revealed")).Any(r => r.Has(P + "debt.evaded")),
            "Sol r3 TRK: the loophole is not gated on the clause bargained into the terms.");
        var clauseWorld = Take(price, dead, "terms", 2, P + "cost.silence_clause");
        check(clauseWorld.Has(P + "cost.silence_clause") && Ch(price, "clause", 0).Next == "raised",
            "Sol r3 TRK: the silence clause is not bargained at the Sphinx's price, or does not raise her.");
        // Sol r3 BEL: the preparation list is for an open debt only.
        check(new[] { "debt.paid", "debt.evaded", "debt.defaulted" }.All(k => story.Scenes.Where(sc => sc.Id.StartsWith(F + "sphinx_list", StringComparison.Ordinal)).All(sc => sc.Forbids.Contains(P + k))),
            "Sol r3 BEL: Nenio prepares for a debt already settled.");
        // Sol r3 INT: the native dissolution is never overridden by a happy page.
        foreach (var epPage in new[] { "epilogue.article", "epilogue.commit", "epilogue.void" })
            check(S(P + epPage).Forbids.Contains("nenio.dissolved"), "Sol r3 INT: " + epPage + " ignores nenio.dissolved.");
        check(!Avail(S(P + "epilogue.article"), World(story, 6, "trickster", "trickster.ever", Started, Committed, "nenio.dissolved")),
            "Sol r3 INT: committed-then-dissolved gets the living article.");
        foreach (var loss in new[] { "nenio.dead", "nenio.killed_by_commander", "nenio.sent_away", "nenio.kicked_out" })
            check(!Avail(S(P + "epilogue.article"), World(story, 6, "trickster", "trickster.ever", Started, Committed, loss))
                  && Avail(S(P + "epilogue.article"), World(story, 6, "trickster", "trickster.ever", Started, Committed, loss, Returned,
                      loss == "nenio.dead" ? P + "cost.recreated" : loss == "nenio.killed_by_commander" ? P + "cost.unremembered" : P + "cost.demoted")) // eng8-q8a: matching paid receipt fixture
                  && !Avail(S(P + "epilogue.commit"), World(story, 6, "trickster", "trickster.ever", Started, loss))
                  && !Avail(S(P + "epilogue.closed"), World(story, 6, "trickster", "trickster.ever", Started, Closed, loss)),
                "Sol r4 INT: a living epilogue plays over an unrecovered loss: " + loss);
        check(!Avail(S(P + "epilogue.closed"), World(story, 6, "trickster", "trickster.ever", Started, Closed, "nenio.dissolved")), "Sol r4 INT: the closed page after the dissolution.");
        check(!Avail(debt, With(owing, P + "debt.paid")), "The debt can be collected twice.");
        var article = S(P + "epilogue.article");
        var owedPara = article.Nodes[0].Paragraphs.Single(pp => pp.Requires.SequenceEqual(new[] { Owes }));
        check(new[] { "debt.paid", "debt.evaded", "debt.defaulted" }.All(k => owedPara.Forbids.Contains(P + k)
              && article.Nodes[0].Paragraphs.Any(pp => pp.Requires.SequenceEqual(new[] { P + k }))),
            "The article does not record how the debt was settled.");

        // Sol INT/BEL: page one reads the native quest (unvisited, prepared at the Ruins, resolved without the riddle).
        var pageOne = S(F + "page_one");
        string Opening(Snapshot w)
        {
            var nodes = new List<string>();
            Program.Walk(pageOne, w, (node, _) => nodes.Add(node));
            return string.Join(",", new[] { "pre", "post", "visiting", "unvisited", "resolved" }.Where(nodes.Contains));
        }
        var scribe5 = World(story, 5, "trickster", "trickster.ever", Scribe, Started);
        check(Visited(pageOne, scribe5).Contains("entry_plain") && !Visited(pageOne, scribe5).Contains("entry")
              && Visited(pageOne, With(scribe5, "nenio.fox_revealed")).Contains("entry"), "Page one announces a rediscovered species before the reveal.");
        check(Opening(scribe5) == "unvisited" && Opening(With(scribe5, "nenio.fox_revealed")) == "pre"
              && Opening(With(scribe5, "nenio.fox_revealed", "nenio.enigma_resolved")) == "resolved"
              && Opening(With(scribe5, "nenio.fox_revealed", "nenio.enigma_resolved", P + "riddle_done")) == "post",
            "Page one announces the Enigma to a Commander who never went near it, or after it was resolved.");
        // Sol BEL: at the edge she recalls reading Sarkoris only if she did.
        var edge = S(F + "edge");
        var edgeNodes = new HashSet<string>();
        Program.Walk(edge, World(story, 5, "trickster", "trickster.ever", Scribe, Started), (node, _) => edgeNodes.Add(node));
        var edgeRead = new HashSet<string>();
        Program.Walk(edge, World(story, 5, "trickster", "trickster.ever", Scribe, Started, F + "architect.the_dead"), (node, _) => edgeRead.Add(node));
        check(!edgeNodes.Contains("sarkoris") && edgeNodes.Contains("read_first") && edgeRead.Contains("sarkoris") && !edgeRead.Contains("read_first"),
            "The edge remembers a reading of Sarkoris that never happened.");

        // Reactions: Anevia at the gate (a Ch1-killed Nenio walks in), guarded by her own return.
        var anevia = S(P + "react.anevia_gate");
        check(anevia.Reaction && anevia.Requires.Contains(Returned) && anevia.Requires.Contains("nenio.killed_by_commander")
              && anevia.Forbids.Contains("anevia_gone") && anevia.ForbidOverrides["anevia_gone"] == "anevia.trickster.returned",
            "Anevia's gate reaction is not guarded by her own fate and return.");

        // Areelu G6(b): her Nenio lines lift the four losses (never the dissolution) on Nenio's return.
        var areeluReact = S("areelu.trickster.react.nenio_two_drafts");
        check(areeluReact.ForbidOverrides.Count == 4
              // eng8-q8a: foreign reactors consume the same matching loss-specific returns.
              && areeluReact.ForbidOverrides["nenio.dead"] == "nenio.life.recreated"
              && areeluReact.ForbidOverrides["nenio.killed_by_commander"] == "nenio.life.unremembered"
              && areeluReact.ForbidOverrides["nenio.sent_away"] == "nenio.life.probation"
              && areeluReact.ForbidOverrides["nenio.kicked_out"] == "nenio.life.probation"
              // end eng8-q8a
              && !areeluReact.ForbidOverrides.ContainsKey("nenio.dissolved"),
            "Areelu's reaction does not carry the G6(b) overrides to Nenio's return.");
        var visitors = S("areelu.trickster.report.visitors").Nodes.Single(n => n.Id == "start").Choices;
        check(visitors.Last().Next == "nenio" && visitors.Last().Requires.SequenceEqual(new[] { Returned }) && visitors.Last().Forbids.SequenceEqual(new[] { "nenio.dissolved" }),
            "Areelu's 'Let Nenio in' has no appended G6(b) twin for a returned Nenio.");
    }
}
