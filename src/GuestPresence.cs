using System;
using System.Linq;
using Kingmaker;
using Kingmaker.Blueprints;
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

        private Vector3 Target => new Vector3(Spec.Position!.X, Spec.Position.Y, Spec.Position.Z);

        internal PresenceObservation Observe(out UnitEntityData? native, out UnitEntityData? copy, out PresenceRecord? record)
        {
            native = copy = null;
            record = null;
            var game = Game.Instance;
            var seen = new PresenceObservation();
            if (game == null || !AreaLoaded(game)) return seen;
            seen.AreaLoaded = true;
            record = Read();
            seen.Recorded = record != null;
            seen.RecordedUnhide = record?.Unhidden == true;
            seen.Submitted = record?.Submitted == true;
            var commander = game.Player.MainCharacter.Value;
            string? copyId = record?.UnitId;
            var units = game.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>()
                .Where(unit => unit.Blueprint == Blueprint && !unit.Destroyed && !unit.DestroyMark && !unit.IsDisposed).ToArray();
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
                seen.NativeAtPosition = Spec.Position == null || (native.Position - Target).sqrMagnitude <= 2.25f;
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
                foreach (var step in steps) Execute(step, native, copy, record);
                Status = !seen.AreaLoaded ? "area not loaded" : (wanted ? "wanted" : "not wanted")
                    + (seen.NativeAlive ? ", native present" + (seen.NativeHidden ? " (hidden)" : "") : "")
                    + (seen.CopyFound ? ", copy present" : "") + (steps.Length > 0 ? " -> " + string.Join("+", steps) : "");
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
                    native!.Translocate(Target, Spec.Position!.Orientation);
                    break;
                case PresenceStep.Hide:
                    native!.IsInGame = false;
                    Write(null);
                    break;
                case PresenceStep.Spawn:
                    // Persist before spawning: an ambiguous submitted record is never spawned twice (TerendelevDelivery pattern).
                    var fresh = new PresenceRecord { Key = Key, UnitId = Guid.NewGuid().ToString(), Submitted = true };
                    Write(fresh);
                    game.EntityCreator.SpawnUnit(Blueprint, Target, Quaternion.Euler(0f, Spec.Position!.Orientation, 0f),
                        game.State.LoadedAreaState.MainState, fresh.UnitId);
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
