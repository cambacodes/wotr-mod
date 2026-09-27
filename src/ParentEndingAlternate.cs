using System;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;

namespace Tirabade
{
    // Caller registers variants, supplies private text, and refreshes once per native page evaluation batch.
    internal static class ParentEndingAlternate
    {
        internal static Binding Attach(BlueprintBookPage page, BlueprintCue original,
            BlueprintCueBaseReference ordinaryReference, BlueprintCueBaseReference? survivorReference,
            Func<BlueprintCue?> select, Func<BlueprintCueBase, bool, bool> wasShown)
        {
            if (page == null || original == null || ordinaryReference == null || select == null || wasShown == null)
                throw new ArgumentNullException("A page, original, ordinary variant and observation delegates are required.");
            var ordinary = ordinaryReference.Get() as BlueprintCue ?? throw new ArgumentException("Ordinary reference is not a cue.");
            var survivor = survivorReference?.Get() as BlueprintCue;
            if (survivorReference != null && survivor == null) throw new ArgumentException("Survivor reference is not a cue.");
            if (ReferenceEquals(survivor, original) || ReferenceEquals(survivor, ordinary))
                throw new ArgumentException("Survivor must be a separate cue.");
            var current = original.Conditions;
            if (current?.Conditions?.Length == 1 && current.Conditions[0] is Member guard
                && guard.Index == 0 && current.Operation == Operation.And)
            {
                var prior = guard.Binding;
                if (guard.Not || !ReferenceEquals(guard.Owner, original) || !ReferenceEquals(prior.Members[0], original)
                    || prior.Members.Length != (survivor == null ? 2 : 3)
                    || !ReferenceEquals(prior.Page, page) || !ReferenceEquals(prior.Members[1], ordinary)
                    || !ReferenceEquals(prior.Members.Last(), survivor ?? ordinary))
                    throw new InvalidOperationException("Existing alternate family differs from requested attachment.");
                prior.CheckPosition();
                prior.Select = select;
                prior.WasShown = wasShown;
                prior.Invalidate();
                return prior;
            }
            if (current == null) throw new ArgumentException("Original cue requires its native checker.");
            var members = survivor == null ? new[] { original, ordinary } : new[] { original, ordinary, survivor };
            if (members.Any(c => c.AssetGuid.Equals(default(BlueprintGuid)))
                || members.Select(c => c.AssetGuid).Distinct().Count() != members.Length)
                throw new ArgumentException("Each family member needs a distinct registered blueprint identity.");
            foreach (var variant in members.Skip(1)) ValidateVariant(original, variant);
            if (members.Select(c => c.Text?.Key).Distinct().Count() != members.Length)
                throw new ArgumentException("Each variant needs its own localization key.");
            int index = page.Cues.FindIndex(r => ReferenceEquals(r.Get(), original));
            if (index < 0 || page.Cues.Count(r => ReferenceEquals(r.Get(), original)) != 1)
                throw new ArgumentException("Original must occupy exactly one page position.");
            if (page.Cues.Any(r => members.Skip(1).Any(c => ReferenceEquals(r.Get(), c))))
                throw new ArgumentException("Variant already occurs in this page.");
            var binding = new Binding(page, members, current, select, wasShown);
            for (int i = 0; i < members.Length; i++)
            {
                var member = new Member { Binding = binding, Index = i, Owner = members[i], name = "$ParentEndingAlternate$" + Guid.NewGuid() };
                members[i].ElementsArray.Add(member);
                members[i].Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] { member } };
            }
            page.Cues.Insert(index, ordinaryReference);
            if (survivorReference != null) page.Cues.Insert(index + 1, survivorReference);
            return binding;
        }

        private static void ValidateVariant(BlueprintCue original, BlueprintCue variant)
        {
            if (ReferenceEquals(original.ElementsArray, variant.ElementsArray))
                throw new ArgumentException("Variant must have its own element registration list.");
            if (original.ShowOnce != variant.ShowOnce || original.ShowOnceCurrentDialog != variant.ShowOnceCurrentDialog)
                throw new ArgumentException("Variant changed native show-once policy.");
            if (variant.Text == null || ReferenceEquals(original.Text, variant.Text)
                || string.IsNullOrWhiteSpace(variant.Text.Key) || variant.Text.Key == original.Text?.Key)
                throw new ArgumentException("Variant needs a private localized text key.");
            // Shared behavior objects retain original element ownership and execute only on the selected cue.
            foreach (var field in typeof(BlueprintCue).GetFields(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.DeclaredOnly))
            {
                if (field.Name == nameof(BlueprintCue.Text)) continue;
                var left = field.GetValue(original);
                var right = field.GetValue(variant);
                if (!(field.FieldType.IsValueType ? Equals(left, right) : ReferenceEquals(left, right)))
                    throw new ArgumentException("Variant changed native cue behavior: " + field.Name);
            }
        }

        internal sealed class Binding
        {
            internal readonly BlueprintBookPage Page;
            internal readonly BlueprintCue[] Members;
            internal readonly ConditionsChecker Original;
            internal Func<BlueprintCue?> Select;
            internal Func<BlueprintCueBase, bool, bool> WasShown;
            private int selected;
            internal Exception? LastObservationError { get; private set; }

            internal Binding(BlueprintBookPage page, BlueprintCue[] members, ConditionsChecker original,
                Func<BlueprintCue?> select, Func<BlueprintCueBase, bool, bool> wasShown)
            { Page = page; Members = members; Original = original; Select = select; WasShown = wasShown; }

            // null selection suppresses the whole family. Unknown selections or failed observations preserve original.
            internal void Refresh()
            {
                selected = 0;
                LastObservationError = null;
                try
                {
                    if (Members[0].ShowOnce && Members.Any(c => WasShown(c, Members[0].ShowOnceCurrentDialog)))
                    { selected = -1; return; }
                    var choice = Select();
                    int index = choice == null ? -1 : Array.FindIndex(Members, c => ReferenceEquals(c, choice));
                    if (choice != null && index < 0) throw new InvalidOperationException("Selector returned an unattached cue.");
                    selected = index;
                }
                catch (Exception ex) { LastObservationError = ex; }
            }

            internal void Invalidate() { selected = 0; }

            internal bool Allows(int index)
            {
                if (selected != index) return false;
                try
                {
                    // An earlier cue may consume a sibling after the batch snapshot.
                    if (Members[0].ShowOnce && Members.Any(c => WasShown(c, Members[0].ShowOnceCurrentDialog)))
                    { selected = -1; return false; }
                }
                catch (Exception ex)
                {
                    LastObservationError = ex;
                    selected = 0;
                    // Variants precede original, so a failed late read can still fall through.
                    if (index != 0) return false;
                }
                return Original.Check();
            }

            internal void CheckPosition()
            {
                var ordered = Members.Skip(1).Concat(Members.Take(1)).ToArray();
                int index = Page.Cues.FindIndex(r => ReferenceEquals(r.Get(), ordered[0]));
                if (index < 0 || index + Members.Length > Page.Cues.Count
                    || ordered.Where((c, offset) => !ReferenceEquals(Page.Cues[index + offset].Get(), c)).Any())
                    throw new InvalidOperationException("Attached cue family was reordered or removed.");
            }
        }

        public sealed class Member : Condition
        {
            internal Binding Binding = null!;
            internal int Index;
            protected override string GetConditionCaption() => "Select one earned parent-ending variant";
            protected override bool CheckCondition() => Binding.Allows(Index);
        }
    }
}
