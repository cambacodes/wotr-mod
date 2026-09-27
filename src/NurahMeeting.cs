using System;
using System.Linq;
using System.Collections.Generic;
using HarmonyLib;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Conditions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.Designers.EventConditionActionSystem.NamedParameters;
using Kingmaker.ElementsSystem;
using Kingmaker.PubSubSystem;
using Newtonsoft.Json;
using UnityEngine;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.View.Spawners;

namespace Tirabade
{
    // A voluntary private visit of retained living Nurah, without actor creation or native history writes.
    internal sealed class NurahMeeting
    {
        internal const string Capital = Rules.NurahCapital;
        internal const string SceneAsset = "3e2b5ea054cd5b2479e7f13134363ef4";
        internal const string Spawner = "c2b298fc-d794-4995-8b49-822b75c3bb62";
        internal const string Unit = Rules.NurahContact;
        internal const string Group = "d0210e61193c8c746bc33bf7d1fff325";
        internal const string Hidden = "245524f91e743b64eaa16445c3ea8e73";
        internal const string Prison = "c922e0cbe25a0cf4dad4ce7a3ca81935";
        internal const string Romance = "9f655e252d334f04884f10188b0d8928";
        internal const string Finale = "f8a7511233524742bc42b25190609f4c";
        internal static readonly string[] Deaths = { "a837c3bc9cbb4e846ab5565915165c91",
            "20927a9471c00814b808fd69e88879c7", "739b9fe9b8998c641b4b3dfed40bc217" };
        internal static readonly string[] Personalities = { "91f7abac0d8e46e19ce8fc45fa3df58e",
            "f74eaab69b3d49d0a222eb1b2834777e", "3d2d02611cd24f579e7b7b411b94263e" };
        private static readonly JerribethRecovery.Source source = new JerribethRecovery.Source(
            Capital, "DrezenCapital_Default_Mechanics", Spawner, Unit);
        private readonly BlueprintEtude romance, prison;
        private readonly BlueprintEtude[] deaths, personalities;
        private readonly BlueprintCue finale;
        internal Exception? LastError { get; private set; }
        internal const string CapitalKtc = "10d01be767521a340978c8e57ab536b6";
        internal const string VisitorCommand = "0971481f9a68c8547a4d7cb0c086b311";
        internal const string Locator = "7b94948a-1954-428f-82d0-94b2adcb1380";
        internal const string HiddenParent = "ce5f755519ff2c945ab4eacd67d3f8e3";
        internal readonly BlueprintEtude Blueprint = null!;
        private readonly Func<string?> acceptedRequest = () => null;
        private readonly BlueprintEtude hidden = null!;
        private readonly BlueprintEtudeConflictingGroup group = null!, capitalKtc = null!;
        private readonly HideUnit show = null!;
        private readonly TranslocateUnit move = null!;
        private readonly LocatorPosition position = null!;
        private readonly LocatorOrientation orientation = null!;


        internal NurahMeeting(Func<string, SimpleBlueprint> resolve)
        {
            T Get<T>(string id) where T : SimpleBlueprint
            {
                var value = resolve(id);
                if (!(value is T typed) || typed.AssetGuid.ToString() != id)
                    throw new InvalidOperationException("Nurah native binding differs: " + id);
                return typed;
            }
            romance = Get<BlueprintEtude>(Romance);
            prison = Get<BlueprintEtude>(Prison);
            deaths = Deaths.Select(Get<BlueprintEtude>).ToArray();
            personalities = Personalities.Select(Get<BlueprintEtude>).ToArray();
            finale = Get<BlueprintCue>(Finale);
        }

