"""Nocticula on the Trickster path: only your shadow, and her brother's voice (Writer/handoffs/trickster/nocticula.md,
families F11 and F01).

Canon: at the Trickster Council the Commander either sides with the Council against her (Council_5-2/Answer_0044
1f7b1dee) or, having pranked her three times (NoctaFooled 9b2af5f3), watches her walk into the war council "drowned out by
the laughter" (Cue_0050 b7c8150d). Both start FightAgaintsNoctaCouncilAllied ed5d1dfa, which starts NocticulaDead e581f609.
She is not dead: at Threshold she speaks through a projection (Threshold_NocticulaSpawn ProjectionBuff c057f62e), the
Commander may ask "Are you afraid I'm going to kill you again?" (Answer_0054 f7cc6463), and her epilogue says she
"disappeared into the shadows and lay low" (Epilogues/Cue_2 bc753cb0). At the Chapter 5 audience she sniffs the air and asks
"Is that you, brother?" (Nocticula/Cue_0001 a12f4858, Cue_0002 11421146), because the Commander came through Socothbenoth's
closet: "This closet will take you and your companions straight to my sister's boudoir... my spells will keep you
hidden" (SocothBriefing/Cue_0012 e5a9d6bb; the closet doctrine is Cue_0011 2f4be0bd), and she knows his enchantments by
their "sickly sweet smell" (Nocticula/Cue_0016 bb552fe4). Authored, and labelled as authored: the shadow that leaves the place where she
fell and slides out under the Council's door; the Commander answering her in her brother's voice; the price she names for
the secret (one unnamed favour, the chair at the Commander's right hand); the projection that can touch.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
DEBRIEF_LIST = "aff2802d5af0f77408793b489334befc"    # c5/Mythic_Trickster/Debrief_Council/AnswersList_0006
DEBRIEF_RETURN = "adf1456e429a3d94693417ef7d090d5e"  # Cue_0005 (Cobblehoof: "Phr!") -> list 0006
SOCOTHBENOTH = "dcd200c627536c449bc8258eada65c9f"    # Units/.../MythicTrickster_Ch3/Socothbenoth (speaks Debrief Cue_0013)
THRESHOLD = "765173e2a9e535e4cb66f0ec767c13af"       # c6/FirstFloor/NocticulaThreshold/AnswersList_0003
T_GREETING = "7d07492b12cf5bd4bb1c88113d5831ab"      # Cue_0002 "You do not disappoint, my chosen..."
T_BLESSING = "90cfcb7b1c0bacc43b27043074f21301"      # Cue_0008 "...bless her knight before the final battle?"
T_DOING_WELL = "c10ef2b50ade65f42bbaa0cdfa61b7f9"    # Cue_0010 "Why? You are doing perfectly well on your own."
T_WHATEVER = "3cc60e02e5176f448a57b342ec52ae31"      # Cue_0046 "Sure. Whatever makes you feel better about yourself."
T_GAME = "77216dc2c3770794f93b010659f4aa64"          # Cue_0056 "Is this a game to you? You've spent too much time..."
AUDIENCE_OPEN = "6a5c262473dfe824886bed3eb3eef59d"   # c5/Mythic_Trickster/Nocticula/AnswersList_0003
AUDIENCE_TRICKERY = "114211469c9ffd149a73f1c853b2776f"  # Cue_0002 "What is this trickery?... If it's you, brother..."
AUDIENCE_YOU = "20451daada07f744b9d7f3e14a37a864"    # Cue_0006 "You? But I could've sworn... Hmph! No matter."
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"      # CompanionDialogues/Daeran/AnswersList_0003
NENIO_HUB = "1ab909cc3a6194840b1475b99547c263"       # CompanionDialogues/Nenio/AnswersList_0015

DEAD = "noct.dead"
FIGHT = "noct.acq.council_fight"
ALIVE = "noct.defeated_not_dead"
PRIMED_SHADOW = "nocticula.trickster.primed_shadow"
PRIMED = "nocticula.trickster.primed"
RETURNED = "nocticula.trickster.returned"
DECLINED = "nocticula.trickster.declined"
SAID_YES = "nocticula.trickster.said_yes"
SECRET = "nocticula.trickster.cost.shade_secret"
PAID = "nocticula.trickster.cost.shade_paid"
REFUSED = "nocticula.trickster.cost.shade_refused"
LATE = "nocticula.trickster.cost.late"
IMPERSONATED = "nocticula.trickster.impersonated"
KEPT = "nocticula.trickster.cost.impersonation_kept"
MOCKED = "nocticula.trickster.cost.mocked"

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={DEAD: ALIVE},
    TricksterAccess={DEAD: dict(detect=[DEAD, FIGHT], device="nocticula.trickster.defeated.shadow", returned=RETURNED)})
# Ledger row 11: doc 04 and the Last Call stalemate read the round-1 name of the S2 leash.
DERIVED = {"nocticula.trickster.cost.forgery_kept": [[KEPT]]}


def nt(id, text, *choices, **kw):
    return n(id, "Nocticula", text, *choices, portrait="Nocticula", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Nocticula", **kw)


def threshold(id, title, entry, nodes, requires, forbids, return_cue, **extra):
    SCENES.append(scene(id, title, "Nocticula", 6, entry, nodes, requires=requires, forbids=forbids, last=6,
                        optional=True, Relationship="nocticula", Chapters=[6], AnswerLists=[THRESHOLD],
                        NativeReturnCue=return_cue, **extra))


# --- S1, defeated at the Council: only your shadow (F11) ---------------------------------------------------------

# The clue (R2-2 primer), inline on Socothbenoth's own debrief list, before the Threshold it answers.
SCENES.append(scene("nocticula.trickster.defeated.debrief_clue", "The floor", "Nocticula", 5,
    "[Look at the place where Nocticula fell.]", [
    nar("floor", '''{n}The place where the Lady in Shadow fell is still dark. Not stained: dark, as if the torchlight declined to touch it.{/n}
{n}While the Council raise their cups, the darkness gathers itself into the outline of a woman lying down. It rises, a pace away from where she lay, as though it had stepped aside to watch. It considers the room. Then it slides, very politely, under the door.{/n}
{n}Nobody else is looking at the floor.{/n}''',
        c("Continue", "socoth")),
    n("socoth", "Socothbenoth", '''"Commander! Stop staring at the floor. Nobody who stares at floors has ever been any fun." {n}The Silken Sin drapes an arm across your shoulders and puts a cup in your hand.{/n} "Drink! We won. My dear sister is a stain on the carpet, and the carpet is not even mine."''',
        c("[Keep it to yourself.]", flags=(PRIMED_SHADOW,)),
        c('[Look away and join the toast] "To the carpet."', abort=True),
        portrait="Nocticula", speaker_unit=SOCOTHBENOTH),
], requires=("trickster", DEAD, FIGHT), forbids=(PRIMED_SHADOW, "noct.threshold_met"), last=5, optional=True,
   Relationship="nocticula", Chapters=[5], AnswerLists=[DEBRIEF_LIST], NativeReturnCue=DEBRIEF_RETURN,
   TricksterDevice=True, TricksterState=DEAD))

JOKE = '[Play a prank on the Queen of Shadows] "Kill you? I wouldn\'t dream of it. I killed your shadow. Mind you don\'t trip over it."'
SHADOW_CHOICES = (c(JOKE, mythic="Trickster", flags=(PRIMED, SECRET, "noct.started")),
                  c("[Say nothing.]", abort=True))

threshold("nocticula.trickster.defeated.shadow", "Only your shadow", '"Still hiding behind a projection, Lady?"', [
    nar("start", '''{n}The projection flickers, the way a candle does when a door opens somewhere it should not. Behind her the fires of Threshold burn steadily, and throw no shadow of her at all.{/n}''',
        c("Continue", "seen", requires=(PRIMED_SHADOW,)),
        c("Continue", "dress", requires=("noct.fooled",), forbids=(PRIMED_SHADOW,)),
        c("Continue", "voice", requires=(MOCKED,), forbids=(PRIMED_SHADOW, "noct.fooled")),
        c("Continue", "base", forbids=(PRIMED_SHADOW, "noct.fooled", MOCKED))),
    nt("seen", '''"Hiding? From you?" {n}Her smile is slow and entirely without warmth.{/n} "You looked at the floor while my brother was drinking. I saw you look. You killed me in front of his clowns, and then you watched the floor, as if you were waiting for it to do something."
"Say what you saw, clown. Say it now, so I can decide what it costs you."''', *SHADOW_CHOICES),
    nt("dress", '''"Hiding?" {n}The projection is dressed properly this time, in black that drinks the torchlight.{/n} "The last time you saw me, I walked into a war council wearing whatever your pranks had left me, and the clowns laughed until they had to be carried out. Then you killed me while they were still laughing."
"Say the joke you have been saving since. Say it now, so I can decide what it costs you."''', *SHADOW_CHOICES),
    nt("voice", '''"Hiding? Coming from you, that is almost a compliment." {n}She tilts her head, as if listening for a second voice under yours.{/n} "You wore my brother's voice into my palace. Now you wear his jokes, and you killed me with his friends watching."
"Say this one, then. Say it now, so I can decide what it costs you."''', *SHADOW_CHOICES),
    nt("base", '''"Hiding? I am standing in front of you, mortal. You simply cannot reach me." {n}She notices you noticing the fires, and the floor behind her. She lets you.{/n} "You killed me in front of my brother's clowns. I have not forgotten the sound they made."
"Whatever joke you have been saving since the Council, say it now, so I can decide what it costs you."''', *SHADOW_CHOICES),
], ("trickster", DEAD, FIGHT), (PRIMED,), T_GAME, TricksterDevice=True, TricksterState=DEAD)

# The late fallback (R2-2): the act happens now, on the page, and the terms are worse.
SCENES.append(scene("nocticula.trickster.defeated.late_shadow", "One shadow too many", "Nocticula", 6, "", [
    nar("wall", '''{n}Past midnight the campfire throws one shadow too many against the wall of your tent. It belongs to nobody in the camp. It is slender, and very still, and it is waiting to see whether you have noticed.{/n}
{n}Somewhere beyond the camp the Wound mutters in its sleep. Tomorrow you go down to meet Areelu.{/n}''',
        c('[Step on the stray shadow] "There you are. I told them I only killed your shadow. Nobody believed me either."',
          "foot", mythic="Trickster"),
        c("[Let it go.]", abort=True)),
    nt("foot", '''{n}The shadow does not move. Your boot does not move either: it cannot. It is standing on something, and the something is laughing, very quietly, from a great way down.{/n}
"Late. And on my foot."
"You had your chance at Threshold, while I was still pretending to be a ghost for my brother's benefit. You spent it on the scenery. Now you pin a queen to your tent wall like a moth, as if that were the same thing." {n}The laughter stops.{/n} "You will pay for both. You will pay more than you would have at the door."''',
        c("[Take your foot off her.]", flags=(PRIMED, SECRET, "noct.started", LATE))),
], requires=("trickster", DEAD, FIGHT, "noct.threshold_met"), forbids=(PRIMED,), last=6, optional=True,
   Relationship="nocticula", Remote=True, Chapters=[6], TricksterDevice=True, TricksterState=DEAD))

AGREED = '"Agreed."'
threshold("nocticula.trickster.defeated.call_in", "The price of a shadow", '"You didn\'t say I was wrong."', [
    nt("price", '''"No. I said you had spent too much time with my brother. A clown who knows where my shadow ends and I begin is a clown I have to price."
"Think what my death is worth. I am told the Abyss is in mourning; I intend to believe it. My rivals will have stopped counting my armies by now, and my dear brother, I hope, has stopped sending me perfume. Every one of them believes I am gone, and while they believe it I am free to do as I please. That silence is worth more than your crusade, and you are carrying it around in your mouth."
{n}She smiles. It does not reach the projection's eyes, because the projection has none.{/n}
"So. What will you take to keep it there?"''',
        c('"Name your price, then."', "terms", forbids=(LATE,)),
        c('"Name your price, then."', "terms_late", requires=(LATE,)),
        c('"Nothing. You keep my secrets, I keep yours."', native_next=T_WHATEVER, flags=(RETURNED, REFUSED)),
        c("[Leave it for later.]", abort=True)),
    nt("terms", '''"One favour. Unnamed. When I ask, you will grant it, and you will not ask what it is for."
{n}The fires lean toward her, very slightly, as if listening.{/n} "Do not look so worried. I have never yet asked anyone for anything they could not afford. I simply ask for it at the worst possible time."''',
        c(AGREED, native_next=T_BLESSING, alignment=("Evil", 1), flags=(RETURNED, PAID))),
    nt("terms_late", '''"One favour. Unnamed. And because you came to me late, and on my foot, you will grant it before you have heard it, and you will smile while you do."
{n}She waits, openly enjoying the wait.{/n} "Smile, Commander. You are already practising."''',
        c(AGREED, native_next=T_BLESSING, alignment=("Evil", 2), flags=(RETURNED, PAID))),
], ("trickster.ever", PRIMED), (RETURNED,), T_GAME, TricksterDevice=True, TricksterState=DEAD)

# The commit (R2-1), a separate beat after the return: her test, her yes or her no, and the heat to the cut.
WHY = (c("Continue", "why_late", requires=(LATE,)),
       c("Continue", "why_floor", requires=(PRIMED_SHADOW,), forbids=(LATE,)),
       c("Continue", "why_dress", requires=("noct.fooled",), forbids=(LATE, PRIMED_SHADOW)),
       c("Continue", "why_voice", requires=(MOCKED,), forbids=(LATE, PRIMED_SHADOW, "noct.fooled")),
       c("Continue", "why_base", forbids=(LATE, PRIMED_SHADOW, "noct.fooled", MOCKED)))
VERDICT = (c('"Then say yes."', "reason_paid", requires=(PAID,), flags=("noct.complete", SAID_YES)),
           c('"Then say yes."', "reason_refused", forbids=(PAID,), flags=("noct.complete", SAID_YES)),
           c('"Or keep your answer. You like owning things."', "refusal"))
threshold("nocticula.trickster.defeated.chair", "Beside me", '"One more question, Lady. Off the record."', [
    nt("test", '''"Nothing in the Abyss is off the record. The Abyss simply has very poor clerks."
"Very well. You have kept my secret for the length of one conversation, which is longer than my brother ever managed. Tell me why I should let a clown who knows where my shadow ends sit anywhere near me when this is over."
{n}The projection leans closer. Its breath is cold, and smells of night-blooming flowers.{/n} "Choose your answer well. I will know if it is one of his."''',
        c('"Because I\'m the only one who\'ll never ask you for anything real."', "verdict_true"),
        c('[Joke] "Because you laughed. Under the projection. I heard it."', "verdict_joke")),
    nt("verdict_true", '''"Liar." {n}She tastes the word, and seems to like it.{/n} "You will ask me for everything, clown, and I will enjoy refusing most of it. Slowly. In front of people."''', *VERDICT),
    nt("verdict_joke", '''"I did not laugh."
{n}The projection's mouth has not moved. Somewhere far below, something does, and the floor of Threshold goes on remembering it afterwards, the way a bell remembers being struck.{/n}''', *VERDICT),
    nt("reason_paid", '''{n}She considers you the way she considered her price: from the end backwards.{/n}
"You agreed to a favour you cannot see the bottom of, and you did not haggle. I have had kings refuse me less, and devils read the terms twice."''',
        *WHY),
    nt("reason_refused", '''{n}She considers you the way she considered her price: from the end backwards.{/n}
"You refused my price to my face, and you are still standing in my light. Nobody has done that since my brother, and he had to be my brother to survive it."''',
        *WHY),
    # What she actually saw of this Commander, by the road taken (Sol BEL: never a clue the player did not witness).
    nt("why_late", '''"You missed me at the door, clown. You walked past my projection and talked about the scenery. And then, the night before the Wound, you found me anyway: one shadow among a camp full of them, on your own tent wall, and you put your boot on the right one." {n}Her mouth curves.{/n} "I have been wondering since what else you notice when you are not trying."''',
        c("Continue", "yes")),
    nt("why_floor", '''"You killed me, clown, and then you looked at the floor while my brother was drinking. Nobody looks at the floor. I have been wondering since what else you notice."''',
        c("Continue", "yes")),
    nt("why_dress", '''"You made me walk into a war council in what your pranks had left me, with my brother's clowns braying, and you killed me before the braying stopped. Nobody has humiliated me that thoroughly in an age. Nobody has ever done it and then stood in front of what was left, asking to be let closer." {n}She savours it.{/n} "I want to see what else you will dare."''',
        c("Continue", "yes")),
    nt("why_voice", '''"You walked into my palace in my brother's voice and walked out with my secret, and then you killed me with his friends watching and never once spent it. A clown who can hold a secret that expensive through a murder." {n}Her eyes narrow, pleased.{/n} "I have been wondering since what else you are holding."''',
        c("Continue", "yes")),
    nt("why_base", '''"You killed me in front of my brother's clowns, and you did not gloat; you went back to your war as if a demon lord were one more chore. Then you came to Threshold and, of everything a mortal could say to a queen's ghost, you told me you had killed my shadow." {n}The projection tilts its head.{/n} "The only true thing anyone has said to me since the Council, and you said it as a joke. I have been wondering since what else you know."''',
        c("Continue", "yes")),
    nt("yes", '''"Yes." {n}No hesitation at all; she has decided long before you asked, and was only waiting to see whether you would.{/n} "Beside me. Not at my feet. Where I can see your hands."
"And since we are being honest, clown, there is one thing a projection does better than a body. It cannot be touched." {n}Her eyes glitter.{/n} "It can touch."''',
        c("Continue", "threshold")),
    nar("threshold", '''{n}The dark around her widens and closes over the two of you like a drawn curtain. Beyond it Threshold goes on, muffled, as though in another room.{/n}
{n}Her fingers find the buckles of your armour before you feel them move: cold at first, then not cold at all. She strips you the way she prices things, piece by piece, watching your face to learn what each piece costs you. You reach for her and close your hands on nothing; she laughs against your throat. "Hands where I can see them. I said so."{/n}
{n}So you keep them where she can see them. She pushes you back onto a throne that was not there a moment ago, settles astride your hips with a weight that is very real indeed, and leans down until her hair falls around you both like a second darkness.{/n}
"I have wanted to do this since the Council," she murmurs against your mouth, amused at herself for saying it. "I want you undone, and I want to watch every step of it, and I want you to remember whose shadow did it." {n}The last fire in Threshold gutters and goes out.{/n}''',
        c('"...Flawless."')),
    nt("refusal", '''"Then no." {n}She is pleased with herself; she has been waiting all evening for someone to offer her the chance.{/n} "Not tonight. Ask me again when Areelu is dead and you are not. If you are dead, I will have had my answer, and I will not have had to give one."''',
        c("[Let her keep her answer.]", flags=(DECLINED,))),
], ("trickster.ever", RETURNED), ("noct.complete", "noct.closed", DECLINED), T_GREETING)

# The morning after the chair, delivered at the next rest before the descent.
SCENES.append(scene("nocticula.trickster.defeated.morning", "Four crescents", "Nocticula", 6, "", [
    nar("start", '''{n}You wake before the camp does, with the taste of night-blooming flowers in your mouth and four small crescents on your shoulder, where a projection's nails had no business reaching.{/n}
{n}On the camp table, in the dust on your maps of the rift, someone has drawn a chair at the right hand of your own. Beneath it, in a hand you have never seen and know at once: "Where I can see you."{/n}
{n}Your companions are carefully not looking at your shoulder. Outside, the Wound is waiting.{/n}''',
        # Save-safe: every choice keeps its slot (choice 0 unchanged); a paid price reads the favour under the chair.
        c("[Buckle your armour over the marks.]", forbids=(PAID,)),
        c("[Read the rest of the dust.]", "note_paid", requires=(PAID,), forbids=("daeran.dead", "daeran.kicked_out")),
        c("[Read the rest of the dust.]", "note_paid_alone", requires=(PAID, "daeran.dead")),
        c("[Read the rest of the dust.]", "note_paid_alone", requires=(PAID, "daeran.kicked_out"), forbids=("daeran.dead",))),
    nar("note_paid", '''{n}Under it, smaller, as an afterthought that is not one: "The favour stands. I have not decided on it. I am enjoying not deciding."{/n}''',
        c("[Buckle your armour over the marks.]", "daeran")),
    nar("note_paid_alone", '''{n}Under it, smaller, as an afterthought that is not one: "The favour stands. I have not decided on it. I am enjoying not deciding."{/n}''',
        c("[Buckle your armour over the marks.]")),
    nar("daeran", '''{n}Daeran reads the dust over your shoulder before you can wipe it. "An unnamed favour. To her." He sets his cup down very carefully.{/n}
"Commander, I have signed some truly ruinous contracts in my life, and every one of them had a number in it."''',
        c("[Wipe the table.]")),
], requires=("trickster.ever", SAID_YES), last=6, optional=True, Relationship="nocticula", Remote=True, Chapters=[6]))


# --- S2, in her palace, unannounced: her brother's voice (F01) ------------------------------------------------------

SCENES.append(scene("nocticula.trickster.palace.brothers_voice", "Is that you, brother?",  "Nocticula", 5,
    '[Answer in Socothbenoth\'s voice] "Sister, darling. You smelled me coming."', [
    nt("sniff", '''{n}Nocticula goes perfectly still. Then she smiles, the way a cat does when the mouse finally speaks.{/n}
"Brother. You came yourself, through my own closets. How very brave, and how very stupid."
"Step out of the shadows, so I can see which of your faces you are wearing today. I should like to know which one to keep."''',
        c('[Keep the voice] "The pretty one, sister. The one you never could resist."', "unmasked"),
        c("[Drop the voice.]", abort=True)),
    nt("unmasked", '''{n}She sniffs again, longer, and her lip curls.{/n}
"No. His scent, but not his sweat. He sweats sugar. You sweat iron."
{n}Something in the Lady in Shadow's face files you away, very precisely, under a heading you will not enjoy.{/n}
"You came through his closet wrapped in his spells, reeking of his sugar, and I called you by his name. That is a secret now, clown, and I keep my secrets the way I keep my pets: fed, and on a short chain." {n}Her voice drops to a purr.{/n} "If anyone ever hears of it, I will know which mouth it came out of. Will they?"''',
        c('"Nobody will hear it from me."', native_next=AUDIENCE_YOU, flags=(IMPERSONATED, KEPT)),
        c("[Laugh in his voice one more time.]", "bookmark")),
    nt("bookmark", '''{n}The room goes very cold, all at once, and the lamps lean away from her.{/n}
"Laugh again in that voice and I will have your tongue bound into a bookmark for his letters. I keep them, you know. All of them. Unopened."
"Now. You will answer my questions in your own voice, and you will be very grateful that I am curious."''',
        c("[Drop the voice.]", native_next=AUDIENCE_YOU, alignment=("Chaotic", 1), flags=(IMPERSONATED, KEPT, MOCKED))),
], requires=("trickster", "closets.known", "noct.acq.audience_started"),
   forbids=("noct.acq.audience_question", IMPERSONATED, DEAD), last=5, optional=True,
   Relationship="nocticula.acquisition", Chapters=[5], AnswerLists=[AUDIENCE_OPEN], NativeReturnCue=AUDIENCE_TRICKERY,
   EntryMythic="PlayerIsTrickster"))


# --- Epilogue pages (S1). Ordered siblings; no page sets a flag or requires another page's id -----------------------

# MinChapter 1, like the other routes' pages: the ending sequence alone decides when a page plays.
ALIVE_AFTER = "trickster.commander_back"   # native Trickster survival or Last Call's bottle (sacrifice is overridden by it)


def page(id, title, text, requires, forbids=(), paragraphs=(), nodes=None, living=False):
    """living=True: the page promises a future with the Commander, so it Forbids sacrifice unless the Commander came back."""
    body = nodes or [nar("end", text, paragraphs=paragraphs)]
    extra = dict(ForbidOverrides={"sacrifice": ALIVE_AFTER}) if living else {}
    SCENES.append(scene(id, title, "Epilogue", 1, "", body, requires=requires,
                        forbids=tuple(forbids) + (("sacrifice",) if living else ()), last=99,
                        Relationship="nocticula", **extra))


page("nocticula.trickster.defeated.epilogue", "A queen does not come back",
    '''{n}What the Abyss buried after the Council was a shadow. Nocticula let Alushinyrra wear black, let every lord of the Abyss believe the Midnight Isles were ripe, and walked out of her own funeral into a quiet she had never been allowed before.{/n}
{n}When the Commander asked her, years later, whether she had ever meant to come back, she said a queen does not come back. She simply stops pretending to be gone.{/n}''',
    ("trickster.ever", RETURNED), living=True, paragraphs=(
        p("She kept the promise she had made at Threshold, and kept it the way she kept everything: jealously, "
          "expensively, and with the lamps lit. At every table the Commander sat at afterwards, the chair at the right "
          "hand was hers, and she was always in it before anyone else arrived.", requires=(SAID_YES,)),))
page("nocticula.trickster.defeated.epilogue.fooled", "The dress",
    '''{n}She never wore the dress from the Council again. She kept it, folded, in the one chest in her palace that has no key.{/n}''',
    ("trickster.ever", RETURNED, "noct.fooled"))
page("nocticula.trickster.defeated.epilogue.punchline", "The most fashionable thing",
    '''{n}The Commander, too, was said to be dead. The two of them agreed it was the most fashionable thing either of them had ever done, and that only one of them had done it properly.{/n}''',
    ("trickster.ever", RETURNED, "trickster.cheated_death"))
page("nocticula.trickster.defeated.epilogue.favour", "The favour",
    '''{n}The Queen of Shadows named her favour in the second spring after Threshold, in a sealed note that smelled of night-blooming flowers. Not a temple, not a war, not a soul. A chair.{/n}
{n}The chair at the Commander's right hand, at every table the Commander would ever sit at, and nobody was to ask whose. Nobody did. The Commander paid it for the rest of a long life, and was never once sure which of them was being watched.{/n}''',
    ("trickster.ever", PAID), living=True)   # Last Call (doc 04): add Forbids lastcall.active when the finale lands (backlog).
page("nocticula.trickster.defeated.epilogue.stalemate", "Places set",
    '''{n}Twice, agents of the Lady in Shadow were found in the Commander's household: a cook who could not cook, a steward who counted the wrong things. Twice, the Commander sent them home with a joke pinned to their sleeves.{/n}
{n}They stayed on anyway, a third and a fourth and a fifth, and after a while the household simply set places for them.{/n}''',
    ("trickster.ever", REFUSED), living=True)
page("nocticula.trickster.defeated.epilogue.unpriced", "An answer owed",
    '''{n}The Commander left Threshold without hearing her price. Nocticula did not send it after. She let it be known in Alushinyrra that the Crusade's Commander owed her an answer, and let the city decide what that meant; the city decided for her, generously, for years.{/n}''',
    ("trickster.ever", PRIMED), forbids=(RETURNED,), living=True)
page("nocticula.trickster.defeated.epilogue.unanswered", "What went down with the Commander",
    '''{n}The Commander went down into the Wound carrying the one secret in the Abyss the Lady in Shadow could not afford loose, and did not come back up with it. The Abyss went on believing her dead. She let it.{/n}
{n}For a year she kept the chair at her right hand empty at every table she sat at, and had anyone who asked whose it was put out of the Midnight Isles. Then she had the chair burned, and went back to being a rumour. It was the only debt she ever let go uncollected, and she never forgave the Wound for collecting it first.{/n}''',
    ("trickster.ever", PRIMED, "sacrifice"), forbids=(ALIVE_AFTER,))
page("nocticula.trickster.defeated.epilogue.unjoked", "Among the many",
    '''{n}After her defeat at the Council, the Lady in Shadow lay low. The Commander was among the many who believed she was dead, and among the few she let go on believing it. It is the only kindness anyone has ever been able to prove against her.{/n}''',
    ("trickster.ever", DEAD, FIGHT), forbids=(PRIMED,))

# R2-6: the late commit, for a Commander who had her price and never asked the question.
OFFER_PAGE = (c("Continue", "yes_page"),)
WHY_LATE_PAGE = (c("Continue", "m_late", requires=(LATE,)),
                 c("Continue", "m_floor", requires=(PRIMED_SHADOW,), forbids=(LATE,)),
                 c("Continue", "m_dress", requires=("noct.fooled",), forbids=(LATE, PRIMED_SHADOW)),
                 c("Continue", "m_voice", requires=(MOCKED,), forbids=(LATE, PRIMED_SHADOW, "noct.fooled")),
                 c("Continue", "m_base", forbids=(LATE, PRIMED_SHADOW, "noct.fooled", MOCKED)))
page("nocticula.trickster.epilogue.commit", "The chair nobody else sat in", "", ("trickster.ever", RETURNED),
    forbids=("noct.complete", "noct.closed", DECLINED), living=True, nodes=[
    # Sol BEL: her test and her road-specific reason come first; the Commander may refuse on every branch. The two opening
    # choices of the first build are retired by gating (never selectable on a page that requires RETURNED).
    nar("offer", '''{n}The Commander never asked the question at Threshold. Nocticula asked her own instead, the first night the Commander slept in Alushinyrra after the war, from the chair nobody else was allowed to sit in.{/n}
"Tell me why I should let a clown who knows where my shadow ends sit anywhere near me." {n}She did not wait for an answer. She had had a year to decide what it was.{/n}''',
        c("[Cross the room to her chair.]", "crossed", forbids=(RETURNED,)),
        c("[Make her say it twice.] \"I didn't hear you.\"", "twice", forbids=(RETURNED,)),
        *WHY_LATE_PAGE),
    nt("m_late", '''"You missed me at the door, and then you found me anyway, one shadow on a tent wall in a camp full of them, and put your boot on the right one. I have been wondering since what else you notice."''', *OFFER_PAGE),
    nt("m_floor", '''"You looked at the floor while my brother was drinking. Nobody looks at the floor. I have been wondering since what else you notice."''', *OFFER_PAGE),
    nt("m_dress", '''"You made me walk into a war council in what your pranks had left me, and you never once apologised. I have been waiting an age for someone that rude."''', *OFFER_PAGE),
    nt("m_voice", '''"You carried my secret through my murder in my brother's voice and never spent it. I want to see what else you can carry."''', *OFFER_PAGE),
    nt("m_base", '''"You told a queen's ghost you had killed her shadow. It was the only true thing anyone said to me that year, and you said it as a joke."''', *OFFER_PAGE),
    nt("yes_page", '''"So. Yes. Beside me, where I can see your hands. Do not make me say it twice. I will deny it."''',
        c("[Cross the room to her chair.]", "crossed"),
        c("[Make her say it twice.] \"I didn't hear you.\"", "twice"),
        c("[Leave the chair beside her empty.]", "refused_page")),
    nar("refused_page", '''{n}The Commander did not cross the room. Nocticula watched the refusal arrive, all the way to the door, and laughed, low, the way she laughed at a card played well against her.{/n}
"Then keep your hands where I cannot see them," she said. "I shall find out what they do anyway." The chair beside hers stayed empty for the rest of the Commander's life, and nobody else was ever allowed to sit in it.{/n}''', c()),
    nar("crossed", '''{n}She did not rise. She let the Commander come to her, all the way across a room built to make petitioners feel the distance, and watched every step of it the way she watched the Abyss: as something that would one day belong to her.{/n}
{n}At the chair she laid one fingertip on the Commander's breastbone and held it there, not pressing, her mouth a breath away. "Kneel, or kiss me. Choose quickly. I bore easily."{/n}''',
        c("[Kiss her.]", "kissed"),
        c("[Kneel.]", "knelt"),
        c("[Step back from the chair.]", "refused_page")),
    nar("kissed", '''{n}Her mouth was warm, which the Commander had not expected; the projection at Threshold had been cold. She pulled the Commander down into the chair and rose over them, astride, one hand flat on the Commander's chest to keep them exactly where she wanted them, and the lamps of her palace went out one by one, in no hurry at all.{/n}''', c()),
    nar("knelt", '''{n}"Better," said the Queen of Shadows, and let her robe fall open over the Commander's head like a tent. Her fingers closed in the Commander's hair, holding them exactly where she wanted them, and the lamps of her palace went out one by one, in no hurry at all.{/n}''', c()),
    nar("twice", '''{n}"You heard me," said the Lady in Shadow, and the lamps in the room dimmed, and a great many things in Alushinyrra shivered for no reason anyone could name.{/n}
{n}Then, very softly, so that nobody in her city would ever be able to swear to it: "Yes." She rose from the chair, took the Commander's wrists in her cool hands and set them on her hips. "There. Where I can see them. Now walk me to the bed, or go back to your inn and dream about it."{/n}''',
        c("[Walk her to the bed.]", "walked"),
        c("[Go back to the inn.]", "inn")),
    nar("walked", '''{n}The Commander walked her backwards, step by step, while she watched. At the bed she turned them both, pushed, and followed the Commander down, and settled astride, and the last lamp went out while she was still smiling.{/n}''', c()),
    nar("inn", '''{n}The Commander went back to the inn, and slept, and dreamed of nothing in particular. She kept her word to the letter: the Queen of Shadows did not set one foot in that dream, and made sure the Commander noticed the absence. At breakfast a note waited beside the bread, in a hand the Commander had never seen and knew at once: "Twice. Do not get used to it."{/n}''', c()),
])
page("nocticula.trickster.epilogue.declined", "Eleven years",
    '''{n}At Threshold she had told the Commander to ask again when Areelu was dead and the Commander was not. The Commander asked. She kept the Commander waiting eleven years for the answer, which was yes, and then pretended there had never been a question.{/n}''',
    ("trickster.ever", DECLINED), forbids=("noct.complete",), living=True)


# --- Reactions (05 section 3.1: exactly Daeran and Nenio) -----------------------------------------------------------

NENIO_BACK = "nenio.trickster.returned"   # Nenio's own Trickster return (nenio_trickster): G6(b) overrides only

REACTIONS = [
    reaction("Daeran", "nocticula.trickster.reaction.daeran", (IMPERSONATED,),
             '''{n}Daeran is laughing before you have finished the story. He has to set his glass down.{/n}
"I once told you Lady Nocticula seemed a bearable enough mistress. I withdraw it. She let you into her private rooms wearing her brother's scent, called you by his name, and you are still breathing. She is an extraordinary mistress."
"Tell me the truth, Commander. Did she blush? No, don't. I prefer to imagine it."''',
             answer_list=DAERAN_HUB, forbids=("daeran.dead", "daeran.kicked_out"), chapter=5, last=5,
             entry='"I visited Nocticula\'s palace."'),
    reaction("Nenio", "nocticula.trickster.reaction.nenio", (ALIVE, SECRET),
             '''{n}Nenio's ears are fully upright. She has a folio open on her knees and is writing in it very fast.{/n}
"A demon lord who is dead and not dead at the same time! A shadow that walks off on its own! I keep a folio of impossible states. She goes on page one, above the cat."
{n}She looks up, pen poised.{/n} "May I measure your shadow too? For a control. Stand still. Stand still! It moved."''',
             answer_list=NENIO_HUB,
             forbids=("nenio.dead", "nenio.killed_by_commander", "nenio.sent_away", "nenio.kicked_out", "nenio.dissolved"),
             ForbidOverrides={"nenio.dead": NENIO_BACK, "nenio.killed_by_commander": NENIO_BACK,
                              "nenio.sent_away": NENIO_BACK, "nenio.kicked_out": NENIO_BACK},
             chapter=6, last=6, entry='"About Nocticula\'s shadow..."'),
]
SCENES.extend(REACTIONS)


# --- The registered routes --------------------------------------------------------------------------------------

EVIDENCE_ANY = ["noct.acq.council_disclosed", "noct.acq.shamira_permission", "noct.acq.shamira_reported", "noct.acq.amused"]
DROPPED_EVIDENCE = ("noct.acq.council_disclosed", "noct.socoth_plan_exposed")
# Harbor endings a chair commit would otherwise reach: they narrate the harbor undertaking she never had with this Commander.
HARBOR_ONLY_ENDINGS = ("noct.ending_sacrifice", "noct.ending_ascent", "noct.ending_changed")
SCENT_LINE = '''"You describe it very prettily. You described my brother prettily too, in my own rooms, with his scent all over you."
{n}The mark on the wax does not move. Her voice does, closer.{/n} "I have not decided to find that funny. I am told I will."'''


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Nocticula Trickster integration missing scene: " + id)
    return by_id[id]


def _node(scene_, id):
    return next(x for x in scene_["Nodes"] if x["Id"] == id)


def _gate(choice, forbids=(), requires=()):
    choice["Forbids"] = [*choice["Forbids"], *[f for f in forbids if f not in choice["Forbids"]]]
    choice["Requires"] = [*choice["Requires"], *[r for r in requires if r not in choice["Requires"]]]


def integrate(payload):
    """Save-safe edits to the registered routes: no id, node or choice is renamed, removed or reordered. New choices are
    appended; the ones they replace are gated off."""
    rel = payload["Relationships"]["nocticula"]
    rel["RotationKey"] = "nocticula"
    payload["Relationships"]["nocticula.acquisition"]["RotationKey"] = "nocticula"
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a Nocticula defeated at the Council may not be as gone as the Abyss "
                        "believes; look carefully after the fight, and speak to her at Threshold.")
    for key, groups in DERIVED.items():
        payload.setdefault("Derived", {})[key] = [list(g) for g in groups]
    ours = {s["Id"] for s in SCENES}
    by_id = {s["Id"]: s for s in payload["Scenes"]}

    for s in payload["Scenes"]:
        if s.get("Relationship") not in ("nocticula", "nocticula.acquisition") or s["Id"] in ours:
            continue
        ending = s["Owner"].endswith("Epilogue")
        if ending and s["Id"].startswith("noct.ending_death"):
            # G6(a): her death ending is not played for a queen who is only in hiding.
            s["Forbids"].append(ALIVE)
        elif DEAD in s["Forbids"]:
            # G6(b) and ledger row 2: defeated is not dead; nothing reaches the Commander between the Council and Threshold.
            s.setdefault("ForbidOverrides", {})[DEAD] = ALIVE
            if not ending:
                if FIGHT not in s["Forbids"]:
                    s["Forbids"].append(FIGHT)
                s["ForbidOverrides"][FIGHT] = RETURNED
    for id in HARBOR_ONLY_ENDINGS:
        _scene(by_id, id)["Forbids"].append(SAID_YES)
    # Sol COX: sacrifice with trickster.commander_back (native Trickster survival, or Last Call's bottle) is a living
    # Commander. The permanent-loss pages (and their acquired copies) Forbid it; the living pages that Forbid sacrifice
    # accept it back.
    for s in payload["Scenes"]:
        if s.get("Relationship") not in ("nocticula", "nocticula.acquisition") or not s["Owner"].endswith("Epilogue") or s["Id"] in ours:
            continue
        if "sacrifice" in s["Requires"] and ALIVE_AFTER not in s["Forbids"]:
            s["Forbids"].append(ALIVE_AFTER)
        elif "sacrifice" in s["Forbids"]:
            s.setdefault("ForbidOverrides", {})["sacrifice"] = ALIVE_AFTER

    # NOC-02: any native answer at the audience earns the channel; the fixed pair of keys is dropped from both letters.
    line = _scene(by_id, "noct.acq.the_missing_line")
    line["Requires"] = [r for r in line["Requires"] if r not in DROPPED_EVIDENCE]
    line["RequiresAnyGroups"] = [list(EVIDENCE_ANY)]
    hand = _scene(by_id, "noct.acq.her_hand")
    hand["Requires"] = [r for r in hand["Requires"] if r not in DROPPED_EVIDENCE]
    # Her first words through the seal remember the voice in her rooms.
    start = _node(hand, "start")
    for choice in list(start["Choices"]):
        _gate(choice, forbids=(KEPT,))
        target = choice["Next"]
        start["Choices"].append(c(choice["Text"], "scent_" + target, requires=(*choice["Requires"], KEPT),
                                  forbids=tuple(f for f in choice["Forbids"] if f != KEPT)))
        hand["Nodes"].append(n("scent_" + target, "Nocticula", SCENT_LINE, c("Continue", target), portrait="Nocticula"))


# --- Court scenes (ledger row 11: Nocticula owns all four; optional; never Forbid, close or set another route's flags) ---
# Canon: Vellexia "has reigned as the leader of Alushinyrra's aristocrats" (enGB 82d99a5c); with her gone "the highest seat
# in Alushinyrra has been vacant" (8b5f3d4a); her house tells callers "Lady Vellexia has temporarily left Alushinyrra"
# (c957420f). Authored: the flowers, the little bird, the black silk.

V_PRESUMED = "vellexia.trickster.presumed_dead"
V_KEPT = "vellexia.trickster.kept_as_mirror"
V_DIMINISHED = "vellexia.trickster.cost.diminished"
SECRET_VELLEXIA = "nocticula.trickster.secret_known.vellexia"
COURT_BLACK = ('"Heard? Alushinyrra wore black for her this season. The highest seat in my city stood empty, and every little '
               'aristocrat beneath it began measuring it for their own backside. I sent flowers. Her doormen still tell callers '
               'that Lady Vellexia has temporarily left Alushinyrra, which is almost witty, for doormen."')
COURT_UNDECIDED = ('{n}Her smile does not move.{/n} "Nobody told me. I am told everything. I have not decided yet whether that '
                   'is an insult to her or to me, and until I decide, it belongs to you."')
COURT_CHOICES = (c('"Ask her yourself. Carefully."', flags=(SECRET_VELLEXIA,)),
                 c("[Say nothing.]", abort=True))

threshold("nocticula.trickster.court.vellexia", "Black for Vellexia", "\"Lady Vellexia of the Upper City. You've heard.\"", [
    nar("start", "{n}At the name the projection's attention sharpens, the way a cat's does at a sound behind a wall. "
                 "The fires of Threshold lean in to listen with her.{/n}",
        c("Continue", "kept", requires=(V_KEPT,)),
        c("Continue", "diminished", requires=(V_DIMINISHED,), forbids=(V_KEPT,)),
        c("Continue", "furniture", forbids=(V_KEPT, V_DIMINISHED))),
    nt("kept", COURT_BLACK + "\n"
       "{n}Her voice drops.{/n} \"Then a little bird told me where she went. She is a looking-glass in your quarters, clown, "
       "and she is awake behind it. You kept her.\"\n"
       "{n}She considers you the way she considers a wager she has already won.{/n} \"I could make you give her back. I will not. A succubus who lets herself "
       "be made into furniture has learned something I could never have taught her. Dust her. And cover her, on the nights "
       "you would rather she did not watch; she will be taking notes for me.\"", *COURT_CHOICES),
    nt("diminished", COURT_BLACK + "\n"
       "\"Then a little bird told me she spent those months hanging on a wall as a very flattering portrait of herself, and "
       "came off it unfinished at the hands.\" " + COURT_UNDECIDED, *COURT_CHOICES),
    nt("furniture", COURT_BLACK + "\n"
       "\"Then a little bird told me my first lady spent those months as a piece of furniture in a mortal's house, and came "
       "out of it in a very bad temper.\" " + COURT_UNDECIDED, *COURT_CHOICES),
], ("trickster.ever", V_PRESUMED), (SECRET_VELLEXIA, FIGHT), T_DOING_WELL, ForbidOverrides={FIGHT: RETURNED})

# Horzalah (ledger row 11, the fourth court): Nocticula's own read of what her city's Guild did with the Commander's ear
# (horzalah_trickster guild.kept sets horzalah.trickster.returned). Canon: Yozz ran "my city's assassins' guild" (Demon-path
# Nocticula_C3/Cue_0014, the lore holds on every path); Baphomet did not answer his daughter (Prison_Baph/Cue_0122). The
# variants read Horzalah's own outcome flags in text only; nothing here gates on her closure.
H_RETURNED = "horzalah.trickster.returned"
H_FREE = "horzalah.trickster.left_free"
H_THREAT = "horzalah.trickster.threatened"
SECRET_HORZALAH = "nocticula.trickster.secret_known.horzalah"
COURT_H_CHOICES = (c('"She would rather have a knife than your patience, Lady."', flags=(SECRET_HORZALAH,)),
                   c("[Say nothing.]", abort=True))
COURT_H = ('"I heard. Yozz\'s girl walked into my city\'s Guild in the middle of the evening, pinned a box over your '
           'contract and untied the ribbon, and my assassins passed a piece of you from hand to hand and bowed to it." '
           '{n}The projection\'s smile is slow.{/n} "Her father said nothing. He never does, for her. One day I will collect '
           'the rent on that silence from him."')

threshold("nocticula.trickster.court.horzalah", "An ear in my city", '"The Guild in your city has a new story, Lady."', [
    nar("start", "{n}At the word Guild the projection's attention sharpens, and the fires of Threshold lean in to listen.{/n}",
        c("Continue", "threat", requires=(H_THREAT,)),
        c("Continue", "free", requires=(H_FREE,), forbids=(H_THREAT,)),
        c("Continue", "kept", forbids=(H_THREAT, H_FREE))),
    nt("kept", COURT_H + "\n\"From her I will collect nothing. A guildmaster who can make my knives kneel to a clown\'s ear is "
       "worth more to me alive, and owing her chair to you, than she would be owing it to me. Debts to you are so much more "
       "amusing to watch.\"", *COURT_H_CHOICES),
    nt("free", COURT_H + "\n\"And then you gave her the door, she tells people. She has not stopped telling people. A "
       "Baphomet\'s brat who cannot stop saying the word door is either in love or planning a murder, and in my city those are "
       "the same errand.\"", *COURT_H_CHOICES),
    nt("threat", COURT_H + "\n{n}Her eyes go to the scar on your cheek.{/n} \"And then you put a knife to her lie, and she opened "
       "your face for it. Good. I would have taken the other ear.\"", *COURT_H_CHOICES),
], ("trickster.ever", H_RETURNED), (SECRET_HORZALAH, FIGHT), T_DOING_WELL, ForbidOverrides={FIGHT: RETURNED})

# b6/b7 belong before the favour page (b8) in the spec's sibling order: appended here, then moved into place.
page("nocticula.trickster.defeated.epilogue.mirror", "A season as furniture",
     "{n}She never forgave Vellexia for the season she spent as furniture, mostly because nobody had told her.{/n}",
     ("trickster.ever", SECRET_VELLEXIA))
# Vellexia's three outcomes are exclusive (each device sets one and forbids itself), so b6 reads the two that end her
# season off the wall, never Forbids the kept one: forbidding another route's unavailable state breaks coexistence.
SCENES[-1]["RequiresAnyGroups"] = [["vellexia.trickster.unmirrored", V_DIMINISHED]]
page("nocticula.trickster.defeated.epilogue.mirror_kept", "Black silk",
     "{n}Every winter a parcel reached the Commander from Alushinyrra: a square of black silk, the right size to cover a tall "
     "mirror, and a card in a hand the Commander knew. \"For the nights she should not watch.\"{/n}",
     ("trickster.ever", SECRET_VELLEXIA, V_KEPT))
_MIRROR_PAGES = [SCENES.pop(), SCENES.pop()][::-1]
_FAVOUR = next(i for i, s in enumerate(SCENES) if s["Id"] == "nocticula.trickster.defeated.epilogue.favour")
SCENES[_FAVOUR:_FAVOUR] = _MIRROR_PAGES


# Arueshalae's favour (ledger row 11: Nocticula writes court.arueshalae; it collects arueshalae's cost.nocticula_favour
# once). Remote: after the Ch5 audience her throne room is walled off (Cue_0019/Cue_0023, native comment) and she has no
# other unit in Chapter 5. Canon: she is "the succubus queen" who allows Arueshalae to follow the Commander
# (Nocticula_main/Cue_0523 b84ef61b) and trades in what people "desire most" (Cue_0520 e50ab396).
A_FAVOUR = "arueshalae.trickster.cost.nocticula_favour"
FAVOUR_CALLED = "nocticula.trickster.favour_called.arueshalae"
FAVOUR_BURNED = "nocticula.trickster.cost.favour_burned"


def ar(id, text, *choices, **kw):
    return n(id, "Arueshalae", text, *choices, portrait="Arueshalae", **kw)


SCENES.append(scene("nocticula.trickster.court.arueshalae", "A favour, called", "Memory", 5, "", [
    nar("seal", '''{n}The letter smells of night-blooming flowers. It is addressed to you and meant for the succubus reading it over your shoulder, who has gone very still.{/n}''',
        c("Continue", "letter")),
    nt("letter", '''"Commander. You owe me a favour for my succubus, and I have decided what it is. Read her this letter aloud, in your own voice, every word."
"'Arueshalae. You were mine before you were anyone's. You are welcome at my table tonight, and every night after. Choose.'"
"That is the whole favour. Whatever she chooses, you have paid."''',
        c("[Read her the letter, word for word.]", "her_side"),
        c("[Burn it where she can see.]", "raised")),
    ar("her_side", '''{n}You read it. Every word, in your own voice, as instructed. She does not interrupt. When you finish, she takes the letter out of your hand.{/n}''',
       c("Continue", "chose", requires=("arueshalae.committed",)),
       c("Continue", "night", forbids=("arueshalae.committed",))),
    ar("chose", '''"...She wants me to choose." {n}She folds the letter very small, and smaller, until it will not fold any more.{/n} "I did. Tell her I said so." {n}She puts it in her bodice, next to the black pearl.{/n} "No. Don't. Let her wonder. It's the only thing I've ever been able to give her that she didn't take."''',
       c("[Let it be.]", flags=(FAVOUR_CALLED,))),
    ar("night", '''"She wants me to choose." {n}She is quiet for a long time.{/n} "One night. I'll go and hear what she has to say. Leave the door unlocked."
{n}She comes back at dawn, smelling of flowers, and does not say what she chose.{/n}''',
       c("[Let it be.]", flags=(FAVOUR_CALLED,))),
    nt("raised", '''{n}The ash does not settle. It turns, on the table, into a second note, in the same beautiful hand.{/n}
"You burned a letter from a queen in front of her own subject. The favour is paid, Commander; you have just shown her what you think of me. She will remember that longer than anything I could have written."''',
       c("[Let the smoke go.]", flags=(FAVOUR_CALLED, FAVOUR_BURNED))),
], requires=("trickster.ever", "arueshalae.started", "arueshalae.trickster.returned", A_FAVOUR, "nocticula.trickster.contact"),
   forbids=(FAVOUR_CALLED, FIGHT), delay=24, last=5, optional=True, Relationship="nocticula", Remote=True, Chapters=[5],
   ForbidOverrides={FIGHT: RETURNED}))
# Shamira behind the Commander's eyes (ledger row 11: Nocticula owns court.shamira; additive, R2). Inline on her own
# Chapter 5 audience list, after the kill, while what is left of her steward is in the Commander's head: she smells her
# on the clown and chooses what to do about it, then continues into her canon line, "You've saved me the trouble of having
# to deal with her." (Nocticula/Cue_0021 84df3b22 -> Cue_0019, the end of the audience). Canon: Shamira "is no longer
# content to rule Alushinyrra on my behalf... She covets my throne instead" (Cue_0015 7cad8bc1); Nocticula knows her
# brother's enchantments by their "sickly sweet smell" (Cue_0016 bb552fe4). Sets only Nocticula's own flags; Shamira's
# route reads them in node text.
AUDIENCE_LIST = "2729c49e2bf20c64caa4f54b352e03f6"   # Nocticula/AnswersList_0007
REPORTED = "84df3b227f54e3e44888b5bb8585089d"        # Nocticula/Cue_0021 "...You've saved me the trouble..."
SECRET_SHAMIRA = "nocticula.trickster.secret_known.shamira"
GREETED = "nocticula.trickster.court.shamira_greeted"
# The evidence that she is in the Commander's head at this audience (straight after the kill, before the closet): the door
# held open at Socothbenoth's briefing (shamira.trickster.primed). Without it she is not in yet: an unprimed Commander only
# finds her drowning at the first rest, after the boudoir is shut, so this audience never sees her. Replaces the round-2
# flask reveal (the flask device was dropped by the coordinator's revision of Shamira's route; 11 §2, 2026-09-29).
SHAMIRA_IN = "shamira.trickster.primed"
SHAMIRA_OUT = ("shamira.trickster.declined", "shamira.trickster.cast_out", "shamira.trickster.embodied")

SCENES.append(scene("nocticula.trickster.court.shamira", "Something behind your eyes", "Nocticula", 5,
    "[Keep your thoughts on the carpet.] \"I've done what I came to do, Lady.\"", [
    nt("sniff", '''{n}Nocticula does not answer at once. She closes her eyes, as she did when she thought you were her brother, and breathes in, slowly, through her nose.{/n}
"You have done something." {n}Her eyes open, and they go straight to your face, and then a little behind it, as if your skull were glass.{/n} "There is blood on you, and my brother's sickly perfume, and under both of them something I have smelled in my bed every night since I pulled her off the black water. Not on you. In you."''',
        c("Continue", "found")),
    nt("found", '''{n}She crosses the room without seeming to walk. She does not touch you. She bends, close enough that you can feel the cold coming off her skin, and looks into your eyes the way one looks into a window at night, for whoever is standing behind the glass.{/n}
"Oh," {n}says the Lady in Shadow, very softly.{/n} "Oh, you clever, clever little thief. You killed her in my bedroom, and you let her in."''',
        c("[Lie] \"There's nobody in here but me, Lady.\"", "lie"),
        c("[Let her look] \"She's here. If you want to say goodbye, say it now.\"", "greet", flags=(GREETED,)),
        c("[Say nothing.]", "silence")),
    nt("lie", '''"Nobody." {n}She smiles, and it is not unkind, which is worse.{/n} "Of course. Keep your nobody, clown. I will not rummage in a guest's head." {n}She straightens a little.{/n} "But I will say one thing to it, since it can hear me."''',
        c("Continue", "hello")),
    nt("greet", '''"Goodbye? To Shamira?" {n}Her laugh is low and entirely delighted.{/n} "Nobody says goodbye to Shamira. She would never forgive it. One says good evening, and one waits to see what she will do next."''',
        c("Continue", "hello")),
    nt("silence", '''"Wise. Very wise. You have learned not to talk in front of me." {n}She tilts her head at your eyes as if at a small, disagreeable animal behind a grille.{/n} "She never did."''',
        c("Continue", "hello")),
    nt("hello", '''{n}She bends close again, right to your face, and speaks past you, to whoever is behind your eyes, the way one speaks to a dog in a kennel.{/n} "Hello, my dear."
{n}That is all. She straightens, and her face is perfectly calm.{/n} "Keep her quiet in my city, clown. If I find her walking around my palace in a borrowed body wanting my chair, I will know whose idea it was." {n}A pause, while she decides something.{/n} "And if I do not find her, I will know that too."''',
        c("[Say nothing more.]", native_next=REPORTED, flags=(SECRET_SHAMIRA,))),
], requires=("trickster", "shamira.killed", SHAMIRA_IN), forbids=(SECRET_SHAMIRA,) + SHAMIRA_OUT, last=5, optional=True,
   Relationship="nocticula", Chapters=[5], AnswerLists=[AUDIENCE_LIST], NativeReturnCue=AUDIENCE_YOU))
