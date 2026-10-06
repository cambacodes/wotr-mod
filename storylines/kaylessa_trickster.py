"""Kaylessa on the Trickster path: "No lamb to the slaughter" (Writer/handoffs/trickster/kaylessa.md; the binding plan is
11-ROSTER-PLAN-2 §2, which replaces the spec's device section: F22 in the dead worlds, the amulet swap in the living one).

Canon: a Kyonin elf of the Sunset Wasps, vigilantes of Calistria, whom Anemora fed false names until they killed the
innocent; captured, broken by the torture she was made to do, and taken by the Dark Fate: "Any elf can become a drow.
Absolutely anyone." (Kaylessa_Reveal/Cue_0024 a5bbf947). The Winter Council sends Forn Autumn Haze to bury the truth with
everyone who has heard it (Forn_Ambush/Cue_0030 103ad8c5, Cue_0056 ad41c004). She calls everyone "soldier" ("Everyone's a
soldier in a war", Kaylessa_main/Cue_0073 425898fa); "I am no lamb to the slaughter" (Cue_0040 1988bcd8). If she lives to the
Chapter 3 ambush she takes Forn's arrow for the Commander and begs to be killed before the beast in her breaks free
(Kaylessa_Reveal/Cue_0037 58f99415); every native answer ends with her dead (Kaylessa_dead 4dd373d7). Her diary: "when my
former comrades approached me, I could not find the strength to draw my dagger and take my own life. I wish I had."
(Kaylessa_Diary c669b34a). Anemora at Iz: "None... except for that blasted Kaylessa." (c5/Iz/Anemora/Cue_0146 c0fb6762).

Devices, earned in play:
- dead worlds (she died in Kenabres or the war camp, or at her plea): the Trickster trades with Shyka the Many at the
  Council, a branch for a branch. Shyka keeps a timeline in which the Commander says yes to becoming Shyka (Shyka_Offer/
  Cue_0018 f40e9f35), the price the Eldest joined the Council to collect. She walks in from the branch that lived,
  remembering this one's death; the Dark Fate is stalled at the hour she died here.
- the living world (the Chapter 3 ambush never came): Forn returns in Chapter 5 with the same false wound; the Commander
  plays along, plans with her, and mid-ambush a Trickery check hangs her illusion amulet (Anemora's craft, a stolen
  courier's face) on Forn, and the Winter Council's own marksmen shoot their own man. The amulet burns out: she can never
  pass as an elf again.
The commit: she hands the Commander the dagger she once could not draw on herself, with no test. Taking it and handing it
back are two different yeses. The courtship lives in kaylessa_wasps (before) and kaylessa_clearing (after).
"""
from story_format import c, n, p, reaction, scene

SCENES = []
REL = "kaylessa"
P = "kaylessa.trickster."
UNIT = "a1569a0739314d04cb8af1d47dcffbe0"          # KaylessaDisguised (war camp: rags and a half-mask; no dialog component)
DREZEN = "2570015799edf594daf2f076f2f975d8"        # DrezenCapital
TAILOR = "253cdb8f434e5a6469b75e18428316e3"        # TailorCapitalTrader: the awning's shade (Arueshalae's fallback sits front 2.0)
PRESENCE = "kaylessa.presence"
PLEA_LIST = "07bc8bac6a8c8074183e6abb6ce56847"     # Kaylessa_Reveal/AnswersList_0029 (her plea)
PLEA_CUE = "58f994154e180a147a4ab18381f9bc8c"      # Kaylessa_Reveal/Cue_0037 "Because you will have to end my life now, soldier."
GOODBYE = "0585a80d0b70442409f30afad8207e9d"       # Kaylessa_Reveal/Cue_0033 "Goodbye, soldier." (the native death)
SHYKA_LIST = "e7236a1fe9273ba498b96b9616b3f379"    # c3/Mythic_Trickster/Council_Shyka/AnswersList_0003
SHYKA_BACK = "cd2b35a474db55544a63f59a67ac67bf"    # Council_Shyka/Cue_0002 (clean return to her list)
ANEVIA_HUB = "33960c7f7af40cd43b7f801a76c87a0b"    # NPC_Common/Anevia/AnswersList_0003
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"    # CompanionDialogues/Woljif/AnswersList_0003

STARTED = "kaylessa.started"
CLOSED = "kaylessa.closed"
COMMITTED = "kaylessa.committed"
DEAD = "kaylessa.dead"
DEAD_L = "kaylessa.dead.latched"
BEGGED = "kaylessa.begged_death"
MET = "kaylessa.met"
UNMASKED = "kaylessa.unmasked"
CAUGHT = "kaylessa.anevia_caught"
TOMB = "kaylessa.tomb"
CAM_KILLED = "kaylessa.camellia_killed"
FORN_DEAD = "kaylessa.forn_dead"
EMBER_MET = "kaylessa.ember_met"
# Keys only this route reads (bound in integrate()).
HEALED = "kaylessa.healed_by_force"               # Kaylessa_main/Answer_0068 [Heal her] (Cue_0071: "an arrow to the eye")
NOTE_DESTROYED = "kaylessa.note_destroyed"        # Forn_main/Answer_0039 [Give him Kaylessa's note] "Destroy it."
NOTE_HELD = "kaylessa.note_held"                  # Kaylessa_Diary (Kaylessa's Message), still carried
ANEMORA_TOLD = "kaylessa.anemora_told"            # c5/Iz/Anemora/Cue_0146 "None... except for that blasted Kaylessa."
TRICKERY1 = "trickster.trickery_tier1"            # MainCharacterFacts: TricksterTrickeryTier1Feature (dispel, as a device)
WARNED_KENABRES = "kaylessa.warned_kenabres"      # Kaylessa_main/Answer_0028 "I believe you. Forn is at the Defender's Heart..."
WARNED_CAMP = "kaylessa.warned_camp"              # Kaylessa_main/Answer_0058 "I believe you. Forn is in the camp, watch out for him."
SELECTED_ANSWERS = {HEALED: "9f98ffa7f2c71cb4c9e5da0c7a053876", NOTE_DESTROYED: "30b5b35e84d649245b0fcba5e8d5cc02",
                    WARNED_KENABRES: "c3e2b86fef76ee441bc66c86ef5f071a", WARNED_CAMP: "8d741378ae169454f89a544029823135"}
FIRST_WORDS = "kaylessa.first_words_seen"        # Kaylessa_main/Cue_0001 "What are you looking at, soldier? Like what you see?"
SEEN_CUES = {ANEMORA_TOLD: ["c0fb6762c057bcc4894d1892a9eb22fc"], FIRST_WORDS: ["2d7d6df431933024591e74d6dfd873e4"]}
INVENTORY = {NOTE_HELD: "c669b34a7b9c2cb42bf6deb5d8d1606f"}
FACTS = {TRICKERY1: "90bc71f1d8482184a9ede0bda4773d94"}

PRIMED = P + "primed"
RETURNED = P + "returned"
DECLINED = P + "declined"
LEFT = P + "left_free"
PROMISED = P + "promised"
ENDING_KEPT = P + "ending_kept"
PRESENCE_ON = P + "presence_on"
LATE_COMMITTED = P + "late_committed"
# The dead worlds.
SHYKA_PRICE = P + "cost.shyka_price"
SHYKA_RAISED = P + "cost.shyka_raised"
SHYKA_AMUSED = P + "shyka_amused"
STALLED = P + "cost.dark_fate_stalled"
TOLD = P + "told_borrowed"
LIED = P + "lied_about_price"
CONFESSED = P + "confessed_price"
# The living world.
WOUND_SEEN = P + "alive.wound_seen"
# PP2 early beat (kaylessa_early, Chapter 2 war camp; path-neutral): her lesson on a false wound, read at the hunter's visit.
TELLS_READ = "kaylessa.early.tells.read"
TELLS_MISSED = "kaylessa.early.tells.missed"
LESSON = '[Watch the bandage the way she taught you at the war camp: watch it when he forgets it.]'
LESSON_DC = '[Remember the sergeant at the cook-fire, and watch the bandage when he forgets it. Perception DC 18.]'
PLANNED = P + "alive.planned"
SHIELD = P + "alive.shield_sworn"
SWAP_CLEAN = P + "alive.swap_clean"
SWAP_FUMBLED = P + "alive.swap_fumbled"
AMULET = P + "cost.amulet_burnt"
COUNCIL_KNOWS = P + "cost.council_knows"
ARROW = P + "cost.arrow_taken"
HER_ARROW = P + "cost.her_collarbone"
BEAST_SEEN = P + "beast_seen"
# Sol quality pass: when Forn died in canon (kaylessa.forn_dead at the hunter's visit) the living chain is a nameless
# successor's, latched at that visit; the swap's own FornIsDead start (E17) must never turn a later scene into his.
SUCCESSOR = P + "alive.successor"
FORN_IS_DEAD = "7a6f0ef4dd004418aa613693dd9d280a"   # FornIsDead, started exactly as native Forn_Ambush/Cue_0040 does
SWAP_OUT = dict(start_etude=FORN_IS_DEAD)
# The spine after her return.
RULES = P + "after.rules"                         # scene ids double as flags once the scene completes
CLOCK_SCENE = P + "after.dark_fate"
BEAST_SCENE = P + "after.the_beast"
KNIFE_SCENE = P + "after.the_knife"
EXTRA_RULE = P + "rule_of_your_own"
RULE_FOUR = P + "rule_four"
CLOCK = P + "clock_named"
BEAST_MET = P + "beast_met"
BEAST_FED = P + "cost.beast_fed"
BEAST_STOPPED = P + "beast_stopped"
WASP_SENT = P + "wasp_sent_home"
KNIFE_SHOWN = P + "knife_shown"
TRUTH_OK = P + "truth_settled"                    # derived: no price lied about, or the lie confessed
WARNED_ANY = P + "warned_her"                     # derived: she was believed, at Kenabres or at the camp (native answers)
READY = "kaylessa.wasps.in_the_dark"               # the kiss after curfew: the played exchange of attraction before the proposal
KNIFE_HELD = P + "knife_held"
KNIFE_BACK = P + "knife_handed_back"
LATE_YES = P + "knife_picked_up"

