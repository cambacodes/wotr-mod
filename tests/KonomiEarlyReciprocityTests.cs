using System;
using System.Linq;
using Tirabade;

internal static class KonomiEarlyReciprocityTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string id = "konomi.a_turn_for_herself";
        const string contact = "ca2d58c5c65723945857e04fb85d30ce";
        Scene Find(string name) => story.Scenes.Single(s => s.Id == "konomi." + name);
        var dance = Find("a_turn_for_herself");
        var letter = Find("letter");
        var evening = Find("evening");
        var supper = evening.Nodes.Single(n => n.Id == "supper");
        var callbacks = supper.Choices.Skip(4).Where(c => c.Next?.StartsWith("remembered_") == true).ToArray();
        Snapshot Play(Scene scene, Snapshot initial)
        {
            var ready = Program.Copy(initial);
            ready.Hour += scene.DelayHours;
            check(Program.CurrentAvailable(story, scene, ready), "Reciprocity predecessor unavailable: " + scene.Id);
            return Program.Walk(scene, ready).First(s => s.Has(scene.Id) && !s.Has("konomi.closed"));
        }
        check(dance.Optional && dance.DelayHours == 0 && dance.ContactUnit == contact,
            "Early encounter lost its optional immediate physical-contact contract.");
        check(letter.DelayHours == 24 && evening.DelayHours == 24
            && !letter.Requires.Contains(id) && !evening.Requires.Contains(id), "Optional encounter changes invitation timing or becomes mandatory.");
        check(callbacks.Length == 4, "Expected four earned preference callbacks.");
        check(supper.Choices.Take(4).Select(c => c.Next).SequenceEqual(new[] { "kiss", "stay", "changed", "quiet" }),
            "Existing supper answer indices changed.");

        foreach (var chapter in new[] { 3, 5 })
        {
            var fresh = new Snapshot { Chapter = chapter, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            fresh.Flags.UnionWith(new[] { "konomi.present", "trickster", "seelah.committed", "arueshalae.committed" });
            fresh.AvailableContacts.Add(contact);
            check(!Program.CurrentAvailable(story, dance, fresh), "Dance opens before expressed interest.");
            fresh = Play(Find("margin"), fresh);
            fresh = Play(Find("reception"), fresh);
            check(Program.CurrentAvailable(story, dance, fresh), "Fresh chapter " + chapter + " cannot take the early encounter.");
            check(!Program.CurrentAvailable(story, letter, fresh), "Encounter accidentally removed original letter delay.");
            check(callbacks.All(c => !Rules.Match(c.Requires, c.Forbids, fresh)), "No-history save sees a fabricated dance memory.");
            var outcomes = Program.Walk(dance, fresh);
            var deferred = outcomes.Single(s => !s.Has(id));
            check(!deferred.Has("konomi.closed") && Program.CurrentAvailable(story, dance, deferred), "Deferring the hour closes or consumes it.");
            var completed = outcomes.Where(s => s.Has(id)).ToArray();
            check(completed.Length == 12, "Not all three participation styles and four preferences are traversable.");
            foreach (var done in completed)
            {
                check(!done.Has("konomi.lovers") && !done.Has("konomi.closed") && !done.Has("konomi.private_night"),
                    "Early encounter prematurely establishes intimacy or closes the route.");
                check(done.Has("seelah.committed") && done.Has("arueshalae.committed") && done.Has("konomi.present")
                    && !done.Has("konomi.dismissed"), "Early encounter rewrites native office or other relationships.");
                check(callbacks.Count(c => Rules.Match(c.Requires, c.Forbids, done)) == 1, "Completed preference has no unique later response.");
                check(!Program.CurrentAvailable(story, letter, done), "Playing optional hour changes original letter deadline.");
                var afterLetter = Play(letter, done);
                var visited = new System.Collections.Generic.HashSet<string>();
                afterLetter.Hour += evening.DelayHours;
                check(Program.CurrentAvailable(story, evening, afterLetter), "Earned preference prevents the original invitation.");
                var lovers = Program.Walk(evening, afterLetter, (node, _) => visited.Add(node));
                var callback = callbacks.Single(c => Rules.Match(c.Requires, c.Forbids, done));
                check(visited.Contains(callback.Next!), "Earned personal response is not on a played supper path.");
                check(lovers.All(s => s.Has("konomi.evening") && s.Has("konomi.lovers")), "Callback loses original evening completion.");
                foreach (var state in lovers)
                    check(!Program.CurrentAvailable(story, dance, state), "Established intimacy can replay the early encounter.");
                var transformed = Program.Copy(afterLetter);
                transformed.Flags.Add("inhuman");
                var changedPages = new System.Collections.Generic.HashSet<string>();
                var changed = Program.Walk(evening, transformed, (node, _) => changedPages.Add(node));
                check(changedPages.Contains(callback.Next!) && changedPages.Contains("changed")
                    && !changedPages.Contains("kiss") && !changedPages.Contains("stay"),
                    "An earned callback invents embodied intimacy after transformation.");
                check(changed.All(s => s.Has("konomi.lovers")), "Transformed callback loses the existing companionship result.");
            }

            // Skipping the addition still plays the original letter and intimate evening.
            var skipped = Play(evening, Play(letter, fresh));
            check(skipped.Has("konomi.lovers") && !skipped.Has(id) && !Program.CurrentAvailable(story, dance, skipped),
                "Old or skip-path lovers are forced through the addition.");
            foreach (var flag in new[] { "konomi.dance_quiet", "konomi.dance_street", "konomi.dance_play", "konomi.dance_beauty" })
            {
                var interrupted = Program.Copy(fresh);
                interrupted.Flags.Add(flag);
                check(callbacks.All(c => !Rules.Match(c.Requires, c.Forbids, interrupted)), "Interrupted preference invents a completed encounter.");
                check(Program.CurrentAvailable(story, dance, interrupted), "Interrupted choice prevents retry.");
            }
            foreach (var mutation in new[] { "missing_contact", "missing_office", "dismissed", "closed", "inhuman", "away", "abyss" })
            {
                var blocked = Program.Copy(fresh);
                if (mutation == "missing_contact") blocked.AvailableContacts.Clear();
                if (mutation == "missing_office") blocked.Flags.Remove("konomi.present");
                if (mutation == "dismissed") blocked.Flags.Add("konomi.dismissed");
                if (mutation == "closed") blocked.Flags.Add("konomi.closed");
                if (mutation == "inhuman") blocked.Flags.Add("inhuman");
                if (mutation == "away") blocked.Area = "elsewhere";
                if (mutation == "abyss") blocked.Chapter = 4;
                check(!Program.CurrentAvailable(story, dance, blocked), "Invalid early entry accepted: " + mutation);
                if (mutation is "missing_contact" or "missing_office" or "dismissed" or "away" or "abyss")
                    check(!Rules.ContactAvailable(story, dance, blocked), "Open scene survives lost native contact: " + mutation);
            }
            var restored = Program.Copy(fresh);
            check(Rules.ContactAvailable(story, dance, restored), "Restored physical contact cannot resume an interrupted page.");
        }
        foreach (var callback in callbacks)
        {
            var page = evening.Nodes.Single(n => n.Id == callback.Next);
            check(page.Choices.Count == 4 && page.Choices.Select(c => c.Next).SequenceEqual(supper.Choices.Take(4).Select(c => c.Next)),
                "Callback does not preserve all original intimacy, quiet and transformed options.");
        }
    }
}
