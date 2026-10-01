using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Iomedae, Trickster (Writer/handoffs/trickster/iomedae.md, Build sheet R6; binding plan 11-ROSTER-PLAN-2 §2, Iomedae block):
// "Her own bridge". She is veiled until the finale: the banner's memory and her herald in Chapter 3-4, her own voice only after
// the Summit, in person only at Threshold and after. One block per rules test (Trk_Iomedae_*): the bindings and hooks, the
// Chapter 3 chain, the Abyss, the Summit, the bare platform, the banner back at Iz or the cathedral's banner, the disputation
// and its refusals, the Threshold act and its reachable yes, the bridge world and every page, the reactors, Last Call and the
// household.
internal static class IomedaeTricksterTests
{
    private const string P = "iomedae.trickster.";
    private const string Committed = "iomedae.committed";
    private const string Closed = "iomedae.closed";
    private const string Started = "iomedae.started";
    private const string Drezen = "2570015799edf594daf2f076f2f975d8";
    private const string Held = "iomedae.banner_in_hand";
    private const string Kept = "iomedae.appointment_kept";
    private const string Carried = P + "banner_carried";
    private const string Declined = P + "declined";
    private const string Called = P + "disputation.called";
    private const string Order = P + "order_banner";
    private const string Latch = "iomedae.key_dies_revealed.latched";
    private const string Active = "lastcall.active";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = Drezen };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 300;
        return state;
    }

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        bool Avail(Scene s, Snapshot w) => Rules.Available(story, s, w);
        Choice Ch(Scene s, string node, int index) => s.Nodes.Single(n => n.Id == node).Choices[index];
        // Memoized on (node, flag set, target edge taken): each distinct state is expanded once, so dialogue cycles (the
        // disputation's "notice" <-> "step_down") terminate and branching stays linear in the number of distinct states, while a
        // path through a wanted edge (Take) is never pruned by an earlier visit that skipped it. Hard cap on outcomes.
        List<(Snapshot state, List<(string node, int index)> path)> Paths(Scene scene, Snapshot initial, (string, int)? via = null)
        {
            var outcomes = new List<(Snapshot, List<(string, int)>)>();
            var seen = new HashSet<string>();
            void Visit(string id, Snapshot state, List<(string, int)> path)
            {
                bool taken = via.HasValue && path.Contains(via.Value);
                if (outcomes.Count >= 2000 || !seen.Add(id + "|" + taken + "|" + string.Join(",", state.Flags.OrderBy(f => f, StringComparer.Ordinal)))) return;
                var node = scene.Nodes.Single(n => n.Id == id);
                for (int i = 0; i < node.Choices.Count; i++)
                {
                    var choice = node.Choices[i];
                    if (!Rules.Match(choice.Requires, choice.Forbids, state)) continue;
                    var next = Program.Copy(state);
                    foreach (var effect in choice.Set)
                        if (next.Flags.Add(effect)) next.Times[effect] = next.Hour;
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
        Snapshot Take(Scene scene, Snapshot w, string node, int index, params string[] also)
        {
            check(Avail(scene, w), "Not available before taking " + scene.Id + "/" + node + "[" + index + "]");
            var hit = Paths(scene, w, (node, index)).Where(o => o.path.Contains((node, index))).Select(o => o.state).FirstOrDefault(r => also.All(r.Has));
            check(hit != null, "No outcome of " + scene.Id + " through " + node + "[" + index + "] with " + string.Join(", ", also));
            return hit ?? w;
        }
        Snapshot Later(Snapshot state, int hours, int? chapter = null, string? area = null)
        {
            var later = Program.Copy(state);
            later.Hour += hours;
            if (chapter.HasValue) later.Chapter = chapter.Value;
            if (area != null) later.Area = area;
            Rules.Complete(story, later);
            return later;
        }
        IEnumerable<string> Reachable(Scene scene, Snapshot initial)
        {
            var seen = new HashSet<string>();
            var stack = new Stack<(string, Snapshot)>();
            stack.Push((scene.Nodes[0].Id, initial));
            while (stack.Count > 0)
            {
                var (id, st) = stack.Pop();
                if (!seen.Add(id)) continue;
                foreach (var choice in scene.Nodes.Single(nn => nn.Id == id).Choices.Where(ch => Rules.Match(ch.Requires, ch.Forbids, st)))
                {
                    var next = Program.Copy(st);
                    foreach (var f in choice.Set) next.Flags.Add(f);
                    foreach (var target in Rules.NextNodes(choice)) stack.Push((target, next));
                }
            }
            return seen.Select(id => scene.Nodes.Single(nn => nn.Id == id).Text);
        }
        bool Shows(Paragraph pp, Snapshot w) => pp.Requires.All(w.Has) && !pp.Forbids.Any(w.Has) && pp.AnyGroups.All(g => g.Any(w.Has));
        string Render(Scene page, Snapshot w) => string.Join(" ", page.Nodes.SelectMany(n => n.Paragraphs).Where(pp => Shows(pp, w)).Select(pp => pp.Text));

        var rel = story.Relationships["iomedae"];
        var mine = story.Scenes.Where(s => s.Relationship == "iomedae").ToArray();
        var own = mine.Where(s => !s.Reaction && !s.Owner.EndsWith("Epilogue", StringComparison.Ordinal)).ToArray();
        var pages = mine.Where(s => s.Owner == "IomedaeEpilogue").ToArray();
        var reactions = mine.Where(s => s.Reaction).ToArray();
        var first = S(P + "dream.banner");
        var question = S(P + "herald.question");
        var answer = S(P + "herald.answer");
        var chasm = S(P + "dream.chasm");
        var test = S(P + "platform.test");
        var knight = S(P + "dream.test");
        var legend = S(P + "herald.legend");
        var silence = S(P + "abyss.silence");
        var summit = S(P + "summit.precedent");
        var bare = S(P + "platform.bare");
        var heraldDream = S(P + "dream.herald");
        var izNight = S(P + "iz.night");
        var order = S(P + "order.banner");
        var disp = S(P + "disputation");
        var mortal = S(P + "dream.mortal");
        var eve = S(P + "dream.eve");
        var wound = S(P + "threshold.banner");

        // Trk_Iomedae_Bindings: the relationship, the banner in hand (Iz Cue_0011), the herald's fate, Nenio's Acts; no presence,
        // no Storyteller hub, every hook where the build sheet puts it; every scene Trickster-gated (v1: all T).
        check(rel.StartedFlag == Started && rel.ClosedFlag == Closed && rel.CommittedFlag == Committed && rel.UnavailableFlags.Length == 0,
            "Trk_Iomedae_Bindings: the relationship does not match the plan (she is never unavailable).");
        check(story.SeenCues[Held].SequenceEqual(new[] { "1a0b602da28e56f4badf9406964e4244" })
              && story.SeenCues["iomedae.herald_saved"].SequenceEqual(new[] { "55ab2d8561d68ad4aae145e4798b43d4" })
              && story.SeenCues["iomedae.herald_fell"].OrderBy(g => g).SequenceEqual(new[] { "1f0fef1fbc666cc42a213671d6b171a2", "c241ccdbc3b178b41b7161d17ff43b17" })
              && story.SeenCues["iomedae.herald_fought"].Length == 3 && !story.SeenCues["iomedae.herald_fought"].Intersect(story.SeenCues["iomedae.herald_fell"]).Any()
              && story.SeenCues["iomedae.nenio_acts"].SequenceEqual(new[] { "cdbc3902b0a3ea742b44922dedeee61b" })
              && story.SeenCues["iz.banner_lost"].SequenceEqual(new[] { "710ed96131bbf4e42b930f87cfd6aa25" })
              && story.Etudes["iz.sock_raised"] == "b99cec06dab2bd24fa3124bad167028f",
            "Trk_Iomedae_Bindings: the banner, the herald or the Acts are not read from their canon cues.");
        check(!story.Presences.Keys.Any(k => k.StartsWith("iomedae", StringComparison.Ordinal))
              && !mine.Any(s => s.AnswerLists.Contains("2f5b7e0b76d3c5a42a431e1e33a8db09") || s.AnswerLists.Contains("00a9aa45318e1da4a8566296ca4768d6")),
            "Trk_Iomedae_Bindings: she has a presence, or a scene uses the Storyteller's hub.");
        check(question.AnswerLists.SequenceEqual(new[] { "797452ab97defe74487c091e59379224" }) && question.NativeReturnCue == "2ea22fac3bb0ed04ba643748d1c2bf8e"
              && answer.AnswerLists.SequenceEqual(question.AnswerLists) && answer.NativeReturnCue == question.NativeReturnCue
              && legend.AnswerLists.SequenceEqual(new[] { "d1abc9044634dec45a396755380c8623" }) && legend.NativeReturnCue == "50ab84494d3f15341bf5f87d712f3030"
              && summit.AnswerLists.SequenceEqual(new[] { "7f18896facfbd614c96e2e4ea2d6c0d5" }) && summit.ReturnToList && summit.NativeReturnCue == null
              && wound.AnswerLists.SequenceEqual(new[] { "294126e3264796e488ce19bfb1851355", "16994192cfa484744bd10852b8dc806f" }) && wound.ReturnToList && wound.NativeReturnCue == null,
            "Trk_Iomedae_Hooks: a hook is not on the build sheet's list and return.");
        check(mine.All(s => s.Requires.Contains("trickster") || s.Requires.Contains("trickster.ever")),
            "Path fit (v1): an Iomedae scene is not Trickster-gated (every scene is T).");
        check(!mine.Any(s => s.Nodes.Any(n => n.Choices.Any(c => c.Set.Any(f => f.StartsWith("trickster.wmt.use.", StringComparison.Ordinal) || f.StartsWith("trickster.lastcall.", StringComparison.Ordinal))))),
            "Trk_Iomedae_Bindings: her route spends a Word Made True or sets a Last Call key (the device is a wager on her choice).");
        check(mine.All(s => !s.Requires.Concat(s.Forbids).Concat(s.RequiresAnyGroups.SelectMany(g => g))
                  .Any(f => (f.EndsWith(".started") || f.EndsWith(".closed") || f.EndsWith(".committed")) && !f.StartsWith("iomedae.", StringComparison.Ordinal))),
            "Coexistence: an Iomedae scene gates on another relationship's lifecycle flag.");

        // Veiled until the finale: before the Summit no page of hers carries her voice; the Chapter 3-4 dreams are the banner's
        // memory (Kind memory), and she speaks as herself (sending) only on pages that follow the Summit's latch.
        var before = own.Where(s => s.Remote && s.MaxChapter <= 4).ToArray();
        check(before.Length == 8 && before.All(s => (s.Kind == "memory" || s.Kind == "event") && s.Nodes.All(n => n.Speaker != "Iomedae")),
            "Trk_Iomedae_Veiled: a Chapter 3-4 page gives her a voice before the Summit (Cue_0087: she only observed).");
        check(own.Where(s => s.Remote && s.Nodes.Any(n => n.Speaker == "Iomedae")).All(s => s.Requires.Contains(Latch) || s.Requires.Contains(Committed)
                  || s.Requires.Contains(P + "disputation.called") || s.Requires.Contains(Held) || s.Requires.Contains("iz.done")),
            "Trk_Iomedae_Veiled: a page in her own voice can play before the Summit.");
        check(!own.Any(s => s.Nodes.Any(n => n.Text.Contains("for the first time") || n.Text.Contains("for a long moment") || n.Text.Contains("does not look away"))),
            "Trk_Iomedae_Tics: a banned tic in her route.");

        // Trk_Iomedae_Chapter3: the banner's first memory at a Drezen rest; the herald prays; no answer; the gorge; the word.
        var c3 = World(story, 3, "trickster", "trickster.ever");
        var abroad = Later(c3, 0, area: "00000000000000000000000000000000");
        check(Avail(first, c3) && !Avail(first, abroad) && !Avail(first, World(story, 3, "trickster.ever", "trickster.failed"))
              && first.Chapters.SequenceEqual(new[] { 3 }) && first.Kind == "memory",
            "Trk_Iomedae_Chapter3: the banner's first memory does not come at a Drezen rest in Chapter 3 on the live path.");
        var d1 = Take(first, c3, "wake", 1, Started);
        var moved = Take(first, c3, "moved", 0, Closed);
        check(d1.Has(Started) && d1.Has(P + "dream.banner") && moved.Has(P + "sent_away") && !moved.Has(Started),
            "Trk_Iomedae_Chapter3: the first dream does not start the route, or moving out from under the banner does not close it.");
        var q = Take(question, d1, "ask", 0, P + "question_sent", P + "asked.whose");
        check(!Avail(question, c3) && Avail(answer, Later(q, 24)) && !Avail(answer, Later(q, 23)) && Avail(chasm, Later(q, 24)),
            "Trk_Iomedae_Chapter3: the herald's question needs the dream, or his answer and the gorge do not wait a day.");
        var a1 = Take(answer, Later(q, 24), "warn", 0, P + "herald_answered");
        check(a1.Has(P + "herald_answered"),
            "Trk_Iomedae_Chapter3: the herald's report is not recorded.");
        var g = Take(chasm, Later(a1, 24), "wake", 0, P + "bridge_seen");
        check(g.Has("iomedae.trickster.bridge_known") && !Avail(test, Later(g, 11)) && Avail(test, Later(g, 12)),
            "Trk_Iomedae_Chapter3: the gorge does not make the legend known, or the word does not wait for it.");
        var t1 = Take(test, Later(g, 12), "start", 1, P + "tested", P + "test.liar");
        var k1 = Take(knight, Later(t1, 24), "slip", 1, P + "test_answered", P + "slip_burned");
        check(k1.Has(P + "slip_burned") && Reachable(knight, Later(t1, 24)).Any(x => x.Contains("not proud of the word"))
              && !Reachable(knight, Later(t1, 24)).Any(x => x.Contains("the name of her dead god")),
            "Trk_Iomedae_Chapter3: the dead knight's memory does not read the word the Commander wrote.");

        // Trk_Iomedae_Chapter4: in the Abyss, the herald tells the Acts (and may be told the dreams); the silence page.
        var c4 = World(story, 4, "trickster", "trickster.ever", Started, P + "dream.banner");
        check(Avail(legend, c4) && legend.Chapters.SequenceEqual(new[] { 4 }) && Take(legend, c4, "dreams", 0, P + "dreams_told").Has(P + "bridge_told")
              && Avail(silence, c4) && !Avail(silence, World(story, 4, "trickster", "trickster.ever")),
            "Trk_Iomedae_Chapter4: the Abyss has no beat for her (the herald's Acts, the silence).");

        // Trk_Iomedae_Summit: the precedent beside the refusal (E14b), a late door into the route, and no romance there.
        var s5 = World(story, 5, "trickster", "trickster.ever", "iomedae.key_dies_revealed");
        var asked = Take(summit, s5, "understand", 0, P + "summit_asked", Started);
        check(asked.Has("iomedae.trickster.bridge_known") && summit.EntryMythic == "PlayerIsTrickster" && !Avail(summit, World(story, 5, "trickster", "trickster.ever"))
              && Reachable(summit, World(story, 5, "trickster", "trickster.ever", "iomedae.key_dies_revealed", P + "dream.banner", Started, P + "bridge_seen")).Any(x => x.Contains("indiscreet"))
              && summit.Nodes.All(n => n.SpeakerUnit == "9a1443603c9353d4194a583a31228c8b"),
            "Trk_Iomedae_Summit: the Summit precedent is not a late door (or not in her unit's voice).");

        // Trk_Iomedae_Plan: the bare platform (before Iz), the herald's fate in her own voice.
        var plan = World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen");
        check(Avail(bare, plan) && !Avail(bare, World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", "iz.done"))
              && Take(bare, plan, "wager", 0, P + "plan.wager").Has(P + "plan.wager"),
            "Trk_Iomedae_Plan: the wager is not conceived on the bare platform before Iz.");
        check(Avail(heraldDream, World(story, 5, "trickster.ever", Started, Latch, "iomedae.herald_saved"))
              && !Avail(heraldDream, World(story, 5, "trickster.ever", Started, "iomedae.herald_saved"))
              && Take(heraldDream, World(story, 5, "trickster.ever", Started, Latch, "iomedae.herald_fell"), "listen", 0, P + "first_spoken").Has(P + "herald_dream"),
            "Trk_Iomedae_Herald: her herald's fate is not answered in her own voice after the Summit.");

        // Trk_Iomedae_Banner: back in hand at Iz, she speaks through it and calls the disputation; the word pays off.
        var iz = World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", Held, P + "tested", P + "test.please");
        check(Avail(izNight, Later(iz, 0, area: "00000000000000000000000000000000")) && !Avail(izNight, World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen"))
              && Take(izNight, iz, "form", 0, Called).Has(P + "first_spoken")
              && Reachable(izNight, iz).Any(x => x.Contains("wax")) && !Reachable(izNight, iz).Any(x => x.Contains("my god's name")),
            "Trk_Iomedae_Banner: the banner in hand does not carry her voice and the call, or she recalls the wrong word.");

        // Trk_Iomedae_Fallback: lost at Iz (or the sock): the cathedral's banner by oath (Lawful 1) or theft (Thievery DC 22),
        // a failed theft turning into the oath; never while the Sword of Valor is in hand.
        var lost = World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", "iz.done", "iz.banner_lost");
        var sock = World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", "iz.done", "iz.banner_lost", "iz.sock_raised");
        var theft = order.Nodes.Single(n => n.Id == "night").Choices.Single(c => c.Check != null).Check!;
        check(Avail(order, lost) && Avail(order, sock) && !Avail(order, World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", "iz.done", "iz.banner_lost", Held))
              && order.RequiresAnyGroups.Length == 1 && order.RequiresAnyGroups[0].Length == 2
              && theft.Skill == "SkillThievery" && theft.DC == 22 && theft.CommanderOnly && theft.Success == "stolen" && theft.Failure == "caught",
            "Trk_Iomedae_Fallback: the cathedral's banner is not reachable exactly when her own was lost.");
        var sworn = Take(order, lost, "swear", 0, Order, P + "cost.oath_sworn", Called);
        var stolen = Take(order, lost, "stolen", 0, Order, P + "cost.banner_stolen", Called);
        check(Ch(order, "swear", 0).Alignment?.Direction == "Lawful" && Ch(order, "swear", 0).Alignment?.Value == 1
              && Paths(order, lost).Where(o => o.path.Contains(("caught2", 0))).All(o => o.state.Has(P + "cost.oath_sworn"))
              && Reachable(order, sock).Any(x => x.Contains("I noticed")) && !Reachable(order, lost).Any(x => x.Contains("I noticed")),
            "Trk_Iomedae_Fallback: the oath is not Lawful 1, a failed theft does not become the oath, or the sock line plays without the sock.");

        // Trk_Iomedae_Disputation: the commit (her concession aloud), SkillLoreReligion DC 24 or plain, and every refusal
        // player-caused (the boast, the mocked madness, the lie about the theft); never after a yes or a no.
        var ready = World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", "iz.done", Held, Called);
        check(!Avail(disp, Later(ready, 0, area: "00000000000000000000000000000000")) && disp.Areas.SequenceEqual(new[] { Drezen }) && disp.DelayHours == 24
              && disp.Chapters.SequenceEqual(new[] { 5 }),
            "Trk_Iomedae_Disputation: the disputation plays away from the platform, or outside Chapter 5.");
        var lores = disp.Nodes.Single(n => n.Id == "obj3").Choices.Where(c => c.Check != null).ToList();
        check(lores.Count == 2 && lores.All(c => c.Check!.Skill == "SkillLoreReligion" && c.Check.CommanderOnly && c.Check.Success == "old_form" && c.Check.Failure == "tangled")
              && lores.Single(c => c.Requires.Contains(P + "canons_studied")).Check!.DC == 20 && lores.Single(c => c.Forbids.Contains(P + "canons_studied")).Check!.DC == 24
              && Take(S(P + "canons"), World(story, 5, "trickster.ever", Started, Called), "win", 0, P + "canons_studied").Has(P + "canons_studied"),
            "Trk_Iomedae_Disputation: the third objection is not SkillLoreReligion DC 24 (20 after the canons).");
        var yes = Take(disp, ready, "will", 0, Committed, P + "cost.buried_to_the_world");
        check(yes.Has(P + "disputed") && !yes.Has(Declined) && Paths(disp, ready).Where(o => o.state.Has(Committed)).All(o => o.state.Has(P + "cost.buried_to_the_world"))
              && disp.Nodes.SelectMany(n => n.Choices).All(c => c.Crusade == null && c.Alignment == null),
            "Trk_Iomedae_Disputation: her concession does not commit, or a yes leaves the world's grave unconceded, or it charges a fee.");
        var boast = Take(disp, ready, "refuse", 0, Declined, P + "cost.boasted");
        check(!boast.Has(Committed) && !boast.Has(Closed) && !Avail(disp, Later(boast, 30)) && !Avail(disp, Later(yes, 30)),
            "Trk_Iomedae_Disputation: the boast is not a soft no (declined, not closed), or the disputation replays.");
        var mad = World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", "iz.done", Held, Called, "iomedae.reproached");
        check(Take(disp, mad, "mocked", 0, Declined).Has(P + "cost.madness_mocked") && Take(disp, mad, "will", 0, Committed).Has(P + "answered.madness")
              && Paths(disp, ready).All(o => !o.path.Any(e => e.node == "madness")),
            "Trk_Iomedae_Disputation: the Trickster ultimate is not a fourth objection (answered, or mocked), or it is raised without it.");
        var thief = World(story, 5, "trickster.ever", Started, Latch, P + "bridge_seen", "iz.done", Order, P + "cost.banner_stolen", Called);
        check(Take(disp, thief, "lied", 0, Declined).Has(P + "cost.lied") && Take(disp, thief, "will", 0, Committed).Has(P + "answered.theft"),
            "Trk_Iomedae_Disputation: a stolen banner is not answered for (or the lie does not end it).");

        // Trk_Iomedae_Refusal: after a no, her silence (a page), and the yes still reachable at the Wound; after the vow, the orders.
        check(Avail(S(P + "silence"), Later(boast, 48)) && !Avail(S(P + "silence"), Later(yes, 48))
              && Reachable(eve, World(story, 6, "trickster.ever", Started, Latch, Held, Committed, P + "cost.buried_to_the_world")).Any(x => x.Contains("costs in ink"))
              && !Reachable(eve, World(story, 6, "trickster.ever", Started, Latch, Held, Committed)).Any(x => x.Contains("costs in ink"))
              && own.Count(x => x.Remote && x.Chapters.Contains(6)) <= 2,
            "Trk_Iomedae_Refusal: the refusal has no aftermath, or the orders are written without the vow.");

        // Trk_Iomedae_Heat: after her concession, the dream she chooses; the kiss, the buckle held, the promise of where.
        var c5c = World(story, 5, "trickster.ever", Started, Committed);
        check(Avail(mortal, c5c) && !Avail(mortal, World(story, 5, "trickster.ever", Started, Declined)) && mortal.Chapters.SequenceEqual(new[] { 5, 6 })
              && Reachable(mortal, c5c).Any(x => x.Contains("Not in a dream")) && Reachable(mortal, c5c).Any(x => x.Contains("Where it flew")),
            "Trk_Iomedae_Heat: the dream of her mortal self is missing, or plays without her concession.");

        // Trk_Iomedae_Eve: the night before Threshold in her own voice; she has not decided.
        check(Avail(eve, World(story, 6, "trickster.ever", Started, Latch, Held)) && Avail(eve, World(story, 6, "trickster.ever", Started, Latch, Order))
              && !Avail(eve, World(story, 6, "trickster.ever", Started, Latch))
              && Reachable(eve, World(story, 6, "trickster.ever", Started, Latch, Held, Committed)).Any(x => x.Contains("I did not promise that I will")),
            "Trk_Iomedae_Eve: the eve dream is missing, or promises the answer.");

        // Trk_Iomedae_Threshold: the device act beside the native sacrifice (E14b); committed carries; after a refusal the truth
        // concedes at the Wound (the reachable yes, no price) and a joke closes; never argued, the argument is made there.
        var t6 = new[] { "trickster", "trickster.ever", Started, Latch, Held, P + "first_spoken" };
        var tc = World(story, 6, t6.Concat(new[] { Committed }).ToArray());
        var td = World(story, 6, t6.Concat(new[] { Declined, P + "cost.boasted", P + "disputed" }).ToArray());
        var tn = World(story, 6, t6);
        check(Avail(wound, tc) && Avail(wound, td) && Avail(wound, tn) && !Avail(wound, World(story, 6, "trickster", "trickster.ever", Started, Latch))
              && Avail(wound, World(story, 6, "trickster", "trickster.ever", Started, Latch, Order))
              && wound.Chapters.SequenceEqual(new[] { 6 }),
            "Trk_Iomedae_Threshold: the banner cannot be unfurled at the Wound where it should (or can without a banner).");
        check(Take(wound, tc, "go", 0, Carried).Has(Carried) && Take(wound, tc, "kiss", 0, Carried).Has(P + "kissed_at_wound"),
            "Trk_Iomedae_Threshold: a committed Commander does not carry the banner in.");
        var truth = Take(wound, td, "decide", 0, Committed, P + "conceded_at_wound", Carried);
        var joke = Take(wound, td, "turned", 0, Closed, Carried);
        var late = Take(wound, tn, "decide", 0, Committed, P + "conceded_at_wound");
        check(truth.Has(P + "cost.buried_to_the_world") && joke.Has(Closed) && !joke.Has(Committed) && late.Has(Carried)
              && Take(wound, tn, "refused", 0, Declined).Has(Carried)
              && Take(wound, World(story, 6, "trickster", "trickster.ever", Started, Latch, Held), "rescue", 0, P + "rescue_only").Has(Carried)
              && !Paths(wound, World(story, 6, "trickster", "trickster.ever", Started, Latch, Held)).Any(o => o.state.Has(Committed))
              && Take(wound, tn, "rescue", 0, P + "rescue_only").Has(P + "cost.buried_to_the_world")
              && wound.Nodes.SelectMany(n => n.Choices).All(c => c.Crusade == null && c.Alignment == null && c.NativeNext == null)
              && Ch(wound, "plant", 2).Abort,
            "Trk_Iomedae_Threshold: after her refusal the truth does not concede at the Wound (or the joke does not close), or the act has a fee.");

        // Trk_Iomedae_RefusalByCause: the Wound answers the offence that was given (the boast, the mocked madness, the lie).
        var tm = World(story, 6, t6.Concat(new[] { Declined, P + "cost.madness_mocked", P + "disputed" }).ToArray());
        var tl = World(story, 6, t6.Concat(new[] { Declined, P + "cost.lied", P + "disputed", Order, P + "cost.banner_stolen" }).ToArray());
        check(Take(wound, tm, "d_mock", 0, Committed).Has(P + "answered.madness") && Take(wound, tl, "d_lie", 0, Committed).Has(P + "answered.theft")
              && !Reachable(wound, tm).Any(x => x.Contains("sure thing")) && !Reachable(wound, tl).Any(x => x.Contains("sure thing"))
              && Take(wound, tm, "d_mock", 1, Closed).Has(Closed),
            "Trk_Iomedae_RefusalByCause: the recovery at the Wound does not answer the offence actually given.");
        var foughtW = World(story, 5, "trickster.ever", Started, Latch, "iomedae.herald_fought");
        check(Avail(heraldDream, foughtW) && !Reachable(heraldDream, foughtW).Any(x => x.Contains("He is gone")),
            "Trk_Iomedae_Herald: a fight alone is told as his death.");

        // Trk_Iomedae_Worlds: the bridge world (she answered) joins commander_back; its pages play; the others in theirs.
        Scene Pg(string id) => S(P + "epilogue." + id);
        var bridgeW = World(story, 6, "trickster.ever", Started, Committed, Carried, "sacrifice", "ending.wound_closed", Held, P + "cost.buried_to_the_world");
        check(bridgeW.Has(Kept) && bridgeW.Has("trickster.commander_back") && bridgeW.Has(P + "cost.miracle_owed")
              && story.Derived["trickster.commander_back"].Any(gr => gr.Length == 1 && gr[0] == Kept),
            "Trk_Iomedae_Worlds: the bridge world is not a Commander who came back (ledger row 16).");
        check(!World(story, 6, "trickster.ever", Started, Carried, Declined, "sacrifice", "ending.wound_closed").Has(Kept)
              && !World(story, 6, "trickster.ever", Started, Committed, "sacrifice", "ending.wound_closed").Has(Kept)
              && !World(story, 6, "trickster.ever", Started, Committed, Carried, "sacrifice").Has(Kept),
            "Trk_Iomedae_Worlds: she answers a banner she was not argued into, one never raised, or a Wound left open.");
        check(Avail(Pg("bridge"), bridgeW) && Avail(Pg("platform"), bridgeW) && Avail(Pg("after"), bridgeW)
              && !Avail(Pg("lived"), bridgeW) && !Avail(Pg("unanswered"), bridgeW) && !Avail(Pg("respect"), bridgeW),
            "Trk_Iomedae_Worlds: the bridge world does not play the bridge, the platform and the after (and only those).");
        var livedW = World(story, 6, "trickster.ever", Started, Committed, "ending.wound_closed");
        var openW = World(story, 6, "trickster.ever", Started, Committed, Carried, "sacrifice", "ending.trickster");
        check(Avail(Pg("lived"), livedW) && Avail(Pg("platform"), livedW) && !Avail(Pg("bridge"), livedW)
              && Avail(Pg("lived"), openW) && Reachable(Pg("lived"), openW).Any(x => x.Contains("told a joke instead")),
            "Trk_Iomedae_Worlds: a committed Commander who lived without the bridge has no page (or the wrong one).");
        var lostW = World(story, 6, "trickster.ever", Started, Committed, "sacrifice", "ending.wound_closed");
        var boastedDead = World(story, 6, "trickster.ever", Started, Declined, P + "cost.boasted", Carried, "sacrifice", "ending.wound_closed");
        check(Avail(Pg("unanswered"), lostW) && !Avail(Pg("platform"), lostW) && Render(Pg("unanswered"), lostW).Contains("never raised")
              && Avail(Pg("unanswered"), boastedDead) && Render(Pg("unanswered"), boastedDead).Contains("offered her a bargain")
              && Pg("unanswered").Forbids.Contains(Active),
            "Trk_Iomedae_Worlds: a Commander she did not answer is not mourned by her page (or it plays beside Last Call's flask).");
        var watched = World(story, 6, "trickster.ever", Started, Declined);
        // Epilogue pages ignore the ClosedFlag (Rules.Available returns before the relationship check), so a closed route's
        // refusal paragraphs do render: the Commander's own no is told.
        var closedW = World(story, 6, "trickster.ever", Started, Closed, P + "sent_away");
        check(Avail(Pg("respect"), closedW) && Render(Pg("respect"), closedW).Contains("moved your bed")
              && Avail(Pg("respect"), watched) && !Avail(Pg("respect"), World(story, 6, "trickster.ever", Started, Committed)),
            "Trk_Iomedae_Worlds: an uncommitted Commander who lived has no page.");
        check(pages.All(pg => pg.Nodes.All(n => n.Choices.All(c => c.Set.Length == 0))) && pages.Length == 8
              && Avail(Pg("gate"), bridgeW) && !Avail(Pg("gate"), livedW),
            "Trk_Iomedae_Pages: a page sets a flag, or a page is missing.");
        var h2 = World(story, 6, "trickster.ever", Started, Committed, Carried, "sacrifice", "ending.wound_closed", Held,
            "trickster.lastcall.taken", "trickster.lastcall.pillar.bottle");
        check(h2.Has(Active) && h2.Has(Kept) && Avail(Pg("bridge"), h2) && Render(Pg("bridge"), h2).Contains("a flask corked in your fist")
              && !Render(Pg("bridge"), h2).Contains("remarkably unoccupied") && Render(Pg("bridge"), bridgeW).Contains("remarkably unoccupied"),
            "Trk_Iomedae_Worlds: with Last Call's flask the bridge page contradicts Areelu's report (found three days later).");
        var orderW = World(story, 6, "trickster.ever", Started, Committed, Carried, "sacrifice", "ending.wound_closed", Order);
        check(Reachable(Pg("bridge"), orderW).Any(x => x.Contains("burned to the bone")) && !Reachable(Pg("bridge"), bridgeW).Any(x => x.Contains("burned to the bone")),
            "Trk_Iomedae_Worlds: the cathedral's banner does not cost the banner hand at the bridge.");

        // Trk_Iomedae_Rescued: the argument conceded without the other thing: she answers, and there is no romance.
        var rescuedW = World(story, 6, "trickster.ever", Started, Carried, P + "rescue_only", "sacrifice", "ending.wound_closed", Held);
        check(rescuedW.Has(P + "rescued") && rescuedW.Has("trickster.commander_back") && rescuedW.Has(P + "buried_alive") && !rescuedW.Has(Kept)
              && Avail(Pg("rescued"), rescuedW) && !Avail(Pg("platform"), rescuedW) && !Avail(Pg("respect"), rescuedW) && !Avail(Pg("unanswered"), rescuedW)
              && !Avail(Pg("bridge"), rescuedW),
            "Trk_Iomedae_Rescued: a rescue without the personal concession plays the romance, or nothing.");
        // Galfrey's continuing public life yields to the buried Commander (audit r2, COX).
        var galfreyW = World(story, 6, "trickster.ever", Started, Committed, Carried, "sacrifice", "ending.wound_closed", Held, "galfrey.final", "galfrey.committed");
        check(!Avail(S("galfrey.trickster.epilogue.alive"), galfreyW) && Avail(S("galfrey.trickster.epilogue.alive_buried"), galfreyW)
              && Avail(S("galfrey.trickster.epilogue.alive"), World(story, 6, "trickster.ever", "galfrey.final", "galfrey.committed")),
            "Trk_Iomedae_Coexist: Galfrey's queen-and-general ending plays beside a Commander who is a grave.");

        // Trk_Iomedae_Intimacy: on the bare platform, after Threshold, she in plain steel; the cut at the first motion astride.
        var plat = Pg("platform");
        check(plat.Nodes.Single(n => n.Id == "down").Text.Contains("comes up astride") && plat.Nodes.Single(n => n.Id == "cloak").Text.Contains("It has been a bridge")
              && Reachable(plat, bridgeW).Any(x => x.Contains("sally port")) && !Reachable(plat, livedW).Any(x => x.Contains("sally port")),
            "Trk_Iomedae_Intimacy: the platform night is not staged to the cut, or the buried Commander is not hidden.");

        // Trk_Iomedae_Reactions: Seelah, Sosiel, Daeran (twice), each on their hub, guarded.
        check(reactions.Length == 6 && S(P + "react.seelah").Requires.Contains("seelah.in_party") && S(P + "react.seelah").AnswerLists.SequenceEqual(new[] { "417fa384f3250634bb71859fbc913453" })
              && S(P + "react.sosiel").Forbids.Contains("sosiel.dead") && S(P + "react.sosiel").AnswerLists.SequenceEqual(new[] { "129b55b8b5d50974f84f7c607d894fd0" })
              && S(P + "react.daeran").Forbids.Contains("daeran.dead") && S(P + "react.daeran_lost").Forbids.Contains(Committed)
              && Avail(S(P + "react.seelah"), World(story, 5, "trickster.ever", P + "disputed", "seelah.in_party"))
              && !Avail(S(P + "react.seelah"), World(story, 5, "trickster.ever", P + "disputed", "seelah.in_party", "seelah_dead"))
              && S(P + "react.seelah_eve").MaxChapter == 6 && S(P + "react.sosiel_frame").Requires.Contains(P + "react.sosiel")
              && reactions.All(r => r.Forbids.Any(f => f.EndsWith(".dead") || f.EndsWith("_dead"))),
            "Trk_Iomedae_Reactions: a reactor is missing, off their hub, or unguarded.");

        // Trk_Iomedae_Chain: the whole spine walked in order with advancing time, from the first dream to the bridge world.
        var w0 = World(story, 3, "trickster", "trickster.ever");
        foreach (var native in new[] { "trickster", "trickster.ever", "chapter_later" }) w0.Times.Remove(native);
        var w1 = Take(first, w0, "wake", 1, Started);
        var w2 = Take(question, Later(w1, 1), "ask", 1, P + "question_sent");
        var w3 = Take(answer, Later(w2, 24), "warn", 0, P + "herald_answered");
        var w4 = Take(chasm, Later(w3, 1), "wake", 1, P + "bridge_seen");
        var w5 = Later(w4, 24, chapter: 5);
        w5.Flags.Add("iomedae.key_dies_revealed"); w5.Times["iomedae.key_dies_revealed"] = w5.Hour;
        Rules.Complete(story, w5);
        var w6 = Take(bare, Later(w5, 12), "wager", 1, P + "plan.wager");
        var w7 = Later(w6, 100, area: "00000000000000000000000000000000");
        w7.Flags.Add(Held); w7.Times[Held] = w7.Hour; w7.Flags.Add("iz.done"); w7.Times["iz.done"] = w7.Hour;
        Rules.Complete(story, w7);
        var w8 = Take(izNight, Later(w7, 6), "win", 0, Called);
        var w9 = Take(disp, Later(w8, 24, area: Drezen), "rain", 0, Committed);
        var w10 = Take(mortal, Later(w9, 24), "where", 0, P + "mortal_seen");
        var w11 = Take(eve, Later(w10, 24, chapter: 6), "there", 0, P + "eve_seen");
        var w12 = Take(wound, Later(w11, 12), "go", 0, Carried);
        w12.Flags.UnionWith(new[] { "sacrifice", "ending.wound_closed" });
        Rules.Complete(story, w12);
        check(w12.Has(Kept) && Avail(Pg("bridge"), w12) && Avail(Pg("platform"), w12) && Avail(Pg("after"), w12),
            "Trk_Iomedae_Chain: the spine does not walk from the first dream to the bridge world.");

        // Trk_Iomedae_LastCall and the household: eligible only by her concession; the coda and the Ledger line.
        var coda = story.Scenes.Single(s => s.Id == "iomedae.lastcall.page");
        check(coda.Requires.Contains(Committed) && coda.Requires.Contains(Active) && coda.Forbids.Contains(Declined) && coda.ForbidOverrides[Declined] == Committed
              && !story.Scenes.Any(s => s.Id == "iomedae.lastcall.call")
              && Render(coda, h2).Contains("never saw the second"),
            "Trk_Iomedae_LastCall: her coda is not wired to her concession, or it has a call-in (her debt is made at the rift).");
        check(story.Derived["iomedae.harem.eligible"].Any(gr => gr.Length == 1 && gr[0] == Committed)
              && story.Derived[P + "late_committed"].Single().SequenceEqual(new[] { "trickster.ever", Committed })
              && !World(story, 6, "trickster.ever", Started, Declined).Has("iomedae.harem.eligible")
              && World(story, 5, "trickster.ever", Committed).Has("iomedae.harem.eligible"),
            "Trk_Iomedae_Household: eligibility follows something other than her concession.");

        Console.WriteLine("PASS: Iomedae Trickster (Trk_Iomedae_*): veiled until Threshold, " + own.Length + " scenes, the disputation and its refusals, the banner (or the cathedral's), the Threshold act, the bridge world, " + pages.Length + " pages, " + reactions.Length + " reactions, Last Call's coda, eligibility.");
    }
}
