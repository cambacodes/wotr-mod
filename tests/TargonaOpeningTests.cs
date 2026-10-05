using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class TargonaOpeningTests
{
#if TARGONA_TESTS
    private static int Main(string[] args)
    {
        var story = System.Text.Json.JsonSerializer.Deserialize<Story>(System.IO.File.ReadAllText(args.Single()),
            new System.Text.Json.JsonSerializerOptions { IncludeFields = true })!;
        Rules.Validate(story);
        var failures = new HashSet<string>();
        int checks = 0;
        void Check(bool result, string message) { checks++; if (!result) failures.Add(message); }
        Run(story, Check);
        TargonaTricksterTests.Run(story, Check);
        foreach (var failure in failures) Console.Error.WriteLine(failure);
        Console.WriteLine($"Targona: {checks} assertions, {failures.Count} failures.");
        return failures.Count == 0 ? 0 : 1;
    }
#endif

    internal static void Run(Story story, Action<bool, string> check)
    {
        string[] ids = { "unasked_question", "second_margin", "the_folded_room", "an_unpromised_future", "the_unscheduled_door", "what_she_keeps" };
        var scenes = ids.Select(id => story.Scenes.Single(s => s.Id == "targona." + id)).ToArray();
        var focused = new Story { Scenes = scenes.ToList(), Relationships = story.Relationships };
        var seen = scenes.ToDictionary(s => s.Id, _ => new HashSet<string>());
        var native = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SelectedAnswers.Keys).Concat(story.SeenCues.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();
        string[] modes = { "none", "angel", "azata", "aeon", "trickster" };
        string[][] alternatives = {
            new[] { "targona.account_public", "targona.account_private" },
            new[] { "targona.fold_found", "targona.fold_failed", "targona.fold_cut" },
            new[] { "targona.story_leaving", "targona.story_receiving" },
            new[] { "targona.extra_ending", "targona.ordinary_ending" }
        };
        check(story.CompletedQuests["targona.ran_treatment_completed"] == "6ec03ce2f763460c8ac89f4c2064c5ad",
            "Targona continuation does not require the real parent treatment quest.");
        check(story.SeenCues["targona.ran_final_seen"].ToHashSet().SetEquals(new[] {
            "ad655c40be31401386b85287483b3841", "cfc5f3cb2cf94672a96cab742e62225d",
            "62c24328ae744ee98fabd219dbe74c92", "ec76729da60441a1b2028f340743c0a8" }),
            "Targona finale memory uses a start marker or wrong endpoint.");

        // r5 (INT/HOW): ward histories are built from the real Trickster scenes (wand night, arrival, stove, vigil), never from
        // fabricated flags; "lettersFirst" reads the first letter at the wayhouse and only then plays the ward chain.
        const string Corr = "targona.correspondence_romanced", Met = "targona.trickster.met", Tp = "targona.trickster.";
        Snapshot Advance(Snapshot s, string id, Func<Snapshot, bool> pick)
        {
            var sc = story.Scenes.Single(x => x.Id == id);
            var ready = Program.Copy(s); ready.Hour += 200; ready.AvailableContacts.Add("81297c673b63b60448ef88a10db6bc78");
            Rules.Complete(story, ready);
            check(Rules.Available(story, sc, ready), "Targona ward chain cannot reach " + id);
            var outs = Program.Walk(sc, ready).Where(pick).ToList();
            check(outs.Count > 0, "Targona ward chain has no wanted outcome in " + id);
            var r = Program.Copy(outs.Count > 0 ? outs[0] : ready);
            r.AvailableContacts.Clear(); Rules.Complete(story, r);
            return r;
        }
        Snapshot Chain(Snapshot s, bool full)
        {
            if (!s.Has(Tp + "cost.wand_unspent"))
                s = Advance(s, Tp + "free.spent_light", o => o.Has(Tp + "cost.wand_unspent"));
            s = Advance(s, Tp + "free.furlough", o => o.Has(Met));
            if (!full) return s;
            s = Advance(s, Tp + "free.the_stove", o => o.Has(Tp + "free.spark"));
            return Advance(s, Tp + "after.ward", o => o.Has("targona.committed"));
        }
        // The wand night may precede the parent romance and her arrival may follow the visit.
        // Neither stove exit turns that existing lover into a colleague or a first-time courtship.
        void CheckParentEndings(Snapshot arrival, string order)
        {
            check(arrival.Has(Tp + "parent_romanced") && arrival.Has(Met) && !arrival.Has("targona.committed"),
                "The mixed ending history does not preserve the played parent romance: " + order);
            foreach (bool spark in new[] { false, true })
            {
                var stove = Advance(arrival, Tp + "free.the_stove",
                    o => o.Has(Tp + (spark ? "free.spark" : "free.colleagues")));
                foreach (string fate in new[] { "alive", "returned", "lost" })
                foreach (bool lastCall in new[] { false, true })
                {
                    if (fate == "lost" && lastCall) continue; // An active Last Call has earned the return.
                    var ending = Program.Copy(stove); ending.Chapter = 6;
                    ending.Flags.ExceptWith(story.Derived.Keys);
                    if (fate != "alive") ending.Flags.Add("sacrifice");
                    if (fate == "returned" || lastCall) ending.Flags.Add("ending.trickster");
                    if (lastCall) ending.Flags.Add("trickster.lastcall.taken");
                    Rules.Complete(story, ending);
                    var pages = story.Scenes.Where(sc => (sc.Relationship == "targona" && sc.Owner == "Epilogue"
                        || sc.Id == "targona.lastcall.page") && Rules.Available(story, sc, ending))
                        .Select(sc => sc.Id).ToHashSet();
                    var expected = new HashSet<string> { Tp + "epilogue." + (fate == "lost" ? "sacrifice" : "furlough") };
                    if (lastCall) expected.Add("targona.lastcall.page");
                    check(pages.SetEquals(expected), "The parent lover gets inconsistent endings: " + order + "/" + spark
                        + "/" + fate + "/" + lastCall + " => " + string.Join(", ", pages));
                    check(ending.Has("targona.ran_romance") && !ending.Has("targona.committed"),
                        "Selecting an ending rewrites the earned relationship: " + order);
                }
            }
        }
        var endStates = new List<(string Order, Snapshot State)>();

        foreach (string mode in modes)
        foreach (bool parentRomance in new[] { false, true })
        foreach (string currentPath in mode == "none" ? new[] { "angel", "trickster" } : new[] { mode })
        foreach (string order in currentPath == "trickster"
                     ? parentRomance ? new[] { "none", "wardMet", "wardCommitted", "lettersFirst", "delayedArrival" }
                                     : new[] { "none", "wardMet", "wardCommitted", "lettersFirst" }
                     : new[] { "none" })
        {
            // eng-final E-Q8-10: the played wand night and ward visit have funds.
            var initial = new Snapshot { Chapter = 5, Area = scenes[0].Areas.Single(), Hour = 1000,
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000 } };
            initial.Flags.UnionWith(new[] { "targona.free", "targona.ran_" + mode, currentPath,
                "seelah.committed", "arueshalae.committed" });
            if (order != "none") initial.Flags.UnionWith(new[] { "trickster.ever", "chapter_later" });
            Rules.Complete(story, initial);
            // The wand night precedes completion of the parent romance; arrival may remain pending.
            if (parentRomance && order != "none")
                initial = Advance(initial, Tp + "free.spent_light", o => o.Has(Tp + "cost.wand_unspent"));
            initial.Flags.UnionWith(new[] { "targona.ran_treatment_completed", "targona.ran_final_seen" });
            if (parentRomance) initial.Flags.Add("targona.ran_romance");
            Rules.Complete(story, initial);
            if (order == "wardMet" || order == "wardCommitted") initial = Chain(initial, order == "wardCommitted");
            if (parentRomance && order == "wardMet") CheckParentEndings(initial, order);
            check(initial.Has(Corr) == (parentRomance || order == "wardCommitted"), "Targona correspondence misreads the earned romance history.");
            var historyNodes = new HashSet<string>();
            var states = new List<Snapshot> { initial };
            for (int index = 0; index < scenes.Length; index++)
            {
                var scene = scenes[index];
                var next = new List<Snapshot>();
                check(scene.ManualOnly && Rules.IsRemote(scene) && scene.ContactUnit == null,
                    "Targona correspondence fabricates a native physical-contact requirement.");
                bool chained = order == "lettersFirst" && index == 1;
                foreach (var prior in states)
                {
                    var ready = Program.Copy(prior);
                    if (chained)
                    {
                        // The reverse order: the first letter has been read; arrival and the ward courtship still open.
                        check(prior.Has("targona.correspondence_opened"), "Targona reverse order did not read the first letter.");
                        ready = Chain(ready, true);
                        check(ready.Has("targona.committed") && ready.Has(Corr), "Reading correspondence blocks the ward courtship.");
                    }
                    else if (index > 0)
                    {
                        check(!Rules.Available(story, scene, ready), "Targona reply ignores the predecessor delay.");
                        ready.Hour += scene.DelayHours;
                    }
                    check(Rules.Available(story, scene, ready), "Attainable parent history cannot enter " + scene.Id);
                    check(Rules.NextRemote(focused, ready) == null, "Targona private correspondence hijacks the rest queue.");
                    foreach (var result in Program.Walk(scene, ready, (node, partial) =>
                    {
                        seen[scene.Id].Add(node);
                        historyNodes.Add(scene.Id + "/" + node);
                        check(partial.Flags.SetEquals(ready.Flags), "Targona records an unacknowledged intermediate outcome.");
                        // Q6 r5 (CAN): Anograt appears, in any node, only in the histories whose treatment created her.
                        if (scene.Nodes.Single(x => x.Id == node).Text.Contains("Anograt", StringComparison.Ordinal))
                            check(mode == "aeon" || mode == "trickster", "Targona names Anograt in a history without her: " + scene.Id + "/" + node);
                        if (node == "anograt" || node == "two")
                            check(mode == "aeon" || mode == "trickster", "Targona invents Anograt for a different transformation history.");
                        if (node == "lover" || node == "romance")
                            check(ready.Has(Corr), "Targona duplicates a romance after the parent friendship decision.");
                        if (node == "friend" || node == "friend_ward")
                            check(!ready.Has(Corr), "Targona addresses an earned lover as a friend.");
                        // r5: one address. After the ward meeting she writes from Drezen's ward, never from the wayhouse.
                        if ((node == "friend" && scene.Id == "targona.unasked_question") || node == "question")
                            check(!ready.Has(Met), "Targona writes from the wayhouse while she works Drezen's ward: " + scene.Id + "/" + node);
                        if (node == "friend_ward" || node == "question_ward")
                            check(ready.Has(Met), "Targona writes from a ward she never came to: " + scene.Id + "/" + node);
                        if (ready.Has(Met))
                            check(!scene.Nodes.Single(x => x.Id == node).Text.Contains("wayhouse", StringComparison.Ordinal),
                                "Targona's ward letter places her at the wayhouse: " + scene.Id + "/" + node);
                    }))
                    {
                        check(ready.Flags.IsSubsetOf(result.Flags), "Targona removes established history.");
                        check(native.All(f => result.Has(f) == ready.Has(f)), "Targona writes native or parent romance state.");
                        check(result.Has("seelah.committed") && result.Has("arueshalae.committed"), "Targona interferes with another romance.");
                        check(result.Has("targona.committed") == ready.Has("targona.committed"), "Correspondence silently awards or drops a full commitment.");
                        check(result.Has("targona.ran_romance") == ready.Has("targona.ran_romance"), "Correspondence rewrites the parent romance history.");
                        check(!result.Has("targona.extra_ending") || currentPath == "trickster", "A non-Trickster uses the authored fate trick.");
                        check(result.AvailableContacts.Count == 0, "A letter invents a loaded Targona actor.");
                        foreach (var group in alternatives)
                            check(group.Count(result.Has) <= 1, "Targona mixes opposing correspondence outcomes.");
                        if (result.Has(scene.Id)) next.Add(result);
                        else check(result.Flags.SetEquals(ready.Flags), "Postponing correspondence records progress.");
                    }
                }
                states = next.GroupBy(s => string.Join("|", s.Flags.OrderBy(f => f))).Select(g => g.First()).ToList();
                check(states.Count > 0, "Targona loses every continuing history.");
            }
            check(states.All(s => s.Has("targona.extension_opening_kept")), "Targona correspondence lacks a played conclusion.");
            check(states.Any(s => s.Has("targona.ordinary_ending")), "Targona forces a supernatural intervention.");
            if (currentPath == "trickster") check(states.Any(s => s.Has("targona.extra_ending")), "Trickster's bespoke continuation is unreachable.");
            if (order == "wardCommitted")
                check(historyNodes.Contains("targona.unasked_question/romance") && historyNodes.Contains("targona.what_she_keeps/lover"),
                    "The ward commitment does not reach the lover letters.");
            if (order == "lettersFirst")
                check(historyNodes.Contains("targona.unasked_question/" + (parentRomance ? "romance" : "friend"))
                      && historyNodes.Contains("targona.an_unpromised_future/question_ward")
                      && historyNodes.Contains("targona.what_she_keeps/lover"), "The reverse order does not move her letters to the ward and the lover page.");
            if (order == "wardMet")
                check(historyNodes.Contains("targona.unasked_question/" + (parentRomance ? "romance" : "friend_ward"))
                      && historyNodes.Contains("targona.what_she_keeps/" + (parentRomance ? "lover" : "friend")),
                    "The ward meeting misreads the parent romance history.");
            endStates.AddRange(states.Select(s => (order, s)));
        }

        // r5: the visit. A wayhouse lover (parent romance) gets the road; the ward's lover gets an hour off the rows instead.
        var threshold = story.Scenes.Single(s => s.Id == "targona.the_open_threshold");
        var evening = story.Scenes.Single(s => s.Id == "targona.ward_evening");
        var eveningNodes = new HashSet<string>();
        var followup = story.Scenes.Single(s => s.Id == "targona.the_key_remains_hers");
        var visitNodes = new HashSet<string>();
        var replyNodes = new HashSet<string>();
        string[] replies = { "desire", "tender", "pause", "correspondence" };
        void ReadReply(Snapshot visit)
        {
            var ready = Program.Copy(visit); Rules.Complete(story, ready);
            if (ready.Hour == ready.Times[threshold.Id])
                check(!Rules.Available(story, followup, ready), "The final reply ignores its delay.");
            ready.Hour = Math.Max(ready.Hour, ready.Times[threshold.Id] + followup.DelayHours);
            check(Rules.Available(story, followup, ready), "The played visit cannot reach the final reply.");
            string reply = replies.Single(r => ready.Has("targona.visit_" + r));
            bool moved = ready.Has(Met);
            var pages = new HashSet<string>();
            foreach (var outcome in Program.Walk(followup, ready, (node, _) =>
            {
                replyNodes.Add(node); pages.Add(node);
                string text = followup.Nodes.Single(n => n.Id == node).Text;
                if (moved)
                    check(!text.Contains("eastern courier", StringComparison.Ordinal)
                          && !text.Contains("key to the wayhouse", StringComparison.Ordinal)
                          && !text.Contains("when the road is quiet", StringComparison.Ordinal),
                        "The final ward reply uses her old wayhouse address: " + node);
            }))
            {
                check(outcome.Has(followup.Id) && !Rules.Available(story, followup, outcome), "The final reply does not finish once.");
                check(outcome.Has("targona.key_reciprocal") != outcome.Has("targona.key_unpressured"), "The final reply loses or mixes its response.");
                check(native.All(f => outcome.Has(f) == ready.Has(f))
                      && outcome.Has("targona.committed") == ready.Has("targona.committed")
                      && outcome.Has("seelah.committed") && outcome.Has("arueshalae.committed"), "The final reply rewrites established relationships.");
            }
            check(pages.SetEquals(moved ? new[] { "start", "start_ward", reply + "_ward" } : new[] { "start", reply }),
                "The final reply does not match its visit outcome and current address: " + reply + "/" + moved);
        }
        foreach (var (order, end) in endStates)
        {
            var later = Program.Copy(end); later.Hour += 200; Rules.Complete(story, later);
            bool ward = later.Has(Met), lover = later.Has(Corr);
            check(Rules.Available(story, threshold, later) == (lover && !ward), "The wayhouse visit opens for the wrong history: " + order);
            check(!Rules.Available(story, evening, later), "The in-person ward evening opens without her at the cots: " + order);
            var present = Program.Copy(later); present.AvailableContacts.Add("81297c673b63b60448ef88a10db6bc78");
            check(Rules.Available(story, evening, present) == (lover && ward), "The ward evening opens for the wrong history: " + order);
            if (lover && ward)
                foreach (var o in Program.Walk(evening, present, (node, _) => eveningNodes.Add(node)))
                    check(o.Has("targona.committed") == present.Has("targona.committed")
                          && o.Has("targona.ran_romance") == present.Has("targona.ran_romance")
                          && !o.Has("targona.closed"), "The ward evening rewrites the commitment.");
            if (lover && !ward)
            {
                var visits = Program.Walk(threshold, later, (node, _) => visitNodes.Add(node)).Where(o => o.Has(threshold.Id)).ToList();
                foreach (var reply in replies)
                    if (later.Has("trickster")) check(visits.Any(o => o.Has("targona.visit_" + reply)), "The visit loses its " + reply + " branch.");
                foreach (var visit in visits)
                {
                    ReadReply(visit);
                    if (order == "delayedArrival")
                    {
                        check(visit.Has(Tp + "cost.wand_unspent") && visit.Has("targona.ran_romance") && !visit.Has(Met),
                            "The mixed history did not keep arrival pending until after the visit.");
                        var arrival = Advance(visit, Tp + "free.furlough", o => o.Has(Met));
                        ReadReply(arrival);
                        CheckParentEndings(arrival, order);
                    }
                }
            }
        }
        check(visitNodes.SetEquals(threshold.Nodes.Select(n => n.Id)), "The played visits leave unreachable prose.");
        check(replyNodes.SetEquals(followup.Nodes.Select(n => n.Id)), "The played final replies leave unreachable prose.");
        check(evening.ContactUnit == "81297c673b63b60448ef88a10db6bc78" && evening.InteractionHub == "targona.presence" && !Rules.IsRemote(evening),
            "The ward evening is delivered as a letter instead of in person.");
        var eveningStart = evening.Nodes.Single(n => n.Id == "start").Choices;
        check(eveningStart.Single(c => c.Next == "paid").Crusade?.Resource == "Finances" && eveningStart.Single(c => c.Next == "paid").Crusade!.Amount == -100
              && eveningStart.Single(c => c.Next == "cover").Crusade == null, "The novices are not paid for, or the lie costs coin.");
        check(eveningNodes.SetEquals(evening.Nodes.Select(n => n.Id)), "The ward evening has unreachable prose.");

        foreach (var scene in scenes)
        {
            check(scene.Nodes.All(n => n.Portrait == "TargonaCorrespondence"),
                "Targona correspondence falls back to unrelated speaker or Tirabade artwork.");
            check(seen[scene.Id].SetEquals(scene.Nodes.Select(n => n.Id)), "Targona has unreachable prose: " + scene.Id);
            var ready = new Snapshot { Chapter = 5, Area = scene.Areas.Single(), Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires); ready.Flags.Add("targona.ran_trickster"); ready.Flags.Add("trickster");
            check(Rules.Available(story, scene, ready), "Targona gate baseline invalid.");
            foreach (string flag in scene.Requires)
            {
                var missing = Program.Copy(ready); missing.Flags.Remove(flag);
                check(!Rules.Available(story, scene, missing), "Targona bypasses parent/native prerequisite " + flag);
            }
            foreach (string flag in scene.Forbids)
            {
                var blocked = Program.Copy(ready); blocked.Flags.Add(flag);
                check(!Rules.Available(story, scene, blocked), "Targona rewrites excluded identity/path/death history " + flag);
            }
            var wrong = Program.Copy(ready); wrong.Flags.Remove("targona.ran_trickster");
            check(!Rules.Available(story, scene, wrong), "Trickster alone fabricates parent treatment progress.");
            wrong = Program.Copy(ready); wrong.Flags.Remove("targona.ran_final_seen"); wrong.Flags.Add("targona.ran_dialog_started");
            check(!Rules.Available(story, scene, wrong), "Starting a dialogue substitutes for the parent finale.");
            wrong = Program.Copy(ready); wrong.Chapter = 3;
            check(!Rules.Available(story, scene, wrong), "Targona extension begins before its chapter-five finale.");
            wrong = Program.Copy(ready); wrong.Area = "outside_drezen";
            check(!Rules.Available(story, scene, wrong), "Drezen correspondence invents delivery elsewhere.");
        }

        var paper = scenes[2];
        var skill = paper.Nodes.SelectMany(n => n.Choices).Single(c => c.Check != null);
        check(skill.Check!.Skill == "SkillPerception" && skill.Check.DC == 25 && skill.Check.CommanderOnly
            && skill.Check.Success == "found" && skill.Check.Failure == "creased" && skill.Set.Length == 0,
            "Targona paper inspection changes its outcome/actor contract.");
        var seed = new Snapshot { Chapter = 5, Area = paper.Areas.Single(), Hour = 1000 };
        seed.Flags.UnionWith(paper.Requires); seed.Flags.Add("targona.ran_trickster");
        Program.Walk(paper, seed, (page, partial) =>
        {
            if (page != "found" && page != "creased") return;
            check(!alternatives[1].Any(partial.Has), "Targona commits an unacknowledged roll outcome.");
            var replay = Program.Copy(partial);
            check(Rules.Available(story, paper, replay), "An interrupted paper inspection cannot reopen.");
            var cut = Program.Walk(paper, replay).Where(s => s.Has("targona.fold_cut")).ToArray();
            check(cut.Length > 0 && cut.All(s => alternatives[1].Count(s.Has) == 1), "Targona failed roll contaminates non-roll replay.");
        });
    }
}
