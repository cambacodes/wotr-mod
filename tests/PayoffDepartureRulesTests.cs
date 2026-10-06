using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text.Json;
using Tirabade;

internal static class PayoffDepartureRulesTests
{
    // Synthetic native observations exercise production epoch ordering, rather
    // than game hours or hypothetical clearing of historical romance receipts.
    static Story Fixture(string woman, DepartureEpochSpec source)
    {
        string lost = source.Overrides.Keys.FirstOrDefault() ?? source.NativeClearReturns.Keys.FirstOrDefault() ?? source.Losses[0];
        string back = source.Overrides.TryGetValue(lost, out var nominated) ? nominated
            : source.NativeClearReturns.TryGetValue(lost, out nominated) ? nominated : source.Returns[0];
        var story = new Story();
        story.Relationships.Clear();
        story.Relationships[woman] = new Relationship { ClosedFlag = woman + ".closed",
            EpochUnavailableFlags = new[] { woman + ".epoch_unavailable" } };
        story.DepartureEpochs[woman] = new DepartureEpochSpec { Relationship = woman,
            Losses = source.Losses, Returns = source.Returns, Overrides = source.Overrides,
            NativeClearReturns = source.NativeClearReturns, UnavailableFlag = woman + ".epoch_unavailable" };
        story.Derived[woman + ".present_now"] = new[] { new[] { "availability.observed" } };
        story.DerivedForbids[woman + ".present_now"] = new[] { woman + ".epoch_unavailable" };
        story.Derived[woman + ".test.eligible"] = new[] { new[] { back } };
        story.DerivedOpenRoutes[woman + ".test.eligible"] = new[] { woman };
        story.Scenes.Add(new Scene { Id = woman + ".test.return", Relationship = woman,
            Nodes = new List<Node> { new Node { Id = "return", Choices = new List<Choice> {
                new Choice { Text = "Earn the existing return", Set = new[] { back } } } } } });
        return story;
    }

    static void Epochs(Story shipped, Action<bool, string> check)
    {
        int women = 0;
        foreach (var pair in shipped.DepartureEpochs.Where(p => p.Value.Returns.Length > 0))
        {
            women++;
            string woman = pair.Key;
            var spec = pair.Value;
            string loss = spec.Overrides.Keys.FirstOrDefault() ?? spec.NativeClearReturns.Keys.FirstOrDefault() ?? spec.Losses[0];
            string back = spec.Overrides.TryGetValue(loss, out var nominated) ? nominated
                : spec.NativeClearReturns.TryGetValue(loss, out nominated) ? nominated : spec.Returns[0];
            bool answersLoss = spec.Overrides.ContainsKey(loss) || spec.NativeClearReturns.ContainsKey(loss);
            var story = Fixture(woman, pair.Value);
            if (spec.Overrides.ContainsKey(loss))
            {
                var legacy = new Snapshot { Chapter = 5, Hour = 100 };
                legacy.Flags.UnionWith(new[] { loss, back });
                legacy.Times[back] = 10; legacy.Times[loss] = 20;
                Rules.Complete(story, legacy);
                check(!legacy.Has(woman + ".present_now"), "eng3-ab imported older return outran later departure: " + woman);
            }
            var state = new Snapshot { Chapter = 5, Hour = 100 };
            Rules.Complete(story, state);
            check(state.Has(woman + ".present_now"), "eng3-ab initially available: " + woman);
            var answer = story.Scenes[0].Nodes[0].Choices[0];
            check(Rules.ChoiceAvailable(answer, state), "eng3-ab earned-return choice: " + woman);
            state.Flags.UnionWith(answer.Set);
            Rules.RecordAvailabilityEvents(story, state, answer.Set);
            Rules.Complete(story, state);
            check(state.Has(woman + ".present_now") && state.Has(woman + ".test.eligible"), "eng3-ab returned control: " + woman);
            // A second departure in the SAME hour follows that return. An old
            // flag remains true; only the new event order changes availability.
            state.Flags.Add(loss);
            Rules.RecordAvailabilityEvents(story, state, new[] { loss });
            Rules.Complete(story, state);
            check(state.Has(back) && !state.Has(woman + ".present_now") && !state.Has(woman + ".test.eligible"),
                "eng3-ab return -> re-depart -> no return: " + woman);
            var options = new JsonSerializerOptions { IncludeFields = true };
            state = JsonSerializer.Deserialize<Snapshot>(JsonSerializer.Serialize(state, options), options)!;
            Rules.Complete(story, state);
            check(!state.Has(woman + ".present_now"), "eng3-ab reload resurrected historical return: " + woman);
            var letter = new Paragraph { Requires = new[] { woman + ".present_now" } };
            check(!Rules.ParagraphVisible(letter, state), "eng3-ab departed correspondence/payoff: " + woman);
            // Native resurrection observes a living body only after the current
            // corpse reader clears; historical authored losses may remain held.
            if (spec.NativeClearReturns.ContainsKey(loss)) state.Flags.Remove(loss);
            Rules.RecordAvailabilityEvents(story, state, new[] { back });
            Rules.Complete(story, state);
            check(state.Has(woman + ".present_now") == answersLoss, "eng3-ab nominated newer return: " + woman);
            if (!spec.NativeClearReturns.ContainsKey(loss))
            {
                state.Flags.Remove(loss); Rules.Complete(story, state);
                check(state.Has(woman + ".present_now") == answersLoss, "eng3-ab cleared historical loss must not invent a return: " + woman);
            }
        }
        check(women > 20, "eng3-ab return-device inventory incomplete");
    }

