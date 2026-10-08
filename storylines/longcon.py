"""The Long Con (Writer/handoffs/15-LONG-CON-OPENING.md, approved 2026-09-30; PP8): "Tell Them Who Sent You".

Canon: at the Blackwing Library pyre the Commander stops Chaleb's crusaders "in the name of... Baphomet!" (the two
TricksterUnlocked answers ReiforceTrixterBefore 8e1bf103 / ReiforceTrixterAfter 52c5fde9 -> Cue_0008 fa744b1c, which starts
CalebFooled 25d3d486). Chaleb swallows it whole: "We wish to join the ranks of the triumphant army of the Worldwound!"
(Cue_0048 6f7256d9), and canon's only exit is the Commander's order to rig the Gray Garrison library (Answer_0043 a970efff
-> Cue_0045 44402c7a "...another two barrels of alchemist's fire from the Gray Garrison storeroom!"), where the Garrison
explosion kills the group (etude 40468eed). Faxon is "the ranking member of the Templars of the Ivory Labyrinth in this
city" (Faxon/Cue_0005 c859d4e6) and hopes to bring Minagho heads (Cue_0019 14ea9eaf); she brands failures (Cue_0016
95e3c205). At Drezen she panics (Final_Battle_Middle/Cue_0001 2979e848), calls the Commander "my mortal toy" (Cue_0018
23c5c70c) and leaves on every native answer (Cue_0013 76d961a0).

Authored, and labelled so: the RRT order "tell them who sent you"; the Gray Garrison storeman who handed over the barrels
and survived the blast (not in the Caleb encounter pool); the templars' questions; the Commander's offer to Minagho; the
crusade's statements, the talk and its consequences. The legend is a cover story, never a mythic power: the mythic tag only
gates the Ch1 entry (EntryMythic TricksterUnlocked, as canon gates its own three Trickster answers).

Gating (doc 15 section 0): pre-banner content reads only TricksterUnlocked (the entry's native MythicRequirement) and
longcon.begun; the crusade's consequences (the talk, section 5) play on every path; the off-path note is the one page
that reads the Trickster flags, and only to stay away from it. Every scene here is Relationship "longcon"; the Areelu
crossing (section 4a) is Relationship "areelu". Route-owned callbacks live in their routes: Minagho's Ch5 variant nodes
(minagho_chivarro_trickster) and Areelu's lens memory (areelu_trickster).
"""
from story_format import c, n, scene
from storylines import lastcall_ledger

SCENES = []
REL = "longcon"
P = "longcon."

RELATIONSHIP = dict(
    Title="The long con",
    Description="A story I started at a pyre in Kenabres. I intend to be the one who finishes it.",
    Objective="See where the story goes",
    Guidance="Fool Chaleb at the Blackwing Library, then choose what he carries into the Gray Garrison.",
    StartedFlag=P + "begun", ClosedFlag=P + "abandoned", CommittedFlag=P + "talk_done",
    UnavailableFlags=[], FailureFlags=[])

# --- Canonical keys (doc 15 section 5.4 table; exact strings) ---------------------------------------------------------
BEGUN, LOUD, QUIET = P + "begun", P + "legend_loud", P + "legend_quiet"
CONFIRMED, PRISONER_SEEN = P + "rumour_confirmed", P + "prisoner_seen"
HANGED, KILLED, CLERK, FED = P + "prisoner_hanged", P + "prisoner_killed", P + "clerk_recorded", P + "legend_fed"
OFFER_HEARD, MINAGHO_KNEW = P + "offer_heard", P + "minagho_knew"
WITNESSED, CITADEL_DONE = P + "citadel_witnessed", P + "citadel_done"
TALK_DONE, STANDS, WARY = P + "talk_done", P + "talk_stands", P + "irabeth_wary"
MINDER, MINDER_SEEN = P + "minder", P + "minder_seen"
PROPOSED, OWED, VIA_IRABETH, VIA_WATCH = P + "sting_proposed", P + "sting_owed", P + "sting_via_irabeth", P + "sting_via_watch"
STING_DONE, STING_REFUSED, EXPOSED, SCAR, AGENT_LOST = (P + "sting_done", P + "sting_refused", P + "sting_exposed",
                                                      P + "sting_scar", P + "agent_lost")
DECEIVED, COLD_SEEN, OFFPATH = P + "watch_deceived", P + "irabeth_cold_seen", P + "offpath_note"
LIED = "irabeth.longcon_lied"
OWNED, NOTED, ACCOUNTED = P + "hanging_owned", P + "hanging_noted", P + "hanging_accounted"
AFTER_SEEN, ACCOUNT_SEEN, ACCOUNT_DECLINED = (P + "irabeth_after_hanging.seen", P + "hanging_account.seen",
                                              P + "hanging_account.declined")
JOKE_SEEN = P + "big_joke.seen"
# Areelu's crossing (section 4a): areelu.early.*
MASK, COURTESY, SILENT, OFFERED = ("areelu.early.mask_counted", "areelu.early.courtesy_done", "areelu.early.read_silent",
                                   "areelu.early.read_offered")

# --- Native readers (bound in trickster_world.BINDINGS) ----------------------------------------------------------------
FOOLED = "CalebFooled"                       # etude 25d3d4863357d7d4bb11243b11059a5a (Cue_0008 fa744b1c OnShow StartEtude)
BOTH_KILLED = "pyre.both_killed"             # SelectedAnswers Answer_0044 da1f8c42 ("one spot... three of you" -> Cue_0047)
ONE_KILLED = "pyre.one_killed"               # SelectedAnswers Answer_0053 d72a3d08 ("deal with him!" -> Cue_0057)
APPOINTED = "longcon.kc_appointed"           # SeenCues Tour_End_Queen/Cue_0057 99b869e1 (Galfrey acknowledges the Knight Commander's appointment)
NURAH_ASKED = "nurah.asked_what_she_wants"   # SelectedAnswers Nurah_After_Battle/Answer_0004 9a962124 (Cue_0009 has played)
NURAH_PACT = "nurah.trickster_recruited"     # etude NurahRecruitedByTrickster a879a3a6 (Answer_0109's pact)
FREED, REFUSED_A, REFUSED_B = "yaniel.freed_answer", "yaniel.refused_0006", "yaniel.refused_0036"
REACHED_CH3 = "longcon.reached_ch3"          # latch: Chapter03 or Chapter05 seen playing (the summons count from it)
IRABETH_GONE = ("irabeth_dead", "irabeth_gone", "irabeth_away")
RETURNED = "irabeth.trickster.returned"
HUB_OVERRIDES = {k: RETURNED for k in IRABETH_GONE}   # section 5.1: a restored Irabeth answers on her own hub
FALLEN = "longcon.drezen_fallen"             # Derived (trickster_world): the Swarm in Chapter 5 (Drezen is a ruin)
LEDGER_KEY = "trickster.secret.longcon"      # Derived: begun on a Trickster run (the Ledger's Secrets page)
DERIVED = {LEDGER_KEY: [[BEGUN, "trickster.ever"]]}

