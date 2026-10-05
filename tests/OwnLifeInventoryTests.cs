using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng7-l07: small real-choice walker for loss transitions; recompute live composites
// exactly as a fresh native snapshot does. Do not retain desired derived facts.
internal static class L07World
{
    internal static Scene Scene(Story story, string id) => story.Scenes.Single(s => s.Id == id);
    internal static Snapshot Refresh(Story story, Snapshot state)
    {
        foreach (var key in story.Derived.Keys.Concat(story.Counts.Keys)) state.Flags.Remove(key);
        Rules.Complete(story, state);
        return state;
    }
    internal static Snapshot Seed(Story story, Scene scene, params string[] extra)
    {
        var state = new Snapshot { Chapter = scene.MinChapter, Hour = 10000, Area = scene.Areas.FirstOrDefault() ?? "",
            CrusadeResources = new Dictionary<string,int> { ["Finances"] = 10000, ["Materials"] = 10000, ["Favors"] = 10000 } };
        void Input(string key)
        {
            // Outcome guards must be computed from observed loss/return history,
            // never supplied to make a nominated consumer appear available.
            if (key.EndsWith(".life.available") || key == "camellia.trickster.veiled_available") return;
            if (story.Derived.TryGetValue(key, out var sources))
            { foreach (var source in sources[0]) Input(source); }
            else state.Flags.Add(key);
        }
        foreach (var key in scene.Requires) Input(key);
        foreach (var g in scene.RequiresAnyGroups) state.Flags.Add(g[0]);
        state.Flags.UnionWith(extra);
        state.Flags.Add("chapter_later");
        // Native contact is a fixture input, not evidence that a return placed a copy.
        if (scene.ContactUnit != null) state.AvailableContacts.Add(scene.ContactUnit);
        state.AvailableContacts.UnionWith(scene.AdditionalContactUnits);
        foreach (var f in state.Flags) state.Times[f] = 1;
        return Refresh(story, state);
    }
    internal static IEnumerable<Snapshot> Play(Story story, Scene scene, Snapshot initial, Action<string, Snapshot>? render = null, bool firstOnly = false)
    {
        var results = new List<Snapshot>();
        void Visit(string id, Snapshot state, HashSet<string> seen)
        {
            if (firstOnly && results.Count > 0) return;
            if (!seen.Add(id)) throw new Exception("l07 cycle " + scene.Id + "/" + id);
            var node = scene.Nodes.Single(n => n.Id == id);
            render?.Invoke(id, state);
            var choices = node.Choices.Where(c => Rules.ChoiceAvailable(c, state)).ToArray();
            if (choices.Length == 0) throw new Exception("Page has no selectable answers: " + scene.Id + "/" + id);
            foreach (var choice in choices)
            {
                if (firstOnly && results.Count > 0) break;
                var next = Program.Copy(state);
                foreach (var flag in choice.Set) { next.Flags.Add(flag); next.Times[flag] = next.Hour; }
                if (choice.Crusade != null && next.CrusadeResources != null)
                    next.CrusadeResources[choice.Crusade.Resource] += choice.Crusade.Amount;
                if (choice.Revive != null) next.Flags.Remove(story.Revivals[choice.Revive].DeathFlag);
                if (choice.Set.Length > 0 || choice.Revive != null) Refresh(story, next);
                if (choice.Next != null || choice.Check != null)
                    foreach (var target in Rules.NextNodes(choice)) Visit(target, Program.Copy(next), new HashSet<string>(seen));
                else
                {
                    if (!choice.Abort) { next.Flags.Add(scene.Id); next.Times[scene.Id] = next.Hour; }
                    results.Add(Refresh(story, next));
                }
            }
        }
        Visit(scene.Nodes[0].Id, Program.Copy(initial), new HashSet<string>());
        return results;
    }
    internal static Snapshot Move(Story story, Scene scene, Snapshot state)
    {
        state = Program.Copy(state);
        state.Chapter = scene.MinChapter; state.Area = scene.Areas.FirstOrDefault() ?? state.Area; state.Hour += 1000;
        return Refresh(story, state);
    }
    internal static Story Clone(Story story)
    {
        var options = new JsonSerializerOptions { IncludeFields = true };
        return JsonSerializer.Deserialize<Story>(JsonSerializer.Serialize(story, options), options)!;
    }
    internal static void RejectMutation(Story story, Action<Story> mutate, Action<Story, Action<bool,string>> run, Action<bool,string> check, string label)
    {
        var changed = Clone(story); mutate(changed);
        bool failed = false;
        try { run(changed, (ok, why) => { if (!ok) throw new Exception(why); }); }
        catch (Exception) { failed = true; }
        check(failed, "l07 mutation passed: " + label);
    }
}

