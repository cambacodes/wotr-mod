using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class AneviaIndependentTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string area = "2570015799edf594daf2f076f2f975d8";
        const string anevia = "b5e867e13503c6f41bb1316705efb4a2";
        const string irabeth = "280d4712dceb37f4a88e98f1f4c6e64f";
        Scene Get(string id) => story.Scenes.Single(s => s.Id == "anevia." + id);
        var seen = new HashSet<string>();
        Snapshot Fresh(int chapter, string partner = "none")
        {
            var state = new Snapshot { Chapter = chapter, Hour = 1000, Area = area };
            state.AvailableContacts.UnionWith(new[] { anevia, irabeth });
            state.Flags.UnionWith(new[] { "trickster", "seelah.committed", "arueshalae.committed" });
            if (partner is "active" or "past") state.Flags.Add("irabeth.lover");
            if (partner == "past") state.Flags.Add("irabeth.closed");
            return state;
        }
        Snapshot Play(string id, Snapshot initial, Func<Snapshot, bool>? select = null)
        {
            var scene = Get(id);
            var state = Program.Copy(initial);
            state.Hour += scene.DelayHours + 1;
            check(Rules.Available(story, scene, state), "Anevia actual predecessor unavailable: " + id);
            if (scene.ContactUnit != null)
            {
                var missing = Program.Copy(state);
                missing.AvailableContacts.Remove(scene.ContactUnit);
                check(!Rules.Available(story, scene, missing) && !Rules.ContactAvailable(story, scene, missing), "Missing actor permits entry or continuation: " + id);
                var moved = Program.Copy(state); moved.Area = "elsewhere";
                check(!Rules.ContactAvailable(story, scene, moved), "Anevia physical scene continues outside its area.");
            }
            var outcomes = Program.Walk(scene, state, (page, partial) =>
            {
                seen.Add(scene.Id + "/" + page);
                check(!partial.Has(scene.Id), "An unfinished page records scene completion.");
                check(state.Flags.IsSubsetOf(partial.Flags), "An unfinished page erases history.");
            });
            foreach (var result in outcomes)
            {
                check(state.Flags.IsSubsetOf(result.Flags), "Anevia clears existing history.");
                foreach (var item in state.Times)
                    check(result.Times[item.Key] == item.Value, "Anevia rewrites a predecessor timestamp.");
                check(result.Has("seelah.committed") && result.Has("arueshalae.committed"), "Anevia changes another partner.");
                check(result.Has("irabeth.closed") == state.Has("irabeth.closed") && result.Has("irabeth.lover") == state.Has("irabeth.lover"), "Anevia authors Irabeth's romance answer.");
                check(result.Has("a_affair") == state.Has("a_affair") && result.Has("i_affair") == state.Has("i_affair"), "Anevia fabricates an old affair.");
                check(!result.Has("closed"), "A local Anevia decision closes the legacy group globally.");
            }
            return outcomes.First(s => s.Has(scene.Id) && !s.Has("anevia.closed") && (select == null || select(s)));
        }
        Snapshot Acquire(int chapter, string partner)
        {
            var state = Fresh(chapter, partner);
            foreach (string id in new[] { "unborrowed_hour", "a_question_at_home", "beths_question", "beths_answer", "her_own_answer" })
                state = Play(id, state);
            check(state.Has("anevia.lover") && state.Has("anevia.personal_ready") && state.Has("anevia.marital_terms_agreed"), "Negotiated acquisition lacks actual agreement.");
            check(!state.Has("a_affair") && !state.Has("i_affair") && !state.Has("trying"), "Negotiated acquisition invents betrayal or a triad.");
            return state;
        }

        Snapshot? developed = null;
        foreach (int chapter in new[] { 3, 5 })
        foreach (string partner in new[] { "none", "active", "past" })
        {
            var acquired = Acquire(chapter, partner);
            foreach (string trace in new[] { "trace_read", "trace_failed", "trace_sorted", "trace_asked" })
            foreach (bool protectDema in new[] { false, true })
            foreach (bool savePapers in new[] { false, true })
            {
                var state = Play("borrowed_signature", acquired, s => s.Has("anevia.public_warning") == protectDema);
                state = Play("the_paper_seller", state, s => s.Has("anevia." + trace));
                check(state.Has("anevia.trace_cistern") == (trace is "trace_read" or "trace_sorted"), "A failed/unattempted reading invents the written location.");
                state = Play("the_woman_with_the_basket", state, s => s.Has("anevia.dema_spared") == protectDema);
                state = Play("the_counting_room", state, s => s.Has("anevia.saved_papers") == savePapers);
                check(state.Has("anevia.records_intact") == savePapers && state.Has("anevia.records_partial") != savePapers, "Evidence cost is not reflected in the result.");
                state = Play("what_the_warning_cost", state);
                state = Play("the_evening_without_a_case", state);
                if (chapter == 3)
                {
                    state = Play("departure_note", state);
                    state.Chapter = 4; state.Area = "abyss";
                    state = Play("the_blank_half", state, s => trace == "trace_read" ? s.Has("anevia.absence_shared_moment") : trace == "trace_failed" ? s.Has("anevia.absence_changed") : s.Has("anevia.absence_unwritten"));
                }
                state.Chapter = 5; state.Area = area;
                state = Play("the_life_she_lived", state);
                check(state.Has("anevia.departed_together") == (chapter == 3), "Fresh Chapter5 invents a pre-Abyss courtship.");
                state = Play("a_key_that_is_hers", state, s => s.Has("anevia.committed") == savePapers);
                state = Play("the_last_ordinary_thing", state);
                check(state.Has("anevia.developed"), "Played personal campaign has no developed completion.");
                var expected = Get(savePapers ? "ending_kept" : "ending_open");
                check(Rules.Available(story, expected, state), "Independent developed ending is inaccessible.");
                check(!Rules.Available(story, Get("ending_unfinished"), state), "Developed romance receives unfinished ending.");
                developed = state;
            }
        }
        check(developed != null, "No full Anevia trajectory was played.");

        // Earn the existing single affair rather than importing its positive flags.
        var affair = Fresh(5);
        foreach (string id in new[] { "a_cup", "a_errand", "a_roof", "a_crossing", "a_morning" })
        {
            var scene = story.Scenes.Single(s => s.Id == id); affair.Hour += 1000;
            check(Rules.Available(story, scene, affair), "Old single-affair predecessor unavailable: " + id);
            affair = Program.Walk(scene, affair).First(s => s.Has(id) && !s.Has("closed") && Program.LegacyTirabadeOutcome(s));
        }
        check(affair.Has("a_affair") && !affair.Has("i_affair"), "Single-affair witness has wrong native story history.");
        affair = Play("one_truth", affair);
        foreach (string id in new[] { "beths_question", "beths_answer", "her_own_answer" }) affair = Play(id, affair);
        check(affair.Has("a_affair") && affair.Has("anevia.single_affair_disclosed") && !affair.Has("i_affair"), "Disclosure rewrites the single affair.");

        // Play both original acquisitions and the original table for the old-save personal entry.
        var legacy = Fresh(5);
        Snapshot? beforeTable = null;
        foreach (string id in "a_cup i_watch a_errand i_hands a_roof i_respite a_crossing i_crossing a_morning i_morning reckoning a_truth i_truth table".Split(' '))
        {
            if (id == "table") beforeTable = Program.Copy(legacy);
            var scene = story.Scenes.Single(s => s.Id == id); legacy.Hour += 1000;
            check(Rules.Available(story, scene, legacy), "Legacy triad predecessor unavailable: " + id);
            legacy = Program.Walk(scene, legacy).First(s => s.Has(id) && !s.Has("closed") && Program.LegacyTirabadeOutcome(s));
        }
        var beforePersonal = Program.Copy(legacy);
        var oldTimes = new Dictionary<string, int>(legacy.Times);
        legacy = Play("a_place_of_our_own", legacy);
        check(legacy.Has("trying") && legacy.Has("a_affair") && legacy.Has("i_affair"), "Personal invitation deletes the triad's actual history.");
        foreach (var item in oldTimes) check(legacy.Times[item.Key] == item.Value, "Personal invitation replays old acquisition.");
        check(!Rules.Available(story, Get("one_truth"), legacy), "Two-affair history receives a one-affair confession.");

        // Explicit bridge output fixtures only; root must separately play the actual shared responses.
        foreach (var basis in new[] { beforeTable!, beforePersonal })
        {
            var split = Program.Copy(basis); split.Flags.Add("tirabade.group_closed");
            check(!Rules.Available(story, Get("an_invitation_afterward"), split), "Group closure invents an individual invitation.");
            split.Flags.Add("tirabade.anevia_continuation_invited");
            split = Play("an_invitation_afterward", split);
            check(split.Has("anevia.personal_ready") && split.Has("anevia.lover"), "Played post-group invitation strands individual continuation.");
            check(split.Has("trying") == basis.Has("trying") && split.Has("table") == basis.Has("table"), "New invitation fabricates or erases shared acquisition.");
            split = Play("borrowed_signature", split);
            check(split.Has("anevia.case_open"), "Post-group continuation cannot reach substantial professional material.");
        }

        foreach (string flag in new[] { "closed", "anevia.closed", "anevia_dead", "anevia_gone", "swarm", "true_lich" })
        {
            var state = Fresh(5); state.Flags.Add(flag);
            check(!Rules.Available(story, Get("unborrowed_hour"), state), "Fresh invitation ignores " + flag);
        }
        var local = Fresh(5); local.Flags.Add("irabeth.closed");
        check(Rules.Available(story, Get("unborrowed_hour"), local), "Irabeth-only refusal closes Anevia's independent acquisition.");

        // Reproduce the review's real early-acquisition history without the optional farewell.
        var noFarewell = Acquire(3, "active");
        var earlyDeparture = Play("departure_note", noFarewell);
        check(!earlyDeparture.Has("anevia.case_consequence_kept"), "Early departure fixture accidentally acquired the later plant.");
        check(!Get("departure_note").Nodes.Single(n => n.Id == "days").Text.Contains("the plant"), "Early goodbye recalls an unacquired cutting.");
        foreach (string id in new[] { "borrowed_signature", "the_paper_seller", "the_woman_with_the_basket", "the_counting_room", "what_the_warning_cost", "the_evening_without_a_case" })
            noFarewell = Play(id, noFarewell);
        check(!noFarewell.Has("anevia.departed_together"), "Skipped-farewell reproduction secretly played the optional visit.");
        noFarewell.Chapter = 5;
        var returnBook = Get("the_life_she_lived");
        var unlettered = returnBook.Nodes[0].Choices[1];
        check(Rules.Match(unlettered.Requires, unlettered.Forbids, noFarewell), "Early lover without a farewell lost the ordinary return conversation.");
        check(!unlettered.Text.Contains("began this after") && !returnBook.Nodes.Single(n => n.Id == "new_days").Text.Contains("still deciding whether to ask"), "Optional farewell still stands in for an acquisition date.");
        noFarewell = Play("the_life_she_lived", noFarewell);
        var promised = Play("a_key_that_is_hers", noFarewell, state => state.Has("anevia.committed"));
        check(promised.Has("anevia.future_chosen") && !promised.Has("anevia.developed"), "Provisional-commitment witness includes the final farewell.");
        check(Rules.Available(story, Get("ending_promised"), promised) && !Rules.Available(story, Get("ending_unfinished"), promised), "Earned lasting commitment is denied before the optional final farewell.");
        check(!Get("beths_answer").Nodes.Single(n => n.Id == "finish").Text.Contains("ordinary acquaintance"), "Active Irabeth lover is demoted by the shared agreement page.");
        var shortAscension = Acquire(5, "none"); shortAscension.Flags.Add("ascended");
        check(!shortAscension.Has("anevia.ordinary_life_kept") && Rules.Available(story, Get("ending_ascended"), shortAscension), "Ascension requires a game the lover never played.");
        check(!Get("ending_ascended").Nodes[0].Text.Contains("little game"), "Short ascension invents the optional game.");

        check(story.Etudes.TryGetValue("anevia.irabeth_killed_by_commander", out var killed) && killed == "c0f261c4a259da741ab0052f0100c2a0", "Commander-caused death is not bound to the actual native etude.");
        foreach (var loss in new[] {
            (Flag: "irabeth_dead", Ending: "ending_grief_unanswered"),
            (Flag: "irabeth_gone", Ending: "ending_wife_absent") })
        {
            var pending = Program.Copy(promised); pending.Flags.Add(loss.Flag);
            check(!pending.Has("anevia.survivor_continues"), "Provisional grief fixture fabricates a played continuation.");
            var endings = story.Scenes.Where(book => book.Relationship == "anevia" && book.Owner == "Epilogue" && Rules.Available(story, book, pending)).ToArray();
            check(endings.Length == 1 && endings[0].Id == "anevia." + loss.Ending, "Wife loss silently drops or duplicates earned romance before a new conversation: " + loss.Flag);
        }
        var departedBereaved = Program.Copy(promised);
        departedBereaved.Flags.UnionWith(new[] { "irabeth_dead", "anevia_gone", "anevia_away" });
        departedBereaved.AvailableContacts.Remove(anevia);
        check(!Rules.Available(story, Get("a_grief_with_a_name"), departedBereaved), "Native post-coronation departure is bypassed for a grief visit.");
        check(Rules.Available(story, Get("ending_gone"), departedBereaved), "Native departure loses the earned relationship's provisional outcome.");
        var responsible = Program.Copy(promised);
        responsible.Flags.UnionWith(new[] { "irabeth_dead", "anevia.irabeth_killed_by_commander" });
        check(!Rules.Available(story, Get("a_grief_with_a_name"), responsible), "Commander who killed Irabeth gets generic support.");
        foreach (bool gone in new[] { false, true })
        {
            if (gone) responsible.Flags.Add("anevia_gone");
            var endings = story.Scenes.Where(book => book.Relationship == "anevia" && book.Owner == "Epilogue" && Rules.Available(story, book, responsible)).ToArray();
            check(endings.Length == 1 && endings[0].Id == "anevia.ending_wife_killed", "Personal responsibility receives contradictory generic bereavement/absence outcome.");
        }

        // Conditional source coverage only. Native post-Iz free-dialogue availability is not proved.
        var surviving = Program.Copy(developed!); surviving.Flags.Add("irabeth_dead");
        surviving = Play("a_grief_with_a_name", surviving);
        check(Rules.Available(story, Get("ending_survivor"), surviving), "Irabeth's death globally kills Anevia's continuation.");
        check(!Rules.Available(story, Get("ending_kept"), surviving) && !Rules.Available(story, Get("ending_open"), surviving), "Bereavement retains an intact-marriage ending.");

        var joint = Program.Copy(developed!); joint.Flags.Add("trying");
        var end = Get(joint.Has("anevia.committed") ? "ending_kept" : "ending_open");
        check(!Rules.Available(story, end, joint), "Personal ending contradicts an active legacy shared ending.");
        joint.Flags.Add("tirabade.group_closed");
        check(Rules.Available(story, end, joint), "Actual group closure cannot permit a continuing individual ending.");
        joint.Flags.Add("closed");
        check(!Rules.Available(story, end, joint), "Group closure overrides a global personal refusal.");

        foreach (var outcome in new[] {
            (Flag: "anevia_dead", Ending: "ending_death"),
            (Flag: "anevia_gone", Ending: "ending_gone"),
            (Flag: "sacrifice", Ending: "ending_sacrifice"),
            (Flag: "ascended", Ending: "ending_ascended"),
            (Flag: "inhuman", Ending: "ending_changed_power") })
        {
            var state = Program.Copy(developed!); state.Flags.Add(outcome.Flag);
            var endings = story.Scenes.Where(s => s.Relationship == "anevia" && s.Owner == "Epilogue" && Rules.Available(story, s, state)).ToArray();
            check(endings.Length == 1 && endings[0].Id == "anevia." + outcome.Ending, "Contradictory or missing independent fate ending: " + outcome.Flag);
            state.Flags.Add("anevia.closed");
            check(!Rules.Available(story, Get(outcome.Ending), state), "Historical lover flag ignores local closure at ending dispatch.");
        }
        check(Rules.Available(story, Get("ending_aeon"), developed!), "Aeon-only dispatcher has no independent memory-ending page.");

        foreach (var scene in story.Scenes.Where(s => s.Relationship == "anevia" && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)))
        {
            check(scene.Remote || scene.ContactUnit == (scene.Owner == "Irabeth" ? irabeth : anevia), "Wrong native contact on " + scene.Id);
            check(scene.Remote || Rules.EntryTargets(scene).SequenceEqual(new[] { scene.Owner == "Irabeth" ? "871af36f2ab2b1f40b5de77976c54276" : "33960c7f7af40cd43b7f801a76c87a0b" }), "Wrong native dialogue attachment.");
            foreach (var page in scene.Nodes) check(seen.Contains(scene.Id + "/" + page.Id), "Unplayed independent page: " + scene.Id + "/" + page.Id);
        }
    }
}
