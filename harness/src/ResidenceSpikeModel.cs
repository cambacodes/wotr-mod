using System;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;

namespace RRT.TestHarness
{
    // P2 feasibility spike for the harem residence (Writer/handoffs/10-HAREM-RESIDENCE.md, 10b-RESIDENCE-SPIKE.md).
    // Pure data and policy: no Unity or game types, so the offline self-test can load it. The runtime half is
    // HarnessRunner.ResidenceSpike (ResidenceSpike.cs).
    public sealed class ResidenceSpikePlan
    {
        // Area TricksterCouncil ("Council Chamber") and its enter points (blueprints.zip, World/Areas/Mythics/TricksterCouncil).
        public const string CouncilArea = "28a49e115795ed44397b5a1503cef4f0";
        public const string EnterNative = "91c44d833734aa540ba18be8e0440cb9";      // TricksterCouncil_Enter (the closet's TeleportParty target)
        // Area mechanics (Addons) the etudes can add to the area; the dev presets name the same sets.
        public const string MechanicsCouncil1 = "f4fa4e2cdac6d51419104a1c7466eaeb";   // TricksterCouncil_Council1 (session members)
        public const string MechanicsNoCouncil = "d56190770d26e1d42800369d4902570f";  // TricksterCouncil_NoCouncil (members at rest)
        public const string MechanicsCouncilFight = "3a6513ad79a05134d837bf302e42d5ee"; // TricksterCouncil_CouncilFight

        /// <summary>BlueprintAreaEnterPoint to load. Default: TricksterCouncil_Enter, the target of the native closet.</summary>
        public string EnterPoint = EnterNative;
        /// <summary>x, y, z, orientation. Default: scene locator Locators/CouncilLoc3, facing the enter point.</summary>
        public float[] Seat = { 0f, 0f, 3.92f, 180f };
        /// <summary>x, y, z the copy is ordered to walk to. Default: Locators/CouncilLoc2 (4.7 m from the seat).</summary>
        public float[] PathTo = { 0f, 0f, -0.80f };
        /// <summary>Candidate native unit blueprints; the first with no live unit in the area is copied (the engine's duplicate guard).</summary>
        public List<string> Units = new List<string>
        {
            "b5e867e13503c6f41bb1316705efb4a2",   // AneviaTirabade_DrezenCapital (anevia.presence)
            "280d4712dceb37f4a88e98f1f4c6e64f",   // IrabethTirabade_DrezenCapital (irabeth.presence)
            "90481a29cc75f424b9891a55c6dcbb53",   // Seelah_NPC_Level1 (seelah.presence)
        };
        /// <summary>Loading the area must finish within this time.</summary>
        public double EntrySeconds = 180;
        /// <summary>After the area loads, wait this long for the game to become idle (native entry triggers run here).</summary>
        public double SettleSeconds = 30;
        public double PathSeconds = 12;
        public float PathMinMetres = 2f;

        public void Normalize()
        {
            if (string.IsNullOrWhiteSpace(EnterPoint)) EnterPoint = EnterNative;
            EnterPoint = Norm(EnterPoint);
            if (Seat == null || Seat.Length != 4) throw new FormatException("residence.seat must be [x, y, z, orientation].");
            if (PathTo == null || PathTo.Length != 3) throw new FormatException("residence.pathTo must be [x, y, z].");
            Units = (Units ?? new List<string>()).Where(u => !string.IsNullOrWhiteSpace(u)).Select(Norm).ToList();
            if (Units.Count == 0) throw new FormatException("residence.units needs at least one unit blueprint guid.");
            if (EntrySeconds < 10) EntrySeconds = 10;
            if (SettleSeconds < 1) SettleSeconds = 1;
            if (PathSeconds < 1) PathSeconds = 1;
            if (PathMinMetres <= 0) PathMinMetres = 0.5f;
        }

        public static string Norm(string guid) => guid.Replace("-", "").Trim().ToLowerInvariant();

        /// <summary>
        /// Names the loaded addon mechanics after the dev preset that loads the same set (TricksterCouncil_Default_Preset:
        /// Council1 + NoCouncil; TricksterCouncil_NoCouncil_Preset: NoCouncil). Anything else is "other".
        /// </summary>
        public static string ClassifyPreset(IEnumerable<string> mechanics)
        {
            var set = new HashSet<string>(mechanics.Select(Norm), StringComparer.Ordinal);
            if (set.Count == 0) return "base";
            if (set.SetEquals(new[] { MechanicsNoCouncil })) return "NoCouncil";
            if (set.SetEquals(new[] { MechanicsCouncil1, MechanicsNoCouncil })) return "Default";
            return "other";
        }
    }

    public sealed class PresenceProbe
    {
        public string? Unit;               // blueprint guid of the copied unit
        public string? UnitName;
        public List<string> Skipped = new List<string>();   // candidates passed over, with the reason
        public float[]? Seat;
        public string? EngineStatus;       // GuestPresence.Status after spawning
        public bool Spawned;               // the engine planned and executed a Spawn
        public bool Exists;                // the copy is in the area state, in game and alive
        public bool HasView;
        public bool ViewActive;
        public bool Rendered;              // a renderer of the view is visible to a camera (needs a rendered window)
        public float[]? Position;          // where the copy stands after spawning
        public double SeatErrorMetres;
        public double PathMovedMetres;
        public double PathRemainingMetres;
        public bool Pathed;
        public string? Dialog;             // RRT presence hub dialog started with the copy as the target unit
        public bool DialogStarted;
        public string? DialogSpeaker;
        public bool Removed;               // the engine removed the copy and forgot its record
        public string? Error;
    }