        // Raw saved invitation callback only; it must never call Main.State.
        internal NurahMeeting(BlueprintEtude blueprint, Func<string?> acceptedRequest,
            Func<string, SimpleBlueprint> resolve) : this(resolve)
        {
            this.acceptedRequest = acceptedRequest ?? throw new ArgumentNullException(nameof(acceptedRequest));
            hidden = (BlueprintEtude)resolve(Hidden);
            group = (BlueprintEtudeConflictingGroup)resolve(Group);
            capitalKtc = (BlueprintEtudeConflictingGroup)resolve(CapitalKtc);
            ValidateHidden(hidden);
            ValidateVisitorCommand((CommandAction)resolve(VisitorCommand));
            if (group.AssetGuid.ToString() != Group || capitalKtc.AssetGuid.ToString() != CapitalKtc
                || resolve(Capital).AssetGuid.ToString() != Capital || new[] { hidden, hidden.Parent.Get(), romance, prison }.Concat(deaths).Concat(personalities)
                    .Any(native => native != null && blueprint.AssetGuid == native.AssetGuid))
                throw new InvalidOperationException("Nurah meeting binding differs from its authored/native contract.");
            Blueprint = blueprint;
            var unit = new UnitFromSpawner { Spawner = Entity(Spawner), Owner = blueprint };
            position = new LocatorPosition { Locator = Entity(Locator), Owner = blueprint };
            orientation = new LocatorOrientation { Locator = Entity(Locator), Owner = blueprint };
            show = new HideUnit { Target = unit, Unhide = true, Owner = blueprint };
            move = new TranslocateUnit { Unit = unit, translocatePosition = Entity(Locator), Owner = blueprint };
            Field(move, "m_CopyRotation", true);
            blueprint.Priority = -90;
            blueprint.ActivationCondition = new ConditionsChecker { Conditions = new Condition[] { new Eligibility { Meeting = this } } };
            blueprint.CompletionCondition = new ConditionsChecker { Conditions = new Condition[] { new NeverComplete() } };
            Field(blueprint, "m_AllowActionStart", true);
            Field(blueprint, "m_Parent", new BlueprintEtudeReference());
            Field(blueprint, "m_StartsParent", false);
            Field(blueprint, "m_CompletesParent", false);
            Field(blueprint, "m_LinkedAreaPart", Reference<BlueprintAreaPartReference>((BlueprintAreaPart)resolve(Capital)));
            Field(blueprint, "m_ConflictingGroups", new List<BlueprintEtudeConflictingGroupReference> { Reference<BlueprintEtudeConflictingGroupReference>(group) });
            blueprint.ComponentsArray = new BlueprintComponent[] { new Placement { name = "RRT_NurahMeetingPlacement", Meeting = this } };
        }

        private static void Field(object target, string name, object value) => AccessTools.Field(target.GetType(), name).SetValue(target, value);
        private static T Reference<T>(SimpleBlueprint blueprint) where T : BlueprintReferenceBase, new()
        {
            var reference = new T();
            Field(reference, "deserializedGuid", blueprint.AssetGuid);
            Field(reference, "<Cached>k__BackingField", blueprint);
            return reference;
        }
        private static EntityReference Entity(string id) => new EntityReference { UniqueId = id, SceneAssetGuid = SceneAsset };
        private static bool ExactEntity(EntityReference entity, string id) => entity.UniqueId == id && entity.SceneAssetGuid == SceneAsset;
        private static bool EmptyAnd(ConditionsChecker checker) => checker.Operation == Operation.And && checker.Conditions.Length == 0;