# --- Hosts -------------------------------------------------------------------------------------------------------------
CALEB_LIST = "99e167bfcc0f3a74ca25cdec4dbe4e39"    # Caleb_MainDialogue/AnswersList_0042 (Cue_0048, Cue_0114, SequenceExit_0088 after Cue_0047)
CALEB_LIST_B = "91fbd759907af9a43ba284ca8845ee45"  # AnswersList_0065 (shown instead after three rebukes; Cue_0057's only list)
CITADEL_LIST = "41dff710486d05d49bbb663f729ddabd"  # Final_Battle_Middle/AnswersList_0004 (Minagho, before she flees)
CITADEL_RETURN = "7be28a1118c8af24ebf757789b9cfa4c"  # Cue_0016 "Oh, I grow so tired of you mortals!..." (only answer: the list)
NURAH_LIST = "2ce412d70ca0f40468252bec95ab2881"    # Nurah_After_Battle/AnswersList_0003 (shared by Cue_0002/0009/0016)
YANIEL_LIST = "e47ef9ec640a1b4488ffb0c6a9983348"   # FakeYaniel_First/AnswersList_0003 (the prisoner in the dungeon)
YANIEL_RETURN = "38bb928a4aa04e64ea2bd3b665d16985"  # Cue_0030 "This war has known many losses..." (only answer: the list)
AREELU_LIST = "4ab7a78f96a994446a56a9bc27ac2bfb"   # FakeYaniel_ToAreelu/AnswersList_0002 (Areelu unmasked)
IRABETH_HUB = "871af36f2ab2b1f40b5de77976c54276"   # NPC_Common/Irabeth/AnswersList_0009
IRABETH = "280d4712dceb37f4a88e98f1f4c6e64f"       # IrabethTirabade_DrezenCapital
DREZEN = "2570015799edf594daf2f076f2f975d8"


def conv(id, text, *choices):
    """The native dialog's own speaker: Chaleb, Minagho, Nurah, Yaniel/Areelu (src/Main.cs InlineSpeaker)."""
    return n(id, "conversant", text, *choices)


def nar(id, text, *choices):
    return n(id, "Narrator", text, *choices)


def ira(id, text, *choices):
    return n(id, "Irabeth", text, *choices, portrait="Irabeth")


# === Section 2: the entry, "Tell them who sent you" (Ch1, Blackwing Library) =========================================

ENTRY = ('"You want into the Goat\'s army? Earn it. Wherever I send you next, you tell them who sent you: {name}. '
         'And you tell them who {name} answers to."')
CHALEB_BASE = ('''{n}Chaleb licks soot off his lip. Behind him the pyre is still smoking.{/n} "One of ours, walking with the crusaders and giving them orders?" {n}He almost laughs.{/n} "Then we've already won. I'll tell them, {mf|sir|ma'am}. Wherever you send me."''')
CHALEB_VARIANTS = [
    ("both_dead", '''{n}He steps over the bodies of his card-mates without looking down.{/n} "Just me, then. Fewer mouths to share the glory."''',
     (BOTH_KILLED,), ()),
    ("one_dead", '''{n}He jerks his head at the survivor, who flinches and keeps his eyes on the dead one.{/n} "He'll carry it too. He'd better."''',
     (ONE_KILLED,), (BOTH_KILLED,)),
]
TELL_DECISIONS = (
    c('"Shout it. Make every one of them hear my name."', "loud", flags=(BEGUN, LOUD), alignment=("Chaotic", 1)),
    c('"Only to whoever hands you the barrels. Quietly."', "quiet", flags=(BEGUN, QUIET), alignment=("Chaotic", 1)),
)
TELL_TAIL = [
    conv("loud", '''"Every one of them." {n}His chest swells under the scorched surcoat, the way it must have swelled the day he swore the Everbright oath, and the day he broke it.{/n} "They'll hear it in the cellars, {mf|sir|ma'am}. They'll hear it in the latrines."''',
         c("Continue")),
    conv("loud_alone", '''"Every one of them." {n}He wipes his blade on the dead man's sleeve and grins as if the two of you shared a joke.{/n} "And there's nobody left to tell it wrong."''',
         c("Continue")),
    conv("quiet", '''"Quiet. Aye." {n}He taps the side of his nose with a sooty finger, a conspirator's gesture, and looks absurdly pleased to be trusted with a secret.{/n} "The storeman, then. Nobody else hears it from me."''',
         c("Continue")),
]


def tell_nodes():
    loud_alone = dict(TELL_DECISIONS[0], Next="loud_alone", Requires=[BOTH_KILLED])
    loud = dict(TELL_DECISIONS[0], Forbids=[BOTH_KILLED])
    decisions = (loud, loud_alone, TELL_DECISIONS[1])
    nodes = [conv("start", CHALEB_BASE,
                  c("Continue", "both_dead", requires=(BOTH_KILLED,)),
                  c("Continue", "one_dead", requires=(ONE_KILLED,), forbids=(BOTH_KILLED,)),
                  *[dict(d, Forbids=sorted(set(d["Forbids"]) | {BOTH_KILLED, ONE_KILLED})) for d in decisions]),
             conv("both_dead", CHALEB_VARIANTS[0][1], *decisions),
             conv("one_dead", CHALEB_VARIANTS[1][1], *decisions)]
    return nodes + TELL_TAIL


for sid, lst in ((P + "tell_them", CALEB_LIST), (P + "tell_them_b", CALEB_LIST_B)):
    SCENES.append(scene(sid, "Tell them who sent you", "Chaleb", 1, ENTRY, tell_nodes(),
        requires=(FOOLED,), forbids=(BEGUN,), last=1, optional=True, Relationship=REL, Chapters=[1],
        AnswerLists=[lst], ReturnToList=True, EntryMythic="TricksterUnlocked",
        ReturnText="{n}Chaleb straightens and waits for his next order, as eager as a dog that has just been thrown a bone.{/n}"))


# === Section 2b: proof it travelled (Ch2): "The Prisoner's Story" =====================================================
# A remote page: the witness is a Gray Garrison storeman (authored; not in the Caleb pool). Two twins by the legend's
# shape. The variant reads the FINAL native history (Answer_0044 can be chosen after tell_them returns to the list).

PRISONER_OPEN = ('''{n}Crusade outriders drag a prisoner into camp at dusk: a cultist in a scorched storeroom apron, caught on the road north. He was running for Drezen, where the Goat's people still hold the walls. He threw down his knife when they surrounded him. When they throw him down in front of you he looks up, and his face falls apart.{/n}
"*You.* They said your name. The ones who came for the barrels."''')
LOUD_PLURAL = ('''"They bragged to the whole Garrison. {name} sent us, they said, {name} is the Goat's own. Everyone heard. Then the library went up, with them in it." {n}He can't stop looking at you.{/n}
"And now they say you're the *Knight Commander*. The templars came round asking who started it. For *her*, they said. The one with the hooves."''')
LOUD_SINGULAR = ('''"One of them. Big man, burned armour. He bragged to the whole Garrison: {name} sent me, {name} is the Goat's own. Then the library went up, with him in it." {n}He can't stop looking at you.{/n}
"And now they say you're the *Knight Commander*. The templars came round asking who started it. For *her*, they said. The one with the hooves."''')
QUIET_TEXT = ('''"The big one leaned over my counter and whispered it while I rolled out the barrels. {name}, he said. The Goat's own. I didn't tell anyone. Not till the library went up and the templars came round asking who'd been in the storeroom." {n}He swallows.{/n}
"For *her*, they said. The one with the hooves. And now they say you're the *Knight Commander*..."''')


