using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-l02: native history selection, separate from E-Q7-12 actor/placement walks.
// Inputs are GUID observations from the verified JSON. Never seed the expected
// history predicate or composite. Render uses ChoiceAvailable and applies Set.
internal static class NativeFactInventoryTests
{
    internal static Snapshot Observe(Story story, JsonElement observations)
    {
        HashSet<string> In(string kind) => observations.TryGetProperty(kind, out var values)
            ? values.EnumerateArray().Select(v => v.GetString()!).ToHashSet() : new HashSet<string>();
        var state = new Snapshot { Chapter = 5, Hour = 10000,
            CrusadeResources = new Dictionary<string, int> { ["Finances"] = 10000, ["Materials"] = 10000, ["Favors"] = 10000 } };
        // eng7-integ: Main supplies chapter observations before completing derived readers.
        state.Flags.Add("chapter_later");
        if (Rules.ChapterFlag(state.Chapter) is string chapter) state.Flags.Add(chapter);
        var cues = In("SeenCues"); var answers = In("SelectedAnswers");
        var playing = In("Etudes"); var completed = In("CompletedEtudes");
        foreach (var pair in story.SeenCues) if (pair.Value.Any(cues.Contains)) state.Flags.Add(pair.Key);
        foreach (var pair in story.SelectedAnswers) if (answers.Contains(pair.Value)) state.Flags.Add(pair.Key);
        foreach (var pair in story.Etudes)
            if (Rules.EtudeHeld(story, pair.Key, playing.Contains(pair.Value), completed.Contains(pair.Value))) state.Flags.Add(pair.Key);
        foreach (var pair in story.CompletedEtudes) if (completed.Contains(pair.Value)) state.Flags.Add(pair.Key);
        foreach (var pair in story.StartedDialogs) if (In("StartedDialogs").Contains(pair.Value)) state.Flags.Add(pair.Key);
        foreach (var pair in story.CompletedQuests) if (In("CompletedQuests").Contains(pair.Value)) state.Flags.Add(pair.Key);
        foreach (var pair in story.QuestObjectives)
            if (In("QuestObjectives").Contains(pair.Value[0] + ":" + pair.Value[1])) state.Flags.Add(pair.Key);
        Rules.Complete(story, state);
        return state;
    }

    private static HashSet<string> Render(Scene scene, string id, Snapshot state, Action<bool, string> check, string scenario)
    {
        var output = new HashSet<string>();
        void Visit(string nodeId, Snapshot from, HashSet<string> path)
        {
            check(path.Add(nodeId), "Q7-10 cycle: " + scenario + "/" + nodeId);
            var node = scene.Nodes.Single(n => n.Id == nodeId);
            output.Add(node.Id);
            foreach (var paragraph in Rules.VisibleParagraphs(node, from))
                output.Add(node.Id + "/paragraph/" + node.Paragraphs.IndexOf(paragraph));
            var choices = node.Choices.Where(c => Rules.ChoiceAvailable(c, from)).ToArray();
            check(choices.Length > 0, "Q7-10 no selectable answer: " + scenario + "/" + nodeId);
            foreach (var choice in choices)
            {
                var next = Program.Copy(from);
                foreach (var flag in choice.Set) next.Flags.Add(flag);
                if (choice.Crusade != null)
                    next.CrusadeResources![choice.Crusade.Resource] += choice.Crusade.Amount;
                foreach (var target in Rules.NextNodes(choice))
                    Visit(target, next, new HashSet<string>(path));
            }
        }
        Visit(id, state, new HashSet<string>());
        return output;
    }

