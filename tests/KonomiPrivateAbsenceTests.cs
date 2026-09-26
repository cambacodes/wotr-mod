using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiPrivateAbsenceTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "konomi." + id);
        var absence = Get("private_absence");
        var reunion = Get("private_reunion");
        var catchup = Get("private_absence_catchup");
        var reached = new HashSet<string>();
        var protectedFlags = story.Etudes.Keys.Concat(story.CompletedEtudes.Keys).Concat(story.CompletedQuests.Keys)
            .Concat(story.SeenCues.Keys).Concat(story.SelectedAnswers.Keys).Concat(story.StartedDialogs.Keys)
            .Concat(new[] { "trickster", "legend", "konomi.committed", "arueshalae.committed", "jerribeth.committed" }).Distinct().ToArray();
        void Preserve(Snapshot before, Snapshot after)
        {
            foreach (var f in protectedFlags) check(before.Has(f) == after.Has(f), "Konomi absence changes protected history: " + f);
        }
        Snapshot Earn(string id, Snapshot input)
        {
            var scene = Get(id);
            input.Hour += 1000;
            check(Rules.Available(story, scene, input), "Konomi earned predecessor cannot continue: " + id);
            return Program.Walk(scene, input).First(s => s.Has(scene.Id) && !s.Has("konomi.closed"));
        }
        List<Snapshot> Walk(Scene scene, Snapshot input)
        {
            var results = Program.Walk(scene, input, (page, partial) =>
            {
                reached.Add(scene.Id + "/" + page);
                if (scene != reunion || page.StartsWith("absence_", StringComparison.Ordinal))
                    check(!partial.Has("konomi.private_absence_answered"), "Konomi unfinished account commits acknowledgement.");
                if (scene != reunion)
                {
                    check(partial.Flags.SetEquals(input.Flags), "Konomi new scene persists an abandoned branch.");
                    check(partial.Times.OrderBy(p => p.Key).SequenceEqual(input.Times.OrderBy(p => p.Key)), "Konomi intermediate timestamp changed.");
                }
            });
            foreach (var result in results) Preserve(input, result);
            return results;
        }
        foreach (bool established in new[] { false, true })
        {
            var start = new Snapshot { Chapter = 3, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
            start.Flags.UnionWith(new[] { "konomi.dismissed", "konomi.office_completed", "trickster", "arueshalae.committed", "jerribeth.committed" });
            // Established affection is a pre-existing valid route fixture; private access onward is actually played.
            if (established) start.Flags.UnionWith(new[] { "konomi.evening", "konomi.lovers", "konomi.disagreement" });
            foreach (string id in new[] { "fate_post", "fate_reply", "private_meeting" }) start = Earn(id, start);
            if (!start.Has("konomi.private_history_ready")) start = Earn("private_history", start);
            foreach (string id in new[] { "carriers", "before_road", "private_departure" }) start = Earn(id, start);
            var away = Program.Copy(start); away.Chapter = 4; away.Area = "abyss";
            check(Rules.Available(story, absence, away), "Fresh or established dismissed route cannot remember Konomi in Chapter 4.");
            var histories = Walk(absence, away).Where(s => s.Has(absence.Id)).ToList();
            check(histories.Count == 4, "Konomi page/memory and wanted/changed histories are incomplete.");
            foreach (var h in histories)
            {
                check(h.Has("konomi.absence_page") != h.Has("konomi.absence_memory"), "Konomi page and memory overlap.");
                check(h.Has("konomi.absence_wanted") != h.Has("konomi.absence_changed"), "Konomi absence topics overlap.");
            }
            // Old saves may have skipped the new absence or kept the original ordinary unsent letter.
            histories.Add(Program.Copy(away));
            if (established)
            {
                foreach (var letter in Program.Walk(Get("unsent"), away))
                    if (letter.Has("konomi.wrote")) histories.Add(letter);
                var legacy = Program.Copy(away); legacy.Flags.Add("konomi.wrote"); histories.Add(legacy);
                // Reproduces an old ordinary return followed by Chapter 5 dismissal/private acquisition.
                // No Chapter 4 private record exists, so it must never claim the earlier exile/reception.
                var late = Program.Copy(away);
                late.Flags.UnionWith(new[] { "konomi.wrote", "konomi.letter_wonder", "konomi.wonder_answered", "konomi.return" });
                histories.Add(late);
                foreach (string response in new[] { "konomi.wonder_answered", "konomi.fear_answered" })
                { var interruptedReturn = Program.Copy(away); interruptedReturn.Flags.UnionWith(new[] { "konomi.wrote", response }); histories.Add(interruptedReturn); }
            }
            foreach (var history in histories)
            foreach (string path in new[] { "trickster", "legend", "other" })
            {
                var back = Program.Copy(history); back.Chapter = 5; back.Area = start.Area;
                back.Flags.Remove("trickster");
                if (path != "other") back.Flags.Add(path);
                foreach (string id in new[] { "capital_letter", "return_offer" }) back = Earn(id, back);
                back.Hour += 1000;
                check(Rules.Available(story, reunion, back), "Optional absence added a reunion prerequisite.");
                var observed = new HashSet<string>();
                Program.Walk(reunion, back, (page, _) => observed.Add(page));
                if ((back.Has("konomi.return") || back.Has("konomi.wonder_answered") || back.Has("konomi.fear_answered")) && !back.Has("konomi.private_absence_kept"))
                {
                    check(observed.Contains("absence_already") && observed.Contains("absence_now"), "Late dismissal lacks a present-focused reply.");
                    check(!observed.Contains("absence_oldletter") && !observed.Contains("absence_her_days") && !observed.Contains("absence_changed"),
                        "Late dismissal duplicates an old letter or invents private exile during the Abyss.");
                }
                var outcomes = Walk(reunion, back).Where(s => s.Has(reunion.Id)).ToList();
                check(outcomes.Any(s => !s.Has("konomi.private_absence_answered")), "Original reunion no longer permits explicit deferral.");
                if (back.Has("konomi.private_absence_kept") || back.Has("konomi.wrote"))
                    check(outcomes.Any(s => s.Has("konomi.private_absence_answered")), "Kept account has no reunion response.");
                foreach (var result in outcomes)
                {
                    if (result.Has("konomi.private_absence_answered"))
                    {
                        check(result.Has("konomi.private_returned") && result.Has("konomi.reunion_kept"), "New reunion branch lost original continuation milestones.");
                        check(!Rules.Available(story, catchup, result), "Answered account repeats in catch-up.");
                    }
                }
                var skipped = outcomes.First(s => !s.Has("konomi.private_absence_answered"));
                check(Rules.Available(story, catchup, skipped), "Older or deferred reunion lacks manual catch-up.");
                foreach (var result in Walk(catchup, skipped))
                {
                    if (!result.Has(catchup.Id)) check(result.Flags.SetEquals(skipped.Flags), "Catch-up deferral changes history.");
                    else check(result.Has("konomi.private_absence_answered"), "Catch-up finishes without acknowledgement.");
                }
                var future = Get("lease_offer"); skipped.Hour += 1000;
                check(Rules.Available(story, future, skipped), "Skipping absence blocks original career continuation.");
            }
        }
        // Reproduce the problematic chronology by playing the real ordinary return before dismissal.
        var lateOffice = new Snapshot { Chapter = 3, Hour = 1000, Area = "2570015799edf594daf2f076f2f975d8" };
        lateOffice.AvailableContacts.Add("ca2d58c5c65723945857e04fb85d30ce");
        lateOffice.Flags.UnionWith(new[] { "konomi.present", "trickster" });
        foreach (string id in new[] { "margin", "reception", "letter", "evening", "disagreement", "leak", "reckoning" }) lateOffice = Earn(id, lateOffice);
        lateOffice.Chapter = 4; lateOffice = Earn("unsent", lateOffice);
        lateOffice.Chapter = 5; lateOffice = Earn("return", lateOffice);
        int originalReturn = lateOffice.Times["konomi.return"];
        lateOffice.Flags.Remove("konomi.present");
        lateOffice.Flags.UnionWith(new[] { "konomi.dismissed", "konomi.office_completed" });
        foreach (string id in new[] { "fate_post", "fate_reply", "private_meeting", "private_history", "carriers", "before_road", "private_departure", "capital_letter", "return_offer" }) lateOffice = Earn(id, lateOffice);
        check(lateOffice.Times["konomi.private_departure"] > originalReturn && !lateOffice.Has("konomi.private_absence_kept"), "Late-dismissal reproduction accidentally used an early exile.");
        lateOffice.Flags.Remove("trickster"); lateOffice.Flags.Add("legend"); lateOffice.Hour += 1000;
        var latePages = new HashSet<string>();
        var lateOutcomes = Program.Walk(reunion, lateOffice, (page, _) => latePages.Add(page));
        check(latePages.Contains("absence_already") && latePages.Contains("absence_now") && latePages.Contains("absence_legend"), "Late Legend reunion lost present circumstances.");
        check(!latePages.Contains("absence_oldletter") && !latePages.Contains("absence_her_days"), "Played late dismissal duplicated delivery or early exile.");
        var lateSkipped = lateOutcomes.First(o => o.Has(reunion.Id) && !o.Has("konomi.private_absence_answered"));
        latePages.Clear();
        Program.Walk(catchup, lateSkipped, (page, _) => latePages.Add(page));
        check(latePages.Contains("absence_already") && !latePages.Contains("absence_oldletter") && !latePages.Contains("absence_her_days"), "Late old-save catch-up fabricates an unplayed chronology.");
        foreach (var scene in new[] { absence, catchup })
        {
            var ready = new Snapshot { Chapter = scene == absence ? 4 : 5, Hour = 50000, Area = scene == absence ? "abyss" : catchup.Areas.Single() };
            ready.Flags.UnionWith(scene.Requires);
            check(Rules.Available(story, scene, ready), "New absence scene baseline invalid.");
            foreach (var flag in scene.Requires)
            { var missing = Program.Copy(ready); missing.Flags.Remove(flag); check(!Rules.Available(story, scene, missing), "Missing private prerequisite admitted: " + flag); }
            foreach (var flag in scene.Forbids.Concat(new[] { "konomi.closed" }))
            { var blocked = Program.Copy(ready); blocked.Flags.Add(flag); check(!Rules.Available(story, scene, blocked), "Absence ignores blocker: " + flag); }
            var wrong = Program.Copy(ready); wrong.Chapter = 3;
            check(!Rules.Available(story, scene, wrong), "Absence continuity appears before its chapter.");
            foreach (var page in scene.Nodes) check(reached.Contains(scene.Id + "/" + page.Id), "Unplayed new page: " + scene.Id + "/" + page.Id);
        }
        foreach (var page in reunion.Nodes.Where(n => n.Id.StartsWith("absence_", StringComparison.Ordinal)))
            check(reached.Contains(reunion.Id + "/" + page.Id), "Unplayed appended reunion page: " + page.Id);
        check(catchup.ManualOnly && catchup.Remote, "Old-save catch-up entered automatic queue.");
        var single = new Story { Scenes = new List<Scene> { catchup }, Relationships = story.Relationships };
        var eligible = new Snapshot { Chapter = 5, Hour = 50000, Area = catchup.Areas.Single() }; eligible.Flags.UnionWith(catchup.Requires);
        check(Rules.NextRemote(single, eligible) == null, "Manual catch-up became compulsory rest content.");
    }
}
