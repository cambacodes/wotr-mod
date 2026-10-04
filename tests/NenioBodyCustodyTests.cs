using System;
using System.Linq;
using System.Text.Json;
using Tirabade;

// E-Q7-25: the current contract restores the retained original; it no longer recreates it.
// RecoveryAttempt is production code. These are checkpoint/rules fixtures, not Unity save tests.
internal static class NenioBodyCustodyTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string P = "nenio.trickster.";
        var price = story.Scenes.Single(s => s.Id == P + "dead.the_price");
        var recreation = story.Scenes.Single(s => s.Id == P + "dead.the_price_recreated");
        Snapshot World(params string[] flags)
        {
            var state = new Snapshot { Chapter = 5, Hour = 10000, Area = Rules.NurahCapital };
            state.Flags.UnionWith(flags);
            Rules.Complete(story, state);
            foreach (string flag in state.Flags) state.Times[flag] = 0;
            return state;
        }
        var dead = World("trickster", "nenio.dead", "revive.nenio.available");
        check(Rules.Available(story, price, dead) && !Rules.Available(story, recreation, dead),
            "E-Q7-25: a retained original was offered recreation instead of restoration");
        check(price.Recovery == "nenio" && story.Revivals["nenio"].Unit == "1b893f7cf2b150e4f8bc2b3c389ba71d",
            "E-Q7-25: restoration lost its original companion binding");
        var returned = price.Nodes.SelectMany(n => n.Choices).Where(c => c.Set.Contains(P + "returned")).ToArray();
        check(returned.Length == 1 && returned[0].Revive == "nenio" && !returned[0].Set.Contains(P + "cost.recreated"),
            "E-Q7-25: a retained-body return bypasses native resurrection or creates a visitor");
        check(!price.Nodes.SelectMany(n => n.Choices).Any(c => c.Set.Contains(P + "cost.recreated")),
            "E-Q7-25: an old recreation choice remains enabled on the retained-body page");
        var savedForbids = recreation.Forbids;
        try
        {
            recreation.Forbids = savedForbids.Where(f => f != P + "body_kept").ToArray();
            check(Rules.Available(story, recreation, dead),
                "E-Q7-25: mutation fixture did not detect removal of retained-body recreation exclusion");
        }
        finally { recreation.Forbids = savedForbids; }
        var savedRevive = returned[0].Revive;
        try
        {
            returned[0].Revive = null;
            check(!price.Nodes.SelectMany(n => n.Choices).Where(c => c.Set.Contains(P + "returned")).All(c => c.Revive == "nenio"),
                "E-Q7-25: return contract cannot detect an omitted original-restoration action");
        }
        finally { returned[0].Revive = savedRevive; }
        var refusal = Program.WalkVia(price, dead, "terms", 1);
        check(refusal.Count > 0 && refusal.All(s => s.Has(P + "let_rest") && !s.Has(P + "returned")),
            "E-Q7-25: refusal granted a return");
        foreach (string blocker in new[] { "nenio.closed", "trickster.failed" })
            check(!Rules.Available(story, price, World("trickster", "nenio.dead", "revive.nenio.available", blocker)),
                "E-Q7-25: original restoration ignored closure/path: " + blocker);
        foreach (string path in new[] { "angel", "legend", "dragon", "swarm" })
            check(!Rules.Available(story, price, World(path, "trickster.ever", "nenio.dead", "revive.nenio.available")),
                "E-Q7-25: off-path restoration opened: " + path);
        check(!Rules.Available(story, price, World("nenio.dead", "revive.nenio.available"))
            && !Rules.Available(story, price, World("trickster", "nenio.dead")),
            "E-Q7-25: off-path or missing-original history can restore Nenio");

        var options = new JsonSerializerOptions { IncludeFields = true };
        T Reload<T>(T value) => JsonSerializer.Deserialize<T>(JsonSerializer.Serialize(value, options), options)!;
        var attempt = new RecoveryAttempt { UnitId = "retained-nenio", Roster = 2, SceneId = price.Id,
            ChoiceJson = JsonSerializer.Serialize(returned[0], options) };
        var native = new RecoveryStatus { UnitId = attempt.UnitId, Roster = attempt.Roster, Eligible = true, Dead = true };
        int calls = 0;
        // Native mutation followed by an exception must withhold progress, then resume without a second resurrection.
        bool restored = attempt.TryApply(() => native, () => {
            calls++; native.Dead = false; native.Conscious = true; throw new Exception("after native restoration");
        }, out _);
        check(!restored && calls == 1, "E-Q7-25: interrupted restoration credited return");
        attempt = Reload(attempt); native = Reload(native);
        check(attempt.TryApply(() => native, () => calls++, out _) && calls == 1,
            "E-Q7-25: reload repeated restoration of a living original");
        native.UnitId = "visitor-nenio";
        check(!attempt.TryApply(() => native, () => calls++, out _) && calls == 1,
            "E-Q7-25: a visitor received the original's restoration credit");
        native.UnitId = attempt.UnitId; native.Eligible = false;
        check(!attempt.TryApply(() => native, () => calls++, out _), "E-Q7-25: missing/duplicate original was restored");
        native.Eligible = true; native.Roster++;
        check(!attempt.TryApply(() => native, () => calls++, out _), "E-Q7-25: changed companion roster received credit");
        native.Roster = attempt.Roster; native.Conscious = false;
        check(!attempt.TryApply(() => native, () => calls++, out _) && calls == 1,
            "E-Q7-25: unconscious partial recovery received credit or another resurrection");
        Console.WriteLine("PASS: E-Q7-25 retained-original restoration contract and checkpoint reload; Unity equipment/selectors require Windows verification.");
    }
}
