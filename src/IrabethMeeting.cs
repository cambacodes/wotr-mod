using System;
using System.Collections.Generic;
using System.Linq;
using HarmonyLib;
using Kingmaker;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Area;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Blueprints.Root;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.Designers.EventConditionActionSystem.Events;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.PubSubSystem;
using Kingmaker.View.Spawners;
using Newtonsoft.Json;

namespace Tirabade
{
    // One accepted meeting with the retained capital actor. No actor creation or native history writes.
    internal sealed class IrabethMeeting
    {
        internal const string Capital = "2570015799edf594daf2f076f2f975d8";
        internal const string Group = "997d865aa6f17cc48b480bd62ba02841";
        internal const string Departure = "99a03d4f02004b76a5e97c85ba0ec37e";
        internal const string Expedition = "260454e5186fbd34694a0393097f77b5";
        internal const string Death = "b14e13f9359585e498fcd81ab95d4d7e";
        internal const string Spawner = "3dc302d8-58ce-44f3-9766-2a437a080108";
        internal const string Unit = "280d4712dceb37f4a88e98f1f4c6e64f";
        internal const string Throne = "48967c3ec4330294ab1f5d24d9b45052";
        internal const string Hidden = "dedf24e8a06c48f449b85044879d3d62";
        internal const string Locator = "adee9a01-42a3-4850-b2d1-4a3dfcee9369";
        private static readonly HashSet<string> background = new HashSet<string> { Hidden, Throne, Departure };
        internal readonly BlueprintEtude Blueprint;
        private readonly BlueprintUnlockableFlag requested;
        private readonly BlueprintEtude departure, expedition, death;
        private readonly BlueprintEtudeConflictingGroup group;
        private readonly HideUnit show;
        private readonly TranslocateUnit move;

        // Caller registers the returned blueprint under its stable authored GUID before loading a save.
        internal IrabethMeeting(BlueprintEtude blueprint, BlueprintUnlockableFlag acceptedRequest,
            Func<string, SimpleBlueprint> resolve)
        {
            Blueprint = blueprint;
            requested = acceptedRequest;
            departure = (BlueprintEtude)resolve(Departure);
            expedition = (BlueprintEtude)resolve(Expedition);
            death = (BlueprintEtude)resolve(Death);
            group = (BlueprintEtudeConflictingGroup)resolve(Group);
            var throne = (BlueprintEtude)resolve(Throne);
            ValidateBackground((BlueprintEtude)resolve(Hidden), Hidden, -100, false);
            ValidateBackground(departure, Departure, 99, false);
            ValidateBackground(throne, Throne, -50, true);
            var actions = throne.ComponentsArray.OfType<EtudePlayTrigger>().Single().Actions.Actions;
            show = (HideUnit)actions[0];
            move = (TranslocateUnit)actions[1];
            if (!(move.Unit is UnitFromSpawner unit) || unit.Spawner.UniqueId != Spawner
                || !(move.translocatePositionEvaluator is LocatorPosition position) || position.Locator.UniqueId != Locator
                || !(move.translocateOrientationEvaluator is LocatorOrientation orientation) || orientation.Locator.UniqueId != Locator
                || !(bool)AccessTools.Field(typeof(TranslocateUnit), "m_CopyRotation").GetValue(move) || position.Offset.sqrMagnitude != 0)
                throw new InvalidOperationException("Irabeth native throne placement differs from the audited contract.");
            if (background.Contains(blueprint.AssetGuid.ToString()) || blueprint.AssetGuid == expedition.AssetGuid
                || blueprint.AssetGuid == death.AssetGuid)
                throw new ArgumentException("Meeting must use an authored blueprint identity.");
            blueprint.Priority = 100;
            blueprint.ActivationCondition = new ConditionsChecker { Conditions = new Condition[] { new Eligibility { Meeting = this } } };
            blueprint.CompletionCondition = new ConditionsChecker { Conditions = new Condition[] { new NeverComplete() } };
            Field(blueprint, "m_AllowActionStart", true);
            Field(blueprint, "m_Parent", new BlueprintEtudeReference());
            Field(blueprint, "m_StartsParent", false);
            Field(blueprint, "m_CompletesParent", false);
            Field(blueprint, "m_LinkedAreaPart", Reference<BlueprintAreaPartReference>((BlueprintAreaPart)resolve(Capital)));
            Field(blueprint, "m_ConflictingGroups", new List<BlueprintEtudeConflictingGroupReference> { Reference<BlueprintEtudeConflictingGroupReference>(group) });
            blueprint.ComponentsArray = new BlueprintComponent[] { new Placement { name = "RRT_IrabethMeetingPlacement", Meeting = this } };
        }

        private static void Field(object target, string name, object value) => AccessTools.Field(target.GetType(), name).SetValue(target, value);
        private static T Reference<T>(SimpleBlueprint blueprint) where T : BlueprintReferenceBase, new()
        {
            var reference = new T();
            Field(reference, "deserializedGuid", blueprint.AssetGuid);
            Field(reference, "<Cached>k__BackingField", blueprint);
            return reference;
        }

