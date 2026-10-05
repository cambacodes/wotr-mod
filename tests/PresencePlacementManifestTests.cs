using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;
using Tirabade;

// E-Q7-33: offline evidence gate. Pending records cannot authorize a destination.
internal static class PresencePlacementManifestTests
{
    internal static string ArchivePath()
    {
        var candidates = new[] { Environment.GetEnvironmentVariable("RRT_BLUEPRINTS_ZIP"),
            "/wrath/blueprints.zip", Path.Combine(Environment.GetEnvironmentVariable("RRT_GAME_DIR") ?? "",
                "blueprints.zip"), @"C:\Program Files (x86)\Steam\steamapps\common\Pathfinder Second Adventure\blueprints.zip" };
        return candidates.FirstOrDefault(p => p != null && File.Exists(p))
            ?? throw new InvalidOperationException("E-Q7-33: blueprint archive required (RRT_BLUEPRINTS_ZIP)");
    }

    internal static JsonElement NativeRecord(string path)
    {
        using var archive = ZipFile.OpenRead(ArchivePath());
        using var stream = (archive.GetEntry(path) ?? throw new Exception("Native fixture missing: " + path)).Open();
        using var json = JsonDocument.Parse(stream);
        return json.RootElement.Clone();
    }

    // Deliberately separate structural validity from verified delivery. The F7 coordinator's
    // street-door staging decision does not substitute for a completed live delivery probe.
    internal static bool Authorized(JsonNode entry, out string reason)
    {
        reason = "pending coordinator live evidence";
        if (entry["status"]?.GetValue<string>() != "verified") return false;
        var probe = entry["probe"];
        if (probe == null || entry["chapter"]?.GetValue<int>() != probe["chapter"]?.GetValue<int>()
            || entry["area"]?.GetValue<string>() != probe["area"]?.GetValue<string>()
            || entry["id"]?.GetValue<string>() != probe["placement"]?.GetValue<string>()
            || string.IsNullOrWhiteSpace(probe["scene"]?.GetValue<string>())
            || string.IsNullOrWhiteSpace(probe["save_sha256"]?.GetValue<string>()))
        { reason = "probe identity/chapter/area/save missing or mismatched"; return false; }
        if (entry["kind"]?.GetValue<string>() == "destination"
            && (entry["position"] is not JsonArray position || position.Count != 3
                || position.Any(p => p == null || !double.IsFinite(p.GetValue<double>()))) )
        { reason = "destination coordinates missing/unsafe"; return false; }
        string? artifact = probe["artifact"]?.GetValue<string>();
        if (artifact == null || !Path.IsPathFullyQualified(artifact) || !File.Exists(artifact)
            || Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(artifact))).ToLowerInvariant() != probe["sha256"]?.GetValue<string>())
        { reason = "probe artifact missing or changed"; return false; }
        var result = JsonNode.Parse(File.ReadAllText(artifact))!;
        if (result["chapter"]?.GetValue<int>() != probe["chapter"]?.GetValue<int>()
            || result["area"]?.GetValue<string>() != probe["area"]?.GetValue<string>()
            || result["placement"]?.GetValue<string>() != probe["placement"]?.GetValue<string>()
            || result["scene"]?.GetValue<string>() != probe["scene"]?.GetValue<string>()
            || result["save_sha256"]?.GetValue<string>() != probe["save_sha256"]?.GetValue<string>()
            || result["position"]?.ToJsonString() != entry["position"]?.ToJsonString()
            || result["at"]?.ToJsonString() != entry["at"]?.ToJsonString()
            || new[] { "walkable", "approachable", "clickable", "occupancy_clear", "after_reload" }
                .Any(k => result[k]?.GetValue<bool>() != true)
            || result["walkable_gap"] == null || result["drift"] == null
            || !double.IsFinite(result["walkable_gap"]!.GetValue<double>())
            || !double.IsFinite(result["drift"]!.GetValue<double>())
            // Existing PresenceSpikePlan.MaxWalkableGap and runtime arrival tolerance: 1.5 m.
            || result["walkable_gap"]!.GetValue<double>() < 0 || result["walkable_gap"]!.GetValue<double>() > 1.5
            || result["drift"]!.GetValue<double>() < 0 || result["drift"]!.GetValue<double>() > 1.5)
        { reason = "probe failed mesh/approach/click/occupancy/reload or differs from placement"; return false; }
        reason = "verified";
        return true;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        DrezenAreaTruth(story, check);
        var manifest = JsonNode.Parse(File.ReadAllText("tools/presence_placement_manifest.json"))!;
        check(manifest["schema_version"]!.GetValue<int>() == 1 && manifest["item"]!.GetValue<string>() == "E-Q7-33",
            "E-Q7-33: unknown placement manifest schema");
        check(manifest["probe_contract"]!["max_walkable_gap"]!.GetValue<double>() == 1.5
            && manifest["probe_contract"]!["max_drift"]!.GetValue<double>() == 1.5,
            "E-Q7-33: manifest differs from existing harness/runtime tolerances");
        using var archive = ZipFile.OpenRead(ArchivePath());
        var types = new Dictionary<string, string>();
        foreach (var target in manifest["native_targets"]!.AsArray())
        {
            using var stream = archive.GetEntry(target!["path"]!.GetValue<string>())!.Open();
            using var memory = new MemoryStream(); stream.CopyTo(memory);
            byte[] bytes = memory.ToArray();
            using var native = JsonDocument.Parse(bytes);
            string guid = native.RootElement.GetProperty("AssetId").GetString()!;
            string type = native.RootElement.GetProperty("Data").GetProperty("$type").GetString()!.Split(", ").Last();
            check(guid == target["guid"]!.GetValue<string>() && type == target["type"]!.GetValue<string>()
                && Convert.ToHexString(SHA256.HashData(bytes)).ToLowerInvariant() == target["sha256"]!.GetValue<string>(),
                "E-Q7-33: pinned native GUID/type/evidence differs: " + guid);
            types.Add(guid, type);
        }
        var entries = manifest["entries"]!.AsArray();
        check(entries.Select(e => e!["id"]!.GetValue<string>()).Distinct().Count() == entries.Count,
            "E-Q7-33: duplicate placement id");
        foreach (var entry in entries)
        {
            check(types[entry!["area"]!.GetValue<string>()] == "BlueprintArea", "E-Q7-33: area is not a verified BlueprintArea");
            if (entry["unit"] != null)
                check(types[entry["unit"]!.GetValue<string>()] == "BlueprintUnit", "E-Q7-33: actor is not a verified BlueprintUnit");
            if (entry["at"]?["NearUnit"] != null)
                check(types[entry["at"]!["NearUnit"]!.GetValue<string>()] == "BlueprintUnit", "E-Q7-33: anchor has wrong type");
            if (entry["at"]?["Locator"] != null)
                check(Guid.TryParse(entry["at"]!["Locator"]!.GetValue<string>(), out _), "E-Q7-33: invalid scene locator identity");
            check(entry["chapter"]!.GetValue<int>() is 3 or 5, "E-Q7-33: unexpected placement chapter");
            string status = entry["status"]!.GetValue<string>();
            check(status is "pending" or "verified", "E-Q7-33: unknown evidence status");
            if (status == "verified")
                check(Authorized(entry, out _), "E-Q7-33: a declared verified placement lacks matching successful live evidence");
            else
                check(entry["position"] == null && entry["probe"] == null && !Authorized(entry, out _)
                    && !string.IsNullOrWhiteSpace(entry["remainder"]?.GetValue<string>()),
                    "E-Q7-33: pending placement assigned guessed coordinates/evidence or hid its remainder");
            if (entry["kind"]!.GetValue<string>() == "presence")
            {
                var presence = story.Presences[entry["consumer"]!.GetValue<string>()];
                var expectedAt = JsonSerializer.SerializeToNode(presence.At, new JsonSerializerOptions { IncludeFields = true, DefaultIgnoreCondition = System.Text.Json.Serialization.JsonIgnoreCondition.WhenWritingNull })!;
                foreach (var property in entry["at"]!.AsObject())
                    check(property.Key == "Distance"
                        ? presence.At!.Distance == property.Value!.GetValue<double>()
                        : property.Key == "Offset"
                        ? JsonSerializer.Deserialize<float[]>(expectedAt[property.Key]!.ToJsonString())!
                            .SequenceEqual(JsonSerializer.Deserialize<float[]>(property.Value!.ToJsonString())!)
                        : expectedAt[property.Key]?.ToJsonString() == property.Value?.ToJsonString(),
                        "E-Q7-33: placement differs from exported anchor: " + property.Key);
                int probeChapter = entry["chapter"]!.GetValue<int>();
                check(presence.Unit == entry["unit"]!.GetValue<string>() && presence.Area == entry["area"]!.GetValue<string>()
                    && presence.MinChapter <= probeChapter && probeChapter <= presence.MaxChapter,
                    "E-Q7-33: exported placement chapter/area/unit differs");
                var state = new Snapshot { Area = presence.Area, Chapter = probeChapter, Hour = 10000 };
                state.Flags.UnionWith(presence.Requires);
                foreach (var group in presence.RequiresAnyGroups) state.Flags.Add(group.First());
                Rules.Complete(story, state);
                check(Rules.PresenceWanted(presence, state), "E-Q7-33: placement positive fixture did not execute: " + entry["id"]);
                check(Rules.PlanPresence(presence, true, new PresenceObservation { AreaLoaded = true, AnchorResolved = false }).Contains(PresenceStep.Blocked),
                    "E-Q7-33: missing anchor did not fail closed");
                state.Chapter = presence.MinChapter - 1;
                check(!Rules.PresenceWanted(presence, state), "E-Q7-33: anchor leaked below chapter window");
                state.Chapter = presence.MaxChapter + 1;
                check(!Rules.PresenceWanted(presence, state), "E-Q7-33: anchor leaked above chapter window");
                state.Chapter = probeChapter; state.Area = "elsewhere";
                check(!Rules.PresenceWanted(presence, state), "E-Q7-33: anchor leaked outside area");
            }
            if (entry["kind"]!.GetValue<string>() == "remote_event")
            {
                var scene = story.Scenes.Single(s => s.Id == entry["consumer"]!.GetValue<string>());
                check(Rules.IsRemote(scene) && scene.ContactUnit == null && !story.Presences.Keys.Any(k => k.StartsWith(entry["route"]!.GetValue<string>()) && entry["route"]!.GetValue<string>() == "chadali"),
                    "E-Q7-33: remote-only inventory is stale; a live placement now needs evidence");
            }
            if (status == "pending") Console.WriteLine("PENDING LIVE: E-Q7-33 " + entry["id"] + " — " + entry["remainder"]);
        }
        var cellar = entries.Single(e => e!["id"]!.GetValue<string>() == "wenduag.cellar")!;
        check(cellar["staging"]?.GetValue<string>() == "street-level cellar entrance"
            && cellar["candidate_position"]?.ToJsonString() == "[-24.63,40.13,57.17]",
            "F7: coordinator cellar-door staging decision missing");
        check(File.ReadAllText("src/WenduagEcho.cs").Contains(
                "TODO_VerifiedCellarPosition = new Vector3(-24.63f, 40.13f, 57.17f)"),
            "F7: runtime cellar-door point differs from the coordinator's verified street point");
        check(!Authorized(cellar, out _), "F7: pending cellar click/reload evidence was called verified");
        var promoted = cellar.DeepClone(); promoted["status"] = "verified";
        check(!Authorized(promoted, out _), "E-Q7-33: promotion without evidence passed");
        // Validator positive and mutation controls use a labelled synthetic probe in system temp,
        // never promote it into the real manifest or call it live evidence.
        string artifact = Path.GetTempFileName();
        try
        {
            promoted["position"] = new JsonArray(1.0, 2.0, 3.0);
            var result = new JsonObject { ["placement"] = "wenduag.cellar", ["chapter"] = 5,
                ["area"] = Rules.NurahCapital, ["scene"] = "synthetic-fixture", ["save_sha256"] = new string('a', 64),
                ["position"] = promoted["position"]!.DeepClone(), ["at"] = null,
                ["walkable"] = true, ["approachable"] = true, ["clickable"] = true, ["occupancy_clear"] = true,
                ["after_reload"] = true, ["walkable_gap"] = 0.2, ["drift"] = 0.3 };
            void SaveProbe()
            {
                File.WriteAllText(artifact, result.ToJsonString());
                var probe = result.DeepClone().AsObject(); probe["artifact"] = artifact;
                probe["sha256"] = Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(artifact))).ToLowerInvariant();
                promoted["probe"] = probe;
            }
            SaveProbe(); check(Authorized(promoted, out _), "E-Q7-33: valid synthetic probe contract rejected");
            foreach (string field in new[] { "walkable", "approachable", "clickable", "occupancy_clear", "after_reload" })
            {
                result[field] = false; SaveProbe(); check(!Authorized(promoted, out _), "E-Q7-33: failed probe accepted: " + field);
                result[field] = true;
            }
            result["walkable_gap"] = 3.0; SaveProbe(); check(!Authorized(promoted, out _), "E-Q7-33: unsafe mesh gap accepted");
            result["walkable_gap"] = 0.2; result["chapter"] = 3; SaveProbe();
            check(!Authorized(promoted, out _), "E-Q7-33: Ch3 probe authorized Ch5 placement");
            result["chapter"] = 5; result["area"] = "elsewhere"; SaveProbe();
            check(!Authorized(promoted, out _), "E-Q7-33: wrong-area probe accepted");
            result["area"] = Rules.NurahCapital; SaveProbe();
            File.AppendAllText(artifact, " "); check(!Authorized(promoted, out _), "E-Q7-33: changed evidence accepted");
        }
        finally { File.Delete(artifact); }
        Console.WriteLine("PASS: E-Q7-33 offline manifest GUID/type/chapter and evidence/mutation gates; pending live placements remain unresolved.");
    }

    private static void DrezenAreaTruth(Story story, Action<bool, string> check)
    {
        var table = JsonNode.Parse(File.ReadAllText("tools/drezen_area_chapters.json"))!;
        var areas = table["areas"]!.AsArray().ToDictionary(a => a!["guid"]!.GetValue<string>(), a => a!);
        foreach (var pair in story.Presences)
        {
            var p = pair.Value;
            check(areas.ContainsKey(p.Area), "F7: presence area absent from reachability table: " + pair.Key);
            var area = areas[p.Area];
            // Area and window are conjunctive: Chapter 4 in a 3..5 window does not
            // invent a capital visit during the Abyss. Exact impossible windows fail.
            var chapters = area["reachable_chapters"]!.AsArray().Select(c => c!.GetValue<int>());
            check(chapters.Any(c => p.MinChapter <= c && c <= p.MaxChapter),
                "F7: presence has no reachable (area, chapter) pair: " + pair.Key);
            if (p.At?.NearUnit != null)
                check(area["units"]!.AsArray().Any(u => u!["guid"]!.GetValue<string>() == p.At.NearUnit),
                    "F7: NearUnit absent from area's native blueprint unit list: " + pair.Key);
        }
        foreach (var scene in story.Scenes.Where(s => !Rules.IsRemote(s) && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)))
            foreach (string area in scene.Areas.Where(a => a == Rules.NurahCapital || a == "83a099db95e0e6e4485a20b10ce7c28d"))
            {
                var chapters = areas[area]["reachable_chapters"]!.AsArray().Select(c => c!.GetValue<int>()).ToArray();
                check(scene.Chapters.Length > 0 ? scene.Chapters.All(chapters.Contains)
                    : chapters.Any(c => scene.MinChapter <= c && c <= scene.MaxChapter),
                    "F7: encounter/hub has an unreachable Drezen chapter: " + scene.Id);
            }
        var presences = story.Presences.ToArray();
        for (int i = 0; i < presences.Length; i++)
            for (int j = i + 1; j < presences.Length; j++)
            {
                var a = presences[i].Value; var b = presences[j].Value;
                if (a.Area != Rules.NurahCapital || b.Area != a.Area || a.At?.NearUnit == null
                    || a.At.NearUnit != b.At?.NearUnit || Rules.PresencesExclusive(a, b)) continue;
                (double X, double Z) Offset(PresenceAnchor at) => at.Side switch {
                    "right" => (at.Distance, 0), "front" => (0, at.Distance),
                    "behind" => (0, -at.Distance), _ => (-at.Distance, 0) };
                var aa = Offset(a.At); var ba = Offset(b.At!);
                double distance = Math.Sqrt(Math.Pow(aa.X - ba.X, 2) + Math.Pow(aa.Z - ba.Z, 2));
                check(distance >= 4 - 0.000001,
                    "F7: coexisting shared-anchor presences are under 4 m apart: " + presences[i].Key + " / " + presences[j].Key);
            }
    }
}
