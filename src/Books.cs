using System;
using System.Collections.Generic;
using System.Linq;
using HarmonyLib;
using Kingmaker;
using Kingmaker.Blueprints;
using Kingmaker.Blueprints.Root.Strings;
using Kingmaker.DialogSystem;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.Localization;
using Kingmaker.UI.Common;

namespace Tirabade
{
    // E15, the RRT book: every paged reading surface (the mailbag, the letter archive, data books such as the Ledger)
    // is a native Book dialog. Each item is one BlueprintBookPage with its own EventPicture (the BookPatch portrait) and
    // text; a per-view runtime cursor decides which page shows. Answers move the cursor in OnSelect, and the dialog
    // selects the next cue after that (DialogController.SelectAnswer runs ActionList.Run, then SelectNextCue), so every
    // navigation answer can point at all of a view's pages and the page condition picks the one under the cursor.
    // Page titles, "N of M" and list labels are written into the localization pack just before the page binds
    // (BookPatch prefix), so the numbers are always current.
    public static partial class Main
    {
        internal const int ListPerPage = 8;

        internal sealed class BookView
        {
            public string Key = "";
            public Func<Snapshot, List<string>> Items = _ => new List<string>();
            public Func<string, string> Label = key => key;
            public string? Cursor;
            public int ListPage;
            public BlueprintDialog? Dialog;
            public readonly List<BlueprintCueBase> ItemPages = new List<BlueprintCueBase>();
            public readonly List<BlueprintCueBase> ListPages = new List<BlueprintCueBase>();
        }

        internal static readonly Dictionary<string, BookView> views = new Dictionary<string, BookView>(StringComparer.Ordinal);
        private static readonly Dictionary<string, Action> pageUpdaters = new Dictionary<string, Action>(StringComparer.Ordinal);

        private static void Put(string id, string value) => LocalizationManager.CurrentPack?.PutString("RRT." + id, value);

        // A portrait key resolves to the mod's own art (Scenes/<key>.png); a letter falls back to its sender, and anything
        // without art keeps the book's native picture rather than a wrong face. List, cover and data-book pages speak as
        // "Book" (no art), not "Narrator", whose default picture is the Anevia and Irabeth scene.
        internal static string PortraitKey(params string?[] keys) => keys.FirstOrDefault(key => !string.IsNullOrEmpty(key)) ?? "";

        internal static List<string> ViewItems(string view) =>
            views.TryGetValue(view, out var v) && enabled && initialized && Game.Instance?.Player != null ? v.Items(State()) : new List<string>();

        // Called before a view's dialog opens (and by its first-page action): the cursor starts on the first item.
        internal static void ViewReset(string view, string? start = null)
        {
            if (!views.TryGetValue(view, out var v)) return;
            var items = ViewItems(view);
            v.Cursor = start != null && items.Contains(start) ? start : items.FirstOrDefault();
            v.ListPage = 0;
        }

        internal static bool OpenView(string view, string? start = null)
        {
            if (!views.TryGetValue(view, out var v) || v.Dialog == null || !Idle() || ViewItems(view).Count == 0 && !view.StartsWith("book.", StringComparison.Ordinal))
                return false;
            ViewReset(view, start);
            Game.Instance.DialogController.StartDialogWithoutTarget(v.Dialog, null);
            return true;
        }

        public sealed class ViewCondition : Condition
        {
            public string View = "";
            public string Mode = "";
            public string Item = "";
            public int Slot;
            public int Parity;
            protected override string GetConditionCaption() => "Three at the Table book view";
            protected override bool CheckCondition()
            {
                if (!views.TryGetValue(View, out var v)) return false;
                var items = ViewItems(View);
                switch (Mode)
                {
                    case "item": return v.Cursor == Item && items.Contains(Item);
                    case "several": return items.Count > 1;
                    case "any": return items.Count > 0;
                    case "list": return v.ListPage % 2 == Parity;
                    case "slot": return Slot < Rules.PageSlice(items, v.ListPage, ListPerPage).Count;
                    case "listmore": return v.ListPage + 1 < Rules.PageCount(items.Count, ListPerPage);
                    case "listless": return v.ListPage > 0;
                    case "section": return books.TryGetValue(View, out var book) && Rules.BookVisible(book, State()).Any(entry => entry.Section == Item);
                    default: return false;
                }
            }
        }

