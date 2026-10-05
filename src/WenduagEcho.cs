using System;
using System.Linq;
using System.Collections.Generic;
using System.Reflection;
using HarmonyLib;
using Kingmaker;
using Kingmaker.AreaLogic.Cutscenes;
using Kingmaker.AreaLogic.Cutscenes.Commands;
using Kingmaker.AreaLogic.Etudes;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.JsonSystem;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.Designers.EventConditionActionSystem.Evaluators;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.EntitySystem.Persistence;
using Kingmaker.Localization;
using Kingmaker.GameModes;
using Kingmaker.UnitLogic;
using Kingmaker.Visual.Animation.Kingmaker;
using Newtonsoft.Json;
using UnityEngine;
using Companion = Kingmaker.Designers.EventConditionActionSystem.Evaluators.CompanionInParty;

namespace Tirabade
{
    // Authored interruption of one reviewed dispatch, never a general Kill/attack patch.
    internal sealed class WenduagEcho
    {
        internal const string E = Rules.WenduagEchoPrefix;
        internal const string Unit = "ae766624c03058440a036de90a7f2009";
        internal const string Lann = "cb29621d99b902e4da6f5d232352fbda";
        internal const string Cue = "c3ca34383f9ee3a4e9908ce68a2e828b";
        internal const string Sequence = "1199b669674bce842db3e128c938d00a";
        internal const string Death = "e25887bed0b17944f76b1f87c9f60abb";
        internal const string Attack = "791c6e19471770249833ca4dbc68aadf";
        internal const string Movement = "a2d9b57cadf57e843b75d8b0ef15b653";
        internal const string End = "bbdc280f084c7e64261f0b5f0463889c";
        internal const string Journey = "ddbcf384507535043a1ad5ad8ad8ea15";
        internal const string Capital = Rules.NurahCapital;
        // F7 coordinator staging: street-level cellar door near the verified Wenduag street point.
        // TODO: verify original-actor approach, click, occupancy and reload live; this is not a basement.
        internal static readonly Vector3? TODO_VerifiedCellarPosition = new Vector3(-24.63f, 40.13f, 57.17f);
        private static readonly string[][] ExpectedTracks = {
            new[] { "7c1d4ba8ea1255549630d99a644562a2" },
            new[] { "256d8625eeecaf54bb96819cfa989a3e", Movement, "2f95cf24e9b8a084a8630e844b4c5081",
                "d7c886f202e78294c6fae07cc7384632", "a4246a12d24497c4b897c6e372d1bf0b" },
            new[] { Attack, Death }
        };
        internal static readonly string[] NativeIds = ExpectedTracks.SelectMany(t => t).Concat(new[] {
            Cue, Sequence, End, Unit, Lann, Journey, "de8b8879260a7be4faea90d407a5c6a2",
            "feda24c3133ae3c4c8337d929d21b529", "93512f636a61892479302f06e3a4ca69" }).Distinct().ToArray();
        private readonly BlueprintEtude saved;
        private readonly Cutscene variant;
        private readonly Func<Snapshot?> snapshot;
        private readonly PlayCutscene nativePlay, adaptedPlay;
        private readonly ActionList nonfatalActions;
        private readonly Dictionary<LocalizedString, string> mourning = new Dictionary<LocalizedString, string>();
        internal Exception? LastError { get; private set; }
        internal bool Installed { get; private set; }
        private static WenduagEcho? installed;

        // Register these save-referenced objects even when evidence later refuses the adapter.
        internal sealed class Blueprints
        {
            internal BlueprintEtude Saved = null!;
            internal Cutscene Sequence = null!;
            internal Gate End = null!;
            internal CommandAction Hit = null!, Incapacitate = null!;
        }

