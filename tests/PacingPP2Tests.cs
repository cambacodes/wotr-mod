using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// PP2 pacing pass (Writer/handoffs/13-PACING-PASS.md sections 2, 2a, 2b, 7): Camellia (Prologue blood, Chapter 2 cart),
// Kaylessa (Chapter 1 wound, Chapter 2 hunter's limp) and Arueshalae (Chapter 2 prison). Each beat: its host and return,
// path-neutral gates, the .seen flag on the first choice, exactly one outcome on every terminal path, once only, no native
// or Trickster effect, and a named consequence reader that changes visibly. Plus the two near-miss fixes (Camellia's
// bowl, late curtain and kept spread; Arueshalae's torn gift, star-candle and the failed-lair reunion).
internal static class PacingPP2Tests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = Drezen };
        state.Flags.UnionWith(flags);
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Node N(Scene scene, string node) => scene.Nodes.Single(n => n.Id == node);
        Choice C(Scene scene, string node, int i) => N(scene, node).Choices[i];
        bool Avail(Scene scene, Snapshot w) => Rules.Available(story, scene, w);
        HashSet<string> Visited(Scene scene, Snapshot w)
        {
            var seen = new HashSet<string>();
            Program.Walk(scene, w, (id, _) => seen.Add(id));
            return seen;
        }

        // ---- Shared contract for every early beat. ----
        void Beat(string id, string rel, int chapter, string list, string? ret, string[] outcomes, Snapshot open, Snapshot[] shut)
        {
            var beat = S(id);
            var seen = id + ".seen";
            check(beat.Relationship == rel && beat.Chapters.SequenceEqual(new[] { chapter }) && beat.MaxChapter == chapter
                  && beat.AnswerLists.SequenceEqual(new[] { list }) && !Rules.IsRemote(beat),
                id + ": not a physical Chapter " + chapter + " entry on its one host list.");
            check(ret == null ? beat.ReturnToList && beat.NativeReturnCue == null && (beat.ReturnText ?? "").Split(' ').Length <= 25
                              : !beat.ReturnToList && beat.NativeReturnCue == ret,
                id + ": the return is not the reviewed one (ReturnToList, or the retchecked native cue).");
            check(beat.Forbids.Contains(seen) && outcomes.All(beat.Forbids.Contains),
                id + ": the beat does not forbid its own .seen and outcome flags.");
            check(!beat.Requires.Concat(beat.Forbids).Concat(beat.RequiresAnyGroups.SelectMany(g => g))
                      .Any(f => f == "trickster" || f == "trickster.ever" || f.Contains(".harem")),
                id + ": a path-neutral beat reads the Trickster or a harem key.");
            var choices = beat.Nodes.SelectMany(n => n.Choices).ToList();
            check(beat.EntryMythic == null && beat.EntryAlignment == null && !beat.TricksterDevice && beat.TricksterState == null
                  && choices.All(ch => ch.Mythic == null && ch.Crusade == null && ch.StartEtude == null && ch.RemoveItem == null
                                       && ch.Revive == null && ch.NativeNext == null && ch.Alignment == null)
                  && choices.SelectMany(ch => ch.Set).All(f => f.StartsWith(id + ".", StringComparison.Ordinal)),
                id + ": a path-neutral beat carries a native, Trickster or foreign effect.");
            check(beat.Nodes[0].Choices.All(ch => ch.Set.Contains(seen)), id + ": the first choice does not consume the beat.");
            check(Avail(beat, open), id + ": the beat is not offered where its host and gates hold.");
            foreach (var w in shut) check(!Avail(beat, w), id + ": the beat is offered outside its moment.");
            var outs = Program.Walk(beat, open);
            check(outs.Count >= outcomes.Length && outs.All(r => r.Has(seen) && outcomes.Count(r.Has) == 1)
                  && outcomes.All(o => outs.Any(r => r.Has(o))),
                id + ": a terminal path does not end in exactly one outcome, or an outcome is unreachable.");
            foreach (var r in outs)
            {
                var again = Program.Copy(r);
                again.Hour += 48;
                check(!Avail(beat, again), id + ": the beat is offered twice.");
            }
        }

        // ---- Camellia. ----
        Beat("camellia.early.blood", "camellia", 0, "1ca6cf08fceeac141a0df689cecc784a", null,
             new[] { "camellia.early.blood.asked", "camellia.early.blood.kept" },
             World(story, 0), new[] { World(story, 1), World(story, 0, "camellia.closed") });
        Beat("camellia.early.cart", "camellia", 2, "f40abd195a8b1ea46945b47576fa732a", null,
             new[] { "camellia.early.cart.shield", "camellia.early.cart.watch" },
             World(story, 2), new[] { World(story, 3), World(story, 2, "camellia.killed") });
        check(new[] { "asked", "shield_her", "watch_her" }.All(n => N(S(n == "asked" ? "camellia.early.blood" : "camellia.early.cart"), n).SpeakerUnit
                  == "397b090721c41044ea3220445300e1b8"),
            "Camellia: her ReturnToList lines do not name her unit (they would be narrated).");

        // Consequence: Two lies and a truth opens with what she kept (index-safe: choice 0 is the old Continue).
        var game = S("camellia.trickster.masks.two_lies");
        check(C(game, "open", 0).Next == "bored" && C(game, "open", 0).Forbids.Length == 4
              && C(game, "open", 1).Next == "early_asked" && C(game, "open", 2).Next == "early_kept"
              && C(game, "open", 3).Next == "early_shield" && C(game, "open", 4).Next == "early_watch",
            "Camellia: Two lies and a truth's opening indices changed, or the early leads are missing.");
        var plain = Visited(game, World(story, 3, "trickster"));
        check(!plain.Any(n => n.StartsWith("early_", StringComparison.Ordinal)) && plain.Contains("bored"),
            "Camellia: the early leads play without their beats.");
        foreach (var (flags, expect) in new[] {
                     (new[] { "camellia.early.blood.asked", "camellia.early.cart.watch" }, new[] { "early_asked", "early_watch" }),
                     (new[] { "camellia.early.blood.kept", "camellia.early.cart.shield" }, new[] { "early_kept", "early_shield" }),
                     (new[] { "camellia.early.cart.shield" }, new[] { "early_shield" }) })
        {
            var visited = Visited(game, World(story, 3, flags.Prepend("trickster").ToArray()));
            check(expect.All(visited.Contains) && visited.Count(n => n.StartsWith("early_", StringComparison.Ordinal)) == expect.Length,
                "Camellia: Two lies and a truth does not recall exactly " + string.Join("+", expect) + ".");
        }

        // ---- Kaylessa. ----
        const string kayList = "30fa5be33ddd7b144963473692af6942";
        const string nods = "c3ac44c65a5183e4f89fd2990a5fc58c";
        Beat("kaylessa.early.dressed", "kaylessa", 1, kayList, nods,
             new[] { "kaylessa.early.dressed.bound", "kaylessa.early.dressed.lied", "kaylessa.early.dressed.waved" },
             World(story, 1), new[] { World(story, 2), World(story, 1, "kaylessa.healed_by_force"), World(story, 1, "kaylessa.dead") });
        var dressed = S("kaylessa.early.dressed");
        var refusedSeen = Visited(dressed, World(story, 1, "kaylessa.refused_spell"));
        var freshSeen = Visited(dressed, World(story, 1));
        check(refusedSeen.Contains("refused") && !refusedSeen.Contains("fresh") && freshSeen.Contains("fresh") && !freshSeen.Contains("refused"),
            "Kaylessa: the wound opens without regard to whether she already refused a spell (Cue_0066).");
        check(C(dressed, "offer", 0).Check?.Skill == "SkillLoreNature" && C(dressed, "offer", 0).Check?.DC == 16,
            "Kaylessa: the binding is not a Lore (Nature) DC 16 check (native precedent: Forn_Ambush/Check_0014).");
        Beat("kaylessa.early.tells", "kaylessa", 2, kayList, nods,
             new[] { "kaylessa.early.tells.read", "kaylessa.early.tells.missed", "kaylessa.early.tells.refused" },
             World(story, 2, "kaylessa.camp_hunt_told"), new[] { World(story, 2), World(story, 1, "kaylessa.camp_hunt_told") });
        check(story.SeenCues["kaylessa.refused_spell"].SequenceEqual(new[] { "0ab8f1a13d91d9e4d8ac8870ca4e576d" })
              && story.SeenCues["kaylessa.camp_hunt_told"].SequenceEqual(new[] { "1988bcd88fe35424ebf4371eec3f96c5", "1a44532f0f3f8a849b8c5284fd19ed40" }),
            "Kaylessa: the early beats' seen-cue keys are not bound to Cue_0066 and Cue_0040/Cue_0053.");

        // Consequence 1: Hands (appended at [2] and [3] of "mine"; [0] and [1] unchanged).
        var hands = story.Scenes.Single(s => s.Id == "kaylessa.wasps.watching_hands");
        check(C(hands, "mine", 0).Next == "kind_end" && C(hands, "mine", 1).Next == "kind_end"
              && C(hands, "mine", 2).Next == "kenabres" && C(hands, "mine", 2).Requires.SequenceEqual(new[] { "kaylessa.early.dressed.bound" })
              && C(hands, "mine", 3).Next == "kenabres_lie" && C(hands, "mine", 3).Requires.SequenceEqual(new[] { "kaylessa.early.dressed.lied" }),
            "Kaylessa: Hands does not offer the Kenabres lines at the appended indices.");
        // Consequence 2: the hunter's visit, both hunters (appended at [3] and [4]; the old study retired by gating).
        var hunter = S("kaylessa.trickster.alive.hunter");
        foreach (var (node, seenNode) in new[] { ("ask", "seen"), ("ask_s", "seen_s") })
        {
            check(C(hunter, node, 1).Check?.DC == 25 && C(hunter, node, 1).Forbids.Contains("kaylessa.early.tells.read")
                  && C(hunter, node, 1).Forbids.Contains("kaylessa.early.tells.missed") && C(hunter, node, 2).Abort
                  && C(hunter, node, 3).Next == seenNode && C(hunter, node, 3).Check == null
                  && C(hunter, node, 3).Requires.SequenceEqual(new[] { "kaylessa.early.tells.read" })
                  && C(hunter, node, 4).Check?.DC == 18 && C(hunter, node, 4).Check?.Success == seenNode
                  && C(hunter, node, 4).Requires.SequenceEqual(new[] { "kaylessa.early.tells.missed" }),
                "Kaylessa: the hunter's visit (" + node + ") does not pay off the war camp lesson at the appended indices.");
        }

        // ---- Arueshalae. ----
        Beat("arueshalae.early.desna", "arueshalae", 2, "7c789226898962e43802ccf27dc88395", "cec49de78daa68e449e2b83cc664661e",
             new[] { "arueshalae.early.desna.kept", "arueshalae.early.desna.doubted", "arueshalae.early.desna.plain" },
             World(story, 2, "arueshalae.prison_desna_named"), new[] { World(story, 2), World(story, 3, "arueshalae.prison_desna_named") });
        check(story.SeenCues["arueshalae.prison_desna_named"].SequenceEqual(new[] { "37899239473b1d5489109c6155245398" }),
            "Arueshalae: the prison beat's gate is not bound to Cue_0008 (she names Desna).");
        check(S("arueshalae.early.desna").Nodes.All(n => n.Speaker == "Arueshalae" || n.Speaker == "Narrator") && S("arueshalae.early.desna").Owner == "Arueshalae",
            "Arueshalae: the prison beat's lines do not take the return cue's speaker (owner == speaker).");
        var studied = S("arueshalae.treatment.studied");
        check(C(studied, "start", 0).Next == "why" && C(studied, "start", 1).Next == "prison_kept"
              && C(studied, "start", 2).Next == "prison_doubted" && C(studied, "start", 3).Next == "prison_plain",
            "Arueshalae: Night reading's opening indices changed, or the prison leads are missing.");
        foreach (var (flag, node) in new[] { ("arueshalae.early.desna.kept", "prison_kept"), ("arueshalae.early.desna.doubted", "prison_doubted"),
                                             ("arueshalae.early.desna.plain", "prison_plain") })
        {
            var visited = Visited(studied, World(story, 3, "trickster", flag));
            check(visited.Contains(node) && visited.Count(n => n.StartsWith("prison_", StringComparison.Ordinal)) == 1 && visited.Contains("why"),
                "Arueshalae: Night reading does not recall the prison exactly once (" + flag + ").");
        }
        check(!Visited(studied, World(story, 3, "trickster")).Any(n => n.StartsWith("prison_", StringComparison.Ordinal)),
            "Arueshalae: Night reading recalls a prison talk that never happened.");

        // ---- Near-miss: Camellia. ----
        foreach (var twin in new[] { "", "_camp", "_alive" })
        {
            var terms = S("camellia.trickster.returned.terms" + twin);
            var bowl = N(terms, "bowl").Text;
            check(bowl.Contains("pour it out") && !bowl.Contains("while she drank"),
                "Camellia: the terms (" + twin + ") still recall Mireya drinking from a bowl that was poured out.");
            var deck = S("camellia.trickster.cards.the_deck_again" + twin);
            check(C(deck, "wont", 0).Next == "wont_close" && C(deck, "silk", 0).Next == "close" && C(deck, "close", 0).Next == "morning"
                  && C(deck, "wont_close", 0).Next == null,
                "Camellia: the kept spread (" + twin + ") still shares the stacked deck's scattered-cards close.");
            var w = World(story, 5, "trickster.ever", "camellia.committed", "camellia.trickster.returned", "camellia.killed",
                          "camellia.trickster.primed", "camellia.trickster.raised");
            var viaWont = Program.WalkVia(deck, w, "meaning", 0);
            var viaStacked = Program.WalkVia(deck, w, "meaning", 1);
            check(viaWont.Count == 1 && viaStacked.Count == 1, "Camellia: the deck's two answers do not each end once.");
        }
        var curtain = N(S("camellia.trickster.killed.late_curtain"), "scroll").Text;
        check(curtain.Contains("Give her back tonight") && !curtain.Contains("three nights more"),
            "Camellia: the late curtain still bargains for three nights it then skips.");

        // Sol r1 (CAN cap): both cemetery pages are delivered only in Drezen.
        foreach (var id in new[] { "camellia.trickster.killed.late_curtain", "camellia.trickster.killed.third_night" })
            check(S(id).Areas.SequenceEqual(new[] { Drezen }), "Camellia: " + id + " can open after a rest outside Drezen.");

        // ---- Near-miss: Arueshalae. ----
        // Sol r1 (CAN cap): the tailor's-awning copies never stage the jeweller's counter or the arcade.
        foreach (var yard in story.Scenes.Where(s => s.Relationship == "arueshalae" && s.Id.EndsWith("_yard", StringComparison.Ordinal)))
            check(!(yard.Entry + string.Join(" ", yard.Nodes.Select(n => n.Text))).Contains("counter")
                  && !string.Join(" ", yard.Nodes.Select(n => n.Text)).Contains("arcade"),
                "Arueshalae: the awning copy " + yard.Id + " is staged at the jeweller's counter or arcade.");
        var sosielTalk = S("arueshalae.trickster.returned.sosiel");
        check(sosielTalk.Requires.Contains("arueshalae.trickster.react.sosiel_fed") && sosielTalk.Forbids.Contains("sosiel.dead")
              && sosielTalk.Forbids.Contains("sosiel.kicked_out"),
            "Arueshalae: the Sosiel conversation recalls an offer he never made, or a Sosiel who is gone.");
        // Sol r2 (INT): both BackToReality release cues mark her changed; the late yes reaches her Last Call coda.
        check(story.SeenCues["arueshalae.back_to_reality"].SequenceEqual(new[] { "6b24754fcea768342a30a1e18ce91b92", "8ad7c2ba0e060e545b12269cc5ced777" }),
            "Arueshalae: the romance branch's release cue (BackToReality/Cue_0025) does not mark her changed.");
        var coda = S("arueshalae.lastcall.page");
        check(coda.RequiresAnyGroups.Any(g => g.Contains("arueshalae.committed") && g.Contains("arueshalae.trickster.late_committed"))
              && coda.Forbids.Contains("arueshalae.trickster.ally") && coda.Forbids.Contains("arueshalae.trickster.declined"),
            "Arueshalae: the Last Call coda ignores the late yes, or plays after her refusal.");
        // Sol r3: arueshalae.changed is the release from the Abyss (two native paths); only BestEnding has the study's flowers.
        check(!story.Scenes.Where(s => s.Relationship == "arueshalae").SelectMany(s => s.Nodes)
                  .SelectMany(n => n.Paragraphs.Select(pp => pp.Text).Prepend(n.Text)).Any(t => t.Contains("the flowers", StringComparison.OrdinalIgnoreCase)),
            "Arueshalae: a changed-state reader still recalls the flowers, which the BackToReality release never shows.");
        check(S("arueshalae.trickster.react.sosiel_chaplain").Requires.Contains("arueshalae.trickster.chaplain.the_dying"),
            "Arueshalae: Sosiel recalls the dying pikeman before the vigil.");
        var counting = S("arueshalae.trickster.returned.counting");
        check(C(counting, "start", 0).Requires.Contains("arueshalae.trickster.react.sosiel_fed") && C(counting, "start", 1).Requires.Contains("arueshalae.trickster.react.lann_prisoner")
              && C(counting, "start", 2).Next == "you_alone" && C(counting, "start", 3).Next == "him_alone",
            "Arueshalae: the count recalls Sosiel's offer or Lann's word where those reactions never played.");
        check(new[] { city, cityYard }.All(s => N(s, "price").Choices.Select(ch => ch.Next).SequenceEqual(new[] { "taste", "cultist", "refuse" })),
            "Arueshalae: the Drezen reunion offers a captive or courier nobody secured.");
        foreach (var id in new[] { "commit", "kept", "kept_fallen", "fallen" })
        {
            var page = S("arueshalae.trickster.epilogue." + id);
            check(page.Forbids.Contains("sacrifice") && page.ForbidOverrides.TryGetValue("sacrifice", out var back) && back == "trickster.commander_back",
                "Arueshalae: the " + id + " ending ignores the Commander's sacrifice.");
        }
        var starving = S("arueshalae.trickster.dead.starving");
        // The route forbids a crusade fee as the device's price; the torn gift's loss is the flag its readers show
        // (her aftertaste, Sosiel's reaction, the epilogue): a voice gone thin that heals, the thread and the scar that don't.
        var thread = N(starving, "thread").Text;
        check(new[] { 0, 1 }.All(i => C(starving, "thread", i).Set.Contains("arueshalae.trickster.cost.gift_torn") && C(starving, "thread", i).Crusade == null)
              && thread.Contains("voice will come back thin") && !thread.Contains("makes a room turn round")
              && story.Scenes.Count(s => s.Relationship == "arueshalae" && (s.Requires.Contains("arueshalae.trickster.cost.gift_torn")
                  || s.Nodes.Any(n => n.Choices.Any(c => c.Requires.Contains("arueshalae.trickster.cost.gift_torn"))
                                      || n.Paragraphs.Any(pp => pp.Requires.Contains("arueshalae.trickster.cost.gift_torn"))))) >= 3,
            "Arueshalae: the torn gift narrates a loss its readers never show.");
        var cure = N(S("arueshalae.treatment.night"), "cure").Text;
        check(cure.Contains("say the whole of the blessing") && !cure.Contains("before she carried you up"),
            "Arueshalae: the star-candle is still lit offstage before the flight.");
        var letter = S("arueshalae.trickster.evil.reunion_letter");
        check(letter.Requires.Contains("arueshalae.lair_unplaced.latched") && letter.Requires.Contains("arueshalae.awning_unplaced.latched")
              && story.Latches["arueshalae.lair_unplaced.latched"].SequenceEqual(new[] { "arueshalae.presence.evil.failed" })
              && story.Latches["arueshalae.awning_unplaced.latched"].SequenceEqual(new[] { "arueshalae.presence.evil_awning.failed" }),
            "Arueshalae: the lipstick note is still the fallback for a failed lair alone.");
        var city = S("arueshalae.trickster.evil.reunion_city");
        var cityYard = S("arueshalae.trickster.evil.reunion_city_yard");
        check(city.InteractionHub == "arueshalae.presence.evil_drezen" && cityYard.InteractionHub == "arueshalae.presence.evil_awning"
              && cityYard.Requires.Contains("arueshalae.presence.evil_drezen.failed")
              && new[] { city, cityYard }.All(s => !Rules.IsRemote(s) && s.Requires.Contains("arueshalae.lair_unplaced.latched")
                                                 && s.Forbids.Contains("arueshalae.trickster.evil.reunion_letter")
                                                 && s.Forbids.Contains("arueshalae.trickster.reunited")),
            "Arueshalae: the failed-lair reunion is not met in person in Drezen.");
        check(story.Presences["arueshalae.presence.evil_drezen"].RequiresAnyGroups.Any(g => g.Contains("arueshalae.lair_unplaced.latched") && g.Contains("arueshalae.trickster.reunited"))
              && story.Presences["arueshalae.presence.evil_awning"].RequiresAnyGroups.Any(g => g.Contains("arueshalae.lair_unplaced.latched") && g.Contains("arueshalae.trickster.reunited")),
            "Arueshalae: the Drezen presences do not stand for a failed lair before the reunion.");
        // The worst late branch with a failed lair: the referral (visit), the second opinion (letter), then in person.
        var late = World(story, 5, "trickster", "trickster.ever", "arueshalae.evil_dead", "arueshalae.evil_dead.latched",
                         "arueshalae.trickster.primed", "arueshalae.trickster.cost.late", "arueshalae.trickster.returned",
                         "arueshalae.trickster.cost.nocticula_debt", "arueshalae.presence.evil.failed");
        late.AvailableContacts.Add("e3bc95db7e2181d41847b3a1d858258d");
        check(Avail(city, late) && !Avail(letter, late),
            "Arueshalae: with the lair failed, the reunion is a third letter instead of a meeting at the arcade.");
        // The lair's .failed is observed only while the lair is loaded; in Drezen only the latch remains (Sol verify #12).
        var travelled = World(story, 5, "trickster", "trickster.ever", "arueshalae.evil_dead", "arueshalae.evil_dead.latched",
                              "arueshalae.trickster.primed", "arueshalae.trickster.cost.late", "arueshalae.trickster.returned",
                              "arueshalae.trickster.cost.nocticula_debt", "arueshalae.lair_unplaced.latched");
        travelled.AvailableContacts.Add("e3bc95db7e2181d41847b3a1d858258d");
        check(!travelled.Has("arueshalae.presence.evil.failed") && Avail(city, travelled) && !Avail(letter, travelled),
            "Arueshalae: after travelling to Drezen the failed-lair reunion is lost with the transient observation.");
        // A torn gift followed by the prisoner's meal still gets her acknowledgment of the gift.
        var after = S("arueshalae.trickster.returned.aftertaste");
        var prisonerTorn = Visited(after, World(story, 3, "trickster.ever", "arueshalae.trickster.returned",
                                                "arueshalae.trickster.cost.fed_on_prisoner", "arueshalae.trickster.cost.gift_torn"));
        check(prisonerTorn.Contains("gift_him") && prisonerTorn.Contains("him") && !prisonerTorn.Contains("you"),
            "Arueshalae: a torn gift with the prisoner's meal skips her acknowledgment of the gift.");
        var bothDrezen = Program.Copy(late);
        bothDrezen.Flags.Add("arueshalae.presence.evil_drezen.failed");
        bothDrezen.AvailableContacts.Add("2c8caedd0a558524ca0ed1ab3132fae1");
        check(Avail(cityYard, bothDrezen) && !Avail(letter, bothDrezen),
            "Arueshalae: with the jeweller gone, the reunion is not met under the tailor's awning.");
        var lateRemote = story.Scenes.Where(s => s.Relationship == "arueshalae" && Rules.IsMailbagLetter(s)
            && (s.Id == "arueshalae.trickster.evil.late_referral" || s.Id == "arueshalae.trickster.evil.second_opinion"
                || s.Id.StartsWith("arueshalae.trickster.evil.reunion", StringComparison.Ordinal))).Select(s => s.Id).ToList();
        check(lateRemote.SequenceEqual(new[] { "arueshalae.trickster.evil.late_referral", "arueshalae.trickster.evil.second_opinion",
                                               "arueshalae.trickster.evil.reunion_letter" }),
            "Arueshalae: the late branch's remote deliveries changed shape (" + string.Join(", ", lateRemote) + ").");
    }
}
