using System;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8a / E-Q8-01. Native events and physical observations are fixtures;
// returns, closures, first-night acceptance and departure receipts come from played answers.
internal static class LatestStateInventoryTests
{
    const string N = "nenio.trickster.", W = "wenduag.trickster.", E = Rules.WenduagEchoPrefix;
    static Snapshot Refresh(Story story, Snapshot state)
    {
        state.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
        if (Rules.ChapterFlag(state.Chapter) is string chapter) state.Flags.Add(chapter);
        Rules.Complete(story, state);
        return state;
    }
    static Snapshot At(Story story, Scene scene, Snapshot history)
    {
        var state = Program.Copy(history);
        state.Chapter = scene.MinChapter; state.Area = scene.Areas.FirstOrDefault() ?? Rules.NurahCapital;
        state.Hour += 100;
        return Refresh(story, state);
    }
    static void EchoObserve(Story story, Snapshot state, string phase, bool living = true, bool wellFormed = true)
    {
        state.Flags.ExceptWith(Rules.WenduagEchoRuntime);
        Rules.ObserveWenduagEchoLife(state, phase, Rules.WenduagEchoCustodyMatches(state, phase, wellFormed), living);
        Refresh(story, state);
    }
    static void NenioCases(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var initial = new InventoryWorldBuilder(story, 5, Rules.NurahCapital);
        initial.Native("trickster"); initial.Native("nenio.dead");
        initial.ObserveActor(story.Revivals["nenio"].Unit, alive: false, retained: true);
        initial.Advance(100);
        var restored = initial.Earn(N + "dead.the_price", N + "returned");
        check(restored.Actors.Single(a => a.Unit == story.Revivals["nenio"].Unit).Alive,
            "q8a: paid Nenio restoration did not revive the retained original");
        check(restored.State.Has(N + "cost.manuscript_surrendered"),
            "q8a: the paid restoration lost its manuscript price; flags=" + string.Join(",", restored.State.Flags.Where(f => f.StartsWith("nenio"))));
        check(Rules.RouteOpen(story.Relationships["nenio"], restored.State), "q8a: paid native restoration remained unavailable");
        check(!restored.Available(N + "dead.the_price"), "q8a: the one-shot return became a repeatable bargain");

        // Progression checkpoint for the earlier dictation; the hypothesis/result
        // answers below actually produce acceptance, first night, refusal and void.
        restored.Checkpoint("prior dictation", N + "scribe", "nenio.folio.demons");
        restored.Advance(100);
        var experiment = restored.Earn(N + "commit.hypothesis", N + "test_running");
        experiment.Advance(100);
        var results = experiment.Walk(N + "commit.result");
        var accepted = results.First(w => w.State.Has("nenio.committed"));
        var closed = results.First(w => w.State.Has("nenio.closed"));
        var voidExperiment = restored.Copy(); voidExperiment.Checkpoint("tampered experimental notes", N + "tampered");
        voidExperiment = voidExperiment.Earn(N + "commit.hypothesis", N + "test_running");
        voidExperiment.Advance(100);
        var declined = voidExperiment.Earn(N + "commit.result", N + "declined");
        var guest = story.Books["trickster.ledger"].Entries.Single(e => e.Id == "guest.nenio");
        foreach (var row in new[] {
            ("night", accepted.State), ("epilogue.article", accepted.State),
            // eng-final: Q8-13 requires the actually played proposal as well as return.
            ("epilogue.commit", experiment.State), ("epilogue.void", declined.State),
            ("epilogue.closed", closed.State) })
        {
            var scene = S(N + row.Item1);
            var live = At(story, scene, row.Item2);
            check(Rules.Available(story, scene, live), "q8a: current living control unavailable: " + scene.Id);
            // Current native loss is observed AFTER the restoration, independently
            // of its old dead.latched timestamp and irrespective of earlier closure.
            var dead = Program.Copy(live); dead.Hour++;
            dead.Flags.Add("nenio.dead"); Refresh(story, dead);
            check(dead.Flags.Contains(N + "returned"), "q8a: historical Nenio payment was erased");
            check(!Rules.Available(story, scene, dead), "q8a: later native death retained living content: " + scene.Id);
            check(!Rules.RouteOpen(story.Relationships["nenio"], dead), "q8a: later native death retained RouteOpen");
            check(!Rules.BookEntryVisible(guest, dead), "q8a: later native death retained Guest List");
            var options = new JsonSerializerOptions { IncludeFields = true };
            dead = JsonSerializer.Deserialize<Snapshot>(JsonSerializer.Serialize(dead, options), options)!;
            Refresh(story, dead);
            check(!Rules.Available(story, scene, dead), "q8a: reload turned the earlier return into a second resurrection");
            // Ordinary native resurrection of the same original clears its current
            // death only. The saved manuscript payment is neither repeated nor erased.
            dead.Flags.Remove("nenio.dead"); dead.Flags.Remove("nenio.life.unavailable");
            Rules.ObserveNenioLife(dead, true, false, false); Refresh(story, dead);
            check(Rules.Available(story, scene, dead), "q8a: later native resurrection did not answer its current death");
            foreach (string unrelated in new[] { "nenio.kicked_out", "nenio.sent_away", "nenio.killed_by_commander", "nenio.dissolved" })
            {
                var lost = Program.Copy(dead); lost.Flags.Add(unrelated); Refresh(story, lost);
                check(!Rules.Available(story, scene, lost), "q8a: native resurrection lifted unrelated loss: " + unrelated + "/" + scene.Id);
            }
            foreach (var problem in new[] { (false, false, false, "missing original"), (true, true, false, "dead original"), (true, false, true, "lost visitor") })
            {
                var unavailable = Program.Copy(live);
                Rules.ObserveNenioLife(unavailable, problem.Item1, problem.Item2, problem.Item3); Refresh(story, unavailable);
                check(!Rules.Available(story, scene, unavailable), "q8a: body observation retained " + problem.Item4 + "/" + scene.Id);
                check(!Rules.BookEntryVisible(guest, unavailable), "q8a: Guest List retained " + problem.Item4);
            }
        }
        // Reuse the existing paid new-vessel and probation receipts on old saves.
        // Their separate loss-specific keys must not require new synthetic payments.
        foreach (var row in new[] { ("nenio.dead", N + "cost.recreated"), ("nenio.killed_by_commander", N + "cost.unremembered"),
            ("nenio.kicked_out", N + "cost.demoted"), ("nenio.sent_away", N + "cost.demoted") })
        {
            var legacy = new Snapshot { Chapter = 5 };
            legacy.Flags.UnionWith(new[] { "trickster", N + "returned", row.Item1, row.Item2 });
            Refresh(story, legacy);
            check(!Rules.Blocks(story.Relationships["nenio"], row.Item1, legacy), "q8a: matching old paid receipt rejected: " + row.Item1);
        }
    }
    static void WenduagCases(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var prep = S(E + "prepare");
        var state = new Snapshot { Chapter = 3, Hour = 10000, Area = Rules.NurahCapital,
            CrusadeResources = new System.Collections.Generic.Dictionary<string, int> { ["Finances"] = 350 } };
        state.Flags.UnionWith(prep.Requires.Where(k => !story.Derived.ContainsKey(k)));
        state.Flags.Add("trickster"); state.Flags.Add(E + "adapter_available");
        Refresh(story, state);
        var page = S("trickster.foresight.page");
        check(Rules.Available(story, page, state), "q8a: paid Shyka prerequisite unavailable");
        state = Program.Walk(page, state).First(s => s.Has("trickster.foresight.accepted"));
        state.Chapter = 4; Refresh(story, state);
        check(Rules.Available(story, prep, state), "q8a: echo preparation unavailable");
        state = Program.Walk(prep, state).First(s => s.Has(E + "ready"));
        // Native interruption and the observed original at its allocated pickup.
        state.Flags.UnionWith(new[] { "wenduag.abyss_fell", "wenduag.dead_any" });
        EchoObserve(story, state, "down");
        state.Flags.Add(E + "casualty_available"); state.SceneContacts.Add(E + "pickup");
        var pickup = S(E + "pickup");
        check(Rules.Available(story, pickup, state), "q8a: prepared pickup unavailable");
        state = Program.Walk(pickup, state).First(s => s.Has(E + "rescued"));
        state.Chapter = 5; state.Hour += 100; state.AvailableContacts.Add(pickup.ContactUnit!);
        EchoObserve(story, state, "arrived"); state.Flags.Add(E + "return_available");
        var returnScene = S(E + "return");
        check(Rules.Available(story, returnScene, state), "q8a: paid rescue did not reach its original's return");
        var outcomes = Program.Walk(returnScene, state);
        var departed = outcomes.First(s => s.Has(E + "departed"));
        EchoObserve(story, departed, "departed");
        check(!departed.Flags.Contains(W + "returned") && !departed.Flags.Contains(E + "returned"), "q8a: departure credited a second return");
        var returned = outcomes.First(s => s.Has(E + "returned"));
        EchoObserve(story, returned, "released");
        foreach (string suffix in new[] { "trial", "gate" })
        {
            returned.Hour += 100;
            var scene = S(W + "court." + suffix);
            check(Rules.Available(story, scene, returned), "q8a: echo courtship unavailable: " + suffix);
            returned = Program.Walk(scene, returned).First(s => s.Has(suffix == "trial" ? W + "proved" : W + "gate_seen"));
            EchoObserve(story, returned, "released");
        }
        returned.Hour += 100;
        var claim = S(W + "court.claim");
        check(Rules.Available(story, claim, returned), "q8a: returned original cannot answer the claim");
        var refused = Program.Walk(claim, returned).First(s => s.Has(W + "court.claim_refused"));
        EchoObserve(story, refused, "released");
        foreach (var row in new[] { (refused, W + "epilogue.refused", "released"), (departed, E + "epilogue.departed", "departed") })
        {
            var ending = S(row.Item2); var live = At(story, ending, row.Item1);
            EchoObserve(story, live, row.Item3);
            check(live.Has("wenduag.life.available") && Rules.Available(story, ending, live), "q8a: living closure lost its nonromantic ending: " + ending.Id);
            check(!Rules.RouteOpen(story.Relationships["wenduag"], live), "q8a: living closure reopened the romance");
            foreach (string key in new[] { W + "partner", W + "with_you", W + "late_committed", "wenduag.harem.eligible", "wenduag.harem.voice.pack" })
                check(!live.Has(key), "q8a: living closure retained romantic reward: " + key);
            foreach (string invalid in new[] { "missing", "dead", "corrupt", "duplicate", "mismatched", "legend" })
            {
                var lost = Program.Copy(live);
                if (invalid == "legend") lost.Flags.Add("legend");
                EchoObserve(story, lost, row.Item3, living: invalid != "missing" && invalid != "dead",
                    wellFormed: invalid != "corrupt" && invalid != "duplicate" && invalid != "mismatched");
                check(!lost.Has("wenduag.life.available") && !Rules.Available(story, ending, lost), "q8a: closure ending retained invalid original: " + invalid);
            }
        }
        // Legacy return -> a later current native death, with no echo observation.
        var legacy = new Snapshot { Chapter = 5 };
        legacy.Flags.UnionWith(new[] { "trickster", W + "returned", W + "primed" }); Refresh(story, legacy);
        check(Rules.RouteOpen(story.Relationships["wenduag"], legacy), "q8a: living old paid return requires a synthetic receipt");
        legacy.Flags.Add("wenduag.dead_any"); Refresh(story, legacy);
        check(legacy.Flags.Contains(W + "returned") && !legacy.Has(W + "returned") && !Rules.RouteOpen(story.Relationships["wenduag"], legacy),
            "q8a: generic legacy return proves life after a later native death");
        // Distinct nominated current-path copy of the native execution remains.
        legacy.Flags.Add("wenduag.killed"); Refresh(story, legacy);
        check(Rules.RouteOpen(story.Relationships["wenduag"], legacy), "q8a: nominated historical execution copy was invalidated");
        legacy.Flags.Add(E + "unavailable"); Refresh(story, legacy);
        check(!Rules.RouteOpen(story.Relationships["wenduag"], legacy), "q8a: earlier execution-copy return hid a saved actor loss");
    }
    internal static void Run(Story story, Action<bool, string> check)
    {
        if (!story.Relationships.ContainsKey("nenio") || !story.Relationships.ContainsKey("wenduag")) return;
        NenioCases(story, check); WenduagCases(story, check);
        Console.WriteLine("PASS: E-Q8-01 paid original restoration -> new death/native resurrection, living closure, paid echo -> refusal/departure, actor-loss negatives and legacy-copy distinction.");
    }
}
