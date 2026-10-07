using System;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

internal static class ParentEndingGuardTests
{
    private sealed class CountCondition : Condition
    {
        internal bool Value;
        internal int Calls;
        protected override string GetConditionCaption() => "Parent fixture";
        protected override bool CheckCondition() { Calls++; return Value; }
    }
    private sealed class CountAction : GameAction
    {
        internal int Calls;
        public override string GetCaption() => "Parent seen arbitration fixture";
        public override void RunAction() { Calls++; }
    }
    internal static void Run(Action<bool, string> check)
    {
        const BindingFlags flags = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
        var service = typeof(Tirabade.Main).Assembly.GetType("Tirabade.ParentEndingGuard", true)!;
        var attach = service.GetMethod("Attach", BindingFlags.Static | BindingFlags.NonPublic)!;
        void Attach(BlueprintCueBase page, Func<bool> available) => attach.Invoke(null, new object[] { page, available });
        // Construction uses actual native page/checker/action classes; parent logic is never flattened.
        foreach (var operation in new[] { Operation.And, Operation.Or })
        {
            var page = new BlueprintBookPage();
            var first = new CountCondition { Value = false, Owner = page, name = "original-first" };
            var second = new CountCondition { Value = true, Not = true, Owner = page, name = "original-second" };
            var original = new ConditionsChecker { Operation = operation, Conditions = new Condition[] { first, second } };
            page.Conditions = original;
            page.ElementsArray.Add(first);
            page.ElementsArray.Add(second);
            var markSeen = new CountAction { Owner = page, name = "original-mark-all-parent-pages" };
            var otherAction = new CountAction { Owner = page, name = "original-other-action" };
            var onShow = new ActionList { Actions = new GameAction[] { markSeen, otherAction } };
            page.OnShow = onShow;
            page.ElementsArray.Add(markSeen);
            page.ElementsArray.Add(otherAction);
            var cues = page.Cues;
            var answers = page.Answers;
            bool replacement = true;
            int observations = 0;
            Attach(page, () => { observations++; return replacement; });
            var guard = page.Conditions.Conditions.Single();
            check(page.Conditions.Operation == Operation.And, "Outer guard must be AND");
            check(ReferenceEquals(guard.GetType().GetField("Original", flags)!.GetValue(guard), original), "Original checker replaced or flattened");
            check(original.Operation == operation && original.Conditions.SequenceEqual(new[] { first, second }), "Original AND/OR ordering changed");
            check(first.Not == false && second.Not && first.Owner == page && second.Owner == page
                && first.name == "original-first" && second.name == "original-second", "Original element identity or negation changed");
            check(guard.Owner == page && page.ElementsArray.Count == 5 && page.ElementsArray.Contains(guard), "Guard owner/elements registration invalid");
            check(!guard.Check() && observations == 1 && first.Calls == 0 && second.Calls == 0,
                "Earned replacement did not short-circuit parent conditions");
            check(ReferenceEquals(page.OnShow, onShow) && onShow.Actions.SequenceEqual(new[] { markSeen, otherAction })
                && markSeen.Calls == 0 && otherAction.Calls == 0, "Attach/check changed or ran parent OnShow actions");
            check(ReferenceEquals(page.Cues, cues) && ReferenceEquals(page.Answers, answers), "Parent story content was rewritten");
            Attach(page, () => false);
            check(ReferenceEquals(page.Conditions.Conditions.Single(), guard) && page.ElementsArray.Count == 5
                && ReferenceEquals(guard.GetType().GetField("Original", flags)!.GetValue(guard), original), "Repeated attachment nested or duplicated guards");
            // Native empty checkers execute headlessly; populated ones enter Unity profiling before evaluating conditions.
            original.Conditions = Array.Empty<Condition>();
            check(guard.Check() == original.Check(), "No replacement changed native empty-checker semantics");
            Attach(page, () => throw new InvalidOperationException("Deliberate unavailable replacement observation"));
            check(guard.Check() == original.Check(), "Failed replacement observation suppressed original empty ending");
            check(guard.GetType().GetProperty("LastObservationError", flags)!.GetValue(guard) is InvalidOperationException,
                "Replacement observation error was discarded");
            Attach(page, () => false);
            check(guard.Check() && guard.GetType().GetProperty("LastObservationError", flags)!.GetValue(guard) == null,
                "Recovered observation retained stale failure");
            // Null entries execute native AND/OR combination and final result without entering Unity-dependent condition profiling.
            original.Conditions = new Condition[] { null! };
            check(guard.Check() == original.Check() && guard.Check() == (operation == Operation.And),
                "False replacement changed native AND/OR final semantics");
            Attach(page, () => throw new InvalidOperationException("Deliberate observation failure"));
            check(guard.Check() == original.Check(), "Observation failure changed native AND/OR result");
            check(markSeen.Calls == 0 && otherAction.Calls == 0, "Evaluation invoked parent seen bookkeeping");
        }
        var cue = new BlueprintCue();
        var cueOriginal = new ConditionsChecker { Conditions = Array.Empty<Condition>() };
        cue.Conditions = cueOriginal;
        var cueOnShow = new ActionList { Actions = Array.Empty<GameAction>() };
        var cueOnStop = new ActionList { Actions = Array.Empty<GameAction>() };
        cue.OnShow = cueOnShow;
        cue.OnStop = cueOnStop;
        var continuation = new CueSelection();
        cue.Continue = continuation;
        Attach(cue, () => true);
        check(!cue.Conditions.Conditions.Single().Check(), "Exact relationship cue cannot be suppressed independently");
        check(ReferenceEquals(cue.OnShow, cueOnShow) && ReferenceEquals(cue.OnStop, cueOnStop)
            && ReferenceEquals(cue.Continue, continuation), "Cue actions or continuation changed");
        Attach(cue, () => false);
        check(cue.Conditions.Conditions.Single().Check() && cue.ElementsArray.Count == 1,
            "Parent-only relationship cue was suppressed or duplicate guard attached");
        var noConditions = new BlueprintBookPage();
        Attach(noConditions, () => false);
        check(noConditions.Conditions.Conditions.Single().Check(), "Absent parent condition was rejected");
        Attach(noConditions, () => true);
        check(!noConditions.Conditions.Conditions.Single().Check(), "Replacement cannot suppress unconditioned parent page");
    }
}

