using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
#if !RRT_RULES_TESTS
using HarmonyLib;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;
using Kingmaker.View;
using UnityEngine;
#endif

namespace Tirabade
{
    // Portable visibility ownership, exercised by the offline rules suite and used by the native adapter.
    public sealed class NativeVisibilityLease<T> where T : class
    {
        private sealed class Identity : IEqualityComparer<T>
        {
            public bool Equals(T? a, T? b) => ReferenceEquals(a, b);
            public int GetHashCode(T value) => System.Runtime.CompilerServices.RuntimeHelpers.GetHashCode(value);
        }
        private readonly Dictionary<T, bool> original = new Dictionary<T, bool>(new Identity());
        private object? owner;
        public void Reset(object? nextOwner)
        {
            if (ReferenceEquals(owner, nextOwner)) return;
            // Old-save entities belong to their old owner; never restore them into a new run.
            original.Clear(); owner = nextOwner;
        }
        public void Hide(T entity, Func<T, bool> read, Action<T, bool> write)
        {
            if (!original.ContainsKey(entity)) original[entity] = read(entity);
            if (read(entity)) write(entity, false);
        }
        public void ReleaseExcept(IEnumerable<T> wanted, Action<T, bool> write, Action<Exception> failed)
        {
            var keep = new HashSet<T>(wanted, new Identity());
            foreach (var entity in original.Keys.Where(e => !keep.Contains(e)).ToArray())
            {
                try { write(entity, original[entity]); original.Remove(entity); }
                catch (Exception ex) { failed(ex); } // Retain ownership so the next tick can retry.
            }
        }
    }

#if !RRT_RULES_TESTS
    // eng7-l04: authored Trickster reconciliation. All identities come from blueprints.zip;
    // only the nominated actions/fields are wrapped. No quest status, XP, death or romance etude changes.
    public sealed class NativeWorldReconciliation
    {
        public const string Burial = "a6e26159152a54c47a70ec91495499cf";
        public const string Prison = "0544675ba14e81e48bb0965823c33efe";
        public const string Escape = "067bd492b3a377d4e9112d929ec62fdb";
        public const string BurialArea = "72672fb14139b1443a6700473cce04d7";
        public const string BurialScene = "42332f3087ee8e34b8fd90aa34d64614";
        public const string PrisonScene = "1c9b1a8d692860647848123dc61f3baa";
        public const string Prisoner = "9bf297f2-559f-4823-8471-c9761999538a";
        public static readonly string[] CorpseIds = {
            "36388267-9dfb-410c-ac7c-e6a96538ce7b", // Regnard (DeadRegnard)
            "8ea39933-3fd6-43fa-9d82-b1dbe03ccadf", // Taeriell (TaerilCorpse)
            "6cacdba8-376e-41ff-9728-5eeff69e5021", // Vestari
            "61dd594e-2a0e-47f5-86b5-937dccccce52", // Cristry
        };
        private readonly Story story;
        private readonly Func<Snapshot?> observe;
        private readonly Action<string> warn;
        private readonly List<HideMapObject> corpses = new List<HideMapObject>();
        private readonly List<(LocalizedString Field, string Target, bool Title)> journals = new List<(LocalizedString, string, bool)>();
        // Lease loaded views only. Never persist a mod-only IsInGame bit into a native actor/object's save state.
        private readonly NativeVisibilityLease<GameObject> visibility = new NativeVisibilityLease<GameObject>();
        private UnitFromSpawner? prisoner;
        private static NativeWorldReconciliation? installed;
        private const BindingFlags Fields = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        private static object? Field(object value, string field) => value.GetType().GetField(field, Fields)?.GetValue(value);
        private static bool Entity(EntityReference? value, string id, string scene) => value != null && value.UniqueId == id && value.SceneAssetGuid == scene;
        private static IEnumerable<(ActionList List, int Index, HideMapObject Action)> Hides(ActionList list)
        {
            for (int i = 0; i < list.Actions.Length; i++)
            {
                if (list.Actions[i] is HideMapObject hide) yield return (list, i, hide);
                if (list.Actions[i] is WorldBranch branch && branch.Original is HideMapObject original) yield return (list, i, original);
                if (list.Actions[i] is Conditional conditional)
                    foreach (var row in Hides(conditional.IfTrue).Concat(Hides(conditional.IfFalse))) yield return row;
            }
        }
        private bool Holds(string target)
        {
            try { var state = observe(); return state != null && (target != Burial || state.Area == BurialArea)
                    && Rules.NativeWorldHolds(story, target, state); }
            catch (Exception ex) { warn("Native world observation failed: " + ex.Message); return false; }
        }
        public NativeWorldReconciliation(Story story, Func<Snapshot?> observe, Func<string, SimpleBlueprint?> resolve, Action<string> warn)
        {
            this.story = story; this.observe = observe; this.warn = warn;
            installed?.visibility.Reset(Game.Instance?.Player);
            installed?.visibility.ReleaseExcept(Array.Empty<GameObject>(), SetView,
                ex => warn("Native visibility release failed: " + ex.Message));
            foreach (var pair in story.NativeWorldReconciliations)
            {
                // Validate the complete target before any mutation of that target. Refusal leaves canon intact.
                try { Install(pair.Key, pair.Value, resolve); }
                catch (Exception ex) { warn("Native reconciliation " + pair.Key + " skipped (canon retained): " + ex.Message); }
            }
            installed = this;
        }
        private void Install(string target, NativeWorldSpec spec, Func<string, SimpleBlueprint?> resolve)
        {
            if (!Rules.ReviewedNativeWorldTargets.ContainsKey(target) || target != spec.Target) throw new InvalidOperationException("unreviewed target");
            var owner = resolve(target) as BlueprintScriptableObject ?? throw new InvalidOperationException("missing native target");
            if (target == Burial)
            {
                if (!(owner is BlueprintEtude etude) || (Field(etude, "m_LinkedAreaPart") as BlueprintReferenceBase)?.Guid.ToString() != BurialArea)
                    throw new InvalidOperationException("Pulura area differs from reviewed evidence");
                var rows = etude.ComponentsArray.OfType<EtudePlayTrigger>().SelectMany(t => Hides(t.Actions))
                    .Where(r => r.Action.MapObject is MapObjectFromScene map && CorpseIds.Contains(map.MapObject.UniqueId)).ToArray();
                if (rows.Length != 4 || rows.Select(r => ((MapObjectFromScene)r.Action.MapObject).MapObject.UniqueId).Distinct().Count() != 4
                    || rows.Any(r => !r.Action.Unhide || ((MapObjectFromScene)r.Action.MapObject).MapObject.SceneAssetGuid != BurialScene))
                    throw new InvalidOperationException("four corpse displays differ from reviewed evidence");
                foreach (var row in rows)
                {
                    if (row.List.Actions[row.Index] is WorldBranch existing)
                    {
                        existing.Holds = () => Holds(target);
                        existing.OnEarned = () => HideDisplay((HideMapObject)existing.Earned);
                        corpses.Add((HideMapObject)existing.Earned);
                        continue;
                    }
                    var hide = new HideMapObject { MapObject = row.Action.MapObject, Unhide = false, Owner = owner, name = "$Buried$" + Guid.NewGuid() };
                    var branch = new WorldBranch { Original = row.Action, Earned = hide, Holds = () => Holds(target),
                        OnEarned = () => HideDisplay(hide), Owner = owner, name = "$Burial$" + Guid.NewGuid() };
                    owner.ElementsArray.Add(hide); owner.ElementsArray.Add(branch);
                    row.List.Actions[row.Index] = branch;
                    corpses.Add(hide);
                }
                return;
            }
            if (target == Prison)
            {
                if (!(owner is BlueprintEtude etude)) throw new InvalidOperationException("prison etude missing");
                var triggers = etude.ComponentsArray.OfType<EtudePlayTrigger>().Where(t => t.Actions.Actions.OfType<Spawn>()
                    .Any(s => s.Spawners.Any(e => Entity(e, Prisoner, PrisonScene)))).ToArray();
                if (triggers.Length != 1) throw new InvalidOperationException("prisoner spawn is no longer unique");
                var trigger = triggers[0];
                var actions = trigger.Actions.Actions;
                var checker = OriginalChecker(trigger.Conditions);
                if (checker.Operation != Operation.And || checker.Conditions.Length != 1
                    || !(checker.Conditions[0] is EtudeStatus)
                    || NativeQ3Recovery.Shape(new ActionList { Actions = new GameAction[] { new Conditional {
                        ConditionsChecker = checker, IfTrue = new ActionList { Actions = Array.Empty<GameAction>() },
                        IfFalse = new ActionList { Actions = Array.Empty<GameAction>() } } } })
                        != "C:And[E:eff0ca2318f96c049b5c9e6785eac196:False:False:False:True:False:False]{}{}"
                    || actions.Length != 2 || !(actions[0] is Spawn spawn) || spawn.Spawners.Length != 1
                    || !Entity(spawn.Spawners[0], Prisoner, PrisonScene) || spawn.ActionsOnSpawn.Actions.Length != 0
                    || !Equals(Field(spawn, "RespawnIfDead"), false) || actions[1].GetType().Name != "ScriptZoneActivate"
                    || !Equals(Field(actions[1], "UseEvaluator"), false) || Field(actions[1], "ScriptZoneEvaluator") != null
                    || !Entity(Field(actions[1], "ScriptZone") as EntityReference, "b8efebdc-2c24-40e6-b189-04fc39ad52a8", PrisonScene))
                    throw new InvalidOperationException("prison spawn/activation differs from reviewed evidence");
                NativeGate.Attach(owner, trigger.Conditions, () => Holds(target));
                prisoner = new UnitFromSpawner { Spawner = spawn.Spawners[0], Owner = owner };
                return;
            }
            if (target == Escape)
            {
                if (!(owner is BlueprintScriptZone zone) || OriginalChecker(zone.TriggerConditions).Operation != Operation.And || OriginalChecker(zone.TriggerConditions).Conditions.Length != 0
                    || NativeQ3Recovery.Shape(zone.EnterActions) != "PlayCutscene:ee638b3fc29d95848aee5bdb74821aaf:False:True:0"
                    || zone.ExitActions.Actions.Length != 0)
                    throw new InvalidOperationException("prison escape sequence differs from reviewed evidence");
                NativeGate.Attach(owner, zone.TriggerConditions, () => Holds(target));
                return;
            }
            // Localization is selected when read, even before quest start. No global localization-pack mutation.
            var description = Field(owner, "Description") as LocalizedString;
            var title = Field(owner, "Title") as LocalizedString;
            if (owner.GetType().Name != (target == "5a5a533c9ce630a48b877f9a194840cb" ? "BlueprintQuest" : "BlueprintQuestObjective")
                || description == null || description.Key != spec.DescriptionKey
                || spec.TitleKey.Length > 0 && (title == null || title.Key != spec.TitleKey))
                throw new InvalidOperationException("journal type/localization differs from reviewed evidence");
            journals.Add((description, target, false));
            if (spec.TitleKey.Length > 0) journals.Add((title!, target, true));
        }
        private static ConditionsChecker OriginalChecker(ConditionsChecker checker) => checker.Conditions.Length == 1
            && checker.Conditions[0] is NativeGate.Guard guard ? guard.Original! : checker;
        private static void SetView(GameObject view, bool visible)
        {
            if (view == null) return;
            // A native hide/departure that occurred during the lease still stands when we release it.
            var entityView = view.GetComponent<EntityViewBase>();
            view.SetActive(visible && (entityView?.Data?.IsInGame ?? true));
        }
        private void HideDisplay(HideMapObject hide)
        {
            visibility.Reset(Game.Instance?.Player);
            var view = hide.MapObject.GetValue()?.View;
            if (view != null && view.gameObject.scene.isLoaded)
                visibility.Hide(view.gameObject, v => v.activeSelf, SetView);
        }
        // Only loaded identities are leased. Reloads use fresh observations; native hidden objects remain hidden on release.
        public void Tick()
        {
            var current = Game.Instance?.Player;
            visibility.Reset(current);
            Snapshot? state = null;
            try { state = observe(); } catch (Exception ex) { warn("Native world tick observation failed: " + ex.Message); }
            var wanted = new HashSet<GameObject>();
            if (state != null && state.Area == BurialArea && Rules.NativeWorldHolds(story, Burial, state))
                foreach (var hide in corpses)
                {
                    try
                    {
                        var view = hide.MapObject.GetValue()?.View;
                        if (view != null && view.gameObject.scene.isLoaded)
                        { visibility.Hide(view.gameObject, v => v.activeSelf, SetView); wanted.Add(view.gameObject); }
                    }
                    catch (Exception ex) { warn("Burial display observation failed: " + ex.Message); }
                }
            if (state != null && Rules.NativeWorldHolds(story, Prison, state) && prisoner != null)
            {
                try
                {
                    var actor = prisoner.GetValue();
                    if (actor != null && actor.View != null && actor.View.gameObject.scene.isLoaded
                        && !actor.State.IsDead && !actor.State.IsFinallyDead
                        && actor.HoldingState != null && actor.HoldingState.AllEntityData.Contains(actor)
                        && actor.HoldingState.IsSceneLoaded && Game.Instance?.State?.LoadedAreaState != null
                        && Game.Instance.State.LoadedAreaState.GetAllSceneStates().Contains(actor.HoldingState))
                    { visibility.Hide(actor.View.gameObject, v => v.activeSelf, SetView); wanted.Add(actor.View.gameObject); }
                }
                catch (Exception ex) { warn("Prisoner observation failed: " + ex.Message); }
            }
            visibility.ReleaseExcept(wanted, SetView, ex => warn("Native visibility release failed: " + ex.Message));
        }
        internal string? JournalText(LocalizedString field)
        {
            var row = journals.SingleOrDefault(r => ReferenceEquals(r.Field, field));
            if (row.Field == null) return null;
            try { var state = observe(); return state == null ? null : Rules.NativeJournalText(story, row.Target, row.Title, state); }
            catch (Exception ex) { warn("Journal observation failed: " + ex.Message); return null; }
        }
        public sealed class WorldBranch : GameAction
        {
            public GameAction Original = null!, Earned = null!;
            public Func<bool> Holds = null!;
            public Action OnEarned = null!;
            public Exception? LastObservationError { get; private set; }
            public GameAction Selected()
            {
                LastObservationError = null;
                try { return Holds() ? Earned : Original; }
                catch (Exception ex) { LastObservationError = ex; return Original; }
            }
            public override string GetCaption() => "Corpse display after completed burial";
            public override void RunAction()
            {
                var selected = Selected();
                if (ReferenceEquals(selected, Earned))
                {
                    // Keep the native saved visibility; the earned display is a reversible view suppression.
                    try { new ActionList { Actions = new[] { Original } }.Run(); OnEarned(); return; }
                    catch (Exception ex) { LastObservationError = ex; selected = Original; }
                }
                new ActionList { Actions = new[] { selected } }.Run();
            }
        }
        [HarmonyPatch(typeof(LocalizedString), "LoadString")]
        private static class JournalPatch
        {
            private static bool Prefix(LocalizedString __instance, ref string __result)
            {
                var text = installed?.JournalText(__instance);
                if (text == null) return true;
                __result = text; return false;
            }
        }
    }
#endif
}
