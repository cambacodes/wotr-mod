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

    // Deliberately separate structural validity from verified delivery. A pending record is
    // a valid inventory entry but is never permission to assign a position in WenduagEcho.
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
                    check(property.Key == "Offset"
                        ? JsonSerializer.Deserialize<float[]>(expectedAt[property.Key]!.ToJsonString())!
                            .SequenceEqual(JsonSerializer.Deserialize<float[]>(property.Value!.ToJsonString())!)
                        : expectedAt[property.Key]?.ToJsonString() == property.Value?.ToJsonString(),
                        "E-Q7-33: placement differs from exported anchor: " + property.Key);
                int probeChapter = entry["chapter"]!.GetValue<int>();
                check(presence.Unit == entry["unit"]!.GetValue<string>() && presence.Area == entry["area"]!.GetValue<string>()
                    && presence.MinChapter <= probeChapter && probeChapter <= presence.MaxChapter,
                    "E-Q7-33: exported placement chapter/area/unit differs");
                var state = new Snapshot { Area = presence.Area, Chapter = probeChapter, Hour = 10000 };
                state.Flags.UnionWith(presence.Requires); Rules.Complete(story, state);
                check(Rules.PresenceWanted(presence, state), "E-Q7-33: placement positive fixture did not execute");
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
        if (!Authorized(cellar, out _))
            check(File.ReadAllText("src/WenduagEcho.cs").Contains("TODO_VerifiedCellarPosition = null"),
                "E-Q7-33: an unverified cellar destination was enabled in runtime");
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
}
