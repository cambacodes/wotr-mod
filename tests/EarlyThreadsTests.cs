using System;
using System.Collections.Generic;
using System.Linq;
using Tirabade;

// The PP9 early threads (Writer/handoffs/15b-EARLY-THREADS.md, acceptance A3-A9 at rules level):
// T2 Hepzamirah <- Voetiel (the Moon priced through her fleeing lash, Woljif's reckoning, the ghost's callback) and
// T3 Shamira <- Telmer (the swallowed tally bought with his freedom, his letter, her find in the Harem).
// Gates, abort paths, once-only consumption, exactly one outcome per terminal path, index safety of the payoffs, and the
// consequence readers (the Ledger lines, Woljif's Chapter 5 answer, the manifest variants).
internal static class EarlyThreadsTests
{
    private const string Q2Dead = "74e18303ff0d4db40b235cd5a38ef12e";
    private const string Q2Alive = "78ff106a5d3b42d4b96adcbd1d1b626c";
    private const string Q3Hub = "cdf898c8df8913340b7b9341590d4117";
    private const string Woljif = "766435873b1361c4287c351de194e5f9";
    private const string Voetiel = "d75ee7e088ea2d64b8b602e2e59ad6a5";
    private const string Dissipate = "a4011b00473994b4dadc6aed381cf504";
    private const string TelmerHub = "ca6d1fdb3b2e1cd42a995788f05efdb2";
    private const string TelmerReturn = "0ff9dfa1944f90b4cb8fb2ceaefadf4b";
    private const string TelmerRelease = "51e53730da8c07443be9a463ed33edcd";
    private const string Moon = "hepzamirah.early.moon_message";
    private const string Reckon = "hepzamirah.early.moon_reckoning";
    private const string Bluff = "woljif.told_bluff";
    private const string Promised = "woljif.moon_promised";
    private const string Doubt = "woljif.moon_doubt";
    private const string Interrogation = "shamira.early.telmer_interrogation";
    private const string Notes = "shamira.early.telmer_notes";
    private const string Exposed = "shamira.early.telmer_exposed";
    private const string Failed = "shamira.early.telmer_failed";
    private const string Letter = "shamira.early.telmer_letter";
    private const string Kept = Letter + ".kept";
    private const string Burned = Letter + ".burned";
    private const string H = "hepzamirah.trickster.";

    private static Snapshot World(Story story, int chapter, params string[] flags)
    {
        var state = new Snapshot { Chapter = chapter, Hour = 5000, Area = "2570015799edf594daf2f076f2f975d8" };
        state.Flags.UnionWith(flags);
        state.Flags.Add(chapter == 1 ? "chapter_one" : "chapter_later");
        state.AvailableContacts.Add("bd2a925967b5f5f489f6da0b03236d03");
        state.AvailableContacts.Add("78549b805f0a63e41805cfe3e02e2ea8");
        Rules.Complete(story, state);
        foreach (var flag in state.Flags.ToList()) state.Times[flag] = state.Hour - 200;
        return state;
    }

    private static bool Shown(Paragraph line, Snapshot s) =>
        line.Requires.All(s.Has) && !line.Forbids.Any(s.Has) && line.AnyGroups.All(g => g.Any(s.Has));