        public sealed class ViewAction : GameAction
        {
            public string View = "";
            public string Op = "";
            public string Item = "";
            public int Slot;
            public override string GetCaption() => "Three at the Table book navigation";
            public override void RunAction()
            {
                if (!views.TryGetValue(View, out var v)) return;
                var items = ViewItems(View);
                switch (Op)
                {
                    case "first": v.Cursor = items.FirstOrDefault(); v.ListPage = 0; break;
                    case "next": v.Cursor = Rules.Step(items, v.Cursor, 1); break;
                    case "prev": v.Cursor = Rules.Step(items, v.Cursor, -1); break;
                    case "set": v.Cursor = items.Contains(Item) ? Item : items.FirstOrDefault(); break;
                    case "list": v.ListPage = Math.Max(0, items.IndexOf(v.Cursor ?? "")) / ListPerPage; break;
                    case "listnext": v.ListPage = Math.Min(v.ListPage + 1, Rules.PageCount(items.Count, ListPerPage) - 1); break;
                    case "listprev": v.ListPage = Math.Max(0, v.ListPage - 1); break;
                    case "slot":
                        var slice = Rules.PageSlice(items, v.ListPage, ListPerPage);
                        if (Slot < slice.Count) v.Cursor = slice[Slot];
                        break;
                    case "section":
                        if (books.TryGetValue(View, out var book))
                            v.Cursor = Rules.BookVisible(book, State()).FirstOrDefault(entry => entry.Section == Item)?.Id ?? v.Cursor;
                        break;
                }
            }
        }

        private static BlueprintAnswer ViewAnswer(string id, string text, BookView view, string op, IEnumerable<BlueprintCueBase> next,
            ViewCondition? show = null, string item = "", int slot = 0)
        {
            var answer = New<BlueprintAnswer>(id);
            InitializeAnswer(answer);
            answer.Text = Text(id, text);
            if (show != null) answer.ShowConditions = Conditions(show);
            answer.OnSelect = Actions(new ViewAction { View = view.Key, Op = op, Item = item, Slot = slot });
            answer.NextCue = Cues(next.ToArray());
            return answer;
        }

        private static BlueprintBookPage ViewPage(string id, string title, Node picture, IEnumerable<BlueprintCueBase> cues, Condition? condition)
        {
            var page = New<BlueprintBookPage>(id);
            page.ShowOnce = false;
            page.Conditions = condition == null ? Conditions() : Conditions(condition);
            page.OnShow = Actions();
            page.Title = Text("title." + id, title);
            foreach (var cue in cues) page.Cues.Add(Ref<BlueprintCueBaseReference>(cue));
            pages.Add(page.AssetGuid.ToString(), picture);
            return page;
        }

        // The list pages of a view: its items eight to a page, each a labelled answer that opens the item's page, with
        // previous/next page. Two alternating pages (the parity condition), so turning a page is always a new cue.
        private static void BuildViewList(BookView view, string listTitle, string intro, IEnumerable<BlueprintAnswer> tail)
        {
            var tailAnswers = tail.ToList();
            var slots = Enumerable.Range(0, ListPerPage).Select(slot => ViewAnswer("answer.view." + view.Key + ".slot." + slot, "", view, "slot",
                view.ItemPages, new ViewCondition { View = view.Key, Mode = "slot", Slot = slot }, slot: slot)).ToList();
            var more = ViewAnswer("answer.view." + view.Key + ".list.next", "[Turn the page.]", view, "listnext", view.ListPages,
                new ViewCondition { View = view.Key, Mode = "listmore" });
            var less = ViewAnswer("answer.view." + view.Key + ".list.prev", "[Turn back a page.]", view, "listprev", view.ListPages,
                new ViewCondition { View = view.Key, Mode = "listless" });
            for (int parity = 0; parity < 2; parity++)
            {
                CueSetup(out var cue, "cue.view." + view.Key + ".list." + parity, intro);
                var page = ViewPage("page.view." + view.Key + ".list." + parity, listTitle, new Node { Id = "list", Speaker = "Book", Text = intro },
                    new[] { cue }, new ViewCondition { View = view.Key, Mode = "list", Parity = parity });
                foreach (var answer in slots.Concat(new[] { more, less }).Concat(tailAnswers)) page.Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
                view.ListPages.Add(page);
                string titleId = "title.page.view." + view.Key + ".list." + parity;
                pageUpdaters[page.AssetGuid.ToString()] = () =>
                {
                    var items = ViewItems(view.Key);
                    Put(titleId, listTitle + " (" + (view.ListPage + 1) + " of " + Rules.PageCount(items.Count, ListPerPage) + ")");
                    var slice = Rules.PageSlice(items, view.ListPage, ListPerPage);
                    for (int slot = 0; slot < ListPerPage; slot++)
                        Put("answer.view." + view.Key + ".slot." + slot, slot < slice.Count ? view.Label(slice[slot]) : "");
                };
            }
        }