def prisoner_choices():
    seen = (PRISONER_SEEN, CONFIRMED)
    return (c('"Hang him before he says it twice."', "hanged", flags=(*seen, HANGED), alignment=("Evil", 1)),
            c('"Let the clerk write it down. Every word."', "clerk", flags=(*seen, CLERK)),
            c('[Bluff] "Let him go, and make sure he gets back to them. Tell him I was *angry* he talked."', flags=seen,
              check=dict(Skill="CheckBluff", DC=15, Success="fed", Failure="killed")))


PRISONER_OUTCOMES = [
    nar("hanged", '''{n}The outriders look at each other, then at you, and then they go and find a rope. He does not beg. He keeps saying your name, quieter each time, until the rope stops him.{/n}''',
        c("Continue")),
    nar("clerk", '''{n}The camp clerk is fetched with ink still on his cuffs. He takes the storeman's statement down in a fair round hand, reads it back, has the man make his mark, and files it with the day's reports. Whoever reads the reports will read your name in it.{/n}''',
        c("Continue")),
    nar("fed", '''{n}You let half the camp hear you call him a traitor and a coward and a dead man, and at full dark the guards turn him loose "to be hunted down properly". He runs north toward Drezen like a man whose master has spared him out of contempt. Whatever he tells them there, he will tell it as the truth.{/n}''',
        c("Continue", flags=(FED,))),
    nar("killed", '''{n}You play the rage too well. The guards believe your anger and not your order: by morning the storeman is dead in the ditch behind the horse lines, "shot escaping". The sergeant reports it to you as a kindness, and waits to be thanked.{/n}''',
        c("Continue", flags=(KILLED,))),
]

SCENES.append(scene(P + "prisoner_loud", "The prisoner's story", "Commander", 2, "", [
    nar("start", PRISONER_OPEN,
        c("Continue", "plural", forbids=(BOTH_KILLED,)),
        c("Continue", "singular", requires=(BOTH_KILLED,))),
    nar("plural", LOUD_PLURAL, *prisoner_choices()),
    nar("singular", LOUD_SINGULAR, *prisoner_choices()),
    *PRISONER_OUTCOMES,
], requires=(LOUD, APPOINTED), forbids=(PRISONER_SEEN,), delay=48, last=2, optional=True, Relationship=REL,
   Remote=True, Chapters=[2], Kind="event"))
SCENES.append(scene(P + "prisoner_quiet", "The prisoner's story", "Commander", 2, "", [
    nar("start", PRISONER_OPEN, c("Continue", "quiet")),
    nar("quiet", QUIET_TEXT, *prisoner_choices()),
    *PRISONER_OUTCOMES,
], requires=(QUIET, APPOINTED), forbids=(PRISONER_SEEN,), delay=168, last=2, optional=True, Relationship=REL,
   Remote=True, Chapters=[2], Kind="event"))


# === Section 3: the offer in the citadel (Ch2, Minagho) ===============================================================
# Inline on Minagho's last list in the citadel; the check forbids ReturnToList, so the scene returns to her own Cue_0016
# (retcheck OK: its only answer is the host list), and her rant replays as her turning back to the room.

CITADEL_ENTRY = ('"You brand the ones who fail you. You just lost the Goat his fortress. Ask your templars what Kenabres '
                 'says about me, and then you\'ll know where to run when he sends for you."')
SCENES.append(scene(P + "citadel_offer", "Where to run", "Minagho", 2, CITADEL_ENTRY, [
    nar("start", '''{n}Staunton stands stunned where she left him, his grey lips still moving without a sound. You raise your voice so that the crusaders who came up the citadel with you catch every word.{/n}''',
        c('[Bluff] [Hold her eyes, as if you already know her answer.]', flags=(WITNESSED, CITADEL_DONE),
          requires=(FED,), check=dict(Skill="CheckBluff", DC=14, Success="heard", Failure="lost")),
        c('[Bluff] [Hold her eyes, as if you already know her answer.]', flags=(WITNESSED, CITADEL_DONE),
          requires=(CONFIRMED,), forbids=(FED,), check=dict(Skill="CheckBluff", DC=16, Success="heard", Failure="lost")),
        c('[Bluff] [Hold her eyes, as if you already know her answer.]', flags=(WITNESSED, CITADEL_DONE),
          forbids=(CONFIRMED,), check=dict(Skill="CheckBluff", DC=20, Success="heard_blind", Failure="lost"))),
    conv("heard", '''{n}Her head keeps jerking toward the doors.{/n} "*You're* the one my templars were whining about?" {n}A shrill little laugh, too fast.{/n} "Good. When he comes looking for a traitor, he'll find you first, my mortal toy." {n}Her voice drops, quick and greedy.{/n} "...And if I ever need something between me and him, I know where it lives."
{n}Then she remembers the room, and the shrillness comes back up, louder, as if you had never spoken.{/n}''',
         c("Continue", flags=(OFFER_HEARD, MINAGHO_KNEW))),
    conv("heard_blind", '''"Run to *you*?" {n}She laughs through her teeth, already edging toward the doors.{/n} "Mortal, you couldn't even keep me in Kenabres." {n}But her face turns back to you, once, and stays a heartbeat too long.{/n} "...Remember you said it. I will."
{n}Then her voice climbs again, back to the room and back to her audience.{/n}''',
         c("Continue", flags=(OFFER_HEARD,))),
    nar("lost", '''{n}Minagho is already turning toward the doors before you finish, and gives no sign that a word of it reached her.{/n}
{n}The crusaders at your back heard every word.{/n}''',
        c("Continue")),
], requires=(BEGUN,), forbids=(CITADEL_DONE,), last=2, optional=True, Relationship=REL, Chapters=[2],
   AnswerLists=[CITADEL_LIST], NativeReturnCue=CITADEL_RETURN))


# === Section 3, Nurah: "the big joke" (Ch2, optional deepening; canon's own Trickster pact) ===========================
# Cue_0009 (the spec's return) has already played when Answer_0004 is selected; replaying it would repeat her "big joke"
# speech straight after this exchange (13 section 2a item 6), so the scene returns to her list.

SCENES.append(scene(P + "big_joke", "The big joke", "Nurah", 2,
    '"If you ever reach their people again, they\'ll tell you I serve the Goat. Don\'t contradict them."', [
    conv("start", '''{n}Nurah's eyes narrow. Then the smirk comes back, slower than before.{/n} "So *that's* the big joke. You told them you were theirs too." {n}She looks down at her bloody hands, and back up at you.{/n}
"Let them believe it. If I get the chance, I'll help you make fools of the lot of them."''',
         c('"Then you\'ll do well."', flags=(JOKE_SEEN,)),
         c('"Don\'t enjoy it too much."', flags=(JOKE_SEEN,))),
], requires=(NURAH_ASKED, BEGUN, NURAH_PACT), forbids=(JOKE_SEEN,), last=2, optional=True, Relationship=REL, Chapters=[2],
   AnswerLists=[NURAH_LIST], ReturnToList=True,
   ReturnText="{n}Nurah wipes her bloody hands on her sleeve, slowly, as though that might help.{/n}"))


# === Section 4a: Areelu, "Two masks" (Ch2; Relationship areelu) ========================================================
# Before the prisoner's fate is decided, the Commander who played the Goat's officer at Blackwing recognises the craft.
# She stays in role. The return is her own Cue_0030 (retcheck OK), which reads as Yaniel going on with the part.