        internal WenduagEcho(Blueprints authored, Func<string, SimpleBlueprint> resolve, Func<Snapshot?> snapshot)
        {
            saved = authored.Saved;
            variant = authored.Sequence;
            this.snapshot = snapshot;
            var cue = Require<BlueprintCue>(resolve, Cue);
            var sequence = Require<Cutscene>(resolve, Sequence);
            var action = Require<CommandAction>(resolve, Death);
            var attack = Require<CommandUnitAttack>(resolve, Attack);
            var movement = Require<CommandMoveUnit>(resolve, Movement);
            Validate(cue, sequence, action, attack, movement, Require<Gate>(resolve, End));
            ValidateMourning(resolve);
            nativePlay = (PlayCutscene)cue.OnStop.Actions[0];
            CopyFields(sequence, variant);
            CopyFields(Require<Gate>(resolve, End), authored.End);
            authored.End.StartedTracks = new List<Track>();
            authored.Hit.EntryCondition = attack.EntryCondition;
            authored.Hit.OnFail = attack.OnFail;
            authored.Hit.Action = Actions(new Hit { Echo = this });
            authored.Incapacitate.EntryCondition = action.EntryCondition;
            authored.Incapacitate.OnFail = action.OnFail;
            // Retain DetachBuff and SwitchFaction, including every native parameter, in their original order.
            authored.Incapacitate.Action = Actions(action.Action.Actions.Take(2).Concat(new GameAction[] {
                new Incapacitate { Echo = this } }).ToArray());
            nonfatalActions = authored.Incapacitate.Action;
            variant.StartedTracks = sequence.StartedTracks.Select(track => new Track {
                Commands = track.Commands.Select(command => command.AssetGuid.ToString() == Attack ? authored.Hit
                    : command.AssetGuid.ToString() == Death ? authored.Incapacitate : command).Cast<CommandBase>().ToList(),
                EndGate = track.EndGate == null ? null : authored.End, Repeat = track.Repeat,
                Comment = track.Comment, IsCollapsed = track.IsCollapsed
            }).ToList();
            variant.OnStopped = Actions(new Completed { Echo = this });
            adaptedPlay = new PlayCutscene { Cutscene = variant, Parameters = nativePlay.Parameters,
                PutInQueue = nativePlay.PutInQueue, CheckExistence = nativePlay.CheckExistence };
            saved.ActivationCondition = Empty();
            saved.CompletionCondition = new ConditionsChecker { Conditions = new Condition[] { new NeverComplete() } };
            SetField(saved, "m_AllowActionStart", true);
            saved.ComponentsArray = new BlueprintComponent[] { new Custody { name = "RRT_WenduagEchoCustody", Echo = this } };
            cue.OnStop = Actions(new Dispatch { Echo = this });
            Installed = true;
            installed = this;
        }

        private static T Require<T>(Func<string, SimpleBlueprint> resolve, string id) where T : SimpleBlueprint
            => resolve(id) is T value && value.AssetGuid.ToString() == id ? value
                : throw new InvalidOperationException("Wenduag echo native type/identity differs: " + id);
        private static void SetField(object target, string name, object value) => AccessTools.Field(target.GetType(), name).SetValue(target, value);
        private static string RefId(object target, string field) =>
            AccessTools.Field(target.GetType(), field)?.GetValue(target) is BlueprintReferenceBase reference
                ? reference.Guid.ToString() : throw new InvalidOperationException("Wenduag native reference missing: " + target.GetType().Name + "." + field);
        private static bool EmptyAnd(ConditionsChecker checker) => checker != null && checker.Operation == Operation.And && checker.Conditions?.Length == 0;
        private static ConditionsChecker Empty() => new ConditionsChecker { Conditions = Array.Empty<Condition>() };
        private static ActionList Actions(params GameAction[] actions) => new ActionList { Actions = actions };
        private static void CopyFields(SimpleBlueprint source, SimpleBlueprint target)
        {
            // Blueprint identity and cache state stay authored; copy only the native command/gate parameters.
            for (Type? type = source.GetType(); type != null && type != typeof(BlueprintScriptableObject); type = type.BaseType)
                foreach (var field in type.GetFields(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.DeclaredOnly))
                    if (!field.IsInitOnly) field.SetValue(target, field.GetValue(source));
        }
        private static bool CompanionMatches(UnitEvaluator? evaluator, string id, bool remote = true)
            => evaluator is Companion companion && RefId(companion, "m_Companion") == id
                && companion.IncludeRemote == remote && companion.IncludeExCompanions == remote && companion.IncludeDettached == remote;

