using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class MinaghoChivarroContinuationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string prefix = "minachiv.";
        const string capital = "2570015799edf594daf2f076f2f975d8";
        // The registered RanRomance continuation; the pair's Trickster route has its own suite (MinaghoChivarroTricksterTests).
        // eng7-f6c begin: native responses use their selector suite, not this continuation's ending arbitration.
        bool Registered(Scene s) => s.Relationship == "minagho_chivarro" && !Rules.IsNativeReplacement(story, s)
            && (!s.Id.StartsWith("minagho_chivarro.trickster.", StringComparison.Ordinal)
                || s.Id == "minagho_chivarro.trickster.epilogue.partner_refused");
        // eng7-f6c end
        var savedVisits = story.Scenes.Where(s => Registered(s) && s.Id.StartsWith(prefix, StringComparison.Ordinal)
            && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var visits = savedVisits.Where(s => !s.Forbids.Contains("chapter_later")).ToArray();
        check(savedVisits.Length == 23 && savedVisits.Length - visits.Length == 9, "Minachiv must retain all 23 saved scenes and retire exactly nine.");
        var endings = story.Scenes.Where(s => Registered(s) && s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        check(visits.Length == 14, "Minagho/Chivarro continuation must deliver its 14 kept visits.");
        var reached = new HashSet<string>();
        var produced = new HashSet<string>();
        var checkedPages = new HashSet<string>();
        var partial = new List<Snapshot>();
        var finished = new List<Snapshot>();
        var native = story.Etudes.Keys.Concat(story.CompletedQuests.Keys).Concat(story.CompletedEtudes.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys).ToHashSet();

        void ObserveCue(Snapshot state, string guid)
        {
            var keys = story.SeenCues.Where(p => p.Value.Contains(guid)).Select(p => p.Key).ToArray();
            check(keys.Length > 0, "Unmapped actual parent terminal cue " + guid);
            state.Flags.UnionWith(keys);
        }
        void ReadEtude(Snapshot state, string guid)
        {
            var keys = story.Etudes.Where(p => p.Value == guid).Select(p => p.Key).ToArray();
            check(keys.Length > 0, "Unmapped actual parent etude " + guid);
            state.Flags.UnionWith(keys);
        }
        HashSet<string> Reads(IEnumerable<Scene> scenes) => scenes.SelectMany(s => s.Requires.Concat(s.RequiresAny).Concat(s.Forbids)
            .Concat(s.RequiresAnyGroups.SelectMany(g => g))
            .Concat(s.Nodes.SelectMany(n => n.Choices.SelectMany(c => c.Requires.Concat(c.Forbids))))).ToHashSet();

        // Each fixture supplies external native/parent observations, never addon progress.
        // The DLL's own books are statically audited separately; this harness does not execute them.
        var fixtures = new[]
        {
            ("freed_trickster", "4dbb41f1fb134b90ab3900dc05488e8f", new[] { "f18391398cb5470c94f8932e9d8d2fd7", "b5c19cd01e364df99f6c946c7da14751" }, true, false),
            ("freed_other", "4dbb41f1fb134b90ab3900dc05488e8f", new[] { "f18391398cb5470c94f8932e9d8d2fd7", "b5c19cd01e364df99f6c946c7da14751" }, false, false),
            ("redemption", "5584da70433e4f079d521d40ce77f230", new[] { "4a29c758798d47a1a32f506d1ca6081b", "592dcdccbef043f58031fa234faf137a", "813cc79c053d4b3e869a0d0ca2f3d85d", "b5c19cd01e364df99f6c946c7da14751" }, false, true),
            ("cult", "4dbb41f1fb134b90ab3900dc05488e8f", new[] { "4a29c758798d47a1a32f506d1ca6081b", "3d21fa8120d040338ec1d4b8461fa536", "b5c19cd01e364df99f6c946c7da14751" }, false, false),
            ("dragon", "5584da70433e4f079d521d40ce77f230", new[] { "e303c58d307849cd892fa5810124da92", "b5c19cd01e364df99f6c946c7da14751" }, false, true),
            ("legend", "5584da70433e4f079d521d40ce77f230", new[] { "a87da83417ff4be28c9ccfaf9b154e96", "b5c19cd01e364df99f6c946c7da14751" }, false, false),
            ("sanctuary", "19099aba216e46e98d446709c3f2e0f3", new[] { "1e6ca1514807446ea2fddd65e4f5bcc8" }, false, false),
            ("ordinary_refusal", "98baa5299ae444bfa1ac8ba8e84f2c7c", new[] { "f18391398cb5470c94f8932e9d8d2fd7" }, false, false),
            ("soft_refusal", "c51a76731dc24865b6c472ffe6bf3e18", new[] { "a87da83417ff4be28c9ccfaf9b154e96" }, false, false),
            ("demon_romance", "c01f7f83a2584555b2f551918f169cdb", new[] { "58557969a797441983022c8ba0400400", "b5c19cd01e364df99f6c946c7da14751" }, false, false),
            ("demon_refusal", "341b62dd58d14906959d3262b12f1a43", new[] { "58557969a797441983022c8ba0400400" }, false, false),
        };
        foreach (var fixture in fixtures)
        {
            var initial = new Snapshot { Chapter = 5, Hour = 1000, Area = capital,
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Favors"] = 10000 } };
            initial.Flags.UnionWith(new[] { "seelah.committed", "jerribeth.committed", "committed", "closed" });
            initial.Flags.UnionWith(story.CompletedQuests.Where(p => p.Value == "5cd5f22437a1465180b45c080899577a").Select(p => p.Key));
            // eng7-l02: a current Trickster plays the authored reunion; native searching is Azata-only.
            if (fixture.Item4)
                initial.Flags.UnionWith(NativeFactInventoryTests.EarnReunion(story, check).Flags);
            else ReadEtude(initial, "71f85264d9064074f9cf74999ecbffa9");
            Rules.Complete(story, initial);
            // eng7-l02 end
            foreach (var guid in fixture.Item3) ReadEtude(initial, guid);
            ObserveCue(initial, fixture.Item2);
            if (fixture.Item4) { initial.Flags.Add("trickster"); ObserveCue(initial, "a8f7a881cc6d427b91cbbee14f43e0ee"); }
            if (fixture.Item5) ObserveCue(initial, "e15de525c99d40c6a6faf0afa61be756");
            var originalNative = initial.Flags.Where(native.Contains).ToHashSet();
            // eng7-l02: the played brand producer also sets the existing shared started flag.
            check(!initial.Flags.Any(f => f.StartsWith(prefix, StringComparison.Ordinal) && f != "minachiv.reunion_history"
                && f != "minachiv.brand_live" // Derived native brand state is not played addon progress.
                && !(fixture.Item4 && f == "minachiv.started")), "Fixture fabricated addon history.");
            check(Program.CurrentAvailable(story, visits[0], initial), "Actual parent terminal rejected: " + fixture.Item1);
            check(endings.All(e => !Program.CurrentAvailable(story, e, initial)), "Unplayed continuation steals a parent-only ending.");
            foreach (var blocker in new[] { "minagho.dead", "chivarro.dead", "inhuman", "minachiv.closed" })
            {
                var blocked = Program.Copy(initial); blocked.Flags.Add(blocker);
                check(!Program.CurrentAvailable(story, visits[0], blocked), "Initial meeting ignores known blocker " + blocker);
            }
            foreach (var missing in new[] { "minagho.ran_complete", "minagho.book_three_finished", "minachiv.reunion_history" })
            {
                var absent = Program.Copy(initial); absent.Flags.Remove(missing);
                if (story.Derived.TryGetValue(missing, out var sources)) absent.Flags.ExceptWith(sources.SelectMany(g => g));
                if (story.Latches.TryGetValue(missing, out var observations)) absent.Flags.ExceptWith(observations);
                check(!Program.CurrentAvailable(story, visits[0], absent), "Parent start uses timers/dialog start instead of " + missing);
            }
            var states = new List<Snapshot> { initial };
            for (int i = 0; i < visits.Length; i++)
            {
                var scene = visits[i]; var next = new List<Snapshot>();
                foreach (var input in states)
                {
                    var ready = Program.Copy(input); ready.Hour += 48;
                    check(Program.CurrentAvailable(story, scene, ready), "Earned parent continuation cannot enter " + fixture.Item1 + "/" + scene.Id);
                    if (scene.Id == "minachiv.the_second_address" && ready.Has("minagho.brand_trick_seen"))
                    {
                        var formerTrickster = Program.Copy(ready); formerTrickster.Flags.Remove("trickster");
                        check(Program.CurrentAvailable(story, scene, formerTrickster), "Changing mythic abandons an already earned meeting.");
                        check(scene.Nodes[0].Choices.Where(c => Rules.Match(c.Requires, c.Forbids, formerTrickster)).All(c => c.Next != "trick"), "Former Trickster retains an unavailable fate power.");
                    }
                    check(scene.Remote && scene.Owner == "Memory" && scene.ContactUnit == null && scene.AdditionalContactUnits.Length == 0 && Rules.EntryTargets(scene).Length == 0, "Narrated visit invents native unit/dialogue delivery.");
                    // Replaying saved histories also covers fallbacks no fresh chain now needs.
                    var histories = new List<Snapshot> { ready };
                    if (scene.Id == "minachiv.what_the_offer_bought")
                    {
                        var parked = Program.Copy(ready);
                        parked.Flags.ExceptWith(new[] { "minachiv.business_chosen", "minachiv.bait_chosen", "minachiv.refusal_chosen",
                            "minachiv.terms_sent", "minachiv.evidence_kept", "minachiv.source_found" });
                        histories.Add(parked);
                    }
                    if (scene.Id == "minachiv.when_the_door_opens")
                        foreach (var ending in new[] { "minachiv.winter_ending", "minachiv.host_ending" })
                        { var parked = Program.Copy(ready); parked.Flags.Add(ending); histories.Add(parked); }
                    if (scene.Id == "minachiv.after_the_last_lamp")
                    {
                        var parked = Program.Copy(ready);
                        parked.Flags.ExceptWith(new[] { "minachiv.after_show_promised", "minachiv.after_show_open" });
                        histories.Add(parked);
                    }
                    foreach (var history in histories)
                    foreach (var result in Program.Walk(scene, history, (id, state) =>
                    {
                        reached.Add(scene.Id + "/" + id);
                        // Job 4 checks and calls now publish their own local receipts before the terminal.
                        var localEffects = scene.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Set).ToHashSet();
                        check(state.Flags.Except(history.Flags).All(f => localEffects.Contains(f) || story.Derived.ContainsKey(f)),
                            "Interrupted continuation fabricated unrelated history: " + scene.Id + "/" + id);
                        check(!state.Has(scene.Id), "Interrupted continuation records completion before its terminal: " + scene.Id + "/" + id);
                        if (scene.Id.EndsWith("the_unhired_evening") && id == "want" && state.Has("minagho.ran_demon"))
                        {
                            var offered = scene.Nodes.Single(n => n.Id == id).Choices.Where(c => Rules.Match(c.Requires, c.Forbids, state));
                            check(offered.All(c => c.Next != "minagho" && c.Next != "together" && c.Next != "slow"), "Demon service is treated as free Minagho consent.");
                        }
                        if (id == "trick" && scene.Id.EndsWith("the_second_address")) check(state.Has("trickster") && state.Has("minagho.brand_trick_seen"), "Fate option invents the witnessed parent brand trick.");
                        if (id == "scrolls") check(state.Has("minagho.chivarro_scrolls_reported"), "Unheard parent scroll report is remembered.");
                        if (scene.Id.EndsWith("after_the_last_lamp") && id == "affection") check(state.Has("minachiv.chivarro_affection"), "Private physical affection lacks Chivarro's own earned agreement.");
                        if (!checkedPages.Add(fixture.Item1 + "/" + scene.Id + "/" + id)) return;
                        check(Rules.ContactAvailable(story, scene, state), "Valid narrated contact fails inside scene.");
                        foreach (var flag in new[] { "minagho.dead", "chivarro.dead", "inhuman" })
                        {
                            var blocked = Program.Copy(state); blocked.Flags.Add(flag);
                            check(!Program.CurrentAvailable(story, scene, blocked) && !Rules.ContactAvailable(story, scene, blocked), "Remote life guard fails: " + flag);
                        }
                        foreach (var missing in new[] { "minagho.ran_complete", "minagho.book_three_finished", "minachiv.reunion_history" })
                        {
                            var blocked = Program.Copy(state); blocked.Flags.Remove(missing);
                            check(!Rules.ContactAvailable(story, scene, blocked), "Remote parent-history guard is entry-only: " + missing);
                        }
                        var away = Program.Copy(state); away.Area = "elsewhere";
                        check(!Program.CurrentAvailable(story, scene, away) && !Rules.ContactAvailable(story, scene, away), "Drezen book continues in another area.");
                        away.Area = capital; away.Chapter = 4;
                        check(!Program.CurrentAvailable(story, scene, away) && !Rules.ContactAvailable(story, scene, away), "Post-Book3 book enters Chapter4.");
                    }))
                    {
                        if (!result.Has(scene.Id))
                        {
                            check(result.Flags.SetEquals(ready.Flags), "Postponement changed history.");
                            continue;
                        }
                        check(!Program.CurrentAvailable(story, scene, result), "Narrated meeting repeats after completion.");
                        check(result.Flags.Where(native.Contains).ToHashSet().SetEquals(originalNative), "Addon changes a native or parent state.");
                        check(new[] { "seelah.committed", "jerribeth.committed", "committed", "closed" }.All(result.Has), "Addon changes unrelated/ToyBox-compatible relationships.");
                        produced.UnionWith(result.Flags.Where(f => f.StartsWith(prefix, StringComparison.Ordinal)
                            || f.StartsWith("minagho_chivarro.partner_stance.", StringComparison.Ordinal)));
                        if (i + 1 < visits.Length)
                        {
                            var following = visits[i + 1];
                            var sameEvening = following.Id == "minachiv.after_the_last_lamp";
                            check(following.DelayHours == (sameEvening ? 0 : 24), "Incorrect authored chronology: " + following.Id);
                            check(Program.CurrentAvailable(story, following, result) == sameEvening, "Immediate after-show entry or earned next-day delay failed: " + following.Id);
                        }
                        next.Add(result);
                    }
                }
                var future = Reads(visits.Skip(i + 1).Concat(endings));
                states = next.GroupBy(s => string.Join("|", s.Flags.Where(future.Contains).OrderBy(f => f))).Select(g => g.First()).ToList();
                check(states.Count > 0, "Campaign has no complete path: " + scene.Id);
                if (i is 0 or 1 or 6 or 11 || scene.Id == "minachiv.what_she_will_take") partial.AddRange(states);
            }
            finished.AddRange(states);
        }
        // Keep the original continuation coverage contract; the stance suite
        // supplies current-Trickster fixtures for the appended decision nodes and their slots.
        foreach (var page in visits.SelectMany(s => s.Nodes.Where(n => !n.Id.StartsWith("stance_", StringComparison.Ordinal)
            && !(n.Id.Contains(".explicit.") && s.Nodes.Where(host => host.Choices.Any(c => c.Next == n.Id))
                .All(host => host.Id.StartsWith("stance_", StringComparison.Ordinal)))
            && !(s.Id == "minachiv.the_performer_and_the_key" && (n.Id == "pleasure" || n.Id == "audience")))
            .Select(n => s.Id + "/" + n.Id))) check(reached.Contains(page), "No earned-history witness for page " + page);
        foreach (var flag in visits.SelectMany(s => s.Nodes).SelectMany(n => n.Choices).SelectMany(c => c.Set).Distinct())
            check(produced.Contains(flag), "No played producer for outcome " + flag);
        var witnessedEndings = new HashSet<string>();
        foreach (var state in finished.Concat(partial))
        {
            var complete = state.Has("minachiv.complete");
            if (state.Has("minagho_chivarro.partner_stance.cooled"))
            {
                var refused = endings.Where(e => Program.CurrentAvailable(story, e, state)).ToArray();
                check(refused.Length == 1 && refused[0].Id == "minagho_chivarro.trickster.epilogue.partner_refused",
                    "Refused stance receives a continuing romance ending.");
                witnessedEndings.Add(refused[0].Id);
                continue;
            }
            var ordinary = endings.Where(e => e.Owner == "Epilogue" && Program.CurrentAvailable(story, e, state)).ToArray();
            check(ordinary.Length == 1, "Normal ending overlap/gap: " + string.Join(",", ordinary.Select(e => e.Id)));
            witnessedEndings.Add(ordinary[0].Id);
            check(complete || ordinary[0].Id.Contains("unfinished"), "Interrupted history receives a completed farewell.");
            if (!complete && state.Has("minachiv.chivarro_lasting")) check(ordinary[0].Id == "minachiv.ending_unfinished_lasting", "Interrupted farewell erases an already chosen Chivarro commitment.");
            foreach (var variant in new[]
            {
                (new[] { "minagho.dead" }, "minagho_lost"),
                (new[] { "chivarro.dead" }, "chivarro_lost"),
                (new[] { "minagho.dead", "chivarro.dead", "ascended", "sacrifice", "inhuman" }, "both_lost"),
                (new[] { "inhuman", "ascended" }, "changed"),   // earned presence: a changed or risen Commander never also lies in the Wound
                (new[] { "ascended" }, "ascent"),
                (new[] { "sacrifice" }, "sacrifice"),
            })
            {
                var changed = Program.Copy(state); changed.Flags.UnionWith(variant.Item1);
                var selected = endings.Where(e => e.Owner == "Epilogue" && Program.CurrentAvailable(story, e, changed)).ToArray();
                var expected = prefix + "ending_" + variant.Item2 + (complete ? "_completed" : "");
                check(selected.Length == 1 && selected[0].Id == expected, "Special ending arbitration failed: " + expected);
                witnessedEndings.Add(selected[0].Id);
            }
            var aeon = endings.Where(e => e.Owner == "AeonEpilogue" && Program.CurrentAvailable(story, e, state)).ToArray();
            check(aeon.Length == 1 && aeon[0].Id == "minachiv.ending_aeon" + (complete ? "_completed" : ""), "Aeon ending lacks an earned complete/interrupted witness.");
            witnessedEndings.Add(aeon[0].Id);
        }
        foreach (var ending in endings)
            check(witnessedEndings.Contains(ending.Id), "No played-history witness selects ending " + ending.Id);
        foreach (var scene in visits)
        foreach (var choice in scene.Nodes.SelectMany(n => n.Choices))
            check(choice.Set.All(f => f.StartsWith(prefix, StringComparison.Ordinal)
                || f.StartsWith("minagho_chivarro.partner_stance.", StringComparison.Ordinal)) && choice.Revive == null, "Continuation writes parent progress or invents recovery.");
    }
}
