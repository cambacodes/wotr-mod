using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using Tirabade;

// Paragraphs have no saved ID. Their ordered slot is the structural identity;
// node, answer and book-entry identities use the shipped IDs and indices.
// This helper never reads localization or prose.
internal static class SurfaceIds
{
    private static readonly ConditionalWeakTable<Story, Dictionary<object, string>> Tables = new();

    private static Dictionary<object, string> Index(Story story)
    {
        var result = new Dictionary<object, string>(ReferenceEqualityComparer.Instance);
        foreach (var scene in story.Scenes)
            foreach (var node in scene.Nodes)
            {
                string id = scene.Id + "/" + node.Id;
                result[node] = "[" + id + "]";
                for (int i = 0; i < node.Choices.Count; i++) result[node.Choices[i]] = "[" + id + "/choice/" + i + "]";
                for (int i = 0; i < node.Paragraphs.Count; i++) result[node.Paragraphs[i]] = "[" + id + "/paragraph/" + i + "]";
            }
        foreach (var book in story.Books)
            foreach (var entry in book.Value.Entries)
            {
                string id = "book/" + book.Key + "/" + entry.Id;
                result[entry] = "[" + id + "]";
                for (int i = 0; i < entry.Lines.Count; i++) result[entry.Lines[i]] = "[" + id + "/line/" + i + "]";
            }
        return result;
    }

    internal static string Of(Story story, object surface) => Tables.GetValue(story, Index)[surface];

    // A callback can appear in several sibling scenes. Match any explicit slot,
    // with delimiters so paragraph 1 cannot accidentally match paragraph 10.
    internal static bool Has(string visible, string slots) => Count(visible, slots) != 0;
    internal static bool Has(IEnumerable<string> visible, string slots) => visible.Any(v => Has(v, slots));
    internal static int Count(string visible, string slots) => slots.Split(']', StringSplitOptions.RemoveEmptyEntries)
        .Select(s => s + "]").Count(s => visible.Contains(s, StringComparison.Ordinal));
}
