using System;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace Tirabade
{
    // Wrap the existing checker intact; replacement eligibility belongs to the caller's earned story state.
    internal static class ParentEndingGuard
    {
        internal static void Attach(BlueprintCueBase cue, Func<bool> replacementAvailable)
        {
            if (cue == null) throw new ArgumentNullException(nameof(cue));
            if (replacementAvailable == null) throw new ArgumentNullException(nameof(replacementAvailable));
            var current = cue.Conditions;
            if (current?.Conditions?.Length == 1 && current.Conditions[0] is Guard existing
                && ReferenceEquals(existing.Owner, cue) && current.Operation == Operation.And)
            {
                existing.ReplacementAvailable = replacementAvailable;
                return;
            }
            var guard = new Guard
            {
                Original = current,
                ReplacementAvailable = replacementAvailable,
                Owner = cue,
                name = "$ParentEndingGuard$" + Guid.NewGuid()
            };
            cue.ElementsArray.Add(guard);
            cue.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] { guard } };
        }

        public sealed class Guard : Condition
        {
            internal ConditionsChecker? Original;
            internal Func<bool> ReplacementAvailable = null!;
            internal Exception? LastObservationError { get; private set; }
            protected override string GetConditionCaption() => "Preserve parent ending unless an earned replacement applies";
            protected override bool CheckCondition()
            {
                bool replaced = false;
                LastObservationError = null;
                try { replaced = ReplacementAvailable(); }
                catch (Exception ex) { LastObservationError = ex; }
                return !replaced && (Original?.Check() ?? true);
            }
        }
    }
}
