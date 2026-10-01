using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Nidalynn, Trickster (Writer/handoffs/11-ROSTER-PLAN-2.md §2, "The egg the golems counted as floor"; spec
// trickster/nidalynn.md for canon and hooks). One block per rules test (Trk_Nidalynn_*): the device on the golems' list and
// its vault fallback, the widow's presence and her chosen form, the hatching and what the Commander says to the crowd
// (confess, lie, burn), the claim given up or kept, her proposal with bread and salt when the hatchling first flies
// (no test, no second ask), the heel of the loaf, the snowfield, Devarra's bill, the reactors and the pages. Her door
// never depends on the Gold Dragon path, and nothing romantic is staged while she wears the widow.
internal static class NidalynnTricksterTests
{
    private const string P = "nidalynn.trickster.";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Jeweller = "bc1093231b1577a4485a730c29595195";
    private const string WidowUnit = "e24a8cb4f83960748b5bead99d58a36e";
    private const string ChosenUnit = "3191b154bbed71b4595a5154ad067e90";
    private const string GolemList = "dd8ac86f25e0f6b4cac75386eb528851";
    private const string GolemReturn = "d39b1e850904daa43b7e6dab3a6e7f83";
    private const string Committed = "nidalynn.committed";
    private const string Closed = "nidalynn.closed";
    private const string Bill = "devarra.trickster.cost.egg_withheld";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(WidowUnit);
        state.AvailableContacts.Add(ChosenUnit);
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
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            var chosen = Ch(scene, node, index);
            var hits = Program.Walk(scene, w).Where(r => chosen.Set.All(r.Has) && (chosen.Set.Length > 0 || r.Has(scene.Id))).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        var mine = story.Scenes.Where(s => s.Relationship == "nidalynn").ToArray();
        var own = mine.Where(s => !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = mine.Where(s => s.Owner == "NidalynnEpilogue").ToArray();
        var reactions = mine.Where(s => s.Reaction).ToArray();
        // Plays every available Nidalynn scene forward and reports whether a flag is reachable.
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
                frontier = next.Take(400).ToList();
            }
            return false;
        }

        var device = S(P + "eggs.lamp_black");
        var vault = S(P + "eggs.vault");
        var stone = S(P + "hearth.grey_stone");
        var widow = S(P + "steps.widow");
        var hearth = S(P + "hearth.listening");
        var kiln = S(P + "kiln.fire");
        var hatching = S(P + "kiln.hatching");
        var owed = S(P + "kiln.truth_owed");
        var whose = S(P + "kiln.whose");
        var again = S(P + "kiln.claim_again");
        var form = S(P + "door.own_form");
        var wings = S(P + "wall.wings");
        var flight = S(P + "ridge.first_flight");
        var heel = S(P + "kiln.the_heel");
        var snow = S(P + "ridge.snowfield");
        var claimedFlight = S(P + "ridge.claimed_flight");
        var smallest = S("devarra.tower.smallest_egg");

        // Shape: the relationship, her two access states, her presences.
        var rel = story.Relationships["nidalynn"];
        check(rel.StartedFlag == "nidalynn.started" && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed && rel.UnavailableFlags.Length == 0
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "golems", "vault" })
              && rel.TricksterAccess["golems"].Device == device.Id && rel.TricksterAccess["vault"].Device == vault.Id
              && rel.TricksterAccess.Values.All(a => a.Returned == P + "met"),
            "Nidalynn's relationship does not match 11 §2.");
        foreach (var key in new[] { "nidalynn.presence", "nidalynn.presence.chosen" })
        {
            var p = story.Presences[key];
            check(p.Area == Drezen && p.At?.NearUnit == Jeweller && p.At.Distance >= 2.0f && p.Dialog == "hub" && p.Forbids.Contains(Closed)
                  && p.MinChapter == 3 && p.MaxChapter == 5,
                "Her presence is not on the jeweller's steps in Drezen, Chapters 3 to 5: " + key);
        }
        check(story.Presences["nidalynn.presence"].Unit == WidowUnit && story.Presences["nidalynn.presence"].Forbids.Contains(P + "form_chosen")
              && story.Presences["nidalynn.presence.chosen"].Unit == ChosenUnit && story.Presences["nidalynn.presence.chosen"].Requires.Contains(P + "form_chosen"),
            "The widow and her chosen form are not two bodies, one after the other.");
        foreach (var crowded in new[] { "0f12118177d102f428a3b30b15b132eb", "a380d926e92f70e429681eb9654478f9", "15f754455d1d87c42a4e14df456d5415" })
            check(story.Presences.Where(p => p.Key.StartsWith("nidalynn", StringComparison.Ordinal)).All(p => p.Value.At?.NearUnit != crowded),
                "Nidalynn stands at a crowded anchor (Fye, the yard or the smith).");
        foreach (var s in own.Where(x => !Rules.IsRemote(x) && x.InteractionHub != null))
            check(s.Areas.SequenceEqual(new[] { Drezen }) && (s.InteractionHub == "nidalynn.presence" ? s.ContactUnit == WidowUnit : s.ContactUnit == ChosenUnit),
                "A step scene is not on her presence: " + s.Id);

        // Trk_Nidalynn_Device: the golems' count, Stealth or Trickery, the fist on a failure, and not smashing it.
        var checks = device.Nodes.SelectMany(n => n.Choices).Where(c => c.Check != null).Select(c => c.Check!).ToArray();
        check(device.AnswerLists.SequenceEqual(new[] { GolemList }) && device.NativeReturnCue == GolemReturn && device.Chapters.SequenceEqual(new[] { 3 })
              && device.TricksterDevice && device.Requires.SequenceEqual(new[] { "trickster" })
              && device.Forbids.Contains("eggs.destroyed") && device.Forbids.Contains("eggs.project")
              && checks.Select(k => k.Skill).OrderBy(k => k).SequenceEqual(new[] { "SkillStealth", "SkillThievery" }) && checks.All(k => k.DC == 22)
              && Ch(device, "look", 0).Mythic == "PlayerIsTrickster" && Ch(device, "look", 1).Mythic == "PlayerIsTrickster" && Ch(device, "look", 2).Abort,
            "Trk_Nidalynn_Device: the ash-bin is not a Trickster's Stealth or Trickery under the golems' fists, before they act.");
        var sanctum = World(story, 3, "trickster", "trickster.ever", "eggs.seen");
        check(Avail(device, sanctum), "Trk_Nidalynn_Device: the golems' list does not offer the count.");
        var walked = Program.Walk(device, sanctum);
        var clean = walked.First(r => r.Has(P + "egg.clean") && r.Has(P + "primed"));
        var fist = walked.First(r => r.Has(P + "cost.hand") && r.Has(P + "primed"));
        check(clean.Has(P + "egg.golems") && fist.Has(P + "egg.golems") && !clean.Has(P + "cost.hand"),
            "Trk_Nidalynn_Device: a clean count and a crushed hand do not both save the egg.");
        var crushed = walked.First(r => r.Has(P + "egg_crushed"));
        check(!crushed.Has(P + "primed") && !Reaches(crushed, "nidalynn.started"), "Trk_Nidalynn_Crushed: the egg under the heel still opens her door.");
        check(!Avail(device, World(story, 3, "trickster", "trickster.ever", "eggs.destroyed"))
              && !Avail(device, World(story, 3, "trickster", "trickster.ever", "eggs.project")),
            "Trk_Nidalynn_Device: the count is offered after the clutch's fate.");
        check(!own.Any(s => s.TricksterDevice && Avail(s, World(story, 3, "trickster.ever", "trickster.failed", "eggs.project"))),
            "Trk_Nidalynn_AfterFailure: a lost Trickster hides an egg.");

        // Trk_Nidalynn_Vault: the crated clutch, before the druids or the cooks; the egg carried out hot.
        var crated = World(story, 3, "trickster", "trickster.ever", "eggs.project");
        check(Avail(vault, Later(story, crated, 25)) && vault.TricksterDevice && Rules.IsRemote(vault) && vault.Kind == "event",
            "Trk_Nidalynn_Vault: the vault is shut while the crates wait.");
        check(!Avail(vault, Later(story, World(story, 3, "trickster", "trickster.ever", "eggs.project", "eggs.druids"), 25))
              && !Avail(vault, Later(story, World(story, 3, "trickster", "trickster.ever", "eggs.project", "eggs.omelet"), 25)),
            "Trk_Nidalynn_Vault: the vault opens after the druids or the cooks took the clutch.");
        var carried = Program.Walk(vault, Later(story, crated, 25));
        check(carried.Any(r => r.Has(P + "primed") && r.Has(P + "cost.palms") && r.Has(P + "egg.vault") && !r.Has(P + "clerk_saw"))
              && carried.Any(r => r.Has(P + "primed") && r.Has(P + "clerk_saw")),
            "Trk_Nidalynn_Vault: the burnt palms or the clerk who saw are missing.");
        check(Reaches(carried.First(r => r.Has(P + "primed")), Committed), "Trk_Nidalynn_Vault: no road to the commit.");

        // Trk_Nidalynn_Door: the grey stone, then the widow on the steps; she reads the clutch's fate in her own words.
        check(Avail(stone, Later(story, clean, 13)) && !Avail(widow, Later(story, clean, 13)), "Trk_Nidalynn_Door: the rock does not come before the widow.");
        var rock = After(stone, Later(story, clean, 13), "end", 0).First();
        check(Avail(widow, Later(story, rock, 25)), "Trk_Nidalynn_Door: the widow is not on her step.");
        foreach (var world in new[] { "eggs.destroyed", "eggs.omelet", "eggs.druids", "eggs.project" })
        {
            var w = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "hearth.grey_stone", world), 25);
            check(Program.Walk(widow, w).All(r => r.Has(P + "met") && r.Has("nidalynn.started")), "Trk_Nidalynn_Door: the widow does not meet the Commander when " + world);
        }
        var met = After(widow, Later(story, rock, 25), "rock", 1).First();
        check(met.Has(P + "told_egg") && After(widow, Later(story, rock, 25), "rock", 0).First().Has(P + "told_rock"), "What the Commander tells her is not recorded.");
        check(Reaches(clean, Committed), "Trk_Nidalynn_Golems: no road to the commit from the golems' count.");
        check(Reaches(fist, Committed), "Trk_Nidalynn_Fist: the crushed hand closes the road.");

        // The spine: the hearth, the kiln, the hatching.
        check(Avail(hearth, Later(story, met, 25)) && !Avail(kiln, Later(story, met, 25)), "The hearth does not come before the kiln.");
        var agreed = Program.Walk(hearth, Later(story, met, 25)).First(r => r.Has(P + "kiln_agreed"));
        check(agreed.Has(P + "revealed"), "She does not tell the Commander what she is before the kiln.");
        var fisted = Later(story, World(story, 3, "trickster.ever", P + "primed", P + "met", "nidalynn.started", P + "cost.hand"), 25);
        check(Program.Walk(hearth, fisted).Any(r => r.Has(P + "hand_set")), "Trk_Nidalynn_Fist: she does not set the hand.");
        var fired = After(kiln, Later(story, agreed, 25), "knocking", 0).First();
        check(fired.Has(P + "kiln") && Avail(hatching, Later(story, fired, 49)), "The kiln does not lead to the hatching.");

        // Trk_Nidalynn_Confess: the crowd at the kiln; the truth costs Favors and the claim question follows.
        var lane = Later(story, fired, 49);
        var her = hatching.Nodes.Single(n => n.Id == "her").Choices;
        check(her.Count == 4 && her[0].Set.Contains(P + "confessed") && her[0].Crusade?.Resource == "Favors"
              && her[1].Set.Contains(P + "lied_at_kiln") && her[2].Set.Contains(Closed) && her[2].Set.Contains(P + "given_to_the_crowd")
              && her[3].Set.Contains(P + "confessed") && her[3].Requires.Contains(P + "egg.vault") && her[0].Forbids.Contains(P + "egg.vault"),
            "Trk_Nidalynn_Confess: the kiln's pivot is not confess, lie or burn.");
        var confessed = After(hatching, lane, "said", 0).First();
        check(confessed.Has(P + "hatched") && confessed.Has(P + "confessed") && Avail(whose, Later(story, confessed, 25)),
            "Trk_Nidalynn_Confess: the confession does not lead to whose she is.");
        var burned = Program.Walk(hatching, lane).First(r => r.Has(P + "given_to_the_crowd"));
        check(burned.Has(Closed) && !Reaches(burned, Committed), "Trk_Nidalynn_Burn: giving her to the fire is not a hard no.");

        // Trk_Nidalynn_Lie: the lie told to the lane; she will not eat at that fire; the muster, or she goes.
        var lied = Program.Walk(hatching, lane).First(r => r.Has(P + "lied_at_kiln"));
        check(lied.Has(P + "hatched") && !Avail(whose, Later(story, lied, 25)) && Avail(owed, Later(story, lied, 49)),
            "Trk_Nidalynn_Lie: the lie does not bring her question.");
        var muster = After(owed, Later(story, lied, 49), "salt", 0).First();
        check(muster.Has(P + "confessed") && Ch(owed, "salt", 0).Crusade?.Amount == -150 && Avail(whose, Later(story, muster, 25)),
            "Trk_Nidalynn_Lie: the muster is not the dearer confession, or does not lead on.");
        var kept = After(owed, Later(story, lied, 49), "salt", 1).First();
        check(kept.Has(Closed) && kept.Has(P + "lie_kept") && !Reaches(kept, Committed), "Trk_Nidalynn_Lie: keeping the lie is not a no.");

        // Trk_Nidalynn_Claim: given up, or kept; a kept claim can still be let go; a claim kept to Chapter 5 flies away.
        var given = After(whose, Later(story, confessed, 25), "choose", 0).First();
        check(given.Has(P + "cost.claim_given_up") && Avail(form, Later(story, given, 25)), "Trk_Nidalynn_Claim: giving her up does not bring her own face.");
        var claimed = After(whose, Later(story, confessed, 25), "choose", 1).First();
        check(claimed.Has(P + "claimed") && !Avail(form, Later(story, claimed, 25)) && Avail(again, Later(story, claimed, 73)),
            "Trk_Nidalynn_Claim: a claim does not stop her, or leaves no second look.");
        var letGo = After(again, Later(story, claimed, 73), "look", 0).First();
        check(letGo.Has(P + "cost.claim_given_up") && Reaches(letGo, Committed), "Trk_Nidalynn_Claim: letting go late does not reopen the road.");
        var keptClaim = After(again, Later(story, claimed, 73), "look", 1).First();
        check(Avail(claimedFlight, Later(story, keptClaim, 49, 5)) && After(claimedFlight, Later(story, keptClaim, 49, 5), "go", 0).First().Has(Closed)
              && !Avail(flight, Later(story, keptClaim, 49, 5)),
            "Trk_Nidalynn_Claim: a claim kept to her first flight does not lose her.");

        // Trk_Nidalynn_Widow: nothing romantic while she wears the widow; her own face comes first.
        var faced = After(form, Later(story, given, 25), "end", 0).First();
        check(faced.Has(P + "form_chosen") && form.Requires.Contains(P + "cost.claim_given_up") && wings.Requires.Contains(P + "form_chosen")
              && flight.Requires.Contains(P + "kissed") && snow.Requires.Contains(Committed),
            "Trk_Nidalynn_Widow: a kiss or the salt can come before her own face.");
        foreach (var s in own.Where(x => x.InteractionHub == "nidalynn.presence"))
            check(!s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).Any(f => f == P + "kissed" || f == Committed || f == P + "snowfield"),
                "A widow's-step scene carries a romantic beat: " + s.Id);

        // Trk_Nidalynn_Commit: she proposes when the hatchling first flies; bread and salt; eating is the yes.
        var kissed = After(wings, Later(story, faced, 25), "almost", 0).First();
        check(!Avail(flight, Later(story, kissed, 49, 3)) && Avail(flight, Later(story, kissed, 49, 5)), "Trk_Nidalynn_Commit: the first flight is not a Chapter 5 beat.");
        var offer = flight.Nodes.Single(n => n.Id == "offer").Choices;
        check(offer.Count == 3 && offer[0].Set.Contains(Committed) && offer[0].Set.Contains(P + "cost.salt_eaten") && offer[1].Set.Contains(P + "bread_kept")
              && !offer[1].Set.Contains(Closed) && offer[2].Set.Contains(Closed) && offer.All(c => c.Check == null && c.Crusade == null),
            "Trk_Nidalynn_Commit: the salt is not a plain yes, a not-yet and a no.");
        var yes = After(flight, Later(story, kissed, 49, 5), "offer", 0).First();
        check(yes.Has(Committed) && Avail(snow, Later(story, yes, 13)), "Trk_Nidalynn_Commit: the yes does not lead to the snowfield.");
        var notYet = After(flight, Later(story, kissed, 49, 5), "offer", 1).First();
        check(Avail(heel, Later(story, notYet, 73)) && After(heel, Later(story, notYet, 73), "wait", 0).First().Has(Committed)
              && Ch(heel, "sit", 0).Abort,
            "Trk_Nidalynn_Heel: the loaf on the shelf does not keep, or cannot be eaten later.");
        var committers = own.Where(s => s.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(Committed))).Select(s => s.Id).OrderBy(i => i);
        check(committers.SequenceEqual(new[] { heel.Id, flight.Id }), "Something other than the salt commits her.");
        check(!own.Any(s => s.Id.Contains("second_ask") || s.Id.Contains("riddle")), "A priced second ask or a riddle test was built.");
        var snowed = After(snow, Later(story, yes, 13), "down_the_hill", 0).First();
        check(snowed.Has(P + "snowfield") && snow.Nodes.Any(n => n.Id == "cut") && snow.Nodes.Single(n => n.Id == "cut").Choices.Count == 1,
            "Trk_Nidalynn_Snowfield: the ridge has no cut.");

        // Devarra's bill (ledger 05 row 5): on her own hub, after the confession; it lands on the Commander on every answer.
        check(smallest.Relationship == "devarra" && smallest.Requires.Contains("nidalynn.trickster.confessed") && smallest.Requires.Contains("devarra.trickster.returned")
              && smallest.Nodes.Single(n => n.Id == "pay").Choices.All(c => c.Set.Contains(Bill)),
            "Trk_Nidalynn_Bill: Devarra's bill is not on her hub, or can be refused.");
        var shortScene = S("devarra.tower.one_short");
        var dvPrimed = Later(story, World(story, 3, "trickster.ever", "devarra.trickster.returned", "devarra.started", P + "primed"), 25);
        check(shortScene.Relationship == "devarra" && Avail(shortScene, dvPrimed) && Program.Walk(shortScene, dvPrimed).All(r => r.Has("devarra.tower.one_short"))
              && shortScene.Nodes.SelectMany(n => n.Choices).All(c => !c.Set.Any(f => f.EndsWith(".closed", StringComparison.Ordinal))),
            "Trk_Nidalynn_Custody: Devarra has no beat when her twelfth egg is taken, or it closes something.");
        var dv = Later(story, World(story, 3, "trickster.ever", "devarra.trickster.returned", "devarra.started", "nidalynn.trickster.confessed"), 25);
        check(Avail(smallest, dv) && Program.Walk(smallest, dv).All(r => r.Has(Bill)), "Trk_Nidalynn_Bill: the bill never lands.");
        foreach (var s in mine)
            check(!s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)).Any(k => k.StartsWith("devarra.", StringComparison.Ordinal)),
                "A Nidalynn scene is gated on Devarra (ledger 05 row 5: node reads only): " + s.Id);
        foreach (var s in mine)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!(key.EndsWith(".closed", StringComparison.Ordinal) && key != Closed) && !key.EndsWith(".dead", StringComparison.Ordinal)
                      && !key.EndsWith("_dead", StringComparison.Ordinal) && !key.StartsWith("mythic.", StringComparison.Ordinal) && key != "dragon",
                    "Nidalynn needs someone else dead or closed, or the Gold Dragon path: " + s.Id + " " + key);

        // Reactors, pages, household.
        check(reactions.Length == 4 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Select(r => r.Owner).OrderBy(o => o).SequenceEqual(new[] { "Greybor", "Ulbrig", "Ulbrig", "Woljif" }),
            "The reactions are not Greybor, Ulbrig and Woljif.");
        check(pages.Length == 9 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        check(story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "form_chosen" })
              && story.Derived["nidalynn.harem.eligible"].Length == 2 && story.Derived.ContainsKey("nidalynn.harem.voice.fed_at_the_fire"),
            "The late commit or the household eligibility is not declared.");
        var produced = new HashSet<string>(mine.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Concat(mine.Select(s => s.Id)));
        foreach (var s in own)
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)).Where(k => k.StartsWith(P, StringComparison.Ordinal)))
                check(produced.Contains(key) || story.Latches.ContainsKey(key), "A Nidalynn gate has no producer: " + s.Id + " requires " + key);

        // Q9 (Sol INT/HOW): the acquisition history is read where it matters: the golems' egg and the vault's egg each reach
        // their own question at the hearth, their own truth on the step and their own confession at the kiln.
        List<string> Visited(Scene s, Snapshot w)
        {
            var ids = new List<string>();
            Program.Walk(s, w, (id, st) => ids.Add(id));
            return ids;
        }
        var golemHearth = Later(story, World(story, 3, "trickster.ever", P + "primed", P + "egg.golems", P + "met", "nidalynn.started"), 25);
        var vaultHearth = Later(story, World(story, 3, "trickster.ever", P + "primed", P + "egg.vault", P + "cost.palms", P + "met", "nidalynn.started"), 25);
        check(Visited(hearth, golemHearth).Contains("why") && !Visited(hearth, golemHearth).Contains("why_vault")
              && Visited(hearth, vaultHearth).Contains("why_vault") && !Visited(hearth, vaultHearth).Contains("why"),
            "Trk_Nidalynn_History: the hearth asks the wrong Commander about the golems or the vault.");
        check(Program.Walk(hearth, vaultHearth).Any(r => r.Has(P + "kiln_agreed")), "Trk_Nidalynn_History: the vault's hearth does not reach the kiln.");
        var vaultStep = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "hearth.grey_stone", P + "egg.vault", "eggs.project"), 25);
        check(Program.WalkVia(widow, vaultStep, "rock", 3).All(r => r.Has(P + "told_egg")) && Program.WalkVia(widow, vaultStep, "rock", 3).Count > 0
              && Program.WalkVia(widow, vaultStep, "rock", 1).Count == 0,
            "Trk_Nidalynn_History: the vault's Commander tells the widow about the golems.");
        var vaultLane = Later(story, World(story, 3, "trickster.ever", P + "primed", P + "egg.vault", P + "met", "nidalynn.started", P + "kiln"), 49);
        var vaultConfessions = Visited(hatching, vaultLane);
        check(vaultConfessions.Contains("confess_vault") && !vaultConfessions.Contains("confess")
              && Program.Walk(hatching, vaultLane).Any(r => r.Has(P + "confessed") && r.Has(P + "hatched")),
            "Trk_Nidalynn_History: the vault's Commander confesses the golems to the lane.");
        check(!Visited(hatching, lane).Contains("confess_vault"), "Trk_Nidalynn_History: the golems' Commander confesses the vault.");

        // Q9 (Sol INT/HOW): the reunion after the Abyss only for a Commander she met before it; a Chapter 5 first meeting gets
        // its own words; the reunion never plays after the first flight, and its news follows what has happened.
        var back = S(P + "door.home_from_the_dark");
        var ch3Met = Program.Walk(widow, Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "hearth.grey_stone", "eggs.project"), 25));
        check(ch3Met.All(r => r.Has(P + "met") && r.Has(P + "met_before_abyss")), "Trk_Nidalynn_Reunion: a Chapter 3 meeting is not latched.");
        var ch5Met = Program.Walk(widow, Later(story, World(story, 5, "trickster", "trickster.ever", "irabeth.chapter_five", P + "primed", P + "hearth.grey_stone", "eggs.project"), 25));
        check(ch5Met.All(r => r.Has(P + "met") && !r.Has(P + "met_before_abyss")), "Trk_Nidalynn_Reunion: a Chapter 5 first meeting is latched as before the Abyss.");
        var homeEarly = Later(story, ch3Met.First(), 13, 5);
        var homeNew = Later(story, ch5Met.First(), 13);
        check(Avail(back, homeEarly) && Avail(back, homeNew), "Trk_Nidalynn_Reunion: the door after the Abyss does not open.");
        check(Visited(back, homeEarly).Contains("look") && !Visited(back, homeEarly).Contains("look_new")
              && Visited(back, homeNew).Contains("look_new") && !Visited(back, homeNew).Contains("look"),
            "Trk_Nidalynn_Reunion: a Chapter 5 first meeting is greeted as a reunion, or the reunion as a stranger.");
        check(!Visited(back, homeNew).Contains("news_egg") && Visited(back, homeNew).Contains("news_hearth"),
            "Trk_Nidalynn_Reunion: the egg's kiln news reaches a Commander who never took it to the kiln.");
        check(!Avail(back, Later(story, World(story, 5, "trickster.ever", P + "primed", P + "met", P + "met_before_abyss", "nidalynn.started", P + "hatched", P + "proposed"), 13)),
            "Trk_Nidalynn_Reunion: the first night home plays after the first flight.");

        // Q9 (Sol VOI): the wolves story makes innocents pay; she will not raise the hatchling on it. Correct it, or she goes.
        var goat = S(P + "kiln.the_goat");
        var goatWorld = Later(story, World(story, 3, "trickster.ever", P + "met", "nidalynn.started", P + "cost.claim_given_up", P + "hatched"), 49);
        var wolves = Program.WalkVia(goat, goatWorld, "her", 2);
        check(wolves.Any(r => r.Has(P + "goat.corrected") && !r.Has(Closed)) && wolves.Any(r => r.Has(P + "goat.lie_kept") && r.Has(Closed))
              && wolves.All(r => r.Has(P + "goat.corrected") || r.Has(Closed)),
            "Trk_Nidalynn_Goat: the wolves story can stand without correction and without her refusal.");
        check(Ch(goat, "after_wolves", 0).Forbids.Contains(P + "goat.wolves"), "Trk_Nidalynn_Goat: the old acceptance of the wolves is not retired.");

        // Q9 (Sol BEL): her own face answers "why now" without the snowfield's breakfast; the torc is shown as it is.
        check(!form.Nodes.Single(n => n.Id == "now").Text.Contains("chewing") && !form.Nodes.Single(n => n.Id == "now").Text.Contains("bread"),
            "Trk_Nidalynn_Staging: her own face eats bread that was never served.");
        var women = S(P + "steps.the_widows_time");
        foreach (var node in women.Nodes)
            check(!node.Text.Contains("or she is not") && !node.Text.Contains("either way"), "Trk_Nidalynn_Staging: the narrator shows an authoring alternative: " + node.Id);
        var leftWorld = Later(story, World(story, 5, "trickster.ever", P + "met", "nidalynn.started", P + "form_chosen", P + "steps.torcs", P + "torc.left"), 25);
        check(Visited(women, leftWorld).Contains("torc_left") && !Visited(women, leftWorld).Contains("torc"),
            "Trk_Nidalynn_Staging: the girl wears a torc the Commander left in the jeweller's tray.");

        // Q9 r2 (Sol INT/BEL): physical visits only in Drezen; the late yes reaches the Last Call coda; living pages need the
        // Commander back, and a page keeps her when the Commander did not come back.
        foreach (var s in own.Where(x => Rules.IsRemote(x) && x.Kind != "letter"))
            check(s.Areas.SequenceEqual(new[] { Drezen }), "Trk_Nidalynn_Area: a Drezen visit plays outside Drezen: " + s.Id);
        var awayWorld = Later(story, World(story, 3, "trickster.ever", P + "primed"), 13);
        awayWorld.Area = "00000000000000000000000000000000";
        check(!Avail(stone, awayWorld), "Trk_Nidalynn_Area: the hearth page plays away from Drezen.");
        var coda = S("nidalynn.lastcall.page");
        check(coda.RequiresAnyGroups.Length == 1 && coda.RequiresAnyGroups[0].Contains(Committed) && coda.RequiresAnyGroups[0].Contains(P + "late_committed"),
            "Trk_Nidalynn_LastCall: the late commit is missing from her coda.");
        foreach (var id in new[] { "salt", "late", "heel" })
            check(S(P + "epilogue." + id).Forbids.Contains("sacrifice") && S(P + "epilogue." + id).ForbidOverrides["sacrifice"] == "trickster.commander_back",
                "Trk_Nidalynn_Sacrifice: a living page plays for a Commander who did not come back: " + id);
        check(Avail(S(P + "epilogue.unreturned"), World(story, 6, "trickster.ever", Committed, "sacrifice")),
            "Trk_Nidalynn_Sacrifice: no page for the Commander who did not come back.");

        check(Avail(S(P + "epilogue.wolves"), World(story, 6, "trickster.ever", Committed, P + "goat.lie_kept", Closed))
              && S("nidalynn.lastcall.page").Forbids.Contains(P + "goat.lie_kept"),
            "Trk_Nidalynn_Goat: leaving over the wolves story has no page, or the Last Call coda still plays.");

        // Every page beat opens from its own gates.
        foreach (var s in own.Where(x => Rules.IsRemote(x) && !x.TricksterDevice))
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray();
            var w = World(story, s.Chapters[0], new[] { "trickster", "trickster.ever", P + "primed", P + "met", "nidalynn.started" }.Concat(needs).ToArray());
            check(Avail(s, Later(story, w, s.DelayHours + 1)), "A Nidalynn page never opens: " + s.Id);
        }
        Console.WriteLine("PASS: Nidalynn Trickster (Trk_Nidalynn_*): the golems' count and the vault, the widow and her own face, the kiln, "
            + "the crowd (confess, lie, burn), the claim, the salt and the heel, the snowfield, Devarra's bill, "
            + reactions.Length + " reactions and " + pages.Length + " pages.");
    }
}
