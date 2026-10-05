using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using Newtonsoft.Json;

namespace RRT.TestHarness
{
    // -Spike Presence: the quiet-copy check (E12d). Spawn-copy presences are instances of native unit blueprints, several of
    // them companions (Player faction, party AI, the companion's voice). The spike spawns copies through RRT's own
    // GuestPresence near the Commander in Drezen, forces their bark triggers, watches them for a while and checks that they
    // stay silent, neutral, out of the party group and out of combat, and start no dialog. Pure data and policy: no Unity or
    // game types, so the offline self-test can load it. The runtime half is HarnessRunner.PresenceSpike (PresenceSpike.cs).
    public sealed class PresenceSpikePlan
    {
        public const string DrezenCapital = "2570015799edf594daf2f076f2f975d8";
        public const string EnterFromThroneRoom = "51ec615b45183294bb9b065d9a913e99";   // DrezenCapital_FromThroneRoom

        /// <summary>Enter point loaded first when the save is not already in Drezen (capital); "" or null: stay in the loaded area.</summary>
        public string? EnterPoint = EnterFromThroneRoom;
        /// <summary>Unit blueprints to copy; each with no live unit in the area is spawned (the engine's duplicate guard).</summary>
        public List<string> Units = new List<string>
        {
            "397b090721c41044ea3220445300e1b8",   // Camelia_Companion (camellia.presence): Player faction, CMP_Camelia_Barks
            "e3bc95db7e2181d41847b3a1d858258d",   // EvilArueshalae_Companion (arueshalae.presence.evil*): Player faction
            "90481a29cc75f424b9891a55c6dcbb53",   // Seelah_NPC_Level1 (seelah.presence): CMP_Seelah_Barks
            "81297c673b63b60448ef88a10db6bc78",   // AngelTargona (targona.presence): AngelTeam faction
        };
        /// <summary>Metres from the Commander the copies stand at (one per quarter turn).</summary>
        public float Distance = 3f;
        /// <summary>Optional scene entity id (a native locator in the loaded area): every copy spawns on it instead of beside the
        /// Commander, as an E12b At.Locator presence would (engine queue 9d: Devarra's Huge dragon at TerendelevUndeadLocator).
        /// The spike then also checks the spot: nearest walkable node, drift after the copy settles, and room for its body.</summary>
        public string? Locator;
        /// <summary>Inspect and click this production GuestPresence instead of spawning quiet copies.</summary>
        public string? Key;
        /// <summary>Alternative to Locator, as an E12b At.NearUnit presence: a native unit blueprint guid standing once in the area, with Side (left|right|front|behind) and AnchorDistance.</summary>
        public string? NearUnit;
        public string Side = "left";
        public float AnchorDistance = 2.5f;
        /// <summary>Optional x,y,z mesh query in the saved area; replaces the quiet-copy spike and never spawns units.</summary>
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public string? Probe;
        public float ProbeRadius = 10f;
        /// <summary>Probe mode only: enter the spike's enter point (Drezen capital) first, like the copy spike does.</summary>
        public bool ProbeEnter;
        [JsonIgnore] public float[]? ProbeCoordinates;
        /// <summary>Largest accepted gap (m) between the locator and the nearest walkable node, and drift of the settled copy.</summary>
        public float MaxWalkableGap = 1.5f;
        /// <summary>How long the copies are watched after their bark triggers are forced.</summary>
        public double ObserveSeconds = 20;
        public double EntrySeconds = 180;
        public double SettleSeconds = 30;