        // "Letter 2 of 5" in the page title, current at every bind.
        private static void TitleUpdater(BookView view, BlueprintBookPage page, string item, Func<int, int, string> title)
        {
            string titleId = "title." + page.name.Substring("RRT_".Length);
            pageUpdaters[page.AssetGuid.ToString()] = () =>
            {
                var items = ViewItems(view.Key);
                Put(titleId, title(items.IndexOf(item) + 1, items.Count));
            };
        }

        // E8b + E15 mailbag v2: one page per waiting letter (the sender's portrait, the seal, "Letter 2 of 5"), read, next,
        // previous, every letter in the satchel (a paged list), letters already read, or later.
        private static void BuildMailbagBook(BookView archive)
        {
            var letters = story.Scenes.Where(Rules.IsMailbagLetter).ToArray();
            var view = new BookView { Key = "mailbag", Items = state => mailbag.Entries(story, state).Select(s => s.Id).ToList(), Label = id => MailbagLabel(SceneById(id)) };
            views[view.Key] = view;
            var pagesByLetter = new Dictionary<string, BlueprintBookPage>();
            foreach (var scene in letters)
            {
                string envelope = scene.Owner == "Memory"
                    ? "{n}Not a letter at all: a memory, surfacing unbidden between one march and the next.{/n}"
                    : "{n}A letter from " + scene.Owner + ", sealed and dated. The courier kept it dry, mostly.{/n}";
                CueSetup(out var cue, "cue.view.mailbag." + scene.Id, envelope + "\n\n" + scene.Title);
                var page = ViewPage("page.view.mailbag." + scene.Id, "Letters", new Node { Id = "envelope", Speaker = scene.Owner,
                    Portrait = PortraitKey(scene.Nodes.FirstOrDefault()?.Portrait, scene.Owner), Text = envelope },
                    new[] { cue }, new ViewCondition { View = view.Key, Mode = "item", Item = scene.Id });
                var read = New<BlueprintAnswer>("answer.view.mailbag." + scene.Id + ".read");
                InitializeAnswer(read);
                read.Text = Text(read.name.Substring("RRT_".Length), "[Break the seal.]");
                read.ShowConditions = Conditions(new MailbagCondition { Scene = scene });
                read.SelectConditions = Conditions(new MailbagCondition { Scene = scene });
                read.OnSelect = Actions(new RouteAction { Start = scene }, new MailbagAction { Reopen = true });
                page.Answers.Add(Ref<BlueprintAnswerBaseReference>(read));
                pagesByLetter[scene.Id] = page;
                view.ItemPages.Add(page);
                TitleUpdater(view, page, scene.Id, (i, n) => "Letters (" + i + " of " + n + ")");
            }
            var later = New<BlueprintAnswer>("answer.view.mailbag.later");
            InitializeAnswer(later);
            later.Text = Text(later.name.Substring("RRT_".Length), "[Read the rest later.]");
            later.OnSelect = Actions(new MailbagAction { Reopen = false });
            var toArchive = ViewAnswer("answer.view.mailbag.archive", "[Letters already read.]", archive, "first", archive.ItemPages,
                new ViewCondition { View = archive.Key, Mode = "any" });
            var next = ViewAnswer("answer.view.mailbag.next", "[The next letter.]", view, "next", view.ItemPages, new ViewCondition { View = view.Key, Mode = "several" });
            var prev = ViewAnswer("answer.view.mailbag.prev", "[The letter before.]", view, "prev", view.ItemPages, new ViewCondition { View = view.Key, Mode = "several" });
            var list = ViewAnswer("answer.view.mailbag.list", "[Tip out the satchel: every letter at once.]", view, "list", view.ListPages,
                new ViewCondition { View = view.Key, Mode = "several" });
            var back = ViewAnswer("answer.view.mailbag.back", "[Back to the letter in hand.]", view, "set", view.ItemPages);
            BuildViewList(view, "The satchel", "{n}Letters, spread across the camp table. Take up whichever you like; the rest will keep.{/n}", new[] { back, toArchive, later });
            foreach (var page in pagesByLetter.Values)
                foreach (var answer in new[] { next, prev, list, toArchive, later }) page.Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
            view.Dialog = ViewDialog("dialog.view.mailbag", view);
        }