    public sealed class ResidenceSpikeResult
    {
        public string EntryMethod = "";
        public string? EnterPoint;
        public string? FromArea;
        /// <summary>The native closet teleports only while neither Obj_6a_KillNocta nor Obj_6b_KillCouncil is complete (ToCouncil_CheckPassedActions).</summary>
        public bool ClosetLive;
        public string? ClosetNote;
        public Dictionary<string, string> EtudesBefore = new Dictionary<string, string>();
        public Dictionary<string, string> EtudesAfter = new Dictionary<string, string>();
        public bool EntryStarted;
        public bool AreaLoaded;
        public double LoadMs;
        public string? EntryError;
        public string? NotIdleAfterEntry;
        public string? GameModeAfterEntry;
        public bool InCombatAfterEntry;
        /// <summary>"name guid scene-loaded" for each addon mechanics the etudes put into the area.</summary>
        public List<string> ActiveMechanics = new List<string>();
        public List<string> ActiveMechanicsGuids = new List<string>();
        public string Preset = "";
        /// <summary>Native actions that ran after the load started (ShowPartySelection, StartCombat, PlayCutscene, TeleportParty).</summary>
        public List<string> NativeActions = new List<string>();
        public List<string> AreaUnits = new List<string>();
        public PresenceProbe Presence = new PresenceProbe();
        public List<string> Screenshots = new List<string>();
        public List<string> Notes = new List<string>();
        public double Ms;
        // Verdicts (Evaluate).
        public bool EntryOk;
        public bool PresetOk;
        public bool PresenceOk;
        public bool Passed;
        public List<string> Findings = new List<string>();

        static readonly string[] Hostile = { "ShowPartySelection", "StartCombat" };

        /// <summary>
        /// (a) entry: the area loaded without an entry error. (b) preset: the loaded mechanics match Default or NoCouncil, no
        /// CouncilFight mechanics, no native party selection or combat, and the game settles idle. (c) presence: the copy
        /// spawned, exists with an active view (rendered, when the window renders), walked at least PathMinMetres, and a dialog
        /// started with it. Findings lists every failed check.
        /// </summary>
        public void Evaluate(bool requireRendered, float pathMinMetres)
        {
            Findings.Clear();
            EntryOk = EntryStarted && AreaLoaded && EntryError == null;
            if (!EntryStarted) Findings.Add("(a) the area load did not start" + (EntryError != null ? ": " + EntryError : ""));
            else if (!AreaLoaded) Findings.Add("(a) the area did not load" + (EntryError != null ? ": " + EntryError : ""));
            else if (EntryError != null) Findings.Add("(a) " + EntryError);

            var hostile = NativeActions.Where(a => Hostile.Any(h => a.StartsWith(h, StringComparison.Ordinal))).ToList();
            bool fight = ActiveMechanicsGuids.Contains(ResidenceSpikePlan.MechanicsCouncilFight);
            PresetOk = EntryOk && (Preset == "Default" || Preset == "NoCouncil") && !fight && hostile.Count == 0
                && NotIdleAfterEntry == null && !InCombatAfterEntry;
            if (EntryOk)
            {
                if (Preset != "Default" && Preset != "NoCouncil") Findings.Add("(b) loaded mechanics are " + Preset + ": " + string.Join(", ", ActiveMechanics));
                if (fight) Findings.Add("(b) the CouncilFight mechanics loaded");
                if (hostile.Count > 0) Findings.Add("(b) native entry actions ran: " + string.Join("; ", hostile));
                if (InCombatAfterEntry) Findings.Add("(b) the party is in combat after entry");
                if (NotIdleAfterEntry != null) Findings.Add("(b) not idle after entry: " + NotIdleAfterEntry);
            }

            var p = Presence;
            PresenceOk = p.Spawned && p.Exists && p.HasView && p.ViewActive && (!requireRendered || p.Rendered)
                && p.Pathed && p.DialogStarted && p.Error == null;
            if (AreaLoaded)
            {
                if (p.Error != null) Findings.Add("(c) " + p.Error);
                if (!p.Spawned) Findings.Add("(c) no copy was spawned" + (p.EngineStatus != null ? " (" + p.EngineStatus + ")" : "")
                    + (p.Skipped.Count > 0 ? "; skipped " + string.Join("; ", p.Skipped) : ""));
                else
                {
                    if (!p.Exists) Findings.Add("(c) the copy is not in the area state, in game and alive");
                    if (!p.HasView || !p.ViewActive) Findings.Add("(c) the copy has no active view");
                    if (requireRendered && !p.Rendered) Findings.Add("(c) no renderer of the copy is visible");
                    if (!p.Pathed) Findings.Add("(c) the copy walked " + p.PathMovedMetres.ToString("0.0") + " m (needs " + pathMinMetres.ToString("0.0") + " m)");
                    if (!p.DialogStarted) Findings.Add("(c) no dialog started with the copy" + (p.Dialog != null ? " (" + p.Dialog + ")" : ""));
                    if (!p.Removed) Findings.Add("(c) the copy was not removed afterwards (cleanup)");
                }
            }
            Passed = EntryOk && PresetOk && PresenceOk && p.Removed;
        }
    }
}