    static void CoarsePayoffs(Story story, Action<bool, string> check)
    {
        // Select the declared surfaces independently of their current gates:
        // removing a gate must not remove the scene from this negative walk.
        using var contracts = JsonDocument.Parse(File.ReadAllText("tools/payoff_contracts.json"));
        var surfaces = contracts.RootElement.GetProperty("routes").EnumerateObject()
            .SelectMany(route => route.Value.GetProperty("surfaces").EnumerateArray()
                .Select(surface => surface.GetProperty("scene").GetString()!)).ToHashSet();
        // The acquired harbour shares Nocticula's seat but has a separate
        // acceptance contract; its coarse agreement alone must stay out.
        var acquired = new Snapshot { Chapter = 6, Hour = 10000 };
        acquired.Flags.UnionWith(new[] { "trickster", "trickster.ever", "noct.acq.renewed_agreement",
            "trickster.lastcall.taken", "ending.trickster" });
        Rules.Complete(story, acquired);
        check(!acquired.Has("nocticula.acquisition.payoff.ordinary") && !acquired.Has("nocticula.harem.eligible"),
            "eng3-ab coarse acquired agreement earned Nocticula's shared seat");
        foreach (var pair in story.Relationships)
        {
            string key = pair.Key + ".payoff.ordinary";
            if (!story.Derived.ContainsKey(key)) continue;
            var state = new Snapshot { Chapter = 6, Hour = 10000 };
            state.Flags.UnionWith(new[] { "trickster", "trickster.ever", pair.Value.StartedFlag, pair.Value.CommittedFlag,
                pair.Key + ".trickster.primed", pair.Key + ".trickster.proposed", pair.Key + ".trickster.envoy" });
            // Include actual coarse proposal/envoy keys named by the audit,
            // plus the ending framework, so codas are tested in their host.
            if (pair.Key == "shamira") state.Flags.Add("shamira.trickster.game_proposed");
            if (pair.Key == "konomi") state.Flags.UnionWith(new[] { "konomi.trickster.cost.accredited", "konomi.trickster.rooms_kept" });
            if (pair.Key == "anevia") state.Flags.UnionWith(new[] { "anevia.trickster.gate_seen", "anevia.trickster.hand_taken" });
            state.Flags.UnionWith(new[] { "trickster.lastcall.taken", "ending.trickster" });
            Rules.Complete(story, state);
            check(!state.Has(key), "eng3-ab coarse commitment earned payoff: " + pair.Key);
            string partner = pair.Key + ".payoff.partner", late = pair.Key + ".trickster.late_committed";
            check(!state.Has(partner) && !state.Has(late), "eng3-ab coarse readiness earned late payoff: " + pair.Key);
            foreach (var entry in story.Books.Values.SelectMany(b => b.Entries).Where(e => e.Id.StartsWith("guest.", StringComparison.Ordinal)))
                check(!Rules.BookEntryVisible(entry, state), "eng3-ab coarse walk reached Guest List: " + entry.Id);
            foreach (var scene in story.Scenes.Where(s => surfaces.Contains(s.Id) || s.Id.EndsWith(".lastcall.call", StringComparison.Ordinal)))
            {
                state.Area = scene.Areas.FirstOrDefault() ?? "";
                check(!Rules.Available(story, scene, state), "eng3-ab coarse walk reached " + scene.Id);
            }
        }
    }

