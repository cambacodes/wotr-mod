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
        // eng-final E-Q8-10: fund the positive fixture; the walker enforces every debit.
        var state = new Snapshot { Chapter = chapter, Area = Drezen, Hour = 5000,
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
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "golems", "straw", "vault" })
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
        var fisted = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "met", "nidalynn.started", P + "cost.hand"), 25);
        check(Program.Walk(hearth, fisted).Any(r => r.Has(P + "hand_set")), "Trk_Nidalynn_Fist: she does not set the hand.");
        var fired = After(kiln, Later(story, agreed, 25), "knocking", 0).First();
        check(fired.Has(P + "kiln") && Avail(hatching, Later(story, fired, 49)), "The kiln does not lead to the hatching.");

        // Trk_Nidalynn_Confess: the crowd at the kiln; the truth costs Favors and the claim question follows.
        var lane = Later(story, fired, 49);
        var her = hatching.Nodes.Single(n => n.Id == "her").Choices;
        check(her.Count == 5 && her[0].Set.Contains(P + "confessed") && her[0].Crusade?.Resource == "Favors"
              && her[0].Forbids.Contains(P + "egg.straw") && her[4].Requires.Contains(P + "cost.slate") && her[4].Set.Contains(P + "confessed")
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
        // eng7-l13: preserve the three saved answers; appended loss exits abort.
        var offer = flight.Nodes.Single(n => n.Id == "offer").Choices.Take(3).ToList();
        check(flight.Nodes.Single(n => n.Id == "offer").Choices.Skip(3).All(c => c.Abort && c.Set.Length == 0), "Appended salt exits grant an outcome.");
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
        var dvPrimed = Later(story, World(story, 3, "trickster", "trickster.ever", "devarra.trickster.returned", "devarra.started", P + "primed"), 25);
        check(shortScene.Relationship == "devarra" && Avail(shortScene, dvPrimed) && Program.Walk(shortScene, dvPrimed).All(r => r.Has("devarra.tower.one_short"))
              && shortScene.Nodes.SelectMany(n => n.Choices).All(c => !c.Set.Any(f => f.EndsWith(".closed", StringComparison.Ordinal))),
            "Trk_Nidalynn_Custody: Devarra has no beat when her twelfth egg is taken, or it closes something.");
        var dv = Later(story, World(story, 3, "trickster", "trickster.ever", "devarra.trickster.returned", "devarra.started", "nidalynn.trickster.confessed"), 25);
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
              && reactions.Select(r => r.Owner).OrderBy(o => o).SequenceEqual(new[] { "Greybor", "Ulbrig", "Ulbrig", "Woljif" })
              && S(P + "react.woljif.small_one").Forbids.Contains("chapter_later"),   // PP10 (Sol COX): Woljif retired by gating
            "The reactions are not Greybor and Ulbrig, with Woljif's retired.");
        // PP10 (Sol COX): the Chapter 4 kiln letter travels with the Storyteller's portal supplies, once he has offered them.
        var kilnLetter = S(P + "letter.from_the_kiln");
        check(kilnLetter.Requires.Contains("storyteller.supplies") && story.SeenCues["storyteller.supplies"].SequenceEqual(new[] { "459bf324a71c81c4ba5f3eead9ba42bb" })
              && !Avail(kilnLetter, Later(story, World(story, 4, "trickster", "trickster.ever", P + "met", "nidalynn.started", P + "kiln"), 25))
              && Avail(kilnLetter, Later(story, World(story, 4, "trickster", "trickster.ever", P + "met", "nidalynn.started", P + "kiln", "storyteller.supplies"), 25))
              && kilnLetter.Nodes[0].Text.Contains("Storyteller"),
            "Trk_Nidalynn_Letter: the kiln letter reaches the Abyss with no carrier.");
        check(pages.Length == 9 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        // eng7-l13: preparation also requires the live outcome contract.
        check(story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "kissed", "nidalynn.outcome.route_open" })
              && !World(story, 6, "trickster", "trickster.ever", P + "met", P + "form_chosen").Has(P + "late_committed")
              && !World(story, 6, "trickster", "trickster.ever", P + "met", P + "form_chosen").Has("nidalynn.harem.eligible")
              && World(story, 6, "trickster", "trickster.ever", P + "met", P + "form_chosen", P + "kissed").Has(P + "late_committed")
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
        var golemHearth = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "egg.golems", P + "met", "nidalynn.started"), 25);
        var vaultHearth = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "egg.vault", P + "cost.palms", P + "met", "nidalynn.started"), 25);
        check(Visited(hearth, golemHearth).Contains("why") && !Visited(hearth, golemHearth).Contains("why_vault")
              && Visited(hearth, vaultHearth).Contains("why_vault") && !Visited(hearth, vaultHearth).Contains("why"),
            "Trk_Nidalynn_History: the hearth asks the wrong Commander about the golems or the vault.");
        check(Program.Walk(hearth, vaultHearth).Any(r => r.Has(P + "kiln_agreed")), "Trk_Nidalynn_History: the vault's hearth does not reach the kiln.");
        var vaultStep = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "hearth.grey_stone", P + "egg.vault", "eggs.project"), 25);
        check(Program.WalkVia(widow, vaultStep, "rock", 3).All(r => r.Has(P + "told_egg")) && Program.WalkVia(widow, vaultStep, "rock", 3).Count > 0
              && Program.WalkVia(widow, vaultStep, "rock", 1).Count == 0,
            "Trk_Nidalynn_History: the vault's Commander tells the widow about the golems.");
        var vaultLane = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "egg.vault", P + "met", "nidalynn.started", P + "kiln"), 49);
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
        // Polish r2 (audit COX): the welcome home is a reunion only; a Chapter 5 first meeting already sat on her step.
        check(Avail(back, homeEarly) && !Avail(back, homeNew), "Trk_Nidalynn_Reunion: the door after the Abyss does not open, or opens for a Chapter 5 first meeting.");
        check(Visited(back, homeEarly).Contains("look") && !Visited(back, homeEarly).Contains("look_new"),
            "Trk_Nidalynn_Reunion: the reunion is greeted as a stranger.");
        var homeHearth = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "hearth.grey_stone", P + "met", P + "met_before_abyss", "nidalynn.started"), 13, 5);
        check(!Visited(back, homeHearth).Contains("news_egg") && Visited(back, homeHearth).Contains("news_hearth"),
            "Trk_Nidalynn_Reunion: the egg's kiln news reaches a Commander who never took it to the kiln.");
        check(!Avail(back, Later(story, World(story, 5, "trickster", "trickster.ever", P + "primed", P + "met", P + "met_before_abyss", "nidalynn.started", P + "hatched", P + "proposed"), 13)),
            "Trk_Nidalynn_Reunion: the first night home plays after the first flight.");

        // Q9 (Sol VOI): the wolves story makes innocents pay; she will not raise the hatchling on it. Correct it, or she goes.
        var goat = S(P + "kiln.the_goat");
        var goatWorld = Later(story, World(story, 3, "trickster", "trickster.ever", P + "met", "nidalynn.started", P + "cost.claim_given_up", P + "hatched"), 49);
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
        var leftWorld = Later(story, World(story, 5, "trickster", "trickster.ever", P + "met", "nidalynn.started", P + "form_chosen", P + "steps.torcs", P + "torc.left"), 25);
        check(Visited(women, leftWorld).Contains("torc_left") && !Visited(women, leftWorld).Contains("torc"),
            "Trk_Nidalynn_Staging: the girl wears a torc the Commander left in the jeweller's tray.");

        // Q9 r2 (Sol INT/BEL): physical visits only in Drezen; the late yes reaches the Last Call coda; living pages need the
        // Commander back, and a page keeps her when the Commander did not come back.
        foreach (var s in own.Where(x => Rules.IsRemote(x) && x.Kind != "letter"))
            check(s.Areas.SequenceEqual(new[] { Drezen }), "Trk_Nidalynn_Area: a Drezen visit plays outside Drezen: " + s.Id);
        var awayWorld = Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed"), 13);
        awayWorld.Area = "00000000000000000000000000000000";
        check(!Avail(stone, awayWorld), "Trk_Nidalynn_Area: the hearth page plays away from Drezen.");
        var coda = S("nidalynn.lastcall.page");
        check(coda.RequiresAnyGroups.Length == 1 && coda.RequiresAnyGroups[0].Contains(Committed) && coda.RequiresAnyGroups[0].Contains(P + "late_committed"),
            "Trk_Nidalynn_LastCall: the late commit is missing from her coda.");
        foreach (var id in new[] { "salt", "late", "heel" })
            check(S(P + "epilogue." + id).Forbids.Contains("sacrifice") && S(P + "epilogue." + id).ForbidOverrides["sacrifice"] == "trickster.commander_back",
                "Trk_Nidalynn_Sacrifice: a living page plays for a Commander who did not come back: " + id);
        check(Avail(S(P + "epilogue.unreturned"), World(story, 6, "trickster", "trickster.ever", Committed, "sacrifice")),
            "Trk_Nidalynn_Sacrifice: no page for the Commander who did not come back.");

        check(Avail(S(P + "epilogue.wolves"), World(story, 6, "trickster", "trickster.ever", Committed, P + "goat.lie_kept", Closed))
              && S("nidalynn.lastcall.page").Forbids.Contains(P + "goat.lie_kept"),
            "Trk_Nidalynn_Goat: leaving over the wolves story has no page, or the Last Call coda still plays.");

        // PP10 (Trk_Nidalynn_Straw): the druids took the clutch after both devices were missed. They carry eleven; the twelfth,
        // left in the straw for dead, is kept by a lie on the stores' slate. It opens the same hearth and the same widow, with
        // its own words at each, and never Devarra's count (which reads PRIMED and tells of an egg carried out of the chamber
        // or the vault). Letting it go out with the bedding is the Commander's no: her door never opens.
        var straw = S(P + "eggs.straw");
        check(rel.TricksterAccess["straw"].Device == straw.Id && straw.TricksterDevice && Rules.IsRemote(straw) && straw.Kind == "event"
              && straw.Requires.Contains("trickster") && straw.Requires.Contains(P + "eggs_given") && straw.Chapters.SequenceEqual(new[] { 3, 5 })
              && story.Latches[P + "eggs_given"].SequenceEqual(new[] { "eggs.druids" }) && straw.DelayHours == 12,
            "Trk_Nidalynn_Straw: the straw is not a Trickster's page after the druids' decree.");
        var druidsTook = World(story, 3, "trickster", "trickster.ever", "eggs.seen", "eggs.project", "eggs.druids");
        check(druidsTook.Has(P + "eggs_given") && Avail(straw, Later(story, druidsTook, 13)) && !Avail(vault, Later(story, druidsTook, 25))
              && !Avail(device, druidsTook),
            "Trk_Nidalynn_Straw: the druids' world has no door, or still offers the golems or the vault.");
        foreach (var shut in new[] { "eggs.omelet", "eggs.destroyed", P + "primed", P + "egg_crushed" })
            check(!Avail(straw, Later(story, World(story, 3, "trickster", "trickster.ever", "eggs.project", "eggs.druids", shut), 13)),
                "Trk_Nidalynn_Straw: the straw opens in a world it does not belong to: " + shut);
        check(!Avail(straw, Later(story, World(story, 3, "trickster.ever", "trickster.failed", "eggs.project", "eggs.druids"), 13))
              && !Avail(straw, Later(story, World(story, 4, "trickster", "trickster.ever", "eggs.project", "eggs.druids"), 13))
              && Avail(straw, Later(story, World(story, 5, "trickster", "trickster.ever", "eggs.project", "eggs.druids"), 13)),
            "Trk_Nidalynn_Straw: a lost Trickster keeps the straw's egg, the straw plays in the Abyss, or a decree finished late has no door.");
        check(Reaches(Program.Walk(straw, Later(story, World(story, 5, "trickster", "trickster.ever", "eggs.project", "eggs.druids", "irabeth.chapter_five"), 13))
                      .First(r => r.Has(P + "egg.straw")), Committed),
            "Trk_Nidalynn_Straw: a Chapter 5 straw egg has no road to the commit.");
        var strawRuns = Program.Walk(straw, Later(story, druidsTook, 13));
        var strawKept = strawRuns.Where(r => r.Has(P + "egg.straw")).ToList();
        check(strawKept.Count == 2 && strawKept.All(r => r.Has(P + "cost.slate")) && strawKept.Any(r => r.Has(P + "quartermaster_knew")) && strawKept.Any(r => !r.Has(P + "quartermaster_knew"))
              && strawKept.All(r => !r.Has(P + "primed")) && Ch(straw, "vault", 0).Check?.Skill == "CheckBluff" && Ch(straw, "vault", 0).Mythic == "PlayerIsTrickster"
              && Ch(straw, "chit", 1).Abort && S("devarra.tower.one_short").Requires.Contains(P + "primed"),
            "Trk_Nidalynn_Straw: the slate's lie, the quartermaster who saw or the deferral is missing, or the straw's egg reaches Devarra's count.");
        var burnt = strawRuns.Single(r => r.Has(P + "straw.burned"));
        check(!burnt.Has(P + "egg.straw") && !Reaches(burnt, "nidalynn.started") && !Avail(straw, Later(story, burnt, 48)),
            "Trk_Nidalynn_Straw: the egg sent out with the bedding still opens her door, or the page plays again.");
        var strawEgg = strawKept.First(r => !r.Has(P + "quartermaster_knew"));
        check(Avail(stone, Later(story, strawEgg, 13)), "Trk_Nidalynn_Straw: the straw's egg never reaches the hearth.");
        var strawStep = Later(story, After(stone, Later(story, strawEgg, 13), "end", 0).First(), 25);
        check(Avail(widow, strawStep) && Visited(widow, strawStep).Contains("straw") && !Visited(widow, strawStep).Contains("druids")
              && Program.WalkVia(widow, strawStep, "rock", 4).Count > 0 && Program.WalkVia(widow, strawStep, "rock", 4).All(r => r.Has(P + "told_egg"))
              && Program.WalkVia(widow, strawStep, "rock", 1).Count == 0 && Program.WalkVia(widow, strawStep, "rock", 3).Count == 0,
            "Trk_Nidalynn_Straw: the widow tells the straw's Commander about the golems or the vault, or never says she was a druid.");
        check(!Visited(widow, Later(story, World(story, 3, "trickster", "trickster.ever", P + "primed", P + "hearth.grey_stone", P + "egg.vault", "eggs.project", "eggs.druids"), 25)).Contains("straw"),
            "Trk_Nidalynn_Straw: the vault's Commander hears the straw.");
        var strawHearth = Later(story, Program.Walk(widow, strawStep).First(r => r.Has(P + "met")), 25);
        check(Visited(hearth, strawHearth).Contains("why_straw") && !Visited(hearth, strawHearth).Contains("why") && !Visited(hearth, strawHearth).Contains("why_vault")
              && Program.Walk(hearth, strawHearth).Any(r => r.Has(P + "kiln_agreed")),
            "Trk_Nidalynn_Straw: the hearth asks the straw's Commander about the golems or the vault, or never reaches the kiln.");
        var strawLane = Later(story, World(story, 3, "trickster", "trickster.ever", P + "egg.straw", P + "cost.slate", P + "hearth.grey_stone", P + "met", "nidalynn.started", P + "kiln", P + "quartermaster_knew"), 49);
        var strawConfessions = Visited(hatching, strawLane);
        check(strawConfessions.Contains("confess_straw") && !strawConfessions.Contains("confess") && !strawConfessions.Contains("confess_vault")
              && strawConfessions.Contains("quartermaster") && !strawConfessions.Contains("clerk")
              && Program.Walk(hatching, strawLane).Any(r => r.Has(P + "confessed") && r.Has(P + "hatched")),
            "Trk_Nidalynn_Straw: the lane hears the wrong confession, or the quartermaster who saw keeps quiet.");
        check(!Visited(hatching, lane).Contains("quartermaster") && !Visited(hatching, lane).Contains("confess_straw"),
            "Trk_Nidalynn_Straw: the golems' Commander hears the quartermaster or confesses the straw.");
        var strawWhose = Later(story, World(story, 3, "trickster", "trickster.ever", P + "egg.straw", P + "met", "nidalynn.started", P + "confessed", P + "hatched"), 25);
        check(Visited(whose, strawWhose).Contains("whose_straw") && !Visited(whose, strawWhose).Contains("whose")
              && Program.WalkVia(whose, strawWhose, "choose", 2).Count == 0 && Program.WalkVia(whose, strawWhose, "choose", 3).All(r => r.Has(P + "claimed"))
              && Program.WalkVia(whose, strawWhose, "choose", 3).Count > 0 && !Visited(whose, Later(story, confessed, 25)).Contains("whose_straw"),
            "Trk_Nidalynn_Straw: whose she is says the straw's Commander stole her, or the others hear the straw.");
        check(Reaches(strawEgg, Committed) && Reaches(strawKept.First(r => r.Has(P + "quartermaster_knew")), Committed),
            "Trk_Nidalynn_Straw: no road to the commit from the straw.");

        // PP10 (Sol COX): the grey dragon's bill on her page agrees with Devarra's Last Call coda: standing, or named at the rift.
        var saltNode = S(P + "epilogue.salt").Nodes.Last();
        var billWorld = World(story, 6, "trickster", "trickster.ever", Committed, Bill);
        var calledWorld = World(story, 6, "trickster", "trickster.ever", Committed, Bill, "devarra.lastcall.called");
        check(Rules.VisibleParagraphs(saltNode, billWorld).Any(t => t.Text.Contains("never paid"))
              && !Rules.VisibleParagraphs(saltNode, billWorld).Any(t => t.Text.Contains("named her bill"))
              && Rules.VisibleParagraphs(saltNode, calledWorld).Any(t => t.Text.Contains("named her bill"))
              && !Rules.VisibleParagraphs(saltNode, calledWorld).Any(t => t.Text.Contains("never paid")),
            "Trk_Nidalynn_Bill: her page says the bill was never paid after Devarra named it at the rift.");

        // Polish (audit INT/BEL/HOW, Trk_Nidalynn_Endings): every ending rendered whole, the page and its visible paragraphs in
        // order, from walked routes. The grey dragon's bill is recorded once wherever it exists; the kiln kept warm, the bowl
        // and the names taught at night belong to the living partner's page alone; a departure says nothing about anyone else.
        string Render(Scene page, Snapshot w) => string.Join("\n", new[] { page.Nodes[0].Text }.Concat(Rules.VisibleParagraphs(page.Nodes[0], w).Select(x => x.Text)));
        int Count(string text, string needle) { int n = 0, at = 0; while ((at = text.IndexOf(needle, at, StringComparison.Ordinal)) >= 0) { n++; at += needle.Length; } return n; }
        Snapshot With(Snapshot s, params string[] flags) { var c = Program.Copy(s); c.Flags.UnionWith(flags); foreach (var context in flags.Where(story.Derived.ContainsKey)) HouseholdTests.Earn(story, c, context); return Later(story, c, 1); }
        string[] Shown(Snapshot w) => pages.Where(pg => Avail(pg, w)).Select(pg => pg.Id.Substring((P + "epilogue.").Length)).OrderBy(x => x, StringComparer.Ordinal).ToArray();
        const string Called = "devarra.lastcall.called";
        const string Standing = "never paid", Named = "named her bill", Windowsill = "windowsill", Bowl = "Eat first", Banked = "banked high", Taught = "taught the Commander";
        var endPage = new Func<string, Scene>(id => S(P + "epilogue." + id));
        // The walk: the confession, Devarra's bill on her own hub, the claim given up, her face, the kiss, then the salt.
        var dvBack = Later(story, With(confessed, "devarra.trickster.returned", "devarra.started"), 25);
        check(Avail(smallest, dvBack), "Trk_Nidalynn_Endings: Devarra's bill cannot be walked from the confession.");
        var billed = Program.Walk(smallest, dvBack).First(r => r.Has(Bill));
        var bGiven = After(whose, Later(story, billed, 25), "choose", 0).First();
        var bFaced = After(form, Later(story, bGiven, 25), "end", 0).First();
        var bKissed = After(wings, Later(story, bFaced, 25), "almost", 0).First();
        var bAsk = Later(story, bKissed, 49, 5);
        var bRejected = After(flight, bAsk, "offer", 2).First();
        var bYes = After(flight, bAsk, "offer", 0).First();
        var bNotYet = After(flight, bAsk, "offer", 1).First();
        var plainRejected = After(flight, Later(story, kissed, 49, 5), "offer", 2).First();
        check(bRejected.Has(Closed) && bRejected.Has(Bill) && bYes.Has(Committed) && bYes.Has(Bill) && !plainRejected.Has(Bill),
            "Trk_Nidalynn_Endings: the walked rejection, yes or no-bill states are wrong.");
        Snapshot End(Snapshot s, params string[] extra) => With(Later(story, s, 200, 6), extra);

        // Rejected after the bill: the departure page alone; the record once, standing or named; no fire kept, nobody's welcome.
        foreach (var (state, called) in new[] { (bRejected, false), (bRejected, true) })
        {
            var w = called ? End(state, Called) : End(state);
            var text = Render(endPage("apart"), w);
            check(Shown(w).SequenceEqual(new[] { "apart" }) && Count(text, called ? Named : Standing) == 1 && Count(text, called ? Standing : Named) == 0
                  && !text.Contains(Banked) && !text.Contains(Bowl) && !text.Contains(Windowsill) && !text.Contains(Taught)
                  && !text.Contains("alone") && !text.Contains("Nobody in Drezen"),
                "Trk_Nidalynn_Endings: the rejected Commander's ending keeps her fire, doubles the bill or speaks for other partners (called=" + called + "): " + text);
            // A concurrent romance changes nothing on her page.
            check(Render(endPage("apart"), With(w, "irabeth.committed", "irabeth.started")) == text,
                "Trk_Nidalynn_Endings: another partner changes the rejected ending.");
        }
        var plainApart = Render(endPage("apart"), End(plainRejected, Called));
        check(!plainApart.Contains(Standing) && !plainApart.Contains(Named), "Trk_Nidalynn_Endings: a bill nobody wrote appears on the departure.");

        // Committed after the bill: her page; standing = the windowsill, named = the record and the bowl; nothing doubled.
        var saltStanding = Render(endPage("salt"), End(bYes));
        var saltNamed = Render(endPage("salt"), End(bYes, Called));
        check(Shown(End(bYes, Called)).SequenceEqual(new[] { "salt" })
              && Count(saltStanding, Standing) == 1 && saltStanding.Contains(Windowsill) && !saltStanding.Contains(Named) && !saltStanding.Contains(Bowl)
              && Count(saltNamed, Named) == 1 && saltNamed.Contains(Bowl) && saltNamed.Contains(Banked) && !saltNamed.Contains(Standing)
              && !Render(endPage("salt"), End(yes, Called)).Contains(Named),
            "Trk_Nidalynn_Endings: her own page records the bill wrongly.");
        // Returned from the sacrifice: the same living page; not returned: the unreturned page, with no nights and no bowl.
        var cameBack = End(bYes, Called, "sacrifice", "trickster.commander_back", P + "wake.name_said");
        var lost = End(bYes, Called, "sacrifice", P + "wake.name_said");
        var lostText = Render(endPage("unreturned"), lost);
        check(Shown(cameBack).SequenceEqual(new[] { "salt" }) && Render(endPage("salt"), cameBack).Contains(Bowl) && Render(endPage("salt"), cameBack).Contains(Taught)
              && Shown(lost).SequenceEqual(new[] { "unreturned" }) && Count(lostText, Named) == 1
              && !lostText.Contains(Bowl) && !lostText.Contains(Banked + " every winter the Commander was away") && !lostText.Contains(Taught) && !lostText.Contains(Windowsill),
            "Trk_Nidalynn_Endings: a Commander who did not come back is fed, taught or visited on the windowsill: " + lostText);
        check(!Render(endPage("unreturned"), End(bYes, "sacrifice")).Contains(Windowsill) && Count(Render(endPage("unreturned"), End(bYes, "sacrifice")), Standing) == 1,
            "Trk_Nidalynn_Endings: the standing bill is not recorded plainly for the Commander who did not come back.");
        // Not yet (the heel): the courtship page; the record once, no domestic payoff.
        var heelText = Render(endPage("heel"), End(bNotYet, Called));
        check(Shown(End(bNotYet, Called)).SequenceEqual(new[] { "heel" }) && Count(heelText, Named) == 1 && !heelText.Contains(Bowl) && !heelText.Contains(Taught),
            "Trk_Nidalynn_Endings: the heel's ending takes the partner's payoff.");
        // The claim kept to her flight, and the lie kept: departures; the record when the flags hold it, never her fire.
        var leftWith = After(claimedFlight, Later(story, keptClaim, 49, 5), "go", 0).First();
        foreach (var (id, state) in new[] { ("claimed", leftWith), ("lie", kept) })
            foreach (var extra in new[] { new string[0], new[] { Bill }, new[] { Bill, Called }, new[] { Bill, Called, Committed, P + "wake.name_said" } })
            {
                var w = End(state, extra);
                var text = Render(endPage(id), w);
                check(Avail(endPage(id), w) && !Shown(w).Contains("salt") && !text.Contains(Bowl) && !text.Contains(Banked) && !text.Contains(Windowsill) && !text.Contains(Taught)
                      && Count(text, Named) == (extra.Contains(Called) ? 1 : 0) && Count(text, Standing) == (extra.Contains(Bill) && !extra.Contains(Called) ? 1 : 0),
                    "Trk_Nidalynn_Endings: the " + id + " departure keeps her fire or loses the record: " + string.Join(",", extra));
            }
        // The wolves and the fire: closures with no shared paragraphs, even with the commit and the wake still held.
        var wolvesWorld = End(World(story, 6, "trickster", "trickster.ever", P + "met", Committed, P + "goat.lie_kept", Closed, P + "wake.name_said", Bill, Called));
        var givenWorld = End(burned, Bill, Called);
        check(Avail(endPage("wolves"), wolvesWorld) && !Shown(wolvesWorld).Contains("salt") && endPage("wolves").Nodes[0].Paragraphs.Count == 0
              && Avail(endPage("given"), givenWorld) && !Shown(givenWorld).Contains("salt") && endPage("given").Nodes[0].Paragraphs.Count == 0,
            "Trk_Nidalynn_Endings: the wolves or the fire ending carries conditional paragraphs or sits beside her page.");

        // NM1 (coordinator ruling; ledger 2/0/1, her Chapter 4 letter stands): her visits are entries on her own step. At a rest
        // only the device event and the grey stone (Chapter 3), the kiln letter (Chapter 4) and her welcome home (Chapter 5).
        var restIds = mine.Where(Rules.IsMailbagLetter).Select(s => s.Id).OrderBy(x => x, StringComparer.Ordinal).ToArray();
        check(restIds.SequenceEqual(new[] { P + "door.home_from_the_dark", P + "eggs.straw", P + "eggs.vault", P + "hearth.grey_stone", P + "letter.from_the_kiln" }),
            "Trk_Nidalynn_Allocation: a visit still arrives at a rest: " + string.Join(", ", restIds));
        // The entry (the device event, then the grey stone) is two deliveries in whichever chapter it falls; after it, Chapter 5
        // has only her welcome home.
        var entry = new[] { P + "eggs.vault", P + "eggs.straw", P + "hearth.grey_stone" };
        check(mine.Where(s => Rules.IsMailbagLetter(s) && s.Chapters.Contains(5) && !entry.Contains(s.Id)).Select(s => s.Id).SequenceEqual(new[] { P + "door.home_from_the_dark" })
              && mine.Where(s => Rules.IsMailbagLetter(s) && s.Chapters.Contains(3) && !entry.Contains(s.Id)).Count() == 0,
            "Trk_Nidalynn_Allocation: a courtship visit is still a rest delivery in Chapter 3 or 5.");
        foreach (var id in new[] { "hearth.listening", "kiln.fire", "kiln.hatching", "kiln.whose", "door.own_form", "wall.wings", "ridge.first_flight",
                                   "ridge.snowfield", "after.first_demon", "kiln.the_heel", "ridge.claimed_flight" })
        {
            var movedStep = S(P + id);
            check(!Rules.IsRemote(movedStep) && movedStep.InteractionHub != null && !string.IsNullOrWhiteSpace(movedStep.Entry) && movedStep.Areas.SequenceEqual(new[] { Drezen }),
                "Trk_Nidalynn_Allocation: a visit is not on her step: " + id);
        }
        foreach (var id in new[] { "kiln.feeding", "kiln.the_druids", "kiln.the_goat", "kiln.in_charge" })
        {
            var widowStep = S(P + id);
            var chosenStep = S(P + id + ".chosen");
            check(widowStep.InteractionHub == "nidalynn.presence" && widowStep.Forbids.Contains(P + "form_chosen") && widowStep.Forbids.Contains(chosenStep.Id)
                  && chosenStep.InteractionHub == "nidalynn.presence.chosen" && chosenStep.Requires.Contains(P + "form_chosen") && chosenStep.Forbids.Contains(widowStep.Id)
                  && chosenStep.ContactUnit == ChosenUnit && widowStep.Nodes.Count == chosenStep.Nodes.Count,
                "Trk_Nidalynn_Allocation: a visit either side of her reveal has no step on both sides: " + id);
        }
        check(S(P + "wall.wings").InteractionHub == "nidalynn.presence.chosen" && S(P + "door.own_form").InteractionHub == "nidalynn.presence"
              && S(P + "ridge.claimed_flight").InteractionHub == "nidalynn.presence",
            "Trk_Nidalynn_Allocation: a visit stands on the wrong body's step.");

        // Polish (coordinator, Trk_Nidalynn_EggOwed): every way the Commander keeps the twelfth egg sets the debt at once, so
        // Devarra can count it on her return; only Devarra's own scene names the bill.
        foreach (var taken in new[] { clean, carried.First(r => r.Has(P + "primed")), strawEgg })
            check(taken.Has(P + "egg_owed") && !taken.Has(Bill), "Trk_Nidalynn_EggOwed: a kept egg does not owe Devarra at once, or names her bill.");
        check(!burnt.Has(P + "egg_owed") && !mine.Concat(own).SelectMany(s => s.Nodes).SelectMany(n => n.Choices).Any(c => c.Set.Contains(Bill)),
            "Trk_Nidalynn_EggOwed: the egg sent out with the bedding still owes, or a Nidalynn scene names Devarra's bill.");

        // Polish r3 (audit INT/BEL/HOW, Trk_Nidalynn_Closures): the wolves closure walked before and after the commit gives the
        // wolves page alone, and after it her Last Call shout goes unanswered (the debt resolved, never called).
        var goatW = S(P + "kiln.the_goat");
        var goatC = S(P + "kiln.the_goat.chosen");
        var callIn = S("nidalynn.lastcall.call");
        var preGoat = Later(story, given, 49);
        check(Avail(goatW, preGoat) && !Avail(goatW, Later(story, plainRejected, 49)) && !Avail(goatC, Later(story, plainRejected, 49)),
            "Trk_Nidalynn_Closures: the goat does not play before the commit, or plays after she has already gone.");
        var preStands = Program.WalkVia(goatW, preGoat, "after_wolves", 2);
        var postGoat = Later(story, yes, 49);
        check(Avail(goatC, postGoat), "Trk_Nidalynn_Closures: the goat does not play after the commit.");
        var postStands = Program.WalkVia(goatC, postGoat, "after_wolves", 2);
        check(preStands.Count > 0 && postStands.Count > 0 && preStands.Concat(postStands).All(r => r.Has(Closed) && r.Has(P + "goat.lie_kept")),
            "Trk_Nidalynn_Closures: keeping the wolves story does not close her.");
        foreach (var r in preStands.Concat(postStands))
        {
            var w = End(r, Bill, Called);
            check(Shown(w).SequenceEqual(new[] { "wolves" }) && !Render(endPage("wolves"), w).Contains("white-haired"),
                "Trk_Nidalynn_Closures: the wolves closure gets more than its own page: " + string.Join(", ", Shown(w)));
        }
        check(!Avail(callIn, End(preStands.First())), "Trk_Nidalynn_Closures: a Commander who never ate the salt is offered her call-in.");
        var callAfter = Program.Walk(callIn, End(postStands.First()));
        var callKept = Program.Walk(callIn, End(yes));
        check(callAfter.Count > 0 && callAfter.All(r => !r.Has("nidalynn.lastcall.called") && r.Has("nidalynn.lastcall.resolved"))
              && callKept.Count > 0 && callKept.All(r => r.Has("nidalynn.lastcall.called")),
            "Trk_Nidalynn_Closures: her shout is answered after she left over the wolves, or not answered while she stays.");
        // Exclusivity over every closure combination the route can hold (each closure flag comes with nidalynn.closed).
        var closureFlags = new[] { Committed, P + "kissed", P + "bread_kept", P + "left_with_it", P + "lie_kept", P + "given_to_the_crowd", P + "goat.lie_kept", "sacrifice", "trickster.commander_back" };
        for (int mask = 0; mask < (1 << closureFlags.Length); mask++)
        {
            var held = closureFlags.Where((f, i) => (mask & (1 << i)) != 0).ToList();
            if (held.Contains("trickster.commander_back") && !held.Contains("sacrifice")) continue;
            var closes = held.Any(f => f == P + "left_with_it" || f == P + "lie_kept" || f == P + "given_to_the_crowd" || f == P + "goat.lie_kept");
            foreach (var closed in closes ? new[] { true } : new[] { false, true })
            {
                var flags = new List<string> { "trickster.ever", P + "met" };
                flags.AddRange(held);
                if (closed) flags.Add(Closed);
                var w = World(story, 6, flags.ToArray());
                check(Shown(w).Length <= 1, "Trk_Nidalynn_Closures: two endings at once: " + string.Join(", ", Shown(w)) + " for " + string.Join(", ", flags));
            }
        }

        // Polish r2 (audit COX, Trk_Nidalynn_LateStart): a Commander who takes the egg in Chapter 5 gets one rest delivery in
        // Chapter 5, worst branch: the vault or the straw page folds the grey stone's nights in; the welcome home never plays.
        foreach (var (late, entryWorld) in new[] {
            (vault, World(story, 5, "trickster", "trickster.ever", "irabeth.chapter_five", "eggs.seen", "eggs.project")),
            (straw, World(story, 5, "trickster", "trickster.ever", "irabeth.chapter_five", "eggs.seen", "eggs.project", "eggs.druids")) })
        {
            var start = Later(story, entryWorld, 25);
            check(Avail(late, start), "Trk_Nidalynn_LateStart: no Chapter 5 door: " + late.Id);
            var kept5 = Program.Walk(late, start).Where(r => r.Has(P + "primed") || r.Has(P + "egg.straw")).ToList();
            check(kept5.Count > 0 && kept5.All(r => r.Has(P + "hearth.grey_stone")) && Visited(late, start).Contains("nights"),
                "Trk_Nidalynn_LateStart: the Chapter 5 page does not fold the grey stone in: " + late.Id);
            // Walk every Nidalynn scene forward through Chapter 5 and count what arrives at a rest.
            var delivered = new HashSet<string> { late.Id };
            var frontier = kept5.Take(2).ToList();
            var seenStates = new HashSet<string>();
            for (int depth = 0; depth < 16 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    var w = Later(story, from, 200, 5);
                    foreach (var s in mine.Where(x => !x.Owner.EndsWith("Epilogue", StringComparison.Ordinal) && Avail(x, w)))
                    {
                        if (Rules.IsMailbagLetter(s)) delivered.Add(s.Id);
                        foreach (var r in Program.Walk(s, w).Take(3))
                            if (seenStates.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                    }
                }
                frontier = next.Take(60).ToList();
            }
            check(delivered.SequenceEqual(new[] { late.Id }),
                "Trk_Nidalynn_LateStart: a Chapter 5 start gets more than one rest delivery: " + string.Join(", ", delivered));
        }
        check(Ch(vault, "carry", 0).Forbids.Contains("irabeth.chapter_five") && Ch(straw, "carry", 0).Forbids.Contains("irabeth.chapter_five")
              && Ch(vault, "carry", 0).Set.Take(3).SequenceEqual(new[] { P + "primed", P + "egg.vault", P + "cost.palms" }),
            "Trk_Nidalynn_LateStart: the Chapter 3 ending of the vault or the straw changed.");

        // Polish r2 (audit BEL): the chosen-form twins never speak the widow's costume in the present tense.
        foreach (var twin in mine.Where(s => s.Id.EndsWith(".chosen", StringComparison.Ordinal)))
            check(!twin.Nodes.Any(n => n.Text.Contains("I wear a belly")) , "Trk_Nidalynn_Twins: her own face still wears the widow's belly: " + twin.Id);
        check(S(P + "kiln.the_goat").Nodes.Single(n => n.Id == "after_wolves").Text.Contains("I wear a belly")
              && S(P + "kiln.the_goat.chosen").Nodes.Single(n => n.Id == "after_wolves").Text.Contains("I wore a belly"),
            "Trk_Nidalynn_Twins: the goat's twins say the wrong thing about the costume.");

        // Every page beat opens from its own gates.
        foreach (var s in own.Where(x => Rules.IsRemote(x) && !x.TricksterDevice))
        {
            var needs = s.Requires.Concat(s.RequiresAnyGroups.Select(g => g[0])).ToArray();
            var w = World(story, s.Chapters[0], new[] { "trickster", "trickster.ever", P + "primed", P + "met", "nidalynn.started" }.Concat(needs).ToArray());
            check(Avail(s, Later(story, w, s.DelayHours + 1)), "A Nidalynn page never opens: " + s.Id);
        }
        Console.WriteLine("PASS: Nidalynn Trickster (Trk_Nidalynn_*): the golems' count, the vault and the druids' straw, the widow and her own face, the kiln, "
            + "the crowd (confess, lie, burn), the claim, the salt and the heel, the snowfield, Devarra's bill, "
            + reactions.Length + " reactions and " + pages.Length + " pages.");
    }
}
