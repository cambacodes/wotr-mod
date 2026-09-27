using System;
using System.Collections.Generic;
using System.Linq;
using HarmonyLib;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.PubSubSystem;
using Newtonsoft.Json;

namespace Tirabade
{
    // A personal visit of the confirmed original actor, without changing office or dismissal history.
    internal sealed class KonomiMeeting
    {
        internal const string Capital = "2570015799edf594daf2f076f2f975d8";
        internal const string Group = "12b19db05c70a2a4fa3210293d35bfd0";
        internal const string Hidden = "0b828275326053d4cb989baddb20bce7";
        internal const string Office = "b5f301fbc4c44535a6309d610d5bd28a";
        internal const string Spawner = "c658c4cf-116e-4b61-9ff9-8905bcf4fd6b";
        internal const string Locator = "e6a7de2a-ce6f-4413-b24d-06daf1990e4c";
        internal const string SceneAsset = "3e2b5ea054cd5b2479e7f13134363ef4";
        internal readonly BlueprintEtude Blueprint;
        private readonly Func<string?> acceptedRequest;
        private readonly BlueprintEtude hidden;
        private readonly BlueprintEtude office;
        private readonly BlueprintEtudeConflictingGroup group;
        private readonly HideUnit show;
        private readonly TranslocateUnit move;
        internal Exception? LastError { get; private set; }

        // Null means no current consent. Each accepted visit/retry supplies a stable saved episode ID.
        // The callback must read raw flags, not Main.State or another observer that calls this helper.
        internal KonomiMeeting(BlueprintEtude blueprint, Func<string?> acceptedRequest, Func<string, SimpleBlueprint> resolve)
        {
            Blueprint = blueprint;
            this.acceptedRequest = acceptedRequest ?? throw new ArgumentNullException(nameof(acceptedRequest));
            hidden = (BlueprintEtude)resolve(Hidden);
            office = (BlueprintEtude)resolve(Office);
            group = (BlueprintEtudeConflictingGroup)resolve(Group);
            ValidatePlacement(hidden, Hidden, -100, false);
            ValidatePlacement(office, Office, -20, true);
            var actions = office.ComponentsArray.OfType<EtudePlayTrigger>().Single().Actions.Actions;
            show = (HideUnit)actions[0];
            move = (TranslocateUnit)actions[1];
            if (!(move.Unit is UnitFromSpawner unit) || !ExactEntity(unit.Spawner, Spawner)
                || !(move.translocatePositionEvaluator is LocatorPosition position) || !ExactEntity(position.Locator, Locator)
                || !(move.translocateOrientationEvaluator is LocatorOrientation orientation) || !ExactEntity(orientation.Locator, Locator)
                || !(bool)AccessTools.Field(typeof(TranslocateUnit), "m_CopyRotation").GetValue(move) || position.Offset.sqrMagnitude != 0)
                throw new InvalidOperationException("Konomi native placement differs from the audited contract.");
            if (blueprint.AssetGuid == hidden.AssetGuid || blueprint.AssetGuid == office.AssetGuid)
                throw new ArgumentException("Meeting requires an authored blueprint identity.");
            blueprint.Priority = -90;
            blueprint.ActivationCondition = new ConditionsChecker { Conditions = new Condition[] { new Eligibility { Meeting = this } } };
            blueprint.CompletionCondition = new ConditionsChecker { Conditions = new Condition[] { new NeverComplete() } };
            Field(blueprint, "m_AllowActionStart", true);
            Field(blueprint, "m_Parent", new BlueprintEtudeReference());
            Field(blueprint, "m_StartsParent", false);
            Field(blueprint, "m_CompletesParent", false);
            Field(blueprint, "m_LinkedAreaPart", Reference<BlueprintAreaPartReference>((BlueprintAreaPart)resolve(Capital)));
            Field(blueprint, "m_ConflictingGroups", new List<BlueprintEtudeConflictingGroupReference> { Reference<BlueprintEtudeConflictingGroupReference>(group) });
            blueprint.ComponentsArray = new BlueprintComponent[] { new Placement { name = "RRT_KonomiMeetingPlacement", Meeting = this } };
        }