RELATIONSHIP = dict(
    Title="No lamb to the slaughter",
    Description=("A drow who knows a truth Kyonin kills to keep buried is living in my city, under a courier's cloak and "
                 "under my protection. She calls me soldier. Neither of us is pretending it is safe."),
    Objective="Keep Kaylessa alive",
    Guidance=("On the Trickster path. If Kaylessa died, ask Shyka the Many at the Council to trade you the timeline where "
              "she lived (Chapters 3 and 5), then look for her in the shade of the tailor's awning in Drezen's market. If "
              "she never died, the hunter Forn will come to you in Chapter 5 to ask a favour; let him think he has it. "
              "She sets the rules, and she may leave."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[DEAD, "inhuman", LEFT], FailureFlags=[],
    UnavailableOverrides={DEAD: RETURNED},
    TricksterAccess={
        "dead": dict(detect=[DEAD], device=P + "dead.borrow", returned=RETURNED),
        "alive": dict(detect=["!" + DEAD], device=P + "alive.hunter", returned=RETURNED),
    },
)

PRESENCES = {
    # A copy of her war-camp disguise under the tailor's awning in the capital market: the one patch of shade at noon, and
    # an anchor no other route stands at on this side (Arueshalae's evil fallback, if it ever spawns, is 3 m off at front 2.0).
    PRESENCE: dict(Unit=UNIT, Area=DREZEN, Mode="spawn-copy", At=dict(NearUnit=TAILOR, Side="left", Distance=2.5),
                   Requires=["trickster.ever", PRESENCE_ON], Forbids=[CLOSED, LEFT], MinChapter=3, MaxChapter=5,
                   AnswerLists=[], Dialog="hub",
                   ContactWindows=[dict(Flag=PRIMED, MinAgeHours=12)],
                   Greeting="{n}In the shade of the tailor's awning, where the lamplight gives out, a woman in a courier's grey "
                            "cloak sits on an upturned crate with a bow across her knees. A shawl is wound up to her eyes. The "
                            "eyes are red, and they have been watching you since you came into the market.{/n}"),
}

DERIVED = {
    PRESENCE_ON: [[DEAD_L, PRIMED], [RETURNED]],
    # R2-6: the last beat before the knife; the epilogue answers a question the war left no time to ask.
    LATE_COMMITTED: [["trickster.ever", KNIFE_SHOWN, READY, TRUTH_OK]],   # the last beats before her proposal (Sol quality pass, BEL)
    # Rule three: the dead worlds' return records the truth told or the lie; the living worlds never lied about a price.
    TRUTH_OK: [[TOLD], [CONFESSED], [SWAP_CLEAN], [SWAP_FUMBLED]],
    WARNED_ANY: [[WARNED_KENABRES], [WARNED_CAMP]],
    # 05 §2.1: the stance hooks come from household.PARTNERS (kaylessa.harem.eligible = committed or late_committed).
}


def kay(id, text, *choices, **kw):
    return n(id, "Kaylessa", text, *choices, portrait="Kaylessa", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Kaylessa", **kw)


def shy(id, text, *choices, **kw):
    return n(id, "Shyka", text, *choices, portrait="Shyka", **kw)


def forn(id, text, *choices, **kw):
    return n(id, "Forn", text, *choices, portrait="Forn", **kw)


def hunter_s(id, text, *choices, **kw):
    """Forn's nameless successor (Forn died in canon): never Forn's name, never Forn's face."""
    return n(id, "Kyonin Hunter", text, *choices, portrait="", **kw)


def meet(id, title, entry, nodes, requires, forbids=(), delay=24, optional=True, chapters=(3, 5), **extra):
    """A physical scene at her presence under the tailor's awning (Chapters 3 and 5; the market is gone in the Abyss)."""
    SCENES.append(scene(id, title, "Kaylessa", min(chapters), entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, LEFT, *forbids))), delay=delay, last=max(chapters),
                        optional=optional, Relationship=REL, Chapters=list(chapters), ContactUnit=UNIT, Areas=[DREZEN],
                        InteractionHub=PRESENCE, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=24, owner="Kaylessa", kind="visit", chapter=3, optional=True,
          **extra):
    """A rest-delivered scene in which she (or the one named) is there in person: a night visit, a ride out of the city."""
    SCENES.append(scene(id, title, owner, chapter, "", nodes, requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, LEFT, *forbids))), delay=delay, last=5, optional=optional,
                        Relationship=REL, Remote=True, Kind=kind, Chapters=[c for c in (3, 5) if c >= chapter],
                        # Sol quality pass (CAN): she is there in person, in Drezen, so the rest must be taken there.
                        **(dict(Areas=[DREZEN]) if kind == "visit" else {}), **extra))


# --- State dead_at_reveal_ch3: the optional primer at her plea (a variant read only; the native death is untouched). ----

SCENES.append(scene(P + "reveal.promise", "Somewhere else", "Kaylessa", 3,
    '[Deliver the killing blow, and make her a promise] "I\'m sorry. Somewhere this goes differently. I\'m going to go and find it."',
    [kay("start", '''{n}She almost smiles. It sits badly on a face that has forgotten how.{/n}
"Somewhere. Don't be sentimental, soldier. It doesn't suit a Trickster." {n}She lifts her chin and gives you her throat, the way a duellist salutes before the first pass.{/n}
"If you find it, tell her from me: never go running to an elf who bleeds too much."''',
         c('[Strike] "Goodbye, Kaylessa."', native_next=GOODBYE, flags=(PROMISED,)))],
    requires=("trickster",), forbids=(DEAD, PROMISED), last=3, Relationship=REL, Chapters=[3],
    AnswerLists=[PLEA_LIST], NativeReturnCue=PLEA_CUE, EntryMythic="PlayerIsTrickster"))


# --- The dead worlds (Chapters 1-3 deaths): Shyka's timeline trade, inline on Shyka's own Council list. --------------

SCENES.append(scene(P + "dead.borrow", "A branch for a branch", "Shyka", 3,
    '[Play a trick on Shyka] "Lend me the timeline where the drow lived. I\'ll bring it back slightly used."',
    [shy("which", '''{n}Shyka laughs, and the laugh starts as a bass and ends as a small girl's giggle.{/n} "A drow! Which drow? We have so many. There is a drow in every third timeline, sitting on a rock, being tragic about something."
{n}They count on fingers that keep changing length.{/n} "Tell us which one, or we'll hand you the wrong one, and then you'll have a stranger in your house who knows your name."''',
         c('"The one who called everyone \'soldier\'."', "trade"),
         c('"The one who asked me to kill her."', "trade", requires=(BEGGED,)),
         c('"The one I killed before I knew who she was."', "trade", forbids=(BEGGED,))),
     shy("trade", '''"Oh, that one. Yes. She lives in quite a lot of branches, if you want to call it living. Hunted, cursed, cross. Very good with a bow." {n}Shyka pauses.{/n} "Lend? We do not lend. We would forget whom we lent it to, and then where would you be? We trade."
"A branch for a branch. The one where the drow lived, for one where you say yes to us. One day soon we will ask you a question, Commander. Somewhere, you already answered it." {n}For a moment the face in front of you is your own, older, and very calm.{/n}''',
         c('[Pay it] "Done. Somewhere, I said yes. Here, I\'m keeping the drow."', "close",
           flags=(PRIMED, SHYKA_PRICE, STARTED), forbids=(SHYKA_RAISED,), alignment=("Chaotic", 1)),
         c('[Offer a branch where you die instead] "Take one where I die. I have plenty."', "cheap"),
         c('[Try to haggle it down] "A branch where I say maybe."',
           check=dict(Skill="CheckDiplomacy", DC=30, Success="amused", Failure="raised")),
         c('[Let her keep the ending she chose] "No. She asked for that one."', "kept",
           requires=(BEGGED,), flags=(ENDING_KEPT, CLOSED)),
         c('[Keep your futures] "Not at that price."', abort=True)),
     shy("cheap", '''"So do we. Thousands of them. They are all dull; you die with your mouth open in nearly every one." {n}The face yawns, and is somebody's grandmother, and yawns again.{/n}
"No. The price does not move."''',
         c('[Back to the price] "Fine. The branch."', "trade_again")),
     shy("trade_again", '''{n}Shyka waits with its hands folded, all eleven fingers of them.{/n} "A branch for a branch. Where you say yes to us. We are very patient. We are also, in several places at once, bored."''',
         c('[Pay it] "Done. Somewhere, I said yes. Here, I\'m keeping the drow."', "close",
           flags=(PRIMED, SHYKA_PRICE, STARTED), forbids=(SHYKA_RAISED,), alignment=("Chaotic", 1)),
         c('[Try to haggle it down] "A branch where I say maybe."',
           check=dict(Skill="CheckDiplomacy", DC=30, Success="amused", Failure="raised")),
         c('[Let her keep the ending she chose] "No. She asked for that one."', "kept",
           requires=(BEGGED,), flags=(ENDING_KEPT, CLOSED)),
         c('[Keep your futures] "Not at that price."', abort=True)),
     shy("amused", '''"Maybe! Nobody offers us maybe. They offer blood and firstborns and very bad poetry." {n}Shyka claps with two hands of different sizes.{/n}
"No. But we shall remember that you tried. Probably."''',
         c('[Pay it] "Done. Somewhere, I said yes, and maybe."', "close",
           flags=(PRIMED, SHYKA_PRICE, STARTED, SHYKA_AMUSED), alignment=("Chaotic", 1))),
     shy("raised", '''"Haggling with Shyka, in Shyka's own hall?" {n}Every face they wear in the next breath frowns at you, one after another, like a row of disappointed aunts.{/n}
"Now it is a branch where you say yes and mean it. Every word. No fingers crossed behind your back. We would see."''',
         c('[Pay the raised price] "Done. Yes, and meant."', "close",
           flags=(PRIMED, SHYKA_PRICE, STARTED, SHYKA_RAISED), alignment=("Chaotic", 1)),
         c('[Refuse the raised price] "No."', abort=True)),
     shy("kept", '''{n}Shyka tilts a head that is, briefly, a goat's.{/n} "A Trickster who leaves a thing lying where it fell. How rare. We shall write it down, and then lose the page."
{n}The goat is a boy now, and the boy looks almost sorry.{/n} "She did ask you nicely. We remember that part. It was in all of them."''',
         c("[Return to the Council.]")),
     shy("close", '''{n}Shyka's current face looks down at its own hand as if it has just been paid. It has.{/n}
"Give it twelve hours. Branches are heavy, and she will arrive where it is dark, because she prefers it." {n}Now the face is an old woman's, sharp and fond.{/n}
"One thing. In her branch she did not die. In yours she did. She will remember both. We can't help that. Nobody can keep a thing like that out of a head. And tell us how it ends. We will forget to ask."''',
         c("[Return to the Council.]"))],
    requires=("trickster", DEAD), forbids=("shyka.gone", "council.fought", "council.fought_nocta_allied", PRIMED, ENDING_KEPT,
                                            RETURNED),
    last=5, Relationship=REL, Chapters=[3, 5], AnswerLists=[SHYKA_LIST], NativeReturnCue=SHYKA_BACK,
    EntryMythic="PlayerIsTrickster", TricksterDevice=True, TricksterState="dead"))


# Shyka gone from the Council (Sol quality pass, INT): the Eldest still exists, so the Trickster leaves an offer in the
# empty hall the way Shyka hears things, and haggles on worse terms, on screen. Chapter 5; the same return follows.
SCENES.append(scene(P + "dead.borrow_sending", "An offer carried through dust", "Shyka", 5, "", [
    nar("start", '''{n}At your camp, you clear a space on the table for the replies your messengers brought back. They have spent your allies' patience tracing the departed Council: favours called in, guides borrowed from the war roads. None found a door you could use.{/n}
{n}You speak the offer over their dust-stained letters: a branch for a branch, for the drow who called everyone soldier. You repeat it twice. The dust begins to gather against the wind.{/n}''',
        c("[Wait until the third hour.]", "answer")),
    shy("answer", '''{n}At the third hour the dust on the letters forms a face, then another.{/n} "You send so many people looking for us. They ought to be looking for demons. How like you."
"Your friends have spent their favours carrying this offer. Those are not our price. We are not at your Council now, Commander. We need not keep its manners. The price is a branch where you say yes and mean it. Every word. Paid now. No fingers crossed."''',
        c('''[Pay it] "Done. Yes, and meant."''', "close",
          flags=(PRIMED, SHYKA_PRICE, SHYKA_RAISED, STARTED), alignment=("Chaotic", 1), crusade=("Favors", -200)),
        c('[Keep your futures] "Not at that price."', abort=True)),
    shy("close", '''"Paid." {n}The dust settles back into dust.{/n} "Give it twelve hours. She will arrive where it is dark, because she prefers it. We make no promises about her manners."''',
        c("[Let the dust settle.]")),
], requires=("trickster", DEAD), forbids=(PRIMED, ENDING_KEPT, RETURNED),
    RequiresAnyGroups=[["shyka.gone", "council.fought", "council.fought_nocta_allied"]],
    last=5, optional=True, Relationship=REL, Remote=True, Kind="sending", Chapters=[5], TricksterDevice=True, TricksterState="dead"))