        public void Normalize()
        {
            Key = string.IsNullOrWhiteSpace(Key) ? null : Key!.Trim();
            if (Key != null && (Probe != null || Locator != null || NearUnit != null))
                throw new FormatException("presence.key cannot be combined with copy/probe overrides.");
            ProbeCoordinates = null;
            if (Probe != null)
            {
                var parts = Probe.Split(',');
                var coordinates = new float[3];
                if (parts.Length != 3 || parts.Where((part, i) => !float.TryParse(part, NumberStyles.Float, CultureInfo.InvariantCulture, out coordinates[i])
                    || float.IsNaN(coordinates[i]) || float.IsInfinity(coordinates[i])).Any())
                    throw new FormatException("presence.probe needs three finite coordinates: x,y,z (decimal point, commas between coordinates).");
                ProbeCoordinates = coordinates;
                if (!string.IsNullOrWhiteSpace(Locator)) throw new FormatException("presence.probe cannot be combined with presence.locator.");
            }
            if (ProbeRadius <= 0f || float.IsNaN(ProbeRadius) || float.IsInfinity(ProbeRadius))
                throw new FormatException("presence.probeRadius must be finite and greater than zero.");
            EnterPoint = string.IsNullOrWhiteSpace(EnterPoint) ? null : ResidenceSpikePlan.Norm(EnterPoint!);
            Locator = string.IsNullOrWhiteSpace(Locator) ? null : Locator!.Trim().ToLowerInvariant();
            if (MaxWalkableGap <= 0f) MaxWalkableGap = 1.5f;
            Units = (Units ?? new List<string>()).Where(u => !string.IsNullOrWhiteSpace(u)).Select(ResidenceSpikePlan.Norm).Distinct().ToList();
            if (Units.Count == 0 && ProbeCoordinates == null && Key == null) throw new FormatException("presence.units needs at least one unit blueprint guid.");
            if (Distance < 1f) Distance = 1f;
            if (ObserveSeconds < 1) ObserveSeconds = 1;
            if (EntrySeconds < 10) EntrySeconds = 10;
            if (SettleSeconds < 1) SettleSeconds = 1;
        }
    }

    public sealed class QuietCopyProbe
    {
        public string? Unit;
        public string? UnitName;
        public string? NativeFaction;      // the blueprint's faction (what the copy had before E12d)
        public string? NativeAsks;         // the blueprint's voice set
        public string? EngineStatus;
        public string? Quiet;              // GuestPresence.LastQuiet at spawn: the repairs applied
        public bool Spawned;
        public bool Exists;
        public string? Faction;
        public bool PlayerFaction;
        public bool PartyGroup;            // in the party's unit group (shares its fights)
        public bool Passive;
        public string? Asks;               // the copy's effective asks list
        public bool AsksSilent;            // no voice event or text in any bark (checked on the live component)
        public bool InCombat;              // ever in combat while watched
        public List<string> Barks = new List<string>();     // audible barks the copy played (voice event or text)
        public bool Removed;
        public string? Error;
        // Locator mode (PresenceSpikePlan.Locator): where the copy was asked to stand and how the spot held it.
        public float[]? Target;            // the locator's position (x, y, z)
        public float? WalkableGap;         // metres from the target to the nearest walkable node
        public float? Drift;               // metres the settled copy stands from the target
        public float? Corpulence;          // the copy's body radius (m)
        public List<string> Crowding = new List<string>();   // other live units inside the copy's body radius + 1 m
    }