        private static void Field(object target, string name, object value) => AccessTools.Field(target.GetType(), name).SetValue(target, value);
        private static T Reference<T>(SimpleBlueprint blueprint) where T : BlueprintReferenceBase, new()
        {
            var reference = new T();
            Field(reference, "deserializedGuid", blueprint.AssetGuid);
            Field(reference, "<Cached>k__BackingField", blueprint);
            return reference;
        }
        private static bool ExactEntity(EntityReference entity, string id) => entity.UniqueId == id
            && entity.SceneAssetGuid == SceneAsset;

        internal static void ValidatePlacement(BlueprintEtude blueprint, string identity, int priority, bool visible)
        {
            var groups = blueprint.ConflictingGroups.Select(reference => reference.Get()).ToArray();
            var triggers = blueprint.ComponentsArray.OfType<EtudePlayTrigger>().ToArray();
            if (blueprint.AssetGuid.ToString() != identity || blueprint.Priority != priority
                || groups.Length != 1 || groups[0]?.AssetGuid.ToString() != Group
                || blueprint.ComponentsArray.Length != 1 || triggers.Length != 1
                || triggers[0].Actions.Actions.Length != (visible ? 2 : 1)
                || !(triggers[0].Actions.Actions[0] is HideUnit hide) || hide.Unhide != visible
                || hide.Fade || hide.SetHideInSaves
                || (bool)AccessTools.Field(typeof(EtudePlayTrigger), "m_Once").GetValue(triggers[0])
                || triggers[0].Conditions.HasConditions
                || !(hide.Target is UnitFromSpawner source) || !ExactEntity(source.Spawner, Spawner))
                throw new InvalidOperationException("Unreviewed Konomi placement: " + identity);
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
                string? request = acceptedRequest();
                if (string.IsNullOrWhiteSpace(request)) return false;
                var actor = RetainedActor();
                if (actor == null) return false;
                var game = Game.Instance;
                var system = game.Player.EtudesSystem;
                var data = SavedData(system.Etudes.GetFact(Blueprint));
                if (!RequestAllows(data, request, actor.UniqueId)) return false;
                var fallback = system.Etudes.GetFact(hidden);
                if (fallback == null || !IrabethMeeting.ReadyUnderPlayingParents(fallback, system.LoadEtudesForAreaPart, game.Player.Campaign)) return false;
                return ClaimsPermit(system, Blueprint, hidden, group,
                    fact => IrabethMeeting.ReadyUnderPlayingParents(fact, system.LoadEtudesForAreaPart, game.Player.Campaign));
            }
            catch (Exception ex) { LastError = ex; return false; }
        }

        internal static bool RequestAllows(MeetingData? data, string? request, string actorId)
            => !string.IsNullOrWhiteSpace(request) && (data == null
                || (data.ActorId == null || data.ActorId == actorId) && (data.Request != request || !data.Failed));

        internal static bool ClaimsPermit(EtudesSystem system, BlueprintEtude meeting, BlueprintEtude fallback,
            BlueprintEtudeConflictingGroup group, Func<Etude, bool> eligible)
        {
            var holder = system.GetConflictingGroupTask(group);
            if (holder != null && !ReferenceEquals(holder, meeting) && !ReferenceEquals(holder, fallback)) return false;
            foreach (var fact in system.Etudes.RawFacts)
            {
                if (ReferenceEquals(fact.Blueprint, meeting) || ReferenceEquals(fact.Blueprint, fallback) || fact.IsCompleted) continue;
                var groups = fact.Blueprint.ConflictingGroups.Select(reference => reference.Get()).ToArray();
                if (groups.Any(item => item == null)) return false;
                if (groups.Contains(group) && eligible(fact)) return false;
            }
            return true;
        }

