using System;
using System.Linq;
using Tirabade;

internal static class CurrentActInventoryTests
{
    private static readonly string[] Acts = {
        "iomedae.trickster.platform.bare", "iomedae.trickster.iz.night", "iomedae.trickster.disputation",
        "mielarah.trickster.raid.ashore", "wenduag.trickster.killed.back", "wenduag.trickster.abyss.back",
        "wenduag.trickster.street.fall", "wenduag.trickster.street.back"
    };
    internal static void Cases(Story story, Action<bool,string> check)
    {
        foreach (var id in Acts)
        {
            var scene = L07World.Scene(story, id);
            var prepared = L07World.Seed(story, scene, "trickster");
            // eng7-integ: l10 retires the completed native fall replays. Their
            // current-power contract still binds, but no positive replay is owed.
            check(scene.Requires.Contains("trickster.now"), "l07 current act lacks live power " + id);
            if (id == "wenduag.trickster.street.fall")
                check(scene.Forbids.Contains("trickster.ever") && !Rules.Available(story, scene, prepared),
                    "l10 retired street replay became available");
            else
            {
                check(Rules.Available(story, scene, prepared), "l07 positive act unavailable " + id);
                check(L07World.Play(story, scene, prepared, firstOnly: true).Any(w => w.Has(scene.Id)), "l07 positive act has no completed producer " + id);
            }
            foreach (var path in new[] { "trickster.failed", "legend", "dragon", "swarm" })
            {
                var left = Program.Copy(prepared); left.Flags.Add(path); L07World.Refresh(story, left);
                check(!Rules.Available(story, scene, left), "l07 former Trickster new act " + id + "/" + path);
            }
        }
        var memory = L07World.Scene(story, "iomedae.trickster.dream.chasm");
        var remembered = L07World.Play(story, memory, L07World.Seed(story, memory, "trickster"), firstOnly: true)
            .Single(w => w.Has("iomedae.trickster.bridge_seen"));
        remembered.Flags.UnionWith(new[] { "iomedae.started", "iomedae.key_dies_revealed" });
        var platform = L07World.Scene(story, "iomedae.trickster.platform.bare");
        var liveWager = L07World.Move(story, platform, remembered);
        check(Rules.Available(story, platform, liveWager), "l07 remembered bridge cannot originate live wager");
        liveWager.Flags.Add("trickster.failed"); L07World.Refresh(story, liveWager);
        check(!Rules.Available(story, platform, liveWager), "l07 Chapter 3 memory originates new wager after failure");
        foreach (var pair in new[] {
            ("wenduag.trickster.killed.cairn", "wenduag.trickster.killed.back", "wenduag.trickster.cairn_built"),
            ("wenduag.trickster.abyss.fall", "wenduag.trickster.abyss.back", "wenduag.trickster.abyss_cairn"),
            ("wenduag.trickster.street.fall", "wenduag.trickster.street.back", "wenduag.trickster.street_cairn") })
        {
            var primer = L07World.Scene(story, pair.Item1);
            if (pair.Item1 != "wenduag.trickster.killed.cairn")
            {
                check(primer.Forbids.Contains("trickster.ever")
                    && !Rules.Available(story, primer, L07World.Seed(story, primer, "trickster")),
                    "l10 retired primer can still earn custody " + pair.Item1);
                continue;
            }
            var primed = L07World.Play(story, primer, L07World.Seed(story, primer, "trickster"), firstOnly: true)
                .Single(w => w.Has(pair.Item3));
            var act = L07World.Scene(story, pair.Item2);
            if (pair.Item2.Contains("abyss")) primed.Flags.Add("wenduag.trickster.abyss_passage"); // separately earned smuggler agreement
            foreach (var path in new[] { "trickster.failed", "legend", "dragon" })
            {
                var former = L07World.Move(story, act, primed); former.Flags.Add(path); L07World.Refresh(story, former);
                check(!Rules.Available(story, act, former), "l07 cairn primer authorizes off-path return " + pair.Item2 + "/" + path);
            }
        }
        // Actual paid search producer precedes the Mielarah return.
        var returnScene = L07World.Scene(story, "mielarah.trickster.raid.ashore");
        var dispatch = story.Scenes.Single(s => s.Id == "mielarah.trickster.raid.overboard");
        var dispatchWorld = L07World.Seed(story, dispatch, "trickster");
        check(Rules.Available(story, dispatch, dispatchWorld), "l07 paid search producer unavailable");
        var paid = L07World.Play(story, dispatch, dispatchWorld)
            .First(w => w.Has("mielarah.trickster.raid.sent_back"));
        foreach (var path in new[] { "legend", "dragon", "trickster.failed" })
        {
            var former = L07World.Move(story, returnScene, paid); former.Flags.Add(path); L07World.Refresh(story, former);
            check(!Rules.Available(story, returnScene, former), "l07 paid search authorizes off-path return " + path);
        }
        var presence = story.Presences["wenduag.presence"];
        foreach (var path in new[] { "trickster.failed", "legend", "dragon", "swarm" })
        {
            var world = new Snapshot { Chapter = 5, Area = presence.Area, Hour = 10000 };
            world.Flags.UnionWith(new[] { "trickster", "chapter_later", "wenduag.trickster.returned" });
            L07World.Refresh(story, world);
            check(Rules.PresenceWanted(presence, world), "l07 live Wenduag copy missing");
            world.Flags.Add(path); L07World.Refresh(story, world);
            check(!Rules.PresenceWanted(presence, world) && world.Has("wenduag.trickster.returned"), "l07 Wenduag presence/history policy " + path);
            check(Rules.PlanPresence(presence, Rules.PresenceWanted(presence, world),
                new PresenceObservation { AreaLoaded = true, Recorded = true, Submitted = true, CopyFound = true, CopyAlive = true })
                .Contains(PresenceStep.Remove), "l07 conversion keeps owned Wenduag copy " + path);
            check(!Rules.PresenceWanted(presence, L07World.Refresh(story, Program.Copy(world))), "l07 reload recreates off-path copy");
            var edit = story.NativeEpilogueEdits["4bb3706172f1ed54ca11db96254c4638"];
            world.Flags.Add("wenduag.committed"); L07World.Refresh(story, world);
            foreach (var variant in Rules.EditVariants(edit)) check(!Rules.WhenHolds(variant.When, world), "l07 native Wenduag alternative off-path");
        }
        // Completed earned life is historical. Path failure neither re-kills her
        // nor removes the blood paid; only the new act/altered actor is withheld.
        var battle = L07World.Scene(story, "camellia.trickster.dead.overacting");
        var earned = L07World.Play(story, battle, L07World.Seed(story, battle, "trickster", "camellia.dead", "revive.camellia.available"))
            .First(w => w.Has("camellia.trickster.returned"));
        earned.Flags.Add("trickster.failed"); L07World.Refresh(story, earned);
        check(earned.Has("camellia.trickster.returned") && earned.Has("camellia.trickster.cost.spirits_owed") && Rules.RouteOpen(story.Relationships["camellia"], earned), "l07 completed earned return erased on conversion");
        foreach (var id in new[] { "wenduag.trickster.epilogue.native_service", "wenduag.trickster.epilogue.native_return" })
            check(!story.Scenes.Any(s => s.Id == id), "l07 obsolete native replacement reintroduced");
        foreach (var key in new[] { "wenduag.epilogue.greybor_contract", "wenduag.epilogue.ember_orphanage" })
            check(!story.NativeGates.ContainsKey(key), "l07 obsolete native gate reintroduced");
        Console.WriteLine("l07 E-Q7-08: live/failed/Legend/Dragon/Swarm act matrix, paid search, native alternatives, presence/reload and earned history executed");
    }
    internal static void Run(Story story, Action<bool,string> check)
    {
        Cases(story, check);
        L07World.RejectMutation(story, s => {
            var scene = L07World.Scene(s, "wenduag.trickster.street.fall");
            scene.Requires = scene.Requires.Where(k => k != "trickster.now").ToArray();
        }, Cases, check, "street OR bypass");
        L07World.RejectMutation(story, s => {
            var edit = s.NativeEpilogueEdits["4bb3706172f1ed54ca11db96254c4638"];
            edit.When = edit.When.Select(g => g.Select(k => k == "trickster.now" ? "trickster.ever" : k).ToArray()).ToArray();
        }, Cases, check, "native When history-only");
    }
}
