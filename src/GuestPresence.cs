using System;
using System.Collections.Generic;
using System.Linq;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Root;
using Kingmaker.Visual.Sound;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.ElementsSystem;
using Kingmaker.View.Spawners;
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
            Rules.ValidatePresenceCopy(key, spec);
            Key = key;
            Spec = spec;
            Blueprint = blueprint;
        }

        internal string SaveKey => SavePrefix + Key;
        // eng7-l06: separate from actor records, which are discarded when placement stops being wanted.
        internal string FailureSaveKey => Rules.PresenceFailureSaveKey(Key);
        internal bool FailureObserved => Game.Instance.Player.SettingsList.TryGetValue(FailureSaveKey, out var value)
            && value is string text && text == "1";
        // eng7-l06 end

        // A saved actor death is distinct from an unloaded actor or a failed anchor.
        internal bool ReturnedActorLost => Read()?.Lost == true;

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
        internal bool CharacterKilled { get; private set; }
        private readonly PresenceReadiness readiness = new PresenceReadiness();
        private readonly System.Diagnostics.Stopwatch readinessClock = System.Diagnostics.Stopwatch.StartNew();

        private void ObserveReadiness(PresenceObservation seen, UnitEntityData? copy, PresenceRecord? record)
        {
            var game = Game.Instance;
            bool viewPending = copy != null && copy.IsInGame && !copy.Suppressed && copy.State.IsConscious
                && !copy.IsEnemy(game.Player.MainCharacter.Value)
                && NativeContact.HasCurrentStorage(copy, game.State.LoadedAreaState, game.Player.CrossSceneState)
                && copy.HoldingState.IsSceneLoaded && (copy.View == null || !copy.View.gameObject.activeInHierarchy);
            seen.CopyInitializing = readiness.Pending(record?.UnitId, seen, viewPending, readinessClock.Elapsed.TotalSeconds);
        }

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
            Enemy = Game.Instance.Player.MainCharacter.Value != null && copy.IsEnemy(Game.Instance.Player.MainCharacter.Value),
            PartyGroup = copy.GroupId == PartyGroupId,
            ForeignGroup = copy.GroupId != copy.UniqueId,
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
            // group's set stale). Group isolation is still required if the neutral faction is unavailable.
            if ((steps & CopyQuiet.Group) != 0)
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

        // F10: SpawnUnit reuses Current, including a native placeholder's BeforeAttachView callback, hidden
        // optimization and body/inventory. A presence must not inherit any of those. Isolate before attachment;
        // Quiet also repairs foreign groups on copies saved by older builds. No native actor is passed here.
        internal static UnitSpawningData CopySpawningData() => ContextData<UnitSpawningData>.Request()
            .BeforeAttachView(copy => copy.GroupId = copy.UniqueId);

        // F11: State.Units covers only the active area part. Ownership comes exclusively from the saved
        // spawn ID; an off-part native twin with the same blueprint must never become our copy.
        internal static UnitEntityData? ObserveRecordedCopy(string? copyId, IEnumerable<EntityDataBase> areaEntities,
            IEnumerable<UnitEntityData> loadedUnits, PresenceObservation seen)
        {
            var copy = copyId == null ? null : areaEntities.OfType<UnitEntityData>().FirstOrDefault(unit =>
                unit.UniqueId == copyId && !unit.Destroyed && !unit.DestroyMark && !unit.IsDisposed);
            seen.CopyFound = copy != null;
            seen.CopyAlive = copy != null && !copy.State.IsDead && !copy.State.IsFinallyDead;
            seen.CopyOutsideLoadedPart = copy != null && !loadedUnits.Contains(copy);
            seen.CopyUsable = copy != null && !seen.CopyOutsideLoadedPart && NativeContact.Usable(copy);
            return copy;
        }

        // eng7-l05: the uniquely recorded unit is the only copy we may retire.
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
            var units = game.State.Units
                .Where(unit => Rules.IsPresenceUnit(blueprintId, unit.OriginalBlueprint?.AssetGuid.ToString(), unit.Blueprint?.AssetGuid.ToString())
                    && !unit.Destroyed && !unit.DestroyMark && !unit.IsDisposed).ToArray();
            copy = ObserveRecordedCopy(copyId, game.State.LoadedAreaState.AllEntityData, game.State.Units, seen);
            // eng7-l05: living unusable twins stay ambiguous, including actors in unloaded storage.
            var natives = units.Where(unit => unit.UniqueId != copyId && !NativeContact.Ignorable(unit)).ToArray();
            seen.NativeCount = natives.Length;
            seen.RecordedNative = record?.NativeUnitId != null;
            seen.RecordedNativeContact = record?.NativeContactId != null; // eng7-l05
            string? nativeId = record?.NativeUnitId; // out parameters cannot be captured by the actor query
            native = seen.RecordedNative ? natives.FirstOrDefault(unit => unit.UniqueId == nativeId)
                : natives.Length == 1 ? natives[0] : null;
            seen.ContactAmbiguous = Rules.SingleUsable(units, actor => NativeContact.Usable(actor), NativeContact.Ignorable) == null
                && units.Any(actor => NativeContact.Usable(actor));
            if (native != null)
            {
                // A primary and its fallback can share a blueprint. The fallback's saved copy is not a native return:
                // accepting it would clear primary.failed and retire the fallback on the following tick.
                string observedNativeId = native.UniqueId;
                seen.NativeOwnedCopy = game.Player.SettingsList.Any(pair => pair.Key != SaveKey
                    && pair.Key.StartsWith(SavePrefix, StringComparison.Ordinal) && pair.Value is string json
                    && PresenceRecord.Parse(json, pair.Key.Substring(SavePrefix.Length))?.UnitId == observedNativeId);
                seen.NativeAlive = commander != null && !native.IsEnemy(commander);
                seen.NativeUsable = NativeContact.Usable(native);
                seen.NativeManageable = NativeContact.Usable(native, allowHidden: true);
                seen.NativeHidden = !native.IsInGame;
                seen.NativeAtPosition = Spec.Position == null && Spec.At == null || seen.AnchorResolved && (native.Position - Target).sqrMagnitude <= 2.25f; // eng7-l05
            }
            return seen;
        }

        // Main thread, idle only. Never throws.
        internal void Tick(bool wanted, Story? receiptStory = null, Snapshot? receiptState = null)  // eng7-l06
        {
            CharacterKilled = false;
            bool demanded = wanted; // eng7-l05: retain accurate demand even if observation throws.
            try
            {
                LastError = null; // eng7-l05
                // eng7-l05: a presence that forbids its own failure must still observe demand. Otherwise the
                // primary clears the flag on its next tick and oscillates with its earned alternate placement.
                if (!wanted && Spec.Forbids.Contains(Rules.PresenceFailedFlag(Key)))
                {
                    var state = Main.State();
                    demanded = !state.Has(Rules.DegradedPrefix + Rules.PresenceRelationship(Key))
                        && Rules.PresenceWanted(Spec, state, Rules.PresenceFailedFlag(Key));
                }
                var priorActor = Actor;
                var seen = Observe(out var native, out var copy, out var record);
                // Only a route-owned copy or a previously delivered native contact is a death witness.
                // Missing, hidden, disposed and ambiguous actors remain availability observations.
                seen.NativeKilled = Key == "kiana.presence" && seen.AreaLoaded
                    && Game.Instance.State.LoadedAreaState.AllEntityData.OfType<UnitEntityData>().Any(unit =>
                        (unit == priorActor || record != null && (unit.UniqueId == record.NativeUnitId
                            || unit.UniqueId == record.NativeContactId))
                        && !unit.Destroyed && !unit.DestroyMark && !unit.IsDisposed
                        && (unit.State.IsDead || unit.State.IsFinallyDead));
                CharacterKilled = Key == "kiana.presence" && Rules.PresenceKilled(seen);
                if (record != null && seen.AreaLoaded && (seen.CopyFound && !seen.CopyAlive
                    || Game.Instance.State.Units.Any(unit =>
                        (unit.UniqueId == record.NativeUnitId || unit.UniqueId == record.NativeContactId)
                        && (unit.State.IsDead || unit.State.IsFinallyDead))))
                { record.Lost = true; Write(record); }
                if (CharacterKilled) { Actor = null; AnchorFailed = false; Status = "character killed"; return; }
                LastQuiet = CopyQuiet.None;
                // Repair an older recorded copy before failure/receipt observation (hostile blueprint copies included).
                if (copy != null && seen.CopyAlive)
                {
                    LastQuiet = Quiet(copy);
                    if (LastQuiet != CopyQuiet.None) seen = Observe(out native, out copy, out record);
                }
                ObserveReadiness(seen, copy, record);
                // Own-failure gates select the fallback; they must not destroy the demanded primary and clear failure.
                var steps = Rules.PlanPresence(Spec, demanded, seen);
                Actor = null; // eng7-l05: publish only the post-transition usable contact.
                // E12b: a wanted presence that cannot be placed (an anchored copy without its anchor, or a reuse-native
                // presence without a usable native actor) is reported, and exposed as <key>.failed for the letter twin.
                AnchorFailed = Rules.PresenceFailed(Spec, demanded, seen);
                // eng7-l06: the completed snapshot supplies earned prerequisites; this tick supplies real observation.
                if (wanted && receiptStory != null && receiptState != null
                    && Rules.RecordPresenceFailure(receiptStory, Key, receiptState, seen))
                    Game.Instance.Player.SettingsList[FailureSaveKey] = "1";
                // eng7-l06 end
                foreach (var step in steps) Execute(step, native, copy, record);
                // E12d: every live copy (fresh, or spawned by an earlier build) is kept inert; never a native unit.
                if (copy != null && seen.CopyAlive && !steps.Contains(PresenceStep.Remove)) LastQuiet |= Quiet(copy);
                // eng7-l05: no stale actor/failure between a spawn, unhide, retirement and hub attachment.
                seen = Observe(out native, out copy, out record);
                ObserveReadiness(seen, copy, record);
                AnchorFailed = Rules.PresenceFailed(Spec, demanded, seen);
                if (wanted && !AnchorFailed)
                {
                    var candidates = Game.Instance.State.Units.Where(unit => Rules.IsPresenceUnit(Spec.Unit,
                        unit.OriginalBlueprint?.AssetGuid.ToString(), unit.Blueprint?.AssetGuid.ToString()));
                    Actor = Rules.SingleUsable(candidates, unit => NativeContact.Usable(unit), NativeContact.Ignorable);
                }
                Status = !seen.AreaLoaded ? "area not loaded" : (wanted ? "wanted" : "not wanted")
                    + (seen.NativeAlive ? ", native present" + (seen.NativeHidden ? " (hidden)" : "") : "")
                    + (seen.CopyFound ? ", copy present" : "") + (LastQuiet != CopyQuiet.None ? " (quieted: " + LastQuiet + ")" : "") + (AnchorFailed ? ", not placed (failed)" : "")
                    + (steps.Length > 0 ? " -> " + string.Join("+", steps) : "");
            }
            catch (Exception ex) { Actor = null; AnchorFailed = demanded; LastError = ex; Status = "error: " + ex.Message; } // eng7-l05
        }

        private void Execute(PresenceStep step, UnitEntityData? native, UnitEntityData? copy, PresenceRecord? record)
        {
            var game = Game.Instance;
            switch (step)
            {
                // eng7-l05: persist native ownership and its pre-placement state before touching it.
                case PresenceStep.RecordNativeContact:
                    Write(new PresenceRecord { Key = Key, NativeContactId = native!.UniqueId });
                    break;
                case PresenceStep.Adopt:
                    Write(new PresenceRecord { Key = Key, NativeUnitId = native!.UniqueId,
                        NativeWasInGame = native.IsInGame, NativePosition = new PresencePosition {
                            X = native.Position.x, Y = native.Position.y, Z = native.Position.z, Orientation = native.Orientation } });
                    break;
                case PresenceStep.RestoreNative:
                    var prior = record!.NativePosition!;
                    native!.Translocate(new Vector3(prior.X, prior.Y, prior.Z), prior.Orientation);
                    native.IsInGame = record.NativeWasInGame;
                    Write(null);
                    break;
                case PresenceStep.Unhide:
                    if (Read()?.NativeUnitId == null) Write(new PresenceRecord { Key = Key, Unhidden = true });
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
                    UnitEntityData? spawned;
                    using (CopySpawningData())
                        spawned = game.EntityCreator.SpawnUnit(Blueprint, Target, Quaternion.Euler(0f, facing, 0f),
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
        public bool Lost; // eng7-integ: additive v1 receipt for the recorded copy's subsequent death.
        public bool Unhidden;
        // eng7-l05: additive v1 save fields; old copy/unhide records retain their meaning.
        public string? NativeUnitId;
        public string? NativeContactId; // eng7-l05: no native state was changed by copy retirement.
        public bool NativeWasInGame;
        public PresencePosition? NativePosition;

        public bool Valid(string key) => Version == 1 && Key == key && (!Submitted || Guid.TryParse(UnitId, out _))
            && (NativeContactId == null || !Submitted && !string.IsNullOrWhiteSpace(NativeContactId))
            && (NativeUnitId == null || !Submitted && !string.IsNullOrWhiteSpace(NativeUnitId) && NativePosition != null); // eng7-l05

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
