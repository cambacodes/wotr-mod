using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Yaniel, Trickster (Writer/handoffs/trickster/yaniel.md; binding plan 11-ROSTER-PLAN-2 §2, Yaniel block and build sheet, R5):
// "The swap: sword for shackle". One block per rules test (Trk_Yaniel_*): the swap at the Fane on both branches (the
// Diplomacy check, the real removal of the form held, the oath, the refusal), the late swap on the walls (23 h / 24 h, every
// Radiance state, before and after Iz), the kill that stands, the oath judged after Iz, Minagho's scene and coexistence, the
// trade-back and the vigil, the niche, the reactors, the pages, and the courtship beats.
internal static class YanielTricksterTests
{
    private const string P = "yaniel.trickster.";
    private const string Committed = "yaniel.committed";
    private const string Closed = "yaniel.closed";
    private const string Started = "yaniel.started";
    private const string Killed = "yaniel.killed.latched";
    private const string Freed = "yaniel.freed.latched";
    private const string Ch5 = "yaniel.ch5.latched";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Unit = "d914111e83e44194db99ab91d8c04632";
    private const string Talk = "8b4733e32e9112a479f8af49c39e3c49";
    private const string DoubtCue = "536ceec8863161f489ef28ddd9c51845";
    private const string HopeCue = "efb1ee540ea049743bd146397641bb9b";
    private const string ToHand = "2e27a01bb56b6ea4587a46d30a0f9ccc";
    private const string Swapped = P + "swapped";
    private const string Carries = P + "carries";
    private const string Judges = P + "judges";
    private const string Oath = P + "cost.oath_deskari";
    private const string Late = P + "cost.late";
    private const string Shackle = P + "cost.shackle_kept";
    private const string Returned = P + "returned";
    private const string Verdict = P + "verdict";
    private const string Broken = P + "oath_broken";
    private const string Stands = P + "oath_stands";
    private const string Declined = P + "declined";
    private const string LeftFree = P + "left_free";
    private const string Niche = P + "niche_seen";
    private const string Refused = P + "fane_refused";
    private static readonly Dictionary<string, string> Forms = new Dictionary<string, string>
    {
        ["yaniel.radiance_masterwork"] = "3b2df06a731030d49a1240b763cb6069",
        ["yaniel.radiance_plus1"] = "de1fc233ad934a0a93a17ebed3ec0cfb",
        ["yaniel.radiance_plus2"] = "6a80e629e9a5ca74da1dabc2984bba3b",
        ["yaniel.radiance_ha4"] = "0ff011d62af77e9428e12ac08f63709e",
        ["yaniel.radiance_ha6"] = "cf5c1a507825f184dacbc3abe14b9db1",
    };

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = Drezen };
        state.AvailableContacts.Add(Unit);
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    private static Snapshot Later(Story story, Snapshot state, int hours, int? chapter = null)
    {
        var later = Program.Copy(state);
        later.Hour += hours;
        if (chapter != null) later.Chapter = chapter.Value;
        Rules.Complete(story, later);
        foreach (var flag in later.Flags.Where(f => !later.Times.ContainsKey(f)).ToList()) later.Times[flag] = state.Hour;
        return later;
    }

    // A native key observed now (e.g. the Chapter05 etude read at the first rest of Chapter 5): its time is the current hour.
    private static Snapshot Observe(Story story, Snapshot state, params string[] keys)
    {
        var now = Program.Copy(state);
        foreach (var key in keys) { now.Flags.Add(key); now.Times.Remove(key); }
        Rules.Complete(story, now);
        foreach (var flag in now.Flags.Where(f => !now.Times.ContainsKey(f)).ToList()) now.Times[flag] = now.Hour;
        return now;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Avail(Scene s, Snapshot w) => Rules.Available(story, s, w);
        Choice Ch(Scene s, string node, int index) => s.Nodes.Single(n => n.Id == node).Choices[index];
        List<(Snapshot state, List<(string node, int index)> path)> Paths(Scene scene, Snapshot initial)
        {
            var outcomes = new List<(Snapshot, List<(string, int)>)>();
            void Visit(string id, Snapshot state, List<(string, int)> path)
            {
                var node = scene.Nodes.Single(n => n.Id == id);
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    if (!Rules.Match(choice.Requires, choice.Forbids, state)) continue;
                    var next = Program.Copy(state);
                    foreach (var effect in choice.Set)
                        if (next.Flags.Add(effect)) next.Times[effect] = next.Hour;
                    if (choice.RemoveItem != null)
                        foreach (var held in Forms.Where(f => f.Value == choice.RemoveItem).Select(f => f.Key)) next.Flags.Remove(held);
                    var edge = new List<(string, int)>(path) { (id, i) };
                    if (choice.Next != null || choice.Check != null)
                        foreach (var target in Rules.NextNodes(choice)) Visit(target, Program.Copy(next), edge);
                    else
                    {
                        if (!choice.Abort) { next.Flags.Add(scene.Id); next.Times[scene.Id] = next.Hour; }
                        Rules.Complete(story, next);
                        outcomes.Add((next, edge));
                    }
                }
            }
            Visit(scene.Nodes[0].Id, initial, new List<(string, int)>());
            return outcomes;
        }
        List<Snapshot> Through(Scene scene, Snapshot w, string node, int index)
        {
            check(Avail(scene, w), "Not available before taking " + scene.Id + "/" + node + "[" + index + "]");
            var hits = Paths(scene, w).Where(o => o.path.Contains((node, index))).Select(o => o.state).ToList();
            check(hits.Count > 0, "No outcome through " + scene.Id + "/" + node + "[" + index + "]");
            return hits;
        }
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            var hit = Through(scene, w, node, index).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            return hit ?? w;
        }

        var rel = story.Relationships["yaniel"];
        var own = story.Scenes.Where(s => s.Relationship == "yaniel" && !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = story.Scenes.Where(s => s.Relationship == "yaniel" && s.Owner == "YanielEpilogue").ToArray();
        var reactions = story.Scenes.Where(s => s.Relationship == "yaniel" && s.Reaction).ToArray();
        var swap = S(P + "fane.swap");
        var hope = S(P + "fane.swap_hope");
        var wall = S(P + "late.wall");
        var found = S(P + "ch5.found");
        var foundLate = S(P + "ch5.found_late");
        var letter = S(P + "verdict.letter");
        var hands = S(P + "verdict.hands");
        var trade = S(P + "commit.trade");
        var vigil = S(P + "commit.vigil");
        var niche = S(P + "visit.niche");
        var minagho = S(P + "ch5.minagho");
        var beats = own.Where(s => s.Id.StartsWith(P + "beat.", StringComparison.Ordinal)).ToArray();

        // Shape and hooks (Trk_Yaniel_Bindings; tools/verify-game-bindings.py resolves every GUID against blueprints.zip).
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed
              && rel.UnavailableFlags.SequenceEqual(new[] { Killed }) && rel.UnavailableOverrides.Count == 0
              && rel.TricksterAccess.Keys.OrderBy(k => k).SequenceEqual(new[] { "doubt", "hope", "late" }),
            "Yaniel's relationship does not match the plan (the kill stands; doubt, hope and late access).");
        check(story.SeenCues["yaniel.fane_doubt"].SequenceEqual(new[] { DoubtCue }) && story.SeenCues["yaniel.fane_hope"].SequenceEqual(new[] { HopeCue })
              && story.SeenCues["yaniel.radiance_sang"].SequenceEqual(new[] { "221a9592527d8b5498346c55549dd2be" })
              && story.SeenCues["yaniel.seelah_sister"].SequenceEqual(new[] { "fd994112dc80453a954e9486f4668d36" })
              && story.SeenCues["yaniel.areelu_unmasked"].SequenceEqual(new[] { "7418d421e3af812439ea312991c37147" })
              && story.SelectedAnswers["yaniel.told_staunton"] == "09d9caa56d1dd4743bb04f8e39ae7459"
              && story.SelectedAnswers["yaniel.told_statue"] == "8f635c7b16eadd44b8a28aac5e937e37"
              && story.Etudes["yaniel.freed"] == "7c5526416ab9e104ba53446c47a8637c" && story.Etudes["yaniel.killed"] == "d6579be891428ff4fba964097afe5794"
              && story.Latches[Freed].SequenceEqual(new[] { "yaniel.freed" }) && story.Latches[Killed].SequenceEqual(new[] { "yaniel.killed" })
              && story.Latches[Ch5].SequenceEqual(new[] { "irabeth.chapter_five" }) && story.Etudes["irabeth.chapter_five"] == "5b01aa690202e584888dfc600a4aac0a"
              && story.CompletedQuests["iz.done"] == "95ff7d975689fcf44b085d10907e711d"
              && Forms.All(f => story.InventoryItems[f.Key] == f.Value && story.RemovableItems.Contains(f.Value))
              && Forms.Keys.All(k => story.Derived["yaniel.radiance_held"].Any(g => g.Length == 1 && g[0] == k)),
            "Trk_Yaniel_Bindings: a native key is not bound as the build sheet lists it.");
        check(!own.Any(s => s.AnswerLists.Contains("0f12118177d102f428a3b30b15b132eb") || s.AnswerLists.Contains("a380d926e92f70e429681eb9654478f9")
                            || s.AnswerLists.Contains("15f754455d1d87c42a4e14df456d5415")),
            "A Yaniel scene hangs on a crowded hub (Fye, the yard, the smith).");
        var presence = story.Presences["yaniel.presence"];
        check(presence.Unit == Unit && presence.Area == Drezen && presence.Mode == "spawn-copy" && presence.Dialog == "hub"
              && presence.At?.Locator == "0e8a0488-bd46-4115-be7a-6674b9358a71" && presence.At?.NearUnit == null
              && presence.MinChapter == 5 && presence.MaxChapter == 5 && presence.Requires.Contains(Returned)
              && presence.Forbids.Contains(Closed) && presence.Forbids.Contains(LeftFree),
            "Her presence is not the spawn-copy at her own Drezen mark (Chapter 5, after she came to stay).");
        var tradeRoom = S(P + "commit.trade_room");
        check(!Rules.IsRemote(trade) && trade.ContactUnit == Unit && trade.InteractionHub == "yaniel.presence"
              && Rules.IsRemote(tradeRoom) && tradeRoom.Requires.Contains("yaniel.presence.failed")
              && tradeRoom.Forbids.Contains(trade.Id) && trade.Forbids.Contains(tradeRoom.Id),
            "R2-3: the commit is not in person on her presence, with the room twin only when the presence fails.");
        check(!own.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal))))),
            "Yaniel's device spends a Word Made True.");
        check(own.Concat(reactions).Concat(pages).All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever")),
            "Path fit (v1): a Yaniel scene is not Trickster-gated (the build sheet tags every scene T).");
        check(story.Scenes.Where(s => s.Relationship == "yaniel").All(s => !s.Forbids.Any(f => f.StartsWith("minachiv.", StringComparison.Ordinal) || f.StartsWith("seelah.", StringComparison.Ordinal))),
            "A Yaniel scene forbids a Minagho/Chivarro or Seelah route flag.");

        // Trk_Yaniel_Swap: the doubt branch (masterwork or +1), inline on her talk hub, back to Cue_0027; Diplomacy DC 20.
        foreach (var form in new[] { "yaniel.radiance_masterwork", "yaniel.radiance_plus1" })
        {
            var w = World(story, 3, "trickster", "trickster.ever", "yaniel.fane_doubt", form);
            check(Avail(swap, w) && !Avail(hope, w) && swap.AnswerLists.SequenceEqual(new[] { Talk }) && swap.NativeReturnCue == DoubtCue
                  && swap.EntryMythic == "PlayerIsTrickster" && swap.TricksterDevice && swap.TricksterState == "doubt",
                "Trk_Yaniel_Swap: the swap is not inline on AnswersList_0010 back to Cue_0027 on the doubt branch (" + form + ").");
            var arg = Ch(swap, "cuff", 0);
            check(arg.Check != null && arg.Check.Skill == "CheckDiplomacy" && arg.Check.DC == 20 && arg.Check.Success == "kept" && arg.Check.Failure == "oath"
                  && Ch(swap, "start", 1).Abort && Ch(swap, "cuff", 1).Abort,
                "Trk_Yaniel_Swap: the argument is not Diplomacy DC 20, or taking the sword back does not leave the swap open.");
            foreach (var reason in new[] { "kept_cannot", "kept_back" })
            {
                var kept = Take(swap, w, reason, form == "yaniel.radiance_masterwork" ? 0 : 1, Swapped, Carries);
                check(!kept.Has(form) && !kept.Has(Judges),
                    "Trk_Yaniel_Swap: success does not remove " + form + " for real (" + reason + ").");
            }
            var sworn = Take(swap, w, "sworn", 0, Swapped, Judges, Oath);
            check(sworn.Has(form) && !sworn.Has(Carries), "Trk_Yaniel_Swap: failure changes the inventory or does not set the oath.");
            var refused = Take(swap, w, "refused", 0, Refused);
            check(!refused.Has(Swapped) && refused.Has(form), "Trk_Yaniel_Swap: giving the cuff back still records a swap.");
        }
        check(swap.Nodes.Concat(hope.Nodes).SelectMany(n => n.Choices).Where(c => c.Next == null && c.Check == null && !c.Abort).All(c => c.NativeNext == ToHand),
            "Trk_Yaniel_Swap: a Fane ending does not play her native farewell (Cue_0012).");
        check(swap.Nodes.SelectMany(n => n.Choices).Where(c => c.RemoveItem != null)
                  .All(c => c.Set.Contains(Carries) && c.Requires.Length == 1 && Forms.ContainsKey(c.Requires[0]) && Forms[c.Requires[0]] == c.RemoveItem),
            "Trk_Yaniel_Swap: a removal is not gated on its own form, or removes on a branch that is not hers.");
        // The hope branch: +2 remade into the +4 Holy Avenger; she keeps that.
        var h = World(story, 3, "trickster", "trickster.ever", "yaniel.fane_hope", "yaniel.radiance_ha4");
        check(Avail(hope, h) && !Avail(swap, h) && hope.NativeReturnCue == HopeCue && hope.TricksterState == "hope",
            "Trk_Yaniel_Swap: the hope branch is not inline back to Cue_0035.");
        var hopeKept = Take(hope, h, "kept_back", 0, Swapped, Carries);
        check(!hopeKept.Has("yaniel.radiance_ha4") && Take(hope, h, "sworn", 0, Judges).Has("yaniel.radiance_ha4"),
            "Trk_Yaniel_Swap: the hope branch does not remove the Holy Avenger on success, or removes it on failure.");
        check(!Avail(swap, World(story, 3, "trickster", "trickster.ever", "yaniel.fane_doubt", "yaniel.radiance_plus1", Swapped))
              && !Avail(swap, World(story, 3, "trickster.was", "yaniel.fane_doubt", "yaniel.radiance_plus1")),
            "Trk_Yaniel_Swap: the swap is offered twice, or off the live Trickster path.");

        // Trk_Yaniel_LateWall: 23 h unavailable, 24 h available after the Chapter 5 latch, for every Radiance state.
        var states = Forms.Keys.Select(k => new[] { k }).Concat(new[] { new string[0] }).ToList();
        foreach (var held in states)
        {
            var before = World(story, 5, new[] { "trickster", "trickster.ever", "yaniel.freed" }.Concat(held).ToArray());
            var at = Observe(story, before, "irabeth.chapter_five");
            check(at.Has(Ch5) && !Avail(wall, Later(story, at, 23)) && Avail(wall, Later(story, at, 24)),
                "Trk_Yaniel_LateWall: the walls do not open exactly 24 h after the Chapter 5 latch (" + string.Join(",", held) + ").");
            var w = Later(story, at, 24);
            if (held.Length == 1)
            {
                var kept = Take(wall, w, "late_kept", Array.IndexOf(new[] { "yaniel.radiance_ha6", "yaniel.radiance_ha4", "yaniel.radiance_plus2", "yaniel.radiance_plus1", "yaniel.radiance_masterwork" }, held[0]),
                    Swapped, Carries, Late);
                check(!kept.Has(held[0]), "Trk_Yaniel_LateWall: success does not remove " + held[0] + ".");
                check(Take(wall, w, "late_sworn", 0, Swapped, Judges, Oath, Late).Has(held[0]), "Trk_Yaniel_LateWall: the late failure does not carry the oath.");
            }
            else
            {
                var sworn = Take(wall, w, "late_sworn", 0, Swapped, Judges, Oath, Late, P + "sword_lost");
                check(!Paths(wall, w).Any(o => o.state.Has(Carries)), "Trk_Yaniel_LateWall: a Commander with no sword can hand her one.");
            }
        }
        // Before and after Iz the late oath names what is still ahead.
        var pre = Later(story, Observe(story, World(story, 5, "trickster", "trickster.ever", "yaniel.freed", "yaniel.radiance_plus1"), "irabeth.chapter_five"), 24);
        var post = Later(story, Observe(story, World(story, 5, "trickster", "trickster.ever", "yaniel.freed", "yaniel.radiance_plus1", "iz.done"), "irabeth.chapter_five"), 24);
        check(Through(wall, pre, "late_iz", 0).Any() && !Paths(wall, pre).Any(o => o.path.Contains(("late_rift", 0)))
              && Through(wall, post, "late_rift", 0).Any() && !Paths(wall, post).Any(o => o.path.Contains(("late_iz", 0))),
            "Trk_Yaniel_LateWall: the late oath does not name Iz before Iz and the Threshold after it.");
        var refusedFane = Later(story, Observe(story, World(story, 5, "trickster", "trickster.ever", "yaniel.freed", Refused, "yaniel.radiance_plus1"), "irabeth.chapter_five"), 24);
        check(Through(wall, refusedFane, "start", 0).Any() && Avail(wall, refusedFane) && wall.TricksterDevice && Rules.IsRemote(wall) && wall.Kind == "visit",
            "Trk_Yaniel_LateWall: a Commander who gave the cuff back at the Fane gets no second chance on the walls.");

        // Trk_Yaniel_KillStands: the kill is the player's own choice; nothing of hers plays after it.
        foreach (var extra in new[] { new[] { "yaniel.fane_doubt", "yaniel.radiance_plus1" }, new[] { Swapped, Carries, Returned, "iz.done" } })
            foreach (var chapter in new[] { 3, 5 })
            {
                var k = Later(story, Observe(story, World(story, chapter, new[] { "trickster", "trickster.ever", "yaniel.freed", "yaniel.killed" }.Concat(extra).ToArray()), "irabeth.chapter_five"), 72);
                check(k.Has(Killed) && !own.Concat(reactions).Any(s => Avail(s, k)), "Trk_Yaniel_KillStands: a scene plays after the kill (chapter " + chapter + ").");
            }
        check(!pages.Any(s => Avail(s, World(story, 6, "trickster.ever", "yaniel.killed", Started, Committed))),
            "Trk_Yaniel_KillStands: a page plays after the kill.");
        // Never freed is an entry condition: no Fane cue, no latch, nothing opens.
        var never = Later(story, Observe(story, World(story, 5, "trickster", "trickster.ever", "yaniel.radiance_plus1"), "irabeth.chapter_five"), 72);
        check(!own.Any(s => Avail(s, never)), "Never freed: a Yaniel scene opens for a woman who was never cut down.");

        // Trk_Yaniel_AllRomanceWalk: carries (the letter from Iz) and judges (her hands), each to the commit and the niche.
        var carried = Take(swap, World(story, 3, "trickster", "trickster.ever", "yaniel.fane_doubt", "yaniel.radiance_plus1"), "kept_back", 1, Swapped, Carries);
        var c5 = Later(story, Observe(story, Later(story, carried, 200, 5), "yaniel.freed", "irabeth.chapter_five"), 24);
        check(!Avail(wall, c5) && Avail(found, c5) && !Avail(foundLate, c5), "Trk_Yaniel_AllRomanceWalk: the Fane swap does not lead to her in Drezen.");
        var home = Observe(story, Take(found, c5, "stay", 0, Returned, Started), P + "drawn.walls");
        check(!Avail(letter, Later(story, home, 24)) && !Avail(trade, Later(story, home, 24)), "The verdict or the trade comes before Iz.");
        var izDone = Observe(story, Later(story, home, 48), "iz.done");
        var afterLetter = Take(letter, Later(story, izDone, 24), "end_quiet", 0, Verdict);
        check(!Avail(hands, Later(story, izDone, 24)) && letter.Kind == "letter", "The carries verdict is not her letter from Iz.");
        var yes = Take(trade, Later(story, afterLetter, 24), "ask", 0, Committed, Shackle);
        check(!Avail(vigil, Later(story, yes, 24)) && Avail(niche, Later(story, yes, 24)) && !Avail(niche, Later(story, yes, 23)),
            "Trk_Yaniel_AllRomanceWalk: the niche does not follow the commit a day later.");
        var nicheDone = Through(niche, Later(story, yes, 24), "morning2", 0).First();
        check(nicheDone.Has(Niche) && nicheDone.Has(P + "morning_seen"), "Trk_Yaniel_AllRomanceWalk: the niche does not end in the morning.");
        check(trade.Nodes.SelectMany(n => n.Choices).All(c => c.Check == null && c.Crusade == null && c.RemoveItem == null)
              && Ch(trade, "ask", 0).Text.StartsWith("[Keep the shackle]", StringComparison.Ordinal) && Ch(trade, "ask", 0).Set.Contains(Committed),
            "The commit carries a test or a price, or the yes is not that neither trades.");

        // Trk_Yaniel_Oath: judges; the verdict reads the pack and the song; a broken oath goes straight to the vigil.
        var judged = World(story, 5, "trickster", "trickster.ever", "yaniel.freed", Swapped, Judges, Oath, Returned, "iz.done", P + "drawn.walls");
        var withSword = Later(story, Observe(story, judged, "yaniel.radiance_plus1"), 24);
        check(Through(hands, withSword, "held_believed", 0).All(o => o.Has(Stands)) && Through(hands, withSword, "held_unproven", 0).All(o => o.Has(P + "oath_unproven") && !o.Has(Stands) && !o.Has(Broken))
              && Ch(hands, "held_word", 0).Check?.DC == 15 && !Avail(letter, withSword),
            "Trk_Yaniel_Oath: holding Radiance after Iz proves the oath by itself, or her doubt condemns an honest Commander.");
        var unproven = Through(hands, withSword, "held_unproven", 0).First();
        check(Avail(trade, Later(story, unproven, 24)) && Through(trade, Later(story, unproven, 24), "judges_open", 2).Any(),
            "Trk_Yaniel_Oath: an unproven oath does not reach the trade, or the trade calls it done.");
        // An oath sworn on the walls after Iz names the Threshold: the verdict holds it pending, never done or broken.
        var threshold = World(story, 5, "trickster", "trickster.ever", "yaniel.freed", Swapped, Judges, Oath, P + "oath_threshold", Returned, "iz.done");
        foreach (var w in new[] { Later(story, threshold, 24), Later(story, Observe(story, threshold, "yaniel.radiance_plus1"), 24) })
            check(Paths(hands, w).All(o => o.state.Has(P + "oath_pending") && !o.state.Has(Stands) && !o.state.Has(Broken)),
                "Trk_Yaniel_Oath: a Threshold oath is judged at the verdict after Iz.");
        var lateRift = Take(wall, post, "late_sworn", 0, P + "oath_threshold");
        check(lateRift.Has(Oath) && lateRift.Has(Judges), "The Threshold oath on the walls is not an oath.");
        // The niche remembers what the Commander actually said about the statue.
        var nicheW = World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, Verdict, Committed, Shackle, P + "beat.statue");
        check(Through(niche, Later(story, Observe(story, nicheW, P + "statue_lied"), 24), "start", 0).Any()
              && Through(niche, Later(story, Observe(story, nicheW, P + "statue_truth"), 24), "start", 1).Any()
              && Through(niche, Later(story, Observe(story, nicheW, P + "statue_scars"), 24), "start", 2).Any(),
            "The niche puts words in the Commander's mouth about the statue.");
        var sang = Later(story, Observe(story, judged, "yaniel.radiance_sang"), 24);
        check(Take(hands, sang, "sang_gone", 0, Verdict, Stands).Has(Stands), "Trk_Yaniel_Oath: the song heard at Iz does not prove the oath.");
        var empty = Later(story, judged, 24);
        var broke = Take(hands, empty, "broken", 0, Verdict, Broken);
        check(Through(hands, empty, "believed", 0).All(r => r.Has(Stands) && !r.Has(Broken)) && Ch(hands, "empty", 1).Check?.DC == 20
              && Ch(hands, "empty", 0).Requires.Contains(P + "sword_lost"),
            "Trk_Yaniel_Oath: the Commander's word is not a Diplomacy DC 20 check, or a lost sword can be talked round.");
        check(!Avail(trade, Later(story, broke, 24)) && Avail(vigil, Later(story, broke, 24)),
            "Trk_Yaniel_Oath: a broken oath still reaches the plain yes, or does not reach the vigil.");
        var knelt = Take(vigil, Later(story, broke, 24), "bell", 0, Committed, Shackle, P + "vigil_stood");
        check(Avail(niche, Later(story, knelt, 24)), "Trk_Yaniel_Oath: the vigil does not reach the niche.");
        var gone = Take(vigil, Later(story, broke, 24), "leave", 0, LeftFree, Closed);
        check(!own.Any(s => Avail(s, Later(story, gone, 72))), "Leaving her to the vigil does not close the route.");

        // The player's no at the trade, and the recovery: the vigil reopens it.
        var gaveBack = Take(trade, Later(story, afterLetter, 24), "given", 0, Declined);
        check(!gaveBack.Has(Committed) && Avail(vigil, Later(story, gaveBack, 24)) && !Avail(trade, Later(story, gaveBack, 24)),
            "Giving the shackle back is not her no with the vigil after it.");
        check(Take(vigil, Later(story, gaveBack, 24), "bell_yes", 0, Committed, Shackle).Has(Committed), "The vigil after a no does not reach the yes.");

        // The late road: the walls, her message, then the same verdict.
        var lateRoad = Take(wall, Later(story, Observe(story, World(story, 5, "trickster", "trickster.ever", "yaniel.freed", "yaniel.radiance_plus1"), "irabeth.chapter_five"), 24),
            "late_kept", 3, Swapped, Carries, Late);
        check(!Avail(found, Later(story, lateRoad, 24)) && Avail(foundLate, Later(story, lateRoad, 24)), "The late road does not reach her message.");
        var lateHome = Take(foundLate, Later(story, lateRoad, 24), "carries", 0, Returned, Started);
        check(Avail(letter, Later(story, Observe(story, lateHome, "iz.done"), 24)), "The late road does not reach the verdict.");
        // A late swap made after Iz never claims she carried the sword there: her verdict is on the wall, not a letter from Iz.
        var postIz = Take(wall, post, "late_kept", 8, Swapped, Carries, Late, P + "handed_after_iz");
        var postHome = Take(foundLate, Later(story, postIz, 24), "carries", 0, Returned);
        check(!Avail(letter, Later(story, postHome, 24)) && Avail(S(P + "verdict.wall"), Later(story, postHome, 24)),
            "A sword handed over after Iz gets her letter about carrying it at Iz.");
        // The trade's yes and the vigil need one of the Commander's own reciprocal choices.
        check(trade.Requires.Contains(P + "drawn") && vigil.Requires.Contains(P + "drawn")
              && !Avail(trade, Later(story, World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, Verdict), 24)),
            "The commit opens without any sign the Commander wanted her.");

        // Trk_Yaniel_MinaghoCoexist: Minagho's route is read, never forbidden; both commits are reachable.
        var mc = World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, "minachiv.started", "minagho_chivarro.trickster.minagho_in", "minachiv.complete", P + "drawn.bite");
        check(Avail(minagho, Later(story, mc, 24)), "Trk_Yaniel_MinaghoCoexist: her scene about Minagho does not open.");
        var told = Take(minagho, Later(story, mc, 24), "truth_end", 0, P + "minagho_told");
        var hid = Take(minagho, Later(story, mc, 24), "hide", 0, "trickster.secret.yaniel_minagho");
        check(Paths(minagho, Later(story, mc, 24)).All(o => !o.state.Flags.Any(f => f.StartsWith("minachiv.", StringComparison.Ordinal) && !mc.Has(f))
                                                          && !o.state.Has(Closed)),
            "Trk_Yaniel_MinaghoCoexist: her scene sets a Minagho/Chivarro flag or closes her route.");
        foreach (var s0 in new[] { told, hid })
        {
            var s1 = Take(letter, Later(story, Observe(story, s0, "iz.done"), 24), "end_quiet", 0, Verdict);
            var s2 = Take(trade, Later(story, s1, 24), "ask", 0, Committed);
            check(s2.Has(Committed) && s2.Has("minachiv.complete"), "Trk_Yaniel_MinaghoCoexist: Yaniel and Minagho are not both committed.");
        }
        check(Through(minagho, Later(story, mc, 24), "start", 0).Any()
              && Through(minagho, Later(story, World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, "minachiv.started", "minagho_chivarro.trickster.chivarro_in"), 24), "start", 1).Any()
              && !Avail(minagho, Later(story, World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, "minachiv.started"), 24))
              && Ch(minagho, "ask", 2).Alignment?.Direction == "Chaotic" && Ch(minagho, "ask", 0).Requires.Contains("minachiv.complete") && Ch(minagho, "ask", 1).Forbids.Contains("minachiv.complete"),
            "Her Minagho scene does not follow what Drezen can show her (Minagho on her crate, or Chivarro asking after her).");
        check(story.Books["trickster.ledger"].Entries.Any(e => e.Id == "secret.yaniel_minagho" && e.Requires.SequenceEqual(new[] { "trickster.secret.yaniel_minagho" })),
            "The secret kept from her is not in the Ledger.");

        // The niche's morning: Seelah fills the lamp if she is in Drezen; the sexton finds it otherwise. Her reaction follows.
        var committed = World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, Verdict, Committed, Shackle);
        check(Through(niche, Later(story, committed, 24), "sexton_seelah", 0).Any()
              && Through(niche, Later(story, World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, Verdict, Committed, "seelah_dead"), 24), "sexton", 0).Any()
              && Through(niche, Later(story, World(story, 5, "trickster", "trickster.ever", Swapped, Carries, Returned, Verdict, Committed, "seelah_gone", "seelah.trickster.returned"), 24), "sexton_seelah", 0).Any(),
            "The morning at the niche does not follow Seelah's fate.");
        var after = S(P + "react.seelah_after");
        var fane = S(P + "react.seelah_fane");
        var sosiel = S(P + "react.sosiel_iron");
        check(reactions.Length == 3 && reactions.Where(s => s.Owner == "Seelah").All(s => s.AnswerLists.SequenceEqual(new[] { "417fa384f3250634bb71859fbc913453" }))
              && sosiel.AnswerLists.SequenceEqual(new[] { "129b55b8b5d50974f84f7c607d894fd0" }) && sosiel.Forbids.Contains("sosiel.dead") && sosiel.Forbids.Contains("sosiel.kicked_out")
              && Avail(sosiel, World(story, 3, "trickster.ever", Swapped)) && !Avail(sosiel, World(story, 3, "trickster.ever", Swapped, "sosiel.dead"))
              && Avail(after, World(story, 5, "trickster.ever", Niche)) && !Avail(after, World(story, 5, "trickster.ever", Niche, "seelah_dead"))
              && Avail(after, World(story, 5, "trickster.ever", Niche, "seelah_dead", "seelah.trickster.returned"))
              && Ch(after, "start", 0).Set.Contains(P + "seelah_blessed")
              && Avail(fane, World(story, 3, "trickster.ever", Swapped, "yaniel.seelah_sister")) && !Avail(fane, World(story, 3, "trickster.ever", Swapped)),
            "Seelah's reactions are not guarded, or speak without her stake (the Fane, the niche).");

        // Pages.
        var pg = pages.ToDictionary(s => s.Id.Substring(P.Length));
        check(pages.Length == 8 && pages.All(s => s.MinChapter == 6 && s.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0 && c.RemoveItem == null && c.Crusade == null))),
            "Yaniel's pages are not eight effect-free Chapter 6 pages.");
        check(Avail(pg["epilogue.together"], World(story, 6, "trickster.ever", Committed, Shackle))
              && Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Returned, Verdict, P + "drawn.walls")) && !Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Returned, Verdict, P + "drawn.walls", Committed))
              && !Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Returned, Verdict)) && Avail(pg["epilogue.unasked"], World(story, 6, "trickster.ever", Returned, Verdict))
              && !Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Returned, Verdict, P + "drawn.walls", Broken)) && Avail(pg["epilogue.broken"], World(story, 6, "trickster.ever", Returned, Verdict, P + "drawn.walls", Broken))
              && !Avail(pg["epilogue.broken"], World(story, 6, "trickster.ever", Returned, Verdict, Broken, Committed))
              && Avail(pg["epilogue.unsettled"], World(story, 6, "trickster.ever", Returned)) && !Avail(pg["epilogue.unsettled"], World(story, 6, "trickster.ever", Returned, Verdict))
              && Avail(pg["epilogue.declined"], World(story, 6, "trickster.ever", Returned, Verdict, Declined)) && !Avail(pg["epilogue.commit"], World(story, 6, "trickster.ever", Returned, Verdict, Declined))
              && Avail(pg["epilogue.left_free"], World(story, 6, "trickster.ever", LeftFree, Closed))
              && !Avail(pg["epilogue.together"], World(story, 6, "trickster.ever", Committed, "sacrifice"))
              && Avail(pg["epilogue.mourned"], World(story, 6, "trickster.ever", Started, Committed, "sacrifice")),
            "Yaniel's pages do not follow the states (together, the late commit, unsettled, declined, free, mourned).");
        // The Last Call coda needs the real commit; eligibility is the commit alone (no late_committed key: 11 §2 review r5 BEL).
        check(story.Scenes.Single(s => s.Id == "yaniel.lastcall.page").Requires.Contains(Committed)
              && story.Derived["yaniel.harem.eligible"].Length == 1 && story.Derived["yaniel.harem.eligible"][0].SequenceEqual(new[] { Committed })
              && !story.Derived.ContainsKey(P + "late_committed"),
            "Last Call or the household treats an uncommitted Yaniel as a partner.");

        // Courtship: every beat reachable; each is a Drezen visit in Chapter 5, optional, before the commit.
        check(beats.Length == 14 && beats.All(s => s.Optional && Rules.IsRemote(s) && s.Kind == "visit" && s.Areas.SequenceEqual(new[] { Drezen })
                                                  && s.Chapters.SequenceEqual(new[] { 5 }) && s.Forbids.Contains(Committed)),
            "Yaniel's courtship is not fourteen optional Chapter 5 visits in Drezen before the commit.");
        var reached = new HashSet<string>();
        foreach (var start in new[] { World(story, 5, "trickster", "trickster.ever", Swapped, Carries, P + "carries_holy", Returned, "yaniel.areelu_unmasked", "yaniel.fake_freed"),
                                      World(story, 5, "trickster", "trickster.ever", Swapped, Judges, Oath, Returned, "yaniel.radiance_plus1", "yaniel.areelu_unmasked") })
        {
            var state = start;
            for (int i = 0; i < 20; i++)
            {
                state = Later(story, state, 48);
                foreach (var scene in beats.Where(s => Avail(s, state)).ToList())
                {
                    var outcome = Program.Walk(scene, state).FirstOrDefault(r => r.Has(scene.Id));
                    if (outcome == null) continue;
                    reached.Add(scene.Id);
                    state = outcome;
                }
            }
        }
        foreach (var scene in beats)
            check(reached.Contains(scene.Id), "Yaniel: the beat " + scene.Id + " is never reachable.");
        // The Chapter 3 letter and the Chapter 4 memory keep the pacing (one beat in each chapter she is away).
        var ch3 = S(P + "ch3.nerosyan");
        var ch4 = S(P + "ch4.shackle");
        check(Avail(ch3, Later(story, World(story, 3, "trickster.ever", Swapped, Carries), 72)) && ch3.Kind == "letter"
              && Avail(ch3, Later(story, World(story, 3, "trickster.ever", Refused), 72))
              && Avail(ch4, Later(story, World(story, 4, "trickster.ever", Swapped), 48)) && ch4.Kind == "memory"
              && Take(ch4, Later(story, World(story, 4, "trickster.ever", Swapped), 48), "worn", 0, P + "cuff_worn").Has(P + "ch4_seen")
              && Avail(S(P + "ch4.block"), Later(story, World(story, 4, "trickster.ever", Swapped, P + "ch4_seen"), 24))
              && Ch(S(P + "ch4.block"), "choose", 1).Check?.Skill == "SkillThievery" && Ch(S(P + "ch4.block"), "choose", 0).Crusade?.Amount == -50,
            "The Chapter 3 letter or the Chapter 4 memory does not arrive.");
        Console.WriteLine("PASS: Yaniel Trickster (Trk_Yaniel_*): the swap on both Fane branches, the walls at 24 h for every Radiance state, "
                          + "the kill that stands, the oath judged after Iz, Minagho, the trade and the vigil, the niche, the reactors, the pages, "
                          + beats.Length + " beats.");
    }
}