SCENES.append(scene("areelu.early.two_masks", "Two masks", "Areelu", 2,
    '"You know exactly where to pause. Whoever you\'re performing for, it isn\'t me."', [
    conv("start", '''{n}The old woman lifts her head. For a heartbeat the clear blue eyes are not tired at all; then the strange smile comes, and goes.{/n}
"Years in this place, and you think I am *performing*?" {n}Her head sinks back toward her chest.{/n} "Perhaps it is easier to believe in a trick than to look at what became of us."''',
         c("[Let it go.]", flags=(MASK,)),
         c('"Perhaps."', flags=(MASK,))),
], requires=(BEGUN,), forbids=(MASK, FREED, REFUSED_A, REFUSED_B), last=2, optional=True, Relationship="areelu",
   Chapters=[2], AnswerLists=[YANIEL_LIST], NativeReturnCue=YANIEL_RETURN, EntryMythic="TricksterUnlocked"))

# The reveal: two twins on her unmasked list. She does not ask (her canon "don't tell me, I want to figure it out for
# myself", Cue_0014 f1a82798); the Commander may volunteer, and she files the answer as one more performance.
COURTESY_ENTRY = '"I counted your pauses in that cell. You knew I was counting."'
SCENES.append(scene("areelu.early.courtesy_freed", "One more performance", "Areelu", 2, COURTESY_ENTRY, [
    conv("start", '''"You saw the mask and broke the shackles anyway." {n}She holds up one ink-smudged finger before you can speak.{/n} "Don't. I'll enjoy working it out."''',
         c("[Say nothing.]", "silent", flags=(COURTESY, SILENT)),
         c('"It was curiosity."', "offered", flags=(COURTESY, OFFERED))),
    conv("silent", '''{n}She tilts her head and watches you say nothing, the way a collector watches a specimen that has not yet decided to move. Then she studies you, and smiles.{/n}''',
         c("Continue")),
    conv("offered", '''"That's what someone would say who wanted me to think it was curiosity." {n}The smile does not change at all.{/n}''',
         c("Continue")),
], requires=(MASK, FREED), forbids=(COURTESY,), last=2, optional=True, Relationship="areelu", Chapters=[2],
   AnswerLists=[AREELU_LIST], ReturnToList=True,
   ReturnText="{n}Areelu folds her ink-smudged hands, quite at ease, and waits.{/n}"))
SCENES.append(scene("areelu.early.courtesy_refused", "One more performance", "Areelu", 2, COURTESY_ENTRY, [
    conv("start", '''"You saw the mask and would not strike the shackles yourself." {n}The same finger.{/n} "No. Let me guess. I like guessing."''',
         c("[Say nothing.]", "silent", flags=(COURTESY, SILENT)),
         c('"Thrift."', "offered", flags=(COURTESY, OFFERED))),
    conv("silent", '''{n}She tilts her head and watches you say nothing, the way a collector watches a specimen that has not yet decided to move. Then she studies you, and smiles.{/n}''',
         c("Continue")),
    conv("offered", '''"Now I have two things to weigh: what you did, and what you would like me to believe about it." {n}She sounds delighted, and looks nothing of the kind.{/n}''',
         c("Continue")),
], requires=(MASK,), RequiresAnyGroups=[[REFUSED_A, REFUSED_B]], forbids=(FREED, COURTESY), last=2, optional=True,
   Relationship="areelu", Chapters=[2], AnswerLists=[AREELU_LIST], ReturnToList=True,
   ReturnText="{n}Areelu's smile doesn't reach anything.{/n}"))


# === Section 5: the cost, paid in Ch3 ("The talk") ====================================================================
# Two voices (Irabeth on her hub or in a letter; an Eagle Watch sergeant in her absence), one node graph: the clause
# about the prisoner (exclusive outcomes of one page), the citadel clause, the skip clause, the hanging prelude, the ask.

CLAUSES = {
    "irabeth": dict(
        clerk_plural=('''"A Gray Garrison storeman's statement is in the clerk's book. It says the men who blew the Garrison library went in shouting your name as the Goat's own."''',
                      (CLERK, LOUD), (BOTH_KILLED,)),
        clerk_singular=('''"A Gray Garrison storeman's statement is in the clerk's book. It says the man who blew the Garrison library went in shouting your name as the Goat's own."''',
                        (CLERK, LOUD, BOTH_KILLED), ()),
        clerk_quiet=('''"A Gray Garrison storeman's statement is in the clerk's book. It says a man whispered your name across his counter as the Goat's own, and the templars made him repeat it."''',
                     (CLERK, QUIET), ()),
        fed=('''"Outriders brought you a Gray Garrison storeman with your name in his mouth as the Goat's own, and you let him walk out of our camp to go and say it again."''',
             (FED,), ()),
        hanged=('''"Outriders brought you a Gray Garrison storeman with your name in his mouth as the Goat's own. A prisoner you had hanged before he could say it twice."''',
                (HANGED,), ()),
        killed=('''"Outriders brought you a Gray Garrison storeman with your name in his mouth as the Goat's own. A prisoner who died 'escaping' from your guards the same night."''',
                (KILLED,), ()),
        citadel='''"And the crusaders who stormed the citadel with you heard you shout an offer to the demon while our dead were still warm. I have three sworn statements."''',
        skip='''"A Kenabres patrol report came up with the supply wagons. They stopped a deserter on the Gray Garrison road, one Chaleb Sazomal, and let him through because he swore {name} had sent him. 'On the Goat's business,' he said, and laughed as if it were a joke. Then he vanished." "I'd like to hear why that sentence has your name in it."''',
        ask='''"I don't want an explanation, Commander. I want to know what you're going to do about it."''',
    ),
    "watch": dict(
        clerk_plural=('''"There's a storeman's statement in the clerk's book, {mf|sir|ma'am}. Gray Garrison. Says the men who blew the library went in shouting your name. As the Goat's own."''',
                      (CLERK, LOUD), (BOTH_KILLED,)),
        clerk_singular=('''"There's a storeman's statement in the clerk's book, {mf|sir|ma'am}. Gray Garrison. Says the man who blew the library went in shouting your name. As the Goat's own."''',
                        (CLERK, LOUD, BOTH_KILLED), ()),
        clerk_quiet=('''"There's a storeman's statement in the clerk's book, {mf|sir|ma'am}. Gray Garrison. Says a man whispered your name over his counter, as the Goat's own, and the templars made him say it again."''',
                     (CLERK, QUIET), ()),
        fed=('''"The outriders say they brought you a Gray Garrison storeman with your name in his mouth, {mf|sir|ma'am}, and you let him walk off to go and say it again."''',
             (FED,), ()),
        hanged=('''"The outriders say they brought you a Gray Garrison storeman with your name in his mouth, {mf|sir|ma'am}. And that you had him hanged before he could say it twice."''',
                (HANGED,), ()),
        killed=('''"The outriders say they brought you a Gray Garrison storeman with your name in his mouth, {mf|sir|ma'am}. Died 'escaping' the same night. The lads on that picket don't talk about it."''',
                (KILLED,), ()),
        citadel='''"And there's three sworn statements from the lads who went up the citadel stair with you. Say you shouted some offer to the demon woman. While our dead were still warm, one of them put it."''',
        skip='''"A patrol report came up from Kenabres with the wagons, {mf|sir|ma'am}. They stopped a deserter on the Gray Garrison road, Chaleb Sazomal by name, and let him through because he swore you'd sent him. 'On the Goat's business,' he said, and laughed. Then he vanished." "The men want to know why your name's in it. I said I'd ask."''',
        ask='''"So I'm to ask what you mean to do about it, {mf|sir|ma'am}. Begging your pardon. Not why. What."''',
    ),
}
PRISONER_CLAUSES = ("clerk_plural", "clerk_singular", "clerk_quiet", "fed", "hanged", "killed")
FIVE = (CLERK, FED, HANGED, KILLED, WITNESSED)   # section 5.2: "none of the five" is the skip case


