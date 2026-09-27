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
        Console.WriteLine("PASS: ER-3 epilogue pages follow their native anchor in authored order; a missing anchor appends.");
    }
}