# The return: at her presence, a day after the trade.
meet(P + "dead.soldier", "Slightly used", '"...Kaylessa?"', [
    nar("open", '''{n}She doesn't get up. She watches you come the whole length of the awning's shadow with the look of someone checking a face against a description.{/n}''',
        c("Continue", "wake_reveal", requires=(BEGGED,)),
        c("Continue", "wake_early", forbids=(BEGGED,))),
    nar("wake_reveal", '''{n}She pulls the shawl down. Skin dark as slate, white hair hacked short, the fangs. Her hand goes to her collarbone, to the place where Forn's men put an arrow in her, and finds nothing there, and stays.{/n}''',
        c("Continue", "camellia", requires=(CAM_KILLED,)),
        c("Continue", "speak", forbids=(CAM_KILLED,))),
    nar("wake_early", '''{n}She pulls the shawl down. Skin dark as slate, white hair hacked short, the fangs. She lays the bow across her palms and turns it, looking along the limbs for the place where your blow snapped it in two. The wood is whole. She keeps looking.{/n}''',
        c("Continue", "speak")),
    kay("camellia", '''"The last face I saw here was your shaman's. She asked everyone else to give us some privacy." {n}Her thumb moves on her collarbone, slowly.{/n}
"She was very gentle about it, soldier. She smiled the whole time. Like a woman arranging flowers."''',
        c("Continue", "speak")),
    kay("speak", '''"I remember dying, soldier. The ground. The cold. You." {n}Her voice is flat, the way a report is flat.{/n}
"And I remember the other thing too. Living. Walking away from it with my bow on my back. Two memories of one night, and both of them feel true, and they don't fit. Like wearing someone else's boots."
"So. Tell me what you did."''',
        c('[Tell her the truth] "I traded with Shyka the Many for the branch where you lived. You\'re borrowed. I\'ll have to give you back slightly used."', "truth", flags=(TOLD,)),
        c('[Lie about the price] "Shyka owed me a favour. You cost me nothing."', "lie", flags=(LIED,))),
    kay("truth", '''"Borrowed." {n}She tries the word with her teeth.{/n} "From that thing that can't keep one face for a whole sentence. What did you give it?"''',
        c("Continue", "truth_begged", requires=(BEGGED,)),
        c("Continue", "truth_early", forbids=(BEGGED,))),
    kay("truth_begged", '''"I asked you for one thing. One clean ending, before the beast got it. I'd earned that much, soldier." {n}Her voice remains level.{/n}
"And you traded it away. You'd better tell me what you bought."''',
        c('"Yes."', "price"),
        c('"You never asked what I wanted."', "price")),
    kay("truth_early", '''"You broke my bow, and then you broke me. Kenabres, or the camp; I remember it very clearly, and I remember it from the ground." {n}She looks at your hands.{/n}
"And afterwards you went shopping in another world for a spare. As if I were a pair of boots you'd worn through."''',
        c('"Yes."', "price"),
        c('"I didn\'t know you then."', "price")),
    kay("price", '''"What did it cost you?" {n}She asks it the way a quartermaster asks, wanting the number, not the story.{/n}''',
        c('[Tell her] "A branch where I say yes to Shyka. Where I become one of them."', "shyka_yes", forbids=(SHYKA_RAISED,)),
        c('[Tell her] "A branch where I say yes to Shyka and mean it. I haggled. I lost."', "shyka_raised", requires=(SHYKA_RAISED,), forbids=("kaylessa.trickster.dead.borrow_sending",)),
        c('"That\'s mine to carry."', "mine"),
        c('[Tell her] "A branch where I say yes to Shyka and mean it. That was their price when I sent the offer after the Council had gone."', "shyka_sending", requires=(SHYKA_RAISED, "kaylessa.trickster.dead.borrow_sending"))),
    kay("shyka_yes", '''"One of them. That thing." {n}She looks you over, checking that all of you is still there.{/n}
"You sold a piece of your own future to bring me here. Either you're a fool, soldier, or you're something worse. I haven't decided which."''',
        c("Continue", "stalled")),
    kay("shyka_raised", '''"You haggled. With that." {n}Her mouth almost twitches; she stops it.{/n}
"A thing with a hundred faces, and you thought you could get a better price. Now it owns a piece of your future. I hope it enjoys the trouble."''',
        c("Continue", "stalled")),
    kay("mine", '''"Fine. Carry it. I'll carry mine." {n}She rewinds the shawl to her eyes with quick, practised turns.{/n} "But I'll find out. I always find out. That's how I ended up here in the first place."''',
        c("Continue", "stalled")),
    kay("lie", '''{n}She watches your mouth while you say it, the way a hunter watches long grass.{/n}
"Nothing costs nothing with that thing. You're lying to me, soldier. Standing there alive, after what happened to me, and lying to my face."
"Keep it, then. I'll find out what you paid. I always find out."''',
        c("Continue", "stalled")),
    kay("stalled", '''"Here's the part that doesn't fit." {n}She presses two fingers flat against her breastbone, where a heart would be.{/n}
"The beast. The thing in me that's been eating me since the Worldwound. Every day a little more, the way a tide comes in. And it's stopped. Not gone. Stopped, as if someone put a thumb on a clock. It stopped the night I died here."
"I don't know how long a thumb lasts, soldier."''',
        c('"Then stay where I can keep an eye on the clock."', "stay"),
        c('"Go where you like. I only wanted you to have the choice."', "choice")),
    kay("stay", '''"Keep an eye on it." {n}She snorts through her nose.{/n} "Everyone in Kyonin wants to keep an eye on me. You'll have to take a number."
{n}But she doesn't go. She settles back against the post of the awning as though she has been sitting there for years.{/n} "I'll be here. The shade's good. Nobody looks under an awning."''',
        c("[Leave her in the shade.]", flags=(RETURNED, STALLED))),
    kay("choice", '''"The choice." {n}For a while she says nothing at all.{/n}
"Nobody's given me one of those since Kyonin. Anemora didn't. Forn didn't. You didn't, the last time we met." {n}She settles back against the post of the awning.{/n} "I'll stay. For now. The shade's good, and I want to see what you do with a thing you've bought and can't use."''',
        c("[Leave her in the shade.]", flags=(RETURNED, STALLED))),
    kay("shyka_sending", '''"It named the price, and you paid it." {n}She looks you over as if something ought to be missing.{/n}
"No Council to sit in. No one there to stop you selling a piece of yourself. Don't expect me to thank you for that, soldier. I'm still deciding what to call it."''',
        c("Continue", "stalled")),
], requires=(DEAD, PRIMED), forbids=(RETURNED,), delay=12, optional=False, TricksterDevice=True, TricksterState="dead")


# --- The living world (Chapter 5; the ambush never came): Forn comes back, and the amulet swap. ------------------------

visit(P + "alive.hunter", "A courtesy between hunters", [
    nar("open", '''{n}There is an elf waiting in your antechamber when you come off the walls: tall, pale, in Kyonin grey with a leaf-shaped brooch at the throat, a bandaged forearm, and a melancholy, courteous face.{/n}''',
        c("Continue", "named", forbids=(FORN_DEAD,)),
        c("Continue", "second", requires=(FORN_DEAD,))),
    nar("named", '''{n}Forn Autumn Haze, hunter of Kyonin's Winter Council, rises and bows as if the war had left him nothing but his manners.{/n}''',
        c("Continue", "ask")),
    nar("second", '''{n}He is not Forn Autumn Haze; Forn is dead. This one wears the same grey, the same brooch, and the same careful sorrow, as if the Winter Council issued it with the cloak. He rises and bows. He gives no name. He says the name does not matter; the duty is the same one.{/n}''',
        c("Continue", "ask_s", flags=(SUCCESSOR,))),
    hunter_s("ask_s", '''"Commander. Forgive the hour. The one I hunt is in Drezen. The man who hunted her before me did not come home, and the Council has sent me to finish his work. She came in under a courier's grey and a face that is not hers, and she has been watching your markets for a week."
"I ask for nothing that would trouble your crusade. Only your leave, and one courtesy: a word, from you, that an elf lies wounded in the ravine below the south wall. She goes to the wounded. She cannot help it. It is the last thing about her that is still one of us."''',
        c('[Play along] "Name the place and the hour. I\'ll send her to you."', "agreed_s", flags=(PRIMED, STARTED),
          alignment=("Chaotic", 1)),
        c("[Study the bandage while he talks]", check=dict(Skill="SkillPerception", DC=25, Success="seen_s", Failure="missed_s"),
          forbids=(TELLS_READ, TELLS_MISSED)),
        c('[Send him away] "No hunting in my city."', abort=True),
        c(LESSON, "seen_s", requires=(TELLS_READ,)),
        c(LESSON_DC, requires=(TELLS_MISSED,), check=dict(Skill="SkillPerception", DC=18, Success="seen_s", Failure="missed_s"))),
    nar("seen_s", '''{n}The bandage is clean where it ought to be foul, and the arm under it moves too easily whenever he forgets it. There is no wound. He has learned his predecessor's trade to the letter. A man who fakes a wound to bring his prey into the open keeps friends with bows somewhere out of the light.{/n}''',
        c('[Play along] "Name the place and the hour. I\'ll send her to you."', "agreed_s", flags=(PRIMED, STARTED, WOUND_SEEN),
          alignment=("Chaotic", 1)),
        c('[Send him away] "No hunting in my city."', abort=True)),
    nar("missed_s", '''{n}The bandage is stained and tight, and he favours the arm the way a wounded man does. If it is theatre, it is good theatre.{/n}''',
        c('[Play along] "Name the place and the hour. I\'ll send her to you."', "agreed_s", flags=(PRIMED, STARTED),
          alignment=("Chaotic", 1)),
        c('[Send him away] "No hunting in my city."', abort=True)),
    hunter_s("agreed_s", '''"Send word when your preparations are ready. We will meet in the ravine below the south wall, on a night when the moon is down. She sees in the dark; we must give her every advantage, or she will suspect a trap." {n}He bows again, lower.{/n}
"You do my people a service they will never be permitted to thank you for. My predecessor would have said that circumstances are stronger than our desires. I have found it simpler not to have desires."''',
        c("[Watch him go.]")),
    forn("ask", '''"Commander. Forgive the hour. The one I hunt is in Drezen. She came in under a courier's grey and a face that is not hers, and she has been watching your markets for a week."
"I ask for nothing that would trouble your crusade. Only your leave, and one courtesy: a word, from you, that an elf lies wounded in the ravine below the south wall. She goes to the wounded. She cannot help it. It is the last thing about her that is still one of us."''',
        c('[Play along] "Name the place and the hour. I\'ll send her to you."', "agreed", flags=(PRIMED, STARTED),
          alignment=("Chaotic", 1)),
        c("[Study the bandage while he talks]", check=dict(Skill="SkillPerception", DC=25, Success="seen", Failure="missed"),
          forbids=(TELLS_READ, TELLS_MISSED)),
        c('[Send him away] "No hunting in my city."', abort=True),
        c(LESSON, "seen", requires=(TELLS_READ,)),
        c(LESSON_DC, requires=(TELLS_MISSED,), check=dict(Skill="SkillPerception", DC=18, Success="seen", Failure="missed"))),
    nar("seen", '''{n}The bandage is clean where it ought to be foul, and the arm under it moves too easily whenever he forgets it. There is no wound. A man who fakes a wound to bring his prey into the open keeps friends with bows somewhere out of the light.{/n}''',
        c('[Play along] "Name the place and the hour. I\'ll send her to you."', "agreed", flags=(PRIMED, STARTED, WOUND_SEEN),
          alignment=("Chaotic", 1)),
        c('[Send him away] "No hunting in my city."', abort=True)),
    nar("missed", '''{n}The bandage is stained and tight, and he favours the arm the way a wounded man does. If it is theatre, it is good theatre.{/n}''',
        c('[Play along] "Name the place and the hour. I\'ll send her to you."', "agreed", flags=(PRIMED, STARTED),
          alignment=("Chaotic", 1)),
        c('[Send him away] "No hunting in my city."', abort=True)),
    forn("agreed", '''"Send word when your preparations are ready. We will meet in the ravine below the south wall, on a night when the moon is down. She sees in the dark; we must give her every advantage, or she will suspect a trap." {n}He bows again, lower.{/n}
"You do my people a service they will never be permitted to thank you for. Some duties are like that. Circumstances are stronger than our desires, Commander. I believe you understand."''',
        c("[Watch him go.]")),
], requires=("trickster",), forbids=(DEAD, PRIMED, RETURNED), delay=0, owner="Forn", chapter=5, optional=False,
    TricksterDevice=True, TricksterState="alive")