        // E15 archive: every letter already read, most recent first, re-read in a read-only replay. Replay pages carry the
        // letter's text and its authored choice labels as page turns: no condition, action, check or effect of any kind.
        private static BookView BuildArchive()
        {
            var letters = story.Scenes.Where(Rules.IsMailbagLetter).ToArray();
            var view = new BookView { Key = "archive", Items = state => Rules.ArchiveLetters(story, state).Select(s => s.Id).ToList(), Label = id => MailbagLabel(SceneById(id)) };
            views[view.Key] = view;
            var covers = new Dictionary<string, BlueprintBookPage>();
            foreach (var scene in letters)
            {
                string kept = scene.Owner == "Memory" ? "{n}A memory you have already lived through once.{/n}" : "{n}A letter from " + scene.Owner + ", read and kept.{/n}";
                CueSetup(out var cue, "cue.view.archive." + scene.Id, kept + "\n\n" + scene.Title);
                covers[scene.Id] = ViewPage("page.view.archive." + scene.Id, "Letters kept", new Node { Id = "kept", Speaker = scene.Owner,
                    Portrait = PortraitKey(scene.Nodes.FirstOrDefault()?.Portrait, scene.Owner), Text = kept },
                    new[] { cue }, new ViewCondition { View = view.Key, Mode = "item", Item = scene.Id });
                view.ItemPages.Add(covers[scene.Id]);
                TitleUpdater(view, covers[scene.Id], scene.Id, (i, n) => "Letters kept (" + i + " of " + n + ")");
            }
            foreach (var scene in letters)
            {
                var replay = new Dictionary<string, BlueprintBookPage>();
                foreach (var node in scene.Nodes)
                {
                    CueSetup(out var cue, "cue.replay." + scene.Id + "." + node.Id, node.Text);
                    replay[node.Id] = ViewPage("page.replay." + scene.Id + "." + node.Id, scene.Title.Length > 0 ? scene.Title : "Letters kept",
                        new Node { Id = node.Id, Speaker = node.Speaker, Portrait = PortraitKey(node.Portrait, node.Speaker == "Narrator" ? scene.Owner : node.Speaker), Text = node.Text },
                        new[] { cue }, null);
                }
                foreach (var node in scene.Nodes)
                {
                    int index = 0;
                    foreach (var edge in Rules.ReplayEdges(scene, node))
                    {
                        var answer = New<BlueprintAnswer>("answer.replay." + scene.Id + "." + node.Id + "." + index++);
                        InitializeAnswer(answer);
                        answer.Text = Text(answer.name.Substring("RRT_".Length), edge.Text);
                        answer.NextCue = Cues(edge.Next != null ? replay[edge.Next] : covers[scene.Id]);
                        replay[node.Id].Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
                    }
                    if (index == 0)
                    {
                        var end = New<BlueprintAnswer>("answer.replay." + scene.Id + "." + node.Id + ".end");
                        InitializeAnswer(end);
                        end.Text = Text(end.name.Substring("RRT_".Length), "[Fold the letter away.]");
                        end.NextCue = Cues(covers[scene.Id]);
                        replay[node.Id].Answers.Add(Ref<BlueprintAnswerBaseReference>(end));
                    }
                }
                var again = New<BlueprintAnswer>("answer.view.archive." + scene.Id + ".read");
                InitializeAnswer(again);
                again.Text = Text(again.name.Substring("RRT_".Length), "[Read it again.]");
                again.NextCue = Cues(replay[scene.Nodes[0].Id]);
                covers[scene.Id].Answers.Add(Ref<BlueprintAnswerBaseReference>(again));
            }
            var next = ViewAnswer("answer.view.archive.next", "[The next letter.]", view, "next", view.ItemPages, new ViewCondition { View = view.Key, Mode = "several" });
            var prev = ViewAnswer("answer.view.archive.prev", "[The letter before.]", view, "prev", view.ItemPages, new ViewCondition { View = view.Key, Mode = "several" });
            var list = ViewAnswer("answer.view.archive.list", "[Leaf through all of them.]", view, "list", view.ListPages, new ViewCondition { View = view.Key, Mode = "several" });
            var back = ViewAnswer("answer.view.archive.back", "[Back to the letter in hand.]", view, "set", view.ItemPages);
            var close = New<BlueprintAnswer>("answer.view.archive.close");
            InitializeAnswer(close);
            close.Text = Text(close.name.Substring("RRT_".Length), "[Put them away.]");
            BuildViewList(view, "Letters kept", "{n}The letters you kept, the newest on top.{/n}", new[] { back, close });
            foreach (var page in covers.Values)
                foreach (var answer in new[] { next, prev, list, close }) page.Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
            view.Dialog = ViewDialog("dialog.view.archive", view);
            return view;
        }