        internal static void Validate(BlueprintCue cue, Cutscene sequence, CommandAction action,
            CommandUnitAttack attack, CommandMoveUnit movement, Gate end)
        {
            if (cue?.Text == null || cue.OnStop?.Actions == null || sequence?.StartedTracks == null
                || sequence.OnStopped?.Actions == null || action?.Action?.Actions == null || attack == null
                || movement == null || end?.StartedTracks == null)
                throw new InvalidOperationException("Wenduag native dispatch has incomplete collections/references.");
            if (cue.AssetGuid.ToString() != Cue || cue.Text.Key != "88228878-33b1-43df-83b2-c3f97d1b8171"
                || cue.OnStop.Actions.Length != 1 || !(cue.OnStop.Actions[0] is PlayCutscene play)
                || play.Cutscene != sequence || play.PutInQueue || !play.CheckExistence || play.Parameters.Parameters.Length != 0
                || sequence.AssetGuid.ToString() != Sequence || sequence.StartedTracks.Count != 3
                || sequence.OnStopped.Actions.Length != 0 || sequence.NonSkippable || sequence.ForbidDialogs
                || end.AssetGuid.ToString() != End || end.StartedTracks.Count != 0
                || end.Op != Operation.And || end.ActivationMode != Gate.ActivationModeType.AllTracks
                || sequence.Op != Operation.And || sequence.ActivationMode != Gate.ActivationModeType.AllTracks)
                throw new InvalidOperationException("Wenduag echo dispatch/gates differ from reviewed native evidence.");
            for (int i = 0; i < ExpectedTracks.Length; i++)
            {
                var track = sequence.StartedTracks[i];
                if (track.Repeat || !track.Commands.Select(c => c.AssetGuid.ToString()).SequenceEqual(ExpectedTracks[i])
                    || track.Commands.Any(c => !EmptyAnd(c.EntryCondition))
                    || (i == 1 ? track.EndGate != null : track.EndGate != end))
                    throw new InvalidOperationException("Wenduag echo track order differs: " + i);
            }
            var position = movement.Target as PositionRelativeToUnit;
            if (action.AssetGuid.ToString() != Death || action.Action.Actions.Length != 3
                || !(action.Action.Actions[0] is DetachBuff detach) || RefId(detach, "m_Buff") != "281a1f606d92728409ee5cbf5599855d"
                || !CompanionMatches(detach.Target, Unit)
                || !(action.Action.Actions[1] is SwitchFaction faction) || !CompanionMatches(faction.Target, Unit)
                || RefId(faction, "m_Faction") != "d64258e86eeb1d8479f35a9b16f6590a" || faction.IncludeGroup || faction.ResetAllRelations
                || !(action.Action.Actions[2] is Kill kill) || !CompanionMatches(kill.Target, Unit) || !CompanionMatches(kill.Killer, Lann)
                || kill.Critical || !kill.DisableBattleLog || !kill.RemoveExp
                || attack.AssetGuid.ToString() != Attack
                || !CompanionMatches((UnitEvaluator)AccessTools.Field(typeof(CommandUnitAttack), "m_UnitEvaluator").GetValue(attack), Lann, false)
                || !CompanionMatches((UnitEvaluator)AccessTools.Field(typeof(CommandUnitAttack), "m_TargetEvaluator").GetValue(attack), Unit)
                || new[] { "m_FullAttack", "m_IsMiss", "m_HitShield", "m_IsRend", "m_NeedLoS" }
                    .Any(field => (bool)AccessTools.Field(typeof(CommandUnitAttack), field).GetValue(attack))
                || !(bool)AccessTools.Field(typeof(CommandUnitAttack), "m_DisableLog").GetValue(attack)
                || movement.AssetGuid.ToString() != Movement || !CompanionMatches(movement.Unit, Unit)
                || position == null || !CompanionMatches(position.Unit, Lann)
                || position.Distance != 1.2f || position.Angle != 0f)
                throw new InvalidOperationException("Wenduag echo actions/evaluators differ from reviewed native evidence.");
        }

