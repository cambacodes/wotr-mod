using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Reflection.Emit;
using HarmonyLib;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Controllers.Dialog;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;

namespace Tirabade
{
    internal sealed class ParentEndingIntegration
    {
        private const string OrdinaryOwner = "Epilogue";
        private const string NativePairPage = "5c95d8e3fa4f3b44896914987cb04b0b";
        private const string NativeSpecialSequence = "f8d7f50e3bb88c143834d234c0b24474";
        private static readonly Dictionary<string, (string Page, string Key)> Evidence = new Dictionary<string, (string, string)>
        {
            ["26789d87b5a44ba988079b4842bad81c"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0001.Text"),
            ["e87b43c31c1c4253a7137c7d6c05b246"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0002.Text"),
            ["819314e916514a498a8e336371b4788e"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0003.Text"),
            ["9bfbb3f217ca476cadbeffc4d389717d"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0004.Text"),
            ["e0551b6120c94d70aa9d10a5fcc4ec86"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0005.Text"),
            ["7edf5529523a4a9da520138783fdeb93"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0006.Text"),
            ["d6b960c14e37492682de6284af1c5417"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0007.Text"),
            ["19fd9027465f4cbebe949b26d04a2826"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0008.Text"),
            ["84e26e3c483c4e7985ac656de08a5b05"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0009.Text"),
            ["f5e580bedafc43f3acb6843fd71d8120"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0000.Text"),
            ["59cf28c3824944fd88547bc61bc5cf62"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0011.Text"),
            ["92162854b221413984468d2663ffcffb"] = ("951e4432cf844a36a8a222b27589fb43", "RanRomMinaSlide0001Cue0012.Text"),
            ["417936bb80bc48f28e1f0cee032d9ab6"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0001.Text"),
            ["6eba6f627ac34cf4955c89e5ad59e106"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0002.Text"),
            ["a875684118e64d7ab29f70ca3460c365"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0003.Text"),
            ["9a5eb7aff04943c28da2260aac68874e"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0004.Text"),
            ["a259e48a6513439483a2d8f31ea7ff39"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0005.Text"),
            ["9806218e467f41acb502b52160ab38dd"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0006.Text"),
            ["cce5f180fbe7455989544c1c81428463"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0007.Text"),
            ["829c837c76f6429fa01d3d2583069b35"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0008.Text"),
            ["f9ec524d3ff04b999afc1e8bfe50ae4e"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0009.Text"),
            ["3b8d47b3c9694002aff26510ac4dedf0"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0000.Text"),
            ["51104e1c8755436e8aa290a6cedfcb3a"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0011.Text"),
            ["fb32a8f9c464496abe90307c68ec271e"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0012.Text"),
            ["222f780971834ea28357b2533f921e9d"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0013.Text"),
            ["a77e415c6eb44d719839e07a3f164d87"] = ("6db8635856e74b6cac46330bd82b4ff5", "RanRomMinaSlide0002Cue0014.Text"),
            ["5570b60904f34d29ab925ef19757f024"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0001.Text"),
            ["0a8411c2cb0a44f1ab317ed425f6ec94"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0002.Text"),
            ["5ab5c6a3c62b4f2ba88053cbbbc47737"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0003.Text"),
            ["dc14cdafb9fa43e8bc3b0816626b3dbe"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0004.Text"),
            ["2741346e336e4c3899748e51bf103460"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0005.Text"),
            ["acb0d15ef71c410484b7c37b270e30fe"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0006.Text"),
            ["f37b7a5fcff84551b86ecbba823e2fa5"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0007.Text"),
            ["982627a0bbd34fe4b16b5b078e56355a"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0008.Text"),
            ["02fd8486e8e44191ab01cf914087a00e"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0009.Text"),
            ["67e3bb3b649d42a4a84115f3c7ac6bf1"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0000.Text"),
            ["2c5edf138eac4848940d8ebbafe1535d"] = ("8df5edb6f69040c69d7da78d2bf20cb6", "RanRomMinaSlide0003Cue0011.Text"),
            ["a7d2f947a47e40bc9d7c0c24da1b9be3"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0001.Text"),
            ["286434b491b74174a97dfd2d7344f57a"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0002.Text"),
            ["784575a522e64ad58f2171abcb073d0c"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0003.Text"),
            ["5db846019acd46ef83f12be220727f50"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0004.Text"),
            ["1f1d17818c9f4057be26e47d1632e2c6"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0005.Text"),
            ["3d4137f1cf98459f996ef1da83737cdb"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0006.Text"),
            ["9e3bd8247f0c40eba62368fe2912bb84"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0007.Text"),
            ["18d22b6258a24fe29dd9d0ea4235432e"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0008.Text"),
            ["8c6accdc29f54a428d3a59786c1c856d"] = ("5a5865ceca0e42049288351a76b18ba9", "RanRomMinaSlide0004Cue0009.Text"),
            ["7d970543808f428380fb1042b32f896e"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0001.Text"),
            ["a1774d0a9fb34fd2ac58abc1c6db55bd"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0002.Text"),
            ["d47984953fc74c488ef0a02588bde92b"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0003.Text"),
            ["b474eb4460cb42729be2717d05e7d42b"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0004.Text"),
            ["f6d5d9bfdf1442528be5e6d81b656ac2"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0005.Text"),
            ["2cd9538f67f7414d808d9032386f6be9"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0006.Text"),
            ["8009e775a3a343c79ef4e40d72bc5e6a"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0007.Text"),
            ["5b0a132d97404072b3d664899871d7b7"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0008.Text"),
            ["a200043a0b9a4d97a0da3fea0c0890a1"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0009.Text"),
            ["0b1b31d7125547219daa747eba45a063"] = ("126762ac92364ac5bdec69c6e3fdfd1a", "RanRomMinaSlide0005Cue0000.Text"),
            ["56f4e95390ec472b855e759fbc548b81"] = ("01677da8df6e42c6b4803ceef524b1fe", "RanRomMinaSlide0006Cue0001.Text"),
            ["85b479a3da8a4fa6b602fedf89201695"] = ("01677da8df6e42c6b4803ceef524b1fe", "RanRomMinaSlide0006Cue0002.Text"),
            ["64afcd565e044e53977e1878444f4ee1"] = ("01677da8df6e42c6b4803ceef524b1fe", "RanRomMinaSlide0006Cue0003.Text"),
            ["b9e2550bc7244f6c8480106b41667d96"] = ("01677da8df6e42c6b4803ceef524b1fe", "RanRomMinaSlide0006Cue0004.Text"),
            ["bb49f54dc0a547c287238b5d7d8489b3"] = ("01677da8df6e42c6b4803ceef524b1fe", "RanRomMinaSlide0006Cue0005.Text"),
            ["5831af75932d43ed902a2d8def2adf3d"] = ("01677da8df6e42c6b4803ceef524b1fe", "RanRomMinaSlide0006Cue0006.Text"),
            ["7b56a6e716ce4aacaae1060fb33c3a0f"] = ("9c5c5825bf3245d0ae763c6e69ecdc38", "RanRomMinaSlide0007Cue0001.Text"),
            ["8399dbc5987b462594b2b4168764e269"] = ("9c5c5825bf3245d0ae763c6e69ecdc38", "RanRomMinaSlide0007Cue0002.Text"),
            ["d6714bd8d48e425d862f854018cb123c"] = ("9c5c5825bf3245d0ae763c6e69ecdc38", "RanRomMinaSlide0007Cue0003.Text"),
            ["ff2042ad95e14b73a5f75f2cfd84b5e4"] = ("9c5c5825bf3245d0ae763c6e69ecdc38", "RanRomMinaSlide0007Cue0004.Text"),
            ["dce10a002c5c4e83838d1b85096b2d15"] = ("3792457f35734d75a4d4b53055f7f5d0", "RanRomMinaSlide0008Cue0001.Text"),
            ["1980e50e5e204431bf643fbad487909f"] = ("3792457f35734d75a4d4b53055f7f5d0", "RanRomMinaSlide0008Cue0002.Text"),
            ["bf05f030b0044487bca43db8296dfe31"] = ("3792457f35734d75a4d4b53055f7f5d0", "RanRomMinaSlide0008Cue0003.Text"),
            ["c47829fba057400c8e0279990be3d25e"] = ("3792457f35734d75a4d4b53055f7f5d0", "056942f6-32d0-4480-8ff7-29356b43db19"),
            ["5787f92575364c1459df8f075676c2db"] = ("5c95d8e3fa4f3b44896914987cb04b0b", "056942f6-32d0-4480-8ff7-29356b43db19"),
        };
        private readonly Story story;
        private readonly Func<Snapshot?> observe;
        private readonly Dictionary<BlueprintBookPage, PagePlan> plans = new Dictionary<BlueprintBookPage, PagePlan>();
        private readonly List<CuePlan> cues = new List<CuePlan>();
        private bool attached;
        internal Exception? LastObservationError { get; private set; }
        private static ParentEndingIntegration? active;
        private static readonly List<Scope> scopes = new List<Scope>();
        private static readonly MethodInfo Play = AccessTools.Method(typeof(DialogController), "PlayBookPage", new[] { typeof(BlueprintBookPage) });
        private static readonly MethodInfo Preview = AccessTools.Method(typeof(DialogController), "CanShowAnyCue", new[] { typeof(BlueprintBookPage) });
        private const string HarmonyId = "RanRomance.Tirabade.ParentEndings";

        private sealed class PagePlan
        {
            internal BlueprintBookPage Page = null!;
            internal ConditionsChecker Original = null!;
            internal BlueprintCueBaseReference[] OriginalCues = null!;
            internal int Elements;
            internal Snapshot? State;
            internal bool Evaluating;
            internal readonly List<ParentEndingAlternate.Binding> Bindings = new List<ParentEndingAlternate.Binding>();
        }
        private sealed class CuePlan
        {
            internal BlueprintCue Original = null!;
            internal PagePlan Page = null!;
            internal ConditionsChecker Checker = null!;
            internal int Elements;
            internal BlueprintCue? Ordinary;
            internal BlueprintCue? Survivor;
        }
        internal sealed class Scope
        {
            internal BlueprintBookPage Page = null!;
            internal bool Playing;
            internal bool Owns;
            internal bool Closed;
        }

        internal static ParentEndingIntegration? Prepare(Story story, BlueprintCueSequence ordinary, BlueprintCueSequence aeon,
            Func<string, SimpleBlueprint> resolve, Func<string, BlueprintCue> register, Func<Snapshot?> observe)
        {
            if (story.ParentEpilogueEdits.Count == 0 && story.ParentEpilogueLossRules.Count == 0) return null;
            var result = new ParentEndingIntegration(story, observe);
            var pageIds = story.ParentEpilogueLossRules.SelectMany(rule => rule.SuppressPages)
                .Concat(story.ParentEpilogueEdits.Keys.Concat(story.ParentEpilogueLossRules.SelectMany(rule => rule.SuppressCues))
                    .Select(id => Evidence.TryGetValue(id, out var evidence) ? evidence.Page : throw new InvalidOperationException("Unreviewed parent cue: " + id)))
                .Distinct().ToArray();
            var reviewedPages = new HashSet<string>(Evidence.Values.Select(value => value.Page));
            foreach (string id in pageIds)
            {
                var sequence = id == NativePairPage ? resolve(NativeSpecialSequence) as BlueprintCueSequence : ordinary;
                if (!reviewedPages.Contains(id) || !(resolve(id) is BlueprintBookPage page)
                    || sequence == null || sequence.Cues.Count(reference => ReferenceEquals(reference.Get(), page)) != 1
                    || aeon.Cues.Any(reference => ReferenceEquals(reference.Get(), page))
                    || page.Conditions == null || page.Cues.Any(reference => reference.Get() == null)
                    || page.ShowOnce != (id != NativePairPage) || page.ShowOnceCurrentDialog)
                    throw new InvalidOperationException("Unreviewed parent page identity, timeline or policy: " + id);
                result.plans.Add(page, new PagePlan { Page = page, Original = page.Conditions,
                    OriginalCues = page.Cues.ToArray(), Elements = page.ElementsArray.Count });
            }
            foreach (string id in story.ParentEpilogueEdits.Keys.Concat(story.ParentEpilogueLossRules.SelectMany(rule => rule.SuppressCues)).Distinct())
            {
                var evidence = Evidence[id];
                if (!(resolve(id) is BlueprintCue cue) || cue.Text?.Key != evidence.Key)
                    throw new InvalidOperationException("Unreviewed original parent cue text: " + id);
                var page = result.plans.Values.Single(plan => plan.Page.AssetGuid.ToString() == evidence.Page);
                if (page.Page.Cues.Count(reference => ReferenceEquals(reference.Get(), cue)) != 1
                    || result.plans.Values.Where(plan => !ReferenceEquals(plan, page)).Any(plan => plan.Page.Cues.Any(reference => ReferenceEquals(reference.Get(), cue))))
                    throw new InvalidOperationException("Original cue moved from its reviewed page: " + id);
                ValidateCue(cue, evidence.Page == NativePairPage);
                if (story.ParentEpilogueEdits.TryGetValue(id, out var edit) && edit.ParentKey != cue.Text.Key)
                    throw new InvalidOperationException("Authored original localization evidence differs: " + id);
                result.cues.Add(new CuePlan { Original = cue, Page = page, Checker = cue.Conditions, Elements = cue.ElementsArray.Count });
            }
            // No originals have been changed. Reject incompatible native hooks before registering variants.
            EnsureHooks();
            foreach (var plan in result.cues)
            {
                string id = plan.Original.AssetGuid.ToString();
                if (story.ParentEpilogueEdits.TryGetValue(id, out var edit) && edit.Text != null)
                    plan.Ordinary = RegisterVariant(register, edit);
                var survivors = story.ParentEpilogueLossRules.Where(rule => rule.SurvivorAlternates.ContainsKey(id)).ToArray();
                if (survivors.Length > 1 || survivors.Length == 1 && plan.Ordinary == null)
                    throw new InvalidOperationException("Unreviewed survivor family: " + id);
                if (survivors.Length == 1) plan.Survivor = RegisterVariant(register, survivors[0].SurvivorAlternates[id]);
            }
            return result;
        }

        private ParentEndingIntegration(Story story, Func<Snapshot?> observe) { this.story = story; this.observe = observe; }

        private static BlueprintCue RegisterVariant(Func<string, BlueprintCue> register, ParentEndingText text)
        {
            var cue = register("parent-ending." + text.LocalizedKey);
            // Bare until Main's generic owner pass finishes; no shared action/condition objects yet.
            cue.Conditions = new ConditionsChecker { Conditions = Array.Empty<Condition>() };
            cue.OnShow = new ActionList { Actions = Array.Empty<GameAction>() };
            cue.OnStop = new ActionList { Actions = Array.Empty<GameAction>() };
            LocalizationManager.CurrentPack.PutString(text.LocalizedKey, text.Text!);
            cue.Text = new LocalizedString();
            AccessTools.Field(typeof(LocalizedString), "m_Key").SetValue(cue.Text, text.LocalizedKey);
            return cue;
        }

        private static void ValidateCue(BlueprintCue cue, bool nativePair)
        {
            // The reviewed targets have no per-cue actions, answers or continuation.
            // Reject additions rather than assume original-self-seen actions survive a new cue GUID.
            if (cue.Conditions == null || cue.ComponentsArray.Length != 0 || cue.OnShow?.Actions == null || cue.OnShow.Actions.Length != 0
                || cue.OnStop?.Actions == null || cue.OnStop.Actions.Length != 0 || cue.Continue?.Cues == null || cue.Continue.Cues.Count != 0
                || cue.Answers == null || cue.Answers.Count != 0 || cue.ShowOnce != !nativePair || cue.ShowOnceCurrentDialog)
                throw new InvalidOperationException("Unreviewed parent cue behavior or self-seen dependency: " + cue.AssetGuid);
        }

        internal void Attach()
        {
            if (attached) return;
            // Recheck every original before mutating any; Main has initialized only the bare variants.
            foreach (var plan in cues)
            {
                ValidateCue(plan.Original, plan.Page.Page.AssetGuid.ToString() == NativePairPage);
                if (!ReferenceEquals(plan.Original.Conditions, plan.Checker) || plan.Original.ElementsArray.Count != plan.Elements
                    || plan.Original.Text?.Key != Evidence[plan.Original.AssetGuid.ToString()].Key)
                    throw new InvalidOperationException("Parent cue changed during registration.");
            }
            foreach (var plan in plans.Values)
                if (!ReferenceEquals(plan.Page.Conditions, plan.Original) || !plan.Page.Cues.SequenceEqual(plan.OriginalCues)
                    || plan.Page.ElementsArray.Count != plan.Elements)
                    throw new InvalidOperationException("Parent page changed during registration.");
            try
            {
                foreach (var plan in cues)
                {
                    foreach (var variant in new[] { plan.Ordinary, plan.Survivor }.Where(cue => cue != null))
                    {
                        var text = variant!.Text;
                        foreach (var field in typeof(BlueprintCue).GetFields(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.DeclaredOnly))
                            field.SetValue(variant, field.GetValue(plan.Original));
                        variant.Text = text;
                        variant.ShowOnce = plan.Original.ShowOnce;
                        variant.ShowOnceCurrentDialog = plan.Original.ShowOnceCurrentDialog;
                    }
                    if (plan.Ordinary != null)
                        plan.Page.Bindings.Add(ParentEndingAlternate.Attach(plan.Page.Page, plan.Original, Reference(plan.Ordinary),
                            plan.Survivor == null ? null : Reference(plan.Survivor), () => Select(plan), WasShown));
                    else ParentEndingGuard.Attach(plan.Original, () => Decision(plan) == ParentEndingSelection.Suppress);
                }
                foreach (var plan in plans.Values)
                    ParentEndingGuard.Attach(plan.Page, () => PageSuppressed(plan));
                attached = true;
                active = this;
            }
            catch
            {
                foreach (var plan in cues)
                {
                    plan.Original.Conditions = plan.Checker;
                    plan.Original.ElementsArray.RemoveRange(plan.Elements, plan.Original.ElementsArray.Count - plan.Elements);
                }
                foreach (var plan in plans.Values)
                {
                    plan.Page.Conditions = plan.Original;
                    plan.Page.Cues.Clear(); plan.Page.Cues.AddRange(plan.OriginalCues);
                    plan.Page.ElementsArray.RemoveRange(plan.Elements, plan.Page.ElementsArray.Count - plan.Elements);
                    plan.Bindings.Clear();
                }
                throw;
            }
        }

        private static BlueprintCueBaseReference Reference(BlueprintCue cue)
        {
            var reference = new BlueprintCueBaseReference();
            AccessTools.Field(typeof(BlueprintReferenceBase), "deserializedGuid").SetValue(reference, cue.AssetGuid);
            return reference;
        }
        private static bool WasShown(BlueprintCueBase cue, bool local) => local
            ? Game.Instance.DialogController.LocalShownCues.Contains(cue) : Game.Instance.Player.Dialog.ShownCues.Contains(cue);
        private ParentEndingSelection Decision(CuePlan plan) => plan.Page.State == null ? ParentEndingSelection.Original
            : Rules.ParentEndingCue(story, plan.Page.Page.AssetGuid.ToString(), plan.Original.AssetGuid.ToString(), OrdinaryOwner, plan.Page.State, out _);
        private BlueprintCue? Select(CuePlan plan)
        {
            switch (Decision(plan))
            {
                case ParentEndingSelection.Suppress: return null;
                case ParentEndingSelection.Ordinary: return plan.Ordinary;
                case ParentEndingSelection.Survivor: return plan.Survivor;
                default: return plan.Original;
            }
        }
        private Snapshot? Observe()
        {
            if (Harmony.HasAnyPatches("RanEpilogue"))
            {
                LastObservationError = new InvalidOperationException("RanEpilogue uses an unverified replacement delivery sequence; preserving original parent endings.");
                return null;
            }
            return observe();
        }

        private bool PageSuppressed(PagePlan plan)
        {
            var state = plan.Evaluating ? plan.State : Observe();
            return state != null && Rules.ParentEndingPageSuppressed(story, plan.Page.AssetGuid.ToString(), OrdinaryOwner, state);
        }
        private void Refresh(PagePlan plan)
        {
            plan.State = null;
            plan.Evaluating = true;
            LastObservationError = null;
            try { plan.State = Observe(); }
            catch (Exception ex) { LastObservationError = ex; }
            foreach (var binding in plan.Bindings) binding.Refresh();
        }
        internal static Scope? Begin(BlueprintBookPage page, bool playing)
        {
            if (active == null || !active.plans.TryGetValue(page, out var plan)) return null;
            var scope = new Scope { Page = page, Playing = playing, Owns = !scopes.Any(prior => ReferenceEquals(prior.Page, page) && !prior.Closed) };
            scopes.Add(scope);
            if (scope.Owns && !playing) active.Refresh(plan);
            return scope;
        }
        internal static void AfterPageShow(BlueprintBookPage page)
        {
            var scope = scopes.LastOrDefault(item => ReferenceEquals(item.Page, page) && item.Playing && !item.Closed);
            if (scope?.Owns == true && active != null) active.Refresh(active.plans[page]);
        }
        internal static void End(Scope? scope)
        {
            if (scope == null || scope.Closed) return;
            scope.Closed = true;
            scopes.Remove(scope);
            if (scope.Owns && active != null && active.plans.TryGetValue(scope.Page, out var plan))
            {
                plan.State = null;
                plan.Evaluating = false;
                foreach (var binding in plan.Bindings) binding.Invalidate();
            }
        }

        private static void PreviewPrefix(BlueprintBookPage page, out Scope? __state) { __state = Begin(page, false); }
        private static void PlayPrefix(BlueprintBookPage page, out Scope? __state) { __state = Begin(page, true); }
        private static void Finished(Scope? __state) { End(__state); }
        private static Exception? Finalized(Exception? __exception, Scope? __state) { End(__state); return __exception; }

        internal static IEnumerable<CodeInstruction> Transpile(IEnumerable<CodeInstruction> instructions)
        {
            var result = instructions.Select(instruction => new CodeInstruction(instruction)).ToList();
            var show = AccessTools.Field(typeof(BlueprintBookPage), nameof(BlueprintBookPage.OnShow));
            var run = AccessTools.Method(typeof(ActionList), nameof(ActionList.Run));
            var matches = Enumerable.Range(0, Math.Max(0, result.Count - 1)).Where(index => result[index].opcode == OpCodes.Ldfld
                && Equals(result[index].operand, show) && result[index + 1].Calls(run)).ToArray();
            if (matches.Length != 1 || matches[0] + 2 >= result.Count || result[matches[0] + 1].blocks.Count != 0
                || result[matches[0] + 2].blocks.Count != 0)
                throw new InvalidOperationException("Native PlayBookPage OnShow boundary differs from the reviewed hook.");
            int insert = matches[0] + 2;
            var load = new CodeInstruction(OpCodes.Ldarg_1);
            result.InsertRange(insert, new[] { load, new CodeInstruction(OpCodes.Call, AccessTools.Method(typeof(ParentEndingIntegration), nameof(AfterPageShow))) });
            return result;
        }
        private static void EnsureHooks()
        {
            var transpiler = AccessTools.Method(typeof(ParentEndingIntegration), nameof(Transpile));
            bool Patched(MethodInfo method, string prefix)
            {
                var info = Harmony.GetPatchInfo(method);
                return info != null && info.Prefixes.Any(patch => patch.owner == HarmonyId && patch.PatchMethod == AccessTools.Method(typeof(ParentEndingIntegration), prefix))
                    && info.Postfixes.Any(patch => patch.owner == HarmonyId && patch.PatchMethod == AccessTools.Method(typeof(ParentEndingIntegration), nameof(Finished)))
                    && info.Finalizers.Any(patch => patch.owner == HarmonyId && patch.PatchMethod == AccessTools.Method(typeof(ParentEndingIntegration), nameof(Finalized)));
            }
            if (Patched(Play, nameof(PlayPrefix)) && Patched(Preview, nameof(PreviewPrefix))
                && Harmony.GetPatchInfo(Play)?.Transpilers.Any(patch => patch.owner == HarmonyId && patch.PatchMethod == transpiler) == true) return;
            // Validate original IL before installing either hook; patched IL is checked again by Transpile.
            Transpile(PatchProcessor.GetOriginalInstructions(Play)).ToArray();
            var harmony = new Harmony(HarmonyId);
            harmony.UnpatchAll(HarmonyId);
            HarmonyMethod Method(string name) => new HarmonyMethod(AccessTools.Method(typeof(ParentEndingIntegration), name));
            try
            {
                harmony.Patch(Preview, prefix: Method(nameof(PreviewPrefix)), postfix: Method(nameof(Finished)), finalizer: Method(nameof(Finalized)));
                harmony.Patch(Play, prefix: Method(nameof(PlayPrefix)), postfix: Method(nameof(Finished)), finalizer: Method(nameof(Finalized)), transpiler: new HarmonyMethod(transpiler));
            }
            catch { harmony.UnpatchAll(HarmonyId); throw; }
        }
    }
}