visit(P + "alive.warning", "The face she wears", [
    nar("open", '''{n}The knife is at your throat before the lamp is lit. It is small, and very sharp, and the hand behind it does not shake. A voice by your ear, low, with the flat patience of someone who has done this before:{/n}''',
        c("Continue", "met", requires=(MET, WARNED_ANY)),
        c("Continue", "stranger", forbids=(MET,)),
        c("Continue", "met_doubted", requires=(MET,), forbids=(WARNED_ANY,))),
    kay("met_doubted", '''"Don't. I saw him leave your door, soldier. The elf with the bandage he doesn't need."
"We've met. That doesn't tell me what you promised him. So tell me why the man who wants my head was just bowing to you on your own doorstep."''',
        c('[Tell her everything] "He wants you in the ravine below the south wall with the moon down, and me for bait. I said yes."', "plan"),
        c('"I promised him you. I didn\'t say which of us would keep the promise."', "plan")),
    kay("met", '''"Don't. I saw him leave your door, soldier. The elf with the bandage he doesn't need."
"I told you once who was hunting me, and you believed me, or near enough. You told me where he was. So tell me why the man who wants my head was just bowing to you on your own doorstep."''',
        c('[Tell her everything] "He wants you in the ravine below the south wall with the moon down, and me for bait. I said yes."', "plan"),
        c('"I promised him you. I didn\'t say which of us would keep the promise."', "plan")),
    kay("stranger", '''"Don't. You don't know me, soldier. You've met the man who hunts me, which is worse for both of us."
"I watched him leave your door, bowing like a courtier. So tell me what you promised him, before I decide what you are."''',
        c('[Tell her everything] "He wants you in the ravine below the south wall with the moon down, and me for bait. I said yes."', "plan"),
        c('"I promised him you. I didn\'t say which of us would keep the promise."', "plan")),
    nar("plan", '''{n}The knife stays a moment longer. Then it's gone, and she steps back into what light there is: a Kyonin girl in a courier's grey, freckled, sunburnt across the nose. The face is wrong for her voice. It is wrong for her eyes.{/n}
{n}She touches the amulet at her throat, and the face goes out like a blown lamp. Under it she is dark as slate, fanged, red-eyed, and very tired.{/n}''',
        c("Continue", "amulet", forbids=(SUCCESSOR,)),
        c("Continue", "amulet_s", requires=(SUCCESSOR,))),
    kay("amulet_s", '''"Anemora's work. Her people wore faces like this round a campfire near your war camp, pretending to be your scouts. I took this one off a dead one in the fog."
"It shows a courier of the Green Road. Some girl they killed on the way to Mendev; I never learned her name. Forn hunted that face across half the country. Forn's dead, and the Council sent the next one with the same cloak and the same list, and he's hunting it now. It's the only elf face I've got, soldier. It's how I buy bread."''',
        c('"Then let him catch it. On somebody else."', "swap"),
        c('"Could that amulet hang round another neck?"', "swap")),
    kay("amulet", '''"Anemora's work. Her people wore faces like this round a campfire near your war camp, pretending to be your scouts. I took this one off a dead one in the fog."
"It shows a courier of the Green Road. Some girl they killed on the way to Mendev; I never learned her name. Forn has been hunting that face across half the country. It's the only elf face I've got, soldier. It's how I buy bread."''',
        c('"Then let him catch it. On somebody else."', "swap"),
        c('"Could that amulet hang round another neck?"', "swap")),
    kay("swap", '''"...On him." {n}Something moves in her face. It isn't a smile, but it used to be one.{/n}
"His marksmen will be up on the ridge with orders: the courier's face, first shot, don't let her speak. If the face is on him when they loose..." {n}She turns the amulet in her fingers.{/n}
"You'd have to lift it off my neck and put it on his in the middle of a fight, with his knife out. It's an alley trick. We did things like it in Kyonin, in Calistria's name, when I was a wasp and not a drow. You'd have to be quick, soldier."
"And when it's done I go down on the stones beside him and I stay down, under the girl's cloak, with his blood on it. From the ridge, in the dark, with the lantern knocked out, they'll count two bodies. They'll want to count two."''',
        c("Continue", "terms")),
    kay("terms", '''"One more thing. If it goes wrong, I take the arrows. Not you. It's my face they're aiming at, and my death they're owed."''',
        c('"Your face. Your arrows."', "agreed", flags=(PLANNED,)),
        c('"No. If it goes wrong, they hit me first."', "refused", flags=(PLANNED, SHIELD))),
    kay("agreed", '''"Good." {n}She puts the courier's face back on with a touch, the way another woman might put on a glove.{/n} "Send the word when we are ready. Don't be early. And don't be kind to him. He'll use it."''',
        c("[Light the lamp.]")),
    kay("refused", '''"Stubborn. Is that a Commander's disease, or a Trickster's?" {n}She looks at you for a while, deciding something, and doesn't tell you what she decides.{/n}
"Fine. Just don't make me watch it happen."''',
        c("[Light the lamp.]")),
], requires=(PRIMED,), forbids=(DEAD, RETURNED, PLANNED), delay=12, chapter=5, optional=False)


visit(P + "alive.amulet_swap", "Kyonin's own arrows", [
    nar("open", '''{n}With the moon down, the ravine below the south wall is as black as the bottom of a well. The hunter lies propped against a stone at the very bottom of it, a lantern turned low at his side, his bandaged arm across his knees: exactly where a wounded man would be found, exactly where a rescuer would have to stand in the light.{/n}''',
        c("Continue", "forn", forbids=(SUCCESSOR,)),
        c("Continue", "forn_s", requires=(SUCCESSOR,))),
    forn("forn", '''"Commander. And the courier." {n}Kaylessa comes down the slope behind you in the Green Road girl's face, her bow unstrung on her back, like a woman who has been told a friend is hurt.{/n}
"I am sorry it must be this way. I truly am. Come into the light, both of you. It will be quicker."''',
        c("Continue", "ridge")),
    hunter_s("forn_s", '''"Commander. And the courier." {n}Kaylessa comes down the slope behind you in the Green Road girl's face, her bow unstrung on her back, like a woman who has been told a friend is hurt.{/n}
"Forn Autumn Haze would have apologised to you both. I never learned how. Come into the light."''',
        c("Continue", "ridge")),
    nar("ridge", '''{n}A pebble rolls somewhere on the ridge above. Then another, on the other side. The hunter's good hand is already on his knife. Kaylessa's shoulder touches yours, once: the only signal you agreed on.{/n}''',
        c("[Unpick the glamour like a trap, and set it again on him]", requires=(TRICKERY1,),
          check=dict(Skill="SkillThievery", DC=24, Success="swap", Failure="fumble")),
        c("[Go for the arm you know is whole]", requires=(WOUND_SEEN,),
          check=dict(Skill="SkillThievery", DC=27, Success="swap", Failure="fumble")),
        c("[Lift the amulet off her and onto him]",
          check=dict(Skill="SkillThievery", DC=32, Success="swap", Failure="fumble"))),
    nar("swap", '''{n}Kaylessa goes first, straight at him, the way she once went at a different trap on a different night. His knife comes up for her throat. You are already inside his reach.{/n}
{n}Two fingers under the cord at her neck, a turn of the wrist, and the cord is over his head before his arm finishes its stroke, the way a wasp's sting is in before the hand can slap. The glamour takes him like water takes dye. For a heartbeat there are two of her in the lamplight: a freckled Green Road girl with the hunter's knife in her hand, and a drow woman throwing herself flat on the stones.{/n}''',
        c("Continue", "volley", forbids=(SUCCESSOR,)),
        c("Continue", "volley_s", requires=(SUCCESSOR,))),
    nar("volley", '''{n}The ridge looses. Six bows, perhaps eight, every one at the face they were told to shoot before it could speak. Forn does not speak. He looks down at the fletching in his chest with an expression of courteous surprise, as if someone has broken a rule of etiquette he had believed was universal.{/n}
{n}The amulet at his throat sputters, flares white, and burns out. The girl's face runs off him like wax, and what slides down the stone is only Forn Autumn Haze, the Winter Council's hunter, killed by Kyonin.{/n}''',
        c("Continue", "after")),
    nar("volley_s", '''{n}The ridge looses. Six bows, perhaps eight, every one at the face they were told to shoot before it could speak. He does not speak. He looks down at the fletching in his chest as though it were an error in a report he had signed without reading.{/n}
{n}The amulet at his throat sputters, flares white, and burns out. The girl's face runs off him like wax, and what slides down the stone is a Winter Council hunter who never gave his name, killed by Kyonin, in the same ravine his predecessor's work had led him to.{/n}''',
        c("Continue", "after")),
    kay("after", '''{n}Up on the ridge somebody shouts a single word in Elven, and then there is the sound of men running the other way. Kaylessa gets up off the stones and stands over him without moving.{/n}
"They counted two. I heard one of them say it, up there, before they ran: two down, the face burnt, the job done." {n}She wipes his blood off the courier's cloak with a handful of grass.{/n} "No one in Kyonin will ever say otherwise. They'll write that he died hunting me, and that I died with him, because the men who saw it want it to be true and the truth is worse than a lie to them." {n}She touches her throat where the cord was. There is nothing there now but her own dark skin.{/n}
"That was the last elf face I had, soldier. The only one I could have walked home in. Burnt out on him."''',
        c("[Say nothing.]", "end"),
        c('"It suited him."', "joke")),
    kay("joke", '''"It did." {n}And then, horribly, she laughs: a short breath through her teeth, over a dead man, in a ravine.{/n} "It did. Gods. It really did."''',
        c("Continue", "end")),
    kay("end", '''"Take me somewhere with a roof, soldier. I'd like to sit down in a place where nobody is aiming at me."''',
        c("[Take her back up the slope.]", flags=(RETURNED, AMULET, SWAP_CLEAN), forbids=(SUCCESSOR,), **SWAP_OUT),
        c("[Take her back up the slope.]", flags=(RETURNED, AMULET, SWAP_CLEAN), requires=(SUCCESSOR,))),
    nar("fumble", '''{n}Your fingers find the cord, and the hunter finds your wrist. He is faster than a wounded man and stronger than a courteous one. The amulet comes off her neck and hangs in his fist between the three of you, blazing, half a face on it and half off.{/n}''',
        c("Continue", "fumble_you", requires=(SHIELD,)),
        c("Continue", "fumble_her", forbids=(SHIELD,))),
    nar("fumble_you", '''{n}The ridge looses at the glare. You get your body between Kaylessa and the light, because you said you would, and the first arrow takes you high in the shoulder, and the second skips off your armour, and then she is past you.{/n}''',
        c("Continue", "beast")),
    nar("fumble_her", '''{n}The ridge looses at the glare. She puts herself in front of you, as she said she would. The arrow takes her low in the collarbone, and she makes a small, flat sound, as though she had been expecting it for years, and she does not fall.{/n}''',
        c("Continue", "beast")),
    nar("beast", '''{n}What she does to him then, she does with her hands. The knife is somewhere on the stones and she doesn't look for it. You hear her, low, a sound that is nothing like her voice, and you see her face in the dying glare of the amulet, and it is delighted.{/n}
{n}By the time the amulet burns out, he has stopped moving, and the ridge is empty. The marksmen have seen enough to carry home.{/n}''',
        c("Continue", "after_fumble")),
    kay("after_fumble", '''"Don't." {n}She's on her knees, holding her hands away from her body as though they belonged to someone else.{/n}
"Don't look at me like that, and don't look away either. You saw it. That's what's in me. It liked that." {n}She draws a breath that shakes all the way down.{/n}
"And they saw it too. They'll tell the Winter Council I'm alive and I'm everything Forn said I was. All of it true, in one night."''',
        c('[Help her up] "Come on. Somewhere with a roof."', flags=(RETURNED, AMULET, SWAP_FUMBLED, COUNCIL_KNOWS, BEAST_SEEN, ARROW),
          requires=(SHIELD,), forbids=(SUCCESSOR,), **SWAP_OUT),
        c('[Help her up] "Come on. Somewhere with a roof."', flags=(RETURNED, AMULET, SWAP_FUMBLED, COUNCIL_KNOWS, BEAST_SEEN, HER_ARROW),
          forbids=(SHIELD, SUCCESSOR), **SWAP_OUT),
        c('[Help her up] "Come on. Somewhere with a roof."', flags=(RETURNED, AMULET, SWAP_FUMBLED, COUNCIL_KNOWS, BEAST_SEEN, ARROW),
          requires=(SHIELD, SUCCESSOR)),
        c('[Help her up] "Come on. Somewhere with a roof."', flags=(RETURNED, AMULET, SWAP_FUMBLED, COUNCIL_KNOWS, BEAST_SEEN, HER_ARROW),
          requires=(SUCCESSOR,), forbids=(SHIELD,))),
], requires=(PLANNED,), forbids=(DEAD, RETURNED), delay=24, chapter=5, optional=False,
    TricksterDevice=True, TricksterState="alive")