        internal static void ValidateBackground(BlueprintEtude blueprint, string identity, int priority, bool visible)
        {
            var groups = blueprint.ConflictingGroups.Select(reference => reference.Get()).ToArray();
            var triggers = blueprint.ComponentsArray.OfType<EtudePlayTrigger>().ToArray();
            if (blueprint.AssetGuid.ToString() != identity || blueprint.Priority != priority
                || groups.Length != 1 || groups[0] == null || groups[0].AssetGuid.ToString() != Group
                || blueprint.ComponentsArray.Length != 1 || triggers.Length != 1
                || triggers[0].Actions.Actions.Length != (visible ? 2 : 1)
                || !(triggers[0].Actions.Actions[0] is HideUnit hide) || hide.Unhide != visible
                || hide.Fade || hide.SetHideInSaves
                || (bool)AccessTools.Field(typeof(EtudePlayTrigger), "m_Once").GetValue(triggers[0])
                || triggers[0].Conditions.Conditions.Length != 0
                || !(hide.Target is UnitFromSpawner source) || source.Spawner.UniqueId != Spawner)
                throw new InvalidOperationException("Unreviewed Irabeth background placement: " + identity);
        }

        // Call from the main-thread update hook, never from an activation predicate.
        // Native selector handles release; this method never writes the claim table or completes a fact.
        internal void Tick()
        {
            var game = Game.Instance;
            if (game?.Player == null || game.IsLoadingSave || game.IsUnloading || LoadingProcess.Instance.IsLoadingInProcess) return;
            var system = game.Player.EtudesSystem;
            if (game.Player.UnlockableFlags.GetFlagValue(requested) > 0 && !system.EtudeIsStarted(Blueprint)
                && !system.EtudeIsCompleted(Blueprint)) system.StartEtude(Blueprint);
            if (system.Etudes.GetFact(Blueprint) != null) system.MarkConditionsDirty();
        }

        internal bool Eligible()
        {
            try
            {
                var game = Game.Instance;
                if (game?.Player == null || game.Player.UnlockableFlags.GetFlagValue(requested) <= 0) return false;
                var system = game.Player.EtudesSystem;
                if (!system.EtudeIsStarted(departure) || system.EtudeIsCompleted(departure)
                    || system.EtudeIsStarted(expedition) || system.EtudeIsCompleted(expedition)
                    || system.EtudeIsStarted(death) || system.EtudeIsCompleted(death)) return false;
                var actor = RetainedActor();
                if (actor == null) return false;
                var departureFact = system.Etudes.GetFact(departure);
                if (departureFact == null || !ReadyUnderPlayingParents(departureFact, system.LoadEtudesForAreaPart, game.Player.Campaign)) return false;
                var data = SavedData(system.Etudes.GetFact(Blueprint));
                if (data != null && data.ActorId != null && data.ActorId != actor.UniqueId) return false;
                return ClaimsPermit(system, Blueprint, group,
                    fact => ReadyUnderPlayingParents(fact, system.LoadEtudesForAreaPart, game.Player.Campaign));
            }
            catch { return false; }
        }

        // A pending low-priority event is still a real commitment. Do not let priority 100 starve it.
        internal static bool ClaimsPermit(EtudesSystem system, BlueprintEtude meeting,
            BlueprintEtudeConflictingGroup group, Func<Etude, bool> eligible)
        {
            var holder = system.GetConflictingGroupTask(group);
            if (holder != null && !ReferenceEquals(holder, meeting) && !background.Contains(holder.AssetGuid.ToString())) return false;
            foreach (var fact in system.Etudes.RawFacts)
            {
                if (ReferenceEquals(fact.Blueprint, meeting) || fact.IsCompleted) continue;
                var groups = fact.Blueprint.ConflictingGroups.Select(reference => reference.Get()).ToArray();
                if (groups.Any(item => item == null)) return false;
                if (!groups.Contains(group) || background.Contains(fact.Blueprint.AssetGuid.ToString())) continue;
                if (eligible(fact)) return false;
            }
            return true;
        }

