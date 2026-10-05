using System;
using System.Collections.Generic;
using Tirabade;

internal static class WorldBuildCacheTests
{
    internal static void Run(Action<bool, string> check)
    {
        var story = new Story();
        story.Derived["earned"] = new[] { new[] { "paid" } };
        var cache = new WorldBuildCache(story);
        var paid = new Snapshot { Chapter = 3, CrusadeResources = new Dictionary<string, int> { ["Finances"] = 100 } };
        paid.Flags.Add("paid");
        var repeat = Program.Copy(paid);
        cache.Complete(paid);
        var invitation = new Choice { Requires = new[] { "earned" } };
        check(Rules.ChoiceAvailable(invitation, paid), "Completed paid world cannot take its earned answer");
        paid.Flags.Clear(); // changing a caller's world must not poison a cached result
        cache.Complete(repeat);
        check(Rules.ChoiceAvailable(invitation, repeat), "Caller mutation corrupted the shared completed world");
        check(cache.Builds == 1 && cache.Hits == 1, "Equal worlds rebuilt the same dependency graph");
        var unearned = new Snapshot { Chapter = 3, CrusadeResources = new Dictionary<string, int> { ["Finances"] = 100 } };
        cache.Complete(unearned);
        check(!Rules.ChoiceAvailable(invitation, unearned), "Paid flags leaked into an unearned world");
        var poor = new Snapshot { Chapter = 3, CrusadeResources = new Dictionary<string, int> { ["Finances"] = 0 } };
        poor.Flags.Add("paid");
        cache.Complete(poor);
        var bargain = new Choice { Crusade = new CrusadeChoice { Resource = "Finances", Amount = -50 } };
        check(!Rules.ChoiceAvailable(bargain, poor), "Completed world cache restores another history's money");
        var changedStory = new Story();
        changedStory.Derived["earned"] = new[] { new[] { "other_receipt" } };
        var changed = new WorldBuildCache(changedStory);
        var missing = new Snapshot { Chapter = 3 }; missing.Flags.Add("paid");
        changed.Complete(missing);
        check(!Rules.ChoiceAvailable(invitation, missing), "Completed worlds were shared across different stories");
    }
}
