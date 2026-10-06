using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

internal static class IrabethPartnerStanceTests
{
    internal static HashSet<string> Run(Story story, Action<bool, string> check)
    {
        const string share = "irabeth.partner_stance.share";
        const string secret = "irabeth.partner_stance.secret";
        const string exclusive = "irabeth.partner_stance.exclusive";
        const string discovered = "irabeth.partner_stance.discovered";
        var reached = new HashSet<string>();
        Scene Get(string id) => story.Scenes.Single(s => s.Id == id);
        Snapshot World(Scene book, params string[] flags)
        {
            var state = new Snapshot { Chapter = 5, Hour = 100000,
                Area = "2570015799edf594daf2f076f2f975d8" };
            state.Flags.UnionWith(book.Requires.Concat(flags));
            state.AvailableContacts.UnionWith(new[] { "280d4712dceb37f4a88e98f1f4c6e64f", "b5e867e13503c6f41bb1316705efb4a2" });
            Rules.Complete(story, state);
            state.Hour += book.DelayHours;
            return state;
        }
        List<Snapshot> Walk(Scene book, Snapshot state) => Program.Walk(book, state,
            (page, _) => reached.Add(book.Id + "/" + page));

        var road = Get("irabeth.a_road_she_would_choose");
        var outcomes = Walk(road, World(road, "trickster", "irabeth.lover"));
        check(outcomes.Any(s => s.Has(share) && s.Has("irabeth.committed")), "Irabeth cannot commit to sharing.");
        check(outcomes.Any(s => s.Has(secret) && s.Has("irabeth.committed")), "Irabeth has no earned affair branch.");
        var demands = outcomes.Where(s => s.Has(exclusive)).ToArray();
        check(demands.Length > 0 && demands.All(s => s.Has("irabeth.closed") && !s.Has("irabeth.committed")),
            "Irabeth's exclusivity refusal silently ended her marriage or committed her.");
        foreach (var state in outcomes)
        {
            check(new[] { share, secret, exclusive }.Count(state.Has) <= 1, "Irabeth records conflicting stances.");
            check(!state.Has("anevia.closed") && !state.Has("anevia.committed"), "Irabeth demand writes Anevia's romance.");
        }
        var widow = Walk(road, World(road, "trickster", "irabeth.lover", "anevia_dead"));
        check(widow.Any(s => s.Has("irabeth.committed")) && widow.All(s => !s.Has(share) && !s.Has(secret) && !s.Has(exclusive)),
            "Irabeth's bereavement invents an agreement from Anevia.");

        foreach (string audience in new[] { "irabeth.the_hour_before_battle", "irabeth.trickster.back_on_duty" })
        foreach (bool remembersBlow in new[] { false, true })
        foreach (var wife in new[] { Array.Empty<string>(), new[] { "anevia_dead" }, new[] { "anevia_gone" },
                     new[] { "anevia_gone", "anevia.trickster.returned", "trickster" } })
        {
            var battle = Get(audience);
            var state = World(battle, new[] { secret, "irabeth.committed", "irabeth.future_lasting", "trickster" }
                .Concat(wife).Concat(remembersBlow ? new[] { "irabeth.trickster.cost.remembers_the_blow" } : Array.Empty<string>()).ToArray());
            check(Rules.Available(story, battle, state), "Wife state blocks the existing pre-battle audience.");
            var fallout = Walk(battle, state);
            check(fallout.Count > 0 && fallout.All(s => s.Has("irabeth.closed")), "Secret affair gets a free pre-battle pardon.");
            if (!state.Has("anevia_dead") && (!state.Has("anevia_gone") || state.Has("anevia.trickster.returned")))
                check(fallout.All(s => s.Has(discovered)), "Living Anevia does not expose the affair.");
        }

        // The refusal page belongs to this route even after its ClosedFlag.
        var ending = Get("irabeth.partner_ending");
        var refusal = World(ending, exclusive, "trickster");
        check(Rules.Available(story, ending, refusal), "Exclusivity refusal has no ending.");
        Walk(ending, refusal);
        foreach (var book in story.Scenes.Where(s => s.Relationship == "irabeth" && s.Owner.EndsWith("Epilogue") && s.Owner != "AeonEpilogue" && !Rules.IsNativeReplacement(story, s)))
        foreach (var page in book.Nodes)
        {
            check(page.Paragraphs.Any(p => p.Requires.Contains(share)) && page.Paragraphs.Any(p => p.Requires.Contains(secret)),
                "Irabeth epilogue forgets stance: " + book.Id + "/" + page.Id);
            check(page.Paragraphs.Any(p => p.Requires.Contains("anevia_dead")) && page.Paragraphs.Any(p => p.Requires.Contains("anevia_gone"))
                  && page.Paragraphs.Any(p => p.Requires.Contains("anevia.trickster.returned")),
                "Irabeth epilogue omits a wife state: " + book.Id + "/" + page.Id);
        }
        var lastCall = Get("irabeth.lastcall.page").Nodes.Single();
        check(lastCall.Paragraphs.Any(p => p.Requires.Contains(share)) && lastCall.Paragraphs.Any(p => p.Requires.Contains("anevia_gone"))
              && lastCall.Paragraphs.Any(p => p.Requires.Contains("anevia_dead")), "Irabeth's Last Call forgets wife or stance.");
        foreach (string cue in new[] { "cba964e33d0a0704d847629be452b359", "2d6b09c6508010e49b882741add89dcf" })
        {
            var variants = Rules.EditVariants(story.NativeEpilogueEdits[cue]);
            foreach (string selectedStance in new[] { share, secret, exclusive, "" })
            foreach (var wife in new[] { Array.Empty<string>(), new[] { "anevia_dead" }, new[] { "anevia_gone" }, new[] { "anevia_gone", "anevia.trickster.returned" } })
            foreach (bool sacrifice in new[] { false, true })
            {
                var state = new Snapshot { Chapter = 6, Hour = 100000 };
                state.Flags.UnionWith(variants[0].When[0].Where(f => !f.StartsWith("!")));
                state.Flags.UnionWith(new[] { "trickster", selectedStance }.Concat(wife).Where(f => f.Length > 0));
                if (sacrifice) state.Flags.Add("sacrifice");
                Rules.Complete(story, state);
                int selected = Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), state);
                string partner = state.Has("anevia_dead") ? "dead" : state.Has("anevia.trickster.returned") ? "returned" : state.Has("anevia_gone") ? "away" : "together";
                string stanceName = selectedStance.Length == 0 ? "unset" : selectedStance.Substring(selectedStance.LastIndexOf('.') + 1);
                string expected = selectedStance.Length == 0 && partner == "together" ? variants[0].Replacement :
                    variants[0].Replacement + ".partner." + partner + "." + stanceName + (sacrifice ? ".mourning" : "");
                check(selected >= 0 && variants[selected].Replacement == expected,
                    "Native Irabeth ending loses wife state or stance.");
                var offPath = Program.Copy(state); offPath.Flags.Remove("trickster.now"); offPath.Flags.Add("legend");
                check(Rules.SelectNativeEditVariant(story, variants, Rules.EditScenes(story, variants), offPath) < 0,
                    "Partner native rewrite plays off Trickster.");
            }
        }
        // The original absent-wife slides must not mask the appended readers
        // when a legacy save has no stance and Anevia is present or dead.
        foreach (var edit in story.NativeEpilogueEdits.Values)
        {
            var all = Rules.EditVariants(edit);
            foreach (var original in all.Where(v => v.Replacement.StartsWith("irabeth.trickster.epilogue.native_") && !v.Replacement.Contains(".partner.")))
            {
                var family = all.Where(v => v.Replacement == original.Replacement || v.Replacement.StartsWith(original.Replacement + ".partner.")).ToArray();
                var source = Get(original.Replacement);
                foreach (var wife in new[] { Array.Empty<string>(), new[] { "anevia_gone" }, new[] { "anevia_dead" } })
                {
                    var state = new Snapshot { Chapter = 6, Hour = 100000 };
                    state.Flags.UnionWith(original.When[0].Where(f => !f.StartsWith("!") && f != "anevia_gone"));
                    state.Flags.UnionWith(source.Requires.Where(f => f != "anevia_gone").Concat(wife));
                    state.Flags.Add("trickster");
                    Rules.Complete(story, state);
                    int selected = Rules.SelectNativeEditVariant(story, family, Rules.EditScenes(story, family), state);
                    string expected = wife.Contains("anevia_gone") ? original.Replacement : original.Replacement +
                        ".partner." + (wife.Contains("anevia_dead") ? "dead" : "together") + ".unset";
                    check(selected >= 0 && family[selected].Replacement == expected,
                        "Legacy native Irabeth ending substitutes departure for Anevia's actual state.");
                }
            }
        }
        // Current-path requirements come from the original native replacement;
        // consuming an already-paid return must not acquire a new path gate.
        foreach (var edit in story.NativeEpilogueEdits.Values)
        {
            var variants = Rules.EditVariants(edit);
            foreach (var variant in variants.Where(v => v.Replacement.StartsWith("irabeth.") && v.Replacement.Contains(".partner.")))
            {
                string originalId = variant.Replacement.Substring(0, variant.Replacement.IndexOf(".partner.", StringComparison.Ordinal));
                var original = variants.Single(v => v.Replacement == originalId);
                check(variant.When.All(g => g.Contains("trickster.now")) == original.When.All(g => g.Contains("trickster.now")),
                    "Partner state adds a path requirement to an already-earned native ending.");
            }
        }
        return reached;
    }
}