    public sealed class PresenceSpikeResult
    {
        public string? Area;
        public string? EntryError;
        public string? NotIdle;
        public List<string> Skipped = new List<string>();
        public List<QuietCopyProbe> Copies = new List<QuietCopyProbe>();
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)] public WalkableProbe? Probe;
        /// <summary>Dialogs that started while the copies were watched (none should: the harness opens none).</summary>
        public List<string> Dialogs = new List<string>();
        public List<string> Notes = new List<string>();
        public ProductionPresenceProbe? Production;
        public ProductionPresenceProbe? ProductionAfterReload;
        public bool ProductionReloadRequired;
        public string? Error;
        public string? Locator;            // the plan's locator, when set
        public string? LocatorError;       // the locator did not resolve in the loaded area
        public float MaxWalkableGap = 1.5f;
        public List<string> Screenshots = new List<string>();
        public double Ms;
        public bool Passed;
        public List<string> Findings = new List<string>();

        /// <summary>
        /// Passes when at least one copy spawned, and every spawned copy exists, is not Player faction, is not in the party
        /// group, is passive, has silent asks, never entered combat, played no audible bark and was removed afterwards, and no
        /// dialog started while the copies were watched. A mesh probe instead needs walkable points and no query error.
        /// Findings lists every failed check.
        /// </summary>
        public void Evaluate()
        {
            Findings.Clear();
            if (Error != null) Findings.Add(Error);
            if (EntryError != null) Findings.Add("entry: " + EntryError);
            if (NotIdle != null) Findings.Add("not idle: " + NotIdle);
            var spawned = Copies.Where(c => c.Spawned).ToList();
            if (Probe != null)
            {
                if (Probe.Error != null) Findings.Add("mesh probe: " + Probe.Error);
                if (Probe.Points.Count == 0 && Probe.Error == null) Findings.Add("mesh probe: no walkable points within " + Probe.Radius + " m");
            }
            if (Production != null) Findings.AddRange(Production.Failures());
            if (ProductionReloadRequired)
            {
                if (ProductionAfterReload == null) Findings.Add("production presence was not checked after reload");
                else
                {
                    Findings.AddRange(ProductionAfterReload.Failures().Select(f => "after reload: " + f));
                    if (ProductionAfterReload.ActorId != Production?.ActorId) Findings.Add("production actor identity changed after reload");
                }
            }
            if (Production == null && Probe == null && Error == null && EntryError == null && NotIdle == null && spawned.Count == 0)
                Findings.Add("no copy was spawned" + (Skipped.Count > 0 ? "; skipped " + string.Join("; ", Skipped) : "")
                    + string.Concat(Copies.Where(c => c.EngineStatus != null).Select(c => "; " + c.UnitName + ": " + c.EngineStatus)));
            foreach (var c in Copies)
            {
                string who = c.UnitName ?? c.Unit ?? "?";
                if (c.Error != null) Findings.Add(who + ": " + c.Error);
                if (!c.Spawned) continue;
                if (!c.Exists) Findings.Add(who + ": the copy is not in the area state, in game and alive");
                if (c.PlayerFaction) Findings.Add(who + ": the copy is Player faction (" + c.Faction + ")");
                if (c.PartyGroup) Findings.Add(who + ": the copy is in the party's unit group");
                if (!c.Passive) Findings.Add(who + ": the copy is not passive");
                if (!c.AsksSilent) Findings.Add(who + ": the copy's asks are voiced (" + c.Asks + ")");
                if (c.InCombat) Findings.Add(who + ": the copy entered combat");
                if (c.Barks.Count > 0) Findings.Add(who + ": the copy barked: " + string.Join(", ", c.Barks.Take(5)));
                if (!c.Removed) Findings.Add(who + ": the copy was not removed afterwards (cleanup)");
            }
            if (LocatorError != null) Findings.Add("locator " + Locator + ": " + LocatorError);
            foreach (var c in Copies.Where(c => c.Spawned && Locator != null))
            {
                string who = c.UnitName ?? c.Unit ?? "?";
                if (c.WalkableGap == null || c.WalkableGap > MaxWalkableGap)
                    Findings.Add(who + ": the locator is " + (c.WalkableGap?.ToString("0.00") ?? "?") + " m from the walkable mesh");
                if (c.Drift == null || c.Drift > MaxWalkableGap)
                    Findings.Add(who + ": the settled copy drifted " + (c.Drift?.ToString("0.00") ?? "?") + " m from the locator");
                if (c.Crowding.Count > 0) Findings.Add(who + ": no room for its body (" + string.Join(", ", c.Crowding.Take(5)) + ")");
            }
            if (Dialogs.Count > 0) Findings.Add("dialogs started while watching: " + string.Join("; ", Dialogs));
            Passed = Findings.Count == 0;
        }
    }
}
