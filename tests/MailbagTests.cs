using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E8b: the mailbag. Every letter deliverable at a rest arrives (one per rotation key, its first in authored order); the player
// reads any of them, in any order, or leaves them for later; letters a read unlocks wait for the next rest.
internal static class MailbagTests
{
    private static Scene Letter(string rel, int i, int maxChapter = 5, int delay = 0) => new Scene
    {
        Id = rel + ".letter" + i, Title = "Letter " + i, Owner = "Konomi", Relationship = rel, Remote = true, MinChapter = 3,
        MaxChapter = maxChapter, DelayHours = delay, Requires = i == 0 ? Array.Empty<string>() : new[] { rel + ".letter" + (i - 1) },
        Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
    };

    private static Story Roster(int count, int delay = 0)
    {
        var story = new Story();
        story.Relationships.Clear();
        for (int r = 0; r < count; r++)
        {
            string rel = "rel" + r;
            story.Relationships[rel] = new Relationship { Title = rel, StartedFlag = rel + ".started", ClosedFlag = rel + ".closed", CommittedFlag = rel + ".committed" };
            for (int i = 0; i < 3; i++) story.Scenes.Add(Letter(rel, i, r == count - 1 ? 3 : 5, i == 0 ? 0 : delay));
        }
        return story;
    }

    private static void Read(Snapshot state, Scene scene)
    {
        state.Flags.Add(scene.Id);
        state.Times[scene.Id] = state.Hour;
    }

