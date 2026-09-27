using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic.Commands.Base;
using Kingmaker.UnitLogic.Interaction;
using Kingmaker.UnitLogic.Parts;

namespace Tirabade
{
    // Transient click ownership only. Arrival and the authored greeting are supplied separately.
    internal sealed class NurahInteraction
    {
        private readonly Func<UnitEntityData?> arrivedActor, commander;
        private readonly BlueprintDialog dialog;
        private readonly Func<bool> canOpen;
        private readonly Action<BlueprintDialog, UnitEntityData, UnitEntityData> startDialog;
        private readonly Click interaction;
        private static readonly FieldInfo? NativeInteractions = AccessTools.Field(typeof(UnitPartInteractions), "m_Interactions");
        private UnitEntityData? actor;
        private UnitEntityData? attachedCommander;
        private UnitPartInteractions? part;
        private bool attached, selectingOthers;
        internal Exception? LastError { get; private set; }

        internal NurahInteraction(NurahMeeting meeting, BlueprintDialog dialog, Func<bool> canOpen)
            : this(meeting.ArrivedActor, () => Game.Instance?.Player?.MainCharacter.Value, dialog, canOpen,
                (greeting, target, user) => Game.Instance.DialogController.StartDialogWithUnit(greeting, target, user)) { }

        // Bounded observation/start substitutes permit headless tests without pretending to run a dialogue.
        internal NurahInteraction(Func<UnitEntityData?> arrivedActor, Func<UnitEntityData?> commander,
            BlueprintDialog dialog, Func<bool> canOpen, Action<BlueprintDialog, UnitEntityData, UnitEntityData> startDialog)
        {
            this.arrivedActor = arrivedActor ?? throw new ArgumentNullException(nameof(arrivedActor));
            this.commander = commander ?? throw new ArgumentNullException(nameof(commander));
            this.dialog = dialog ?? throw new ArgumentNullException(nameof(dialog));
            this.canOpen = canOpen ?? throw new ArgumentNullException(nameof(canOpen));
            this.startDialog = startDialog ?? throw new ArgumentNullException(nameof(startDialog));
            interaction = new Click(this);
        }

        internal void Tick()
        {
            try
            {
                var current = arrivedActor();
                var user = commander();
                if (current == null || user == null || !canOpen()) { Withdraw(); return; }
                if (!ReferenceEquals(actor, current) || !ReferenceEquals(attachedCommander, user)
                    || !ReferenceEquals(part, current.Get<UnitPartInteractions>()))
                {
                    Withdraw();
                    actor = current;
                    attachedCommander = user;
                    part = current.Ensure<UnitPartInteractions>();
                }
                if (part == null || !part.AreInteractionsEnabled || HasOtherInteraction(user) || !Proof(user, current)) { Withdraw(); return; }
                if (!attached) { part.AddInteraction(interaction); attached = true; }
                LastError = null;
            }
            catch (Exception ex) { LastError = ex; Withdraw(); }
        }

        internal void Withdraw()
        {
            if (attached) part?.RemoveInteraction(interaction);
            attached = false;
            actor = null;
            attachedCommander = null;
            part = null;
        }

        // Ask the native selector while making only this interaction unavailable; no list is rewritten.
        private bool HasOtherInteraction(UnitEntityData user)
        {
            selectingOthers = true;
            try
            {
                if (part!.SelectClickInteraction(user) != null) return true;
                // Native development mode also returns null for tied candidates; inspect without changing the list.
                if (!(NativeInteractions?.GetValue(part) is IEnumerable<IUnitInteraction> candidates))
                    throw new InvalidOperationException("Native interaction candidates cannot be verified.");
                return candidates.ToArray().Any(candidate => !ReferenceEquals(candidate, interaction)
                    && !candidate.IsApproach && candidate.IsAvailable(user, actor!));
            }
            finally { selectingOthers = false; }
        }

        private bool Available(UnitEntityData user, UnitEntityData target)
        {
            if (selectingOthers || !attached || !ReferenceEquals(target, actor)) return false;
            try
            {
                return Proof(user, target) && !HasOtherInteraction(user) && Proof(user, target);
            }
            catch (Exception ex) { LastError = ex; return false; }
        }

        private bool Proof(UnitEntityData user, UnitEntityData target)
            => ReferenceEquals(user, attachedCommander) && ReferenceEquals(user, commander())
                && ReferenceEquals(target, actor) && ReferenceEquals(target, arrivedActor()) && canOpen()
                && part != null && ReferenceEquals(part, target.Get<UnitPartInteractions>()) && part.AreInteractionsEnabled;

        private sealed class Click : IUnitInteraction
        {
            private readonly NurahInteraction owner;
            internal Click(NurahInteraction owner) { this.owner = owner; }
            public float Distance => 2f;
            public bool IsApproach => false;
            public float ApproachCooldown => 0f;
            public bool MainPlayerPreferred => true;
            public UnitPartInteractions.PriorityType Priority => UnitPartInteractions.PriorityType.EtudeBracket;
            public bool IsAvailable(UnitEntityData initiator, UnitEntityData target) => owner.Available(initiator, target);
            public UnitCommand.ResultType Interact(UnitEntityData user, UnitEntityData target)
            {
                if (!owner.Available(user, target)) return UnitCommand.ResultType.Fail;
                try
                {
                    owner.startDialog(owner.dialog, target, user);
                    return UnitCommand.ResultType.Success;
                }
                catch (Exception ex) { owner.LastError = ex; return UnitCommand.ResultType.Fail; }
            }
        }
    }
}
