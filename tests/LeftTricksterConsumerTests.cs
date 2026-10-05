using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Tirabade;

// eng8-q8b: real Rules availability, not a second path simulator.
internal static class LeftTricksterConsumerTests
{
    private const string W = "wenduag.trickster.";
    private static readonly string[] Paths = { "legend", "dragon", "swarm", "trickster.failed" };

    internal static void Run(Story story, Action<bool, string> check)
    {
        using var doc = JsonDocument.Parse(File.ReadAllText("tools/left_trickster_consumer_contracts.json"));
        var contract = doc.RootElement;
        var ids = contract.GetProperty("scenes").EnumerateArray().Select(e => e.GetString()!).ToHashSet();
        var prefix = contract.GetProperty("court_prefix").GetString()!;
        var consumers = story.Scenes.Where(s => ids.Contains(s.Id) || s.Id.StartsWith(prefix, StringComparison.Ordinal)).ToArray();
        check(consumers.Length >= 30, "q8b consumer inventory lost native twins or sibling entries");
        foreach (var id in ids) check(consumers.Any(s => s.Id == id), "q8b missing consumer " + id);

        // Earn the legacy return through the existing cairn and acceptance
        // choices. Native killed/dead observations are fixture inputs only.
        var cairn = L07World.Scene(story, W + "killed.cairn");
        var buried = L07World.Play(story, cairn, L07World.Seed(story, cairn, "trickster", "wenduag.killed", "wenduag.dead_any", "lann.in_party"))
            .First(w => w.Has(W + "cairn_built") && w.Has(W + "cost.lied_to_lann"));
        var back = L07World.Scene(story, W + "killed.back");
        var offered = L07World.Move(story, back, buried);
        check(Rules.Available(story, back, offered), "q8b earned legacy return unavailable");
        var outcomes = L07World.Play(story, back, offered).ToArray();
        var returned = outcomes.First(w => w.Has(W + "returned"));
        var refused = outcomes.First(w => w.Has(W + "stay_dead_ordered"));
        check(!buried.Has(W + "returned") && returned.Has(W + "returned"), "q8b return did not originate at its producer");
        check(returned.Has(W + "cairn_built") && returned.Has(W + "cost.lied_to_lann"),
            "q8b return lost its earned burial/payment history");

        // Also earn the native-companion branch through the actual outbid;
        // native recruitment is observed, not inferred from a copied actor.
        var bid = L07World.Scene(story, W + "traitor.bid");
        var kept = L07World.Play(story, bid, L07World.Seed(story, bid, "trickster", "wenduag.in_party"))
            .First(w => w.Has(W + "bought"));
        var ready = new Dictionary<string, Snapshot>();
        Snapshot At(Scene scene, Snapshot history)
        {
            var state = L07World.Move(story, scene, history);
            if (scene.ContactUnit != null) state.AvailableContacts.Add(scene.ContactUnit);
            state.AvailableContacts.UnionWith(scene.AdditionalContactUnits);
            state.Flags.UnionWith(new[] { "regill.in_party", "lann.in_party", "savamelekh.dead.l", "yaniel.freed" });
            // Her independent in-person return is an external fixture. L14
            // owns its presence gate; this lane never earns it for the player.
            if (scene.Id.Contains("court.vellexia"))
            {
                var external = L07World.Seed(story, scene, "trickster");
                state.Flags.UnionWith(external.Flags.Where(k => k.StartsWith("vellexia.", StringComparison.Ordinal)));
            }
            foreach (var flag in state.Flags) if (!state.Times.ContainsKey(flag)) state.Times[flag] = 1;
            return L07World.Refresh(story, state);
        }
        Snapshot Earn(string suffix, Snapshot history, Func<Snapshot, bool> success)
        {
            var scene = L07World.Scene(story, W + suffix);
            var start = At(scene, history);
            check(Rules.Available(story, scene, start), "q8b earned progression unavailable " + scene.Id);
            ready[scene.Id] = start;
            return L07World.Play(story, scene, start).First(success);
        }
        foreach (var initial in new[] { returned, kept })
        {
            bool inParty = initial.Has("wenduag.in_party");
            string twin = inParty ? ".native_visit" : "";
            var proven = Earn("court.trial" + twin, initial, w => w.Has(W + "proved"));
            var gate = Earn("court.gate" + twin, proven, w => w.Has(W + "gate_seen"));
            string claim = "court." + (inParty ? "claim_in_person" : "claim");
            var committed = Earn(claim, gate, w => w.Has("wenduag.committed"));
            var rejected = L07World.Play(story, L07World.Scene(story, W + claim), ready[W + claim])
                .First(w => w.Has(W + "court.claim_refused"));
            var intimate = Earn("court.cairn" + twin, committed, w => w.Has(W + "court.cairn"));
            Earn("court.morning" + twin, intimate, w => w.Has(W + "court.morning"));
            foreach (var suffix in new[] { "vellexia", "yaniel", "neathers", "hunt", "gongs" })
                ready[W + "court." + suffix + twin] = At(L07World.Scene(story, W + "court." + suffix + twin), committed);
            if (!inParty)
            {
                ready[W + "court.stinger"] = At(L07World.Scene(story, W + "court.stinger"), returned);
                var stingerTwin = At(L07World.Scene(story, W + "court.stinger.native_visit"), returned);
                stingerTwin.Flags.Add("wenduag.in_party"); L07World.Refresh(story, stingerTwin);
                ready[W + "court.stinger.native_visit"] = stingerTwin; // inherited legacy/native-history surface
                ready[W + "epilogue.pack"] = At(L07World.Scene(story, W + "epilogue.pack"), committed);
                ready[W + "epilogue.unclaimed"] = At(L07World.Scene(story, W + "epilogue.unclaimed"), returned);
                ready[W + "epilogue.refused"] = At(L07World.Scene(story, W + "epilogue.refused"), rejected);
                ready[W + "epilogue.dead"] = At(L07World.Scene(story, W + "epilogue.dead"), refused);
                var truth = Earn("lann.truth", returned, w => w.Has(W + "lann.paid"));
                ready[W + "lann.found_out"] = At(L07World.Scene(story, W + "lann.found_out"), returned);
                var morning = At(L07World.Scene(story, W + "react.lann_morning"), intimate);
                morning.Flags.UnionWith(truth.Flags.Where(k => k.StartsWith(W + "lann.", StringComparison.Ordinal)));
                ready[W + "react.lann_morning"] = L07World.Refresh(story, morning);
                ready[W + "react.regill_watch"] = At(L07World.Scene(story, W + "react.regill_watch"), returned);
            }
        }
        ready[W + "killed.cellar"] = At(L07World.Scene(story, W + "killed.cellar"), returned);

        foreach (var scene in consumers)
        {
            check(scene.Requires.Contains("trickster.now"), "q8b entry guard absent " + scene.Id);
            // Mapped sites use the producer histories above. The two Irabeth
            // street siblings are old staged-street histories, whose producer
            // is retired; keep their save fixture separate from live traversal.
            bool legacyStreet = scene.Id == W + "react.irabeth_traitor" || scene.Id == W + "react.irabeth_suspicion";
            check(ready.ContainsKey(scene.Id) || legacyStreet, "q8b consumer lacks an earned producer history " + scene.Id);
            var prepared = ready.TryGetValue(scene.Id, out var history)
                ? history : L07World.Seed(story, scene, "trickster");
            L07World.Refresh(story, prepared);
            check(Rules.Available(story, scene, prepared), "q8b current consumer unavailable " + scene.Id);
            // Existing claim fallback is retired in favor of physical contact.
            foreach (var path in Paths)
            {
                foreach (bool staleMembership in new[] { false, true })
                {
                    var former = Program.Copy(prepared);
                    if (!staleMembership) former.Flags.Remove("trickster");
                    former.Flags.Add(path); L07World.Refresh(story, former);
                    check(former.Has("trickster.ever"), "q8b conversion lost the historical path latch");
                    check(!Rules.Available(story, scene, former), "q8b off-path consumer " + scene.Id + "/" + path);
                    check(!Rules.Available(story, scene, L07World.Refresh(story, Program.Copy(former))),
                        "q8b reload exposed consumer " + scene.Id + "/" + path);
                }
            }
        }

        foreach (var path in Paths)
        {
            var former = Program.Copy(returned); former.Flags.Add(path); L07World.Refresh(story, former);
            check(former.Flags.Contains(W + "returned") && former.Has("wenduag.killed") && former.Has("wenduag.dead_any"),
                "q8b erased history/native fate " + path);
            check(!former.Has(Rules.WenduagEchoPrefix + "returned_available") && !former.Has("wenduag.life.available"),
                "q8b legacy return still lifts death after conversion " + path);
            check(!Rules.RouteOpen(story.Relationships["wenduag"], former), "q8b legacy route open after conversion " + path);
            foreach (var id in new[] { W + "epilogue.unclaimed", W + "epilogue.refused", W + "epilogue.pack" })
                check(!Rules.Available(story, L07World.Scene(story, id), L07World.Move(story, L07World.Scene(story, id), former)),
                    "q8b paid legacy consumer off-path " + id);
            var closure = L07World.Move(story, L07World.Scene(story, W + "epilogue.dead"), refused);
            closure.Flags.Add(path); L07World.Refresh(story, closure);
            check(!Rules.Available(story, L07World.Scene(story, W + "epilogue.dead"), closure), "q8b staged-dead closure off-path");
        }

        // Native living companion remains alive; authored Trickster courtship
        // is withheld. This policy never manufactures a native death.
        var native = L07World.Seed(story, L07World.Scene(story, W + "court.trial.native_visit"), "trickster", "wenduag.in_party");
        native.Flags.Remove(W + "returned"); native.Flags.Add(W + "bought"); L07World.Refresh(story, native);
        native.Flags.Add("legend"); L07World.Refresh(story, native);
        check(native.Has("wenduag.in_party") && native.Has("wenduag.life.available"), "q8b conversion killed native companion");

        // Persistent paid resurrection control uses its real producer. The
        // legacy-copy rule must never be generalized to all completed returns.
        var battle = L07World.Scene(story, "camellia.trickster.dead.overacting");
        var paid = L07World.Play(story, battle, L07World.Seed(story, battle, "trickster", "camellia.dead", "revive.camellia.available"))
            .First(w => w.Has("camellia.trickster.returned"));
        foreach (var path in new[] { "legend", "dragon", "trickster.failed" })
        {
            var later = Program.Copy(paid); later.Flags.Add(path); L07World.Refresh(story, later);
            check(later.Has("camellia.trickster.returned") && later.Has("camellia.trickster.cost.spirits_owed")
                && later.Has("camellia.life.available") && Rules.RouteOpen(story.Relationships["camellia"], later),
                "q8b persistent paid return invalidated " + path);
        }
        Console.WriteLine("eng8-q8b: current/off-path/reload consumer matrix; earned legacy return, native fate and persistent paid-return controls");
    }
}
