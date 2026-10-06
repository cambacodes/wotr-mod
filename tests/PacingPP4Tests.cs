using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// Pacing pass PP4 (Writer/handoffs/13-PACING-PASS.md sections 2a, 4, 7, 9; 15b-EARLY-THREADS.md T1 acceptance A1, A1b, A2, A9,
// A9b, A9c; storylines/pacing_pp4.py): Gresilla's borrowed credit (Chapter 3, Trickster), Nocticula's hoard (Chapter 4 in
// person) and Kiana's wedding court (Chapter 3). Per beat: host, return-to-list, gate at its moment and absent at a wrong one on
// the same list, chapter window, once-only (abort included), one outcome per terminal path, no native key, no time spent (no
// Chapter 3 native romance key delayed), inert readers, and the readers appended without moving any existing index.
internal static class PacingPP4Tests
{
    private const string Credit = "nocticula.early.gresilla_credit";
    private const string Delivered = "nocticula.early.gresilla_delivered";
    private const string Credited = "nocticula.gresilla_credited";
    private const string Exposed = "nocticula.gresilla_exposed";
    private const string Hoard = "nocticula.ch4.hoard";
    private const string Cast = "kiana.wedding.cast";
    private static readonly string[] Audiences = { "noct.acq.audience_missed", "noct.acq.audience_rejected", "noct.acq.audience_patronage" };

    private sealed record Beat(string Id, string Relationship, int Chapter, string List, string[] Outcomes, string[] Gate, string Wrong, bool Trickster);

    private static readonly Beat[] Beats = {
        new(Credit, "nocticula", 3, "8a69c5acce98db74d87ff06fdcf1b975", new[] { Credit, Credit + ".declined" },
            new[] { "trickster", "gresilla.darrazand_heard" }, "gresilla.attacked", true),
        new(Hoard, "nocticula", 4, "09a3f2100af13ae429e1dedf27e32a80",
            new[] { Hoard + ".appraised", Hoard + ".bitten", Hoard + ".spent", Hoard + ".declined" }, new[] { "noct.ch4.nahyndri_told" }, "", false),
        new(Cast, "kiana", 3, "ad91a2aed6132554782ca2ad10a1ee2a",
            new[] { Cast + ".captive", Cast + ".hunter", Cast + ".guest", Cast + ".declined" }, Array.Empty<string>(), "kiana.ceremony_begun", false),
    };

    // Scenes allowed to read each beat's flags (besides the beat itself).
    private static readonly Dictionary<string, string[]> Readers = new()
    {
        [Credit] = Array.Empty<string>(),   // read through the Derived delivery key only
        [Hoard] = Audiences,
        [Cast] = new[] { "kiana.trickster.ward_rounds" },
    };