def talk_nodes(voice, speak, opening, sets, prelude):
    """The talk's graph for one voice. sets = per-outcome flag tuples; prelude = the hanging nodes for this voice."""
    t = CLAUSES[voice]

    def after_prisoner():
        return (c("Continue", "citadel", requires=(WITNESSED,)),
                c("Continue", "hanging", requires=(HANGED,), forbids=(WITNESSED,)),
                c("Continue", "ask", forbids=(WITNESSED, HANGED)))
    start_choices = [c("Continue", key, requires=t[key][1], forbids=t[key][2]) for key in PRISONER_CLAUSES]
    start_choices += [c("Continue", "citadel", requires=(WITNESSED,), forbids=(CLERK, FED, HANGED, KILLED)),
                      c("Continue", "skip", forbids=FIVE)]
    nodes = [speak("start", opening, *start_choices)]
    nodes += [speak(key, t[key][0], *after_prisoner()) for key in PRISONER_CLAUSES]
    nodes.append(speak("citadel", t["citadel"], c("Continue", "hanging", requires=(HANGED,)),
                       c("Continue", "ask", forbids=(HANGED,))))
    nodes.append(speak("skip", t["skip"], c("Continue", "ask", flags=(CONFIRMED,))))
    nodes += prelude
    lie = c('[Bluff] "It was never a rumour. It\'s been a Watch-sanctioned ruse since Kenabres. Your own people in the lower city knew."',
            check=dict(Skill="CheckBluff", DC=20, Success="lie_ok", Failure="lie_bad"), alignment=("Chaotic", 1))
    nodes.append(speak("ask", t["ask"],
        c('"Pay the companies who lost people in the citadel. Out of the crusade\'s purse. Tonight."', "coin",
          flags=sets["coin"], forbids=(HANGED,), crusade=("Favors", -100)),
        c('"Let them talk. I\'ve been called worse by better."', "stand", flags=sets["stand"]),
        c('"Then let\'s use it. The cults think I\'m theirs. Put me in a cellar as bait, and have the Watch follow whoever comes."',
          "propose", flags=sets["propose"]),
        lie))
    return nodes


def irabeth_outcomes(speak):
    return [
        speak("coin", '''"...That'll stop the talk in the ranks." {n}She makes a note in the margin, small and exact.{/n} "It won't stop me wondering."''',
              c("Continue")),
        speak("stand", '''"Then they'll keep talking." {n}She closes the ledger.{/n} "And I'll keep listening."''',
              c("Continue")),
        speak("propose", '''{n}She is quiet while she weighs it, turning her pen end over end.{/n} "You're offering to be the bait for a story you started." {n}A slow nod.{/n} "Fine. We run it properly, and you *attend*. I'll send word when a contact bites."''',
              c("Continue")),
        speak("lie_ok", '''{n}She frowns, and then decides that her own people failing to tell her is the likelier failure. You watch her decide it.{/n} "Then we'll finish it properly. You'll be the bait, in a cellar in the lower city. I'll send word."''',
              c("Continue", flags=(TALK_DONE, LIED, OWED, VIA_IRABETH))),
        speak("lie_bad", '''"My people in the lower city report to me, Commander." {n}Not a flicker.{/n} "That's a good story. Tell it to someone who doesn't sign their pay."''',
              c("Continue", flags=(TALK_DONE, STANDS, WARY))),
    ]


def watch_outcomes(speak):
    return [
        speak("coin", '''"Coin, {mf|sir|ma'am}. Aye. That'll quiet the barracks." {n}He doesn't look quieted.{/n} "The Watch'll still want a man on your door, mind. Orders from upstairs. Nothing personal."''',
              c("Continue")),
        speak("stand", '''"Let them talk." {n}He repeats it as if committing it to memory for someone above him.{/n} "Then the Watch'll put a man on your door, {mf|sir|ma'am}. So nobody gets ideas. Either way round."''',
              c("Continue")),
        speak("propose", '''{n}He blinks, then straightens, as if somebody had finally given him an order he understood.{/n} "Bait. In a cellar. With us in the dark." {n}A slow grin.{/n} "Commander Tirabade would've liked that. I'll pass it up, {mf|sir|ma'am}, and somebody'll send word when a contact bites."''',
              c("Continue")),
        speak("lie_ok", '''"Sanctioned. Since Kenabres." {n}Relief floods his face: the one answer that means none of it is his problem.{/n} "Then we'll finish it, {mf|sir|ma'am}. A cellar in the lower city, you as the bait. Somebody'll send word."''',
              c("Continue", flags=(TALK_DONE, DECEIVED, OWED, VIA_WATCH))),
        speak("lie_bad", '''"Sanctioned." {n}He says it the way a man tests a coin with his teeth.{/n} "Commander Tirabade kept her own books, {mf|sir|ma'am}, and there's nothing like that in them. I'll tell the men you said so. And the Watch'll be putting a man on your door."''',
              c("Continue", flags=(TALK_DONE, STANDS, MINDER))),
    ]


IRABETH_SETS = dict(coin=(TALK_DONE, WARY), stand=(TALK_DONE, STANDS, WARY), propose=(TALK_DONE, PROPOSED, OWED, VIA_IRABETH))
WATCH_SETS = dict(coin=(TALK_DONE, MINDER), stand=(TALK_DONE, STANDS, MINDER), propose=(TALK_DONE, PROPOSED, OWED, VIA_WATCH))


def irabeth_prelude(speak):
    """Section 5.2b: the hanging, answered first (Irabeth). Both answers set hanging_owned and irabeth_wary."""
    return [
        speak("hanging", '''"Before any of that." {n}Her voice stays level, which is worse.{/n} "You hanged a man who had surrendered. On what authority, and for what crime?"''',
              c('"He\'d have spread it further. I stopped it."', "hanging_spread", flags=(OWNED, WARY)),
              c('"He was a cultist. That\'s the crime."', "hanging_crime", flags=(OWNED, WARY))),
        speak("hanging_spread", '''"You executed a prisoner to protect a *rumour*." {n}She lets that sit in the room between you.{/n} "Paying the companies won't answer for a hanging, Commander. So don't offer."''',
              c("Continue", "ask")),
        speak("hanging_crime", '''"Then who questioned him? What did he tell us before you killed him?" {n}She waits.{/n}
{n}Nobody questioned him. She knows it. She writes something down anyway.{/n} "Paying the companies won't answer for a hanging, Commander. So don't offer."''',
              c("Continue", "ask")),
    ]


def watch_prelude(speak):
    """Section 5.2b, sergeant version: no interrogation (above his rank); the hanging goes into the minder's orders."""
    return [
        speak("hanging", '''"And the hanging, {mf|sir|ma'am}." {n}He looks at the wall behind your head.{/n} "That's not mine to ask about. It's gone up to the Watch officers. They've written it into someone's standing orders, is all I know."''',
              c("Continue", "ask", flags=(NOTED, MINDER))),
    ]


