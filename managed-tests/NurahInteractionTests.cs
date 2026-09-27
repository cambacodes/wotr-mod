using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Reflection.Emit;
using System.Runtime.Serialization;
using HarmonyLib;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.EntitySystem;
using Kingmaker.EntitySystem.Entities;
using Kingmaker.UnitLogic;
using Kingmaker.UnitLogic.Commands.Base;
using Kingmaker.UnitLogic.Interaction;
using Kingmaker.UnitLogic.Parts;

internal static class NurahInteractionTests
{
    private const BindingFlags Members = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static | BindingFlags.Instance;
    private static void Set(object target, string field, object value) => AccessTools.Field(target.GetType(), field).SetValue(target, value);
    private static UnitEntityData Actor()
    {
        var actor = (UnitEntityData)FormatterServices.GetUninitializedObject(typeof(UnitEntityData));
        var descriptor = (UnitDescriptor)FormatterServices.GetUninitializedObject(typeof(UnitDescriptor));
        Set(actor, "<Descriptor>k__BackingField", descriptor);
        Set(descriptor, "<Unit>k__BackingField", actor);
        Set(actor, "Parts", new EntityPartsManager(actor));
        return actor;
    }

    // Execute native development-mode arbitration; omit only Unity configuration/logging dependencies.
    private static IEnumerable<CodeInstruction> SelectionWithoutBuildMode(IEnumerable<CodeInstruction> instructions)
    {
        int replaced = 0, logs = 0;
        foreach (var instruction in instructions)
        {
            if (instruction.operand is MethodInfo method && method.DeclaringType?.FullName == "Kingmaker.Utility.BuildModeUtility"
                && method.Name == "get_IsDevelopment")
            {
                replaced++;
                yield return new CodeInstruction(OpCodes.Ldc_I4_1).WithLabels(instruction.labels.ToArray());
            }
            else if (instruction.operand is MethodInfo log && log.DeclaringType?.FullName == "Kingmaker.QA.LogChannelEx"
                && log.Name == "ErrorWithReport")
            {
                logs++;
                int pops = log.GetParameters().Length + (log.IsStatic ? 0 : 1);
                for (int i = 0; i < pops; i++)
                    yield return new CodeInstruction(OpCodes.Pop).WithLabels(i == 0 ? instruction.labels.ToArray() : Array.Empty<Label>());
            }
            else yield return instruction;
        }
        if (replaced != 1 || logs != 1) throw new InvalidOperationException("Native selector diagnostics shape changed.");
    }

    private static bool FixtureUnitName(ref string __result) { __result = "fixture"; return false; }

    private sealed class NativeClick : IUnitInteraction
    {
        internal bool Ready;
        internal UnitPartInteractions.PriorityType NativePriority = UnitPartInteractions.PriorityType.Spawner;
        internal Action? Observe;
        public float Distance => 2;
        public bool IsApproach => false;
        public float ApproachCooldown => 0;
        public bool MainPlayerPreferred => true;
        public UnitPartInteractions.PriorityType Priority => NativePriority;
        public bool IsAvailable(UnitEntityData user, UnitEntityData target) { Observe?.Invoke(); return Ready; }
        public UnitCommand.ResultType Interact(UnitEntityData user, UnitEntityData target) => UnitCommand.ResultType.Success;
    }

