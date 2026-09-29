using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.UI.MVVM._PCView.Dialog.BookEvent;
using Kingmaker.UI.MVVM._PCView.Dialog.Dialog;
using Kingmaker.UI.MVVM._VM.Dialog.BookEvent;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace Tirabade
{
    public static partial class Main
    {
        // E15b: book-page polish for RRT pages only. A native Owlcat book page is left exactly as the game built it: every
        // change is recorded and restored the moment a non-RRT page binds.
        //   1. the paper overlay drawn over the illustration is thinned to at most 15% (our art is full colour; the native
        //      paintings are made to sit under it);
        //   2. on a short page the answers follow the text instead of being pinned to the foot of the page;
        //   3. a speaker who is not the page's owner gets a small name caption over the illustration.
        internal static class BookPolish
        {
            internal const float OverlayMaxAlpha = 0.15f;
            internal const int ShortPageChars = 700;
            internal const float LetterPortraitScale = 0.6f;
            internal static readonly Color LetterTint = new Color(1f, 0.96f, 0.88f, 1f);

            internal static readonly Type ViewType = typeof(BookEventPCView).BaseType!;
            internal static readonly FieldInfo? PictureField = AccessTools.Field(ViewType, "m_Picture");
            internal static readonly FieldInfo? CuesLayoutField = AccessTools.Field(ViewType, "m_CuesLayoutGroup");
            internal static readonly FieldInfo? CueViewField = AccessTools.Field(ViewType, "m_CueView");

            private static readonly Dictionary<Graphic, Color> savedColors = new Dictionary<Graphic, Color>();
            private static readonly Dictionary<LayoutElement, float> savedFlex = new Dictionary<LayoutElement, float>();
            private static readonly Dictionary<RectTransform, Vector3> savedScale = new Dictionary<RectTransform, Vector3>();
            private static readonly Dictionary<Image, bool> savedAspect = new Dictionary<Image, bool>();
            private static readonly List<Outline> addedFrames = new List<Outline>();
            private static GameObject? captionRoot;
            private static TextMeshProUGUI? captionText;
            private static bool dumped;

            // Headless builds (managed tests) have no mod entry; logging is best effort.
            private static void Log(string message) { try { entry?.Logger.Log(message); } catch { } }

            // The paper overlay keeps its native alpha when that is already light; a heavier one is thinned to 15%.
            internal static float OverlayAlpha(float native) => Math.Min(native, OverlayMaxAlpha);

            // A page whose text fits comfortably on one page (well under the paginator's capacity) is "short".
            internal static bool IsShortPage(IEnumerable<string> texts) => texts.Sum(t => t?.Length ?? 0) < ShortPageChars;

            // The caption names a speaker who is neither the narrator, the pair ("Together") nor the page's owner.
            internal static string? CaptionFor(string? speaker, string? owner)
            {
                if (string.IsNullOrEmpty(speaker) || owner == null) return null;
                if (speaker == "Narrator" || speaker == "Together" || speaker == owner) return null;
                return speaker;
            }

            // E15b letters: a remote scene is correspondence. Its page is headed "Letter from <Owner>" (or "A parcel from
            // <Owner>"). Epilogue pages and memories are not letters.
            internal static string? LetterHeader(Scene scene)
            {
                if (!Rules.IsRemote(scene) || scene.Owner.EndsWith("Epilogue", StringComparison.Ordinal) || scene.Owner == "Memory") return null;
                string sender = scene.Owner == "Together" ? "Anevia and Irabeth" : scene.Owner;
                return (scene.Parcel ? "A parcel from " : "Letter from ") + sender;
            }

            internal static string PageTitle(Scene scene) =>
                LetterHeader(scene) is string header ? (scene.Title.Length > 0 ? header + ": " + scene.Title : header) : scene.Title;

            internal static bool IsLetterPage(string guid) => letterPages.Contains(guid);

            internal static bool IsRrtPage(BlueprintBookPage? page, out Node? node, out string? owner)
            {
                node = null; owner = null;
                if (page == null) return false;
                string guid = page.AssetGuid.ToString();
                if (!pages.TryGetValue(guid, out var n)) return false;
                node = n;
                pageOwners.TryGetValue(guid, out owner);
                return true;
            }

            private static BlueprintBookPage? Page(object view) =>
                (Traverse.Create(view).Property("ViewModel").GetValue() as BookEventVM)?.BlueprintBookPage?.Value;

            private static void Restore()
            {
                foreach (var pair in savedColors) if (pair.Key != null) pair.Key.color = pair.Value;
                savedColors.Clear();
                foreach (var pair in savedFlex) if (pair.Key != null) pair.Key.flexibleHeight = pair.Value;
                savedFlex.Clear();
                foreach (var pair in savedScale) if (pair.Key != null) pair.Key.localScale = pair.Value;
                savedScale.Clear();
                foreach (var pair in savedAspect) if (pair.Key != null) pair.Key.preserveAspect = pair.Value;
                savedAspect.Clear();
                foreach (var frame in addedFrames) if (frame != null) UnityEngine.Object.Destroy(frame);
                addedFrames.Clear();
                if (captionRoot != null) captionRoot.SetActive(false);
            }

            // True when b is drawn after a (later in hierarchy order, so on top within one canvas).
            private static bool DrawnAfter(Transform a, Transform b)
            {
                var pa = Path(a); var pb = Path(b);
                for (int i = 0; i < Math.Min(pa.Count, pb.Count); i++)
                    if (pa[i] != pb[i]) return pb[i] > pa[i];
                return pb.Count > pa.Count; // a descendant of a draws after a
            }

            private static List<int> Path(Transform t)
            {
                var path = new List<int>();
                for (var x = t; x != null; x = x.parent) path.Insert(0, x.GetSiblingIndex());
                return path;
            }

            private static float Overlap(RectTransform a, RectTransform b)
            {
                var ca = new Vector3[4]; var cb = new Vector3[4];
                a.GetWorldCorners(ca); b.GetWorldCorners(cb);
                float w = Math.Max(0, Math.Min(ca[2].x, cb[2].x) - Math.Max(ca[0].x, cb[0].x));
                float h = Math.Max(0, Math.Min(ca[2].y, cb[2].y) - Math.Max(ca[0].y, cb[0].y));
                float area = (ca[2].x - ca[0].x) * (ca[2].y - ca[0].y);
                return area <= 0 ? 0 : w * h / area;
            }

            private static void Dump(Image picture)
            {
                if (dumped) return;
                dumped = true;
                var root = picture.transform.parent != null ? picture.transform.parent : picture.transform;
                foreach (var g in root.GetComponentsInChildren<Graphic>(true))
                    Log("E15b book picture layer: " + g.name + " (" + g.GetType().Name + ") alpha " + g.color.a.ToString("0.00")
                        + (g == picture ? " [picture]" : DrawnAfter(picture.transform, g.transform) ? " [over]" : " [under]")
                        + " overlap " + Overlap(picture.rectTransform, g.rectTransform).ToString("0.00"));
            }

            internal static void ApplyPicture(object view)
            {
                try
                {
                    Restore();
                    if (!IsRrtPage(Page(view), out var node, out var owner)) return;
                    if (!(PictureField?.GetValue(view) is Image picture)) return;
                    Dump(picture);
                    // Our illustration at full strength.
                    if (picture.color.a < 1f) { savedColors[picture] = picture.color; picture.color = new Color(picture.color.r, picture.color.g, picture.color.b, 1f); }
                    // Thin any paper layer drawn over the illustration (not text, not the picture itself).
                    var root = picture.transform.parent != null ? picture.transform.parent : picture.transform;
                    foreach (var g in root.GetComponentsInChildren<Graphic>(true))
                    {
                        if (g == picture || g is TMP_Text || g is Text) continue;
                        if (!DrawnAfter(picture.transform, g.transform) || Overlap(picture.rectTransform, g.rectTransform) < 0.5f) continue;
                        float alpha = OverlayAlpha(g.color.a);
                        if (alpha >= g.color.a) continue;
                        savedColors[g] = g.color;
                        g.color = new Color(g.color.r, g.color.g, g.color.b, alpha);
                    }
                    var bookPage = Page(view);
                    if (bookPage != null && IsLetterPage(bookPage.AssetGuid.ToString()))
                    {
                        // Correspondence: the sender's portrait sits smaller, framed like a miniature pinned to the letter, on a
                        // warm paper tint, signed below. In-person pages keep the full illustration.
                        var rect = picture.rectTransform;
                        savedScale[rect] = rect.localScale;
                        rect.localScale = rect.localScale * LetterPortraitScale;
                        savedAspect[picture] = picture.preserveAspect;
                        picture.preserveAspect = true;
                        if (!savedColors.ContainsKey(picture)) savedColors[picture] = picture.color;
                        picture.color = LetterTint;
                        var frame = picture.gameObject.AddComponent<Outline>();
                        frame.effectColor = new Color(0.36f, 0.25f, 0.14f, 0.9f);
                        frame.effectDistance = new Vector2(6f, -6f);
                        addedFrames.Add(frame);
                        Caption(view, picture, "— " + (owner == "Together" ? "Anevia and Irabeth" : owner ?? node!.Speaker));
                    }
                    else Caption(view, picture, CaptionFor(node!.Speaker, owner));
                }
                catch (Exception ex) { Log("E15b picture polish skipped: " + ex.Message); }
            }

            private static void Caption(object view, Image picture, string? name)
            {
                if (name == null) return;
                if (captionRoot == null)
                {
                    captionRoot = new GameObject("RRT_Caption", typeof(RectTransform), typeof(Image));
                    var back = captionRoot.GetComponent<Image>();
                    back.color = new Color(0f, 0f, 0f, 0.55f);
                    back.raycastTarget = false;
                    var label = new GameObject("RRT_CaptionText", typeof(RectTransform), typeof(TextMeshProUGUI));
                    label.transform.SetParent(captionRoot.transform, false);
                    captionText = label.GetComponent<TextMeshProUGUI>();
                    var template = (CueViewField?.GetValue(view) as DialogCueView)?.Text;
                    if (template != null) { captionText.font = template.font; captionText.fontSharedMaterial = template.fontSharedMaterial; }
                    captionText.fontSize = 24;
                    captionText.alignment = TextAlignmentOptions.Center;
                    captionText.color = new Color(0.93f, 0.87f, 0.74f, 1f);
                    captionText.raycastTarget = false;
                    var lr = label.GetComponent<RectTransform>();
                    lr.anchorMin = Vector2.zero; lr.anchorMax = Vector2.one; lr.offsetMin = Vector2.zero; lr.offsetMax = Vector2.zero;
                }
                captionRoot.transform.SetParent(picture.transform, false);
                captionRoot.transform.SetAsLastSibling();
                var rt = captionRoot.GetComponent<RectTransform>();
                rt.anchorMin = new Vector2(0f, 0f); rt.anchorMax = new Vector2(1f, 0f); rt.pivot = new Vector2(0.5f, 0f);
                rt.anchoredPosition = new Vector2(0f, 24f); rt.sizeDelta = new Vector2(0f, 40f);
                captionText!.text = name;
                captionRoot.SetActive(true);
            }

            // Short RRT page: the cue block stops stretching, so the answers follow the text. Long pages keep the native
            // layout (the paginator measures the stretched block to split text into pages).
            internal static void ApplyLayout(object view)
            {
                try
                {
                    foreach (var pair in savedFlex) if (pair.Key != null) pair.Key.flexibleHeight = pair.Value;
                    savedFlex.Clear();
                    var page = Page(view);
                    if (!IsRrtPage(page, out var node, out _)) return;
                    var texts = new List<string> { node!.Text };
                    texts.AddRange(node.Paragraphs.Select(p => p.Text));
                    if (!IsShortPage(texts)) return;
                    if (!(CuesLayoutField?.GetValue(view) is Component cues)) return;
                    foreach (var element in cues.GetComponents<LayoutElement>())
                    {
                        if (element.flexibleHeight <= 0) continue;
                        savedFlex[element] = element.flexibleHeight;
                        element.flexibleHeight = 0;
                    }
                    if (savedFlex.Count > 0 && cues.transform.parent is RectTransform parent) LayoutRebuilder.MarkLayoutForRebuild(parent);
                }
                catch (Exception ex) { Log("E15b layout polish skipped: " + ex.Message); }
            }
        }

        [HarmonyPatch]
        private static class BookPicturePatch
        {
            private static MethodBase TargetMethod() => AccessTools.Method(BookPolish.ViewType, "SetPicture");
            [HarmonyPostfix]
            private static void Postfix(object __instance) => BookPolish.ApplyPicture(__instance);
        }

        [HarmonyPatch]
        private static class BookLayoutPatch
        {
            private static MethodBase TargetMethod() => AccessTools.Method(BookPolish.ViewType, "OnContentChanged");
            [HarmonyPostfix]
            private static void Postfix(object __instance) => BookPolish.ApplyLayout(__instance);
        }
    }
}
