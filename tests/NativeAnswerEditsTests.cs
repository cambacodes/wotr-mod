// eng7-f1: earned history and current-path rules for native answer presentation.
using System;
using System.Linq;
using Tirabade;

internal static class NativeAnswerEditsTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        check(story.NativeAnswerEdits.Count == 3, "Kiana findings 020/021/027 must register three answer edits");
        foreach (var pair in story.NativeAnswerEdits)
        foreach (string paid in new[] { "kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back" })
        {
            var world = new Snapshot { Chapter = 5 };
            world.Flags.Add(paid);
            check(!Rules.NativeAnswerHolds(story, pair.Key, world), "Paid answer edit fired off Trickster");
            world.Flags.Add("trickster.now");
            check(Rules.NativeAnswerHolds(story, pair.Key, world), "Paid Trickster answer keeps obsolete rescue text");
            world.Flags.Add(Rules.DegradedPrefix + "kiana");
            check(!Rules.NativeAnswerHolds(story, pair.Key, world), "Degraded route changed a native answer");
            world.Flags.Clear();
            world.Flags.UnionWith(new[] { "trickster.now", "kiana.committed", "kiana.trickster.returned", "foresight.page_taken" });
            check(!Rules.NativeAnswerHolds(story, pair.Key, world), "Individual return/commitment/page gave the guests a free recovery");
            world.Flags.UnionWith(new[] { "trickster.ever", "legend", paid });
            world.Flags.Remove("trickster.now");
            check(!Rules.NativeAnswerHolds(story, pair.Key, world), "Past Trickster answer edit survived path conversion");
        }
        var spec = story.NativeAnswerEdits.First().Value;
        var original = spec.When;
        foreach (var wrong in new[] { new[] { "trickster.ever", "kiana.trickster.guests_ransomed" },
                                     new[] { "trickster.now", "kiana.committed" } })
        {
            spec.When = new[] { wrong };
            bool refused = false;
            try { Rules.Validate(story); } catch (InvalidOperationException) { refused = true; }
            check(refused, "Rules accepted an answer edit without current path and paid recovery");
        }
        spec.When = original;
    }
}
