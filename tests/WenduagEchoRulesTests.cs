using System;
using System.Linq;
using Tirabade;

internal static class WenduagEchoRulesTests
{
    internal static void Run(Story story, Action<bool, string> check)
    {
        const string E = Rules.WenduagEchoPrefix;
        const string W = "wenduag.trickster.";
        const string unit = "ae766624c03058440a036de90a7f2009";
        Scene Scene(string id) => story.Scenes.Single(s => s.Id == id);
        void Refresh(Snapshot state)
        {
            state.Flags.ExceptWith(story.Derived.Keys.Concat(story.Counts.Keys));
            Rules.Complete(story, state); // BuildState observes a fresh snapshot every frame.
        }
        Snapshot World(int chapter, params string[] flags)
        {
            var state = new Snapshot { Chapter = chapter, Hour = 9000, Area = Rules.NurahCapital };
            state.Flags.UnionWith(flags);
            Rules.Complete(story, state);
            foreach (string flag in state.Flags) state.Times[flag] = 0;
            return state;
        }
        var pickup = Scene(E + "pickup");
        var down = World(4, "trickster", "trickster.foresight.accepted", E + "ready", E + "valid",
            E + "casualty_available", "wenduag.abyss_fell", "wenduag.dead_any");
        down.SceneContacts.Add(pickup.Id);
        check(!down.AvailableContacts.Contains(unit), "Pickup leaked into shared conscious contacts");
        check(Rules.Available(story, pickup, down), "Unconscious original cannot enter pickup");
        check(Rules.ContactAvailable(story, pickup, down), "Pickup continuation lost the unconscious original");
        foreach (var scene in story.Scenes.Where(s => s.ContactUnit == unit && s.Id != pickup.Id))
            check(!Rules.ContactAvailable(story, scene, down), "Unconscious pickup exposed sibling contact: " + scene.Id);
        var lost = Program.Copy(down);
        lost.SceneContacts.Clear();
        check(!Rules.Available(story, pickup, lost) && !Rules.ContactAvailable(story, pickup, lost), "Pickup retained unresolved contact");
        foreach (string closure in new[] { "wenduag.killed", "wenduag.closed", "wenduag.kicked_out", "trickster.failed", "legend", "dragon", "swarm" })
        {
            var blocked = Program.Copy(down);
            blocked.Flags.Add(closure);
            Refresh(blocked);
            check(!Rules.Available(story, pickup, blocked), "Pickup bypassed closure/path: " + closure);
        }
        var returned = World(5, "trickster", "trickster.foresight.accepted", E + "ready", E + "rescued", E + "returned",
            E + "valid", W + "returned", W + "primed", W + "proved", W + "gate_seen",
            "wenduag.started", "wenduag.committed", "wenduag.abyss_fell", "wenduag.dead_any");
        returned.AvailableContacts.Add(unit);
        check(returned.Has(W + "with_you") && returned.Has(W + "partner"), "Valid echo return lost inherited presence");
        check(story.NativeEpilogueEdits.Values.Any(e => e.When.Any(g => g.Contains("wenduag.committed"))
            && Rules.WhenHolds(e.When, returned)), "Live Trickster control lost its native ending variant");
        var courting = World(5, "trickster", "trickster.foresight.accepted", E + "ready", E + "rescued", E + "returned",
            E + "valid", W + "returned", W + "primed", "wenduag.started", "wenduag.abyss_fell", "wenduag.dead_any");
        courting.AvailableContacts.Add(unit);
        foreach (string suffix in new[] { "trial", "gate", "claim" })
        {
            var scene = Scene(W + "court." + suffix);
            check(Rules.Available(story, scene, courting), "Echo courtship lost its next surface: " + suffix);
            var outcomes = Program.Walk(scene, courting);
            string earned = suffix == "trial" ? W + "proved" : suffix == "gate" ? W + "gate_seen" : "wenduag.committed";
            courting = outcomes.First(s => s.Has(earned));
            courting.Hour += 100;
        }
        check(courting.Has("wenduag.committed") && !courting.Has("wenduag.in_party"), "Echo claim required recruitment or failed commitment");
        foreach (string problem in new[] { "actor.dead", "custody.corrupt", "actor.duplicate", "legend", "dragon", "swarm", "trickster.failed" })
        {
            var invalid = Program.Copy(returned);
            invalid.Flags.Add(problem);
            invalid.Flags.Add(E + "unavailable"); // Observation supplies this for death, corruption, duplicates and path loss.
            invalid.AvailableContacts.Clear();
            Refresh(invalid);
            check(invalid.Flags.Contains(W + "returned") && !invalid.Has(W + "returned"), "Historical return was erased or remained sufficient");
            foreach (string flag in new[] { W + "with_you", W + "partner", W + "late_committed", "wenduag.harem.voice.pack" })
                check(!invalid.Has(flag), "Invalid custody retained eligibility: " + flag);
            foreach (var scene in story.Scenes.Where(s => s.Relationship == "wenduag" && s.Recovery == null))
                check(!Rules.Available(story, scene, invalid), "Invalid custody retained interaction/ending: " + scene.Id);
            foreach (var edit in story.NativeEpilogueEdits.Values.Where(e => e.When.Any(group => group.Contains("wenduag.committed"))))
                check(!Rules.WhenHolds(edit.When, invalid), "Invalid/off-path echo retained native ending edit");
            foreach (var suppression in story.NativeEpilogueSuppressions.Values.Where(s => s.Relationship == "wenduag"))
                check(!Rules.WhenHolds(suppression.When, invalid), "Invalid/off-path echo retained native slide suppression");
        }
        foreach (string gone in new[] { "alive", "lann.dead", "lann.kicked_out", "lann.plot_absent", "unknown" })
        {
            var ending = Program.Copy(returned);
            ending.Flags.Add(E + "cost.used_lann");
            if (gone == "alive") ending.Flags.Add("lann.in_party");
            else if (gone != "unknown") ending.Flags.Add(gone);
            foreach (string suffix in new[] { "pack", "unclaimed", "refused" })
            {
                var cost = Scene(W + "epilogue." + suffix).Nodes[0].Paragraphs.Where(p => p.Requires.Contains(E + "cost.used_lann")).ToArray();
                check(cost.Count(p => Rules.ParagraphVisible(p, ending)) == (gone == "unknown" ? 0 : 1), "Lann ending cost contradicted state: " + gone + "/" + suffix);
            }
        }
        Console.WriteLine("PASS: Wenduag echo scoped pickup, continuation, retained claim contact, invalid custody consumers and Lann ending variants.");
    }
}