    static void ShippedDepartureConsumers(Story story, Action<bool, string> check)
    {
        using var contracts = JsonDocument.Parse(File.ReadAllText("tools/departure_contracts.json"));
        foreach (var woman in contracts.RootElement.GetProperty("women").EnumerateObject())
        {
            var epoch = story.DepartureEpochs[woman.Name];
            if (epoch.Returns.Length == 0) continue;
            int controls = 0;
            string back = epoch.Overrides.Values.FirstOrDefault() ?? epoch.Returns[0];
            string lost = woman.Name + ".returned_actor_lost";
            foreach (var surface in woman.Value.GetProperty("surfaces").EnumerateArray())
            {
                var scene = story.Scenes.Single(s => s.Id == surface.GetProperty("scene").GetString());
                JsonElement target = default;
                using var encoded = JsonDocument.Parse(JsonSerializer.Serialize(scene, new JsonSerializerOptions { IncludeFields = true }));
                target = encoded.RootElement;
                if (surface.TryGetProperty("node", out var nodeId))
                {
                    target = target.GetProperty("Nodes").EnumerateArray().Single(n => n.GetProperty("Id").GetString() == nodeId.GetString());
                    target = surface.TryGetProperty("choice", out var answer)
                        ? target.GetProperty("Choices")[answer.GetInt32()]
                        : target.GetProperty("Paragraphs")[surface.GetProperty("paragraph").GetInt32()];
                }
                // Predicate checkpoints provide the consumer's earlier earned
                // receipts. The new loss is recorded after its existing return;
                // these fixtures do not claim to exercise a return producer.
                var state = L07World.Seed(story, scene);
                foreach (var key in target.GetProperty("Requires").EnumerateArray())
                    HouseholdTests.Earn(story, state, key.GetString()!);
                HouseholdTests.Earn(story, state, back);
                Rules.Complete(story, state); // observe fixture losses before the later earned return
                Rules.RecordAvailabilityEvents(story, state,
                    epoch.ReturnTriggers.TryGetValue(back, out var receipts) ? receipts : new[] { back });
                Rules.Complete(story, state);
                bool Visible()
                {
                    if (!surface.TryGetProperty("node", out var id)) return Rules.Available(story, scene, state);
                    var node = scene.Nodes.Single(n => n.Id == id.GetString());
                    return surface.TryGetProperty("choice", out var choice)
                        ? Rules.ChoiceAvailable(node.Choices[choice.GetInt32()], state)
                        : Rules.ParagraphVisible(node.Paragraphs[surface.GetProperty("paragraph").GetInt32()], state);
                }
                if (Visible()) controls++;
                state.Flags.Add(lost);
                Rules.RecordAvailabilityEvents(story, state, new[] { lost });
                Rules.Complete(story, state);
                check(!Visible(), "eng3-ab shipped consumer reused historical return after actor loss: " + woman.Name + "/" + scene.Id);
            }
            check(controls > 0, "eng3-ab shipped departure negatives have no available control: " + woman.Name);
        }
    }

