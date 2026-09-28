using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Arsinoe, Trickster (Writer/handoffs/trickster/arsinoe.md): the leased cauldron. Lease -> collection -> epilogue pages,
// plus the E14c collector paragraph on the registered kept endings and the two allocated reactions.
internal static class ArsinoeTricksterTests
{
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Contact = "a609ed9b2205d034bb3bb04d2a255681";
    private const string Lease = "arsinoe.trickster.cauldron.lease";
    private const string Collection = "arsinoe.trickster.cauldron.collection";

    private static Snapshot World(Story story, params string[] flags)
    {
        var state = new Snapshot { Chapter = 5, Area = Drezen, Hour = 5000 };
        state.Flags.UnionWith(flags);
        state.AvailableContacts.Add(Contact);
        Rules.Complete(story, state);
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        var lease = story.Scenes.Single(s => s.Id == Lease);
        var collection = story.Scenes.Single(s => s.Id == Collection);
        var epilogues = story.Scenes.Where(s => s.Id.StartsWith("arsinoe.trickster.epilogue.", StringComparison.Ordinal)).ToArray();
        check(epilogues.Length == 4 && epilogues.All(e => e.Owner == "Epilogue"), "Arsinoe Trickster epilogue pages missing.");
        check(new[] { lease, collection }.All(s => s.AnswerLists.SequenceEqual(new[] { "ecaf5cfe8087a4f45a2269974f4885c9" }) && s.ContactUnit == Contact),
            "Arsinoe Trickster beats leave her own vendor list.");

        // Trk_Arsinoe_InCapital / PathFailed: no cauldron, or the path lost, no lease.
        check(!Rules.Available(story, lease, World(story, "trickster", "arsinoe.capital")), "Lease offered without the Council's cauldron.");
        check(!Rules.Available(story, lease, World(story, "trickster.was", "trickster.failed", "arsinoe.capital", "council.cauldron_given")),
            "Lease offered after the Trickster path failed.");
        var ready = World(story, "trickster", "arsinoe.capital", "council.cauldron_given");
        check(Rules.Available(story, lease, ready), "Trk_Arsinoe_Cauldron: lease unavailable.");
        check(!Rules.Available(story, collection, ready), "Collection before the lease.");
        var notCapital = Program.Copy(ready); notCapital.Chapter = 4;
        check(!Rules.Available(story, lease, notCapital), "Physical lease outside chapter five.");

        // Native effects live on the joke only; the failed haggle adds its surcharge.
        var joke = lease.Nodes.Single(n => n.Id == "terms").Choices[0];
        check(joke.Mythic == "PlayerIsTrickster" && joke.Alignment?.Direction == "Lawful" && joke.Alignment.Value == 1
              && joke.Crusade?.Resource == "Finances" && joke.Crusade.Amount == -500, "Lease joke lost its native price.");
        var raised = lease.Nodes.Single(n => n.Id == "raised").Choices.Single();
        check(raised.Crusade?.Amount == -200 && raised.Set.Contains("arsinoe.trickster.cost.rent_raised"), "Failed haggle is free.");
        var haggle = lease.Nodes.Single(n => n.Id == "rent").Choices.Single(c => c.Check != null).Check!;
        check(haggle.Skill == "CheckDiplomacy" && haggle.DC == 25 && haggle.CommanderOnly, "Haggle uses the wrong check.");

        foreach (bool shamira in new[] { false, true })
        foreach (bool fought in new[] { false, true })
        {
            var start = Program.Copy(ready);
            if (shamira) start.Flags.Add("shamira.killed");
            if (fought) start.Flags.Add("council.fought");
            var pages = new HashSet<string>();
            var results = Program.Walk(lease, start, (page, partial) =>
            {
                pages.Add(page);
                check(partial.Flags.SetEquals(start.Flags) || page == "leased" || page == "discount" || page == "grudge",
                    "Lease writes history before it is signed: " + page);
            });
            check(pages.Contains("shamira") == shamira, "Shamira's essence node ignores ShamiraKilled.");
            check(pages.Contains("grudge") == fought, "Grudge node ignores the Council fight.");
            var signed = results.Where(r => r.Has(Lease)).ToList();
            check(signed.Count > 0 && signed.All(r => r.Has("arsinoe.trickster.primed") && r.Has("arsinoe.trickster.cost.lien")),
                "Signed lease does not prime the collection.");
            check(results.Where(r => !r.Has(Lease)).All(r => r.Flags.SetEquals(start.Flags)), "Refusing the lease changes history.");
            check(results.Any(r => !r.Has(Lease)), "The lease cannot be refused or postponed.");
            foreach (var after in signed)
            {
                check(!Rules.Available(story, lease, after), "Lease replays.");
                var later = Program.Copy(after); later.Hour += collection.DelayHours;
                Rules.Complete(story, later);
                check(Rules.Available(story, collection, later), "Trk_Arsinoe_Cauldron: collection unreachable.");
                var early = Program.Copy(after); early.Hour += collection.DelayHours - 1;
                check(!Rules.Available(story, collection, early), "Collection ignores its delay.");
                // Ledger row 14: the lease does not close on the Council's fate; the collection survives losing the path.
                var lost = Program.Copy(later); lost.Flags.Remove("trickster"); lost.Flags.Add("trickster.was"); lost.Flags.Add("socot.gone");
                Rules.Complete(story, lost);
                check(Rules.Available(story, collection, lost), "Collection lost with the live Trickster path.");
            }
        }

        foreach (bool lover in new[] { false, true })
        foreach (bool king in new[] { false, true })
        {
            var start = World(story, "trickster", "arsinoe.capital", "arsinoe.trickster.primed", "arsinoe.trickster.cost.lien", Lease);
            if (lover) start.Flags.UnionWith(new[] { "arsinoe.started", "arsinoe.campaign_lover", "arsinoe.committed" });
            if (king) { start.Flags.Add("fool_king.crowned"); Rules.Complete(story, start); }
            var pages = new HashSet<string>();
            var results = Program.Walk(collection, start, (page, _) => pages.Add(page));
            check(pages.Contains("threshold") == lover && pages.Contains("morning") == lover, "Intimate beat ignores the registered lover state.");
            check(pages.Contains("still") == king, "Fool King's still pledged without the King.");
            check(!pages.Contains("wedding") && !pages.Contains("rider"), "Other routes' costs read without their flags.");
            check(results.All(r => r.Has(Collection)), "Collection has a non-terminal exit.");
            check(results.Any(r => r.Has("arsinoe.trickster.stays_to_collect") && r.Has("arsinoe.started")), "Trk_Arsinoe_Flirt unreachable.");
            check(results.Any(r => r.Has("arsinoe.trickster.collection_closed") && !r.Has("arsinoe.trickster.stays_to_collect")),
                "Collection cannot be kept to business.");
            check(results.All(r => !r.Has("arsinoe.closed") && (!lover || r.Has("arsinoe.committed"))), "Collection closes or erases the romance.");
            check(results.Any(r => r.Has("arsinoe.trickster.cost.collateral_worldwound")), "Worldwound pledge unreachable.");
            foreach (var r in results) check(!Rules.Available(story, collection, r), "Collection replays.");
        }

        // Epilogue pages: exactly one cauldron page per finale, and the lien page splits on the Wound's closure.
        foreach (bool burst in new[] { false, true })
        foreach (bool wound in new[] { false, true })
        foreach (bool closed in new[] { false, true })
        {
            var end = World(story, "trickster.was", "arsinoe.trickster.cost.lien", "arsinoe.trickster.primed");
            end.Chapter = 6;
            if (burst) end.Flags.Add("siphon.burst_council");
            if (wound) end.Flags.Add("arsinoe.trickster.cost.collateral_worldwound");
            if (closed) end.Flags.Add("ending.wound_closed");
            Rules.Complete(story, end);
            var shown = epilogues.Where(e => Rules.Available(story, e, end)).Select(e => e.Id).ToList();
            check(shown.Count(id => id.EndsWith("bill_to_threshold") || id.EndsWith("pot_returned")) == 1, "Cauldron fate page missing or doubled.");
            check(shown.Contains("arsinoe.trickster.epilogue.bill_to_threshold") == burst, "Siphon burst ignored.");
            check(shown.Count(id => id.Contains("foreclosure")) == (wound ? 1 : 0), "Worldwound lien page wrong.");
        }

        // The collector paragraph rides on the registered kept endings (E14c), never as a second page.
        foreach (string id in new[] { "arsinoe_ending_kept", "arsinoe_ending_open", "arsinoe_ending_promised" })
        {
            var para = story.Scenes.Single(s => s.Id == id).Nodes[0].Paragraphs;
            check(para != null && para.Any(p => p.Requires.SequenceEqual(new[] { "arsinoe.trickster.stays_to_collect" })),
                "Collector paragraph missing on " + id);
        }

        // Reactions: exactly the two allocated reactors, both reading the lien.
        var reactions = story.Scenes.Where(s => s.Relationship == "arsinoe" && s.Reaction).ToArray();
        check(reactions.Length == 2 && reactions.All(r => r.Requires.Contains("arsinoe.trickster.cost.lien")), "Arsinoe reactions changed.");
    }
}