        private void ValidateMourning(Func<string, SimpleBlueprint> resolve)
        {
            var answer = Require<BlueprintAnswer>(resolve, "de8b8879260a7be4faea90d407a5c6a2");
            var cue = Require<BlueprintCue>(resolve, "feda24c3133ae3c4c8337d929d21b529");
            var reply = Require<BlueprintCue>(resolve, "93512f636a61892479302f06e3a4ca69");
            if (answer.Text.Key != "06d1eb8a-c860-4eaa-bca0-a3f13b97dddf" || answer.OnSelect.Actions.Length != 0
                || answer.NextCue.Cues.Count != 1 || answer.NextCue.Cues[0].Guid.ToString() != reply.AssetGuid.ToString()
                || cue.Text.Key != "306ff469-b221-474d-81b1-44d2ff4ec058" || !EmptyAnd(cue.Conditions)
                || cue.OnShow.Actions.Length != 0 || cue.OnStop.Actions.Length != 0 || cue.Continue.Cues.Count != 1
                || cue.Continue.Cues[0].Guid.ToString() != "e71b40e4361614e4a9341af9ae5fb35e"
                || reply.Text.Key != "140a542a-52da-405a-b140-8d4ced00e54e" || !EmptyAnd(reply.Conditions)
                || reply.OnShow.Actions.Length != 0 || reply.OnStop.Actions.Length != 0 || reply.Continue.Cues.Count != 0
                || reply.Answers.Count != 1 || reply.Answers[0].Guid.ToString() != "b409187619de6d64abf4b95f715bbd8b")
                throw new InvalidOperationException("Wenduag echo mourning edits differ from reviewed evidence.");
            // Authored DLC variants of these exact localized fields only; conditions, actions and saved identities stay native.
            mourning[answer.Text] = "\"She's breathing. What will you do about Wenduag?\"";
            mourning[cue.Text] = "{n}The hook catches her belt as Lann strikes. You turn the shaft under her weight. "
                + "She falls sideways, clawing at the stone. Lann draws back for another blow; you drag her beyond his reach. "
                + "He wipes the black streaks from his face and looks down at Wenduag.{/n} \"Still breathing. "
                + "Of course she is. Commander, keep that hook on her. I've had enough of her second chances for today.\"";
            mourning[reply.Text] = "\"Right now? Keep out of reach. After that, we still have Savamelekh to deal with. "
                + "I'm not turning my back on either of them.\"";
        }