    internal static void Run(Story story, Action<bool, string> check)
    {
        Scene S(string id) => story.Scenes.Single(s => s.Id == id);
        Choice C(Scene scene, string node, int i) => scene.Nodes.Single(n => n.Id == node).Choices[i];
        Node N(Scene scene, string node) => scene.Nodes.Single(n => n.Id == node);
        bool Avail(Scene scene, Snapshot w) => Rules.Available(story, scene, w);
        var ledger = story.Books["trickster.ledger"].Entries;

        // ---- T2: the message (Chapter 3, Woljif's second quest, both of Voetiel's lists). ----
        var moon = S(Moon);
        check(moon.Relationship == "hepzamirah" && moon.ReturnToList && moon.NativeReturnCue == null
              && moon.AnswerLists.SequenceEqual(new[] { Q2Dead, Q2Alive }) && moon.Chapters.SequenceEqual(new[] { 3 })
              && moon.Requires.SequenceEqual(new[] { "trickster", "hepzamirah.present_now" }) && moon.Forbids.Contains(Moon) && moon.Forbids.Contains(Moon + ".seen")
              && (moon.ReturnText ?? "").Split(' ').Length <= 25,
            "T2: the message is not a Chapter 3 ReturnToList entry on both of Voetiel's lists, once only.");
        check(Avail(moon, World(story, 3, "trickster")) && !Avail(moon, World(story, 3)) && !Avail(moon, World(story, 4, "trickster")),
            "T2: the message is offered off the live Trickster or outside Chapter 3.");
        check(N(moon, "start").Speaker == "conversant" && N(moon, "spoken").Speaker == "conversant"
              && N(moon, "woljif_asks").SpeakerUnit == Woljif,
            "T2: Voetiel (the Q2 conversant) and Woljif (his unit) are not wired as speakers.");
        check(C(moon, "start", 0).Alignment?.Direction == "Evil" && C(moon, "start", 0).Set.Contains(Moon) && C(moon, "start", 0).Set.Contains(Moon + ".seen")
              && C(moon, "start", 1).Abort && C(moon, "start", 1).Set.SequenceEqual(new[] { Moon + ".declined", Moon + ".seen" }),
            "T2: the offer and its abort do not consume the beat where they are spoken.");
        var said = World(story, 3, "trickster");
        var moonOut = Program.Walk(moon, said);
        check(moonOut.Count == 3 && moonOut.All(r => r.Has(Moon + ".seen"))
              && moonOut.All(r => new[] { Moon, Moon + ".declined" }.Count(r.Has) == 1)
              && moonOut.Count(r => r.Has(Moon) && r.Has(Bluff)) == 1 && moonOut.Count(r => r.Has(Moon) && !r.Has(Bluff)) == 1,
            "T2: a message path does not end in exactly one outcome (offered, with or without the bluff, or declined).");
        foreach (var r in moonOut)
        {
            var again = Program.Copy(r);
            again.Hour += 1;
            check(!Avail(moon, again), "T2: the message is offered twice.");
        }

        // ---- T2: the reckoning (Chapter 4, Woljif's third quest). ----
        var reckon = S(Reckon);
        check(reckon.ReturnToList && reckon.AnswerLists.SequenceEqual(new[] { Q3Hub }) && reckon.Chapters.SequenceEqual(new[] { 4 })
              && reckon.Requires.SequenceEqual(new[] { "trickster", Moon, "hepzamirah.present_now" }) && reckon.Forbids.Contains(Reckon + ".seen"),
            "T2: the reckoning is not a Chapter 4 ReturnToList entry on the Q3 hub that needs the message.");
        check(Avail(reckon, World(story, 4, "trickster", Moon)) && !Avail(reckon, World(story, 4, "trickster"))
              && !Avail(reckon, World(story, 4, "trickster", Moon + ".declined")),
            "T2: the reckoning ignores whether the offer was spoken.");
        check(N(reckon, "start").SpeakerUnit == Voetiel && N(reckon, "start_bluff").SpeakerUnit == Voetiel
              && N(reckon, "promised").SpeakerUnit == Woljif && N(reckon, "doubt").SpeakerUnit == Woljif,
            "T2: in Q3 (Woljif is the dialog's speaker) Voetiel's lines do not name his unit.");
        check(C(reckon, "start", 0).Next == "start_bluff" && C(reckon, "start", 0).Requires.SequenceEqual(new[] { Bluff })
              && C(reckon, "start", 1).Next == "promised" && C(reckon, "start", 1).Forbids.Contains(Bluff)
              && C(reckon, "start", 2).Next == "doubt" && C(reckon, "start", 2).Forbids.Contains(Bluff)
              && C(reckon, "start_bluff", 0).Next == "promised" && C(reckon, "start_bluff", 1).Next == "doubt"
              && N(reckon, "start").Choices.All(c => c.Set.Contains(Reckon + ".seen")),
            "T2: the reckoning's indices or its first-choice consumption differ from 15b.");
        foreach (var bluffed in new[] { false, true })
        {
            var w = bluffed ? World(story, 4, "trickster", Moon, Bluff) : World(story, 4, "trickster", Moon);
            var visited = new HashSet<string>();
            var outs = Program.Walk(reckon, w, (id, _) => visited.Add(id));
            check(outs.Count == 2 && outs.All(r => new[] { Promised, Doubt }.Count(r.Has) == 1 && r.Has(Reckon))
                  && visited.Contains("start_bluff") == bluffed && !outs.Any(r => Avail(reckon, r)),
                "T2: the reckoning (bluff " + bluffed + ") does not end in exactly one of promised/doubt, once.");
        }

        // ---- T2: the ghost's callback, index-safe at [2] on sneer in both setups. ----
        foreach (var setup in new[] { S(H + "ghost.first_time"), S(H + "ghost.second_time") })
        {
            check(C(setup, "sneer", 0).NativeNext == Dissipate && C(setup, "sneer", 1).Set.Contains("hepzamirah.closed")
                  && C(setup, "sneer", 2).Next == "moon_callback" && C(setup, "sneer", 2).Requires.SequenceEqual(new[] { Moon })
                  && C(setup, "moon_callback", 0).NativeNext == Dissipate
                  && C(setup, "moon_callback", 0).Set.Contains(H + "primed") && C(setup, "moon_callback", 0).Set.Contains(H + "moon_callback"),
                "T2: the callback on " + setup.Id + " moved sneer [0]/[1] or does not prime the device.");
            var ghost = World(story, 5, "trickster", "hepzamirah.dead", "alderpash.leavable", Moon);
            var without = World(story, 5, "trickster", "hepzamirah.dead", "alderpash.leavable");
            check(Program.Walk(setup, ghost).Any(r => r.Has(H + "moon_callback") && r.Has(H + "primed"))
                  && !Program.Walk(setup, without).Any(r => r.Has(H + "moon_callback")),
                "T2: the callback is not offered exactly when the message was spoken: " + setup.Id);
        }

        // ---- T2: Woljif's later answer (Chapter 5, his hub), and the Ledger page. ----
        var wPromised = S(H + "react.woljif_promised");
        var wDoubt = S(H + "react.woljif_doubt");
        var back = new[] { "trickster.ever", H + "returned" };
        check(Avail(wPromised, World(story, 5, back.Append(Promised).ToArray())) && !Avail(wDoubt, World(story, 5, back.Append(Promised).ToArray()))
              && Avail(wDoubt, World(story, 5, back.Append(Doubt).ToArray())) && !Avail(wPromised, World(story, 5, back.Append(Doubt).ToArray()))
              && !Avail(wPromised, World(story, 5, back.Append(Promised).Append("woljif.dead").ToArray()))
              && !Avail(wDoubt, World(story, 5, back.Append(Doubt).Append(H + "cost.confined").ToArray()))
              && Avail(wDoubt, World(story, 5, back.Append(Doubt).Append(H + "cost.confined").Append(H + "flesh.released").ToArray()))
              && !Avail(wPromised, World(story, 5, Promised)),
            "T2: Woljif's Chapter 5 answer does not follow promised/doubt, her return, his availability and her release.");
        var moonPage = ledger.Single(e => e.Id == "early.woljif_moon");
        var heard = new Snapshot();
        heard.Flags.Add(Moon);
        Rules.Complete(story, heard);
        check(moonPage.Section == "Secrets" && moonPage.Requires.SequenceEqual(new[] { "trickster.secret.woljif_moon" }) && heard.Has(moonPage.Requires[0]),
            "T2: the Ledger page is not a Secrets page on the spoken message.");
        foreach (var (flags, expected) in new[] { (new[] { Moon, Promised }, 0), (new[] { Moon, Doubt }, 1), (new[] { Moon }, 2),
                                                  (new[] { Moon, Bluff }, 3), (new[] { Moon, Bluff, Promised }, 0) })
        {
            var s = new Snapshot();
            s.Flags.UnionWith(flags);
            var shown = moonPage.Lines.Select((l, i) => (l, i)).Where(t => Shown(t.l, s)).Select(t => t.i).ToList();
            check(shown.SequenceEqual(new[] { expected }), "T2: the Ledger shows the wrong line for " + string.Join(",", flags));
        }
        foreach (var page in new[] { moonPage })
            foreach (var line in page.Lines)
                ;
        var t2Readers = new[] { Bluff, Promised, Doubt };
        foreach (var s in story.Scenes.Where(s => s.Id != Reckon && !s.Id.StartsWith(H + "react.woljif_", StringComparison.Ordinal)))
            check(!t2Readers.Any(f => s.Requires.Contains(f) || s.Forbids.Contains(f)
                    || s.Nodes.Any(n => n.Choices.Any(c => c.Requires.Contains(f) || c.Forbids.Contains(f)))),
                "T2: a scene outside the thread reads Woljif's Moon flags: " + s.Id);

        // ---- T3: the interrogation (Chapter 3, the cult camp). ----
        var ask = S(Interrogation);
        check(ask.Relationship == "shamira" && !ask.ReturnToList && ask.AnswerLists.SequenceEqual(new[] { TelmerHub })
              && ask.NativeReturnCue == TelmerReturn && ask.Chapters.SequenceEqual(new[] { 3 }) && ask.Requires.SequenceEqual(new[] { "trickster", "shamira.present_now" })
              && ask.Forbids.Contains(Interrogation) && ask.Forbids.Contains(Interrogation + ".seen") && N(ask, "start").Speaker == "conversant",
            "T3: the interrogation is not an inline Chapter 3 entry on Telmer's hub returning to Cue_0024.");
        check(Avail(ask, World(story, 3, "trickster")) && !Avail(ask, World(story, 3)) && !Avail(ask, World(story, 4, "trickster")),
            "T3: the interrogation is offered off the live Trickster or outside Chapter 3.");
        var press = C(ask, "start", 0);
        check(press.Check?.Skill == "CheckIntimidate" && press.Check!.DC == 18 && press.Set.Contains(Interrogation + ".seen")
              && C(ask, "start", 1).Abort && C(ask, "start", 1).Set.SequenceEqual(new[] { Interrogation + ".declined", Interrogation + ".seen" }),
            "T3: the Intimidate DC 18 or the consuming abort differ from 15b.");
        check(C(ask, "recite", 0).NativeNext == TelmerRelease && C(ask, "recite", 0).Alignment?.Direction == "Chaotic"
              && C(ask, "recite", 0).Set.SequenceEqual(new[] { Notes, Exposed }) && C(ask, "garbled", 0).Set.SequenceEqual(new[] { Failed }),
            "T3: the release or the failure does not set its own outcome.");
        var askOut = Program.Walk(ask, World(story, 3, "trickster"));
        check(askOut.Count == 3 && askOut.All(r => r.Has(Interrogation + ".seen"))
              && askOut.All(r => new[] { Notes, Failed, Interrogation + ".declined" }.Count(r.Has) == 1)
              && askOut.Where(r => r.Has(Failed)).All(r => r.Has(Interrogation) && !r.Has(Notes))
              && askOut.Where(r => r.Has(Interrogation + ".declined")).All(r => !r.Has(Interrogation)),
            "T3: an interrogation path does not end in exactly one outcome (notes, failed, declined).");
        foreach (var r in askOut)
        {
            var again = Program.Copy(r);
            again.Hour += 1;
            check(!Avail(ask, again), "T3: the interrogation is offered twice.");
        }
        foreach (var (flags, released) in new[] { (new[] { Notes }, true), (new[] { "telmer.spared_0017" }, true),
                                                   (new[] { "telmer.spared_0018" }, true), (new[] { Failed }, false) })
        {
            var s = new Snapshot { Chapter = 3 };
            s.Flags.UnionWith(flags);
            Rules.Complete(story, s);
            check(s.Has("telmer.released") == released, "T3: telmer.released is wrong for " + string.Join(",", flags));
        }

        // ---- T3: the letter (Chapter 3, 48 h after the release; text by the Xanthir outcome). ----
        var letter = S(Letter);
        check(Rules.IsRemote(letter) && letter.Kind == "letter" && letter.Chapters.SequenceEqual(new[] { 3 }) && letter.DelayHours == 48
              && letter.Requires.SequenceEqual(new[] { "trickster", Notes, "shamira.reachable_by_letter" }) && letter.Forbids.Contains(Letter + ".seen"),
            "T3: the letter is not a Chapter 3 letter 48 h after the release.");
        var freed = World(story, 3, "trickster", Notes, Exposed);
        freed.Times[Notes] = freed.Hour;
        var at47 = Program.Copy(freed); at47.Hour += 47;
        var at48 = Program.Copy(freed); at48.Hour += 48;
        var ch4 = Program.Copy(at48); ch4.Chapter = 4;
        check(!Avail(letter, at47) && Avail(letter, at48) && !Avail(letter, ch4) && !Avail(letter, World(story, 3, "trickster", Failed)),
            "T3: the letter comes early, after Chapter 3, or without the release.");
        foreach (var dead in new[] { false, true })
        {
            var w = Program.Copy(at48);
            if (dead) w.Flags.Add("xanthir.dead");
            var visited = new HashSet<string>();
            var outs = Program.Walk(letter, w, (id, _) => visited.Add(id));
            check(outs.Count == 2 && outs.All(r => r.Has(Letter + ".seen") && new[] { Kept, Burned }.Count(r.Has) == 1)
                  && visited.Contains("dead") == dead && visited.Contains("alive") == !dead && !outs.Any(r => Avail(letter, r)),
                "T3: the letter (Xanthir dead " + dead + ") does not pick its variant, or is offered twice.");
        }

        // ---- T3: her find in the Harem, index-safe at [3] on game. ----
        var read = S("shamira.trickster.ch4.read");
        check(C(read, "game", 0).Next == "found_war" && C(read, "game", 1).Next == "found_her" && C(read, "game", 2).Next == "recipes"
              && C(read, "game", 3).Next == "manifest" && C(read, "game", 3).Requires.SequenceEqual(new[] { Notes })
              && new[] { "shamira.trickster.read", "shamira.started", "shamira.trickster.manifest_shown" }.All(C(read, "game", 3).Set.Contains),
            "T3: the payoff moved game [0]-[2], or does not set READ and STARTED.");
        foreach (var (flags, letterShown) in new[] { (new[] { "trickster", Notes, Exposed }, false), (new[] { "trickster", Notes, Exposed, Kept }, true) })
        {
            var visited = new HashSet<string>();
            var outs = Program.Walk(read, World(story, 4, flags), (id, _) => visited.Add(id));
            check(outs.Any(r => r.Has("shamira.trickster.manifest_shown")) && visited.Contains("manifest_exposed")
                  && visited.Contains("manifest_letter") == letterShown,
                "T3: the manifest does not show its exposure and letter variants as the flags say.");
        }
        check(!Program.Walk(read, World(story, 4, "trickster")).Any(r => r.Has("shamira.trickster.manifest_shown")),
            "T3: the manifest is offered without the tally.");
        var telmerPage = ledger.Single(e => e.Id == "early.telmer");
        check(telmerPage.Section == "Secrets" && telmerPage.Requires.SequenceEqual(new[] { "trickster.secret.telmer_tally" })
              && World(story, 3, Notes).Has("trickster.secret.telmer_tally") && !World(story, 3, Failed).Has("trickster.secret.telmer_tally")
              && Shown(telmerPage.Lines[0], World(story, 3, Notes, Exposed)) && !Shown(telmerPage.Lines[1], World(story, 3, Notes, Exposed))
              && Shown(telmerPage.Lines[1], World(story, 3, Notes, Exposed, Kept)),
            "T3: the Ledger page does not read the exposure and the kept letter.");

        // Coexistence: no thread scene reads another woman's committed, closed or harem state, or sets a native etude.
        foreach (var s in new[] { moon, reckon, ask, letter })
        {
            check(s.Nodes.All(n => n.Choices.All(c => c.StartEtude == null)), "A thread scene starts a native etude: " + s.Id);
            check(!s.Requires.Concat(s.Forbids).Any(f => f.EndsWith(".committed", StringComparison.Ordinal) || f.EndsWith(".closed", StringComparison.Ordinal)
                    || f.Contains(".harem.")), "A thread scene reads a partner state: " + s.Id);
        }
        Console.WriteLine("PASS: early threads T2 (Hepzamirah <- Voetiel) and T3 (Shamira <- Telmer): gates, aborts, once-only, outcomes, payoffs and readers.");
    }
}