# --- The spine after her return (both worlds): rules, the clock, the beast, the knife. -----------------------------

meet(RULES, "Soldier's rules", '"Still here?"', [
    nar("open", '''{n}She has the crate again, and the shade, and a cup of the tailor's tea she hasn't touched. The tailor has stopped asking her to buy anything. Beyond the awning Drezen goes on being loud: carts, a sergeant shouting names, somebody hammering a new hinge onto a door the demons broke.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Still here. If I'm staying in your city, we need rules. Soldiers need rules, or they start having ideas."
{n}She counts them off on her fingers, the way she would count arrows.{/n}
"One. I'm not your drow. Not anyone's. Not in the street, not in your reports, not in your head."''',
        c("Continue", "two_healed", requires=(HEALED,)),
        c("Continue", "two", forbids=(HEALED,))),
    kay("two_healed", '''"Two. No magic on me without asking." {n}Her eyes narrow.{/n} "You know that one. You were the last person who tried. Kenabres, with the city burning, and you stuck a spell in me like I was a sack of grain. I told you then about the arrow and the eye. I meant it."''',
        c("Continue", "three")),
    kay("two", '''"Two. No magic on me without asking. The last healer who laid hands on me without my leave got a promise about an arrow and an eye. I don't like being changed, soldier. Not even a little. Not even for my own good."''',
        c("Continue", "three")),
    kay("three", '''"Three. Don't lie to me." {n}She says it more quietly than the others.{/n} "I've had enough lies to last two lifetimes. Anemora's names. Forn's manners. Kyonin's whole shining history. I'm done swallowing them."''',
        c("Continue", "lied", requires=(LIED,), forbids=(CONFESSED,)),
        c("Continue", "rules", forbids=(LIED,)),
        c("Continue", "rules", requires=(LIED, CONFESSED))),
    kay("lied", '''{n}She keeps the third finger up.{/n} "Which you've already broken. You still owe me what that thing at your Council took for me. I haven't forgotten, and I won't."''',
        c('[Confess] "A branch where I become one of Shyka. They named their terms. I paid them."', "confess", flags=(CONFESSED,)),
        c('"Another time."', "rules")),
    kay("confess", '''{n}She doesn't answer right away. She puts the cup down, carefully, on the edge of the crate.{/n}
"You lied because the truth was ugly. I know. I used to do it for a living." {n}She looks up.{/n} "Don't do it again. Rule three stands. It's the only one I'd kill over."''',
        c("Continue", "rules")),
    kay("rules", '''"That's mine. Three rules. They're not many. Most soldiers get more."''',
        c('[Agree to all three] "Your rules."', "agree"),
        c('[Add one of your own] "One of mine: when you go out after dark, you tell somebody which way."', "mine",
          flags=(EXTRA_RULE,)),
        c('"Rule four: I get to break one of yours, once, and you don\'t get to know which."', "four", flags=(RULE_FOUR,))),
    kay("agree", '''"Just like that." {n}She studies you over the rim of the cup.{/n} "Most people argue. Forn would have argued for an hour and bowed at the end. Anemora would have agreed with everything and meant none of it."
"You agreed like a soldier taking orders. I don't know yet whether that's a compliment."''',
        c("[Leave her to the market.]")),
    kay("mine", '''"Tell somebody which way." {n}She repeats it as if you'd asked her to wear a bell.{/n} "I've been hunted across two countries. Nobody's known which way I went since Kyonin. That's why I'm alive. Or was. Or am again."
{n}She turns the cup a quarter-turn on the crate.{/n} "Fine. I'll tell you. Not the sergeant, not your clerk. You. And if you're ever the one who comes after me, soldier, I'll know exactly who talked."''',
        c("[Leave her to the market.]")),
    kay("four", '''{n}She looks, briefly, as if she might throw the tea at you. Then something gives, very slightly, at the corner of her mouth.{/n}
"You're a Trickster. Of course you'd want a loaded die in the rules." {n}She shakes her head.{/n} "Fine. One. Once. And when you break it, I'll know which, because I'll be looking for it every day from now until you do. You'll have bought yourself a wife's suspicion without the wedding."''',
        c("[Leave her to the market.]")),
], requires=(RETURNED,), forbids=(RULES,), delay=24, optional=False)


meet(CLOCK_SCENE, "The clock", '"You\'re counting something."', [
    nar("open", '''{n}A strip of cloth is tied around her wrist, knotted at one end. Her thumb travels over it while the market carts rattle past.{/n}''',
        c("Continue", "stalled", requires=(STALLED,)),
        c("Continue", "clean", requires=(SWAP_CLEAN,), forbids=(SUCCESSOR,)),
        c("Continue", "fumbled", requires=(SWAP_FUMBLED,)),
        c("Continue", "clean_s", requires=(SWAP_CLEAN, SUCCESSOR))),
    kay("stalled", '''"Days. Since Shyka put me down in your market." {n}She holds up her wrist.{/n} "Every morning I check. In the Worldwound it was a little further in each time, like water through a boot. Now it stays in the same place."
"I keep waiting for the thumb to slip."''',
        c("Continue", "what")),
    kay("clean", '''"Days. Since the ravine." {n}She holds up the wrist.{/n}
"Every morning I check. It moves, soldier. A little each week, like water through a boot. But I watched Forn go down with Kyonin's arrows in him, and I waited for it to howl, the way it did when I first saw him bleed in Mendev. It didn't. It didn't move at all."
"I don't know what that means. I'm afraid to hope it means anything."''',
        c("Continue", "what")),
    kay("clean_s", '''"Days. Since the ravine." {n}She holds up the wrist.{/n}
"Every morning I check. It moves, soldier. A little each week, like water through a boot. But I watched the Council's new man go down with Kyonin's arrows in him, in Forn's cloak, with Forn's list in his coat, and I waited for it to howl. It didn't. It didn't move at all."
"I don't know what that means. I'm afraid to hope it means anything."''',
        c("Continue", "what")),
    kay("fumbled", '''"Days. Since the ravine." {n}She holds up the wrist, and her hand is not quite steady.{/n}
"You saw it. It came out and it had him and I let it. And now it's further in than it's ever been. I can feel the edge of it when I'm tired, soldier, like standing too near a drop in the dark. I keep tying them. I don't know how many more there'll be."''',
        c("Continue", "what")),
    kay("what", '''"It's in my blood now, the whole curse of my people. Any elf can become a drow. Any one of them. All you have to do is stop fighting for long enough." {n}She pulls the knot on her wrist tighter.{/n}
"There's no cure. There's no Light Fate, whatever your healers hope. The road only goes one way, and I'm a long way down it. I'm telling you so you'll know what you're keeping in your city."''',
        c('"Then we watch it together."', "together", flags=(CLOCK,)),
        c('"One-way roads are my favourite kind. I\'ve never once walked one the way it was built."', "trickster", flags=(CLOCK,)),
        c('"What do you need from me?"', "need", flags=(CLOCK,))),
    kay("together", '''"Together." {n}She turns the word over like a strange coin, foreign, probably counterfeit.{/n}
"The last person who said that to me was Anemora. She said it every night, holding my hand on the knife." {n}She lets go of the knot.{/n} "You say it differently. I haven't worked out how yet."''',
        c("[Stay a while in the shade with her.]")),
    kay("trickster", '''"Oh, you're so proud of yourself." {n}But her mouth has moved, and it doesn't quite move back.{/n}
"Walk it backwards, then. Walk it sideways. Walk it on your hands, soldier. When you find the way out of a curse older than Kyonin, come and tell me, and I'll walk it with you." {n}She pauses.{/n} "Until then I'll tie knots."''',
        c("[Stay a while in the shade with her.]")),
    kay("need", '''"Nothing. That's the trouble." {n}She laughs without any sound.{/n}
"In the Worldwound I needed a knife, and I had one, and I was too weak to use it. Here I need nothing. A roof. The shade. Somebody who doesn't lie. And every day I have them, the easier it would be to stop fighting." {n}She looks at you.{/n} "Don't make it too easy, soldier."''',
        c("[Stay a while in the shade with her.]")),
], requires=(RULES,), forbids=(CLOCK,), delay=24, optional=False,
    RequiresAnyGroups=[[STALLED, SWAP_CLEAN, SWAP_FUMBLED]])   # every return carries exactly one of these


meet(BEAST_SCENE, "The lamp-holder", '"You look like you\'ve heard something."', [
    kay("open", '''"Walk with me, soldier. Your guards have a woman from the north road. They say she wore a dead crusader's tabard and led travellers toward a false campfire." {n}She gets up, leaving the bow against the crate.{/n} "They say they caught one of Anemora's scouts. I want to see whom they caught."''',
        c("[Go with her down to the cells.]", "cell")),
    nar("cell", '''{n}In the last cell a drow woman is chained to the wall. A crusader's tabard hangs over her mail. The gaoler lifts his lantern and begins his report: the patrol found her beside an abandoned camp; a carter swore she had beckoned him off the road.{/n}
"Kay." {n}The prisoner looks past the lantern at Kaylessa. Kaylessa puts a hand on the gaoler's arm, stopping the report.{/n}''',
        c("Continue", "who")),
    kay("who", '''"Tessariel. We were Wasps together. We used to get reports just like yours." {n}She releases the gaoler's arm.{/n} "A name. A witness. Enough to go out with knives. Anemora supplied both."
"I don't know what happened on your road. I know this woman. When Anemora offered us protection, she bent the knee. When they taught me what to do to the prisoners, she held the lamp. Every night. So I could see my work."
{n}Tessariel lowers her eyes. Kaylessa watches her hands on the chain.{/n}''',
        c("Continue", "ask")),
    nar("ask", '''{n}Something changes in the set of Kaylessa's shoulders. Her breathing slows. Her lips have drawn back from the fangs, and she doesn't seem to know it.{/n}''',
        c("Continue", "key")),
    kay("key", '''"Give me the key and an hour, soldier. Then go and have a drink somewhere. Don't come back until you're sent for."
{n}She turns her head to look at you, and her eyes are very bright.{/n} "I know what's asking. I'm asking anyway. That's how you'll know it's winning."''',
        c('[Give her the key and walk away] "Take your hour."', "fed", flags=(BEAST_MET, BEAST_FED), alignment=("Evil", 1)),
        c('[Stand in the doorway] "No. Not her. Not like this."', "stopped", flags=(BEAST_MET, BEAST_STOPPED)),
        c('[Offer her a crueller revenge] "Let her live. Send her home to tell Kyonin what she did, and what you both are."',
          check=dict(Skill="CheckDiplomacy", DC=26, Success="witness", Failure="too_late"))),
    nar("too_late", '''{n}She isn't listening. She's looking at Tessariel's hands on the chain, and whatever looks out through her eyes has already decided. There is no more time for clever words. There is only the key in your hand, and the doorway.{/n}''',
        c('[Give her the key and walk away] "Take your hour."', "fed", flags=(BEAST_MET, BEAST_FED), alignment=("Evil", 1)),
        c('[Stand in the doorway] "No."', "stopped", flags=(BEAST_MET, BEAST_STOPPED))),
    nar("fed", '''{n}You give her the key. She takes it without touching your fingers. On the stairs you hear the first sound behind you, and it isn't Tessariel's.{/n}
{n}An hour later Kaylessa comes up into the market with clean hands and sits down on her crate under the awning. She has washed her face. Her shoulders are loose, like a woman after a long sleep.{/n}''',
        c("Continue", "fed_after")),
    kay("fed_after", '''"It's quiet now. For tonight." {n}She looks at her hands in her lap.{/n}
"She held the lamp for nobody, soldier. I didn't need one. I see perfectly well in the dark." {n}The words are light. Her voice isn't.{/n} "Don't ever give me that key again. Or do. I can't tell any more which of us is asking."''',
        c("[Sit with her until the market closes.]")),
    nar("stopped", '''{n}You put yourself in the doorway, between her and the woman on the chain. She simply looks at you, the way she looked at Forn once, down a long drop. Then the knife is in her hand.{/n}''',
        c("Continue", "stopped_knife")),
    kay("stopped_knife", '''"Move, soldier." {n}Her voice is almost gentle.{/n} "You don't know what she did. You don't know what I did while she watched. Move."''',
        c("[Don't move.]", "stopped_after")),
    kay("stopped_after", '''{n}The knife is a finger's breadth from your throat for as long as it takes Tessariel to say the name again, and then it isn't. Kaylessa puts it away with a shaking hand.{/n}
"You'd have let me cut you. To keep her whole. Her." {n}A bad, broken sound that means to be a laugh.{/n} "She isn't worth it. Neither am I. Thank you, soldier. I hate you for it. Both. Let's go before I change my mind."''',
        c("[Take her back up into the light.]")),
    kay("witness", '''{n}It takes her a long time to hear you. When she does, she turns and looks at Tessariel properly, as though somebody had finally held the lamp the right way round.{/n}
"Crueller." {n}Something in her face comes back from wherever it went.{/n} "Yes. Send her home. Let her stand in front of the Winter Council and say it with her own mouth: we were wasps, we're drow, any elf can. Let them try to bury her. She's harder to bury than a letter."''',
        c("Continue", "witness_after")),
    kay("witness_after", '''"Tessariel." {n}She crouches by the chain, close enough to be bitten.{/n} "You're going home. You'll walk into Kyonin with that face on, no amulet, no courier's cloak, and you'll tell them who taught you. If you don't, I'll hear. I always hear."
{n}Tessariel stares at her. Then, very slowly, she nods.{/n}
{n}Kaylessa stands, and hands you the key, and doesn't let go of it straight away.{/n} "That was a good trick, soldier. Don't do it to me."''',
        c("[Unlock the chain.]", flags=(BEAST_MET, WASP_SENT))),
], requires=(CLOCK,), forbids=(BEAST_MET,), delay=48, optional=False)