        public sealed class Record
        {
            [JsonProperty] public int Version = 1;
            [JsonProperty] public string? ActorId, SourceArea, SourceStorage, Attempt;
            [JsonProperty] public string Phase = "pending";
            [JsonProperty] public bool Incapacitated, PassiveAdded, UntargetableAdded, JourneyObserved;
            [JsonProperty] public int PickupHour = -1;
            internal bool WellFormed => Version == 1 && !string.IsNullOrWhiteSpace(ActorId)
                && !string.IsNullOrWhiteSpace(SourceArea) && !string.IsNullOrWhiteSpace(SourceStorage)
                && Guid.TryParse(Attempt, out var attempt) && attempt != Guid.Empty
                && new[] { "pending", "down", "hidden", "transport", "arrived", "released", "invalid" }.Contains(Phase)
                && (Phase == "pending" || Phase == "invalid" || Incapacitated && PassiveAdded
                    && (Phase == "released" ? !UntargetableAdded : UntargetableAdded)
                    && (Phase == "down" ? PickupHour == -1 && !JourneyObserved : PickupHour >= 0)
                    && (Phase != "arrived" && Phase != "released" || JourneyObserved));
        }
        private Record? Data()
        {
            var fact = Game.Instance?.Player?.EtudesSystem.Etudes.GetFact(saved);
            if (fact == null) return null;
            foreach (var component in fact.Components)
                if (component.SourceBlueprintComponent is Custody && component.TryGetData<Record>(out var data)) return data;
            return null;
        }
        private static bool Living(UnitEntityData actor) => !actor.Destroyed && !actor.DestroyMark && !actor.IsDisposed
            && !actor.State.IsDead && !actor.State.IsFinallyDead && !actor.State.MarkedForDeath;
        private IEnumerable<UnitEntityData> Actors()
        {
            var game = Game.Instance;
            return game.State.Units.Concat(game.Player.CrossSceneState.AllEntityData.OfType<UnitEntityData>())
                .Concat(game.State.SavedAreaStates.SelectMany(a => a.AllEntityData).OfType<UnitEntityData>())
                .Where(a => a.Blueprint?.AssetGuid.ToString() == Unit || a.OriginalBlueprint?.AssetGuid.ToString() == Unit).Distinct();
        }
        private UnitEntityData? Original(Record data)
        {
            if (!data.WellFormed || data.Phase == "invalid") return null;
            var matches = Actors().ToArray();
            // A duplicate is a custody failure, even if hidden or dead. Never select a convenient living twin.
            if (matches.Length > 1) { data.Phase = "invalid"; return null; }
            var actor = matches.SingleOrDefault();
            if (actor == null) return null; // unloaded/unresolved storage is unavailable, not death
            if (actor.UniqueId != data.ActorId || !Living(actor)) { data.Phase = "invalid"; return null; }
            var area = Game.Instance.State.LoadedAreaState;
            return area != null && NativeContact.HasCurrentStorage(actor, area, Game.Instance.Player.CrossSceneState) ? actor : null;
        }
        private static bool LivePath(Snapshot state) => state.Has("trickster")
            && !new[] { "trickster.failed", "dragon", "legend", "swarm" }.Any(state.Has);
        private static bool Closed(Snapshot state) => new[] { "wenduag.killed", "wenduag.kicked_out", "wenduag.closed",
            "wenduag.q3_killed", "wenduag.q3_sent_away", "wenduag.hello_sent_away", "wenduag.hello_attacked",
            "wenduag.romance_active", "wenduag.romance_finished", "wenduag.romance_finished.latched" }.Any(state.Has);
        private static bool Page(Snapshot state) => state.Has("trickster.foresight.accepted") || state.Has("foresight.page_taken");
        private static bool Loaded(UnitEntityData actor)
        {
            var game = Game.Instance;
            var view = actor.View;
            return Living(actor) && game.State.LoadedAreaState != null
                && NativeContact.HasCurrentStorage(actor, game.State.LoadedAreaState, game.Player.CrossSceneState)
                && (ReferenceEquals(actor.HoldingState, game.Player.CrossSceneState) || actor.HoldingState!.IsSceneLoaded)
                && view != null && ReferenceEquals(view.Data, actor) && view.gameObject.scene.isLoaded
                && view.gameObject.activeInHierarchy && actor.IsInGame && !actor.Suppressed;
        }
        private UnitEntityData? LannActor()
        {
            var matches = Game.Instance.State.Units.Where(a => a.Blueprint.AssetGuid.ToString() == Lann && Living(a)).ToArray();
            return matches.Length == 1 ? matches[0] : null;
        }
        private bool CanAdapt(Snapshot? state)
        {
            var game = Game.Instance;
            var commander = game?.Player?.MainCharacter.Value;
            var matches = Actors().ToArray();
            var actor = matches.Length == 1 ? matches[0] : null;
            var lann = LannActor();
            return Installed && state != null && state.Chapter == 4 && LivePath(state) && Page(state)
                && state.Has(E + "ready") && !Closed(state) && Data() == null
                && actor != null && Loaded(actor) && commander != null && Loaded(commander) && commander.State.IsConscious
                && lann != null && Loaded(lann) && lann.State.IsConscious && game!.Player.PartyAndPets.Contains(lann);
        }
        private void DispatchSequence()
        {
            var state = snapshot();
            if (Data() != null) return; // A saved dispatch must never repeat its attack, adapted or native.
            if (state == null || !CanAdapt(state)) { nativePlay.RunAction(); return; }
            var actor = Actors().Single();
            var game = Game.Instance;
            game.Player.EtudesSystem.StartEtude(saved);
            var data = Data() ?? throw new InvalidOperationException("Wenduag custody record unavailable before dispatch.");
            data.ActorId = actor.UniqueId;
            data.SourceArea = state.Area;
            data.SourceStorage = actor.HoldingState!.SceneName;
            data.Attempt = Guid.NewGuid().ToString();
            data.Phase = "pending"; // saved before any adapted operation
            // Stabilize the living defeated actor before native DetachBuff removes its immortality.
            actor.Damage = Math.Min(actor.Damage, Math.Max(0, actor.Stats.HitPoints.ModifiedValue - 1));
            var lann = LannActor()!;
            game.Player.MainCharacter.Value.Translocate(lann.Position + Quaternion.Euler(0, lann.Orientation + 90, 0) * Vector3.forward * 1.2f, lann.Orientation);
            adaptedPlay.RunAction();
        }
        private void IncapacitateOriginal()
        {
            var data = Data();
            if (data == null || data.Phase != "pending" || data.Incapacitated) return;
            var actor = Original(data);
            if (actor == null) { data.Phase = "invalid"; return; }
            // Only an actor still alive can have its wound stabilized; no death bits are cleared.
            actor.Damage = Math.Min(actor.Damage, Math.Max(0, actor.Stats.HitPoints.ModifiedValue - 1));
            actor.State.AddCondition(UnitCondition.Unconscious);
            data.Incapacitated = true;
            actor.Passive.Retain(); data.PassiveAdded = true;
            actor.State.Features.IsUntargetable.Retain(); data.UntargetableAdded = true;
            if (actor.IsInCombat) actor.LeaveCombat();
        }
        private void CompleteSequence()
        {
            var data = Data();
            if (data?.Phase != "pending") return;
            // Native cutscene skip may complete before an action track runs. Complete the same
            // nonfatal actions once; never replay the hit or substitute a second actor.
            if (!data.Incapacitated && Original(data) is UnitEntityData living && Loaded(living)) nonfatalActions.Run();
            if (!data.Incapacitated) return;
            var actor = Original(data);
            if (actor != null && actor.State.IsUnconscious && actor.Damage < actor.Stats.HitPoints.ModifiedValue)
                data.Phase = "down";
        }

