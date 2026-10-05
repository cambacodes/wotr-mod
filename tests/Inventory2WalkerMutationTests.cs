using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8f: executable sentinels distinguish exact edges from identical final effects.
internal static class Inventory2WalkerMutationTests
{
    private static Scene Clone(Scene scene) => JsonSerializer.Deserialize<Scene>(JsonSerializer.Serialize(scene,
        new JsonSerializerOptions { IncludeFields = true }), new JsonSerializerOptions { IncludeFields = true })!;

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        // Predicate fixtures for edge/payment mutations; these do not certify native placement or return provenance.
        Snapshot Fixture(Scene scene, params string[] flags)
        {
            var state = new Snapshot { Chapter = 5, Hour = 5000, Area = scene.Areas.FirstOrDefault() ?? "" };
            state.Flags.UnionWith(scene.Requires.Concat(flags));
            foreach (var flag in state.Flags) state.Times[flag] = 0;
            Rules.Complete(story, state);
            return state;
        }
        var camellia = S("camellia.trickster.killed.performance");
        var cam = Fixture(camellia, "trickster", "trickster.ever", "camellia.trickster.primed", "camellia.trickster.raised");
        check(Program.WalkVia(camellia, cam, "gallows", 0).Count > 0
            && Program.WalkVia(camellia, cam, "stones", 0).Count > 0
            && Program.WalkVia(camellia, cam, "unsigned", 0).Count > 0
            && Program.WalkVia(camellia, cam, "unsigned", 0).All(w => w.Has("camellia.closed")),
            "eng8-q8f: Camellia named gallows/stones/refusal traversals");
        var sibling = Clone(camellia);
        sibling.Nodes.Single(n => n.Id == "fill").Choices[1].Next = "gallows";
        check(Program.Walk(sibling, cam).Any(w => w.Has("camellia.trickster.cost.grave_filled"))
            && Program.WalkVia(sibling, cam, "stones", 0).Count == 0,
            "eng8-q8f: same grave-filled effects must not certify the stones node");

        var nenio = S("nenio.trickster.taken.riddle");
        var fox = Fixture(nenio, "trickster", "trickster.ever", "nenio.asked_to_leave");
        check(Program.WalkVia(nenio, fox, "told", 0).Count > 0
            && Program.WalkVia(nenio, fox, "lost", 0).Count > 0
            && Program.WalkVia(nenio, fox, "start", 3).Count > 0
            && Program.WalkVia(nenio, fox, "start", 3).All(w => !w.Has("nenio.trickster.riddle_declined")),
            "eng8-q8f: Nenio told/check-failure/zero-effect exact branches");
        var noTold = Clone(nenio);
        noTold.Nodes.Single(n => n.Id == "stake").Choices[1].Next = "lost";
        check(Program.Walk(noTold, fox).Any(w => w.Has("nenio.trickster.riddle_declined"))
            && Program.WalkVia(noTold, fox, "told", 0).Count == 0,
            "eng8-q8f: shared declined flag must not certify the told node");
        var noLost = Clone(nenio);
        noLost.Nodes.Single(n => n.Id == "tangled_her").Choices[0].Check!.Failure = "told";
        check(Program.WalkVia(noLost, fox, "lost", 0).Count == 0,
            "eng8-q8f: a rerouted failed check cannot certify lost");
        var blockedZero = Clone(nenio);
        blockedZero.Nodes[0].Choices[3].Requires = new[] { "sentinel.absent" };
        check(Program.Walk(blockedZero, fox).Count > 0 && Program.WalkVia(blockedZero, fox, "start", 3).Count == 0,
            "eng8-q8f: an unavailable empty-Set answer cannot borrow a sibling completion");

        var late = S("horzalah.trickster.late.at_night");
        var payment = late.Nodes.Single(n => n.Id == "no_priest").Choices[0].Crusade!;
        foreach (int? balance in new int?[] { 100, 99, 0, null })
        {
            var state = Fixture(late, "trickster", "trickster.ever", "horzalah.trickster.refused");
            state.CrusadeResources = balance == null ? null : new Dictionary<string, int> { [payment.Resource] = balance.Value };
            var paid = Program.WalkVia(late, state, "no_priest", 0);
            check((paid.Count > 0) == (balance >= 100), "eng8-q8f: production Horzalah affordability " + balance);
            if (balance >= 100)
                check(paid.All(w => w.CrusadeResources![payment.Resource] == balance - 100 && w.Has(late.Id)
                    && w.Has("horzalah.trickster.cost.ear")) && state.CrusadeResources![payment.Resource] == balance,
                    "eng8-q8f: paid cut must debit exactly once without mutating the input");
            else
                check(Program.Walk(late, state).Any(w => !w.Has(late.Id) && !w.Has("horzalah.trickster.primed")),
                    "eng8-q8f: generated insufficient-funds exit aborts before paid outcome/completion");
        }
        var noResource = Fixture(late, "trickster", "trickster.ever", "horzalah.trickster.refused");
        noResource.CrusadeResources = new Dictionary<string, int> { ["Finances"] = 1000 };
        check(Program.WalkVia(late, noResource, "no_priest", 0).Count == 0,
            "eng8-q8f: an unrelated resource balance cannot fund the late cut");
        // Synthetic liability distinguishes entry processing from choice effects and proves abort timing.
        var liability = new Scene { Id = "sentinel.payment", Nodes = new List<Node> {
            new Node { Id = "payment", EnterSet = new[] { "sentinel.incurred" }, Choices = new List<Choice> {
                new Choice { Set = new[] { "sentinel.reward" }, Crusade = new CrusadeChoice { Resource = "Favors", Amount = -100 } } } } } };
        var missing = Program.Walk(liability, new Snapshot { Chapter = 5 }).Single();
        check(missing.Has("sentinel.incurred") && !missing.Has("sentinel.reward") && !missing.Has(liability.Id),
            "eng8-q8f: EnterNode precedes the generated payment exit");
        var funded = Program.WalkVia(liability, new Snapshot { Chapter = 5,
            CrusadeResources = new Dictionary<string, int> { ["Favors"] = 100 } }, "payment", 0).Single();
        check(funded.Has("sentinel.incurred") && funded.Has("sentinel.reward") && funded.CrusadeResources!["Favors"] == 0,
            "eng8-q8f: entry, availability and debit sentinels");
        Console.WriteLine("PASS: eng8-q8f exact-branch/payment mutations");
    }
}
