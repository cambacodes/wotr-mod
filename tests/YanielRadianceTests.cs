using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// E10 party-only read (storylines/yaniel_radiance.py): where Yaniel looks at the Commander's hip, or the Commander draws
// Radiance or hands it to her, the gate reads yaniel.radiance_in_party (PartyItems: the party inventory, never the shared
// stash). yaniel.radiance_held (party or stash) is left only on the hall-peg epilogue paragraph.
internal static class YanielRadianceTests
{
    private const string Held = "yaniel.radiance_held", InHand = "yaniel.radiance_in_party";
    private static readonly string[] Forms = { "masterwork", "plus1", "plus2", "ha4", "ha6" };

    internal static void Run(Story story, Action<bool, string> check)
    {
        check(Forms.All(f => story.PartyItems.TryGetValue("yaniel.radiance_party." + f, out var guid)
                && story.InventoryItems.TryGetValue("yaniel.radiance_" + f, out var same) && guid == same),
            "Trk_Yaniel_Radiance: the party-only forms do not mirror the inventory forms.");
        check(story.Derived.TryGetValue(InHand, out var groups) && groups.Length == 5 && groups.All(g => g.Length == 1 && story.PartyItems.ContainsKey(g[0])),
            "Trk_Yaniel_Radiance: radiance_in_party is not the OR of the five party-only forms.");
        check(story.Derived[Held].Length == 5, "Trk_Yaniel_Radiance: the broad radiance_held read changed meaning (old saves).");
        var yaniel = story.Scenes.Where(s => s.Relationship == "yaniel" || s.Id.StartsWith("yaniel.", StringComparison.Ordinal)).ToList();
        // The broad read survives only on the hall-peg paragraph (the sword hung at home after the war: the stash will do).
        foreach (var scene in yaniel)
        {
            check(!scene.Requires.Contains(Held) && !scene.Forbids.Contains(Held), "Trk_Yaniel_Radiance: a scene still gates on the stash: " + scene.Id);
            foreach (var node in scene.Nodes)
            {
                foreach (var choice in node.Choices)
                    check(!choice.Requires.Contains(Held) && !choice.Forbids.Contains(Held),
                        "Trk_Yaniel_Radiance: a choice still reads the stash: " + scene.Id + "/" + node.Id);
                foreach (var paragraph in node.Paragraphs.Where(p => p.Requires.Contains(Held) || p.Forbids.Contains(Held)))
                    check(paragraph.Text.Contains("hung in the Commander's hall"), "Trk_Yaniel_Radiance: a paragraph still reads the stash: " + scene.Id);
            }
        }
        // Stash-only, party, none: each moved choice pair shows exactly one branch, and the stash-only world takes the empty one.
        var pairs = new (string Scene, string Node, int Held, int Empty)[]
        {
            ("yaniel.trickster.late.wall", "wall", 0, 1), ("yaniel.trickster.ch5.found", "start", 1, 2), ("yaniel.trickster.ch5.found_late", "msg", 2, 3),
            ("yaniel.trickster.commit.trade", "room", 1, 2), ("yaniel.trickster.beat.staunton", "brand", 1, 2), ("yaniel.trickster.beat.raid", "start", 2, 3),
        };
        foreach (var (sceneId, nodeId, held, empty) in pairs)
        {
            var choices = story.Scenes.Single(s => s.Id == sceneId).Nodes.Single(n => n.Id == nodeId).Choices;
            check(choices[held].Requires.Contains(InHand) && choices[empty].Forbids.Contains(InHand),
                "Trk_Yaniel_Radiance: the drawn-sword pair does not read the party-only key: " + sceneId);
        }
        var hands = story.Scenes.Single(s => s.Id == "yaniel.trickster.verdict.hands").Nodes.Single(n => n.Id == "start").Choices;
        check(hands[0].Requires.Contains(InHand) && hands[1].Forbids.Contains(InHand) && hands[2].Requires.Contains(InHand)
              && hands[3].Forbids.Contains(InHand) && hands[4].Forbids.Contains(InHand), "Trk_Yaniel_Radiance: the verdict's hip branches do not read the party.");
        check(story.Scenes.Single(s => s.Id == "yaniel.trickster.beat.drill").Requires.Contains(InHand), "Trk_Yaniel_Radiance: the drill does not need the sword on you.");
        foreach (bool party in new[] { false, true })
        {
            var state = new Snapshot { Chapter = 5 };
            state.Flags.Add("yaniel.radiance_plus2");                   // in the stash (or the party: the broad read holds either way)
            if (party) state.Flags.Add("yaniel.radiance_party.plus2");
            Rules.Complete(story, state);
            check(state.Has(Held) && state.Has(InHand) == party, "Trk_Yaniel_Radiance: the Derived reads are wrong, party=" + party);
        }
    }
}
