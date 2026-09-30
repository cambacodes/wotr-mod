using System;
using System.Linq;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Root;
using Kingmaker.Visual.Sound;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Newtonsoft.Json;
using UnityEngine;

namespace Tirabade
{
    // E12 (GLOBAL-07-lite): a data-driven "returned presence" for one relationship, generalizing the placement the
    // Konomi/Irabeth/Nurah meetings do by hand. The decisions are pure (Rules.PlanPresence); this class only observes the
    // loaded area and executes them on the main thread, while idle.
    //
    // What persists in a save, and what survives uninstalling the mod:
    //  - Player.SettingsList["RanRomance.Tirabade.Presence.<key>"]: a JSON string (PresenceRecord). An orphan string after
    //    uninstall; the game ignores unknown SettingsList entries. No custom component, etude or blueprint is created.
    //  - reuse-native: the native unit's own IsInGame flag and position (native unit state). Native etudes re-hide or re-place
    //    it on their next activation, with or without the mod.
    //  - spawn-copy: the copy is a plain instance of the NATIVE unit blueprint in the area's main scene state, so it loads
    //    without the mod. It is removed when the presence stops being wanted; if the mod is uninstalled while a copy stands,
    //    that copy stays in that area as an idle native NPC (documented limitation). A copy is never spawned while any live
    //    unit of the blueprint is in the area (duplicate guard), and never twice for one record.
    //  - E12d quiet copy: the copy's own unit state is set to native values (Neutrals faction, its own unit group, the native
    //    silent asks list PC_None_Barks as OverrideAsks) and it is marked Passive at run time (not saved; re-applied on every
    //    tick). All four are plain native state, so a save without the mod loads the copy as a silent, neutral bystander.
    internal sealed class GuestPresence
    {
        internal const string SavePrefix = "RanRomance.Tirabade.Presence.";
        internal readonly string Key;
        internal readonly Presence Spec;
        internal readonly BlueprintUnit Blueprint;
        internal Exception? LastError { get; private set; }
        internal string Status { get; private set; } = "not observed";

        internal GuestPresence(string key, Presence spec, BlueprintUnit blueprint)
        {
            Key = key;
            Spec = spec;
            Blueprint = blueprint;
        }

        internal string SaveKey => SavePrefix + Key;

        internal PresenceRecord? Read()
        {
            if (!Game.Instance.Player.SettingsList.TryGetValue(SaveKey, out var value)) return null;
            return value is string json ? PresenceRecord.Parse(json, Key) : null;
        }

        private void Write(PresenceRecord? record)
        {
            if (record == null) Game.Instance.Player.SettingsList.Remove(SaveKey);
            else Game.Instance.Player.SettingsList[SaveKey] = JsonConvert.SerializeObject(record);
        }

        private bool AreaLoaded(Game game) => game.Player != null && !game.IsLoadingSave && !game.IsUnloading
            && !LoadingProcess.Instance.IsLoadingInProcess && game.State.LoadedAreaState?.MainState != null
            && game.CurrentlyLoadedArea?.AssetGuid.ToString() == Spec.Area;

        // E12b: the placement for this tick (captured Position, or the live At anchor plus its offset).
        private Vector3 target;
        private float facing;
        internal bool AnchorFailed { get; private set; }
        // E12c: the unit a click-to-talk hub attaches to (our copy, else the present native unit), refreshed each tick.
        internal UnitEntityData? Actor { get; private set; }

        private bool ResolveTarget(Game game)
        {
            if (Spec.At == null)
            {
                if (Spec.Position == null) return false;
                target = new Vector3(Spec.Position.X, Spec.Position.Y, Spec.Position.Z);
                facing = Spec.Position.Orientation;
                return true;
            }
            Vector3 anchor;
            float orientation = 0f;
            if (Spec.At.NearUnit != null)
            {
                var guid = BlueprintGuid.Parse(Spec.At.NearUnit);
                var near = game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>().Where(unit => unit.Blueprint?.AssetGuid == guid
                    && !unit.Destroyed && !unit.DestroyMark && !unit.IsDisposed && unit.IsInGame && !unit.State.IsDead && !unit.State.IsFinallyDead).Take(2).ToArray();
                if (near.Length != 1) return false;
                anchor = near[0].Position;
                orientation = near[0].Orientation;
            }
            else
            {
                var entity = EntityService.Instance.GetEntity(Spec.At.Locator!);
                if (entity == null || entity.Destroyed) return false;
                anchor = entity.Position;
            }
            var offset = Rules.AnchorOffset(Spec.At, orientation);
            target = anchor + new Vector3(offset.Dx, 0f, offset.Dz);
            facing = offset.Facing;
            return true;
        }

