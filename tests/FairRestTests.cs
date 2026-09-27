using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// GLOBAL-03: with many concurrent relationships (Trickster + ToyBox), rest letters rotate fairly.
internal static class FairRestTests
{
    public static void Run(Action<bool, string> check)
    {
        const int count = 13;
        var story = new Story();
        story.Relationships.Clear();
        for (int r = 0; r < count; r++)
        {
            string rel = "rel" + r;
            story.Relationships[rel] = new Relationship { Title = rel, StartedFlag = rel + ".started", ClosedFlag = rel + ".closed", CommittedFlag = rel + ".committed" };
            for (int i = 0; i < 3; i++)
                story.Scenes.Add(new Scene
                {
                    Id = rel + ".letter" + i, Title = "Letter", Owner = "Memory", Relationship = rel, Remote = true, MinChapter = 3,
                    MaxChapter = r == count - 1 ? 3 : 5, Requires = i == 0 ? Array.Empty<string>() : new[] { rel + ".letter" + (i - 1) },
                    Nodes = new List<Node> { new Node { Id = "start", Text = "x", Choices = new List<Choice> { new Choice() } } }
                });
        }
        var state = new Snapshot { Chapter = 3, Hour = 1000 };
        var served = new Dictionary<string, int>();
        var order = new List<string>();
        for (int rest = 0; rest < count; rest++)
        {
            var scene = Rules.NextRemote(story, state, served);
            check(scene != null, "Fair scheduler starved every relationship at rest " + rest);
            order.Add(scene!.Relationship);
            served[scene.Relationship] = state.Hour;
            state.Flags.Add(scene.Id);
            state.Times[scene.Id] = state.Hour;
            state.Hour += 24;
        }
        check(order.Distinct().Count() == count, "Some relationship was served twice before all were served once: " + string.Join(",", order));
        check(order[0] == "rel" + (count - 1), "The relationship whose window closes soonest was not served first: " + order[0]);
        // The legacy overload keeps authored order for existing callers.
        check(Rules.NextRemote(story, new Snapshot { Chapter = 3, Hour = 1000 })?.Id == "rel0.letter0", "Legacy NextRemote order changed.");
    }
}