        internal static readonly Dictionary<string, BookSpec> books = new Dictionary<string, BookSpec>(StringComparer.Ordinal);

        // E15 data books: a contents page (title, opening, one answer per section with something to read), then one page per
        // visible entry: its portrait, text, conditional lines and a closing tooltip link; next/previous, contents, close.
        private static void BuildDataBook(string id, BookSpec book)
        {
            string key = "book." + id;
            books[key] = book;
            var view = new BookView { Key = key, Items = state => Rules.BookVisible(book, state).Select(e => e.Id).ToList(),
                Label = entryId => book.Entries.First(e => e.Id == entryId).Title };
            views[key] = view;
            CueSetup(out var coverCue, "cue.book." + id + ".cover", book.Opening.Length > 0 ? book.Opening : "{n}" + book.Title + "{/n}");
            var cover = ViewPage("page.book." + id + ".cover", book.Title, new Node { Id = "cover", Speaker = "Book", Portrait = book.Portrait, Text = book.Opening },
                new[] { coverCue }, null);
            foreach (var entry in book.Entries)
            {
                var cues = new List<BlueprintCueBase>();
                CueSetup(out var text, "cue.book." + id + "." + entry.Id, entry.Text);
                cues.Add(text);
                int line = 0;
                foreach (var paragraph in entry.Lines)
                {
                    CueSetup(out var extra, "cue.book." + id + "." + entry.Id + ".line." + line++, paragraph.Text);
                    extra.Conditions = Conditions(new ParagraphCondition { Paragraph = paragraph });
                    cues.Add(extra);
                }
                if (entry.Tooltip.Length > 0)
                {
                    CueSetup(out var tip, "cue.book." + id + "." + entry.Id + ".tooltip", "{n}{g|" + entry.Tooltip + "}" + story.Glossary[entry.Tooltip].Name + "{/g}{/n}");
                    cues.Add(tip);
                }
                var page = ViewPage("page.book." + id + "." + entry.Id, book.Title, new Node { Id = entry.Id, Speaker = "Book",
                    Portrait = PortraitKey(entry.Portrait, book.Portrait), Text = entry.Text }, cues, new ViewCondition { View = key, Mode = "item", Item = entry.Id });
                view.ItemPages.Add(page);
                string section = entry.Section;
                TitleUpdater(view, page, entry.Id, (i, n) =>
                {
                    var visible = Rules.BookVisible(book, State()).Where(e => e.Section == section).Select(e => e.Id).ToList();
                    return section + " (" + (visible.IndexOf(entry.Id) + 1) + " of " + visible.Count + ")";
                });
            }
            var contents = New<BlueprintAnswer>("answer.book." + id + ".contents");
            InitializeAnswer(contents);
            contents.Text = Text(contents.name.Substring("RRT_".Length), "[Back to the contents.]");
            contents.NextCue = Cues(cover);
            var close = New<BlueprintAnswer>("answer.book." + id + ".close");
            InitializeAnswer(close);
            close.Text = Text(close.name.Substring("RRT_".Length), "[Close the book.]");
            int s = 0;
            foreach (var section in book.Sections)
                cover.Answers.Add(Ref<BlueprintAnswerBaseReference>(ViewAnswer("answer.book." + id + ".section." + s++, "[" + section + "]", view, "section",
                    view.ItemPages, new ViewCondition { View = key, Mode = "section", Item = section }, item: section)));
            cover.Answers.Add(Ref<BlueprintAnswerBaseReference>(close));
            var next = ViewAnswer("answer.book." + id + ".next", "[Turn the page.]", view, "next", view.ItemPages, new ViewCondition { View = key, Mode = "several" });
            var prev = ViewAnswer("answer.book." + id + ".prev", "[Turn back a page.]", view, "prev", view.ItemPages, new ViewCondition { View = key, Mode = "several" });
            foreach (var page in view.ItemPages.Cast<BlueprintBookPage>())
                foreach (var answer in new[] { next, prev, contents, close }) page.Answers.Add(Ref<BlueprintAnswerBaseReference>(answer));
            var dialog = New<BlueprintDialog>("dialog.book." + id);
            dialog.Type = DialogType.Book;
            dialog.Conditions = Conditions();
            dialog.FirstCue = Cues(cover);
            dialog.TurnPlayer = false;
            dialog.TurnFirstSpeaker = false;
            dialog.StartActions = Actions();
            dialog.FinishActions = Actions(new RouteAction { StopSpeech = true });
            view.Dialog = dialog;
        }

