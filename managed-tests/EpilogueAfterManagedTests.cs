using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Tirabade;

// ER-3: Main.InsertEpiloguePage places anchored pages right after their native anchor, in authored order.
internal static class EpilogueAfterManagedTests
{
    public static void Run(Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        BlueprintCueBaseReference Ref(string name)
        {
            var reference = new BlueprintCueBaseReference();
            typeof(BlueprintReferenceBase).GetField("deserializedGuid", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)!
                .SetValue(reference, id("fixture.er3." + name));
            return reference;
        }
        var insert = typeof(Main).GetMethod("InsertEpiloguePage", BindingFlags.NonPublic | BindingFlags.Static)!;
        bool Insert(List<BlueprintCueBaseReference> cues, BlueprintCueBaseReference page, string? after) =>
            (bool)insert.Invoke(null, new object?[] { cues, page, after })!;
        BlueprintCueBaseReference a = Ref("a"), anchor = Ref("anchor"), c = Ref("c"), p1 = Ref("p1"), p2 = Ref("p2"), p3 = Ref("p3"), p4 = Ref("p4");
        var cues = new List<BlueprintCueBaseReference> { a, anchor, c };
        string anchorGuid = anchor.Guid.ToString();
        check(Insert(cues, p1, anchorGuid) && Insert(cues, p2, anchorGuid), "Anchored insert reported failure.");
        check(!Insert(cues, p3, id("fixture.er3.missing").ToString()), "A missing anchor was reported as placed.");
        check(Insert(cues, p4, null), "An unanchored append reported failure.");
        check(cues.SequenceEqual(new[] { a, anchor, p1, p2, c, p3, p4 }), "Anchored pages are out of order: "
            + string.Join(",", cues.Select(r => r == a ? "a" : r == anchor ? "anchor" : r == c ? "c" : r == p1 ? "p1" : r == p2 ? "p2" : r == p3 ? "p3" : "p4")));
        // Regression: Areelu-style reports precede the page they follow in Story.Scenes.
        // Include a chained forward reference, sibling pages, and both native anchors.
        Scene Page(string name, string after) => new Scene { Id = name, Owner = "Epilogue",
            EpilogueSequence = "PlayerFinalChoice", EpilogueAfter = after,
            Nodes = new List<Tirabade.Node> { new Tirabade.Node { Id = "start" } } };
        var late = Page("late", anchorGuid);
        var first = Page("first", "scene:late");
        var second = Page("second", "scene:late");
        var chain = Page("chain", "scene:first");
        var other = Page("other", c.Guid.ToString());
        var fixture = new Story { Scenes = new List<Scene> { chain, first, second, other, late } };
        var sourceOrder = fixture.Scenes.ToArray();
        var order = Rules.EpilogueInsertionOrder(fixture);
        check(order.SequenceEqual(new[] { other, late, first, chain, second }), "Forward scene anchors were not scheduled before their reports.");
        check(fixture.Scenes.SequenceEqual(sourceOrder), "Scheduling reordered serialized scene identities.");
        var scheduled = new List<BlueprintCueBaseReference> { a, anchor, c };
        var refs = fixture.Scenes.ToDictionary(s => s.Id, s => Ref(s.Id));
        string ResolvePage(string name) => refs[fixture.Scenes.Single(s => name == "page." + s.Id + ".start").Id].Guid.ToString();
        foreach (var scene in order)
            check(Insert(scheduled, refs[scene.Id], Rules.EpilogueAnchor(fixture, scene.EpilogueAfter, ResolvePage)),
                "Scheduled scene anchor was missing: " + scene.Id);
        check(scheduled.SequenceEqual(new[] { a, anchor, refs["late"], refs["first"], refs["chain"], refs["second"], c, refs["other"] }),
            "Forward/chained epilogue reports misplaced or native members moved.");
        var earlierSibling = Page("earlier", anchorGuid);
        var siblings = new Story { Scenes = new List<Scene> { first, earlierSibling, late } };
        check(Rules.EpilogueInsertionOrder(siblings).SequenceEqual(new[] { earlierSibling, late, first }),
            "Scheduling a forward dependency moved it ahead of an earlier sibling on the same native anchor.");
        late.EpilogueAfter = "scene:chain";
        bool cyclic = false;
        try { Rules.EpilogueInsertionOrder(fixture); } catch (InvalidOperationException) { cyclic = true; }
        check(cyclic, "Cyclic anchors must fail scheduling.");
        Console.WriteLine("PASS: ER-3/E14a native and forward scene anchors resolve before insertion; a missing anchor appends.");
    }
}
