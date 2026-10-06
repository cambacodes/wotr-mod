using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Engine contract tests, not a substitute for playing each authored romance graph.
internal static class ExpansionTests
{
    public static void Run(Action<bool, string> check)
    {
        var story = new Story();
        foreach (var name in new[] { "seelah", "vellexia" })
            story.Relationships.Add(name, new Relationship
            {
                Title = name, StartedFlag = name + ".started", ClosedFlag = name + ".closed",
                CommittedFlag = name + ".committed", UnavailableFlags = new[] { name + ".dead" }
            });
        var seelah = new Scene
        {
            Id = "seelah.test", Relationship = "seelah", Owner = "Seelah",
            AnswerLists = new[] { "417fa384f3250634bb71859fbc913453" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "Test fixture", Choices = new List<Choice> { new Choice() } } }
        };
        var vellexia = new Scene
        {
            Id = "vellexia.test", Relationship = "vellexia", Owner = "Vellexia", MinChapter = 4,
            AnswerLists = new[] { "7f394dd6cd32c44408a59bd08eb1512a" },
            Nodes = new List<Node> { new Node { Id = "start", Text = "Test fixture", Choices = new List<Choice> { new Choice() } } }
        };
        story.Scenes.AddRange(new[] { seelah, vellexia });
        Rules.Validate(story);
        var state = new Snapshot { Chapter = 4, Hour = 8000 };
        state.Flags.UnionWith(new[] { "closed", "committed", "anevia_dead", "irabeth_gone" });
        check(Rules.Available(story, seelah, state), "The original couple must not govern Seelah.");
        check(Rules.Available(story, vellexia, state), "An Abyss character must be available in Act 4.");
        foreach (var path in new[] { "angel", "aeon", "azata", "demon", "trickster", "lich", "true_lich", "swarm", "devil", "dragon", "legend" })
        {
            state.Flags.Add(path);
            check(Rules.Available(story, seelah, state) && Rules.Available(story, vellexia, state), "Engine applied an implicit mythic ban: " + path);
            state.Flags.Remove(path);
        }
        state.Flags.UnionWith(new[] { "seelah.committed", "vellexia.committed" });
        check(Rules.Available(story, seelah, state) && Rules.Available(story, vellexia, state), "Simultaneous commitments blocked later meetings.");
        state.Flags.Add("seelah.closed");
        check(!Rules.Available(story, seelah, state) && Rules.Available(story, vellexia, state), "Closing one relationship affected the other.");
        state.Flags.Remove("seelah.closed");
        state.Flags.Add("vellexia.dead");
        check(Rules.Available(story, seelah, state) && !Rules.Available(story, vellexia, state), "A character's absence was not scoped to her relationship.");
        check(Rules.EntryTargets(seelah).Single() != Rules.EntryTargets(vellexia).Single(), "Different owners share an accidental dialogue target.");
        seelah.AnswerLists = Array.Empty<string>();
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("attachment"), "Missing entry point produced the wrong diagnostic."); }
        seelah.Remote = true;
        Rules.Validate(story);
        check(Rules.EntryTargets(seelah).Length == 0 && Rules.IsRemote(seelah), "Remote correspondence was attached to an NPC dialogue.");
        seelah.Chapters = new[] { 1, 2, 3, 5 };
        check(!Rules.Available(story, seelah, state), "Authored separation chapters were ignored.");
        state.Chapter = 5;
        check(Rules.Available(story, seelah, state), "A remote meeting failed to return after separation.");
        seelah.Requires = new[] { "seelah.previous" };
        seelah.DelayHours = 24;
        state.Flags.Add("seelah.previous");
        state.Times["seelah.previous"] = state.Hour;
        check(!Rules.Available(story, seelah, state), "A remote meeting bypassed its delay.");
        state.Hour += 24;
        check(Rules.Available(story, seelah, state), "A remote meeting's delay never expired.");
        state.Flags.Add(seelah.Id);
        check(!Rules.Available(story, seelah, state), "A finished remote meeting repeated.");
        story.Relationships["seelah"].ClosedFlag = "closed";
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("shared"), "Shared relationship state produced the wrong diagnostic."); }
        story.Relationships["seelah"].ClosedFlag = "seelah.closed";
        story.SelectedAnswers.Add("native.choice", "73c5728c4c6658344bedcc1b666e598c");
        story.CompletedEtudes.Add("native.finished", "b5f301fbc4c44535a6309d610d5bd28a");
        Rules.Validate(story);
        seelah.Nodes[0].Choices[0].Set = new[] { "native.choice" };
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("selected-answer"), "Native choice collision has wrong diagnostic."); }
        seelah.Nodes[0].Choices[0].Set = new[] { "native.finished" };
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("completed-etude"), "Native completion collision has wrong diagnostic."); }
        seelah.Nodes[0].Choices[0].Set = Array.Empty<string>();
        story.CompletedEtudes.Add("native.choice", "b5f301fbc4c44535a6309d610d5bd28a");
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("selected-answer"), "Native alias collision has wrong diagnostic."); }
        story.CompletedEtudes.Remove("native.choice");
        story.SelectedAnswers.Add("hour.seelah.test", "73c5728c4c6658344bedcc1b666e598c");
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("selected-answer"), "Native timestamp collision has wrong diagnostic."); }
        story.SelectedAnswers.Remove("hour.seelah.test");
        story.SelectedAnswers.Add("inhuman", "73c5728c4c6658344bedcc1b666e598c");
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("selected-answer"), "Native derived-state collision has wrong diagnostic."); }
        story.SelectedAnswers.Remove("inhuman");
        story.SelectedAnswers["native.choice"] = "not-a-guid";
        try { Rules.Validate(story);  }
        catch (InvalidOperationException ex) { check(ex.Message.Contains("selected-answer"), "Malformed native answer has wrong diagnostic."); }
    }
}