        internal void Observe(Snapshot state)
        {
            try
            {
                if (Installed) state.Flags.Add(E + "adapter_available");
                var data = Data();
                bool origin = data != null || state.Has(E + "rescued") || state.Has(E + "returned");
                if (!origin) return;
                if (data == null || !data.WellFormed || Closed(state) || !state.Has(E + "ready")
                    || state.Has(E + "rescued") != (data.Phase == "hidden" || data.Phase == "transport" || data.Phase == "arrived" || data.Phase == "released")
                    || state.Has(E + "returned") != (data.Phase == "released"))
                {
                    if (data != null) data.Phase = "invalid";
                    state.Flags.Add(E + "unavailable"); return;
                }
                var actor = Original(data);
                if (actor == null || !LivePath(state) || !Page(state)) { state.Flags.Add(E + "unavailable"); return; }
                state.Flags.Add(E + "valid");
                bool safe = !Game.Instance.IsLoadingSave && !Game.Instance.IsUnloading && !LoadingProcess.Instance.IsLoadingInProcess
                    && !Game.Instance.Player.IsInCombat && Game.Instance.Player.MainCharacter.Value?.State.IsConscious == true;
                if (data.Phase == "down" && safe && state.Area == data.SourceArea && actor.HoldingState?.SceneName == data.SourceStorage
                    && Loaded(actor) && actor.State.IsUnconscious
                    && LannActor() is UnitEntityData lann && Loaded(lann))
                {
                    state.Flags.Add(E + "casualty_available");
                    state.SceneContacts.Add(E + "pickup");
                }
                if (data.Phase == "arrived" && safe && Loaded(actor) && state.Area == Capital && state.Chapter == 5)
                    state.Flags.Add(E + "return_available");
                // Only the released original grants continuing presence, never an intermediate custody phase.
                if (data.Phase != "released" && data.Phase != "down" && data.Phase != "arrived")
                    state.Flags.Add(E + "unavailable");
            }
            catch (Exception ex) { LastError = ex; state.Flags.Add(E + "unavailable"); }
        }
        internal UnitEntityData? ContactActor(bool pickup)
        {
            var state = snapshot();
            var data = Data();
            if (state == null || data == null || state.Has(E + "unavailable")) return null;
            if (pickup ? !state.Has(E + "casualty_available") : data.Phase != "arrived" && data.Phase != "released") return null;
            var actor = Original(data);
            return actor != null && Loaded(actor) ? actor : null;
        }
        internal bool OwnsOriginal => Data() != null;
        internal bool ApplyChoice(Scene scene, Choice choice, Action recordProgress)
        {
            var state = snapshot();
            if (state == null || !LivePath(state) || !Page(state) || Closed(state)) return false;
            var data = Data();
            var actor = data == null ? null : Original(data);
            if ((scene.Id == E + "pickup" || scene.Id == E + "return")
                && (actor == null || !Loaded(actor) || data!.Phase != (scene.Id == E + "pickup" ? "down" : "arrived"))) return false;
            var kingdom = Game.Instance.Player.Kingdom;
            int cost = choice.Crusade == null ? 0 : Math.Abs(choice.Crusade.Amount);
            if (cost != 0 && (kingdom == null || kingdom.Resources.Finances < cost)) return false;
            var storage = actor?.HoldingState;
            bool inGame = actor?.IsInGame ?? false;
            bool untargetableAdded = data?.UntargetableAdded ?? false;
            string? phase = data?.Phase;
            int pickupHour = data?.PickupHour ?? -1;
            bool paid = false;
            try
            {
                if (cost != 0) { kingdom.SpendResource(Kingmaker.Kingdom.KingdomResourcesAmount.FromFinances(cost)); paid = true; }
                if (!Transition(scene, choice)) throw new InvalidOperationException("Wenduag custody changed during payment.");
                recordProgress();
                return true;
            }
            catch (Exception ex)
            {
                LastError = ex;
                if (paid) kingdom.GainResource(Kingmaker.Kingdom.KingdomResourcesAmount.FromFinances(cost));
                if (data != null && actor != null)
                {
                    if (storage != null && !ReferenceEquals(actor.HoldingState, storage))
                    { actor.HoldingState?.RemoveEntityData(actor); storage.AddEntityData(actor); }
                    actor.IsInGame = inGame;
                    if (untargetableAdded && !data.UntargetableAdded) actor.State.Features.IsUntargetable.Retain();
                    data.UntargetableAdded = untargetableAdded;
                    data.Phase = phase!; data.PickupHour = pickupHour;
                }
                return false;
            }
        }

