using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Dorgelinda Stranglehold, Trickster (Writer/handoffs/trickster/dorgelinda-stranglehold.md; F16): "Nothing's missing".
// One block per spec rules test (Trk_Dorgelinda_*), the shape of each hook, and the weekly counts that make the audit a
// courtship (dorgelinda_ledger): every beat reachable on its own path, the intimate night only after the commit.
internal static class DorgelindaTricksterTests
{
    private const string Unit = "8692bff6041c47a0b13158d5977f291b";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Hub = "fa57cf97ea01bf34e9a30f6ad444381e";
    private const string P = "dorgelinda.trickster.";
    private const string L = "dorgelinda.ledger.";

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
        foreach (var context in flags.Where(story.Derived.ContainsKey))
            HouseholdTests.Earn(story, state, context);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add(Unit);
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later);
        return later;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var countersign = S(P + "caravans.countersign");
        var recount = S(P + "tribunal.recount");
        var stocktake = S(P + "office.stocktake");
        var open = S(P + "audit.open");
        var weekly = S(P + "after.weekly_count");
        var methods = S(P + "after.fellows_methods");
        var commit = S(P + "after.commit");
        var secondAsk = S(P + "after.second_ask");
        var pages = story.Scenes.Where(s => s.Relationship == "dorgelinda" && s.Owner == "DorgelindaEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "dorgelinda" && s.Reaction).ToArray();
        var own = story.Scenes.Where(s => s.Relationship == "dorgelinda" && !s.Reaction && s.Owner == "Dorgelinda").ToArray();
        var ledger = own.Where(s => s.Id.StartsWith(L, StringComparison.Ordinal)).ToArray();
        bool Any(Snapshot w, params Scene[] scenes) => scenes.Any(s => Rules.Available(story, s, w));
        List<Snapshot> Play(Scene scene, Snapshot w) => Program.Walk(scene, w).Where(r => r.Has(scene.Id)).ToList();
        Snapshot Pick(Scene scene, Snapshot w, params string[] flags)
        {
            var hit = Play(scene, w).Where(r => flags.All(r.Has))
                .OrderBy(r => !flags.Contains("dorgelinda.closed") && r.Has("dorgelinda.closed") ? 1 : 0).FirstOrDefault();
            check(hit != null, "No outcome of " + scene.Id + " sets " + string.Join(", ", flags));
            return hit ?? w;
        }
        Choice Choice(Scene scene, string node, int index) => scene.Nodes.Single(n => n.Id == node).Choices[index];
        // The outcomes of a walk that took the named choice of the named node.
        List<Snapshot> After(Scene scene, Snapshot w, string node, int index)
        {
            // Q9 (Sol HOW): only the outcomes of paths that actually take the named choice.
            var hits = Program.WalkVia(scene, w, node, index);
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        // Plays every available Dorgelinda scene forward and reports whether a flag is ever held.
        using var reachability = new ReachabilityCache();
        bool Reaches(Snapshot start, string flag, int chapter = 5)
            => reachability.Reaches(start, flag, chapter, () => Explore(Program.Copy(start), chapter));
        IEnumerable<Snapshot> Explore(Snapshot start, int chapter)
        {
            var seen = new HashSet<string>();
            var frontier = new List<Snapshot> { start };
            for (int depth = 0; depth < 12 && frontier.Count > 0; depth++)
            {
                var next = new List<Snapshot>();
                foreach (var from in frontier)
                {
                    yield return from;
                    var w = Later(story, from, 100, chapter);
                    foreach (var scene in own.Where(s => Rules.Available(story, s, w)))
                        foreach (var r in Program.Walk(scene, w))
                        {
                            yield return r;
                            if (seen.Add(string.Join(",", r.Flags.OrderBy(f => f)))) next.Add(r);
                        }
                }
                frontier = next;
            }
        }

        // Shape and hooks.
        var rel = story.Relationships["dorgelinda"];
        check(rel.StartedFlag == "dorgelinda.started" && rel.ClosedFlag == "dorgelinda.closed" && rel.CommittedFlag == "dorgelinda.committed"
              && rel.UnavailableFlags.SequenceEqual(new[] { "swarm" }) && rel.UnavailableOverrides.Count == 0
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "dorgelinda.caravans_known", "dorgelinda.fellows_tribunal", "dorgelinda.present" }),
            "Dorgelinda's relationship does not match the spec.");
        check(countersign.AnswerLists.SequenceEqual(new[] { "1f5aae1aab3b5b34ea3a0cbb1d0ca0b9" })
              && countersign.NativeReturnCue == "3de8c946e5e8fca46bfd39dfd4f9aa61" && countersign.ContactUnit == null
              && countersign.Chapters.SequenceEqual(new[] { 3 }) && countersign.EntryMythic == "PlayerIsTrickster"
              && countersign.EntryAlignment?.Direction == "Chaotic" && countersign.Forbids.Contains("dorgelinda.fellows_tribunal"),
            "The countersign is not an inline Trickster answer on the Logistics_4 verdict list, before the tribunal.");
        check(recount.AnswerLists.SequenceEqual(new[] { "cba15a10b7929e44ca32745529948d0c" })
              && recount.NativeReturnCue == "647f755c8107d404a9ed894923d1d732" && recount.ContactUnit == null
              && recount.Chapters.SequenceEqual(new[] { 3 }) && recount.EntryMythic == "PlayerIsTrickster",
            "The recount is not an inline preface on the Logistics_5 verdict list (Chapter 3).");
        check(recount.Nodes.Single(n => n.Id == "count").Choices.Count == 2
              && Choice(recount, "count", 0).Requires.Contains(P + "cost.carts_signed")
              && Choice(recount, "count", 1).Forbids.Contains(P + "cost.carts_signed"),
            "The recount's dispatch node does not split on the rider.");
        foreach (var index in new[] { 0, 1 })
            check(Choice(recount, "audit", index).Crusade?.Resource == "Materials" && Choice(recount, "audit", index).Crusade!.Amount == -200,
                "The warehouse written off is not paid for in Materials: audit/" + index);
        check(Choice(stocktake, "sign", 0).Crusade?.Resource == "Materials" && Choice(stocktake, "sign", 0).Crusade!.Amount == -100
              && stocktake.Chapters.SequenceEqual(new[] { 5 }) && stocktake.EntryMythic == "PlayerIsTrickster",
            "The stocktake is not the Chapter 5 Trickster signature with its frozen column.");
        // PP5: the Chapter 4 crate (cold_iron_and_wool) is the one page read away from her desk; its own block checks its shape.
        foreach (var s in own.Where(s => s != countersign && s != recount && s.Id != L + "cold_iron_and_wool"))
            check(s.AnswerLists.SequenceEqual(new[] { Hub }) && s.ContactUnit == Unit && s.Areas.SequenceEqual(new[] { Drezen })
                  && !Rules.IsRemote(s) && s.Forbids.Contains("dorgelinda.closed"),
                "A Dorgelinda scene is not at her own desk in Drezen: " + s.Id);
        foreach (var s in story.Scenes.Where(s => s.Relationship == "dorgelinda"))
        {
            check(!s.Requires.Contains("swarm") && !s.TricksterDevice, "A Dorgelinda scene serves the swarm: " + s.Id);
            foreach (var key in s.Requires.Concat(s.RequiresAnyGroups.SelectMany(g => g)))
                check(!key.EndsWith(".dead", StringComparison.Ordinal) && !key.EndsWith("_dead", StringComparison.Ordinal)
                      && !key.EndsWith(".closed", StringComparison.Ordinal) || key == "dorgelinda.closed",
                    "Dorgelinda needs someone dead or closed: " + s.Id + " " + key);
        }
        var dirty = Choice(methods, "dirty", 0);
        check(dirty.Crusade?.Resource == "Materials" && dirty.Crusade.Amount == 150 && dirty.Alignment?.Direction == "Evil",
            "Keeping the Fellows' book neither pays nor stains.");
        check(Choice(commit, "yes_boots", 0).Crusade?.Amount == -200 && Choice(secondAsk, "price", 0).Crusade?.Amount == -100,
            "The boots or the full accounting are free.");
        check(reactions.Length == 8 && reactions.All(r => r.Nodes.Count == 1)
              && reactions.Where(r => r.Owner == "Lann").All(r => r.Requires.Contains("lann.in_party") && r.Forbids.Contains("lann.dead"))
              && reactions.Where(r => r.Owner == "Regill").All(r => r.Requires.Contains("regill.in_party") && r.Forbids.Contains("regill.dead"))
              && reactions.Where(r => r.Owner == "Konomi").All(r => r.Requires.Contains("konomi.in_office")
                  && r.ForbidOverrides["konomi.dismissed"] == "konomi.trickster.returned"),
            "The reactions are not exactly Konomi, Regill and Lann behind their guards.");
        check(pages.Length == 6 && pages.All(p => p.MinChapter == 6 && p.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.Crusade == null))),
            "The epilogue pages carry effects or are missing.");
        // eng7-l13: preparation also requires the live outcome contract.
        check(story.Derived["dorgelinda.trickster.late_committed"].Single().SequenceEqual(new[] { "trickster.ever", P + "methods_heard", "dorgelinda.outcome.route_open", "dorgelinda.trickster.late_committed.without.dorgelinda.trickster.declined", "dorgelinda.outcome.accepted" }),
            "The late entitlement lacks her explicit acceptance.");

        // Trk_Dorgelinda_Countersign: the rider, signed at the caravan council, before the tribunal.
        var caravans = World(story, 3, "trickster", "dorgelinda.caravans_known");
        check(Rules.Available(story, countersign, caravans) && !Rules.Available(story, recount, caravans),
            "Trk_Dorgelinda_Countersign: the countersign is shut, or the recount opens early.");
        var signed = After(countersign, caravans, "rider", 0).First();
        check(signed.Has(P + "cost.carts_signed") && countersign.EntryAlignment?.Value == 1,
            "Trk_Dorgelinda_Countersign: the rider is not written, or the entry does not shift Chaotic.");
        var tribunal = Later(story, signed, 24);
        tribunal.Flags.UnionWith(new[] { "dorgelinda.fellows_tribunal", "dorgelinda.present" });
        check(Rules.Available(story, recount, tribunal) && !Rules.Available(story, countersign, tribunal),
            "Trk_Dorgelinda_Countersign: the recount does not follow the rider.");
        check(Play(countersign, caravans).Any(r => !r.Has(P + "cost.carts_signed")), "The pen cannot be handed back.");
        check(Reaches(signed, "dorgelinda.committed", 3) || Reaches(Pick(recount, tribunal, P + "primed"), "dorgelinda.committed"),
            "Trk_Dorgelinda_Countersign: no road from the rider to the commit.");

        // Trk_Dorgelinda_Prepared: the rider read at the tribunal.
        var prepared = World(story, 3, "trickster", "dorgelinda.fellows_tribunal", "dorgelinda.present", P + "cost.carts_signed");
        var prep = After(recount, prepared, "audit", 0).First();
        check(prep.Has(P + "primed") && prep.Has(P + "cost.audit") && !prep.Has(P + "cost.late"),
            "Trk_Dorgelinda_Prepared: the prepared recount reads as late.");
        check(Rules.Available(story, open, Later(story, prep, 48)), "Trk_Dorgelinda_Prepared: the audit does not open 48 h later.");
        check(!Rules.Available(story, open, Later(story, prep, 24)), "The audit opens before two days have passed.");
        check(Reaches(prep, "dorgelinda.committed"), "Trk_Dorgelinda_Prepared: no road to the commit.");

        // Trk_Dorgelinda_Tribunal: the late line, ink wet, witnessed.
        var late = World(story, 3, "trickster", "dorgelinda.fellows_tribunal", "dorgelinda.present");
        var wet = After(recount, late, "audit", 1).First();
        check(wet.Has(P + "primed") && wet.Has(P + "cost.audit") && wet.Has(P + "cost.late") && !wet.Has(P + "cost.carts_signed"),
            "Trk_Dorgelinda_Tribunal: the late line does not cost the late terms.");
        check(Rules.Available(story, open, Later(story, wet, 48)), "Trk_Dorgelinda_Tribunal: no audit after the wet ink.");
        check(Play(open, Later(story, wet, 48)).Where(r => r.Has(P + "returned")).All(r => r.Has(P + "cost.twice_weekly")),
            "Wet ink does not cost twice-weekly audits.");
        check(Reaches(wet, "dorgelinda.committed"), "Trk_Dorgelinda_Tribunal: no road to the commit.");

        // Trk_Dorgelinda_Return: the audit opens; the commit is not in the return scene.
        var primed = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "primed");
        var back = After(open, primed, "terms", 0).First();
        check(back.Has(P + "returned") && back.Has("dorgelinda.started") && !back.Has("dorgelinda.committed"),
            "Trk_Dorgelinda_Return: the audit does not return her, or commits.");
        check(open.Nodes.SelectMany(n => n.Choices).All(c => !c.Set.Contains("dorgelinda.committed")), "The return scene commits.");
        var afterBack = Later(story, back, 48);
        check(Rules.Available(story, weekly, afterBack) && !Rules.Available(story, commit, afterBack),
            "Trk_Dorgelinda_Return: the weekly count does not follow, or the commit skips it.");
        check(Play(open, primed).Any(r => r.Has("dorgelinda.closed")), "Silencing her audit is not her hard no.");
        check(Reaches(back, "dorgelinda.committed"), "Trk_Dorgelinda_Return: no road to the commit.");

        // Trk_Dorgelinda_Commit.
        var ready = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", P + "methods_heard", P + "hands_clean");
        check(Rules.Available(story, commit, ready), "Trk_Dorgelinda_Commit: the commit is shut.");
        var yes = After(commit, ready, "yes", 0).First();
        check(yes.Has("dorgelinda.committed") && !yes.Has(P + "declined"), "Trk_Dorgelinda_Commit: yes does not commit.");
        check(Play(commit, ready).Any(r => r.Has(P + "declined") && !r.Has("dorgelinda.committed")),
            "Her 'Not today' is not reachable.");
        var boots = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", P + "methods_heard",
            P + "hands_dirty", P + "cost.boots_owed");
        check(After(commit, boots, "yes_boots", 0).All(r => r.Has(P + "cost.boots_paid")), "The last pair of boots is not paid.");

        // Trk_Dorgelinda_Declined: the priced second ask.
        var declined = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", P + "methods_heard",
            P + "declined", P + "after.commit");
        check(Rules.Available(story, secondAsk, Later(story, declined, 72)) && !Rules.Available(story, commit, declined),
            "Trk_Dorgelinda_Declined: the second ask is shut, or the commit reopens.");
        var told = After(secondAsk, Later(story, declined, 72), "told", 0).First();
        check(told.Has("dorgelinda.committed") && told.Has(P + "cost.told_all"), "Trk_Dorgelinda_Declined: telling all does not commit.");
        check(Play(secondAsk, Later(story, declined, 72)).Any(r => r.Has("dorgelinda.closed")), "Her hard no is not reachable.");

        // Trk_Dorgelinda_Stocktake: no tribunal by Chapter 5.
        var office = World(story, 5, "trickster", "dorgelinda.present");
        check(Rules.Available(story, stocktake, office) && !Rules.Available(story, recount, office),
            "Trk_Dorgelinda_Stocktake: the stocktake is shut, or the recount opens.");
        var abyss = After(stocktake, office, "sign", 0).First();
        check(abyss.Has(P + "primed") && abyss.Has(P + "cost.audit") && abyss.Has(P + "cost.abyss_signed"),
            "Trk_Dorgelinda_Stocktake: the signature does not prime the audit.");
        check(Rules.Available(story, open, Later(story, abyss, 48)), "Trk_Dorgelinda_Stocktake: no audit follows.");
        check(Reaches(abyss, "dorgelinda.committed"), "Trk_Dorgelinda_Stocktake: no road to the commit.");

        // Trk_Dorgelinda_Exclusive.
        var both = World(story, 5, "trickster", "dorgelinda.fellows_tribunal", "dorgelinda.present");
        check(!Rules.Available(story, stocktake, both), "Trk_Dorgelinda_Exclusive: the stocktake opens after a tribunal.");
        check(Rules.Available(story, recount, World(story, 3, "trickster", "dorgelinda.fellows_tribunal", "dorgelinda.present")),
            "Trk_Dorgelinda_Exclusive: the recount is shut at its tribunal.");

        // ENGINE-Q5: even a primed audit completes a new device and needs the live path.
        var failed = World(story, 3, "trickster.ever", "trickster.failed", P + "primed", "dorgelinda.present");
        check(!Any(failed, open, recount, countersign),
            "Trk_Dorgelinda_FailedPath: a device completes without the live path.");
        var failed5 = World(story, 5, "trickster.ever", "trickster.failed", "dorgelinda.present");
        check(!Any(failed5, stocktake, open), "Trk_Dorgelinda_FailedPath_Ch5: a lost path still signs the stocktake.");

        // Trk_Dorgelinda_Silenced: her hard no closes everything of hers and nothing of anyone else's.
        var silenced = World(story, 5, "trickster", "dorgelinda.present", P + "primed", "dorgelinda.closed");
        check(!Any(silenced, open, weekly, commit) && !ledger.Any(s => Rules.Available(story, s, silenced)),
            "Trk_Dorgelinda_Silenced: a closed audit still opens a scene.");
        foreach (var s in story.Scenes.Where(s => s.Relationship != "dorgelinda"))
            check(!s.Requires.Contains("dorgelinda.closed") && !s.Forbids.Contains("dorgelinda.closed") || s.Relationship == "dorgelinda",
                "Another route reads Dorgelinda's closure: " + s.Id);

        // The weekly counts: a courtship between the audit and the commit, each beat on its own path.
        var hand = S(L + "the_hand");
        var grip = S(L + "stranglehold");
        var debts = S(L + "old_debts");
        var council = S(L + "after_the_council");
        var gate = S(L + "the_west_gate");
        var warehouse = S(L + "the_warehouse");
        var bartley = S(L + "the_corporals_account");
        var vrock = S(L + "the_vrocks_driver");
        var receipts = S(L + "receipts");
        var rations = S(L + "half_rations");
        var weight = S(L + "weight_discrepancy");
        var revels = S(L + "the_kings_bill");
        var faith = S(L + "buying_forgiveness");
        var night = S(L + "after_hours");
        var morning = S(L + "morning_count");
        var afterWar = S(L + "after_the_war");
        var inquiry = S(L + "the_inquiry");
        var forward = S(L + "carried_forward");
        var counted3 = World(story, 3, "trickster", "trickster.ever", "dorgelinda.present", "dorgelinda.fellows_tribunal", P + "primed",
            P + "cost.carts_signed", P + "cost.audit", P + "returned", P + "counted");
        check(Rules.Available(story, hand, counted3) && Rules.Available(story, warehouse, counted3) && Rules.Available(story, vrock, counted3),
            "The Chapter 3 weekly counts do not open after the first count.");
        var s3 = counted3;
        foreach (var beat in new[] { hand, grip, debts, council, gate })
        {
            s3 = Later(story, s3, 72);
            check(Rules.Available(story, beat, s3), "The weekly counts break their chain at " + beat.Id);
            s3 = Play(beat, s3).First();
        }
        check(!Rules.Available(story, warehouse, World(story, 3, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", P + "cost.abyss_signed")),
            "Bartley's warehouse opens on a run with no tribunal.");
        check(!Rules.Available(story, vrock, World(story, 3, "trickster", "trickster.ever", "dorgelinda.present", "dorgelinda.fellows_tribunal", P + "returned", P + "counted", P + "cost.late")),
            "The vrock's driver opens without the rider.");
        var wh = Play(warehouse, counted3);
        check(wh.Any(r => r.Has(L + "potions_ours")) && wh.Any(r => r.Has(L + "potions_bartley")), "The potions cannot go either way.");
        check(Rules.Available(story, bartley, Later(story, wh.First(), 72)), "Bartley's account does not follow the warehouse.");
        check(!Rules.Available(story, night, Later(story, counted3, 100, 5)), "The night comes before the commit.");
        var counted5 = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "primed", P + "cost.carts_signed",
            P + "returned", P + "counted");
        check(Rules.Available(story, receipts, counted5) && Rules.Available(story, weight, counted5),
            "The Chapter 5 counts do not open after the Abyss.");
        check(!Rules.Available(story, receipts, World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", P + "cost.abyss_signed")),
            "The Abyss receipts open for a Commander she only met in Chapter 5.");
        check(!Rules.Available(story, revels, counted5)
              && Rules.Available(story, revels, World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", "dorgelinda.merry_city")),
            "The King's bill does not wait for the Trickster's coronation.");
        var fed = Play(rations, Later(story, Play(receipts, counted5).First(), 72));
        check(fed.Count > 0 && Rules.Available(story, faith, Later(story, fed.First(), 72)), "Faith does not follow the rations.");
        var lovers = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", P + "methods_heard", P + "hands_clean",
            "dorgelinda.committed");
        check(Rules.Available(story, night, Later(story, lovers, 12)), "The night does not follow the commit.");
        var nights = Play(night, Later(story, lovers, 12));
        check(nights.All(r => r.Has(L + "night_kept")) && night.Nodes.Any(n => n.Id == "threshold"),
            "The night does not reach its threshold.");
        // Directive 12 on the generated text: the threshold stages desire and the initiating motion, and the cut lands
        // there, on the node's only choice; nothing past the start of the act is narrated.
        var threshold = night.Nodes.Single(n => n.Id == "threshold");
        check(threshold.Choices.Count == 1 && threshold.Choices[0].Next == L + "after_hours.explicit.1"
              && night.Nodes.Single(n => n.Id == L + "after_hours.explicit.1").Choices.Single().Next == null
              && night.Nodes.Single(n => n.Id == L + "after_hours.explicit.1").Choices.Single().Set.Contains(L + "night_kept"),
            "The cut does not land on the threshold.");
        var mornings = Play(morning, Later(story, nights.First(), 6));
        check(mornings.Count > 0 && Rules.Available(story, afterWar, Later(story, mornings.First(), 24))
              && Rules.Available(story, inquiry, Later(story, mornings.First(), 48)),
            "The morning after has no consequences to follow.");
        var inquiries = Play(inquiry, Later(story, mornings.First(), 48));
        check(inquiries.Any(r => r.Has(L + "true_books_sent")) && inquiries.Any(r => r.Has(L + "clean_copy_sent"))
              && inquiries.Any(r => r.Has(L + "her_name_sent")), "The inquiry's three answers are not all reachable.");
        check(Choice(inquiry, "choice", 0).Crusade?.Resource == "Favors" && Choice(inquiry, "choice", 1).Alignment?.Direction == "Chaotic",
            "The inquiry's answers cost nothing.");
        check(Rules.Available(story, forward, Later(story, inquiries.First(), 48)), "The last march does not follow the inquiry.");
        // Her other columns: the Commander's answer decides. Honesty gets her terms, "my business" a colder allowance,
        // a lie her hard no (her cup back, the line ruled off) with its own page.
        var others = S(L + "other_columns");
        var soloColumns = Play(others, Later(story, mornings.First(), 24));
        check(soloColumns.Any(r => r.Has(L + "sole_line")) && !soloColumns.Any(r => r.Has(L + "terms_kept")),
            "A sole lover is made to disclose invented partners.");
        var sharedColumns = Later(story, mornings.First(), 24);
        sharedColumns.Flags.Add(L + "native_arueshalae");
        Rules.Complete(story, sharedColumns);
        var columns = Play(others, sharedColumns);
        check(columns.Any(r => r.Has(L + "terms_kept")) && columns.Any(r => r.Has(L + "unblessed")) && columns.Any(r => r.Has(L + "narrowed") && !r.Has("dorgelinda.closed"))
              && columns.Any(r => r.Has("dorgelinda.closed")), "Her answer to the other columns is not a real choice.");
        // Round 3: generated-story receipts permit successive additions after
        // an initially shared arrangement. Native romances supply actual readers.
        var soloAnswers = others.Nodes.Single(n => n.Id == "says").Choices
            .Where(c => Rules.ChoiceAvailable(c, mornings.First()) && (c.Next == "lie" || c.Next == "nobody")).ToArray();
        check(soloAnswers.Length == 1 && soloAnswers[0].Next == "nobody", "Solo denial is duplicated.");
        var honestShared = columns.First(r => r.Has(L + "terms_kept"));
        check(honestShared.Has(L + "disclosed.arueshalae"), "Initial disclosure has no named receipt.");
        var changed = S(L + "changed_columns");
        var ongoing = changed;
        var addition = Later(story, honestShared, 24);
        addition.Flags.Add("galfrey.romance_active");
        Rules.Complete(story, addition);
        check(Rules.Available(story, changed, addition), "Shared arrangement cannot disclose another lover.");
        var renewed = Program.Walk(changed, addition).First(r => r.Has(L + "disclosed.galfrey"));
        check(!renewed.Has(changed.Id) && !renewed.Has(L + "new_columns"), "First renewal was not recorded accurately.");
        renewed.Flags.Add("camellia.romance");
        Rules.Complete(story, renewed);
        check(Rules.Available(story, ongoing, renewed), "Second addition has no conversation.");
        var again = Program.Walk(ongoing, renewed).First(r => r.Has(L + "disclosed.camellia"));
        check(!again.Has(ongoing.Id) && !again.Has(L + "new_columns"), "Renewal cannot recur or invents an undisclosed lover.");
        again.Flags.Add("wenduag.romance_active");
        Rules.Complete(story, again);
        check(Rules.Available(story, ongoing, again), "Third addition cannot use the continuing conversation.");
        check(Program.Walk(ongoing, again).Any(r => r.Has(L + "disclosed.wenduag")), "Third addition was not disclosed.");

        check(Rules.Available(story, S(P + "epilogue.ruled_off"), World(story, 6, "trickster", "trickster.ever", "dorgelinda.committed", P + "methods_heard", "dorgelinda.closed"))
              && !Rules.Available(story, S(P + "epilogue.committed"), World(story, 6, "trickster", "trickster.ever", "dorgelinda.committed", P + "methods_heard", "dorgelinda.closed")),
            "Her ruled-off line has no page, or the committed page still plays.");
        var committedPage = S(P + "epilogue.committed").Nodes[0];
        foreach (var flag in new[] { L + "true_books_sent", L + "clean_copy_sent", L + "her_name_sent", L + "receipt_signed" })
            check(committedPage.Paragraphs.Any(p => p.Requires.Contains(flag)), "Her epilogue forgets " + flag);

        // Q9 (Sol INT): a tribunal held in Chapter 3 with the injected recount never taken still opens the route in Chapter 5,
        // through her closed tribunal books: a new witnessed signature, late terms; walking away keeps it replayable.
        var books = S(P + "office.tribunal_books");
        var heldTribunal = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", "dorgelinda.fellows_tribunal", "dorgelinda.verdict_prison");
        check(Rules.Available(story, books, heldTribunal) && !Rules.Available(story, stocktake, heldTribunal) && !Rules.Available(story, recount, heldTribunal)
              && books.Chapters.SequenceEqual(new[] { 5 }) && books.EntryMythic == "PlayerIsTrickster",
            "Trk_Dorgelinda_TribunalBooks: a held tribunal without the recount has no Chapter 5 entry.");
        check(!Rules.Available(story, books, World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", "dorgelinda.fellows_tribunal", P + "primed")),
            "Trk_Dorgelinda_TribunalBooks: the tribunal books open after the recount already primed the audit.");
        var reviewed = Program.WalkVia(books, heldTribunal, "sign", 0);
        check(reviewed.Count > 0 && reviewed.All(r => r.Has(P + "primed") && r.Has(P + "cost.late") && r.Has(P + "cost.tribunal_books")),
            "Trk_Dorgelinda_TribunalBooks: the late signature does not prime the audit on late terms.");
        check(Program.WalkVia(books, heldTribunal, "hole", 1).All(r => !r.Has(books.Id) && !r.Has(P + "primed")),
            "Trk_Dorgelinda_TribunalBooks: declining to sign records the scene.");
        var reviewOpen = Later(story, reviewed.First(), 48);
        check(Rules.Available(story, open, reviewOpen) && Program.WalkVia(open, reviewOpen, "start", 6).Count > 0
              && Program.WalkVia(open, reviewOpen, "path", 4).Count > 0
              && Program.Walk(open, reviewOpen, (id, st) => check(!id.StartsWith("verdict_", StringComparison.Ordinal) && id != "path_late",
                  "Trk_Dorgelinda_TribunalBooks: the late signing replays the tribunal's verdict or wet ink: " + id)).Count > 0,
            "Trk_Dorgelinda_TribunalBooks: the audit does not open on its own history.");
        check(Reaches(reviewed.First(), "dorgelinda.committed"), "Trk_Dorgelinda_TribunalBooks: no road to the commit.");

        // Q9 r2 (Sol CAN): a conscience kept at the council (Logistics_8-2, the warehouses refilled) is a surplus-era question.
        var conscienceWorld = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", "dorgelinda.conscience_kept");
        Program.Walk(methods, conscienceWorld, (id, st) => check(id != "start", "The conscience branch replays the shortage pitch."));
        check(Program.WalkVia(methods, conscienceWorld, "start_surplus", 0).All(r => r.Has(P + "hands_clean")),
            "The surplus-era second book cannot be burned.");
        // Q9 r2 (Sol INT): a Commander with nobody else can say so.
        check(Program.WalkVia(others, Later(story, mornings.First(), 24), "says", 4).All(r => r.Has(L + "sole_line") && !r.Has("dorgelinda.closed")),
            "Her other columns force a Commander with nobody else to invent somebody.");

        // Q9 (Sol CAN): the King is billed only when the Fool King was crowned.
        check(Choice(revels, "bill", 1).Requires.Contains("dorgelinda.king_revel"), "The no-King city can bill a King.");
        var merryOnly = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", "dorgelinda.merry_city");
        Program.Walk(revels, merryOnly, (id, st) => check(id != "king" && id != "crowned", "The no-King cellar reaches the King: " + id));

        // Q9 (Sol BEL): the plague ward never thanks the Commander for a rope spared after an execution verdict.
        var ward = S(L + "the_plague_ward");
        check(story.Derived["dorgelinda.verdict_hanged"].Length == 2, "The derived hanging verdict is missing.");
        var hangedWard = World(story, 3, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted", "dorgelinda.fellows_tribunal",
            "dorgelinda.verdict_hanged_wenduag", L + "the_warehouse", L + "potions_ours");
        Program.Walk(ward, hangedWard, (id, st) => check(id != "rope" && id != "wait", "The ward spares a hanged man's rope: " + id));
        check(Program.WalkVia(ward, hangedWard, "outside", 2).Count > 0 && Program.WalkVia(ward, hangedWard, "outside", 3).Count > 0,
            "The hanged ward has no closing words.");

        // Q9 (Sol BEL): walking out of the quarrel stays walked out; the repair is a later, explicit choice.
        var quarrel = S(L + "hammer_and_tongs");
        var coldCounts = S(L + "cold_counts");
        var walked = Program.WalkVia(quarrel, World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", "dorgelinda.committed", L + "other_columns"), "seal", 1);
        check(walked.Count > 0 && walked.All(r => r.Has(L + "quarrel_cold") && !r.Has(L + "quarrel_mended")),
            "Leaving the quarrel still mends it.");
        check(!Rules.Available(story, coldCounts, Later(story, walked.First(), 48)) && Rules.Available(story, coldCounts, Later(story, walked.First(), 168)),
            "The cold counts do not follow the walk-out.");
        var counts = Program.Walk(coldCounts, Later(story, walked.First(), 168));
        check(counts.Any(r => r.Has(L + "quarrel_mended")) && counts.Any(r => r.Has(L + "quarrel_unmended") && !r.Has(L + "quarrel_mended")),
            "The cold counts do not offer both the apology and the standing quarrel.");

        // Q9 (Sol INT): the smaller yes comes after the one morning, and keeps her after-the-war talk to herself.
        check(others.Requires.Contains(L + "morning_count") && !Rules.Available(story, others, Later(story, nights.First(), 24)),
            "Her other columns can come before the morning the smaller yes forbids.");
        var narrowed = World(story, 5, "trickster", "trickster.ever", "dorgelinda.present", "dorgelinda.committed", L + "after_hours", L + "morning_count", L + "narrowed");
        Program.Walk(afterWar, narrowed, (id, st) => check(id != "after" && id != "where", "The smaller yes still tells her after: " + id));

        // Q9 (Sol COX): the bottled-death return keeps her closing page, and the late commit reaches her Last Call coda.
        check(S(P + "epilogue.after_the_war").ForbidOverrides["sacrifice"] == "trickster.commander_back",
            "Her closing page vanishes on the Last Call return.");
        var coda = S("dorgelinda.lastcall.page");
        check(coda.RequiresAnyGroups.Length == 1 && coda.RequiresAnyGroups[0].Contains("dorgelinda.committed")
              && coda.RequiresAnyGroups[0].Contains(P + "late_committed") && coda.Forbids.Contains(P + "declined"),
            "The late commit is missing from her Last Call coda.");

        // PP5 (Chapter 4): cold iron and wool. A crate she packed before the Abyss, opened at the first camp; no courier.
        var wool = S(L + "cold_iron_and_wool");
        check(Rules.IsRemote(wool) && wool.Kind == "letter" && wool.Chapters.SequenceEqual(new[] { 4 }) && wool.MinChapter == 4 && wool.MaxChapter == 4
              && wool.Relationship == "dorgelinda" && wool.Requires.Contains("trickster.ever") && wool.Requires.Contains(P + "counted"),
            "Cold iron and wool lost its shape (a Chapter 4 letter on her counted route).");
        var counted4 = World(story, 4, "trickster", "trickster.ever", P + "returned", P + "counted");
        check(Rules.Available(story, wool, counted4), "Cold iron and wool does not open in the Abyss.");
        foreach (int ch in new[] { 3, 5 })
            check(!Rules.Available(story, wool, World(story, ch, "trickster", "trickster.ever", "dorgelinda.present", P + "returned", P + "counted")),
                "Cold iron and wool opens outside the Abyss: Chapter " + ch);
        check(!Rules.Available(story, wool, World(story, 4, "trickster", "trickster.ever")), "The crate is packed for a Commander she never counted.");
        check(!Rules.Available(story, wool, World(story, 4, "trickster", "trickster.ever", P + "counted", "dorgelinda.closed")), "The crate ignores a closed route.");
        var woolPages = new HashSet<string>();
        var spent = Program.Walk(wool, counted4, (page, _) => woolPages.Add(page)).Where(r => r.Has(wool.Id)).ToList();
        string[] woolWays = { L + "wool_shared", L + "wool_kept", L + "wool_traded" };
        check(spent.Count == 3 && woolWays.All(f => spent.Count(r => r.Has(f)) == 1) && spent.All(r => !Rules.Available(story, wool, Later(story, r, 48))),
            "The wool cannot go three ways, or the crate is opened twice.");
        check(woolPages.Contains("note") && !woolPages.Contains("note_heel"), "The right heel is minded for boots she never fitted.");
        var heelPages = new HashSet<string>();
        Program.Walk(wool, World(story, 4, "trickster", "trickster.ever", P + "returned", P + "counted", L + "fitted"), (page, _) => heelPages.Add(page));
        check(heelPages.Contains("note_heel") && !heelPages.Contains("note"), "The fitted boots lose their heel line.");
        // Chapter 5: receipts reads the wool back, each answer only for its own Commander, appended after the original three.
        var column = receipts.Nodes.Single(n => n.Id == "column").Choices;
        check(column.Count == 6 && column[0].Next == "pack" && column[1].Next == "thought" && column[2].Next == "miss"
              && column.Skip(3).Select(c => c.Requires.Single()).SequenceEqual(woolWays), "The wool's answers were not appended to receipts.");
        foreach (var r in spent)
        {
            var home = Later(story, r, 0, 5); home.Flags.Add("dorgelinda.present"); Rules.Complete(story, home);
            check(Rules.Available(story, receipts, home), "Receipts does not follow the wool.");
            var seen = new HashSet<string>();
            var outcomes = Program.Walk(receipts, home, (page, _) => seen.Add(page));
            string want = woolWays.Single(r.Has).Substring(L.Length);
            check(seen.Contains(want) && woolWays.Count(w => seen.Contains(w.Substring(L.Length))) == 1 && outcomes.Any(o => o.Has(L + "welcomed")),
                "Receipts reads the wrong wool: " + want);
        }

    }
}