    internal static Snapshot EarnReunion(Story story, Action<bool, string> check)
    {
        // Native C4 spare -> her existing paid brand conversation -> the wardrobe reunion.
        // MIN_IN and REUNITED come only from accepting their actual authored answers.
        using var inputs = JsonDocument.Parse("{\"Etudes\":[\"978762feac7873d4e925d85202e2c89c\"]}");
        var state = Observe(story, inputs.RootElement);
        state.Flags.Add("trickster");
        Rules.Complete(story, state);
        Snapshot Play(string id, string outcome)
        {
            var scene = story.Scenes.Single(s => s.Id == id);
            var results = Program.Walk(scene, state, (nodeId, at) => {
                var node = scene.Nodes.Single(n => n.Id == nodeId);
                foreach (var choice in node.Choices.Where(c => Rules.Match(c.Requires, c.Forbids, at)))
                    check(Rules.ChoiceAvailable(choice, at), "Q7-10 reunion producer cannot pay: " + id + "/" + nodeId);
            });
            var earned = results.First(s => s.Has(outcome));
            Rules.Complete(story, earned);
            Console.WriteLine("Q7-10 EXECUTED producer=" + id + " outcome=" + outcome);
            return earned;
        }
        state = Play("minagho_chivarro.trickster.spared.brand", "minagho_chivarro.trickster.minagho_in");
        state.Flags.Add("closets.known"); // existing native wardrobe encounter, not the reunion outcome
        state = Play("minagho_chivarro.trickster.reunion.wardrobe", "minagho_chivarro.trickster.reunited");
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var path = Path.Combine("tools", "native_fact_inventory_expectations.json");
        using var doc = JsonDocument.Parse(File.ReadAllText(path));
        foreach (var fixture in doc.RootElement.GetProperty("cases").EnumerateArray())
        {
            string name = fixture.GetProperty("name").GetString()!;
            var observations = fixture.GetProperty("observations");
            var state = Observe(story, observations);
            foreach (var flag in fixture.GetProperty("present").EnumerateArray())
                check(state.Has(flag.GetString()!), "Q7-10 missed witness: " + name + "/" + flag.GetString());
            foreach (var flag in fixture.GetProperty("absent").EnumerateArray())
                check(!state.Has(flag.GetString()!), "Q7-10 invented witness: " + name + "/" + flag.GetString());
            string sceneId = fixture.GetProperty("scene").GetString()!;
            if (sceneId.Length == 0)
            {
                Console.WriteLine("Q7-10 EXECUTED " + name + " observations=" + observations.GetRawText() + " flags=" + string.Join(",", state.Flags.OrderBy(f => f)));
                continue;
            }
            var scene = story.Scenes.Single(s => s.Id == sceneId);
            // Owner prerequisites isolate callback selection. Optional native history is supplied solely by Observe.
            foreach (var flag in scene.Requires.Where(f => !Rules.NativeKeys(story).Contains(f) && !story.Derived.ContainsKey(f))) state.Flags.Add(flag);
            state.Flags.Add("trickster");
            // Test the returned Kaylessa's account in the begged-death history, not the amulet substitution.
            if (sceneId == "kaylessa.wasps.last_words") state.Flags.Add("kaylessa.begged_death");
            Rules.Complete(story, state);
            string nodeId = fixture.GetProperty("node").GetString()!;
            if (nodeId.Length == 0) nodeId = scene.Nodes[0].Id;
            var node = scene.Nodes.Single(n => n.Id == nodeId);
            var targets = node.Choices.Where(c => Rules.ChoiceAvailable(c, state)).Select(c => c.Next).ToHashSet();
            foreach (var target in fixture.GetProperty("targets").EnumerateArray())
                check(targets.Contains(target.GetString()), "Q7-10 missing history branch: " + name + "/" + target.GetString());
            foreach (var target in fixture.GetProperty("excluded").EnumerateArray())
                check(!targets.Contains(target.GetString()), "Q7-10 unearned history branch: " + name + "/" + target.GetString());
            var visited = Render(scene, nodeId, state, check, name);
            var expected = fixture.GetProperty("visited_any").EnumerateArray().Select(id => id.GetString()!).ToArray();
            check(expected.Length == 0 || expected.Any(visited.Contains), "Q7-10 missing callback slot: " + name + "/" + string.Join(",", expected));
            foreach (var id in fixture.GetProperty("not_visited").EnumerateArray())
                check(!visited.Contains(id.GetString()!), "Q7-10 unearned callback slot: " + name + "/" + id.GetString());
            Console.WriteLine("Q7-10 EXECUTED " + name + " observations=" + observations.GetRawText()
                + " visited=" + string.Join(",", visited));

        }

        // The historical visitor/arcade conversations no longer ship. Never recreate them for a fixture.
        check(!story.Scenes.Any(s => s.Id == "nenio.folio.who_are_you_visitor" || s.Id == "nenio.folio.who_are_you_arcade"),
            "Q7-10 historical who_are_you twins reappeared");
        var handled = story.Scenes.Single(s => s.Id == "eritrice.council.the_motion_to_expel_voted").Nodes.Single(n => n.Id == "handled");
        check(handled.Choices.All(c => c.Crusade == null),
            "Q7-10 unimplemented paid undertaking reappeared");

        // Select both actually earned Areelu outcomes, with the route wager/commitment retained.
        var ending = story.Scenes.Single(s => s.Id == "areelu.trickster.finale.ascended");
        foreach (var producer in new[] { "ascend_areelu", "ascend_all", "ascend_alone", "ascend_companions" })
        {
            var state = new Snapshot { Chapter = 6, Hour = 10000 };
            state.Flags.UnionWith(new[] { producer, "trickster", "trickster.ever", "areelu.trickster.wager_struck", "areelu.committed" });
            Rules.Complete(story, state);
            bool expected = producer == "ascend_areelu" || producer == "ascend_all";
            check(Rules.Available(story, ending, state) == expected, "Q7-10 Areelu outcome selection: " + producer);
            state.Flags.Remove("areelu.trickster.wager_struck");
            check(!Rules.Available(story, ending, state), "Q7-10 ascent waived the earned wager");
        }

        // Play an existing reunion producer, then consume it alongside verified parent Book 3 history.
        var result = EarnReunion(story, check);
        check(!result.Has("chivarro.searching"), "Q7-10 authored reunion fabricated the native Azata etude");
        Rules.Complete(story, result);
        check(result.Has("minachiv.reunion_history"), "Q7-10 earned reunion cannot supply continuation history");
        foreach (var scene in story.Scenes.Where(s => s.Id.StartsWith("minachiv.") && s.Requires.Contains("minachiv.reunion_history")))
            check(!scene.Requires.Contains("chivarro.searching"), "Q7-10 continuation still requires native Azata searching: " + scene.Id);

        var page = story.Scenes.Single(s => s.Id == "galfrey.lastcall.page").Nodes[0];
        foreach (bool native in new[] { false, true })
        {
            var state = new Snapshot();
            state.Flags.Add(native ? "galfrey.romance_finished" : "galfrey.trickster.alive.committed");
            var text = string.Join(" ", Rules.VisibleParagraphs(page, state).Select(p => SurfaceIds.Of(story, p)));
            check(SurfaceIds.Has(text, native ? "[galfrey.lastcall.page/page/paragraph/6]" : "[galfrey.lastcall.page/page/paragraph/5]"), "Q7-10 Galfrey provenance lost");
            check(!SurfaceIds.Has(text, native ? "[galfrey.lastcall.page/page/paragraph/5]" : "[galfrey.lastcall.page/page/paragraph/6]"), "Q7-10 Galfrey incompatible crown history");
        }
    }
}