    internal static void Run(Action<bool, string> check)
    {
        var harmony = new Harmony("RanRomance.Tirabade.NurahInteractionTests");
        var selection = typeof(UnitPartInteractions).GetMethod("SelectClickInteraction")!;
        harmony.Patch(selection, transpiler: new HarmonyMethod(typeof(NurahInteractionTests).GetMethod("SelectionWithoutBuildMode", Members)!));
        harmony.Patch(typeof(UnitDescriptor).GetMethod("ToString", Members),
            prefix: new HarmonyMethod(typeof(NurahInteractionTests).GetMethod("FixtureUnitName", Members)!));
        object? service = null;
        var type = typeof(Tirabade.Main).Assembly.GetType("Tirabade.NurahInteraction", true)!;
        try
        {
            var actor = Actor(); var replacement = Actor(); var user = Actor(); var stranger = Actor();
            UnitEntityData? observed = null, commander = user;
            bool ready = true, throws = false, hubThrows = false, startThrows = false;
            int starts = 0;
            var greeting = new BlueprintDialog();
            BlueprintDialog? opened = null; UnitEntityData? targetSeen = null, userSeen = null;
            service = Activator.CreateInstance(type, Members, null, new object[] {
                new Func<UnitEntityData?>(() => throws ? throw new InvalidOperationException("observation failed") : observed),
                new Func<UnitEntityData?>(() => commander), greeting, new Func<bool>(() => hubThrows ? throw new InvalidOperationException("hub failed") : ready),
                new Action<BlueprintDialog, UnitEntityData, UnitEntityData>((dialog,target,initiator) => { if(startThrows) throw new InvalidOperationException("start failed"); starts++; opened=dialog;targetSeen=target;userSeen=initiator; }) }, null)!;
            void Tick() => type.GetMethod("Tick", Members)!.Invoke(service, null);
            void Withdraw() => type.GetMethod("Withdraw", Members)!.Invoke(service, null);
            IUnitInteraction? Selected(UnitEntityData unit) => unit.Get<UnitPartInteractions>()?.SelectClickInteraction(user);
            int Count(UnitPartInteractions part) => ((List<IUnitInteraction>)AccessTools.Field(typeof(UnitPartInteractions), "m_Interactions").GetValue(part)).Count;
            Tick(); check(actor.Get<UnitPartInteractions>() == null && starts == 0, "Missing arrival created interaction state");
            observed = actor; ready = false; Tick(); check(Selected(actor) == null, "Unavailable hub exposed goodbye-only menu");
            ready = true; Tick();
            var part = actor.Get<UnitPartInteractions>(); var click = Selected(actor);
            check(click != null && !click.IsApproach && click.MainPlayerPreferred, "Arrived actor lacks click-only interaction");
            check(Count(part) == 1, "Attachment created duplicate interactions");
            Tick(); check(Count(part) == 1 && ReferenceEquals(Selected(actor), click), "Repeated Tick duplicated or replaced interaction");
            check(!click!.IsAvailable(stranger, actor) && click.Interact(stranger, actor) == UnitCommand.ResultType.Fail && starts == 0,
                "Non-Commander started visit");
            check(click.Interact(user, replacement) == UnitCommand.ResultType.Fail && starts == 0, "Wrong target started visit");
            check(click.Interact(user, actor) == UnitCommand.ResultType.Success && starts == 1 && ReferenceEquals(opened,greeting)
                && ReferenceEquals(targetSeen,actor) && ReferenceEquals(userSeen,user), "Click did not forward exact greeting/actor/Commander");
            observed = null;
            check(click.Interact(user,actor) == UnitCommand.ResultType.Fail && starts == 1, "Stale selected click bypassed lost arrival");
            Tick(); check(Count(part) == 0, "Lost arrival retained addon interaction");
            observed = actor; Tick();
            ready = false; check(click.Interact(user,actor) == UnitCommand.ResultType.Fail, "Click bypassed lost route availability");
            Tick(); check(Count(part) == 0, "Lost route availability retained addon interaction");
            ready = true; Tick();
            var native = new NativeClick { Ready = true }; part.AddInteraction(native);
            check(ReferenceEquals(Selected(actor),native) && !click.IsAvailable(user,actor), "Addon shadowed newly available native interaction");
            check(click.Interact(user,actor) == UnitCommand.ResultType.Fail && starts == 1, "Previously selected addon ignored native arbitration at click");
            native.NativePriority = UnitPartInteractions.PriorityType.EtudeBracket;
            check(ReferenceEquals(Selected(actor),native) && !click.IsAvailable(user,actor), "Equal-priority native interaction competed with addon");
            Tick(); check(Count(part) == 1 && ReferenceEquals(Selected(actor),native), "Withdrawal removed native interaction");
            native.Ready = false; Tick(); check(Count(part) == 2 && ReferenceEquals(Selected(actor),click), "Dormant native interaction permanently blocked visit");
            observed = replacement; Tick();
            check(Count(part) == 1 && Selected(replacement) != null && !click.IsAvailable(user,actor), "Actor change left old addon attachment");
            observed = actor; Tick();
            commander = stranger;
            check(!click.IsAvailable(user,actor) && !click.IsAvailable(stranger,actor), "Commander change accepted stale attachment");
            Tick(); check(click.IsAvailable(stranger,actor) && !click.IsAvailable(user,actor), "Tick did not rebind current Commander");
            commander = user; Tick();
            var priorPart = actor.Get<UnitPartInteractions>(); Set(actor,"Parts",new EntityPartsManager(actor)); Tick();
            check(Count(priorPart) == 1 && Count(actor.Get<UnitPartInteractions>()) == 1, "Part replacement retained old addon or removed native entry");
            part = actor.Get<UnitPartInteractions>(); part.AreInteractionsEnabled = false;
            check(!click.IsAvailable(user,actor), "Disabled native interactions still admitted addon");
            Tick(); check(Count(part) == 0, "Disabled interactions retained addon");
            part.AreInteractionsEnabled = true; Tick();
            var changing = new NativeClick { Observe = () => observed = null }; part.AddInteraction(changing);
            check(click.Interact(user,actor) == UnitCommand.ResultType.Fail && starts == 1,
                "Native availability callback invalidated arrival but click still started");
            part.RemoveInteraction(changing); observed = actor; Tick();
            throws = true; check(!click.IsAvailable(user,actor), "Throwing observer granted availability");
            Tick(); check(Count(part) == 0 && type.GetProperty("LastError",Members)!.GetValue(service) is Exception, "Observer failure retained interaction or lost error");
            throws = false; Tick();
            hubThrows = true; check(click.Interact(user,actor) == UnitCommand.ResultType.Fail && starts == 1, "Hub predicate failure opened dialogue");
            Tick(); check(Count(part) == 0, "Hub predicate exception retained attachment");
            hubThrows = false; Tick();
            startThrows = true; check(click.Interact(user,actor) == UnitCommand.ResultType.Fail && starts == 1
                && type.GetProperty("LastError",Members)!.GetValue(service) is Exception, "Dialogue start exception escaped or returned success");
            startThrows = false;
            var failingNative = new NativeClick { Observe = () => throw new InvalidOperationException("native availability failed") };
            part.AddInteraction(failingNative);
            check(click.Interact(user,actor) == UnitCommand.ResultType.Fail && starts == 1, "Native arbitration exception opened dialogue");
            Tick(); check(Count(part) == 1, "Native arbitration failure removed foreign entry or retained addon");
            part.RemoveInteraction(failingNative); Tick(); Withdraw(); Withdraw();
            check(Count(part) == 0 && starts == 1, "Explicit repeated withdrawal mutated conversation or retained interaction");
            var equalOne = new NativeClick { Ready = true, NativePriority = UnitPartInteractions.PriorityType.EtudeBracket };
            var equalTwo = new NativeClick { Ready = true, NativePriority = UnitPartInteractions.PriorityType.EtudeBracket };
            part.AddInteraction(equalOne); part.AddInteraction(equalTwo);
            var originals = ((List<IUnitInteraction>)AccessTools.Field(typeof(UnitPartInteractions), "m_Interactions").GetValue(part)).ToArray();
            check(Selected(actor) == null, "Native development selector did not reproduce equal-priority ambiguity");
            Tick();
            check(Count(part) == 2 && originals.SequenceEqual((List<IUnitInteraction>)AccessTools.Field(typeof(UnitPartInteractions), "m_Interactions").GetValue(part)),
                "Ambiguous native selection attached a third interaction or changed original entries");
            check(click.Interact(user, actor) == UnitCommand.ResultType.Fail && starts == 1,
                "Stale click bypassed ambiguous native candidates");
            equalOne.Ready = equalTwo.Ready = false; Tick();
            check(Count(part) == 3 && ReferenceEquals(Selected(actor), click), "Dormant equal-priority entries blocked genuinely available addon");
            equalOne.Ready = equalTwo.Ready = true;
            check(!click.IsAvailable(user, actor) && click.Interact(user, actor) == UnitCommand.ResultType.Fail,
                "New native tie did not invalidate already attached addon at click");
            Tick();
            check(Count(part) == 2 && originals.SequenceEqual((List<IUnitInteraction>)AccessTools.Field(typeof(UnitPartInteractions), "m_Interactions").GetValue(part)),
                "Tie withdrawal did not preserve exact original native references/order");
        }
        finally
        {
            if (service != null) type.GetMethod("Withdraw", Members)!.Invoke(service, null);
            harmony.UnpatchAll(harmony.Id);
        }
    }
}