    static void SharedSeatOrder(Action<bool, string> check)
    {
        // Shared route closure is a composite: complete its two current
        // availability inputs before the route-dependent eligibility reader.
        var story = new Story();
        story.Relationships.Clear();
        story.Relationships["pair"] = new Relationship { ClosedFlag = "pair.closed",
            EpochUnavailableFlags = new[] { "pair.epoch_unavailable" } };
        story.Derived["pair.test.eligible"] = new[] { new[] { "pair.accepted" } };
        story.DerivedOpenRoutes["pair.test.eligible"] = new[] { "pair" };
        story.Derived["pair.epoch_unavailable"] = new[] { new[] { "first.epoch_unavailable", "second.epoch_unavailable" } };
        foreach (string woman in new[] { "first", "second" })
            story.DepartureEpochs[woman] = new DepartureEpochSpec { Relationship = "pair",
                Losses = new[] { woman + ".departed" }, Returns = new[] { woman + ".returned" },
                Overrides = new Dictionary<string, string> { [woman + ".departed"] = woman + ".returned" },
                UnavailableFlag = woman + ".epoch_unavailable" };
        var state = new Snapshot();
        state.Flags.UnionWith(new[] { "pair.accepted", "first.returned", "second.returned" });
        Rules.Complete(story, state);
        check(state.Has("pair.test.eligible"), "eng3-ab shared seat control unavailable");
        state.Flags.Add("first.departed");
        Rules.RecordAvailabilityEvents(story, state, new[] { "first.departed" });
        Rules.Complete(story, state);
        check(state.Has("pair.test.eligible"), "eng3-ab one departure removed the independent seat");
        state.Flags.Add("second.departed");
        Rules.RecordAvailabilityEvents(story, state, new[] { "second.departed" });
        Rules.Complete(story, state);
        check(state.Has("pair.epoch_unavailable") && !state.Has("pair.test.eligible"),
            "eng3-ab shared eligibility was computed before both departures");
    }