meet(KNIFE_SCENE, "The dagger she didn't draw", '"What have you got there?"', [
    nar("open", '''{n}She has a dagger across her knees instead of the bow. It's a slender thing, leaf-shaped, with a hilt of pale Kyonin wood gone dark from hands. She's cleaning it, though there is nothing on it to clean.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Every wasp had one. Our own blade, blessed at the Savored Sting's altar the night we swore." {n}She turns it so the edge catches what little light there is.{/n}
"When Tessariel and the others came for me, after they'd all bent the knee, I had this in my belt. I knew exactly where to put it. I'd been taught." {n}She's quiet a moment.{/n} "I didn't. I couldn't find the strength to draw it. I wrote that down later, somewhere. That I wished I had."''',
        c("Continue", "fed", requires=(BEAST_FED,)),
        c("Continue", "stopped", requires=(BEAST_STOPPED,)),
        c("Continue", "sent", requires=(WASP_SENT,))),
    kay("fed", '''"So I carry it for the beast now. When it comes the rest of the way, I'll do what I couldn't do that night." {n}She doesn't look at you.{/n}
"It came very close, down in your cells. I had this in my boot the whole hour, and I didn't think of it once."''',
        c("Continue", "why")),
    kay("stopped", '''"So I carry it for the beast now. When it comes the rest of the way, I'll do what I couldn't do that night." {n}She glances at your throat, then away.{/n}
"I nearly used it on the wrong neck, in your cells. You didn't move. Idiot."''',
        c("Continue", "why")),
    kay("sent", '''"So I carry it for the beast now. When it comes the rest of the way, I'll do what I couldn't do that night." {n}Something that is almost a smile.{/n}
"Tessariel will be halfway to the border by now. I keep thinking of her walking into the Council's hall with her own face on. Better than any knife."''',
        c("Continue", "why")),
    kay("why", '''"I'm telling you because you ought to know where it is. In my left boot, mostly. Under my hand when I sleep." {n}She slides it back into its sheath, slowly.{/n}
"And because I'm tired of being the only one who knows."''',
        c('"Can I hold it?"', "hold", flags=(KNIFE_SHOWN,)),
        c('"Keep it close, then."', "close", flags=(KNIFE_SHOWN,)),
        c('"When the time comes, you won\'t be the one holding it alone."', "alone", flags=(KNIFE_SHOWN,))),
    kay("hold", '''{n}She looks at your open hand without moving. Then she puts the dagger in it, hilt first, and keeps two fingers on the pommel the whole time, and takes it back.{/n}
"Not yet." {n}Her fingers stay on the pommel a moment longer than they need to.{/n}''',
        c("[Let her keep it.]")),
    kay("close", '''"Always." {n}She pats the boot.{/n} "It's the one thing I own that nobody gave me and nobody took. Anemora never found it. Forn never found it. Your people never found it, either, when they went through my things."''',
        c("[Let her keep it.]")),
    kay("alone", '''{n}Her hand stops on the sheath.{/n} "Don't say things like that to me, soldier. Not unless you've thought about what they mean."
{n}She doesn't tell you to take it back. She sits there with her hand on the knife and her eyes on you, and she lets the words stay said.{/n}''',
        c("[Let her keep it.]")),
], requires=(BEAST_MET,), forbids=(KNIFE_SHOWN,), delay=24, optional=False,
    RequiresAnyGroups=[[BEAST_STOPPED, BEAST_FED, WASP_SENT]])   # every way out of the cells sets one


# --- The commit: she proposes. The knife, hilt first, no test. ------------------------------------------------------

meet(P + "commit", "Hilt first", '"You wanted to talk to me?"', [
    nar("open", '''{n}She isn't on the crate. She's standing at the back of the awning, where the shade is deepest, with the shawl down and the Kyonin dagger in her hand. When you come under the awning she doesn't sheathe it.{/n}''',
        c("Continue", "truth_first", requires=(LIED,), forbids=(CONFESSED,)),
        c("Continue", "speech", forbids=(LIED,)),
        c("Continue", "speech", requires=(LIED, CONFESSED))),
    kay("truth_first", '''"Rule three, soldier. You still haven't told me what that thing at your Council took for me. You lied about it on the first day, and it's been sitting in my throat ever since." {n}Her grip on the hilt doesn't change.{/n}
"Say it now. I'm not doing this with a lie still in the room."''',
        c('[Confess] "A branch where I become one of Shyka. They named their terms. I paid them."', "confessed", flags=(CONFESSED,)),
        c('"Not yet."', "not_yet")),
    kay("confessed", '''{n}She lets out a breath she seems to have been holding since the market.{/n} "There. That wasn't hard. That was only the truth."''',
        c("Continue", "speech")),
    kay("not_yet", '''"Not yet." {n}She nods, slowly, the way she'd note a wind change, and slides the dagger back into her boot.{/n}
"Then not tonight either. Rule three, soldier. I'm not handing my death to somebody who's still lying to me about my life." {n}She pulls the shawl up to her eyes.{/n} "I'll ask once more. Somewhere I choose. Have your answer ready."''',
        c("[Let her go.]", flags=(DECLINED,))),
    kay("speech", '''"Anemora made me into this to prove a point. Kyonin wants me dead to hide the point. Forn came for me with a speech about duty." {n}She turns the dagger in her hand until the blade lies along her own wrist.{/n}
"You're the first one in two years who wanted something from me that wasn't about the point. I don't know what it is yet. I think I want to find out."''',
        c("Continue", "fed", requires=(BEAST_FED,)),
        c("Continue", "offer", forbids=(BEAST_FED,))),
    kay("fed", '''"And I don't trust my own hand any more. Not since your cells." {n}She says it plainly, the way she'd report a broken wagon.{/n}''',
        c("Continue", "offer")),
    nar("offer", '''{n}She holds the dagger out to you, hilt first. Her hand is very steady.{/n}''',
        c("Continue", "ask")),
    kay("ask", '''"This is the knife I meant for the beast. For the night it comes the rest of the way. I couldn't use it on myself once, and I've been afraid ever since that I won't manage it the second time either."
"You stayed after we settled the rules. You heard about the clock and didn't leave. You went down into your own cells with me knowing what I might do there, and you came back up with me after." {n}Her mouth twists.{/n} "So it's yours. Take it, soldier."''',
        c('[Take the knife] "I\'ll hold it."', "took", flags=(COMMITTED, KNIFE_HELD)),
        c('[Close her fingers back around the hilt] "It\'s yours. So is the choice. I\'m staying either way."', "back",
          flags=(COMMITTED, KNIFE_BACK), forbids=(BEAST_FED,)),
        c('[Don\'t take it] "Not like this. Not as your executioner."', "no", flags=(DECLINED,)),
        c('[Give her the road] "Go to Kyonin. Tell your story yourself. I\'ll see you get there."', "road",
          flags=(LEFT, CLOSED)),
        c('[Close her fingers back around the hilt] "It\'s yours. So is the choice. I\'m staying either way."', "not_after",
          flags=(COMMITTED, KNIFE_HELD), requires=(BEAST_FED,))),
    kay("took", '''{n}You close your hand on the hilt. She lets go of it slowly, one finger at a time, as though she were letting go of a rope over a drop.{/n}
"There." {n}She looks at her empty hand.{/n} "That's the lightest I've been since Kyonin."
{n}Then she reaches up and pulls your face down to hers and kisses you, hard, with her fingers in your hair and her fangs careful.{/n}''',
        c("Continue", "after")),
    kay("back", '''{n}Your fingers close over hers on the hilt, and push the knife gently back against her own palm.{/n}
{n}She stares at your hand on hers. Something in her face breaks open, and she lets it.{/n} "You'd leave it with me. After everything you've seen." {n}Her voice has gone rough.{/n} "Nobody's ever left my death in my own hand, soldier. They take it off me, or they hold it for me."
{n}She kisses you with the knife still between your joined hands, hard, her fangs careful, and doesn't let go of either.{/n}''',
        c("Continue", "after")),
    kay("not_after", '''"No." {n}She pulls her hand out from under yours and pushes the hilt into your palm, and holds your fingers closed round it with both of hers.{/n}
"Not after the cells. I know what that hand does when it's left alone. Hold it for me, soldier. That's what I'm asking. That's all I'm asking."
{n}And then she kisses you, hard, and doesn't let go of your fingers.{/n}''',
        c("Continue", "after")),
    kay("after", '''{n}When she lets you go she's breathing fast, and her eyes are very red in the dark of the awning.{/n}
"Another night. Not here. Somewhere I choose." {n}She pulls the shawl back up to her eyes, and over it she looks younger than you've ever seen her.{/n} "Mind the rules, soldier."''',
        c("[Watch her go.]")),
    kay("no", '''{n}She looks at the knife, and at your empty hands.{/n}
"Not as my executioner." {n}She nods, slowly.{/n} "That's fair. It's not what I asked you, but it's fair." {n}She puts the dagger back in her boot.{/n}
"I'm not taking it back, soldier. I'm putting it away. There's a difference. One day I'll put it down somewhere, and you'll decide."''',
        c("[Let her go.]")),
    kay("road", '''"Kyonin." {n}She lowers the knife.{/n} "You'd send me home. With the truth. To the people who sent Forn."
{n}She looks, for a heartbeat, as if she might say yes to something else. Then her face closes, the way a door closes on a lit room.{/n} "You're right. It's mine to tell. Nobody else's." {n}She sheathes the dagger.{/n} "Goodbye, soldier. Thank you for the choice. It's the second one you've given me."''',
        c("[Watch her go.]")),
], requires=(KNIFE_SHOWN, READY), forbids=(COMMITTED, DECLINED), delay=24, optional=False)