def irabeth_letter_outcomes(speak):
    """The summons' replies: the Commander writes back, and Irabeth's answer comes by the same runner."""
    return [
        speak("coin", '''{n}Her answer comes back by the same runner, one line under your own:{/n} "That'll stop the talk in the ranks. It won't stop me wondering."''',
              c("Continue")),
        speak("stand", '''{n}Her answer comes back by the same runner:{/n} "Then they'll keep talking. And I'll keep listening."''',
              c("Continue")),
        speak("propose", '''{n}Her answer takes until evening, and is longer than her first note.{/n} "You're offering to be the bait for a story you started. Fine. We run it properly, and you *attend*. I'll send word when a contact bites."''',
              c("Continue")),
        speak("lie_ok", '''{n}Her answer takes until evening.{/n} "Then my own people failed to tell me, and I'll be having words with them. We'll finish it properly. You'll be the bait, in a cellar in the lower city. I'll send word."''',
              c("Continue", flags=(TALK_DONE, LIED, OWED, VIA_IRABETH))),
        speak("lie_bad", '''{n}Her answer comes back within the hour.{/n} "My people in the lower city report to me, Commander. That's a good story. Tell it to someone who doesn't sign their pay."''',
              c("Continue", flags=(TALK_DONE, STANDS, WARY))),
    ]


def irabeth_letter_prelude(speak):
    return [
        speak("hanging", '''"Before any of that. You hanged a man who had surrendered. On what authority, and for what crime? Answer me in writing, if you won't come."''',
              c('"He\'d have spread it further. I stopped it."', "hanging_spread", flags=(OWNED, WARY)),
              c('"He was a cultist. That\'s the crime."', "hanging_crime", flags=(OWNED, WARY))),
        speak("hanging_spread", '''{n}She has underlined one word of your answer and sent it back.{/n} "You executed a prisoner to protect a *rumour*. Paying the companies won't answer for a hanging, Commander. So don't offer."''',
              c("Continue", "ask")),
        speak("hanging_crime", '''{n}Her reply is two lines.{/n} "Then who questioned him? What did he tell us before you killed him?"
{n}Nobody questioned him, and she knows it. The second line:{/n} "Paying the companies won't answer for a hanging, Commander. So don't offer."''',
              c("Continue", "ask")),
    ]


def watch_letter_outcomes(speak):
    return [
        speak("coin", '''{n}A reply comes back from the Watch house in the same careful hand:{/n} "Coin. Aye. That'll quiet the barracks. The officers say there's still to be a man on your door, nights. Orders. Nothing personal."''',
              c("Continue")),
        speak("stand", '''{n}A reply comes back from the Watch house:{/n} "Let them talk, you said. Then the officers say there's to be a man on your door, so nobody gets ideas. Either way round."''',
              c("Continue")),
        speak("propose", '''{n}A reply comes back from the Watch house, and for once the spelling is good:{/n} "Bait, in a cellar, with us in the dark. Commander Tirabade would've liked that. Word will be sent when a contact bites."''',
              c("Continue")),
        speak("lie_ok", '''{n}A reply comes back from the Watch house, with relief in every line:{/n} "Sanctioned since Kenabres. Then it's not ours to fret over. We'll finish it: a cellar in the lower city, you as the bait. Word will be sent."''',
              c("Continue", flags=(TALK_DONE, DECEIVED, OWED, VIA_WATCH))),
        speak("lie_bad", '''{n}A reply comes back from the Watch house:{/n} "Commander Tirabade kept her own books, and there's nothing like that in them. The men have been told what you said. And there's to be a man on your door."''',
              c("Continue", flags=(TALK_DONE, STANDS, MINDER))),
    ]


def watch_letter_prelude(speak):
    return [
        speak("hanging", '''"And about the hanging. That's not ours to ask about. It's gone up to the Watch officers, and they've written it into someone's standing orders, is all we know."''',
              c("Continue", "ask", flags=(NOTED, MINDER))),
    ]


IRA_OPEN = ('''{n}Irabeth closes the ledger she was reading and does not put it away. The officers' room is empty except for the two of you, which is not an accident.{/n}
"I have, Commander. In private, before it goes anywhere else."''')
SGT_OPEN = ('''{n}An Eagle Watch sergeant is waiting outside your quarters, helmet under his arm, the way men wait for a flogging.{/n}
"Commander Tirabade's gone, so it falls to me. The men have a question, {mf|sir|ma'am}, and I'm the one who drew the short straw."''')
IRA_LETTER_OPEN = ('''{n}The note is in Irabeth's square hand, folded twice, sealed with plain wax and no device. It is short.{/n}
"Commander. You have not come to me, so this comes to you. I would rather have said it to your face. Here it is anyway."''')
WATCH_LETTER_OPEN = ('''{n}The note comes under the door, on Eagle Watch paper, signed by a sergeant whose name you do not know. The hand is careful and badly spelled.{/n}
"With respect, {mf|sir|ma'am}. Commander Tirabade not being here, the men asked me to put it to you."''')


def ira_letter(id, text, *choices):
    return n(id, "Irabeth", text, *choices, portrait="Irabeth")


TALK_GATES = dict(last=5, optional=True, Relationship=REL)

SCENES.append(scene(P + "the_talk", "The talk", "Irabeth", 3, '"You look like you\'ve been waiting to say something, Irabeth."',
    [*talk_nodes("irabeth", ira, IRA_OPEN, IRABETH_SETS, irabeth_prelude(ira)), *irabeth_outcomes(ira)],
    requires=(BEGUN,), forbids=(TALK_DONE, *IRABETH_GONE, FALLEN), Chapters=[3, 5], Areas=[DREZEN], ContactUnit=IRABETH,
    AnswerLists=[IRABETH_HUB], ForbidOverrides=dict(HUB_OVERRIDES), **TALK_GATES))
SCENES.append(scene(P + "the_talk_sergeant", "The men have a question", "Commander", 3, "",
    [*talk_nodes("watch", nar, SGT_OPEN, WATCH_SETS, watch_prelude(nar)), *watch_outcomes(nar)],
    requires=(BEGUN, REACHED_CH3), RequiresAnyGroups=[list(IRABETH_GONE)], forbids=(TALK_DONE, RETURNED), delay=72,
    Chapters=[3], Remote=True, Kind="event", last=3, optional=True, Relationship=REL))
SCENES.append(scene(P + "the_summons", "The talk, in writing", "Irabeth", 3, "",
    [*talk_nodes("irabeth", ira_letter, IRA_LETTER_OPEN, IRABETH_SETS, irabeth_letter_prelude(ira_letter)),
     *irabeth_letter_outcomes(ira_letter)],
    requires=(BEGUN, REACHED_CH3), forbids=(TALK_DONE, *IRABETH_GONE, FALLEN), ForbidOverrides=dict(HUB_OVERRIDES), delay=96,
    Chapters=[3, 5], Remote=True, Kind="letter", **TALK_GATES))
SCENES.append(scene(P + "the_summons_watch", "The men's question", "Commander", 3, "",
    [*talk_nodes("watch", nar, WATCH_LETTER_OPEN, WATCH_SETS, watch_letter_prelude(nar)), *watch_letter_outcomes(nar)],
    requires=(BEGUN, REACHED_CH3), RequiresAnyGroups=[list(IRABETH_GONE)], forbids=(TALK_DONE, RETURNED, FALLEN), delay=96,
    Chapters=[3, 5], Remote=True, Kind="event", **TALK_GATES))


# === Section 5.2b: Irabeth after the hanging; the inquiry =============================================================