    static void LaterFriendship(Story story, Action<bool, string> check)
    {
        var future = story.Scenes.Single(s => s.Id == "arsinoe_what_she_asks");
        var roof = story.Scenes.Single(s => s.Id == "arsinoe_roofs");
        // The older acceptance and first cart are fixture history; both later
        // friendship decisions below come from selectable authored choices.
        var accepted = L07World.Seed(story, roof, "trickster", "arsinoe.trickster.late_accepted",
            "arsinoe.continuation_kept", "arsinoe_the_first_cart");
        check(accepted.Has("arsinoe.trickster.late_committed") && Rules.Available(story, roof, accepted),
            "eng3-ab accepted Arsinoe control unavailable");
        var packed = L07World.Play(story, roof, accepted).First(s => s.Has("arsinoe.friendship"));
        var before = L07World.Move(story, future, packed);
        before.AvailableContacts.Add(future.ContactUnit!);
        check(Rules.Available(story, future, before), "eng3-ab later Arsinoe future discussion unavailable");
        var friend = L07World.Play(story, future, before).First(s => s.Has("arsinoe.campaign_friend"));
        friend.Chapter = 6;
        friend.Flags.UnionWith(new[] { "trickster.lastcall.taken", "ending.trickster" });
        L07World.Refresh(story, friend);
        check(!friend.Has("arsinoe.trickster.late_committed") && !friend.Has("arsinoe.harem.eligible"),
            "eng3-ab actual later friendship preserves earlier romance intent");
        check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "arsinoe.lastcall.page"), friend),
            "eng3-ab actual later friendship reaches Last Call");
        check(!Rules.BookEntryVisible(story.Books["trickster.ledger"].Entries.Single(e => e.Id == "guest.arsinoe"), friend),
            "eng3-ab actual later friendship reaches Guest List");
    }

    static void PairedNativeReturnThenDeparture(Story story, Action<bool, string> check)
    {
        foreach (bool committed in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 6 };
            state.Flags.UnionWith(new[] { "trickster", "irabeth_dead", "anevia_gone",
                "irabeth.trickster.returned", "anevia.trickster.returned" });
            if (committed) state.Flags.UnionWith(new[] { "anevia.committed",
                "anevia.trickster.gate_seen", "anevia.trickster.terms_kept" });
            Rules.Complete(story, state);
            string id = "anevia.trickster.epilogue.native_tirabade_" + (committed ? "together" : "back");
            var scene = story.Scenes.Single(s => s.Id == id);
            check(Rules.Available(story, scene, state), "eng3-ab actual paired native return control: " + id);
            state.Flags.Add("irabeth_gone");
            Rules.RecordAvailabilityEvents(story, state, new[] { "irabeth_gone" });
            Rules.Complete(story, state);
            check(state.Has("irabeth.trickster.returned") && !Rules.Available(story, scene, state),
                "eng3-ab paired native slide reused Irabeth's historical return: " + id);
        }
    }

    static void QualifiedReturnHistory(Action<bool, string> check)
    {
        const string woman = "qualified", back = "qualified.return", paid = "qualified.paid", loss = "qualified.dead";
        var source = new DepartureEpochSpec { Losses = new[] { loss }, Returns = new[] { back },
            Overrides = new Dictionary<string,string> { [loss] = back } };
        var story = Fixture(woman, source);
        story.DepartureEpochs[woman].ReturnTriggers[back] = new[] { paid };
        story.Derived[back] = new[] { new[] { paid, "qualified.witness" } };
        var state = new Snapshot { Chapter = 5 };
        state.Flags.Add(paid); Rules.Complete(story, state);
        state.Flags.UnionWith(new[] { loss, "qualified.witness" });
        Rules.RecordAvailabilityEvents(story, state, new[] { loss }); Rules.Complete(story, state);
        check(!state.Has(woman + ".present_now"), "eng3-ab later death evidence refreshed an older paid return");
        Rules.RecordAvailabilityEvents(story, state, new[] { paid }); Rules.Complete(story, state);
        check(state.Has(woman + ".present_now"), "eng3-ab actual newer return receipt unavailable");
        Rules.RecordAvailabilityEvents(story, state, new[] { loss }); Rules.Complete(story, state);
        state.Flags.Remove("qualified.witness"); Rules.Complete(story, state);
        state.Flags.Add("qualified.witness"); Rules.Complete(story, state);
        check(!state.Has(woman + ".present_now"), "eng3-ab liveness qualifier recycled a historical return");
    }

    static void SouthernAbsenceLife(Story story, Action<bool, string> check)
    {
        foreach (bool historicalReturn in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 3, Hour = 100 };
            state.Flags.UnionWith(new[] { "trickster", "chapter_later", "irabeth_gone" });
            Rules.Complete(story, state);
            check(state.Has("irabeth.absence.alive") && !state.Has("irabeth.present_now"),
                "eng3-ab native southern absence confused living away with a Drezen return");
            if (historicalReturn)
            {
                state.Flags.Add("irabeth.trickster.returned");
                Rules.RecordAvailabilityEvents(story, state, new[] { "irabeth.trickster.returned" });
                Rules.Complete(story, state);
            }
            state.Flags.Add("irabeth_dead");
            Rules.RecordAvailabilityEvents(story, state, new[] { "irabeth_dead" });
            Rules.Complete(story, state);
            check(!state.Has("irabeth.absence.alive"),
                "eng3-ab southern absence report reused life before a later death");
        }
    }

    static void LivingCamellia(Story story, Action<bool, string> check)
    {
        var scene = story.Scenes.Single(s => s.Id == "camellia.trickster.returned.test_alive");
        // Named terms are earlier fixture history; acceptance below comes
        // from her actual living commitment answers, with no death or return.
        var before = L07World.Seed(story, scene, "trickster");
        check(!before.Has("camellia.trickster.death_observed") && !before.Has("camellia.trickster.returned"),
            "eng3-ab living Camellia fixture fabricated death");
        check(Rules.Available(story, scene, before), "eng3-ab living Camellia invitation unavailable");
        var accepted = L07World.Play(story, scene, before).First(s => s.Has("camellia.committed"));
        check(accepted.Has("camellia.payoff.ordinary") && !accepted.Has("camellia.trickster.death_observed"),
            "eng3-ab living Camellia acceptance incorrectly requires a coffin");
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        if (story.DepartureEpochs.Count == 0) return;
        Epochs(story, check);
        CoarsePayoffs(story, check);
        SharedSeatOrder(check);
        ShippedDepartureConsumers(story, check);
        LaterFriendship(story, check);
        LivingCamellia(story, check);
        SouthernAbsenceLife(story, check);
        PairedNativeReturnThenDeparture(story, check);
        QualifiedReturnHistory(check);
        Console.WriteLine("PASS: eng3-ab coarse payoff negatives; every return-device woman's same-hour return/departure/reload epoch order.");
    }
}
