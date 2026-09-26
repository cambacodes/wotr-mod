using System;
using System.Linq;
using Tirabade;

internal static class KonomiLettersTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var letter = story.Scenes.Single(s => s.Id == "konomi.unsent");
        var returned = story.Scenes.Single(s => s.Id == "konomi.return");
        var start = new Snapshot { Chapter = 4, Hour = 1000 };
        start.Flags.UnionWith(new[] { "konomi.evening", "seelah.committed", "kiana.committed" });
        var letters = Program.Walk(letter, start);
        check(letters.Count == 5, "Konomi letter does not provide five distinct authored intentions.");
        foreach (var written in letters)
        {
            check(written.Has("konomi.letter_wonder") != written.Has("konomi.letter_fear"), "Konomi letter conflates wonder and fear.");
            var state = Program.Copy(written);
            state.Chapter = 5; state.Hour += 48;
            state.Area = returned.Areas.FirstOrDefault() ?? "";
            state.Flags.UnionWith(returned.Requires);
            check(Rules.Available(story, returned, state), "Konomi cannot receive the retained letter.");
            var outcomes = Program.Walk(returned, state);
            string expected = written.Has("konomi.letter_fear") ? "konomi.fear_answered" : "konomi.wonder_answered";
            string other = written.Has("konomi.letter_fear") ? "konomi.wonder_answered" : "konomi.fear_answered";
            check(outcomes.Any(s => s.Has(expected)), "Konomi cannot answer the actual letter.");
            check(outcomes.All(s => !s.Has(other)), "Konomi answers a letter the Commander did not write.");
            check(outcomes.Any(s => !s.Has(expected)), "Asking about Konomi forces delivery of the letter.");
            check(outcomes.All(s => s.Has("seelah.committed") && s.Has("kiana.committed") && s.Has("konomi.returned")), "Konomi letter changes another romance or loses the reunion.");
        }
        foreach (string history in new[] { "legacy", "wonder", "fear", "both" })
        {
            var state = new Snapshot { Chapter = 5, Hour = 1000 };
            state.Flags.UnionWith(returned.Requires);
            state.Flags.Add("konomi.wrote");
            if (history == "wonder" || history == "both") state.Flags.Add("konomi.letter_wonder");
            if (history == "fear" || history == "both") state.Flags.Add("konomi.letter_fear");
            var outcomes = Program.Walk(returned, state);
            check(outcomes.All(s => s.Has("konomi.returned")), "Older Konomi letter history has no completed reunion.");
            if (history == "legacy") check(outcomes.All(s => !s.Has("konomi.wonder_answered") && !s.Has("konomi.fear_answered")), "Legacy letter invents its missing subject.");
            if (history == "both") check(outcomes.Any(s => s.Has("konomi.fear_answered")) && outcomes.All(s => !s.Has("konomi.wonder_answered")), "Overlapping letter history does not retain fear precedence.");
        }
    }
}