        internal static void ValidateHidden(BlueprintEtude blueprint)
        {
            var triggers = blueprint.ComponentsArray.OfType<EtudePlayTrigger>().ToArray();
            var groups = blueprint.ConflictingGroups.Select(item => item.Get()).ToArray();
            if (blueprint.AssetGuid.ToString() != Hidden || blueprint.Priority != -100
                || blueprint.Parent.Get()?.AssetGuid.ToString() != HiddenParent
                || !EmptyAnd(blueprint.ActivationCondition) || !EmptyAnd(blueprint.CompletionCondition)
                || groups.Length != 1 || groups[0]?.AssetGuid.ToString() != Group
                || blueprint.ComponentsArray.Length != 1 || triggers.Length != 1)
                throw new InvalidOperationException("Unreviewed Nurah hidden fallback.");
            var trigger = triggers[0];
            if ((bool)AccessTools.Field(typeof(EtudePlayTrigger), "m_Once").GetValue(trigger)
                || trigger.Actions.Actions.Length != 1 || !(trigger.Actions.Actions[0] is HideUnit hide)
                || hide.Unhide || hide.Fade || hide.SetHideInSaves
                || !(hide.Target is UnitFromSpawner unit) || !ExactEntity(unit.Spawner, Spawner)
                || trigger.Conditions.Operation != Operation.And || trigger.Conditions.Conditions.Length != 1
                || !(trigger.Conditions.Conditions[0] is OrAndLogic logic) || !logic.Not
                || logic.ConditionsChecker.Operation != Operation.Or || logic.ConditionsChecker.Conditions.Length != 1
                || !(logic.ConditionsChecker.Conditions[0] is EtudeStatus death) || death.Not
                || death.Etude?.AssetGuid.ToString() != Deaths[0] || !death.Playing
                || death.Started || death.Completed || death.NotStarted || death.CompletionInProgress)
                throw new InvalidOperationException("Nurah hidden action/condition differs from native evidence.");
        }

        internal static void ValidateVisitorCommand(CommandAction command)
        {
            if (command.AssetGuid.ToString() != VisitorCommand || !EmptyAnd(command.EntryCondition)
                || command.Action.Actions.Length != 2 || !(command.Action.Actions[0] is HideUnit hide)
                || !hide.Unhide || hide.Fade || hide.SetHideInSaves
                || !(hide.Target is NamedParameterUnit shown) || shown.Parameter != "Unit"
                || !(command.Action.Actions[1] is TranslocateUnit moved)
                || !(moved.Unit is NamedParameterUnit target) || target.Parameter != "Unit"
                || !ExactEntity(moved.translocatePosition, Locator) || moved.translocatePositionEvaluator != null
                || moved.translocateOrientationEvaluator != null
                || !(bool)AccessTools.Field(typeof(TranslocateUnit), "m_CopyRotation").GetValue(moved))
                throw new InvalidOperationException("Native private visitor placement differs from reviewed evidence.");
        }

        internal bool CorrespondenceAvailable()
        {
            try
            {
                var game = Game.Instance;
                if (game?.Player == null) return false;
                var actor = RetainedActor();
                if (actor == null) return false;
                var data = Blueprint == null ? null : SavedData(game.Player.EtudesSystem.Etudes.GetFact(Blueprint));
                if (data?.ActorId != null && data.ActorId != actor.UniqueId) return false;
                var system = game.Player.EtudesSystem;
                return HistoryPermits(system.Etudes.GetFact(romance),
                    PrisonBlocks(system, prison),
                    deaths.Any(etude => system.EtudeIsStarted(etude) || system.EtudeIsCompleted(etude)),
                    personalities.Select(etude => system.Etudes.GetFact(etude)).ToArray(),
                    game.Player.Dialog.ShownCues.Contains(finale));
            }
            catch (Exception ex) { LastError = ex; return false; }
        }

        // Native saved completion is published before the fact finishes deactivating.
        internal static bool PrisonBlocks(EtudesSystem system, BlueprintEtude prison)
        {
            var fact = system.Etudes.GetFact(prison);
            return fact != null && (!fact.IsCompleted || fact.IsPlaying || fact.CompletionInProgress)
                || system.EtudeIsStarted(prison) && !system.EtudeIsCompleted(prison);
        }

        // Historical imprisonment may be complete after release; current imprisonment still blocks.
        internal static bool HistoryPermits(Etude? romance, bool imprisoned, bool deathHistory,
            Etude?[] personalities, bool finaleSeen)
            => finaleSeen && romance != null && romance.IsPlaying && !romance.IsCompleted && !romance.CompletionInProgress
                && !imprisoned && !deathHistory
                && personalities.Length == 3 && personalities.Count(fact => fact != null && fact.IsPlaying
                    && !fact.IsCompleted && !fact.CompletionInProgress) == 1;