# The knife, put down somewhere: her answer to the Commander's no (and to an unconfessed lie), with no price attached.
visit(P + "after.knife_on_table", "Put down somewhere", [
    nar("open", '''{n}When you come back to your quarters there is a dagger lying on your table: slender, leaf-shaped, with a hilt of pale Kyonin wood gone dark from hands. No note. The shutters are open and the lamp has been put out, because she prefers it dark.{/n}''',
        c("Continue", "lied", requires=(LIED,), forbids=(CONFESSED,)),
        c("Continue", "knife", forbids=(LIED,)),
        c("Continue", "knife", requires=(LIED, CONFESSED))),
    nar("lied", '''{n}Beside the blade there is a strip of cloth with its knots, and one word scratched into the wood of the table with the knife's point: PRICE.{/n}''',
        c('[Scratch the answer beside it] "My branch. Becoming one of Shyka, on the terms they named."', "knife", flags=(CONFESSED,)),
        c("[Leave the word unanswered.]", "leave_lie")),
    nar("knife", '''{n}The open shutter screens her from the doorway. She rests one hand on its edge, quite still. When you turn toward her, she steps out from behind it and looks at the knife.{/n}''',
        c("[Pick up the knife.]", "picked", flags=(COMMITTED, KNIFE_HELD, LATE_YES)),
        c("[Take it to the window and put it back in her hand.]", "handed", flags=(COMMITTED, KNIFE_BACK, LATE_YES),
          forbids=(BEAST_FED,)),
        c("[Leave it where it lies.]", "leave")),
    kay("picked", '''"Took you long enough." {n}She catches your collar with her empty hand and pulls you against the window frame. Her mouth finds yours, hard; then she draws back just far enough to look at the dagger.{/n} "Keep that where you can reach it. And come here, soldier."''',
        c("[Go to the window.]")),
    kay("handed", '''{n}Her fingers close round the hilt, and round yours.{/n} "Of course you'd do it the difficult way." {n}She sheathes the dagger in her boot before pulling you down beside her. Her kiss is hard enough to leave you holding the sill.{/n}''',
        c("[Stay.]")),
    nar("leave", '''{n}After a while the dagger goes from the table without your seeing it move, and the shutters close from outside.{/n}
{n}In the morning the shade under the tailor's awning is empty, and the crate has been turned over, and on the bottom of it someone has scratched the outline of a wasp.{/n}''',
        c("[Let her go.]", flags=(LEFT, CLOSED))),
    kay("leave_lie", '''{n}After a while the dagger goes from the table without your seeing it move.{/n}
"Rule three," {n}says the dark by the window, quite calmly.{/n} "It's the only one I'd kill over. I don't want to kill you, soldier. So I'll go."''',
        c("[Let her go.]", flags=(LEFT, CLOSED))),
], requires=(DECLINED,), forbids=(COMMITTED,), delay=72)


# --- Epilogue pages (Owner KaylessaEpilogue; appended in authored order; no effects). ----------------------------------

EP = dict(last=6, Relationship=REL)
KEPT_PARAS = (
    p("{n}Nobody ever worked out what Shyka the Many did with the branch the Commander paid for it. Once in a long while a note in three handwritings arrived, asking how it was going. She always made the Commander answer it.{/n}", requires=(SHYKA_PRICE,), forbids=(SHYKA_RAISED,)),
    p('''{n}Shyka kept the branch in which the Commander said yes and meant it. Kaylessa still reminded the Commander how the price had risen when they tried to bargain. She enjoyed that part of the story.{/n}''', requires=(SHYKA_RAISED,), forbids=("kaylessa.trickster.dead.borrow_sending",)),
    p("{n}The beast in her never took another step. It sat where it had stopped on the night she died in the Commander's world, and every morning of her life she checked it, and every morning it was there, and the Commander learned to wait until she had checked before saying good morning.{/n}", requires=(STALLED,), forbids=(BEAST_FED,)),
    p('''{n}The beast had fed in the crusade's cells, and it did not forget. Some mornings the thumb on Shyka's borrowed clock slipped a little. On those mornings she checked the knife before speaking. The Commander learned to wait.{/n}''', requires=(BEAST_FED, STALLED)),
    p("{n}The Winter Council's records list the drow Kaylessa as dead in Mendev, killed in the same night as the Council's hunter Forn Autumn Haze. The Council never asked who killed whom. It preferred not to know.{/n}", requires=(SWAP_CLEAN,), forbids=(SUCCESSOR, "kaylessa.wasps.letter_sent", "kaylessa.wasps.claimed_as_scout", "kaylessa.wasps.let_them_look")),
    p("{n}The Winter Council's records list the drow Kaylessa as dead in Mendev, killed in the same night as the nameless hunter it sent after Forn Autumn Haze. The Council never asked who killed whom. It preferred not to know.{/n}", requires=(SWAP_CLEAN, SUCCESSOR), forbids=("kaylessa.wasps.letter_sent", "kaylessa.wasps.claimed_as_scout", "kaylessa.wasps.let_them_look")),
    p('''{n}The living curse never stopped. When it advanced, she tied another knot in a strip of cloth and hung the strips by the door. The Commander learned to count them, and kept the number unspoken.{/n}''', any_groups=((SWAP_CLEAN, SWAP_FUMBLED),)),
    p("{n}The Winter Council knew she lived. Twice more it sent hunters. The first was found in the Drezen ravine with his own arrows in him. The second never arrived; the crusade's border patrol said he had turned for home, and would not say what they had told him.{/n}", requires=(COUNCIL_KNOWS,),
      forbids=("kaylessa.clearing.hunter_turned_back", "kaylessa.clearing.hunter_hers")),
    p("{n}The Winter Council knew she lived. The hunter it sent walked back into Kyonin with both hands broken and a letter pinned to his coat in her writing, and the Council hid him as it had hidden everything else. It sent no one after him.{/n}", requires=(COUNCIL_KNOWS,),
      any_groups=(("kaylessa.clearing.hunter_turned_back", "kaylessa.clearing.hunter_hers"),)),
    p("{n}She never again wore a face that was not her own. When she went among people she went wrapped to the eyes, or she went as she was, and let them stare.{/n}", requires=(AMULET,)),
    p("{n}The Commander carried a white scar high on one shoulder, from a Kyonin arrow meant for someone else. She would put her thumb on it sometimes, absently, in company, the way other women touch a ring.{/n}", requires=(ARROW,)),
    p("{n}In Kyonin a drow woman named Tessariel stood before the Winter Council with her own face on and told them where she had learned what she knew. The Council had her removed. It could not have the words removed. They went round the border forts for years.{/n}", requires=(WASP_SENT,)),
    p('''{n}The Commander kept the Kyonin dagger. It hung by the door, where either could reach it. She checked that it was there on bad mornings, and never asked for it back.{/n}''', requires=(KNIFE_HELD,)),
    p('''{n}She kept the Kyonin dagger sheathed in her left boot. The Commander had closed her fingers around it, and left her the choice. She sharpened it when it needed sharpening. The curse was still there.{/n}''', requires=(KNIFE_BACK,)),
    p("{n}In the clearing where Forn sprang his trap stands a tomb that Kyonin marksmen raised for a woman they had been told was dead. She visited it every year and left the flowers there that Calistrians leave for the vengeful dead, and read her own name aloud, and corrected nothing.{/n}", requires=(TOMB,)),
    p("{n}She kept her suspicion of the fourth rule to the end, and watched for the day the Commander would break one of hers. Nobody could say, afterwards, whether that day ever came. She said it had, and that she had allowed it.{/n}", requires=(RULE_FOUR,)),
    p("{n}She told the Commander which way she went, every night she went out. She never told anyone else.{/n}", requires=(EXTRA_RULE,)),
    p('''{n}Shyka kept the branch bought through the sending after the Council had gone. The Eldest had named the price; the Commander had paid it outright. Kaylessa did not forget what had been spent to bring her there.{/n}''', requires=(SHYKA_RAISED, "kaylessa.trickster.dead.borrow_sending")),
    p("{n}The beast had fed in the crusade's cells, and the curse kept advancing. She tied fresh knots in the cloth when it moved. On the worst mornings she checked the knots twice, then the knife, before saying a word to the Commander.{/n}", requires=(BEAST_FED,), any_groups=((SWAP_CLEAN, SWAP_FUMBLED),), forbids=(STALLED,)),
    p('''{n}Her living account reached Avennara. The Council called it a lie and forbade copies; the border guards made copies anyway. The Council had to answer a living witness, not a buried name. Kaylessa read the opened reply, strung her bow and kept watch.{/n}''', requires=("kaylessa.wasps.letter_sent",)),
    p('''{n}The Council investigated the Commander\'s drow scout. Kaylessa changed her night patrols and watched the eastern roads. She kept her name from strangers who came asking at the tailor's.{/n}''', requires=("kaylessa.wasps.claimed_as_scout",), forbids=("kaylessa.wasps.letter_sent",)),
    p('''{n}Word of the drow archer in Drezen's market travelled east. Hunters began asking at the tailor's. Kaylessa kept her own name from their questions and came home by a different gate.{/n}''', requires=("kaylessa.wasps.let_them_look",), forbids=("kaylessa.wasps.letter_sent", "kaylessa.wasps.claimed_as_scout")),
    p('''{n}Avennara's reply acknowledged the account of the Green Road courier. The border kept rolls; her family would have the truth of the capture. Kaylessa kept the acknowledgement with her own papers.{/n}''', requires=("kaylessa.wasps.remembered_the_courier", "kaylessa.wasps.letter_sent")),
    p("{n}The hunter from the cooper's cellar returned to Kyonin with broken fingers and a letter pinned to his coat. Kaylessa signed her name in full. The Council could no longer pretend not to know who lived in Drezen.{/n}", forbids=(COUNCIL_KNOWS,), any_groups=(("kaylessa.clearing.hunter_turned_back", "kaylessa.clearing.hunter_hers"),)),

)
# R2: these correspondence/exposure receipts also belong to late, allied and road endings.
EXPOSURE_PARAS = KEPT_PARAS[-5:]