AFTER_HANGING_TEXT = ('''{n}She is off duty, out of armour, sitting on the edge of the officers' table with a cup she has not drunk from. She doesn't stand when you come in.{/n}
"I keep thinking about that prisoner. I swore to serve the crusade, Commander. I never swore to look away when a prisoner is killed."''')
AFTER_HANGING_CHOICES = (
    c("[Stay and listen.]", "after_stay", flags=(AFTER_SEEN,)),
    c("[Leave her to it.]", flags=(AFTER_SEEN,)))
AFTER_STAY = ('''"I'll tell you why I'm still here. Not because you were right. Because you'll answer for it." {n}She looks up at last.{/n} "Won't you."''')
SCENES.append(scene(P + "irabeth_after_hanging", "Still in the room", "Irabeth", 3, '"Irabeth."', [
    ira("start", AFTER_HANGING_TEXT, *AFTER_HANGING_CHOICES),
    ira("after_stay", AFTER_STAY, c("Continue")),
], requires=(OWNED, TALK_DONE), forbids=(AFTER_SEEN, *IRABETH_GONE, FALLEN), delay=24, Chapters=[3, 5], Areas=[DREZEN],
   ContactUnit=IRABETH, AnswerLists=[IRABETH_HUB], ForbidOverrides=dict(HUB_OVERRIDES), **TALK_GATES))
# The summons-letter fallback (section 5.2b): in Chapter 5 she is away with the Queen and writes instead.
SCENES.append(scene(P + "irabeth_after_hanging_letter", "Still in the room", "Irabeth", 5, "", [
    ira_letter("start", '''{n}Irabeth's letter reaches you in a hand less square than usual.{/n}
"I keep thinking about that prisoner. I swore to serve the crusade. I never swore to look away when a prisoner is killed. I'll tell you why I still serve it beside you. Not because you were right. Because you'll answer for it."
{n}Below it, after a gap, as if added later:{/n} "Won't you."''',
        c("[Keep the letter.]", flags=(AFTER_SEEN,)),
        c("[Burn it.]", flags=(AFTER_SEEN,))),
], requires=(OWNED, TALK_DONE, "irabeth_away"), forbids=(AFTER_SEEN, "irabeth_dead", "irabeth_gone", RETURNED, FALLEN), delay=24,
   Chapters=[5], Remote=True, Kind="letter", **TALK_GATES))

SCENES.append(scene(P + "hanging_account", "In front of her officers", "Irabeth", 3, '"About the prisoner."', [
    ira("start", '''"If you want to answer for it, you'll do it properly." {n}She doesn't soften it.{/n} "In front of my officers."''',
        c("[Submit to the inquiry.]", "inquiry", flags=(ACCOUNT_SEEN,)),
        c('"Not now."', abort=True, flags=(ACCOUNT_SEEN, ACCOUNT_DECLINED))),
    nar("inquiry", '''{n}It takes an hour in the officers' room. Three Eagle Watch lieutenants sit along one side of the table, Irabeth at its head. Your account is written down as you give it, the storeman, the rope, the reason, and then it is read aloud back to you in a clerk's flat voice, so you hear your own words without your tone in them.{/n}
{n}The reprimand is entered under your name. Nobody looks away while it is written.{/n}''',
        c("[Sign it.]", flags=(ACCOUNTED,))),
], requires=(OWNED, AFTER_SEEN), forbids=(ACCOUNTED, ACCOUNT_SEEN, *IRABETH_GONE, FALLEN), Chapters=[3, 5], Areas=[DREZEN],
   ContactUnit=IRABETH, AnswerLists=[IRABETH_HUB], ForbidOverrides=dict(HUB_OVERRIDES), **TALK_GATES))


# === Section 5.4: the enacted consequences ============================================================================

SCENES.append(scene(P + "irabeth_cold", "Watch business", "Irabeth", 3, '"Irabeth, a moment."', [
    ira("start", '''{n}She is briefing her officers when you come in, and she finishes the report to *them* first: the gate rotas, a missing crate of bolts, a drunk sergeant demoted. Only then does she turn.{/n}
"Commander. Watch business: ask, and I'll answer. I won't bring it to you unasked any more. And any unofficial order from you, I'll want a witness."''',
        c('"Understood."', flags=(COLD_SEEN,)),
        c('"You\'re making a point of this in front of them."', "point", flags=(COLD_SEEN,))),
    ira("point", '''"Yes." {n}Her officers find somewhere else to look.{/n} "That's the point."''', c("Continue")),
], requires=(WARY,), forbids=(COLD_SEEN, *IRABETH_GONE, FALLEN), delay=72, Chapters=[3, 5], Areas=[DREZEN], ContactUnit=IRABETH,
   AnswerLists=[IRABETH_HUB], ForbidOverrides=dict(HUB_OVERRIDES), **TALK_GATES))

SCENES.append(scene(P + "the_minder", "A guard on the door", "Commander", 3, "", [
    nar("start", '''{n}When you come back to your quarters there is an Eagle Watch sergeant bedding down across your door, a blanket, a crossbow and a heel of bread. He gets up when he sees you, not quickly.{/n}
"Orders, {mf|sir|ma'am}. Somebody on this door, nights. So nobody gets ideas, either way round." {n}He doesn't say which way round he means.{/n}''',
        c("Continue", "prisoners", requires=(NOTED,)),
        c("[Step over him.]", flags=(MINDER_SEEN,), forbids=(NOTED,)),
        c('"Get a proper blanket, at least."', flags=(MINDER_SEEN,), forbids=(NOTED,))),
    nar("prisoners", '''"...And I'm to witness any order you give about the prisoners. The officers want every word written down." {n}He says it to a point just past your ear.{/n} "That's the whole of it."''',
        c("[Step over him.]", flags=(MINDER_SEEN,)),
        c('"Get a proper blanket, at least."', flags=(MINDER_SEEN,))),
], requires=(MINDER,), forbids=(MINDER_SEEN, FALLEN), delay=48, Chapters=[3, 5], Areas=[DREZEN], Remote=True, Kind="event",
   **TALK_GATES))