    internal static void Run(Action<bool, string> check)
    {
        // Listing: all thirteen waiting relationships arrive at one rest (no bag size), each with its first letter, in story order.
        const int count = 13;
        var story = Roster(count);
        Rules.Validate(story);
        var state = new Snapshot { Chapter = 3, Hour = 1000 };
        var bag = new Mailbag();
        check(bag.Fill(story, state) == count, "Mailbag did not receive every waiting relationship at one rest.");
        var entries = bag.Entries(story, state);
        check(entries.Select(s => s.Id).SequenceEqual(Enumerable.Range(0, count).Select(r => "rel" + r + ".letter0")),
            "Mailbag entries are not the first letters in authored order: " + string.Join(",", entries.Select(s => s.Id)));

        // Reading several in one sitting, in any order: the rest stay unread in the bag.
        foreach (var id in new[] { "rel5.letter0", "rel0.letter0", "rel12.letter0" }) Read(state, story.Scenes.Single(s => s.Id == id));
        entries = bag.Entries(story, state);
        check(entries.Count == count - 3 && !entries.Any(s => s.Id == "rel5.letter0" || s.Id == "rel0.letter0" || s.Id == "rel12.letter0"),
            "Read letters are still listed, or unread ones were lost.");

        // A read unlocks the route's next letter, but it waits for the next rest (authored pacing), and never sits beside
        // its predecessor.
        check(!entries.Any(s => s.Id == "rel5.letter1"), "A letter unlocked mid-sitting arrived without a rest.");
        state.Hour += 16;
        int added = bag.Fill(story, state);
        entries = bag.Entries(story, state);
        check(added == 3 && entries.Any(s => s.Id == "rel5.letter1") && entries.Any(s => s.Id == "rel0.letter1") && entries.Any(s => s.Id == "rel12.letter1"),
            "The next rest did not deliver exactly the three unlocked follow-up letters (got " + added + ").");
        check(entries.Count(s => s.Id == "rel1.letter0") == 1, "Leaving a letter unread duplicated it or dropped it.");
        foreach (var group in entries.GroupBy(s => s.Relationship))
            check(group.Count() == 1, "Two letters of one route listed together: " + group.Key);

        // Letters that stop being available (overtaken) leave the bag.
        story.Scenes.Single(s => s.Id == "rel2.letter0").Forbids = new[] { "rel2.moved_on" };
        state.Flags.Add("rel2.moved_on");
        check(!bag.Entries(story, state).Any(s => s.Id == "rel2.letter0"), "An unavailable letter stayed in the mailbag.");

        // DelayHours: a follow-up arrives only at a rest after its delay has run.
        var slow = Roster(2, delay: 48);
        var slowState = new Snapshot { Chapter = 3, Hour = 500 };
        var slowBag = new Mailbag();
        slowBag.Fill(slow, slowState);
        Read(slowState, slow.Scenes.Single(s => s.Id == "rel0.letter0"));
        slowState.Hour += 24;
        slowBag.Fill(slow, slowState);
        check(!slowBag.Entries(slow, slowState).Any(s => s.Id == "rel0.letter1"), "A delayed letter arrived before its DelayHours.");
        slowState.Hour += 24;
        slowBag.Fill(slow, slowState);
        check(slowBag.Entries(slow, slowState).Any(s => s.Id == "rel0.letter1"), "A delayed letter did not arrive once its delay had run.");

        // Rotation keys: relationships sharing a key deliver one letter per rest between them.
        var shared = Roster(3);
        shared.Relationships["rel1"].RotationKey = "pair";
        shared.Relationships["rel2"].RotationKey = "pair";
        var sharedBag = new Mailbag();
        sharedBag.Fill(shared, new Snapshot { Chapter = 3, Hour = 10 });
        var sharedIds = sharedBag.Arrived.Select(s => s.Relationship).ToList();
        check(sharedIds.Count == 2 && sharedIds.Contains("rel0") && sharedIds.Count(r => r == "rel1" || r == "rel2") == 1,
            "Relationships sharing a rotation key both arrived at one rest: " + string.Join(",", sharedIds));

        // Manual reads and epilogue pages never arrive by post.
        var mixed = Roster(1);
        mixed.Scenes[0].ManualOnly = true;
        mixed.Scenes.Add(new Scene { Id = "rel0.page", Title = "Page", Owner = "Epilogue", Relationship = "rel0", Remote = true, MinChapter = 3,
            Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } } });
        check(Rules.MailbagArrivals(mixed, new Snapshot { Chapter = 3, Hour = 10 }).Count == 0, "A manual read or epilogue page arrived in the mailbag.");

        // Old saves: nothing the mailbag keeps is saved. A save made under the E8 post bag (served.* stamps, some letters read)
        // yields exactly the letters the old scheduler could have delivered, one per relationship, whatever the bag size.
        var old = Roster(6);
        var oldState = new Snapshot { Chapter = 3, Hour = 2000 };
        foreach (var id in new[] { "rel0.letter0", "rel0.letter1", "rel3.letter0" }) Read(oldState, old.Scenes.Single(s => s.Id == id));
        oldState.Flags.Add(Rules.ServedPrefix + "rel0");
        oldState.Hour += 100;
        var legacy = Rules.NextRemoteBag(old, oldState, new Dictionary<string, int> { ["rel0"] = 1900, ["rel3"] = 1950 }, 100);
        var arrivals = Rules.MailbagArrivals(old, oldState);
        check(legacy.Select(s => s.Id).OrderBy(x => x).SequenceEqual(arrivals.Select(s => s.Id).OrderBy(x => x)),
            "Old-save state: mailbag arrivals differ from the post bag's deliverable letters.");
        check(arrivals.Any(s => s.Id == "rel0.letter2") && arrivals.Any(s => s.Id == "rel3.letter1"), "Old-save progress was not continued.");

        // Opt-out: the E8 post bag is unchanged (PostBagTests keeps covering it); the legacy scheduler still answers.
        check(Rules.NextRemote(Roster(3), new Snapshot { Chapter = 3, Hour = 10 })?.Id == "rel0.letter0", "The opt-out scheduler changed.");
        Console.WriteLine("PASS: E8b mailbag (every letter arrives, read any, leave unread, one per route, DelayHours, rotation keys, old saves).");
    }
}
