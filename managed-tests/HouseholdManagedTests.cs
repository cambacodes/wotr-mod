using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.AreaLogic.QuestSystem;
using Kingmaker.Blueprints;
using Kingmaker.DialogSystem.Blueprints;
using Tirabade;

// E16, the household's Table as the real Build constructs it: "[The corner table]" on Thaberdine's tavern lists (a native
// opener that opens the Table view), the Table menu (two alternating list pages of six slots that queue the chosen scene,
// "[More…]" / back, "[Open the Ledger]", leave last), and the Ledger book carrying the household sections.
internal static class HouseholdManagedTests
{
    public static void Run(Story story, Func<string, BlueprintGuid> id, Action<bool, string> check)
    {
        var views = (System.Collections.IDictionary)typeof(Main).GetField("views", BindingFlags.NonPublic | BindingFlags.Static)!.GetValue(null);
        BlueprintAnswer A(BlueprintAnswerBaseReference r) => (BlueprintAnswer)r.Get();

        foreach (var opener in story.Openers)
        {
            var list = ResourcesLibrary.TryGetBlueprint(BlueprintGuid.Parse(opener.AnswerList)) as BlueprintAnswersList;
            var reference = list?.Answers.SingleOrDefault(r => r.Guid == id("opener." + opener.Id));
            var answer = reference == null ? null : A(reference);
            check(answer != null && list!.Answers.Count >= 2 && list.Answers.IndexOf(reference!) < list.Answers.Count - 1,
                "A native opener is not on its list, before the list's last native answer: " + opener.Id);
            check(answer!.ShowConditions.Conditions.Single() is Main.OpenerCondition oc && oc.Opener == opener
                && answer.SelectConditions.Conditions.Single() is Main.OpenerCondition
                && answer.OnSelect.Actions.Single() is Main.OpenerAction oa && oa.View == opener.View && answer.NextCue.Cues.Count == 0,
                "A native opener does not end the native dialog and open its view: " + opener.Id);
        }
        check(story.Openers.Any(o => o.View == "table"), "No opener leads to the Table.");

        foreach (var allowance in story.RestAllowances)
        {
            var flag = ResourcesLibrary.TryGetBlueprint(id("flag." + Rules.RestSpentPrefix + allowance.Key)) as BlueprintUnlockableFlag;
            check(flag != null, "Rest allowance has no stable native save flag: " + allowance.Key);
            var manager = new UnlockableFlagsManager();
            manager.UnlockedFlags.Add(flag!, allowance.Value);
            check(manager.GetFlagValue(flag!) == allowance.Value, "Native flag container lost the spent allowance: " + allowance.Key);
        }
        check(views.Contains("table"), "The Table view was not built.");
        var view = views["table"]!;
        var lists = ((List<BlueprintCueBase>)view.GetType().GetField("ListPages")!.GetValue(view)!).Cast<BlueprintBookPage>().ToList();
        var dialog = (BlueprintDialog)view.GetType().GetField("Dialog")!.GetValue(view)!;
        check((int)view.GetType().GetField("PerPage")!.GetValue(view)! == 6 && lists.Count == 2 && dialog.Type.ToString() == "Book"
            && dialog.FirstCue.Cues.Select(c => c.Guid).SequenceEqual(lists.Select(p => p.AssetGuid)), "The Table menu is not a two-page book of six.");
        foreach (var page in lists)
        {
            var answers = page.Answers.Select(A).ToList();
            check(answers.Count == 10, "The Table page does not offer six slots, more, back, the Ledger and leave.");
            check(answers.Take(6).All(a => a.ShowConditions.Conditions.Single() is Main.ViewCondition vc && vc.Mode == "slot"
                && a.OnSelect.Actions.Length == 2 && a.OnSelect.Actions[0] is Main.ViewAction va && va.Op == "slot"
                && a.OnSelect.Actions[1] is Main.TableAction ta && ta.Start && a.NextCue.Cues.Count == 0),
                "A Table slot does not pick the scene and end the menu to queue it.");
            check(answers[6].OnSelect.Actions.Single() is Main.ViewAction more && more.Op == "listnext"
                && answers[7].OnSelect.Actions.Single() is Main.ViewAction back && back.Op == "listprev", "The Table menu does not page.");
            check(answers[8].OnSelect.Actions.Single() is Main.TableAction open && open.Open == "book.trickster.ledger"
                && answers[8].ShowConditions.Conditions.Single() is Main.ViewCondition lc && lc.View == "book.trickster.ledger" && lc.Mode == "any",
                "'[Open the Ledger]' does not open the Ledger (only when it has pages).");
            check(answers[9].OnSelect.Actions.Length == 0 && answers[9].NextCue.Cues.Count == 0 && answers[9].ShowConditions.Conditions.Length == 0,
                "'[Leave the table.]' is not the last, unconditional answer.");
        }
        check(views.Contains("book.trickster.ledger"), "The Ledger book was not built.");
        var ledger = story.Books["trickster.ledger"];
        foreach (var entry in ledger.Entries.Where(e => e.Section == "Guest List" || e.Section == "Seating Notes"))
            check(ResourcesLibrary.TryGetBlueprint(id("page.book.trickster.ledger." + entry.Id)) is BlueprintBookPage,
                "A household Ledger entry has no page: " + entry.Id);
    }
}
