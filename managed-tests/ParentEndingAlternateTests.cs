using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;

internal static class ParentEndingAlternateTests
{
    private const BindingFlags Fields = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
    private sealed class CountAction : GameAction
    {
        internal int Calls;
        internal Action? Effect;
        public override string GetCaption() => "Original cue action";
        public override void RunAction() { Calls++; Effect?.Invoke(); }
    }
    private sealed class NestedCondition : Condition
    {
        internal ConditionsChecker Nested = new ConditionsChecker { Operation = Operation.Or, Conditions = new Condition[] { null! } };
        protected override string GetConditionCaption() => "Nested original checker";
        protected override bool CheckCondition() => Nested.Check();
    }
    private static FieldInfo Field(Type type, string name)
    {
        for (Type? current = type; current != null; current = current.BaseType)
        {
            var field = current.GetField(name, Fields | BindingFlags.DeclaredOnly);
            if (field != null) return field;
        }
        throw new MissingFieldException(name);
    }
    private static LocalizedString Text(string key)
    {
        var result = new LocalizedString(); Field(result.GetType(), "m_Key").SetValue(result, key); return result;
    }
    private static BlueprintCueBaseReference Reference(BlueprintCueBase cue)
    {
        var result = new BlueprintCueBaseReference();
        Field(result.GetType(), "deserializedGuid").SetValue(result, cue.AssetGuid);
        Field(result.GetType(), "<Cached>k__BackingField").SetValue(result, cue);
        return result;
    }
    private static BlueprintCue Variant(BlueprintCue original, string suffix)
    {
        var variant = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(Guid.NewGuid().ToString("N")), name = suffix };
        foreach (var field in typeof(BlueprintCue).GetFields(Fields | BindingFlags.DeclaredOnly)) field.SetValue(variant, field.GetValue(original));
        variant.Text = Text("private." + suffix);
        variant.ShowOnce = original.ShowOnce;
        variant.ShowOnceCurrentDialog = original.ShowOnceCurrentDialog;
        return variant;
    }

    internal static void Run(Action<bool, string> check)
    {
        var type = typeof(Tirabade.Main).Assembly.GetType("Tirabade.ParentEndingAlternate", true)!;
        var attach = type.GetMethod("Attach", BindingFlags.Static | BindingFlags.NonPublic)!;
        object Attach(BlueprintBookPage page, BlueprintCue original, BlueprintCue ordinary, BlueprintCue? survivor,
            Func<BlueprintCue?> select, Func<BlueprintCueBase, bool, bool> seen) => attach.Invoke(null,
                new object?[] { page, original, Reference(ordinary), survivor == null ? null : Reference(survivor), select, seen })!;
        void Refresh(object binding) => binding.GetType().GetMethod("Refresh", Fields)!.Invoke(binding, null);
        void Invalidate(object binding) => binding.GetType().GetMethod("Invalidate", Fields)!.Invoke(binding, null);
        bool Eligible(BlueprintCue cue) => cue.Conditions.Conditions.Single().Check();
        Exception? Error(object binding) => binding.GetType().GetProperty("LastObservationError", Fields)!.GetValue(binding) as Exception;
        void Rejected(Action action, string message)
        {
            bool rejected = false;
            try { action(); } catch (TargetInvocationException ex) when (ex.InnerException is ArgumentException || ex.InnerException is InvalidOperationException) { rejected = true; }
            check(rejected, message);
        }

        foreach (bool local in new[] { false, true })
        {
            var page = new BlueprintBookPage();
            var original = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(Guid.NewGuid().ToString("N")), name = "original", Text = Text("native.shared"),
                ShowOnce = true, ShowOnceCurrentDialog = local, Conditions = new ConditionsChecker { Operation = Operation.Or, Conditions = Array.Empty<Condition>() },
                OnShow = new ActionList(), OnStop = new ActionList(), Continue = new CueSelection(), Speaker = new DialogSpeaker { NoSpeaker = true } };
            var shownAction = new CountAction { Owner = original, name = "native-action" };
            var stoppedAction = new CountAction { Owner = original, name = "native-stop" };
            original.OnShow.Actions = new GameAction[] { shownAction };
            original.OnStop.Actions = new GameAction[] { stoppedAction };
            original.ElementsArray.Add(shownAction); original.ElementsArray.Add(stoppedAction);
            var before = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(Guid.NewGuid().ToString("N")) };
            var after = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(Guid.NewGuid().ToString("N")) };
            page.Cues.AddRange(new[] { Reference(before), Reference(original), Reference(after) });
            var pageAction = new CountAction { Owner = page, name = "mark-eight-pages-seen" };
            page.OnShow = new ActionList { Actions = new GameAction[] { pageAction } };
            var pageActions = page.OnShow;
            var pageChecker = page.Conditions;
            var originalChecker = original.Conditions;
            var ordinary = Variant(original, "ordinary." + local);
            var survivor = Variant(original, "survivor." + local);
            var originalText = original.Text;
            var seen = new HashSet<BlueprintCueBase>();
            BlueprintCue? selected = ordinary;
            int observations = 0;
            Func<BlueprintCue?> selector = () => { observations++; return selected; };
            Func<BlueprintCueBase, bool, bool> wasSeen = (cue, useLocal) => { check(useLocal == local, "Wrong native show-once scope"); return seen.Contains(cue); };
            var binding = Attach(page, original, ordinary, survivor, selector, wasSeen);
            check(page.Cues.Select(r => r.Get()).SequenceEqual(new BlueprintCueBase[] { before, ordinary, survivor, original, after }), "Alternate moved unrelated page entries");
            check(ReferenceEquals(page.OnShow, pageActions) && ReferenceEquals(page.Conditions, pageChecker) && pageAction.Calls == 0, "Attachment copied or ran page behavior");
            check(ReferenceEquals(original.Text, originalText) && original.Text.Key == "native.shared", "Original localization was changed");
            check(shownAction.Owner == original && stoppedAction.Owner == original && ordinary.ElementsArray.Count == 1 && survivor.ElementsArray.Count == 1, "Native ownership or variant elements changed");
            check(ReferenceEquals(ordinary.OnShow, original.OnShow) && ReferenceEquals(survivor.OnStop, original.OnStop)
                && ReferenceEquals(ordinary.Continue, original.Continue), "Original behavior identities were lost");
            check(Eligible(original) && !Eligible(ordinary) && !Eligible(survivor) && observations == 0, "Unrefreshed helper does not preserve original");
            Refresh(binding);
            check(!Eligible(original) && Eligible(ordinary) && !Eligible(survivor) && observations == 1, "Ordinary selection is not exclusive");
            selected = survivor;
            check(Eligible(ordinary) && !Eligible(survivor) && observations == 1, "Selection changed within one evaluation batch");
            Refresh(binding);
            check(!Eligible(original) && !Eligible(ordinary) && Eligible(survivor), "Survivor selection did not take precedence");
            selected = null; Refresh(binding);
            check(!Eligible(original) && !Eligible(ordinary) && !Eligible(survivor), "Explicit suppression left a sibling visible");
            selected = ordinary; Refresh(binding);
            shownAction.Effect = () => selected = survivor;
            // Execute the exact shared native ActionList once through the selected alternate.
            ordinary.OnShow.Run();
            check(shownAction.Calls == 1 && Eligible(ordinary) && !Eligible(survivor) && pageAction.Calls == 0, "OnShow side effect changed selection or duplicated page actions");
            ordinary.OnStop.Run();
            check(stoppedAction.Calls == 1 && stoppedAction.Owner == original, "Alternate lost or reparented OnStop");
            Invalidate(binding);
            check(Eligible(original) && !Eligible(ordinary), "Finished batch left sticky alternate selection");
            foreach (var consumed in new[] { original, ordinary, survivor })
            {
                seen.Add(consumed); Refresh(binding);
                check(!Eligible(original) && !Eligible(ordinary) && !Eligible(survivor), "Consumed sibling replayed through a fresh GUID");
                seen.Clear();
            }
            int count = original.ElementsArray.Count;
            var repeat = Attach(page, original, ordinary, survivor, () => throw new InvalidOperationException("Observation failed"), wasSeen);
            check(ReferenceEquals(repeat, binding) && page.Cues.Count == 5 && original.ElementsArray.Count == count, "Repeated attach duplicates family or guards");
            Refresh(binding);
            check(Eligible(original) && !Eligible(ordinary) && Error(binding) is InvalidOperationException, "Observation failure did not preserve original");
            Attach(page, original, ordinary, survivor, () => ordinary, wasSeen); Refresh(binding);
            check(Error(binding) == null && Eligible(ordinary), "Recovered observation retained failure");
            Attach(page, original, ordinary, survivor, () => before, wasSeen); Refresh(binding);
            check(Error(binding) is InvalidOperationException && Eligible(original), "Unknown selector result hid original");
            Attach(page, original, ordinary, survivor, () => ordinary, (cue, scope) => throw new InvalidOperationException("Seen observation failed")); Refresh(binding);
            check(Error(binding) is InvalidOperationException && Eligible(original), "Seen read failure did not preserve original");
            bool lateFailure = false;
            Attach(page, original, ordinary, survivor, () => ordinary, (cue, scope) => lateFailure ? throw new InvalidOperationException("Late seen failure") : seen.Contains(cue));
            Refresh(binding); lateFailure = true;
            check(!Eligible(ordinary) && !Eligible(survivor) && Eligible(original), "Late read failure cannot fall through to retained original");
            lateFailure = false; Refresh(binding); seen.Add(original);
            check(!Eligible(ordinary) && !Eligible(original), "Original consumed after Refresh replayed through alternate");
            seen.Clear(); Attach(page, original, ordinary, survivor, () => original, wasSeen); Refresh(binding);
            originalChecker.Conditions = new Condition[] { null! };
            check(!Eligible(original), "Original empty-entry OR semantics were replaced");
            originalChecker.Operation = Operation.And;
            check(Eligible(original), "Original AND semantics were replaced");
            var nested = new NestedCondition { Owner = original, Not = true, name = "native-nested" };
            originalChecker.Conditions = new Condition[] { nested };
            check(ReferenceEquals(binding.GetType().GetField("Original", Fields)!.GetValue(binding), originalChecker)
                && nested.Not && nested.Nested.Operation == Operation.Or && nested.Owner == original, "Nested checker identity was flattened or reparented");
            Rejected(() => Attach(page, original, ordinary, ordinary, selector, wasSeen), "Duplicate survivor accepted");
        }

        var plain = new BlueprintCue { AssetGuid = BlueprintGuid.Parse(Guid.NewGuid().ToString("N")), Text = Text("native.plain"),
            Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() }, OnShow = new ActionList(), OnStop = new ActionList(), Continue = new CueSelection() };
        var plainPage = new BlueprintBookPage(); plainPage.Cues.Add(Reference(plain));
        var changedAction = Variant(plain, "bad.action"); changedAction.OnShow = new ActionList();
        Rejected(() => Attach(plainPage, plain, changedAction, null, () => changedAction, (c, local) => false), "Changed native OnShow was accepted");
        var sharedText = Variant(plain, "bad.text"); sharedText.Text = Text("native.plain");
        Rejected(() => Attach(plainPage, plain, sharedText, null, () => sharedText, (c, local) => false), "Shared native localization key was accepted");
        var duplicateId = Variant(plain, "bad.id"); duplicateId.AssetGuid = plain.AssetGuid;
        Rejected(() => Attach(plainPage, plain, duplicateId, null, () => duplicateId, (c, local) => false), "Duplicate blueprint identity was accepted");
        check(plainPage.Cues.Count == 1 && plain.ElementsArray.Count == 0, "Rejected attachment partially mutated the original");
        var plainAlternate = Variant(plain, "plain.alternate");
        var plainBinding = Attach(plainPage, plain, plainAlternate, null, () => plainAlternate, (c, local) => throw new Exception("Repeatable cue must not query seen history"));
        Refresh(plainBinding);
        check(!Eligible(plain) && Eligible(plainAlternate), "Repeatable cue inherited an invented show-once limit");
        var secondAttach = Attach(plainPage, plain, plainAlternate, null, () => plain, (c, local) => false);
        Refresh(secondAttach);
        check(ReferenceEquals(plainBinding, secondAttach) && Eligible(plain) && !Eligible(plainAlternate), "Two-member family was not idempotent");
        plainPage.Cues.Reverse();
        Rejected(() => Attach(plainPage, plain, plainAlternate, null, () => plain, (c, local) => false), "Unknown page reordering was silently accepted");
    }
}
