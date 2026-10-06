using System;
using System.Linq;
using Tirabade;

internal static class ReturnProvenanceInventoryTests
{
    private const string P = "camellia.trickster.";
    internal static void Cases(Story story, Action<bool,string> check)
    {
        Scene S(string id) => L07World.Scene(story, id);
        var battle = S(P + "dead.overacting");
        var initial = L07World.Seed(story, battle, "trickster", "camellia.dead", "revive.camellia.available");
        check(Rules.Available(story, battle, initial), "l07 battlefield producer unavailable");
        var returned = L07World.Play(story, battle, initial).First(w => w.Has(P + "returned"));
        check(!returned.Has("camellia.dead") && !returned.Has(P + "cost.knows_you_tried"), "l07 battlefield resurrection has coffin provenance");
        var terms = S(P + "returned.terms_camp");
        returned.AvailableContacts.Add(terms.ContactUnit!);
        returned.Flags.Add(P + "beat.lesson"); returned.Times[P + "beat.lesson"] = 1;
        var ready = L07World.Move(story, terms, returned);
        check(Rules.Available(story, terms, ready), "l07 battlefield terms unavailable");
        var agreed = L07World.Play(story, terms, ready).First(w => w.Has(P + "terms_named"));
        var test = S(P + "returned.test_camp");
        var testWorld = L07World.Move(story, test, agreed);
        check(Rules.Available(story, test, testWorld), "l07 battlefield commitment producer unavailable");
        var committed = L07World.Play(story, test, testWorld).First(w => w.Has("camellia.committed"));

        // Verified Q3_KillCamellia starts these two etudes; DEAD is the live
        // companion death observation. No completed coffin producer occurs here.
        foreach (var history in new[] { agreed, committed })
        {
            var killed = Program.Copy(history);
            killed.Flags.UnionWith(new[] { "camellia.killed", "camellia.kicked_out", "camellia.dead" });
            L07World.Refresh(story, killed);
            check(!Rules.RouteOpen(story.Relationships["camellia"], killed), "l07 stale battlefield return lifts FinalTruth execution");
            foreach (var id in new[] { "epilogue.kept", "epilogue.kept_on_record", "epilogue.commit", "epilogue.commit_on_record", "react.regill_grave", "react.regill_quarters" })
            {
                var scene = S(P + id); var state = L07World.Move(story, scene, killed);
                state.Flags.Add("regill.in_party");
                if (id.EndsWith("on_record")) state.Flags.Add("sacrifice");
                check(!Rules.Available(story, scene, L07World.Refresh(story, state)), "l07 executed Camellia consumer " + id);
            }
            var late = S("camellia.lastcall.page"); var lc = L07World.Move(story, late, killed);
            lc.Flags.UnionWith(new[] { "trickster.lastcall.taken", "ending.trickster", "trickster.lastcall.open", "seelah.committed", "chapter_later" });
            L07World.Refresh(story, lc);
            check(!Rules.Available(story, late, lc) && !lc.Has("camellia.lastcall.callable"), "l07 executed Camellia Last Call");
            foreach (var id in new[] { "guest.camellia", "seating.seelah.camellia" })
                check(!Rules.BookEntryVisible(story.Books["trickster.ledger"].Entries.Single(e => e.Id == id), lc), "l07 executed Camellia book " + id);
            var presence = story.Presences["camellia.presence"]; killed.Area = presence.Area; killed.Chapter = 5;
            check(!Rules.PresenceWanted(presence, killed), "l07 executed Camellia copy");
            var proofs = S("nurah.trickster.after.proofs");
            // The parcel follows Nurah's earned return from her own death;
            // importing a death after a previously observed return would instead
            // be the new-departure case this engine now correctly suppresses.
            var packet = L07World.Seed(story, proofs, killed.Flags.Concat(new[] {
                "nurah.ran_off", "nurah.trickster.cost.late", "nurah.trickster.returned",
                "nurah.trickster.larva_rumour", "nurah.dead_camellia" }).ToArray());
            Rules.RecordAvailabilityEvents(story, packet, new[] { "nurah.trickster.returned" });
            L07World.Refresh(story, packet);
            check(Rules.Available(story, proofs, packet), "l07 ordinary proofs continuation unavailable");
            var visited = new System.Collections.Generic.HashSet<string>();
            L07World.Play(story, proofs, packet, (id, _) => visited.Add(id)).ToArray();
            check(!visited.Any(id => id.StartsWith("card")), "l07 stale Camellia dispatch stages living widow");
            foreach (var id in new[] { "pardon", "market", "supper", "draft" })
            {
                var card = S("nurah.trickster.react.camellia_veiled_" + id);
                var world = L07World.Seed(story, card, killed.Flags.ToArray());
                check(!Rules.Available(story, card, world), "l07 stale veiled card " + id);
            }
        }
        // Genuine paid coffin path, with no direct injection of the completion.
        var third = S(P + "killed.third_night");
        var coffin = L07World.Seed(story, third, "trickster", "camellia.kicked_out", "camellia.dead");
        check(Rules.Available(story, third, coffin), "l07 genuine coffin ritual unavailable");
        var raised = L07World.Play(story, third, coffin).First(w => w.Has(P + "raised"));
        check(!raised.Has(P + "cost.knows_you_tried"), "l07 coffin agreement completed before producer");
        var presenceBefore = story.Presences["camellia.presence"];
        check(Rules.PresenceWanted(presenceBefore, raised), "l07 paid coffin cannot reach return agreement");
        var letter = S(P + "killed.performance_letter");
        raised.Flags.Add("camellia.presence.failed"); // negative placement selects existing letter, not proof of placement
        var letterWorld = L07World.Move(story, letter, raised);
        check(Rules.Available(story, letter, letterWorld), "l07 genuine coffin agreement letter unavailable");
        var complete = L07World.Play(story, letter, letterWorld).First(w => w.Has(P + "cost.knows_you_tried"));
        check(Rules.RouteOpen(story.Relationships["camellia"], complete) && complete.Has(P + "veiled_available"), "l07 genuine coffin return rejected");
        var grave = S(P + "react.regill_grave"); var graveWorld = L07World.Move(story, grave, complete);
        graveWorld.Flags.Add("regill.in_party"); graveWorld.AvailableContacts.Add(grave.ContactUnit!);
        check(Rules.Available(story, grave, L07World.Refresh(story, graveWorld)), "l07 completed coffin loses Regill reaction");

        // Refusal after a battlefield return, then another live native death.
        var refusal = L07World.Play(story, test, testWorld).First(w => w.Has("camellia.closed"));
        refusal.Flags.Add("camellia.dead");
        var refused = S(P + "epilogue.refused"); refusal = L07World.Move(story, refused, refusal);
        refusal.Flags.Add(P + "cost.asked_her_tame"); L07World.Refresh(story, refusal);
        check(Rules.Available(story, refused, refusal), "l07 Commander-only refused consequence erased");
        check(!Rules.ParagraphVisible(refused.Nodes.Single().Paragraphs[2], refusal), "l07 refusal followed by unreturned death stages living murder");
        Console.WriteLine("l07 E-Q7-11: battlefield -> terms/commit -> Q3 execution; paid coffin -> letter agreement; refusal -> second death; all consumers executed");
    }
    internal static void Run(Story story, Action<bool,string> check)
    {
        Cases(story, check);
        L07World.RejectMutation(story, s => {
            // Isolate the original provenance guard from the new epoch
            // backstop. The eng3 inventory tests that backstop independently.
            s.Relationships["camellia"].EpochUnavailableFlags = Array.Empty<string>();
            s.Relationships["camellia"].UnavailableOverrides["camellia.killed"] = P + "returned";
            s.Relationships["camellia"].UnavailableOverrides["camellia.dead"] = P + "returned";
        }, Cases, check, "generic killed/dead return");
        L07World.RejectMutation(story, s => {
            foreach (var c in L07World.Scene(s, P + "killed.performance_letter").Nodes.SelectMany(n => n.Choices))
                c.Set = c.Set.Where(f => f != P + "cost.knows_you_tried").ToArray();
        }, Cases, check, "remove coffin completion producer");
    }
}
