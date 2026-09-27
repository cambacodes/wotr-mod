using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiReturnInvitationTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var letter = story.Scenes.Single(s => s.Id == "konomi.return_letter");
        var first = story.Scenes.Single(s => s.Id == "konomi.return_first_words");
        const string proof = "konomi.retained_return_confirmed";
        const string correspondence = "konomi.return_correspondence_available";
        const string contact = "konomi.return_contact_available";
        const string accepted = "konomi.return_meeting_accepted";
        const string declined = "konomi.return_visit_declined";
        const string unit = "ca2d58c5c65723945857e04fb85d30ce";
        var reached = new HashSet<string>();
        check(Rules.IsRemote(letter) && letter.AfterRecovery == "konomi" && letter.ContactUnit == null,
            "Invitation requires physical arrival before the hidden woman can reply.");
        check(letter.DelayHours == 12 && first.Requires.Contains(accepted), "Invitation timing or earned first-visit consent is missing.");
        foreach (int chapter in new[] { 3, 5 })
        foreach (string office in new[] { "active", "dismissed", "unappointed" })
        foreach (string prior in new[] { "unmet", "lover", "closed", "farewell", "parted" })
        {
            var state = new Snapshot { Chapter = chapter, Area = letter.Areas.Single(), Hour = 500 };
            state.Flags.UnionWith(new[] { proof, correspondence, "legend", "seelah.committed" });
            state.Times[proof] = state.Hour;
            if (office == "active") state.Flags.Add("konomi.present");
            if (office == "dismissed") state.Flags.UnionWith(new[] { "konomi.dismissed", "konomi.office_completed" });
            if (prior == "lover") state.Flags.Add("konomi.lovers");
            if (prior == "closed") state.Flags.Add("konomi.closed");
            if (prior == "farewell") state.Flags.Add("konomi.farewell");
            if (prior == "parted") state.Flags.Add("konomi.private_parted");
            check(!Rules.Available(story, letter, state), "Return letter ignored recovery rest interval.");
            state.Hour += 12;
            check(Rules.Available(story, letter, state), "Living hidden restored Konomi cannot answer a personal letter.");
            check(!Rules.Available(story, first, state), "Remote eligibility became physical access.");
            var outcomes = Program.Walk(letter, state, (node, _) => reached.Add(node));
            check(outcomes.Any(s => !s.Has(letter.Id) && !s.Has(accepted) && !s.Has(declined)),
                "Postponing a letter completed or refused it.");
            check(outcomes.Any(s => s.Has(declined)) && outcomes.Any(s => s.Has(accepted)), "Invitation lost refusal or acceptance.");
            foreach (var outcome in outcomes)
            {
                check(state.Flags.All(outcome.Has), "Correspondence removed prior history or another romance.");
                check(outcome.Flags.Except(state.Flags).All(flag => flag == letter.Id || flag == accepted || flag == declined),
                    "Correspondence invented office, romance, recovery or arrival evidence.");
                check(!Rules.Available(story, first, outcome), "Accepted correspondence alone manufactured physical arrival.");
                var arrived = Program.Copy(outcome);
                arrived.Flags.Add(contact);
                arrived.AvailableContacts.Add(unit);
                check(Rules.Available(story, first, arrived) == outcome.Has(accepted),
                    "Actual physical availability ignored the reply or failed after consent.");
                if (outcome.Has(letter.Id)) check(!Rules.Available(story, letter, outcome), "Completed correspondence replays.");
                else check(Rules.Available(story, letter, outcome), "Postponed correspondence cannot be resumed.");
            }
            foreach (string required in new[] { proof, correspondence })
            {
                var absent = Program.Copy(state); absent.Flags.Remove(required);
                check(!Rules.Available(story, letter, absent) && !Rules.ContactAvailable(story, letter, absent),
                    "Remote reply ignored lost positive evidence: " + required);
            }
            var dead = Program.Copy(state); dead.Flags.Add("konomi.retained_dead");
            check(!Rules.Available(story, letter, dead) && !Rules.ContactAvailable(story, letter, dead), "Dead Konomi answers a new letter.");
            var completed = Program.Copy(state); completed.Flags.Add(first.Id);
            check(!Rules.Available(story, letter, completed), "An existing completed first visit demands retroactive consent.");
        }
        check(reached.SetEquals(letter.Nodes.Select(node => node.Id)), "Invitation has an unplayed page.");
    }
}
