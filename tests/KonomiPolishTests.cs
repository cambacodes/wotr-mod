using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class KonomiPolishTests
{
    internal static void CheckProvenance(Scene scene, string page, Snapshot state, Action<bool, string> check)
    {
        string? original = scene.Id switch
        {
            "konomi.before_road" => "new",
            "konomi.chosen_evening" => "pleasure",
            "konomi.private_last_visit" => "business",
            _ => null
        };
        if (original == null || (page != original && page != "missed_" + original)) return;
        bool voluntary = state.Has("konomi.missed_private_access") && !state.Has("konomi.dismissed");
        check((page == "missed_" + original) == voluntary, "Konomi polish: played private history invents a dismissal.");
        string prose = scene.Nodes.Single(n => n.Id == page).Text;
        check(!voluntary || (!prose.Contains("lost the court") && !prose.Contains("lost the office")
            && !prose.Contains("dismissed")), "Konomi polish: voluntary rendered callback loses her credentials.");
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == "konomi." + id);
        const string access = "konomi.missed_private_access";
        const string dismissed = "konomi.dismissed";
        const string accredited = "konomi.trickster.cost.accredited";
        const string audience = "konomi.trickster.never_arrived.audience";

        // Completion, rather than placement, payment or a remote substitute, supplies the witness.
        var courtyard = S("the_courtyard_introduction");
        var start = courtyard.Nodes.Single(n => n.Id == "start");
        foreach (bool physical in new[] { false, true })
        foreach (bool letter in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 3, Hour = 5000 };
            state.Flags.UnionWith(new[] { accredited, "konomi.trickster.returned", "konomi.trickster.arrived", "konomi.missed_appointment" });
            if (physical) state.Flags.Add(audience);
            if (letter) state.Flags.Add("konomi.trickster.never_arrived.audience_letter");
            check(Rules.ChoiceAvailable(start.Choices[3], state) == physical,
                "Konomi polish: credentials callback lacks a completed physical audience.");
            check(Rules.ChoiceAvailable(start.Choices[4], state) == !physical,
                "Konomi polish: remote/no-witness history loses its first meeting.");
            check(start.Choices[2].Abort && Rules.ChoiceAvailable(start.Choices[2], state),
                "Konomi polish: courtyard postponement was lost.");
            var pages = new HashSet<string>();
            var outcomes = Program.Walk(courtyard, state, (id, _) => pages.Add(id));
            check(pages.Contains("again_audience") == physical && pages.Contains("again_letter") == !physical,
                "Konomi polish: rendered courtyard misstates the encounter.");
            check(pages.Contains("work") && pages.Contains("company") && outcomes.Any(s => s.Has(access)),
                "Konomi polish: truthful first meeting blocks existing private access.");
        }
        var ordinary = new Snapshot(); ordinary.Flags.Add("konomi.missed_personal_invitation");
        check(Rules.ChoiceAvailable(start.Choices[0], ordinary) && !Rules.ChoiceAvailable(start.Choices[3], ordinary)
              && !Rules.ChoiceAvailable(start.Choices[4], ordinary), "Konomi polish: accreditation leaked into ordinary invitation.");
        ordinary.Flags.Clear(); ordinary.Flags.Add("konomi.missed_known_invitation");
        check(Rules.ChoiceAvailable(start.Choices[1], ordinary), "Konomi polish: ordinary correspondence lost its answer.");

        // Both histories true retain the grievance; voluntary access alone cannot invent it.
        foreach (var beat in new[] { ("before_road", "histories", 1, "new"),
                                    ("chosen_evening", "heard", 0, "pleasure"),
                                    ("private_last_visit", "start", 0, "business") })
        {
            var scene = S(beat.Item1);
            var incoming = scene.Nodes.Single(n => n.Id == beat.Item2);
            var original = scene.Nodes.Single(n => n.Id == beat.Item4);
            var variant = scene.Nodes.Single(n => n.Id == "missed_" + beat.Item4);
            check(incoming.Choices[beat.Item3].Next == original.Id, "Konomi polish: saved answer index changed.");
            check(original.Choices.Select(c => (c.Next, string.Join("|", c.Set)))
                .SequenceEqual(variant.Choices.Select(c => (c.Next, string.Join("|", c.Set)))),
                "Konomi polish: prose variant changed continuation or outcomes.");
            foreach (bool hasAccess in new[] { false, true })
            foreach (bool hasDismissal in new[] { false, true })
            {
                var state = new Snapshot();
                if (hasAccess) state.Flags.Add(access);
                if (hasDismissal) state.Flags.Add(dismissed);
                var available = incoming.Choices.Where(c => c.Next == original.Id || c.Next == variant.Id)
                    .Where(c => Rules.ChoiceAvailable(c, state)).ToList();
                check(available.Count == 1 && available[0].Next == (hasAccess && !hasDismissal ? variant.Id : original.Id),
                    "Konomi polish: false dismissal or missing mixed-history answer at " + scene.Id);
                if (beat.Item1 == "before_road")
                {
                    state.Flags.Add("konomi.lovers");
                    check(!incoming.Choices.Where(c => c.Next == original.Id || c.Next == variant.Id)
                        .Any(c => Rules.ChoiceAvailable(c, state)), "Konomi polish: non-lover copy bypasses lovers exclusion.");
                }
            }
        }
        var road = S("before_road").Nodes.Single(n => n.Id == "histories");
        check(road.Choices[2].Next == "missed_lovers" && road.Choices[3].Next == "lovers",
            "Konomi polish: established lovers' appended answer indices changed.");

        int legendAnswers = 0;
        foreach (string id in new[] { "private_reunion", "private_absence_catchup" })
        {
            var scene = S(id);
            foreach (var node in scene.Nodes.Where(n => n.Choices.Any(c => c.Next == "absence_legend")))
            {
                legendAnswers++;
                var answer = node.Choices[0];
                check(answer.Next == "absence_legend" && answer.Requires.SequenceEqual(new[] { "legend" })
                    && answer.Text == "\"I chose to become Legend. I still want you in the life I chose.\"",
                    "Konomi polish: a copied Legend answer recalls unearned postal power.");
            }
            var reply = scene.Nodes.Single(n => n.Id == "absence_legend");
            check(!reply.Text.Contains("clerk") && !reply.Text.Contains("impossible door")
                && reply.Text.Contains("Do you still want those evenings, Commander?")
                && reply.Choices[0].Next == "absence_close", "Konomi polish: Legend reply invents delivery or loses its question.");
        }
        check(legendAnswers == 7, "Konomi polish: Legend sibling set changed.");
    }
}