        private static BlueprintDialog ViewDialog(string id, BookView view)
        {
            var dialog = New<BlueprintDialog>(id);
            dialog.Type = DialogType.Book;
            dialog.Conditions = Conditions();
            dialog.FirstCue = Cues(view.ItemPages.ToArray());
            dialog.TurnPlayer = false;
            dialog.TurnFirstSpeaker = false;
            dialog.StartActions = Actions();
            dialog.FinishActions = Actions(new RouteAction { StopSpeech = true });
            return dialog;
        }

        private static Scene SceneById(string id) => story.Scenes.First(s => s.Id == id);

        // E15: build every book surface. The mailbag v1 dialog stays registered (save names) but the v2 book is shown.
        private static void BuildBooks()
        {
            views.Clear();
            pageUpdaters.Clear();
            books.Clear();
            if (story.Scenes.Any(Rules.IsMailbagLetter))
            {
                var archive = BuildArchive();
                BuildMailbagBook(archive);
            }
            foreach (var pair in story.Books) BuildDataBook(pair.Key, pair.Value);
            RegisterGlossary();
        }

        // E15 tooltips: RRT glossary entries join the native glossary, so {g|RRT_Key}words{/g} in any RRT text shows the
        // native tooltip. Added after GlossaryHolder.Initialize (patch below) or immediately when it already ran.
        private static readonly List<GlossaryEntry> glossary = new List<GlossaryEntry>();

        private static void RegisterGlossary()
        {
            glossary.Clear();
            foreach (var pair in story.Glossary)
                glossary.Add(new GlossaryEntry { Key = pair.Key, Name = Text("glossary." + pair.Key + ".name", pair.Value.Name),
                    Description = Text("glossary." + pair.Key + ".description", pair.Value.Description) });
            if (AccessTools.Field(typeof(GlossaryHolder), "s_Initialized")?.GetValue(null) is true) InjectGlossary();
        }

        internal static int InjectGlossary()
        {
            if (AccessTools.Field(typeof(GlossaryHolder), "s_EntriesbyKey")?.GetValue(null) is not Dictionary<string, GlossaryEntry> entries) return 0;
            // GlossaryHolder.GetEntry looks keys up lower-cased (key.ToLowerInvariant()), as Initialize stores the native ones.
            foreach (var entry in glossary) entries[entry.Key.ToLowerInvariant()] = entry;
            return glossary.Count;
        }

        internal static IReadOnlyList<GlossaryEntry> GlossaryEntries => glossary;

        [HarmonyPatch(typeof(GlossaryHolder), "Initialize")]
        private static class GlossaryPatch
        {
            [HarmonyPostfix]
            private static void Postfix() => InjectGlossary();
        }

        // Harness/tests: the text a view page would show right now.
        internal static void UpdatePage(string guid)
        {
            if (pageUpdaters.TryGetValue(guid, out var update)) update();
        }
    }
}
