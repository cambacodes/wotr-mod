using System;
using System.Linq;
using Tirabade;

// ChivarroKilled split (storylines/chivarro_death.py): ChivarroKilled (chivarro.dead) also starts when the to-the-death
// fight begins (ChivarroAbusedScene gate f6b3213f); only the unit's death trigger also completes AvengeInsults/Obj3.
// chivarro.dead_confirmed = both. chivarro.dead keeps its meaning for old saves.
internal static class ChivarroDeathTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        check(story.Etudes.TryGetValue("chivarro.dead", out var etude) && etude == "fd2ab9b67ce3e284184b1894c82c6c5d",
            "Chivarro_Death: chivarro.dead is no longer ChivarroKilled (old saves read it).");
        check(story.QuestObjectives.TryGetValue("chivarro.exile_objective_done", out var obj) && obj.SequenceEqual(new[] { "7ce588c0d2e296b41be4f754edbe60d3", "Completed" }),
            "Chivarro_Death: the confirmation is not Obj3_ExiledChivarro Completed.");
        check(story.Derived.TryGetValue("chivarro.dead_confirmed", out var groups) && groups.Length == 1
              && groups[0].OrderBy(k => k).SequenceEqual(new[] { "chivarro.dead", "chivarro.exile_objective_done" }),
            "Chivarro_Death: dead_confirmed is not ChivarroKilled AND Obj3 completed.");
        foreach (var (what, flags, confirmed) in new (string, string[], bool)[]
        {
            ("fight begun, Chivarro alive", new[] { "chivarro.dead" }, false),
            ("death trigger fired", new[] { "chivarro.dead", "chivarro.exile_objective_done" }, true),
            ("no etude (objective alone)", new[] { "chivarro.exile_objective_done" }, false),
        })
        {
            var state = new Snapshot { Chapter = 4 };
            state.Flags.UnionWith(flags);
            Rules.Complete(story, state);
            check(state.Has("chivarro.dead_confirmed") == confirmed && state.Has("chivarro.dead") == flags.Contains("chivarro.dead"),
                "Chivarro_Death: " + what);
        }
    }
}