        // Native arbitration and synchronization decide when parents play. Recheck after selection
        // before placement; a newly playing parent can make its pending child block this meeting.
        internal static bool ReadyUnderPlayingParents(Etude fact, BlueprintAreaPart area, BlueprintCampaign campaign)
        {
            var seen = new HashSet<Etude>();
            for (Etude? current = fact; current != null; current = current.Parent)
            {
                if (!seen.Add(current)) throw new InvalidOperationException("Cyclic native etude parent.");
                if (!ReferenceEquals(current, fact) && !current.IsPlaying) return false;
                if (current.IsCompleted || current.CompletionInProgress || !current.IsLinkedCampaign(campaign)
                    || current.Blueprint.HasLinkedAreaPart && !current.Blueprint.IsLinkedAreaPart(area)
                    || !current.Blueprint.ActivationCondition.Check()) return false;
                if (!current.Blueprint.Parent.IsEmpty() && (current.Parent == null
                    || !ReferenceEquals(current.Blueprint.Parent.Get(), current.Parent.Blueprint)))
                    throw new InvalidOperationException("Unresolved native etude parent.");
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
                || game.State.LoadedAreaState?.AreaGuid.ToString() != Capital) return null;
            var evidence = TirabadeRecoveryObserver.Observe().Single(item => item.Source.Spawner == Spawner);
            if (evidence.Kind != JerribethRecovery.Evidence.RetainedAlive || evidence.ActorId == null) return null;
            if (!(EntityService.Instance.GetEntity(Spawner) is UnitSpawnerBase.MyData source) || source.HasDied) return null;
            if (!(EntityService.Instance.GetEntity(evidence.ActorId) is UnitEntityData actor)
                || actor.View == null || !ReferenceEquals(actor.View.Data, actor)
                || !actor.View.gameObject.scene.isLoaded || !actor.State.IsConscious || actor.Suppressed
                || game.Player.IsInCombat || game.Player.MainCharacter.Value == null
                || !game.Player.MainCharacter.Value.State.IsConscious
                || actor.IsEnemy(Game.Instance.Player.MainCharacter.Value)) return null;
            // Any retained Iz representation needs its separate recovery/travel decision.
            foreach (var area in game.State.SavedAreaStates)
                if (area.AreaGuid.ToString() == "2ccc6731787b6ec41ab5adc13f1b9ce9"
                    && area.GetAllSceneStates().SelectMany(state => state.AllEntityData).OfType<UnitSpawnerBase.MyData>()
                        .Any(spawner => izSpawners.Contains(spawner.UniqueId) && (spawner.HasSpawned || spawner.HasDied))) return null;
            return actor;
        }
        private static readonly HashSet<string> izSpawners = new HashSet<string> {
            "8b5b891b-a569-42c0-a7dd-7177760fa64a", "bf142b5f-85f6-439e-9e23-f23646e22401", "d16d93ee-d53c-43da-9d0a-ff27eea9d15e"
        };

        internal bool Arrived()
        {
            try
            {
                if (!Eligible()) return false;
                var system = Game.Instance.Player.EtudesSystem;
                var fact = system.Etudes.GetFact(Blueprint);
                var actor = RetainedActor();
                return fact != null && fact.IsPlaying && actor != null
                    && SavedData(fact)?.ActorId == actor.UniqueId
                    && ReferenceEquals(system.GetConflictingGroupTask(group), Blueprint)
                    && NativeContact.IsAvailable(actor.Blueprint)
                    && (actor.Position - move.translocatePositionEvaluator.GetValue()).sqrMagnitude <= 2.25f;
            }
            catch { return false; }
        }

        private bool Place(MeetingData data)
        {
            if (!Eligible() || !ReferenceEquals(Game.Instance.Player.EtudesSystem.GetConflictingGroupTask(group), Blueprint)) return false;
            var actor = RetainedActor();
            if (actor == null || data.ActorId != null && data.ActorId != actor.UniqueId) return false;
            if (!ReferenceEquals(move.Unit.GetValue(), actor) || !ReferenceEquals(show.Target.GetValue(), actor)) return false;
            data.ActorId = actor.UniqueId;
            // Resolve the locator before unhiding. Neither native action can create a unit.
            move.translocatePositionEvaluator.GetValue();
            move.translocateOrientationEvaluator.GetValue();
            move.RunAction();
            show.RunAction();
            return true;
        }

        public sealed class MeetingData
        {
            [JsonProperty] public string? ActorId;
            [JsonIgnore] public bool Placed;
        }
        [TypeId("fae9dfc53a7c46f5ba7e87643f391b7e")]
        public sealed class Placement : EtudeBracketTrigger<MeetingData>, IEtudesUpdateHandler
        {
            internal IrabethMeeting Meeting = null!;
            protected override void OnActivate() { Data.Placed = false; }
            protected override void OnPostLoad() { Data.Placed = false; }
            protected override void OnEnter() { OnEtudesUpdate(); }
            protected override void OnResume() { Data.Placed = false; }
            public void OnEtudesUpdate()
            {
                if (!Data.Placed) Data.Placed = Meeting.Place(Data);
            }
        }
        public sealed class Eligibility : Condition
        {
            internal IrabethMeeting Meeting = null!;
            protected override string GetConditionCaption() => "Accepted retained Irabeth meeting is available";
            protected override bool CheckCondition() => Meeting.Eligible();
        }
        public sealed class NeverComplete : Condition
        {
            protected override string GetConditionCaption() => "Meeting placement never completes native history";
            protected override bool CheckCondition() => false;
        }
    }
}
