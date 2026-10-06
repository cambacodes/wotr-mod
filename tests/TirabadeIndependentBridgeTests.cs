using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

internal static class TirabadeIndependentBridgeTests
{
    internal static void Run(Story story, Story original, Action<bool, string> check)
    {
        const string anevia = "b5e867e13503c6f41bb1316705efb4a2";
        const string irabeth = "280d4712dceb37f4a88e98f1f4c6e64f";
        const string negotiated = "tirabade.negotiated_table";
        const string closed = "tirabade.group_closed";
        Scene Book(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot Ready(Scene book)
        {
            var state = new Snapshot { Chapter = book.MinChapter, Hour = 10000,
                Area = "2570015799edf594daf2f076f2f975d8" };
            state.AvailableContacts.UnionWith(new[] { anevia, irabeth });
            foreach (string key in book.Requires) HouseholdTests.Earn(story, state, key);
            Rules.Complete(story, state);
            return state;
        }
        void NoInventedHistory(Snapshot state) => check(!new[] { "a_affair", "i_affair", "reckoning", "a_truth", "i_truth", "table" }.Any(state.Has),
            "Negotiated bridge invented affair or unplayed legacy history.");

        var options = new JsonSerializerOptions { IncludeFields = true };
        foreach (var prior in original.Scenes.Where(s => s.Relationship == "tirabade"))
        {
            var revised = Book(prior.Id);
            foreach (var oldPage in prior.Nodes)
            {
                var newPage = revised.Nodes.Single(n => n.Id == oldPage.Id);
                check(newPage.Choices.Count >= oldPage.Choices.Count, "Bridge removed saved answer indices.");
                for (int i = 0; i < oldPage.Choices.Count; i++)
                {
                    var comparison = JsonSerializer.Deserialize<Choice>(JsonSerializer.Serialize(newPage.Choices[i], options), options)!;
                    comparison.Forbids = comparison.Forbids.Where(flag => flag != negotiated).ToArray();
                    check(JsonSerializer.Serialize(comparison, options) == JsonSerializer.Serialize(oldPage.Choices[i], options),
                        "Bridge changed a legacy answer beyond excluding the mutually exclusive new history: " + prior.Id + "/" + oldPage.Id + "/" + i);
                }
            }
        }
        foreach (var pair in new[] { ("a_roof", "anevia", "i_watch"), ("i_respite", "irabeth", "a_cup") })
        {
            var book = Book(pair.Item1);
            var outcomes = Program.Walk(book, Ready(book));
            check(outcomes.Any(s => s.Has("closed")), "Original global refusal no longer exists.");
            var local = outcomes.First(s => s.Has(pair.Item2 + ".local_declined"));
            check(!local.Has("closed") && Rules.Available(story, Book(pair.Item3), local),
                "Local refusal closes the other woman's legacy acquisition.");
            check(!Rules.Available(story, book, local), "Local refusal permits repeated acquisition.");
            var honest = outcomes.First(s => s.Has(pair.Item2 + ".courtship_requested"));
            NoInventedHistory(honest);
            check(!honest.Has(pair.Item2 + ".lover") && !honest.Has(pair.Item2 + ".marital_terms_agreed"),
                "Honest request grants an unplayed relationship.");
            check(!Rules.Available(story, Book(pair.Item2 == "anevia" ? "a_crossing" : "i_crossing"), honest),
                "Honest request still starts the secret first affair.");
        }

        var table = Book(negotiated);
        var seed = Ready(table);
        check(Rules.Available(story, table, seed), "Eligible negotiated invitation is unavailable.");
        foreach (string prerequisite in table.Requires)
        {
            var missing = Program.Copy(seed); missing.Flags.Remove(prerequisite);
            check(!Rules.Available(story, table, missing), "Shared invitation bypasses earned bond: " + prerequisite);
        }
        var results = Program.Walk(table, seed, (_, partial) => {
            foreach (string actor in new[] { anevia, irabeth })
            {
                var lost = Program.Copy(partial); lost.AvailableContacts.Remove(actor);
                check(!Rules.ContactAvailable(story, table, lost), "Joint page survives participant loss.");
            }
        });
        foreach (var result in results) NoInventedHistory(result);
        var together = results.First(s => s.Has("trying"));
        check(together.Has(negotiated) && !together.Has("committed"), "Supper skips commitment development.");
        var separate = results.First(s => s.Has(closed));
        check(!separate.Has("closed") && !separate.Has("anevia.closed") && !separate.Has("irabeth.closed"),
            "Declining group romance closes individual relationships.");
        check(results.Any(s => !s.Has(negotiated) && !s.Has(closed)), "Delay permanently records a decision.");

        together.Hour += 72;
        var ordinary = Book("ordinary");
        check(Rules.Available(story, ordinary, together), "Negotiated table cannot enter ordinary shared life.");
        var ordinaryResults = Program.Walk(ordinary, together, (id, _) =>
            check(id != "rank", "Negotiated entry reads the old sneaking-around reprimand."));
        together = ordinaryResults.First(s => s.Has("kept_terms") && !s.Has("closed"));
        NoInventedHistory(together);
        check(Rules.Available(story, Book("departure"), together), "Negotiated relationship cannot say goodbye before Act4.");
        together.Chapter = 4;
        var letter = Book("tirabade.negotiated_letter");
        check(Rules.Available(story, letter, together) && !Rules.Available(story, Book("abyss_letter"), together),
            "Negotiated absence missing or old betrayal letter also available.");
        together = Program.Walk(letter, together).First();
        check(!together.Has("abyss_letter") && !together.Has("wrote_letter"), "New letter claims old letter or glove callback.");
        together.Hour += 72;
        check(Rules.Available(story, Book("abyss_dream"), together), "Actual new letter cannot support the shared dream.");
        together.Chapter = 5;
        var reunion = Book("return");
        check(Rules.Available(story, reunion, together), "Negotiated relationship cannot reunite.");
        Program.Walk(reunion, together, (id, _) => check(id != "back" && id != "letter", "Reunion invents secret courtship or old glove letter."));

        var developedIds = new HashSet<string>(new[] { "a_self", "i_self", "return", "power", "future", "shared_night", "last_watch" }
            .Concat(story.Scenes.Where(s => s.Id.StartsWith("three_", StringComparison.Ordinal)
                && s.Id != "three_choose_days" && s.Id != "three_more_days").Select(s => s.Id)));
        together.Flags.Add("azata");
        for (int visit = 0; visit < developedIds.Count; visit++)
        {
            together.Hour += 72;
            var next = story.Scenes.FirstOrDefault(s => developedIds.Contains(s.Id) && Rules.Available(story, s, together));
            if (next == null) break;
            var outcomes = Program.Walk(next, together, (id, _) => {
                if (next.Id == "power") check(id != "azata", "Negotiated Azata invents the original affair.");
                if (next.Id == "future") check(id != "choice" && id != "yes", "Negotiated commitment recalls an unplayed betrayal.");
            });
            together = outcomes.Where(s => s.Has(next.Id) && !s.Has("closed") && !s.Has(closed)
                && !s.Has("anevia.closed") && !s.Has("irabeth.closed"))
                .OrderByDescending(s => s.Flags.Count).First();
            NoInventedHistory(together);
        }
        check(together.Has("three_progression.developed") && together.Has("last_words"),
            "Negotiated relationship cannot play the developed campaign and farewell.");
        together.Chapter = 6;
        var developedEndings = story.Scenes.Where(s => s.Relationship == "tirabade" && s.Owner == "Epilogue" && Rules.Available(story, s, together)).ToArray();
        check(developedEndings.Length == 1 && developedEndings[0].Id == "tirabade.negotiated_ending_together",
            "Developed negotiated ending is missing, doubled or recalls old betrayals.");

        foreach (string meeting in new[] { "table", "future", "parting" })
        {
            var book = Book(meeting);
            var state = Ready(book);
            state.Flags.UnionWith(new[] { "a_affair", "i_affair", "a_morning", "i_morning", "reckoning" });
            var split = Program.Walk(book, state).Where(s => s.Has(closed)).ToList();
            check(split.Count >= 3, "Shared meeting lacks individual and separate continuation options.");
            foreach (var result in split)
            {
                check(!result.Has("closed") && result.Has("a_affair") && result.Has("i_affair"), "Split erases history or sets global refusal.");
                check(!result.Has("anevia.lover") && !result.Has("irabeth.lover"), "Shared split automatically awards individual romance.");
                check(!Rules.Available(story, Book("ordinary"), result), "Shared life continues after group closure.");
                if (result.Has("tirabade.anevia_continuation_invited"))
                {
                    result.Hour += 72;
                    check(Rules.Available(story, Book("anevia.an_invitation_afterward"), result), "Real shared split strands Anevia's individual invitation.");
                }
            }
        }
        foreach (var scenario in new[] { "", "loss", "inhuman" })
        {
            var state = Ready(table); state.Flags.Add(negotiated); state.Chapter = 6;
            if (scenario != "") state.Flags.Add(scenario);
            if (scenario == "loss") state.Flags.Add("irabeth_dead");
            if (scenario == "inhuman") state.Flags.Add("swarm");
            var endings = story.Scenes.Where(s => s.Relationship == "tirabade" && s.Owner == "Epilogue" && Rules.Available(story, s, state)).ToArray();
            check(endings.Length == 1, "Negotiated interrupted outcome has missing or overlapping endings: " + scenario);
            NoInventedHistory(state);
        }
    }
}