internal static class OwnLifeInventoryTests
{
    internal static void Cases(Story story, Action<bool,string> check)
    {
        Scene S(string id) => L07World.Scene(story, id);
        // Play the real postponement and later refusal; historical hunger remains.
        var lair = S("devarra.trickster.after.lair");
        var before = L07World.Seed(story, lair, "trickster", "devarra.trickster.flown");
        check(Rules.Available(story, lair, before), "l07 lair producer unavailable");
        var hungry = L07World.Play(story, lair, before).First(w => w.Has("devarra.trickster.left_hungry"));
        var retry = S("devarra.tower.back_up_the_mountain");
        var visit = L07World.Move(story, retry, hungry);
        check(Rules.Available(story, retry, visit), "l07 hungry retry unavailable");
        var refused = L07World.Play(story, retry, visit).First(w => w.Has("devarra.closed"));
        var ending = S("devarra.trickster.epilogue.hungry");
        check(!Rules.Available(story, ending, L07World.Move(story, ending, refused)), "l07 hungry continues after refusal");
        var no = S("devarra.trickster.epilogue.refused");
        check(Rules.Available(story, no, L07World.Move(story, no, refused)), "l07 independent refusal ending lost");
        var committed = L07World.Play(story, lair, before).First(w => w.Has("devarra.committed"));
        committed.Flags.UnionWith(new[] { "swarm", "inhuman", "trickster.failed" });
        var woken = S("devarra.trickster.epilogue.woken");
        check(!Rules.Available(story, woken, L07World.Move(story, woken, committed)), "l07 Swarm bodily romance leaks");

        // Both real Anevia breakup pages, after the renewal producer.
        var renewal = S("anevia.trickster.gone.commit");
        foreach (var breakup in new[] { "anevia.a_key_that_is_hers", "anevia.a_grief_with_a_name" })
        {
            var start = L07World.Seed(story, renewal, "trickster", "anevia.lover", "anevia.return_ready", "anevia.case_consequence_kept");
            check(Rules.Available(story, renewal, start), "l07 renewal producer unavailable");
            var renewed = L07World.Play(story, renewal, start).First(w => w.Has("anevia.trickster.terms_kept") || w.Has("anevia.trickster.cost.her_key"));
            if (breakup.Contains("grief")) renewed.Flags.Add("irabeth_dead");
            var scene = S(breakup); var ready = L07World.Move(story, scene, renewed);
            check(Rules.Available(story, scene, ready), "l07 breakup unavailable " + breakup);
            var parted = L07World.Play(story, scene, ready).First(w => w.Has("anevia.parted"));
            var page = S("anevia.ending_parted"); var after = L07World.Move(story, page, parted);
            check(Rules.Available(story, page, after), "l07 parted consequence missing");
            var paragraphs = page.Nodes.Single().Paragraphs;
            foreach (int i in new[] { 9, 11, 12 }) check(!Rules.ParagraphVisible(paragraphs[i], after), "l07 romantic paragraph after breakup " + i);
            check(Rules.ParagraphVisible(paragraphs[15], after), "l07 historical goodbye erased");
        }

        foreach (var loss in story.Relationships["wenduag"].UnavailableFlags.Append("wenduag.closed"))
        {
            foreach (var id in new[] { "pack", "unclaimed", "refused", "native_ascent" })
            {
                var page = S("wenduag.trickster.epilogue." + id);
                var state = L07World.Seed(story, page, "trickster", loss);
                if (id == "refused" && loss == "wenduag.closed") continue; // living refusal is legitimate
                check(!Rules.Available(story, page, state), "l07 Wenduag ending leaks " + id + "/" + loss);
            }
            foreach (var partner in new[] { "wenduag.committed", "wenduag.romance_finished.latched" })
            {
                var state = L07World.Seed(story, S("wenduag.lastcall.page"), "trickster", partner, loss);
                check(!Rules.BookEntryVisible(story.Books["trickster.ledger"].Entries.Single(e => e.Id == "guest.wenduag"), state), "l07 Guest List leaks " + loss);
                check(!Rules.Available(story, S("wenduag.lastcall.page"), state), "l07 coda leaks " + loss);
            }
            var presence = story.Presences["wenduag.presence"];
            var world = new Snapshot { Chapter = 5, Hour = 10000, Area = presence.Area };
            world.Flags.UnionWith(new[] { "trickster", "chapter_later", "wenduag.trickster.returned", loss });
            L07World.Refresh(story, world);
            check(Rules.PresenceWanted(presence, world) == Rules.RouteOpen(story.Relationships["wenduag"], world), "l07 Wenduag physical presence ignores loss/earned return " + loss);
            world.Flags.Remove("wenduag.trickster.returned"); L07World.Refresh(story, world);
            check(!Rules.PresenceWanted(presence, world), "l07 unreturned Wenduag physical presence " + loss);
            check(Rules.PlanPresence(presence, Rules.PresenceWanted(presence, world),
                new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true, CopyFound = true, CopyAlive = true })
                .Contains(PresenceStep.Remove), "l07 lost Wenduag owned copy is not removed " + loss);
        }
        var ward = S("minagho_chivarro.trickster.reunion.wardrobe");
        var dead = L07World.Seed(story, ward, "trickster", "minagho_chivarro.trickster.minagho_in", "minagho.dead");
        var rendered = new HashSet<string>();
        check(Rules.Available(story, ward, dead), "l07 Chivarro wardrobe wrongly loses solo branch");
        L07World.Play(story, ward, dead, (id, _) => rendered.Add(id)).ToArray();
        check(rendered.Contains("alone") && !rendered.Contains("which"), "l07 wardrobe stages unrecovered Minagho");
        dead.Flags.Add("minagho_chivarro.trickster.returned_minagho"); L07World.Refresh(story, dead); rendered.Clear();
        L07World.Play(story, ward, dead, (id, _) => rendered.Add(id)).ToArray();
        check(rendered.Contains("which") && !rendered.Contains("alone"), "l07 wardrobe rejects earned Minagho return");
        foreach (var id in new[] { "pair", "minagho" })
        {
            var page = S("minagho_chivarro.trickster.epilogue." + id);
            var state = L07World.Seed(story, page, "trickster", "minagho.dead");
            check(!Rules.Available(story, page, state), "l07 dead Minagho ending " + id);
            state.Flags.Add("minagho_chivarro.trickster.returned_minagho"); L07World.Refresh(story, state);
            check(Rules.Available(story, page, state), "l07 returned Minagho ending missing " + id);
        }
        foreach (var id in new[] { "chivarro", "owned" })
        {
            var page = S("minagho_chivarro.trickster.epilogue." + id);
            var state = L07World.Seed(story, page, "trickster", "minagho.dead", "minagho_chivarro.trickster.minagho_in");
            check(Rules.Available(story, page, state), "l07 surviving Chivarro consequence lost");
            var p = page.Nodes.Single().Paragraphs[id == "chivarro" ? 2 : 0];
            check(!Rules.ParagraphVisible(p, state), "l07 visitor paragraph stages corpse");
            if (id == "chivarro") check(Rules.ParagraphVisible(page.Nodes.Single().Paragraphs[0], state), "l07 existing loss variant missing");
        }
        // Same stale-life class in the sibling late invitation and owned ending.
        var invitation = S("minagho_chivarro.trickster.epilogue.commit");
        var invited = L07World.Seed(story, invitation, "trickster", "minagho.dead",
            "minagho_chivarro.trickster.tprev.house", "minagho_chivarro.trickster.reunited");
        check(Rules.Available(story, invitation, invited), "l07 surviving Chivarro loses late invitation");
        rendered.Clear();
        L07World.Play(story, invitation, invited, (id, _) => rendered.Add(id)).ToArray();
        check(rendered.Contains("waiting") && !rendered.Contains("pair"), "l07 late invitation stages lost Minagho");
        invited.Flags.Add("minagho_chivarro.trickster.returned_minagho"); L07World.Refresh(story, invited); rendered.Clear();
        L07World.Play(story, invitation, invited, (id, _) => rendered.Add(id)).ToArray();
        check(rendered.Contains("pair") && !rendered.Contains("waiting"), "l07 late invitation rejects earned Minagho return");
        foreach (var id in new[] { "pair", "chivarro", "owned", "commit" })
        {
            var page = S("minagho_chivarro.trickster.epilogue." + id);
            var lost = L07World.Seed(story, page, "trickster", "chivarro.dead");
            check(!Rules.Available(story, page, lost), "l07 lost Chivarro sibling ending " + id);
            lost.Flags.Add("minagho_chivarro.trickster.returned_chivarro"); L07World.Refresh(story, lost);
            check(Rules.Available(story, page, lost), "l07 earned Chivarro sibling ending missing " + id);
        }
        Console.WriteLine("l07 E-Q7-06: executed renewal/breakups, hunger/refusal, Swarm, terminal-loss consumers and wardrobe variants");
    }
    internal static void Run(Story story, Action<bool,string> check)
    {
        Cases(story, check);
        L07World.RejectMutation(story, s => L07World.Scene(s, "devarra.trickster.epilogue.hungry").Forbids = Array.Empty<string>(), Cases, check, "remove hungry closure");
        L07World.RejectMutation(story, s => L07World.Scene(s, "minagho_chivarro.trickster.epilogue.pair").Requires = L07World.Scene(s, "minagho_chivarro.trickster.epilogue.pair").Requires.Where(k => k != "minagho.life.available" && k != "minagho_chivarro.outcome.eligible").ToArray(), Cases, check, "remove all Minagho life guards at the pair consumer");
    }
}