        internal static UnitEntityData? Inspect(string area, SceneEntitiesState[] states,
            Func<SceneEntitiesState, bool> loaded, Func<string, EntityDataBase?> lookup)
        {
            var observed = JerribethRecovery.Inspect(source, area, states, loaded, lookup);
            if (observed.Kind != JerribethRecovery.Evidence.RetainedAlive) return null;
            var entries = states.SelectMany(state => state.AllEntityData).ToArray();
            var spawners = entries.OfType<UnitSpawnerBase.MyData>().Where(item => item.SpawnedUnit.UniqueId == observed.ActorId).ToArray();
            if (spawners.Length != 1 || spawners[0].UniqueId != Spawner || spawners[0].HasDied
                || entries.OfType<UnitEntityData>().Count(actor => actor.Blueprint.AssetGuid.ToString() == Unit) != 1) return null;
            return lookup(observed.ActorId!) as UnitEntityData;
        }

        private static UnitEntityData? RetainedActor()
        {
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading || LoadingProcess.Instance.IsLoadingInProcess
                || game.State.LoadedAreaState?.AreaGuid.ToString() != Capital || game.Player.IsInCombat) return null;
            var commander = game.Player.MainCharacter.Value;
            if (commander == null || !commander.State.IsConscious || commander.State.IsDead || commander.State.IsFinallyDead) return null;
            var area = game.State.LoadedAreaState;
            if (game.State.SavedAreaStates.Any(saved => saved.AreaGuid.ToString() == Capital && !ReferenceEquals(saved, area))) return null;
            var actor = Inspect(Capital, area.GetAllSceneStates().ToArray(),
                state => state.IsSceneLoaded && state.IsSceneLoadedThreadSafe && state.IsPostLoadExecuted && !state.SkipSerialize,
                id => EntityService.Instance.GetEntity(id));
            return actor != null && actor.State.IsConscious && !actor.Suppressed && !actor.IsEnemy(commander) ? actor : null;
        }
        internal void Tick()
        {
            EtudesSystem? system = null;
            try
            {
                var game = Game.Instance;
                if (game?.Player == null || game.IsLoadingSave || game.IsUnloading || LoadingProcess.Instance.IsLoadingInProcess) return;
                system = game.Player.EtudesSystem;
                if (!string.IsNullOrWhiteSpace(acceptedRequest()) && !system.EtudeIsStarted(Blueprint)
                    && !system.EtudeIsCompleted(Blueprint)) system.StartEtude(Blueprint);
            }
            catch (Exception ex) { LastError = ex; }
            finally
            {
                // A failed consent observation must also trigger native withdrawal evaluation.
                if (system?.Etudes.GetFact(Blueprint) != null) system.MarkConditionsDirty();
            }
        }

        internal bool Eligible()
        {
            try
            {
                var request = acceptedRequest();
                if (string.IsNullOrWhiteSpace(request) || !CorrespondenceAvailable()) return false;
                var actor = RetainedActor();
                var game = Game.Instance;
                var system = game.Player.EtudesSystem;
                if (actor == null || !RequestAllows(SavedData(system.Etudes.GetFact(Blueprint)), request, actor.UniqueId)) return false;
                var fallback = system.Etudes.GetFact(hidden);
                if (fallback == null || !IrabethMeeting.ReadyUnderPlayingParents(fallback, system.LoadEtudesForAreaPart, game.Player.Campaign)) return false;
                bool Ready(Etude fact) => IrabethMeeting.ReadyUnderPlayingParents(fact, system.LoadEtudesForAreaPart, game.Player.Campaign);
                return ClaimsPermit(system, Blueprint, hidden, group, capitalKtc, Ready) && LocationFree(actor);
            }
            catch (Exception ex) { LastError = ex; return false; }
        }

        internal static bool ClaimsPermit(EtudesSystem system, BlueprintEtude meeting, BlueprintEtude hidden,
            BlueprintEtudeConflictingGroup actorGroup, BlueprintEtudeConflictingGroup ktcGroup, Func<Etude, bool> ready)
            => KonomiMeeting.ClaimsPermit(system, meeting, hidden, actorGroup, ready)
                && system.GetConflictingGroupTask(ktcGroup) == null
                && KonomiMeeting.ClaimsPermit(system, meeting, hidden, ktcGroup, ready);