        private static MeetingData? SavedData(Etude? fact)
        {
            if (fact == null) return null;
            foreach (var component in fact.Components)
                if (component.SourceBlueprintComponent is Placement && component.TryGetData<MeetingData>(out var data)) return data;
            return null;
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
            var actor = KonomiRecovery.Inspect(Capital, area.GetAllSceneStates().ToArray(),
                state => state.IsSceneLoaded && state.IsSceneLoadedThreadSafe && state.IsPostLoadExecuted && !state.SkipSerialize,
                id => EntityService.Instance.GetEntity(id));
            if (actor == null || !KonomiRecovery.HasVerifiedReturn(actor) || !actor.State.IsConscious || actor.Suppressed
                || actor.IsEnemy(commander) || actor.View == null || !ReferenceEquals(actor.View.Data, actor)
                || !actor.View.gameObject.scene.isLoaded) return null;
            return actor;
        }

        private bool Held() => ReferenceEquals(Game.Instance.Player.EtudesSystem.GetConflictingGroupTask(group), Blueprint);
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

        internal bool ContactAvailable()
        {
            try
            {
                var holder = Game.Instance?.Player?.EtudesSystem.GetConflictingGroupTask(group);
                return ContactPermitted(holder, Blueprint, office, Arrived, KonomiRecovery.ReturnContactAvailable);
            }
            catch (Exception ex) { LastError = ex; return false; }
        }

        internal static bool ContactPermitted(BlueprintEtude? holder, BlueprintEtude meeting, BlueprintEtude office,
            Func<bool> arrived, Func<bool> contact)
            => ReferenceEquals(holder, meeting) ? arrived() : ReferenceEquals(holder, office) && contact();

        internal bool Arrived()
        {
            try
            {
                if (!Eligible() || !Held()) return false;
                var fact = Game.Instance.Player.EtudesSystem.Etudes.GetFact(Blueprint);
                var actor = RetainedActor();
                var data = SavedData(fact);
                return fact != null && fact.IsPlaying && actor != null && data != null && !data.Failed
                    && data.Request == acceptedRequest() && data.ActorId == actor.UniqueId
                    && !actor.HasDummyView && KonomiRecovery.ReturnContactAvailable()
                    && (actor.Position - move.translocatePositionEvaluator.GetValue()).sqrMagnitude <= 2.25f;
            }
            catch (Exception ex) { LastError = ex; return false; }
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
            // Preflight before any native mutation. View identity may change during native unhide.
            move.translocatePositionEvaluator.GetValue();
            move.translocateOrientationEvaluator.GetValue();
            data.ActorId = actor.UniqueId;
            data.Request = request;
            return AttemptPlacement(data, () =>
            {
                show.RunAction();
                if (!Eligible() || !Held() || acceptedRequest() != request || !ReferenceEquals(RetainedActor(), actor)) return false;
                var currentView = actor.View;
                if (currentView == null || actor.HasDummyView || !ReferenceEquals(currentView.Data, actor)
                    || !currentView.gameObject.scene.isLoaded || !currentView.gameObject.activeInHierarchy) return false;
                move.RunAction();
                LastError = null;
                return Arrived();
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
        [TypeId("b460e4d8f74f48e28dc474568382ff24b")]
        public sealed class Placement : EtudeBracketTrigger<MeetingData>, IEtudesUpdateHandler
        {
            internal KonomiMeeting Meeting = null!;
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
            internal KonomiMeeting Meeting = null!;
            protected override string GetConditionCaption() => "Accepted recovered Konomi personal meeting";
            protected override bool CheckCondition() => Meeting.Eligible();
        }
        public sealed class NeverComplete : Condition
        {
            protected override string GetConditionCaption() => "Temporary meeting does not complete native history";
            protected override bool CheckCondition() => false;
        }
    }
}
