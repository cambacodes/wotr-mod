using System;
using System.Collections.Generic;
using System.Linq;

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
        /// <summary>How long the copies are watched after their bark triggers are forced.</summary>
        public double ObserveSeconds = 20;
        public double EntrySeconds = 180;
        public double SettleSeconds = 30;

        public void Normalize()
        {
            EnterPoint = string.IsNullOrWhiteSpace(EnterPoint) ? null : ResidenceSpikePlan.Norm(EnterPoint!);
            Units = (Units ?? new List<string>()).Where(u => !string.IsNullOrWhiteSpace(u)).Select(ResidenceSpikePlan.Norm).Distinct().ToList();
            if (Units.Count == 0) throw new FormatException("presence.units needs at least one unit blueprint guid.");
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
    }

    public sealed class PresenceSpikeResult
    {
        public string? Area;
        public string? EntryError;
        public string? NotIdle;
        public List<string> Skipped = new List<string>();
        public List<QuietCopyProbe> Copies = new List<QuietCopyProbe>();
        /// <summary>Dialogs that started while the copies were watched (none should: the harness opens none).</summary>
        public List<string> Dialogs = new List<string>();
        public List<string> Notes = new List<string>();
        public string? Error;
        public double Ms;
        public bool Passed;
        public List<string> Findings = new List<string>();

        /// <summary>
        /// Passes when at least one copy spawned, and every spawned copy exists, is not Player faction, is not in the party
        /// group, is passive, has silent asks, never entered combat, played no audible bark and was removed afterwards, and no
        /// dialog started while the copies were watched. Findings lists every failed check.
        /// </summary>
        public void Evaluate()
        {
            Findings.Clear();
            if (Error != null) Findings.Add(Error);
            if (EntryError != null) Findings.Add("entry: " + EntryError);
            if (NotIdle != null) Findings.Add("not idle: " + NotIdle);
            var spawned = Copies.Where(c => c.Spawned).ToList();
            if (Error == null && EntryError == null && NotIdle == null && spawned.Count == 0)
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
            if (Dialogs.Count > 0) Findings.Add("dialogs started while watching: " + string.Join("; ", Dialogs));
            Passed = Findings.Count == 0;
        }
    }
}
