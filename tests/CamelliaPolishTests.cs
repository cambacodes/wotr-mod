using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Reviewed polish: fresh native observations, real payments and encounter-specific callbacks.
// No pre-aged return or derived-outcome fixtures are used for the timing acceptance.
internal static class CamelliaPolishTests
{
    const string P = "camellia.trickster.";
    const string Dead = "camellia.dead", Killed = "camellia.killed";

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == P + id);
        Node N(Scene scene, string id) => scene.Nodes.Single(n => n.Id == id);
        Snapshot Fresh(params string[] flags)
        {
            var state = new Snapshot { Chapter = 3, Hour = 0,
                Area = "2570015799edf594daf2f076f2f975d8",
                CrusadeResources = new Dictionary<string, int> { ["Finances"] = 100 } };
            state.Flags.UnionWith(new[] { "trickster", "chapter_later" }.Concat(flags));
            Observe(state);
            return state;
        }
        void Observe(Snapshot state)
        {
            // Main.State rebuilds composites. Main.RecordLatches persists observed latch flags and their hour.
            state.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
            var before = new HashSet<string>(state.Flags);
            Rules.Complete(story, state);
            foreach (var key in story.Latches.Keys.Where(k => state.Has(k) && !before.Contains(k)))
                state.Times[key] = state.Hour;
        }
        bool Available(Scene scene, Snapshot state) => Rules.Available(story, scene, state);
        var third = S("killed.third_night");
        var late = S("killed.late_curtain");
        var prepaid = S("killed.late_curtain_prepared");
        var physical = S("killed.performance");
        var letter = S("killed.performance_letter");
        foreach (var exposure in new[] { "camellia.mireya_unmasked", P + "amulet_kept" })
        {
            var state = Fresh(exposure);
            foreach (var (scene, old, known) in new[] {
                (S("masks.mireya"), "who", "who_known"), (S("cards.a_bowl_for_mireya"), "her", "her_known") })
                check(!Rules.ChoiceAvailable(N(scene, "open").Choices[0], state)
                    && Rules.ChoiceAvailable(N(scene, "open").Choices[1], state)
                    && N(scene, "open").Choices[0].Next == old && N(scene, "open").Choices[1].Next == known,
                    "Camellia: exposure replays an ignorant introduction or shifts the saved answer index.");
            var bowl = N(S("cards.a_bowl_for_mireya"), "her_known").Choices;
            check(bowl.Take(3).Select(c => c.Next).SequenceEqual(new[] { "hold", "refuse", "grace" })
                && bowl.Where(c => Rules.ChoiceAvailable(c, state)).Select(c => c.Next)
                    .SequenceEqual(new[] { "hold_known", "grace_known", "refuse_known" }),
                "Camellia: known bowl participation lost the saved slots or informed alternatives.");
        }
        foreach (var suffix in new[] { "", "_camp", "_alive" })
        {
            var dance = S("day.the_second_dance" + suffix);
            var state = Fresh(P + "encounter.knife_off");
            check(!Rules.ChoiceAvailable(N(dance, "morning.dance").Choices[0], state)
                && Rules.ChoiceAvailable(N(dance, "morning.dance").Choices[1], state),
                "Camellia: an earlier knife-off encounter selected this dance's morning.");
            state.Flags.Add(dance.Id + ".knife_off");
            check(Rules.ChoiceAvailable(N(dance, "morning.dance").Choices[0], state)
                && !Rules.ChoiceAvailable(N(dance, "morning.dance").Choices[1], state),
                "Camellia: this dance's knife receipt did not select its morning.");
            var breakfast = S("evening.breakfast" + suffix);
            state.Flags.UnionWith(new[] { "not_today", "all", "mine", "knife_off", "knife_on" }
                .Select(o => P + "encounter." + o + ".morning"));
            var shown = N(breakfast, "open").Choices.Where(c => Rules.ChoiceAvailable(c, state)).ToArray();
            check(shown.Length == 5 && shown.Select(c => c.Text).Distinct().Count() == 5,
                "Camellia: coexisting breakfast memories are indistinguishable or unavailable.");
        }
        var refused = S("epilogue.refused_living");
        foreach (var source in new[] { "returned.terms_alive", "returned.test_alive" })
        {
            var state = Fresh("camellia.closed", P + source); state.Chapter = 6; Observe(state);
            check(Available(refused, state), "Camellia: a living terms/test refusal has no personal closure page.");
            foreach (var loss in new[] { Dead, Killed, "camellia.kicked_out", "sacrifice" })
            {
                var lost = Program.Copy(state); lost.Flags.Add(loss); Observe(lost);
                check(!Available(refused, lost), "Camellia: living refusal leaks through " + loss);
            }
        }
        var early = Fresh("camellia.closed"); early.Chapter = 6; Observe(early);
        check(!Available(refused, early), "Camellia: early shutdown was rewritten as a late personal refusal.");
        check(physical.DelayHours == 0 && letter.DelayHours == 96, "Camellia: reunion delay still repeats the custody wait.");
        // The unprepared zero-delay return lets delivery timing be proved independently of A1's blocked clock.
        var awaitingRaise = Fresh(Killed, Dead);
        awaitingRaise.Hour = 200; Observe(awaitingRaise);
        check(Available(late, awaitingRaise), "Camellia: a confirmed unprepared corpse has no late return.");
        var raised = Program.WalkVia(late, awaitingRaise, "scroll", 0).First(w => w.Has(P + "raised"));
        check(raised.Times[P + "raised"] == 200 && raised.CrusadeResources!["Finances"] == 0
            && raised.Has(P + "cost.sexton_paid"), "Camellia: the real hour-200 raise skipped its service payment.");
        raised.AvailableContacts.Add("397b090721c41044ea3220445300e1b8"); Observe(raised);
        check(Available(physical, raised), "Camellia: a new raise cannot meet the physical mourner at hour 200.");
        raised.Flags.Add("camellia.presence.failed"); raised.AvailableContacts.Clear();
        raised.Hour = 295; Observe(raised); check(!Available(letter, raised), "Camellia: fallback letter arrived before hour 296.");
        raised.Hour = 296; Observe(raised); check(Available(letter, raised), "Camellia: failed contact cannot receive the 96-hour fallback.");
        raised.Flags.Remove("camellia.presence.failed"); Observe(raised);
        check(!Available(letter, raised), "Camellia: a fallback letter appeared without failed contact.");
        raised.Flags.UnionWith(new[] { "camellia.presence.failed", physical.Id }); Observe(raised);
        check(!Available(letter, raised), "Camellia: a successful reunion received a second delivery.");

        Console.WriteLine("PASS: Camellia exposure, current dance mornings, living refusals and real 0/96-hour delivery checks.");
        check(story.Latches.TryGetValue(P + "native_death_observed", out var deathSources) && deathSources.SequenceEqual(new[] { Dead })
            && story.Derived[P + "death_observed"].Single().SequenceEqual(new[] { P + "native_death_observed" })
            && story.Derived[P + "killed_corpse_observed"].Single().SequenceEqual(new[] { Killed, Dead }),
            "Camellia: the native death clock or current execution/corpse gate is missing.");
        foreach (var origin in new[] { "hub", "q1_order", "q3_verdict" })
        {
            var state = Fresh(Killed, P + "primed");
            if (origin == "q3_verdict") state.Chapter = 5;
            state.Hour = 100; Observe(state);
            check(!state.Has(P + "death_observed") && !Available(third, state)
                && !Available(late, state) && !Available(prepaid, state),
                "Camellia: unresolved combat opened a coffin: " + origin);
            state.Flags.Add(Dead); Observe(state);
            check(state.Has(P + "death_observed") && state.Times[P + "native_death_observed"] == 100,
                "Camellia: derived corpse observation was not latched by a fresh production snapshot at hour 100.");
            state.Hour = 171; Observe(state);
            check(!Available(third, state), "Camellia: the third night began before 72 hours dead.");
            state.Hour = 172; Observe(state);
            check(Available(third, state) && N(third, "start").Choices[0].Crusade?.Amount == -100,
                "Camellia: the third night did not open at 72 hours dead.");
            state.Flags.Remove(Dead); Observe(state);
            check(!Available(third, state), "Camellia: a stale death timestamp certified a living actor.");
        }
        var battlefield = Fresh(Dead);
        check(battlefield.Has(P + "death_observed") && !Available(third, battlefield),
            "Camellia: an observed battlefield death supplied execution eligibility.");
        battlefield.Flags.Remove(Dead);
        battlefield.Flags.UnionWith(new[] { Killed, P + "returned" }); Observe(battlefield);
        check(!Available(late, battlefield) && !Available(prepaid, battlefield),
            "Camellia: an earlier battlefield revival bought a second unresolved return.");

        foreach (bool paid in new[] { false, true })
        {
            var state = Fresh(Killed);
            if (paid) state.Flags.Add(P + "spirits_bargained");
            state.Hour = 100; state.Flags.Add(Dead); Observe(state);
            check(Available(late, state) == !paid && !Available(prepaid, state),
                "Camellia: an unprimed prepaid kill got the immediate/dearer fallback.");
            state.Hour = 172; Observe(state);
            var host = paid ? prepaid : late;
            check(Available(host, state) && !Available(paid ? late : prepaid, state),
                "Camellia: fallback preparation histories overlap or have no host.");
            check(!N(host, "coffin").Choices[0].Set.Contains(P + "raised")
                && N(host, "scroll").Choices[0].Set.Contains(P + "raised"),
                "Camellia: the fallback records life before showing breath.");
            var outcomes = Program.WalkVia(host, state, "scroll", 0);
            check(outcomes.Count > 0 && outcomes.All(w => w.Has(P + "raised")
                && w.Has(P + "cost.sexton_paid") && w.CrusadeResources!["Finances"] == 0
                && w.Has(P + "cost.bargain_late") == !paid),
                "Camellia: the service was not paid once, or the prepaid return was charged a late bargain.");
            foreach (int? finances in new int?[] { 99, null })
            {
                var poor = Program.Copy(state);
                poor.CrusadeResources = finances.HasValue ? new Dictionary<string, int> { ["Finances"] = finances.Value } : null;
                check(!Rules.ChoiceAvailable(N(host, "choose").Choices[0], poor)
                    && Rules.ChoiceAvailable(N(host, "choose").Choices[1], poor),
                    "Camellia: unaffordable digging or missing refusal exit.");
            }
        }
        Console.WriteLine("PASS: Camellia reviewed polish histories, payments, callbacks and living refusal.");
    }
}