        private bool LocationFree(UnitEntityData actor)
        {
            var game = Game.Instance;
            IEnumerable<Occupant> Observe()
            {
                foreach (var other in game.State.Units)
                {
                    var observed = new Occupant { Actor = other, PartyOrPet = game.Player.PartyAndPets.Contains(other),
                        InGame = other.IsInGame, Dummy = other.HasDummyView,
                        Removed = other.Destroyed || other.DestroyMark || other.IsDisposed };
                    if (!ReferenceEquals(other, actor) && !observed.PartyOrPet && observed.InGame && !observed.Dummy && !observed.Removed)
                    {
                        var view = other.View;
                        if (view != null)
                        {
                            observed.Loaded = view.gameObject.scene.isLoaded;
                            observed.Active = view.gameObject.activeInHierarchy;
                            observed.OwnView = ReferenceEquals(view.Data, other);
                            if (observed.Loaded && observed.Active && observed.OwnView) observed.Position = other.Position;
                        }
                    }
                    yield return observed;
                }
            }
            return LocationFree(actor, position.GetValue(), Observe());
        }

        // Unity observations are separate from the occupancy decision; no substitute creates a view.
        internal struct Occupant
        {
            internal UnitEntityData Actor;
            internal bool PartyOrPet, InGame, Dummy, Removed, Loaded, Active, OwnView;
            internal Vector3 Position;
        }

        internal static bool LocationFree(UnitEntityData actor, Vector3 destination, IEnumerable<Occupant> occupants)
        {
            foreach (var other in occupants)
            {
                if (ReferenceEquals(other.Actor, actor) || other.PartyOrPet || !other.InGame || other.Dummy
                    || other.Removed || !other.Loaded || !other.Active) continue;
                if (!other.OwnView || (other.Position - destination).sqrMagnitude < 9f) return false;
            }
            return true;
        }

        private bool Held() => ReferenceEquals(Game.Instance.Player.EtudesSystem.GetConflictingGroupTask(group), Blueprint);

        internal bool Arrived() => ArrivedActor() != null;

        internal UnitEntityData? ArrivedActor()
        {
            try
            {
                if (!Eligible() || !Held()) return null;
                var fact = Game.Instance.Player.EtudesSystem.Etudes.GetFact(Blueprint);
                var actor = RetainedActor();
                var data = SavedData(fact);
                return fact != null && fact.IsPlaying && actor != null && data != null && !data.Failed
                    && data.Request == acceptedRequest() && data.ActorId == actor.UniqueId
                    && !actor.HasDummyView && NativeContact.IsAvailable(actor.Blueprint)
                    && (actor.Position - position.GetValue()).sqrMagnitude <= 2.25f ? actor : null;
            }
            catch (Exception ex) { LastError = ex; return null; }
        }

        internal static bool RequestAllows(MeetingData? data, string? request, string actorId)
            => !string.IsNullOrWhiteSpace(request) && (data == null
                || (data.ActorId == null || data.ActorId == actorId) && (data.Request != request || !data.Failed));

        private static MeetingData? SavedData(Etude? fact)
        {
            if (fact == null) return null;
            foreach (var component in fact.Components)
                if (component.SourceBlueprintComponent is Placement && component.TryGetData<MeetingData>(out var data)) return data;
            return null;
        }

        internal string? CurrentRequest
        {
            get
            {
                try { return acceptedRequest(); }
                catch (Exception ex) { LastError = ex; return null; }
            }
        }

        // Failure is saved separately from exceptions; a partial unhide can fail without throwing.
        internal bool SavedFailed
        {
            get
            {
                try
                {
                    var request = CurrentRequest;
                    if (string.IsNullOrWhiteSpace(request)) return false;
                    var data = SavedData(Game.Instance?.Player?.EtudesSystem.Etudes.GetFact(Blueprint));
                    return data != null && data.Request == request && data.Failed;
                }
                catch (Exception ex) { LastError = ex; return false; }
            }
        }

