using System;
using System.Linq;
using Tirabade;

internal static class KonomiPrivateHearingTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        var hearing = story.Scenes.SingleOrDefault(s => s.Id == "konomi.private_hearing");
        check(hearing != null, "Dismissed Konomi has no playable path to finish the pending hearing after her private return.");
        if (hearing == null) return;
        var after = story.Scenes.Single(s => s.Id == "konomi.private_hearing_after");
        var letter = story.Scenes.Single(s => s.Id == "konomi.private_new_letter");
        foreach (int chapter in new[] { 3, 5 })
        foreach (bool publicReply in new[] { false, true })
        foreach (bool priorDenial in new[] { false, true })
        {
            var initial = new Snapshot { Chapter = chapter, Hour = 1000, Area = hearing.Areas.Single() };
            initial.Flags.UnionWith(hearing.Requires);
            initial.Flags.UnionWith(new[] { "legend", "konomi.lovers", "seelah.committed", "konomi.private_hearing_needed" });
            initial.Flags.Add(publicReply ? "konomi.public" : "konomi.discreet");
            if (priorDenial) initial.Flags.UnionWith(new[] { "konomi.almost_denied", "konomi.apologized" });
            check(Rules.Available(story, hearing, initial), "Restored private contact cannot attend its pending hearing.");
            foreach (var result in Program.Walk(hearing, initial))
            {
                if (!result.Has(hearing.Id))
                {
                    check(result.Flags.SetEquals(initial.Flags), "Postponed private hearing writes a finding.");
                    continue;
                }
                check(result.Has("konomi.hearing_finished") && result.Has("konomi.hearing_buyer_barred") != result.Has("konomi.hearing_buyer_unbarred"), "Private hearing loses the actual evidence outcome.");
                check(!Rules.Available(story, after, result), "Private hearing aftermath skips its delay.");
                result.Hour += 24;
                check(Rules.Available(story, after, result), "Private hearing aftermath cannot continue.");
                foreach (var evening in Program.Walk(after, result))
                {
                    check(evening.Has("konomi.hearing_evening_kept") && evening.Has("konomi.hearing_trust_repaired") == priorDenial, "Private hearing invents or loses trust repair.");
                    check(evening.Has("seelah.committed") && !evening.Has("konomi.present") && evening.Has("konomi.office_completed"), "Private hearing changes other romances or restores her native office.");
                    evening.Hour += 24;
                    check(Rules.Available(story, letter, evening) == evening.Has("konomi.hearing_new_letter"), "Private hearing loses or invents a promised letter.");
                    if (!evening.Has("konomi.hearing_new_letter")) continue;
                    foreach (var outing in Program.Walk(letter, evening).Where(s => s.Has(letter.Id)))
                    {
                        check(outing.Has("konomi.new_letter_outing") && outing.Has("seelah.committed"), "Private letter does not deliver its outing or erases another commitment.");
                        var nativeContact = Program.Copy(outing); nativeContact.Flags.Add("konomi.present");
                        foreach (string original in new[] { "hearing", "hearing_after", "new_letter" })
                            check(!Rules.Available(story, story.Scenes.Single(s => s.Id == "konomi." + original), nativeContact), "Contact change replays an already completed shared event: " + original);
                    }
                }
            }
        }
        foreach (var scene in new[] { hearing, after, letter })
        {
            var ready = new Snapshot { Chapter = 5, Area = scene.Areas.Single(), Hour = 1000 };
            ready.Flags.UnionWith(scene.Requires);
            check(Rules.Available(story, scene, ready), "Private hearing readiness fixture invalid.");
            check(scene.Remote && !Rules.EntryTargets(scene).Any(), "Private hearing wrongly attaches to dismissed officer dialogue.");
            foreach (string flag in scene.Requires)
            {
                var state = Program.Copy(ready); state.Flags.Remove(flag);
                check(!Rules.Available(story, scene, state), "Private hearing ignores contact or progression requirement: " + flag);
            }
            foreach (string flag in new[] { "konomi.present", "inhuman", "konomi.closed", "konomi.farewell", "konomi.private_future" })
            {
                var state = Program.Copy(ready); state.Flags.Add(flag);
                check(!Rules.Available(story, scene, state), "Private hearing ignores unavailable contact: " + flag);
            }
            ready.Times[scene.Requires.Last()] = 1000;
            ready.Hour = 1000 + scene.DelayHours - 1;
            check(!Rules.Available(story, scene, ready), "Private hearing skips its scheduling delay.");
            ready.Hour++;
            check(Rules.Available(story, scene, ready), "Private hearing misses its exact scheduling boundary.");
            ready.Chapter = 4;
            check(!Rules.Available(story, scene, ready), "Private hearing creates an Abyss meeting.");
        }
        var migrated = new Snapshot { Chapter = 5, Area = hearing.Areas.Single(), Hour = 1000 };
        migrated.Flags.UnionWith(hearing.Requires);
        migrated.Flags.UnionWith(new[] { "konomi.hearing", "konomi.hearing_finished", "konomi.hearing_buyer_barred" });
        check(!Rules.Available(story, hearing, migrated) && Rules.Available(story, after, migrated), "A hearing completed before dismissal must resume at its unfinished aftermath.");
        migrated.Flags.UnionWith(new[] { "konomi.hearing_after", "konomi.hearing_evening_kept", "konomi.hearing_new_letter" });
        check(!Rules.Available(story, after, migrated) && Rules.Available(story, letter, migrated), "A promise made before dismissal must resume at its unfinished outing.");
        migrated.Flags.UnionWith(new[] { "konomi.new_letter", "konomi.new_letter_outing" });
        check(!Rules.Available(story, letter, migrated), "A pre-dismissal outing must not repeat after contact changes.");
    }
}