SCENES.append(scene(P + "epilogue.no_lamb", "", "KaylessaEpilogue", 6, "", [
    nar("page", '''{n}The drow Kaylessa, once of the Sunset Wasps of Kyonin, stayed at the Commander's side through the Threshold and after it. She called the Commander "soldier" to the end of her days, in public and in private and in the middle of arguments, and nobody who heard it ever mistook it for anything but what it was.{/n}
{n}She was never tame. She kept her rules and made the Commander keep them. She hunted, at night, the kind of men the law had missed, and came home before light, and some of the men were found and some were not.{/n}
{n}She was not cured. There is no Light Fate. She lived with what was in her the way a soldier lives with a wound that will not close: carefully and angrily, one morning at a time, and she checked it every one of them.{/n}''',
        paragraphs=KEPT_PARAS)],
    requires=("trickster.ever", COMMITTED), forbids=(CLOSED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(P + "epilogue.commit", "", "KaylessaEpilogue", 6, "", [
    nar("page", '''{n}One evening after Threshold, Kaylessa walked into the Commander's rooms. The shutters were open; a low lamp burned on the table. She laid the Kyonin dagger beside it, hilt toward the Commander.{/n}
{n}"Your choice, soldier. I wanted to be sure you knew what you were taking."{/n}''',
        paragraphs=(
            p('''{n}The Commander closed a hand around the hilt. She let go, finger by finger. "After the knife," she said, and caught their collar. Her free hand worked at the grey laces at her throat.{/n}''', forbids=("kaylessa.clearing.night",)),
            p('''{n}The Commander closed a hand around the hilt. She let go, finger by finger. "No grass this time, soldier." She caught their collar and drew them toward the bed.{/n}''', requires=("kaylessa.clearing.night",)),
            # Explicit slot: late first night or chosen return; no flags and no cure.
            dict(p('''{n}She put out the lamp, caught the Commander\'s collar and drew them down beside her. Her kiss was hard, her hand steady. For tonight, she left the war outside the shutters.{/n}'''), Id=P + 'epilogue.commit.explicit.1'),
            p('''{n}In the morning the dagger hung on a nail by the door. Her first movement on waking was to check the clock. Then she told the Commander that they snored.{/n}''', forbids=(KNIFE_BACK,)),
            p('''{n}In the morning the dagger was sheathed in her left boot. Her first movement on waking was to check the clock. Then she told the Commander that they snored.{/n}''', requires=(KNIFE_BACK,)),
            p('''{n}She hunted at night and returned before daylight, tapping on the shutter. She kept her rules. On bad mornings she checked that the knife was within reach before climbing into bed. She was never cured.{/n}'''),
            p("{n}The beast in her never moved again from where it had stopped on the night of her death. She checked it every morning of her life.{/n}", requires=(STALLED,), forbids=(BEAST_FED,)),
            p('''{n}The beast had fed in the crusade's cells, and it did not forget. Some mornings the thumb on Shyka's borrowed clock slipped a little. On those mornings she checked the knife before speaking. The Commander learned to wait.{/n}''', requires=(BEAST_FED, STALLED)),
            p("{n}She never again wore a face that was not her own.{/n}", requires=(AMULET,)),
            p("{n}Tessariel's story reached every border fort in Kyonin before the Winter Council could bury it.{/n}", requires=(WASP_SENT,)),
            p("{n}In the living world the clock never stopped. She tied a knot for every step it took, and hung the strips by the door beside the knife.{/n}", any_groups=((SWAP_CLEAN, SWAP_FUMBLED),)),
            p("{n}The beast had fed in the crusade's cells, and the curse kept advancing. She tied fresh knots in the cloth when it moved. On the worst mornings she checked the knots twice, then the knife, before saying a word to the Commander.{/n}", requires=(BEAST_FED,), any_groups=((SWAP_CLEAN, SWAP_FUMBLED),), forbids=(STALLED,)),
        ) + EXPOSURE_PARAS)],
    requires=("trickster.ever", LATE_COMMITTED), forbids=(COMMITTED, CLOSED, DECLINED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(P + "epilogue.ally", "", "KaylessaEpilogue", 6, "", [
    nar("page", '''{n}Kaylessa stayed in Drezen until the war was over, under the tailor's awning, with her bow across her knees. When the Commander sat beside her, she made room. She kept her rules.{/n}
{n}She was not cured. She checked the clock each morning. When it moved, she said so; when it did not, she drank the tailor's tea and watched the gate.{/n}''', paragraphs=(
            p('''{n}There had been a kiss in the streets after curfew. But the Commander never told her what Shyka had taken. The price of her return lay between them, unspoken. She kept the dagger in her own hand.{/n}''', requires=("kaylessa.wasps.in_the_dark", LIED), forbids=(CONFESSED,)),
            p('''{n}There had been a kiss in the streets after curfew. When the Commander came under the awning, she still wanted them to stay. She kept the dagger in her own boot. There had been no promise to share a life.{/n}''', requires=("kaylessa.wasps.in_the_dark",), forbids=(LIED,)),
            p('''{n}The Commander had finally told her the price. She did not forget the lie, or the kiss in the dark. She still made room under the awning. The dagger remained in her own keeping.{/n}''', requires=("kaylessa.wasps.in_the_dark", LIED, CONFESSED)),
            p('''{n}The Commander knew where to find her: in the shade, watching the gate. Their talks returned to the war and the danger she carried. The knife remained hers.{/n}''', forbids=("kaylessa.wasps.in_the_dark",)),
        ) + EXPOSURE_PARAS)],
    requires=("trickster.ever", CLOCK), forbids=(LATE_COMMITTED, COMMITTED, CLOSED, DECLINED, LEFT), **EP))

SCENES.append(scene(P + "epilogue.declined", "", "KaylessaEpilogue", 6, "", [
    nar("page", '''{n}Kaylessa left the Commander's city after the fighting at Threshold ended, with no letter and no goodbye. She left the crate under the tailor's awning turned over, with a wasp scratched on the bottom of it, and the tailor kept it for years because nobody would buy it.{/n}
{n}She had said once that one day she would put the knife down somewhere, and the Commander would decide. She did not say where, or when. People who knew them both said the Commander never passed an open window at night without looking in.{/n}''')],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), **EP))

SCENES.append(scene(P + "epilogue.road", "", "KaylessaEpilogue", 6, "", [
    nar("page", '''{n}Kaylessa went home. She walked into Kyonin wrapped to the eyes in a courier's grey, and when she reached the border fort she unwrapped herself in the gateway and let the sentries see her as she was, and asked for Avennara by name.{/n}
{n}What she told the Winter Council, and what the Council did about it, is not written down anywhere the Council can reach. But for a long time afterwards the word went round the border forts, from sentry to sentry, in the dark: any elf. Any one of us. Absolutely anyone.{/n}
{n}The Commander received one letter from her, years later, with no signature. It said only: "Still no lamb, soldier."{/n}''',
        paragraphs=(p("{n}The letter was tied with a strip of cloth. It had no knots in it.{/n}", requires=(STALLED,)),
                    p("{n}She carried her account of the Green Road courier home herself. Avennara took it to the rolls of missing riders. Kaylessa waited for the search instead of letting another woman's disappearance pass for her own escape.{/n}", requires=("kaylessa.wasps.remembered_the_courier",), forbids=("kaylessa.wasps.letter_sent",))) + EXPOSURE_PARAS)],
    requires=("trickster.ever", LEFT), forbids=(COMMITTED,), **EP))


# --- Reactions: exactly the allocated three reactors (ledger 05 §3.1 row 26): Anevia, Woljif ("Chief"), Shyka. ----------

ANEVIA_GUARD = dict(ForbidOverrides={"anevia_gone": "anevia.trickster.returned"})
WOLJIF_GONE = ("woljif.dead", "woljif.kicked_out")

SCENES.append(reaction("Anevia", P + "react.anevia_amulet", (RETURNED, CAUGHT),
    '''"That one under the tailor's awning. Same girl I caught in your war camp, askin' every tent after a tall elf. I knocked some trinket out of her hand and it went off like a firework." {n}Anevia rolls her shoulders, easy, watchful.{/n}
"She still looks at me like I owe her for it. Maybe I do. Tell her the gate's watched both ways, Commander. And tell her I said hello, if she's the type."''',
    answer_list=ANEVIA_HUB, forbids=("anevia_gone",), chapter=3, last=5, Chapters=[3, 5],
    entry='"Seen anything odd at the market?"', portrait="Anevia", **ANEVIA_GUARD))

SCENES.append(reaction("Anevia", P + "react.anevia_awning", (RETURNED,),
    '''"There's somebody under the tailor's awning been watchin' my gate. Wrapped to the eyes. Stands like a soldier, sits like a hunter, and never buys a thing." {n}Anevia doesn't look toward the market. She doesn't need to.{/n}
"If she's yours, sweetheart, tell her she's got good habits. If she's not yours, tell me, and I'll go ask her who she is."''',
    answer_list=ANEVIA_HUB, forbids=("anevia_gone", CAUGHT), chapter=3, last=5, Chapters=[3, 5],
    entry='"Seen anything odd at the market?"', portrait="Anevia", **ANEVIA_GUARD))

SCENES.append(reaction("Anevia", P + "react.anevia_ravine", (SWAP_CLEAN,),
    '''"The south patrol brought an elf up out of the ravine after your little expedition. Kyonin grey, nice brooch, six Kyonin arrows in him. Kyonin's own fletching; I checked." {n}Anevia turns a pen through her fingers.{/n}
"I wrote it up as 'killed by allies, misadventure'. Nobody's come to claim him. Funny, that. Almost like somebody would rather he'd never been here at all."''',
    answer_list=ANEVIA_HUB, forbids=("anevia_gone",), chapter=5, last=5, Chapters=[5],
    entry='"Anything from the south patrol?"', portrait="Anevia", **ANEVIA_GUARD))

SCENES.append(reaction("Woljif", P + "react.woljif_goat", (RETURNED, "participant.woljif.available"),
    '''"Chief, there's a drow at the tailor's. Wrapped up like a dumpling, but it's a drow, I know a drow." {n}Woljif lowers his voice to what he believes is a whisper.{/n}
"She told me if I told anybody, she'd tell everybody about the thing with the goat. I don't know how she knows about the goat. Nobody knows about the goat. So I'm tellin' you, and only you, and that's not tellin' anybody, right?"''',
    answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5],
    entry='"You look worried."', portrait="Woljif"))

SCENES.append(reaction("Woljif", P + "react.woljif_haggled", (RETURNED, BEGGED, "participant.woljif.available"),
    '''"Chief, that drow asked you for a clean ending. Now she's under the tailor's awning, and that face-changin' whatsit has got a piece of your future." {n}Woljif rubs his neck.{/n}
"That's either the most romantic thing I ever heard or the worst. Maybe both. Probably both. Don't ever do that for me, all right? I'd never live it down."''',
    answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5],
    entry='"Something on your mind?"', portrait="Woljif"))

# Sol quality pass (BEL): the morning after the clearing, seen by the one companion who never misses a comings and goings.
SCENES.append(reaction("Woljif", P + "react.woljif_morning", ("kaylessa.clearing.grey_light", "participant.woljif.available"),
    '''"Chief. You rode in the east gate at the second horn with grass all down your back, and you got off that horse like someone who's been sat on a rock since dawn." {n}Woljif lowers his voice to what he believes is a whisper.{/n}
"And the one at the tailor's has had her shawl down when you rode in. Down! I saw her whole face. She nodded at me. I didn't know what to do, so I nodded back, and kept my bloody hands on my own purse. One nod doesn't make those teeth any smaller." {n}He squints at you.{/n} "Don't tell me where you were. I don't want to know. I want to know a bit."''',
    answer_list=WOLJIF_HUB, forbids=WOLJIF_GONE, chapter=3, last=5, Chapters=[3, 5],
    entry='"Something you want to say?"', portrait="Woljif"))

SCENES.append(reaction("Shyka", P + "react.shyka_note", (SHYKA_PRICE, RETURNED),
    '''{n}A note, folded into a shape that keeps changing when you are not looking at it, in three different handwritings, one of them yours.{/n}
"The branch you paid with is keeping well. In it you said yes, and we are very happy there, or will be, or were. How does this one end? We forgot to ask. We are asking." {n}At the bottom, in a child's hand:{/n} "Does she still say soldier?"''',
    remote=True, forbids=("shyka.gone",), chapter=3, last=5, Chapters=[3, 5], Kind="letter", portrait="Shyka"))


def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register the new relationship's own keys, its presence and its portrait fallbacks. Scenes are added by
    expansion.py; world keys the matrix already verified (kaylessa.dead, begged_death, tomb...) bind on demand."""
    _bind(payload, "SelectedAnswers", SELECTED_ANSWERS)
    _bind(payload, "SeenCues", SEEN_CUES)
    _bind(payload, "InventoryItems", INVENTORY)
    # R2: native automatic closure is history, not the Council's paid concealment.
    _bind(payload, "Etudes", {"kaylessa.message_auto_completed": "28582721f157405da88b3bf0afae97d6"})
    removable = payload.setdefault("RemovableItems", [])
    if INVENTORY[NOTE_HELD] not in removable:
        removable.append(INVENTORY[NOTE_HELD])
    _bind(payload, "MainCharacterFacts", FACTS)
    # E17: the ravine starts FornIsDead exactly as native Forn_Ambush/Cue_0040 would have (kaylessa.forn_dead reads it).
    startable = payload.setdefault("StartableEtudes", [])
    if FORN_IS_DEAD not in startable:
        startable.append(FORN_IS_DEAD)
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != groups:
            raise ValueError("Conflicting binding: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    payload.setdefault("Presences", {}).update({k: dict(v) for k, v in PRESENCES.items()})
    # Native BlueprintPortraits (the units' own m_Portrait) until custom art ships; a custom PNG always wins.
    fallbacks = payload.setdefault("PortraitFallbacks", {})
    for key, guid in (("Kaylessa", "f1d4b8ee52d14783a73cf6dea090ed41"), ("Forn", "d35dce02ae4c478b92cb92a9d35342f3"),
                      ("Shyka", "94e05a227c144fcaa0a37b1aa28110a1")):
        fallbacks.setdefault(key, guid)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'kaylessa.trickster.alive.amulet_swap',
    'kaylessa.trickster.dead.soldier',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