        private bool Place(MeetingData data)
        {
            string? request = null;
            try
            {
                if (!Eligible() || !Held()) return false;
                var actor = RetainedActor();
                request = acceptedRequest();
                if (actor == null || string.IsNullOrWhiteSpace(request) || data.ActorId != null && data.ActorId != actor.UniqueId) return false;
                if (!ReferenceEquals(move.Unit.GetValue(), actor) || !ReferenceEquals(show.Target.GetValue(), actor)) return false;
                bool arrived = PlaceNative(data, actor, request!);
                if (data.Failed) Game.Instance.Player.EtudesSystem.MarkConditionsDirty();
                return arrived;
            }
            catch (Exception ex)
            {
                LastError = ex;
                data.Request = request ?? data.Request;
                data.Failed = true;
                Game.Instance?.Player?.EtudesSystem.MarkConditionsDirty();
                return false;
            }
        }

        private bool PlaceNative(MeetingData data, UnitEntityData actor, string request)
        {
            bool Permitted() => Eligible() && Held() && acceptedRequest() == request && ReferenceEquals(RetainedActor(), actor);
            bool CurrentViewUsable()
            {
                var currentView = actor.View;
                return currentView != null && !actor.HasDummyView && ReferenceEquals(currentView.Data, actor)
                    && currentView.gameObject.scene.isLoaded && currentView.gameObject.activeInHierarchy;
            }
            return PlaceObserved(data, request, actor.UniqueId, Permitted,
                () => { position.GetValue(); orientation.GetValue(); }, show.RunAction, CurrentViewUsable,
                move.RunAction, () => { LastError = null; return Arrived(); });
        }

        // Same ordered protocol for native operations and bounded headless operation substitutes.
        internal static bool PlaceObserved(MeetingData data, string? request, string actorId, Func<bool> permitted,
            Action preflight, Action unhide, Func<bool> currentViewUsable, Action translocate, Func<bool> arrived)
        {
            if (!RequestAllows(data, request, actorId) || !permitted()) return false;
            preflight();
            if (!permitted()) return false;
            data.ActorId = actorId;
            data.Request = request;
            return AttemptPlacement(data, () =>
            {
                unhide();
                if (!permitted() || !currentViewUsable()) return false;
                translocate();
                return arrived();
            });
        }

        // Once unhide is attempted, any unverified result needs an explicit new retry episode.
        // Ordinary preemption before an attempt remains deferred and keeps its existing invitation.
        internal static bool AttemptPlacement(MeetingData data, Func<bool> attempt)
        {
            bool arrived = false;
            data.Failed = false;
            try { arrived = attempt(); return arrived; }
            finally { data.Failed = !arrived; }
        }


        public sealed class MeetingData
        {
            [JsonProperty] public string? ActorId;
            [JsonProperty] public string? Request;
            [JsonProperty] public bool Failed;
            [JsonIgnore] public bool Placed;
        }
        [TypeId("19fab8d8b0254e3c8d66fa56ff1a0c84")]
        public sealed class Placement : EtudeBracketTrigger<MeetingData>, IEtudesUpdateHandler
        {
            internal NurahMeeting Meeting = null!;
            protected override void OnActivate() { Data.Placed = false; }
            protected override void OnPostLoad() { Data.Placed = false; }
            protected override void OnEnter() { OnEtudesUpdate(); }
            protected override void OnResume() { Data.Placed = false; }
            public void OnEtudesUpdate()
            {
                if (!Data.Placed || !Meeting.Arrived()) Data.Placed = Meeting.Place(Data);
            }
        }
        public sealed class Eligibility : Condition
        {
            internal NurahMeeting Meeting = null!;
            protected override string GetConditionCaption() => "Accepted living Nurah private appointment";
            protected override bool CheckCondition() => Meeting.Eligible();
        }
        public sealed class NeverComplete : Condition
        {
            protected override string GetConditionCaption() => "Temporary meeting does not complete native history";
            protected override bool CheckCondition() => false;
        }
    }
}