STING_OPEN = ('''{n}Word comes at dusk: a contact has bitten. A man who calls himself a dealer in candles wants to meet the Goat's officer in a cellar under a cooper's yard in the lower city, tonight, alone.{/n}
{n}The Watch has the street. How close they stand is up to you.{/n}''')
SCENES.append(scene(P + "the_sting", "Bait", "Commander", 3, "", [
    nar("start", STING_OPEN,
        c('[Bluff] "[Keep the Watch close.]"', check=dict(Skill="CheckBluff", DC=22, Success="close_ok", Failure="close_bad")),
        c('[Bluff] "[Send the Watch back. Make it convincing.]"', check=dict(Skill="CheckBluff", DC=16, Success="back_ok", Failure="back_bad")),
        c("[Don't go.]", "refused_proposed", requires=(VIA_IRABETH,), forbids=(LIED,)),
        c("[Don't go.]", "refused_lied", requires=(VIA_IRABETH, LIED)),
        c("[Don't go.]", "refused_watch", requires=(VIA_WATCH,), forbids=(VIA_IRABETH,))),
    nar("close_ok", '''{n}He is nervous, and he has reason: you can hear the Watch breathing in the dark above the stair. But you play the Goat's officer the way you played it at the pyre, bored and certain, and boredom is the one thing a frightened cultist cannot fake. He gives you a name, a cell, and a password, and the Watch takes him on the stair. Nobody dies. But his lookout saw you go down under the Goat's name, and the lookout is gone before the Watch reaches the street.{/n}''',
        c("Continue", flags=(STING_DONE, EXPOSED))),
    nar("close_bad", '''{n}He smells the Watch before you have finished your first sentence. The candle goes out; a knife comes out of the dark where he was, and finds you under the ribs before the Watch is down the stair. They take him. You walk back up on your own feet, mostly, past the empty doorway where his lookout stood.{/n}''',
        c("Continue", flags=(STING_DONE, EXPOSED, SCAR))),
    nar("back_ok", '''{n}With the Watch two streets off he relaxes, and talks: a name, a cell, a password. You let him go, as agreed. The agent shadowing him out stays too far back to be seen, and too far back to help; at dawn they find the Watch agent in the gutter behind a tannery. The cell is taken by noon.{/n}''',
        c("Continue", flags=(STING_DONE, EXPOSED, AGENT_LOST))),
    nar("back_bad", '''{n}With the Watch two streets off he relaxes, and then he hears something in your voice he doesn't like. The knife finds you under the ribs. By the time you can shout, he is up the stair and away, and the agent who tries to follow him is found in the gutter at dawn.{/n}''',
        c("Continue", flags=(STING_DONE, EXPOSED, SCAR, AGENT_LOST))),
    nar("refused_proposed", '''{n}You don't go. The Watch waits in the cold all night for an officer who never comes down the stair, and the contact goes back to wherever such men go. In the morning Irabeth sends one line:{/n} "You proposed it, Commander."''',
        c("Continue", flags=(STING_REFUSED, WARY))),
    nar("refused_lied", '''{n}You don't go. The Watch waits in the cold all night for an officer who never comes down the stair, and the contact goes back to wherever such men go. In the morning Irabeth sends one line:{/n} "Your ruse, Commander. Your absence."''',
        c("Continue", flags=(STING_REFUSED, WARY))),
    nar("refused_watch", '''{n}You don't go. The Watch waits in the cold all night for an officer who never comes down the stair. By evening there is a sergeant bedding down across your door, and nobody has to tell you why.{/n}''',
        c("Continue", flags=(STING_REFUSED, MINDER))),
], requires=(OWED,), forbids=(STING_DONE, STING_REFUSED, FALLEN), delay=72, Chapters=[3, 5], Areas=[DREZEN], Remote=True,
   Kind="event", **TALK_GATES))


# === Section 6: off the Trickster path, the crusade's own answer ======================================================

SCENES.append(scene(P + "offpath_note", "Ours", "Commander", 3, "", [
    nar("start", '''{n}Someone has nailed a leaflet to the post by the Drezen market well: cheap paper, a soot-black goat's head, and four words in a cultist's careful capitals.{/n}
{n}"{name} IS OURS."{/n}
{n}Under it, in a crusader's hand and a different ink, somebody has written one more:{/n} "liar."''',
        c("[Tear it down.]", flags=(OFFPATH,)),
        c("[Leave it where it is.]", flags=(OFFPATH,))),
], requires=(BEGUN,), forbids=("trickster", "trickster.ever", OFFPATH, FALLEN), delay=1, Chapters=[3, 5], Areas=[DREZEN],
   Remote=True, Kind="event", **TALK_GATES))


# === The Ledger (section 5.4 lines; Last Call, Trickster) ==============================================================

L = lastcall_ledger._line
lastcall_ledger.early(dict(
    Id="early.longcon", Section="Secrets", Portrait="", Title="The Goat's crusader",
    Text="{n}At the Blackwing pyre you told a deserter to carry your name into the Gray Garrison as the Goat's own. He did. "
         "The story has been walking ahead of you ever since.{/n}",
    Lines=[L("{n}Reputation: the Goat's crusader. Never denied.{/n}", requires=[STANDS]),
           L("{n}Irabeth Tirabade stopped trusting your unofficial orders.{/n}", requires=[WARY]),
           L("{n}She told you so to your face, in front of her officers.{/n}", requires=[COLD_SEEN]),
           L("{n}Irabeth knows you hanged a surrendered man. You never answered for it.{/n}", requires=[OWNED], forbids=[ACCOUNTED]),
           L("{n}Irabeth knows you hanged a surrendered man. You answered for it, in front of her officers.{/n}", requires=[OWNED, ACCOUNTED]),
           L("{n}The Eagle Watch posted a guard on your door.{/n}", requires=[MINDER], forbids=[MINDER_SEEN]),
           L("{n}An Eagle Watch sergeant slept across your door. On orders.{/n}", requires=[MINDER_SEEN]),
           L("{n}You still owe the Watch a night as bait in a cellar.{/n}", requires=[OWED], forbids=[STING_DONE, STING_REFUSED]),
           L("{n}You played the Goat's officer in a Drezen cellar for the Watch. Everyone came home.{/n}", requires=[STING_DONE], forbids=[AGENT_LOST]),
           L("{n}You played the Goat's officer in a Drezen cellar for the Watch. You sent their agent too far back. He didn't come home.{/n}", requires=[STING_DONE, AGENT_LOST]),
           L("{n}The lower city knows your face now, as the Goat's.{/n}", requires=[EXPOSED]),
           L("{n}...and you carry the scar from the knife that found you instead.{/n}", requires=[SCAR]),
           L("{n}You never showed up for your own operation. Somebody noticed.{/n}", requires=[STING_REFUSED]),
           L("{n}She believed you.{/n}", requires=[LIED], forbids=[WARY]),
           L("{n}The rumour: never answered for.{/n}", requires=[BEGUN], forbids=[TALK_DONE])],
    Requires=[LEDGER_KEY], Forbids=[], AnyGroups=[], Tooltip="RRT_Secret"))


# --- Path fit (13 directive update 2026-09-29): the Long Con is v1 Trickster-only at its entry (TricksterUnlocked: the
# pre-banner scenes are T in that sense); the crusade's consequences and the off-path note play on every path (N-all,
# doc 15 section 0). No romance content here; nothing is N-fit.
T_SCENES = {P + "tell_them", P + "tell_them_b", P + "prisoner_loud", P + "prisoner_quiet", P + "citadel_offer", P + "big_joke",
            "areelu.early.two_masks", "areelu.early.courtesy_freed", "areelu.early.courtesy_refused"}
PATH_FIT = {s["Id"]: ("T" if s["Id"] in T_SCENES else "N-all") for s in SCENES}
PATH_FIT_V2 = {}

# Section 8 reader lint (doc 15): the longcon.* keys outside these scenes are read only by the route callbacks below.
CALLBACK_READERS = {
    OFFER_HEARD: ("minagho_chivarro.trickster.spared.brand", "minagho_chivarro.trickster.spared.brand_letter"),
    EXPOSED: ("minagho_chivarro.trickster.spared.brand", "minagho_chivarro.trickster.spared.brand_letter"),
    MASK: ("areelu.trickster.rivalry.lens",), SILENT: ("areelu.trickster.rivalry.lens",),
    OFFERED: ("areelu.trickster.rivalry.lens",),
}


def integrate(payload):
    """Register the framework relationship and its Derived Ledger key. World keys bind in trickster_world."""
    payload["Relationships"][REL] = dict(RELATIONSHIP)
    for key, groups in DERIVED.items():
        payload.setdefault("Derived", {})[key] = [list(g) for g in groups]