        private Vector3 Target => target;

        // E12d: native blueprints the quiet copy uses (blueprints.zip): the Neutrals faction and PC_None_Barks, the empty voice.
        internal const string NeutralFaction = "d8de50cc80eb4dc409a983991e0b77ad";
        internal const string SilentAsks = "e7b22776ba8e2b84eaaff98e439639a7";
        internal const string PartyGroupId = "<directly-controllable-unit>";
        internal CopyQuiet LastQuiet { get; private set; }

        internal static CopyObservation ObserveCopy(UnitEntityData copy) => new CopyObservation
        {
            PlayerFaction = copy.Descriptor.Faction == BlueprintRoot.Instance.PlayerFaction,
            PartyGroup = copy.GroupId == PartyGroupId,
            Silenced = copy.Descriptor.OverrideAsks?.AssetGuid.ToString() == SilentAsks,
            Passive = copy.Passive,
        };

        // Main thread. Applies the repairs Rules.PlanQuiet asks for; a missing native blueprint skips only its own repair.
        internal static CopyQuiet Quiet(UnitEntityData copy)
        {
            var steps = Rules.PlanQuiet(ObserveCopy(copy));
            var done = CopyQuiet.None;
            var neutral = (steps & CopyQuiet.Faction) != 0 ? ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(NeutralFaction)) as BlueprintFaction : null;
            // The group goes first: UnitGroup.Remove takes the copy's faction out of the old group's faction set, so it must
            // still be the faction the copy joined with (after a switch it logs "Has no item in set" and leaves the party
            // group's set stale). A copy whose faction cannot be switched keeps its group too.
            if ((steps & CopyQuiet.Group) != 0 && ((steps & CopyQuiet.Faction) == 0 || neutral != null))
            {
                copy.GroupId = copy.UniqueId;   // what a non-player unit's group id defaults to
                done |= CopyQuiet.Group;
            }
            if (neutral != null)
            {
                // Also moves the copy's equipment out of the party's shared inventory (UnitDescriptor.SetupInventory).
                copy.Descriptor.SwitchFactions(neutral, true);
                done |= CopyQuiet.Faction;
            }
            if ((steps & CopyQuiet.Silence) != 0
                && ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(SilentAsks)) is BlueprintUnitAsksList silent)
            {
                copy.Descriptor.OverrideAsks = silent;
                copy.View?.UpdateAsks();
                done |= CopyQuiet.Silence;
            }
            if ((steps & CopyQuiet.Passive) != 0)
            {
                copy.Passive.Retain();
                if (copy.IsInCombat) copy.LeaveCombat();
                done |= CopyQuiet.Passive;
            }
            return done;
        }

        internal PresenceObservation Observe(out UnitEntityData? native, out UnitEntityData? copy, out PresenceRecord? record)
        {
            native = copy = null;
            record = null;
            var game = Game.Instance;
            var seen = new PresenceObservation();
            if (game == null || !AreaLoaded(game)) return seen;
            seen.AreaLoaded = true;
            seen.AnchorResolved = ResolveTarget(game);
            record = Read();
            seen.Recorded = record != null;
            seen.RecordedUnhide = record?.Unhidden == true;
            seen.Submitted = record?.Submitted == true;
            var commander = game.Player.MainCharacter.Value;
            string? copyId = record?.UnitId;
            // A blueprint with a PretendUnit component (Seelah_NPC_Level1 -> Seelah_Companion, CR20_EvilArueshalae_NPC ->
            // EvilArueshalae_Companion) reports the pretended blueprint as Blueprint once its facts activate, so our copy and
            // natives are matched by OriginalBlueprint as well (Rules.IsPresenceUnit).
            string blueprintId = Blueprint.AssetGuid.ToString();
            var units = game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>()
                .Where(unit => Rules.IsPresenceUnit(blueprintId, unit.OriginalBlueprint?.AssetGuid.ToString(), unit.Blueprint?.AssetGuid.ToString())
                    && !unit.Destroyed && !unit.DestroyMark && !unit.IsDisposed).ToArray();
            copy = copyId == null ? null : units.FirstOrDefault(unit => unit.UniqueId == copyId);
            seen.CopyFound = copy != null;
            seen.CopyAlive = copy != null && !copy.State.IsDead && !copy.State.IsFinallyDead;
            var natives = units.Where(unit => unit.UniqueId != copyId && !unit.State.IsDead && !unit.State.IsFinallyDead
                && (commander == null || !unit.IsEnemy(commander))).Take(2).ToArray();
            if (natives.Length == 1)
            {
                native = natives[0];
                seen.NativeAlive = true;
                seen.NativeHidden = !native.IsInGame;
                seen.NativeAtPosition = Spec.Position == null && Spec.At == null || !seen.AnchorResolved || (native.Position - Target).sqrMagnitude <= 2.25f;
            }
            return seen;
        }

        // Main thread, idle only. Never throws.
        internal void Tick(bool wanted)
        {
            try
            {
                var seen = Observe(out var native, out var copy, out var record);
                var steps = Rules.PlanPresence(Spec, wanted, seen);
                Actor = !wanted ? null : copy != null && seen.CopyAlive && copy.IsInGame ? copy : native != null && native.IsInGame ? native : null;
                // E12b: an anchored copy that cannot be placed is reported, and exposed as <key>.failed for the letter twin.
                AnchorFailed = wanted && seen.AreaLoaded && Spec.At != null && !seen.AnchorResolved && !seen.CopyFound && !seen.NativeAlive;
                LastQuiet = CopyQuiet.None;
                foreach (var step in steps) Execute(step, native, copy, record);
                // E12d: every live copy (fresh, or spawned by an earlier build) is kept inert; never a native unit.
                if (copy != null && seen.CopyAlive && !steps.Contains(PresenceStep.Remove)) LastQuiet |= Quiet(copy);
                Status = !seen.AreaLoaded ? "area not loaded" : (wanted ? "wanted" : "not wanted")
                    + (seen.NativeAlive ? ", native present" + (seen.NativeHidden ? " (hidden)" : "") : "")
                    + (seen.CopyFound ? ", copy present" : "") + (LastQuiet != CopyQuiet.None ? " (quieted: " + LastQuiet + ")" : "") + (AnchorFailed ? ", anchor not found (not spawned)" : "")
                    + (steps.Length > 0 ? " -> " + string.Join("+", steps) : "");
            }
            catch (Exception ex) { LastError = ex; Status = "error: " + ex.Message; }
        }

        private void Execute(PresenceStep step, UnitEntityData? native, UnitEntityData? copy, PresenceRecord? record)
        {
            var game = Game.Instance;
            switch (step)
            {
                case PresenceStep.Unhide:
                    Write(new PresenceRecord { Key = Key, Unhidden = true });
                    native!.IsInGame = true;
                    break;
                case PresenceStep.Move:
                    native!.Translocate(Target, facing);
                    break;
                case PresenceStep.Hide:
                    native!.IsInGame = false;
                    Write(null);
                    break;
                case PresenceStep.Spawn:
                    // Persist before spawning: an ambiguous submitted record is never spawned twice (TerendelevDelivery pattern).
                    var fresh = new PresenceRecord { Key = Key, UnitId = Guid.NewGuid().ToString(), Submitted = true };
                    Write(fresh);
                    var spawned = game.EntityCreator.SpawnUnit(Blueprint, Target, Quaternion.Euler(0f, facing, 0f),
                        game.State.LoadedAreaState.MainState, fresh.UnitId);
                    // E12d: quiet before the first frame, so the copy never barks or joins a fight as the native unit would.
                    if (spawned != null) LastQuiet = Quiet(spawned);
                    break;
                case PresenceStep.Remove:
                    copy!.IsInGame = false;
                    copy.MarkForDestroy();
                    Write(null);
                    break;
                case PresenceStep.Forget:
                    Write(null);
                    break;
            }
        }

        // For the in-game harness and the UMM log: one line per presence.
        internal string Report(bool wanted) => Key + " [" + Spec.Mode + "] " + (wanted ? "wanted" : "not wanted") + "; " + Status;
    }

    public sealed class PresenceRecord
    {
        public int Version = 1;
        public string Key = "";
        public string? UnitId;
        public bool Submitted;
        public bool Unhidden;

        public bool Valid(string key) => Version == 1 && Key == key && (!Submitted || Guid.TryParse(UnitId, out _));

        public static PresenceRecord? Parse(string json, string key)
        {
            try
            {
                var record = JsonConvert.DeserializeObject<PresenceRecord>(json);
                return record != null && record.Valid(key) ? record : null;
            }
            catch { return null; }
        }
    }
}
