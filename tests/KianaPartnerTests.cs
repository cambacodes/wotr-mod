using System;
using System.Linq;
using Tirabade;

internal static class KianaPartnerTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        var state = new Snapshot { Chapter = 5, Hour = 10000, Area = "2570015799edf594daf2f076f2f975d8" };
        state.Flags.UnionWith(new[] { "trickster", "chapter_later", "seelah.souls_returned", "seelah.in_party" });
        state.AvailableContacts.Add("180b0eaa5dce387458d2ebf0ee943985");
        Rules.Complete(story, state);
        Snapshot Earn(string id, Snapshot input, string flag)
        {
            var ready = Program.Copy(input); ready.Hour += 200;
            Rules.Complete(story, ready);
            check(Rules.Available(story, S(id), ready), "Partner producer unavailable: " + id);
            var result = Program.Walk(S(id), ready).FirstOrDefault(r => r.Has(flag) && !r.Has("kiana.closed"));
            check(result != null, "Partner producer has no earned path: " + id + " -> " + flag);
            return result!;
        }
        state = Earn("kiana.trickster.aftermath.letter_waited", state, "kiana.trickster.met");
        state = Earn("kiana.marriage", state, "kiana.waited");
        state = Earn("kiana.answer", state, "kiana.partner_unsettled");
        state = Earn("kiana.date", state, "kiana.lovers");
        state.Hour += 200;
        foreach (string id in new[] { "kiana.morning", "kiana.trickster.late_question" })
        {
            var ready = Program.Copy(state); Rules.Complete(story, ready);
            check(Rules.Available(story, S(id), ready), "Unsettled partner blocks existing commitment host: " + id);
            var outcomes = Program.Walk(S(id), ready);
            foreach (string stance in new[] { "share", "exclusive", "secret" })
            {
                var accepted = outcomes.Where(r => r.Has("kiana.committed") && r.Has("kiana.partner_stance." + stance)).ToArray();
                check(accepted.Length > 0, id + ": missing earned " + stance);
                foreach (var result in accepted)
                {
                    check(new[] { "share", "exclusive", "secret" }.Count(s => result.Has("kiana.partner_stance." + s)) == 1,
                        "Commitment records competing stances");
                    check(result.Has("kiana.separated") == (stance == "exclusive"), "Stance silently changes marriage");
                    if (stance == "share") check(result.Has("kiana.partner_elan_terms_kept"), "Share skips Elan's answer");
                    if (stance == "exclusive") check(result.Has("kiana.partner_breakup_spoken"), "Exclusive skips breakup reaction");
                    if (stance == "secret") check(result.Has("kiana.affair"), "Secret skips affair receipt");
                }
            }
            check(outcomes.Any(r => r.Has("kiana.closed") && r.Has("kiana.partner_stance.exclusive") && !r.Has("kiana.committed")),
                "Kiana cannot refuse an exclusive order");
            var affair = outcomes.First(r => r.Has("kiana.partner_stance.secret") && r.Has("kiana.committed"));
            Rules.Complete(story, affair);
            var discovery = S("kiana.partner_discovery");
            check(discovery.AnswerLists.SequenceEqual(new[] { "a237e3aaab7c937468829bba3578770d" })
                && Rules.Available(story, discovery, affair), "Affair cannot be exposed at native reconciliation");
            foreach (var exposed in Program.Walk(discovery, affair))
                check(exposed.Has("kiana.partner_secret_exposed") && exposed.Has("kiana.closed") && !exposed.Has("kiana.separated"),
                    "Discovery gives free forgiveness or silently breaks the marriage");
            var dead = Program.Copy(affair); dead.Flags.Add("kiana.elan.death_seen"); Rules.Complete(story, dead);
            check(!Rules.Available(story, discovery, dead), "Dead Elan appears at discovery");
        }
        check(story.SeenCues["kiana.elan.death_seen"].Contains("10eb3a708933ebc4c865ed9ae6e72805"), "Death evidence is missing");
        Console.WriteLine("PASS: Kiana earned share/exclusive/secret, refusal, native discovery and death negatives.");
    }
}