    private static Snapshot At(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 3000, Area = "" };
        state.Flags.UnionWith(flags);
        if (Rules.ChapterFlag(chapter) is string chapterFlag) state.Flags.Add(chapterFlag);
        Rules.Complete(story, state);
        return state;
    }

    private static IEnumerable<string> Reads(Scene s) => s.Requires.Concat(s.Forbids).Concat(s.RequiresAny)
        .Concat(s.RequiresAnyGroups.SelectMany(g => g))
        .Concat(s.Nodes.SelectMany(n => n.Choices).SelectMany(c => c.Requires.Concat(c.Forbids)))
        .Concat(s.Nodes.SelectMany(n => n.Paragraphs).SelectMany(p => p.Requires.Concat(p.Forbids).Concat(p.AnyGroups.SelectMany(g => g))));

    private static bool Shown(Paragraph line, Snapshot s) =>
        line.Requires.All(s.Has) && !line.Forbids.Any(s.Has) && line.AnyGroups.All(g => g.Any(s.Has));

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Node N(Scene scene, string node) => scene.Nodes.Single(n => n.Id == node);
        IEnumerable<Choice> Choices(Scene s) => s.Nodes.SelectMany(n => n.Choices);
        var native = new HashSet<string>(Rules.NativeKeys(story));

        // Bindings (verified in blueprints.zip, 2026-10-01).
        check(story.SeenCues.TryGetValue("gresilla.darrazand_heard", out var heard) && heard.SequenceEqual(new[] { "0fd2a480a6c73694abb54dbb0f2bc470" }),
            "PP4: gresilla.darrazand_heard is not NocticulaPriestess Cue_0014.");
        check(story.SelectedAnswers.TryGetValue("gresilla.attacked", out var attack) && attack == "23d2a8e402c2a3c45a3c2976b042aa4f",
            "PP4: gresilla.attacked is not her [Attack] Answer_0003.");
        check(story.StartedDialogs.TryGetValue("fane.darrazand_defeated", out var fane) && fane == "878ad1608527aec41b3a87bfe8afdbcd",
            "PP4: the Fane delivery is not MidnightFaneFinal_dialog.");
        check(story.SeenCues.TryGetValue("noct.ch4.nahyndri_told", out var told) && told.SequenceEqual(new[] { "018edb7d408b5e84eabcab2dfc1b38ec" }),
            "PP4: noct.ch4.nahyndri_told is not Nocticula_main Cue_0206.");
        check(story.SeenCues.TryGetValue("kiana.ceremony_begun", out var ceremony) && ceremony.SequenceEqual(new[] { "7b2d088e3a4ebc94787276799bb4d2d8" }),
            "PP4: kiana.ceremony_begun is not WeddingUnexpected Cue_0001.");
        check(story.Derived.TryGetValue(Delivered, out var delivered) && delivered.Length == 1
              && delivered[0].OrderBy(x => x).SequenceEqual(new[] { "fane.darrazand_defeated", Credit }), "PP4: the T1 delivery key is not credit + the Fane report.");

        foreach (var b in Beats)
        {
            var scene = S(b.Id);
            check(scene.Relationship == b.Relationship && scene.AnswerLists.SequenceEqual(new[] { b.List })
                  && Rules.EntryTargets(scene).SequenceEqual(new[] { b.List }), b.Id + ": wrong relationship or host list.");
            check(scene.ReturnToList && scene.NativeReturnCue == null && !string.IsNullOrWhiteSpace(scene.ReturnText),
                b.Id + ": not a return-to-list beat with its own return line.");
            check(scene.Chapters.SequenceEqual(new[] { b.Chapter }) && scene.MinChapter == b.Chapter && scene.MaxChapter == b.Chapter && scene.Optional,
                b.Id + ": the window is not its host's chapter.");
            check(!string.IsNullOrWhiteSpace(scene.Entry), b.Id + ": empty inline entry.");
            // No native time: inline, no delay, not a rest delivery (13 section 9: no Chapter 3 romance key is delayed).
            check(!scene.Remote && scene.DelayHours == 0, b.Id + ": spends time (remote or delayed).");

            var open = At(story, b.Chapter, b.Gate);
            check(Rules.Available(story, scene, open), b.Id + ": closed at its own moment.");
            check(!Rules.Available(story, scene, At(story, b.Chapter + 1, b.Gate)), b.Id + ": open a chapter late.");
            check(!Rules.Available(story, scene, At(story, b.Chapter - 1, b.Gate)), b.Id + ": open a chapter early.");
            foreach (var g in b.Gate)
                check(!Rules.Available(story, scene, At(story, b.Chapter, b.Gate.Where(x => x != g).ToArray())), b.Id + ": open without " + g + ".");
            if (b.Wrong != "")
                check(!Rules.Available(story, scene, At(story, b.Chapter, b.Gate.Append(b.Wrong).ToArray())), b.Id + ": open after " + b.Wrong + ".");
            if (!b.Trickster)
                check(Rules.Available(story, scene, At(story, b.Chapter, b.Gate.Append("trickster").ToArray()))
                      && !Reads(scene).Any(f => f == "trickster" || f == "trickster.ever"), b.Id + ": an N-all beat reads the Trickster.");

            // Branches: every first-node choice records .seen; every terminal path (abort included) sets exactly one outcome.
            check(scene.Nodes[0].Choices.All(c => c.Set.Contains(b.Id + ".seen")), b.Id + ": a first-node choice does not record .seen.");
            check(b.Outcomes.Append(b.Id + ".seen").All(scene.Forbids.Contains), b.Id + ": Forbids lack an outcome or .seen.");
            var outcomes = Program.Walk(scene, open);
            check(outcomes.All(o => b.Outcomes.Count(o.Has) == 1 && o.Has(b.Id + ".seen")), b.Id + ": a terminal path sets no outcome, or more than one.");
            check(b.Outcomes.All(f => outcomes.Any(o => o.Has(f))), b.Id + ": an outcome is unreachable.");
            check(Choices(scene).All(c => c.Check == null && c.StartEtude == null && c.Mythic == null && c.Revive == null && c.NativeNext == null
                                          && c.Set.All(f => !native.Contains(f))), b.Id + ": a check, an etude, a native key or a native jump.");
            check(!Reads(scene).Any(f => f.Contains(".harem") || f.EndsWith(".committed", StringComparison.Ordinal)), b.Id + ": reads a harem or committed flag.");
            check(Choices(scene).Count(c => c.Abort) == 1, b.Id + ": no single abort.");

            // Once: played or interrupted after the first answer, it never comes back; before it, nothing is set (A9, A9c).
            foreach (var played in outcomes)
            {
                var again = Program.Copy(played); again.Hour += 200;
                check(!Rules.Available(story, scene, again), b.Id + ": replaying the host offers the beat again.");
            }
            check(!Rules.Available(story, scene, At(story, b.Chapter, b.Gate.Append(b.Id + ".seen").ToArray())), b.Id + ": an interrupted beat is offered again.");

            // Inert readers.
            var mine = new HashSet<string>(b.Outcomes.Append(b.Id + ".seen").Append(b.Id));
            var readers = story.Scenes.Where(s => s.Id != b.Id && Reads(s).Any(mine.Contains)).Select(s => s.Id).OrderBy(x => x).ToArray();
            check(readers.SequenceEqual(Readers[b.Id].OrderBy(x => x)), b.Id + ": unexpected readers: " + string.Join(", ", readers));
            check(!story.Scenes.Where(s => s.Id != b.Id).SelectMany(s => Choices(s)).Any(c => c.Set.Any(mine.Contains)), b.Id + ": another scene sets its flags.");
        }

        // T1 (A1): the spoken offer commits credit, .seen and Chaotic 1; "Forget I said it" is an abort that consumes the beat.
        var credit = S(Credit);
        var ask = credit.Nodes[0].Choices;
        check(ask.Count == 2 && ask[0].Next == "sent" && ask[0].Set.Contains(Credit) && ask[0].Alignment?.Direction == "Chaotic"
              && ask[1].Abort && ask[1].Set.SequenceEqual(new[] { Credit + ".declined", Credit + ".seen" }), "T1: ask is not [offer, abort].");
        check(credit.Nodes.Where(n => n.Id != "ask").All(n => n.Speaker == "conversant") && credit.Nodes[0].Speaker == "conversant",
            "T1: Gresilla's nodes do not speak through the conversant.");

        // A1b: delivery only after the report to the Queen.
        var credited = At(story, 5, "trickster", Credit);
        var reported = At(story, 5, "trickster", Credit, "fane.darrazand_defeated");
        check(!credited.Has(Delivered) && reported.Has(Delivered) && reported.Has("trickster.secret.gresilla_harp"), "T1: delivery does not wait for the Fane.");

        // A2: the payoff at request, in every audience variant; [0]/[1] keep their places; [2]/[3] only after delivery.
        foreach (var id in Audiences)
        {
            var audience = S(id);
            var request = N(audience, "request").Choices;
            check(request[0].Next == "price" && request[1].Next == "decline" && request.Count >= 7, id + ": request lost its original answers.");
            var harp = request.FindIndex(c => c.Next == "harp");
            var author = request.FindIndex(c => c.Next == "author");
            check(harp == 2 && author == 3, id + ": the T1 answers are not request [2]/[3].");
            check(!Rules.Match(request[2].Requires, request[2].Forbids, credited) && Rules.Match(request[2].Requires, request[2].Forbids, reported)
                  && Rules.Match(request[3].Requires, request[3].Forbids, reported), id + ": the T1 answers ignore delivery.");
            check(N(audience, "harp").Choices.All(c => c.Next == "price") && N(audience, "author").Choices.All(c => c.Next == "price"),
                id + ": a T1 branch skips her price.");
            var authorChoices = N(audience, "author").Choices;
            check(authorChoices.All(c => c.Set.Contains(Exposed) && c.Set.Contains("noct.acq.author_offer") && c.Set.Contains("noct.acq.collateral_given")
                                         && c.Set.Count(f => f.StartsWith("noct.acq.pledge_", StringComparison.Ordinal)) == 1),
                id + ": exposure and pledge are not written together.");
            check(request[3].Set.Length == 0, id + ": author records the exposure before the pledge.");
            var walk = Program.WalkVia(audience, Program.Copy(reported).Also("noct.acq.audience_question"), "request", 2);
            check(walk.Count > 0 && walk.All(o => o.Has(Credited)), id + ": the harp answer does not reach an ending with the standing kept.");
            // The Chapter 4 recall: one answer per stance, appended after the T1 pair, each visible only with its stance.
            foreach (var (stance, at) in new[] { ("appraised", 4), ("bitten", 5), ("spent", 6) })
            {
                var choice = request[at];
                var with = At(story, 5, "trickster", Hoard + "." + stance);
                check(choice.Next == "hoard_" + stance && Rules.Match(choice.Requires, choice.Forbids, with)
                      && !Rules.Match(choice.Requires, choice.Forbids, At(story, 5, "trickster", Hoard + ".declined"))
                      && N(audience, "hoard_" + stance).Choices.All(c => c.Next == "price"), id + ": the Chapter 4 " + stance + " recall is wrong.");
            }
        }

        // The pledge and the retained standing are called in at her_hand/terms (15b residual).
        var hand = S("noct.acq.her_hand");
        var terms = N(hand, "terms").Choices;
        check(terms[0].Next == null && new[] { "noct.acq.pledge_names", "noct.acq.pledge_fear", Credited }.All(terms[0].Forbids.Contains),
            "her_hand: the original terms answer still shows for a pledged or credited Commander.");
        foreach (var (flag, node) in new[] { ("noct.acq.pledge_names", "call_names"), ("noct.acq.pledge_fear", "call_fear"), (Credited, "call_harp") })
        {
            var twin = terms.FindIndex(c => c.Next == node);
            check(twin >= 1 && terms[twin].Requires.SequenceEqual(new[] { flag }), "her_hand: no call-in for " + flag + ".");
            var state = At(story, 5, flag, "noct.acq.channel_narrow");
            var ends = Program.WalkVia(hand, state, "terms", twin);
            check(ends.Count >= 2 && ends.All(o => o.Has("noct.acq.her_hand_done") && o.Has("noct.acq.correspondence_trial")),
                "her_hand: a call-in loses the trial correspondence (" + node + ").");
        }

        // The Ledger's Secrets page (durable reader).
        var page = story.Books["trickster.ledger"].Entries.Single(e => e.Id == "early.gresilla_harp");
        check(page.Section == "Secrets" && page.Requires.SequenceEqual(new[] { "trickster.secret.gresilla_harp" }), "T1: the Ledger page is not a Secrets page.");
        var dupe = new Snapshot(); dupe.Flags.UnionWith(new[] { Delivered });
        var sold = new Snapshot(); sold.Flags.UnionWith(new[] { Delivered, Exposed, "noct.acq.pledge_fear" });
        check(page.Lines.Count(l => Shown(l, dupe)) == 1 && Shown(page.Lines[0], dupe), "T1: the dupe's Ledger line is wrong.");
        check(!Shown(page.Lines[0], sold) && Shown(page.Lines[1], sold) && Shown(page.Lines[4], sold), "T1: the exposed Ledger lines are wrong.");

        // Kiana's wedding, recalled on her rounds: [0]-[3] keep their places; one answer per stance.
        var rounds = S("kiana.trickster.ward_rounds");
        var start = N(rounds, "start").Choices;
        check(start.Count >= 9 && start.Take(7).Select(c => c.Next).SequenceEqual(
            new[] { "rounds", "wrist", "wrist", "wrist_early", "court_captive", "court_hunter", "court_guest" }),
            "ward_rounds: an original answer moved.");
        foreach (var (stance, at) in new[] { ("captive", 4), ("hunter", 5), ("guest", 6) })
        {
            var choice = start[at];
            check(choice.Next == "court_" + stance && Rules.Match(choice.Requires, choice.Forbids, At(story, 5, Cast + "." + stance))
                  && !Rules.Match(choice.Requires, choice.Forbids, At(story, 5, Cast + ".declined"))
                  && N(rounds, "court_" + stance).Choices[0].Next == "rounds"
                  && N(rounds, "court_" + stance).Choices[0].Requires.Contains("kiana.trickster.ward_guests_home"),
                "ward_rounds: the " + stance + " recall lost its saved target or release gate.");
        }

        // P3: all five callers retain their saved rounds answer and append the
        // captive/postponed histories. A wedding stance alone never frees guests.
        foreach (var caller in new[] { "start", "wrist_early", "court_captive", "court_hunter", "court_guest" })
        {
            var choices = N(rounds, caller).Choices;
            int appended = caller == "start" ? 7 : 1;
            check(choices[0].Next == "rounds"
                  && choices[appended].Next == "rounds_captive"
                  && choices[appended + 1].Next == "rounds_no_wedding",
                "ward_rounds: saved/appended targets changed at " + caller);
            foreach (var stance in new[] { "captive", "hunter", "guest" })
            foreach (var receipt in new[] { "", "seelah.souls_returned", "kiana.trickster.guests_ransomed", "kiana.trickster.guests_bought_back" })
            foreach (bool postponed in new[] { false, true })
            {
                var flags = new List<string> { "trickster", Cast + "." + stance };
                if (receipt != "") flags.Add(receipt);
                if (postponed) flags.Add("kiana.history_betrothed");
                var state = At(story, 5, flags.ToArray());
                string target = postponed ? "rounds_no_wedding" : receipt == "" ? "rounds_captive" : "rounds";
                var histories = choices.Where(c => new[] { "rounds", "rounds_captive", "rounds_no_wedding" }.Contains(c.Next))
                    .Where(c => Rules.ChoiceAvailable(c, state)).ToArray();
                check(histories.Length == 1 && histories[0].Next == target,
                    "ward_rounds: wrong or overlapping history at " + caller + "/" + stance + "/" + receipt + "/" + postponed);
                var outcomes = Program.WalkVia(rounds, state, caller, choices.IndexOf(histories[0]));
                bool matchingStance = !caller.StartsWith("court_", StringComparison.Ordinal) || caller == "court_" + stance;
                check(matchingStance ? outcomes.Count > 0 && outcomes.All(o => o.Has("kiana.trickster.rounds_kept")) : outcomes.Count == 0,
                    "ward_rounds: wrong recall reachability or completion at " + caller + "/" + stance + "/" + target);
            }
        }

        // The hosts belong to their own dialogs: no other RRT scene rides them.
        foreach (var b in Beats)
            check(story.Scenes.Where(s => Rules.EntryTargets(s).Contains(b.List)).Select(s => s.Id).SequenceEqual(new[] { b.Id }),
                b.Id + ": another scene rides its host list.");
    }

    private static Snapshot Also(this Snapshot s, string flag) { s.Flags.Add(flag); return s; }
}
