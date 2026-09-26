using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class JerribethFateTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string actor = "417ce3dcf3a9707488f2b9b2a790814b";
        const string upper = "8217b05e37078414981d994151f0ffb1";
        const string nexus = "7847c3e3537104f4694167af0b9fcd0e";
        const string drezen = "2570015799edf594daf2f076f2f975d8";
        var envelope = story.Scenes.Single(s => s.Id == "jerribeth.fate_envelope");
        var letter = story.Scenes.Single(s => s.Id == "jerribeth.fate_letter");
        var invitation = story.Scenes.Single(s => s.Id == "jerribeth.invitation");
        var route = new Story { Scenes = story.Scenes.Where(s => s.Relationship == "jerribeth").ToList(), Relationships = story.Relationships };
        var seen = new HashSet<string>();
        var native = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Distinct().ToArray();
        var initial = new Snapshot { Chapter = 4, Hour = 1000, Area = upper };
        initial.Flags.UnionWith(new[] { "trickster", "jerribeth.met", "jerribeth.refuge_known", "seelah.committed", "kiana.committed" });

        void Preserve(Snapshot before, Snapshot after)
        {
            foreach (string flag in native.Concat(new[] { "jerribeth.started", "jerribeth.invitation", "jerribeth.attracted",
                "jerribeth.lovers", "jerribeth.committed", "jerribeth.closed", "jerribeth.farewell", "jerribeth.fate_terms",
                "seelah.committed", "kiana.committed" }))
                check(before.Has(flag) == after.Has(flag), "Fate letter rewrites native or relationship history: " + flag);
            check(before.AvailableContacts.SetEquals(after.AvailableContacts), "Fate letter manufactures or restores a native contact.");
        }

        check(envelope.ContactUnit == actor && !Rules.IsRemote(envelope), "Fate envelope is not tied to the verified living actor.");
        check(Rules.EntryTargets(envelope).SequenceEqual(new[] { "19786fae9c29f9d439e374bb857c2e84" }), "Fate envelope uses an unverified native answer list.");
        check(envelope.Areas.SequenceEqual(new[] { upper }) && envelope.Chapters.SequenceEqual(new[] { 4 }), "Fate envelope uses the wrong native area/window.");
        check(!Rules.Available(story, envelope, initial), "History flags alone manufacture Jerribeth's presence.");
        initial.Flags.Add(actor);
        check(!Rules.Available(story, envelope, initial), "A fake authored actor flag bypasses native contact observation.");
        initial.Flags.Remove(actor);
        initial.AvailableContacts.Add(actor);
        check(Rules.Available(story, envelope, initial), "Living Act 4 contact cannot consider the Trickster proposal.");
        check(Rules.NextRemote(route, initial) == null, "Physical fate proposal enters the rest queue.");
        foreach (string missing in new[] { "trickster", "jerribeth.refuge_known" })
        {
            var blocked = Program.Copy(initial); blocked.Flags.Remove(missing);
            check(!Rules.Available(story, envelope, blocked), "Fate proposal invents a prerequisite: " + missing);
            check(!Rules.ContactAvailable(story, envelope, blocked), "Resumed native contact ignores missing prerequisite: " + missing);
        }
        foreach (string flag in new[] { "jerribeth.closed", "jerribeth.unavailable", "jerribeth.patron_lost" })
        {
            var blocked = Program.Copy(initial); blocked.Flags.Add(flag);
            check(!Rules.Available(story, envelope, blocked), "Fate invitation rewrites closure or native departure: " + flag);
        }
        foreach (int chapter in new[] { 3, 5 })
        {
            var blocked = Program.Copy(initial); blocked.Chapter = chapter;
            check(!Rules.Available(story, envelope, blocked) && !Rules.ContactAvailable(story, envelope, blocked), "Fate meeting ignores chapter loss.");
        }
        var elsewhere = Program.Copy(initial); elsewhere.Area = nexus;
        check(!Rules.Available(story, envelope, elsewhere) && !Rules.ContactAvailable(story, envelope, elsewhere), "Native fate meeting follows the player out of the manor.");
        var absent = Program.Copy(initial); absent.AvailableContacts.Clear();
        check(!Rules.ContactAvailable(story, envelope, absent), "Resumed fate meeting survives loss of its actual actor.");
        absent.AvailableContacts.Add(actor); absent.Flags.Add("jerribeth.unavailable");
        check(!Rules.ContactAvailable(story, envelope, absent), "Resumed fate meeting bypasses native hostility/death.");

        foreach (bool alreadyInvited in new[] { false, true })
        {
            var before = Program.Copy(initial);
            if (alreadyInvited)
            {
                before.Flags.UnionWith(new[] { "jerribeth.invitation", "jerribeth.started", "jerribeth.attracted",
                    "jerribeth.lovers", "jerribeth.committed" });
                before.Times["jerribeth.invitation"] = 400;
            }
            var outcomes = Program.Walk(envelope, before, (node, _) => seen.Add(envelope.Id + "/" + node));
            foreach (var outcome in outcomes)
            {
                Preserve(before, outcome);
                check(!Rules.Available(story, letter, outcome), "Fate reply arrives before its actual predecessor delay.");
                if (!outcome.Has(envelope.Id))
                {
                    check(outcome.Flags.SetEquals(before.Flags), "Abandoning the experiment grants contact history.");
                    continue;
                }
                check(!Rules.Available(story, envelope, outcome), "Completed fate experiment repeats.");
                if (outcome.Has("jerribeth.fate_experiment_refused"))
                {
                    check(!outcome.Has("jerribeth.fate_note_prepared") && !outcome.Has("jerribeth.closed"), "Refusal either grants a letter or closes ordinary courtship.");
                    continue;
                }
                check(outcome.Has("jerribeth.fate_question_work") != outcome.Has("jerribeth.fate_question_company"), "Fate letter question histories overlap.");
                foreach (int chapter in new[] { 4, 5 })
                foreach (bool patronLost in new[] { false, true })
                {
                    var waiting = Program.Copy(outcome);
                    waiting.Chapter = chapter; waiting.Area = chapter == 4 ? nexus : drezen;
                    waiting.AvailableContacts.Clear();
                    if (chapter == 5) waiting.Flags.Remove("trickster");
                    if (patronLost) waiting.Flags.Add("jerribeth.patron_lost");
                    waiting.Hour += 23;
                    check(!Rules.Available(story, letter, waiting), "Fate letter ignores its 24-hour wait.");
                    if (!alreadyInvited) check(!Rules.Available(story, invitation, waiting), "Normal invitation bypasses the explicitly chosen pending letter.");
                    waiting.Hour++;
                    check(Rules.Available(story, letter, waiting), "Previously prepared letter cannot arrive after departure, chapter change, or mythic change.");
                    if (!alreadyInvited) check(Rules.NextRemote(route, waiting)?.Id == letter.Id, "Unplayed original invitation hides the selected fate consequence.");
                    foreach (string flag in new[] { "jerribeth.closed", "jerribeth.unavailable" })
                    {
                        var blocked = Program.Copy(waiting); blocked.Flags.Add(flag);
                        check(!Rules.Available(story, letter, blocked), "Fate letter restores an ended or unavailable relationship: " + flag);
                    }
                    var replies = Program.Walk(letter, waiting, (node, _) => seen.Add(letter.Id + "/" + node));
                    foreach (var reply in replies)
                    {
                        Preserve(waiting, reply);
                        if (!reply.Has(letter.Id))
                        {
                            check(reply.Flags.SetEquals(waiting.Flags), "Postponing the letter records its answer.");
                            continue;
                        }
                        check(reply.Has("jerribeth.fate_note_read"), "Finished fate consequence does not release the normal invitation.");
                        if (alreadyInvited)
                            check(reply.Times["jerribeth.invitation"] == 400 && !Rules.Available(story, invitation, reply), "Fate letter replays or retimes an existing invitation.");
                        else
                        {
                            check(Rules.Available(story, invitation, reply), "Ordinary voluntary courtship remains blocked after fate reply.");
                            var choices = Program.Walk(invitation, reply);
                            check(choices.Any(s => s.Has("jerribeth.closed")) && choices.Any(s => s.Has(invitation.Id) && !s.Has("jerribeth.closed")),
                                "Fate access removes the actual choice to accept or reject ordinary correspondence.");
                        }
                    }
                }
            }
        }
        check(seen.SetEquals(new[] { envelope, letter }.SelectMany(s => s.Nodes.Select(n => s.Id + "/" + n.Id))), "Fate tests omit a played page.");
        var ordinary = Program.Copy(initial); ordinary.Flags.Remove("trickster"); ordinary.Area = nexus;
        check(Rules.Available(story, invitation, ordinary), "Trickster addition restricts the existing ordinary route for another mythic.");
    }
}