        private bool Transition(Scene? scene, Choice? choice)
        {
            if (scene == null || choice == null || scene.Id != E + "pickup" && scene.Id != E + "return") return true;
            var data = Data();
            var actor = data == null ? null : Original(data);
            if (actor == null || !Loaded(actor)) return false;
            if (choice.Set.Contains(E + "rescued"))
            {
                if (data!.Phase != "down") return false;
                data.Phase = "hidden";
                data.PickupHour = (int)Game.Instance.Player.GameTime.TotalHours;
                // Move the exact entity between native persistent stores, never construct another unit.
                actor.HoldingState!.RemoveEntityData(actor);
                Game.Instance.Player.CrossSceneState.AddEntityData(actor);
                actor.IsInGame = false;
                data.Phase = "transport";
            }
            else if (choice.Set.Contains(E + "returned"))
            {
                if (data!.Phase != "arrived") return false;
                data.Phase = "released";
                if (data.UntargetableAdded) { actor.State.Features.IsUntargetable.Release(); data.UntargetableAdded = false; }
            }
            else if (choice.Set.Contains("wenduag.closed")) { actor.IsInGame = false; data!.Phase = "invalid"; }
            return true;
        }
        internal void Tick()
        {
            try
            {
                var game = Game.Instance;
                if (game?.Player == null || game.IsLoadingSave || game.IsUnloading || LoadingProcess.Instance.IsLoadingInProcess) return;
                var data = Data();
                if (data == null || data.Phase != "transport") return;
                var state = snapshot();
                if (state == null || state.Has(E + "unavailable"))
                {
                    // Transport itself is unavailable for conversation; consult identity and path separately.
                    if (state == null || !LivePath(state) || !Page(state) || Closed(state)) return;
                }
                var answer = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(Journey)) as BlueprintAnswer;
                if (answer != null && game.Player.Dialog.SelectedAnswers.Contains(answer)) data.JourneyObserved = true;
                if (!data.JourneyObserved || state.Chapter != 5 || state.Area != Capital || game.Player.IsInCombat
                    || game.DialogController.Dialog != null || game.CurrentMode != GameModeType.Default
                    || game.Player.Dialog.Scheduled != null || TODO_VerifiedCellarPosition == null) return;
                var actor = Original(data);
                if (actor == null) return;
                var target = TODO_VerifiedCellarPosition.Value;
                if (game.State.Units.Any(other => !ReferenceEquals(other, actor) && Loaded(other)
                    && (other.Position - target).sqrMagnitude < 9f)) return;
                actor.Translocate(target, 0f);
                actor.GroupId = actor.UniqueId;
                actor.Descriptor.SwitchFactions((BlueprintFaction)ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(GuestPresence.NeutralFaction)), true);
                actor.State.RemoveCondition(UnitCondition.Unconscious);
                actor.IsInGame = true;
                if (Loaded(actor) && actor.State.IsConscious && (actor.Position - target).sqrMagnitude <= 2.25f) data.Phase = "arrived";
            }
            catch (Exception ex) { LastError = ex; }
        }
        internal string? MourningText(LocalizedString field)
        {
            if (!mourning.TryGetValue(field, out var text)) return null;
            var state = snapshot();
            var data = Data();
            return state != null && state.Has(E + "valid") && data != null && data.Incapacitated
                && data.Phase != "pending" && data.Phase != "invalid" ? text : null;
        }

        [TypeId("4cc9475b0a9e4ea58231c9726c53549a")]
        public sealed class Custody : EtudeBracketTrigger<Record>
        {
            internal WenduagEcho Echo = null!;
            protected override void OnActivate() { _ = Data; }
            protected override void OnPostLoad() { /* Native component JSON holds custody; never replay a hit here. */ }
        }
        public sealed class NeverComplete : Condition
        {
            protected override string GetConditionCaption() => "Wenduag original custody persists";
            protected override bool CheckCondition() => false;
        }
        public sealed class Dispatch : GameAction
        {
            internal WenduagEcho Echo = null!;
            public override string GetCaption() => "Reviewed Wenduag death or paid hook interruption";
            public override void RunAction() => Echo.DispatchSequence();
        }
        public sealed class Hit : GameAction
        {
            internal WenduagEcho Echo = null!;
            public override string GetCaption() => "Lann's damage-free blow, interrupted by the hooked shaft";
            public override void RunAction()
            {
                // Animation only: no UnitAttack, RuleAttackWithWeapon or damage command can fire.
                Echo.LannActor()?.View?.AnimationManager.Execute(UnitAnimationType.MainHandAttack);
            }
        }
        public sealed class Incapacitate : GameAction
        {
            internal WenduagEcho Echo = null!;
            public override string GetCaption() => "Stabilize the living original under the hooked shaft";
            public override void RunAction() => Echo.IncapacitateOriginal();
        }
        public sealed class Completed : GameAction
        {
            internal WenduagEcho Echo = null!;
            public override string GetCaption() => "Complete the reviewed Wenduag interruption";
            public override void RunAction() => Echo.CompleteSequence();
        }
        [HarmonyPatch(typeof(LocalizedString), "LoadString")]
        private static class MourningPatch
        {
            private static bool Prefix(LocalizedString __instance, ref string __result)
            {
                var text = installed?.MourningText(__instance);
                if (text == null) return true;
                __result = text; return false;
            }
        }
    }
}
