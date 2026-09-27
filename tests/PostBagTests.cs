using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E8 (TT-09, ER-4): a rest delivers a post bag of up to PostBagSize letters from distinct rotation keys.
internal static class PostBagTests
{
    private static Scene Letter(string rel, int i, int maxChapter = 5) => new Scene
    {
        Id = rel + ".letter" + i, Title = "Letter", Owner = "Memory", Relationship = rel, Remote = true, MinChapter = 3,
        MaxChapter = maxChapter, Requires = i == 0 ? Array.Empty<string>() : new[] { rel + ".letter" + (i - 1) },
        Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
    };

    private static Story Roster(int count)
    {
        var story = new Story();
        story.Relationships.Clear();
        for (int r = 0; r < count; r++)
        {
            string rel = "rel" + r;
            story.Relationships[rel] = new Relationship { Title = rel, StartedFlag = rel + ".started", ClosedFlag = rel + ".closed", CommittedFlag = rel + ".committed" };
            for (int i = 0; i < 3; i++) story.Scenes.Add(Letter(rel, i, r == count - 1 ? 3 : 5));
        }
        return story;
    }

    internal static void Run(Action<bool, string> check)
    {
        // 13 waiting relationships are all served within ceil(13/3) = 5 rests.
        const int count = 13;
        var story = Roster(count);
        Rules.Validate(story);
        check(story.PostBagSize == 3 && story.QueueCapPerRelationship == 2, "Post-bag defaults changed.");
        var state = new Snapshot { Chapter = 3, Hour = 1000 };
        var served = new Dictionary<string, int>();
        var bag = new PostBag();
        var firstLetters = new HashSet<string>();
        int rests = 0;
        while (firstLetters.Count < count && rests < 20)
        {
            rests++;
            bag.Fill(story, state, served, story.PostBagSize);
            check(bag.Queue.Count <= story.PostBagSize, "A bag exceeded PostBagSize.");
            check(bag.Queue.Select(s => Rules.RotationKey(story, s.Relationship)).Distinct().Count() == bag.Queue.Count, "A bag repeated a rotation key.");
            // The letters chain: each read letter is followed by the next one while no dialog is open.
            for (var scene = bag.Next(story, state); scene != null; scene = bag.Next(story, state))
            {
                if (scene.Id.EndsWith(".letter0", StringComparison.Ordinal)) firstLetters.Add(scene.Relationship);
                served[scene.Relationship] = state.Hour;
                state.Flags.Add(scene.Id);
                state.Times[scene.Id] = state.Hour;
            }
            state.Hour += 16;
        }
        check(firstLetters.Count == count && rests == (count + 2) / 3, "13 relationships were not all served in ceil(13/3) rests: " + rests);

        // Urgency: the soonest-closing window goes first; the bag itself is in story list order.
        var fresh = new Snapshot { Chapter = 3, Hour = 1000 };
        var first = Rules.NextRemoteBag(story, fresh, new Dictionary<string, int>(), 3);
        check(first.Count == 3 && first.Any(s => s.Relationship == "rel12"), "The soonest-closing relationship was left out of the first bag.");
        check(first.Select(s => story.Scenes.IndexOf(s)).SequenceEqual(first.Select(s => story.Scenes.IndexOf(s)).OrderBy(i => i)), "Bag not in story list order.");
        // Then the least recently served.
        var recency = new Dictionary<string, int> { ["rel0"] = 900, ["rel1"] = 900 };
        var second = Rules.NextRemoteBag(story, fresh, recency, 3);
        check(!second.Any(s => s.Relationship == "rel0" || s.Relationship == "rel1"), "Recently served relationships were preferred.");

        // ER-4: relationships sharing a rotation key take one slot.
        story.Relationships["rel1"].RotationKey = "rel0";
        var shared = Rules.NextRemoteBag(story, fresh, new Dictionary<string, int>(), 13);
        check(shared.Count == 12 && shared.Count(s => s.Relationship == "rel0" || s.Relationship == "rel1") == 1, "Shared rotation key delivered twice in one bag.");
        story.Relationships["rel1"].RotationKey = null;

        // Queue cap: a relationship holding `cap` undelivered letters gets no more; queued letters are not repeated.
        var queued = new List<Scene> { story.Scenes.Single(s => s.Id == "rel0.letter0") };
        var capped = Rules.NextRemoteBag(story, fresh, new Dictionary<string, int>(), 13, queued, 1);
        check(!capped.Any(s => s.Relationship == "rel0"), "Queue cap per relationship ignored.");
        var repeat = Rules.NextRemoteBag(story, fresh, new Dictionary<string, int>(), 13, queued, 2);
        check(!repeat.Contains(queued[0]), "A queued letter was bagged again.");

        // A letter that stops being available before its turn is dropped, and the chain continues.
        var drop = new PostBag();
        drop.Fill(story, fresh, new Dictionary<string, int>(), 2);
        var skipped = drop.Queue[0];
        var later = Program.Copy(fresh);
        later.Flags.Add(skipped.Id);
        check(drop.Next(story, later) == drop.Queue.FirstOrDefault() || drop.Queue.Count == 0, "Post bag delivered an unavailable letter.");

        // Manual-only and epilogue scenes never enter a bag; validation bounds.
        story.Scenes[0].ManualOnly = true;
        check(!Rules.NextRemoteBag(story, fresh, new Dictionary<string, int>(), 13).Contains(story.Scenes[0]), "A manual-only letter entered a bag.");
        story.Scenes[0].ManualOnly = false;
        foreach (var (what, mutate) in new (string, Action<Story>)[] {
            ("bag size 0", s => s.PostBagSize = 0), ("bag size 11", s => s.PostBagSize = 11), ("cap 0", s => s.QueueCapPerRelationship = 0),
            ("blank rotation key", s => s.Relationships["rel0"].RotationKey = " ") })
        {
            var bad = Roster(2);
            mutate(bad);
            bool rejected = false;
            try { Rules.Validate(bad); } catch (InvalidOperationException) { rejected = true; }
            check(rejected, "Invalid post-bag setting accepted: " + what);
        }
    }
}
