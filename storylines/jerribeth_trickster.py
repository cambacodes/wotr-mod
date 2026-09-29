"""Jerribeth on the Trickster path: the tenant and the toast (Writer/handoffs/trickster/jerribeth.md, families F14 and F05).

Canon: in the Ivory Sanctum she speaks inside the Commander's head ("You have arrived, Commander," comes the high-pitched
voice in your head: JerribethGreetings/Cue_0001 8a632a52), prices every answer ("I will tell you what I know only if you
fulfill your part of the deal": Cue_0018 4f837220), and served Baphomet "for as long as it benefited me more than it cost
me" (Cue_0031 7c5e45ae). Nenio explains at the greeting that oolioddroo lay their eggs in a sleeping creature and that
the hatchlings "influence the thought processes of the host" (Cue_0045 93dfa959). In Wintersun she "merely planted a few...
ideas in their heads" (JerribethReveal/Cue_0008 063d159a). JerribethDead cd866695 is canon and stays set.
Authored, and labelled as authored: at the deal she lays a thought-seed in the Commander, "a small investment". The seed
dies with its mother unless it has a claim to the house; the Commander's joke gives it one: rent. That is the Trickster's
property that isn't there (TricksterKnowledgeArcanaTier3Feature 5e26c673), applied to her own biology. A Commander who
never met her drinks to her, and one of her Wintersun ideas, still lodged in a deserter, hears the toast.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
GREETING_DEAL = "190fda58a169c9340b626f1a503c696f"   # c3/IvorySanctum/JerribethGreetings/AnswersList_0011 (the deal list)
DEAL_PRICE = "4f8372200576ead4e86c7c2606c580d0"      # Cue_0018 "...only if you fulfill your part of the deal." -> list 0011
FINAL_LIST = "5cca8ccea46e72343a4544c44be9790c"      # JerribetnFinal/AnswersList_0004, beside [Attack] Answer_0017
KING_HUB = "6dccfd39947ef4242a8afbe36b21a46c"        # c3/Mythic_Trickster/FoolKing_Tavern/AnswersList_0054
KING_RETURN = "7b050ba0745bf144e815632e39b34853"     # Cue_0065 "Beer is a noble drink!" -> list 0054
CAMELLIA_HUB = "589d83230bbbfd04bb1220ee4fef1ce1"    # Dialgoue_CameliaMain
WOLJIF_HUB = "e41585da330233143b34ef64d7d62d69"      # CompanionDialogues/Woljif/AnswersList_0003
DREZEN = "2570015799edf594daf2f076f2f975d8"
NEXUS = "7847c3e3537104f4694167af0b9fcd0e"

DEAD = "jerribeth.unavailable"
PRIMED = "jerribeth.trickster.primed"
RETURNED = "jerribeth.trickster.returned"
DECLINED = "jerribeth.trickster.declined"
MET_BY_TOAST = "jerribeth.trickster.met_by_toast"
TENANT = "jerribeth.trickster.cost.tenant"
LATE = "jerribeth.trickster.cost.late"
HOST = "jerribeth.trickster.cost.host"
LODGER = "jerribeth.trickster.cost.lodger"
STATUE = "jerribeth.trickster.body.statue"
LOCUST = "jerribeth.trickster.body.locust"
TOAST = "jerribeth.trickster.cost.toast"
TOAST_HOST = "jerribeth.trickster.cost.toast_host"      # the toast branch: the man who poured the cup, given to her
TOAST_MEMORY = "jerribeth.trickster.cost.toast_memory"  # the toast branch: the Commander paid with the night of the toast
LEVY = "jerribeth.trickster.toast_levy"            # the letter twin: the toast was drunk with the Wintersun levy
FORFEIT = "jerribeth.trickster.cost.forfeit"
NO_FORFEIT = "jerribeth.trickster.no_forfeit"      # her hard no at jerribeth.future: "I do not sign blank pages."
LATE_COMMITTED = "jerribeth.trickster.late_committed"
KILLED = "jerribeth.killed_by_commander"
BETRAYED = "jerribeth.betrayed_commander"
INSULTED = "jerribeth.insulted"
EGG_LORE = "jerribeth.egg_lore_heard"
WINTERSUN_IDEA = "jerribeth.wintersun_idea_seen"

RELATIONSHIP_PATCH = dict(
    UnavailableOverrides={DEAD: RETURNED},
    TricksterAccess={
        "dead": dict(detect=[DEAD], device="jerribeth.trickster.dead.tenant", returned=RETURNED),
        "never_met": dict(detect=["!jerribeth.met", "!" + DEAD], device="jerribeth.trickster.never_met.toast_king",
                          returned=MET_BY_TOAST),
    })
SEEN_CUES = {
    INSULTED: ["10939d0d12eb7fb4da65a58553e19f04",       # Greetings/Cue_0002 "You did me a grave insult at our last meeting."
               "09391300eaf00664886c2e05458a8b24"],      # Reveal/Cue_0031 "I will remember this, Commander."
    BETRAYED: ["09280d586e0118b4882abcdb5a4787c6",       # JerribetnFinal/Cue_0012 "...the only thing standing between me..."
               "8ccd036dc7f03704590ac5787c3997d2"],      # JerribetnFinal/Cue_0029
    WINTERSUN_IDEA: ["063d159af56b4c54292e6e2eaca8ca08"],  # Reveal/Cue_0008 "I merely planted a few... ideas in their heads."
}
SELECTED_ANSWERS = {
    "jerribeth.trickster.attack_final": "e3158fbb613ebec4bade9b91b9c31aed",    # JerribetnFinal/Answer_0017 [Attack]
    "jerribeth.trickster.attack_bored": "807cc780b4bdcbe49a69aa179576857d",    # Greetings/Answer_0008 [Attack] "You're boring me"
    "jerribeth.trickster.attack_refused": "0149f56290ac8d540a83ec5e92f10c51",  # Greetings/Answer_0016 [Attack] "...Die!"
}
DERIVED = {KILLED: [[key] for key in SELECTED_ANSWERS]}
PERMANENT = (DEAD,)   # JER-11: a completed JerribethDead still counts as her death


def j(id, text, *choices, **kw):
    return n(id, "Jerribeth", text, *choices, portrait="Jerribeth", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Jerribeth", **kw)


def ladder(steps, last):
    """A run of optional variant nodes: steps = [(node_id, requires, make(choices) -> node)], each shown only when its
    requires hold; every node continues to the next step that applies, then to `last`. Returns the choices that enter
    the run and the nodes."""
    def entry(k):
        # From position k, go to the first later step whose requires hold, skipping the ones before it.
        out, skipped = [], []
        for node_id, req, _ in steps[k:]:
            out.append(c("Continue", node_id, requires=req, forbids=tuple(f for f in skipped)))
            if len(req) != 1:
                raise ValueError("ladder steps take one flag")
            skipped.append(req[0])
        out.append(c("Continue", last, forbids=tuple(skipped)))
        return out
    nodes = [make(*entry(k + 1)) for k, (_, _, make) in enumerate(steps)]
    return entry(0), nodes


# --- State dead_at_sanctum: the tenant (F14) ----------------------------------------------------------------------

# Primer A: inline on the deal list, before she names her price; the lease returns to Cue_0018.
SCENES.append(scene("jerribeth.trickster.dead.setup_greeting", "Rent", "Jerribeth", 3,
    '[Play a prank on the Lady of the Sun] "Plant whatever you like. I\'m charging rent."', [
    j("lease", '''{n}The buzzing in your skull stops, as if something with many legs has gone very still.{/n}
"Rent."
{n}A pause, long enough for the Sanctum's cold to find the back of your neck.{/n}
"You would charge a demon rent for the use of your own head. How very mortal. I always read the small print, Commander. Yours has none."
{n}Laughter, high and abrasive, like a buzzing insect, and for one moment it comes from inside your ear rather than beside it.{/n}
"Do you know what I left in Wintersun? Ideas. I have not been there in months, and they are still there, because the heads they live in grew used to them. A thought a house keeps does not need its mother, crusader. It needs the house."
{n}The antennae tilt, pricing you.{/n}
"Very well. Lease accepted. And I shall pay my rent in the only coin a tenant like me carries: one of your memories a month, my choice, taken in lieu of repairs. Consider it a small investment on my part. You will not feel it. Probably."''',
      c("Continue", "lore", requires=(EGG_LORE,)),
      c('"Now. The deal."', forbids=(EGG_LORE,), flags=(PRIMED,))),
    j("lore", '''"Your fox has told you what we lay, and where. And still you offer me a room."
{n}The antennae dip, almost a bow.{/n}
"I shall try to be a quiet lodger. I make no promises about the neighbours."''',
      c('"Now. The deal."', flags=(PRIMED,))),
], requires=("trickster",), forbids=(PRIMED, DEAD), last=3, optional=True, Relationship="jerribeth", Chapters=[3],
   AnswerLists=[GREETING_DEAL], NativeReturnCue=DEAL_PRICE, EntryMythic="PlayerIsTrickster"))

# Primer B: not inline (no JerribetnFinal cue reopens list 0004 cleanly); talking to her again reopens the native list.
SCENES.append(scene("jerribeth.trickster.dead.setup_final", "A lease, read in advance", "Jerribeth", 3,
    '"One more thing, before we finish."', [
    j("lease", '''{n}The needle stops halfway into the locust.{/n}
"You are thinking very loudly, crusader. About rent."
{n}She does not look up from the pinning case. She reads the thought anyway, in your head, in the time it takes the needle to finish its way through the carapace.{/n}
"A lease I have not been offered yet, for a room I have not yet taken. No forfeit clause. No term. No exit. You write contracts like a child, Commander."
{n}The locust twitches once on its pin and is still.{/n}
"Say it aloud. I prefer my bargains witnessed, even when the only witness is you."''',
      c('[Play a prank on the Lady of the Sun] "Plant whatever you like. I\'m charging rent."', "accepted",
        mythic="Trickster", flags=(PRIMED,)),
      c('"On second thought, keep out of my head."', abort=True)),
    j("accepted", '''"Accepted."
{n}Something settles behind your left eye, light as a moth on a sleeve.{/n}
"A room you give is a room I keep, even when I am not there to keep it. Ask Wintersun. I pay my rent in your memories, one a month, my choice. Deals with demons are a losing game, Commander. I said so myself. We shall see which of us is losing this one."''',
      c('"We\'ll see."')),
], requires=("trickster",), forbids=(PRIMED, DEAD), last=3, optional=True, Relationship="jerribeth", Chapters=[3],
   AnswerLists=[FINAL_LIST]))

# Late fallback (R2-2): the act happens now, on the page, over a dying seed; the id is historic, nothing is backdated.
SCENES.append(scene("jerribeth.trickster.dead.backdated", "Signed late", "Jerribeth", 3, "", [
    nar("start", '''{n}Near dawn a thought arrives that is not yours. It is neat, it is patient, and it is starving.{/n}''',
      c("Continue", "tenant_late")),
    j("tenant_late", '''"I laid something in you at the Sanctum, Commander. A small investment. You did not notice. Nobody ever does."
{n}The voice is faint, and very precise, the way a clerk is precise with the last coin in the drawer.{/n}
"It is dying with me. Slowly, because you are warm."
{n}The thought turns over, testing the walls of your skull, and a little less of it turns back.{/n}
"A creature of the Abyss may stay where it has a claim. It has none. Unless you give it one."''',
      c("Continue", "lore", requires=(EGG_LORE,)),
      c('[Play a prank on the Lady of the Sun] "Plant whatever you like. I\'m charging rent. From tonight."', "signed",
        forbids=(EGG_LORE,), mythic="Trickster", alignment=("Evil", 1), flags=(PRIMED, LATE)),
      c('"Get out of my head."', "evicted", forbids=(EGG_LORE,), flags=(DECLINED,))),
    j("lore", '''"Your fox told you what we lay, and where. You listened. And still you slept."''',
      c('[Play a prank on the Lady of the Sun] "Plant whatever you like. I\'m charging rent. From tonight."', "signed",
        mythic="Trickster", alignment=("Evil", 1), flags=(PRIMED, LATE)),
      c('"Get out of my head."', "evicted", flags=(DECLINED,))),
    j("signed", '''{n}Something in your skull stops dying. It takes the lease with both hands, the way a drowning thing takes a rope.{/n}
"Rent. From *tonight*. And no forfeit clause. You are very bad at this, Commander."
{n}The buzzing comes back, stronger, and settles in to stay.{/n}
"I will honour a lease signed this late exactly as long as it amuses me. Do try to remain amusing."''',
      c('"Sleep well, tenant."')),
    nar("evicted", '''{n}The thought does not argue. It goes on dying, quietly, the way a candle does, and by the time the camp is awake there is nothing behind your eyes but your own tiredness.{/n}
{n}For a day or two you catch yourself listening for a laugh that does not come.{/n}''',
      c('"Good riddance."')),
], requires=("trickster", DEAD), forbids=(PRIMED, RETURNED, DECLINED), last=5, optional=True, Relationship="jerribeth",
   Remote=True, Chapters=[3, 5], Areas=[DREZEN, NEXUS], TricksterDevice=True, TricksterState="dead"))


def _variant(node_id, text):
    return lambda *choices: j(node_id, text, *choices) if not text.startswith("{n}") else nar(node_id, text, *choices)


TENANT_VARIANTS = [
    ("v_late", (LATE,), _variant("v_late", '''"Our lease was signed late, over a seed that was already dying. I will honour it exactly as long as it amuses me. You will know when it stops."''')),
    ("v_killed", (KILLED,), _variant("v_killed", '''"You killed me, Commander. And then you carried me home. Considerate."''')),
    ("v_betrayed", (BETRAYED,), _variant("v_betrayed", '''"I tried to kill you. You were quicker. I bear no grudge. I bear rent."''')),
    ("v_insulted", (INSULTED,), _variant("v_insulted", '''"And I told you I would remember. I am, as it happens, *inside* the remembering."''')),
    ("v_failed", ("trickster.failed",), _variant("v_failed", '''"Your little power is gone, I notice. The trick went out of you like air out of a bladder. My lease did not."''')),
]
_TENANT_ENTRY, _TENANT_NODES = ladder(TENANT_VARIANTS, "house")

SCENES.append(scene("jerribeth.trickster.dead.tenant", "The tenant", "Jerribeth", 3, "", [
    nar("start", '''{n}Near dawn a thought arrives that is not yours. It is neat, it is patient, and it is counting.{/n}''',
      c("Continue", "tenant")),
    j("tenant", '''"Commander. You told me I could plant whatever I liked, and that you would charge rent. I planted. You charged."
{n}The voice is exactly where it was in the Sanctum: behind your eyes, a little to the left.{/n}
"When the sword went through me, the seed began to die, as my children do when I do. Then it found what my Wintersun ideas found: a house that had agreed to keep it. You gave it a room, and it paid its rent every month, the way I set it: one of your memories, taken and kept. A house that has been paid is a house that holds."
{n}Laughter buzzes behind your eyes, high and abrasive.{/n}
"I am in arrears. You are haunted. Which of us minds more, do you think?"''', *_TENANT_ENTRY),
    *_TENANT_NODES,
    j("house", '''"Do not make that face. You cannot see it; I can."
{n}Something turns over in your memory, idly, the way a guest turns over the ornaments on a shelf.{/n}
"A seed needs somewhere to grow, and I will not spend my second life as an itch. Choose where I live, or I will choose. I have already walked through your memories, and I know which of your officers sleeps soundly."''',
      c('"The Lady of the Sun statue. You always liked being worshipped."', "statue_done", crusade=("Favors", -100),
        flags=(RETURNED, TENANT, "jerribeth.started", STATUE)),
      c('"One of Xanthir\'s locusts. You pinned them for a reason."', "locust_done", crusade=("Materials", -100),
        flags=(RETURNED, TENANT, "jerribeth.started", LOCUST)),
      c('[Give her a host] "Take a deserter from the stockade. Nobody will miss him."', "host_done", alignment=("Evil", 2),
        flags=(RETURNED, TENANT, "jerribeth.started", HOST)),
      c('"Stay where you are. Rent\'s due on the first of the month."', "lodger_done", alignment=("Chaotic", 1),
        flags=(RETURNED, TENANT, "jerribeth.started", LODGER)),
      c('"Not tonight."', abort=True)),
    nar("statue_done", '''{n}Four days later a Wintersun idol of the Lady of the Sun arrives in camp under canvas, gilt and serene and a head taller than the carters who unload it. The chaplains want a favour for the room it takes up, and a second favour for the prayers they will have to say around it.{/n}
{n}At night its gilt face turns, very slightly, toward your window.{/n}''',
      c('"Goodnight, my lady."')),
    nar("locust_done", '''{n}A salvage team goes back into the Ivory Sanctum for her pinning case and brings it out whole, cursing the stairs. One needle has been pulled.{/n}
{n}On your desk, under a glass, a locust cleans its face with its forelegs, slowly and very thoroughly, and keeps every one of its eyes on you.{/n}''',
      c('"Mind the papers."')),
    j("host_done", '''"*Now* you have taste."
{n}In the morning the stockade reports one prisoner fewer, and a sentry who swears the man walked out past him at the change of watch, smiling, with his hands folded behind his back like a courtier.{/n}
{n}Nobody asks the man's name. Nobody ever will.{/n}''',
      c('"Keep him clean."')),
    nar("lodger_done", '''{n}On the first night of the month you laugh at nothing, high and abrasive, and the aide bringing your dispatches drops one of them.{/n}
{n}In the morning you cannot remember the name of your first horse. You look for it, the way you would feel for a missing tooth, and find only a neat, swept space where it used to be.{/n}''',
      c('"Paid in full."')),
], requires=("trickster.ever", PRIMED, DEAD), forbids=(RETURNED, DECLINED), delay=48, last=5, optional=True,
   Relationship="jerribeth", Remote=True, Chapters=[3, 4, 5], Areas=[DREZEN, NEXUS], TricksterDevice=True,
   TricksterState="dead"))


# --- State never_met: the toast (F05) ------------------------------------------------------------------------------

VOICE = '''"Whoever you are *not*. How generous, to make yourself the single exception in a demon's life."
{n}The voice is too high for the throat it comes out of, and it takes the long way round the words, tasting them.{/n}
"I left a few ideas in Wintersun, Commander. They keep. This one {what}."
{n}The deserter's mouth stays shut. The laughter comes from inside your own head, high and abrasive, and his face goes slack while it lasts.{/n}
"I have never met you. I intend to. Then we shall see which of us the joke was on."'''

# Inline on the King's hub: Owner-voiced cues take the native speaker (the King), every other node is unvoiced prose, so
# the deserter's borrowed voice is narrated rather than put in the King's mouth.
SCENES.append(scene("jerribeth.trickster.never_met.toast_king", "A toast to the Lady of the Sun", "Thaberdine", 5,
    '[Raise your cup to the Lady of the Sun] "To the Lady of the Sun, who\'ll betray whoever I\'m not."', [
    n("king", "Thaberdine", '''"The Lady of the what? Never heard of her. To her! Bottoms up, no stopping!"''',
      c("Continue", "host"), portrait="Jerribeth"),   # inline: the King's own native portrait is shown
    nar("host", '''{n}The tavern roars and drinks. At the end of the bench a Wintersun deserter in a sun-stitched collar puts his cup down without drinking.{/n}
{n}His eyes go flat and bright at the same time, like a beetle's back.{/n}''',
      c("Continue", "voice")),
    nar("voice", VOICE.replace("{what}", "drinks"),
      c('"Then come and find out."', flags=(MET_BY_TOAST, TOAST, "jerribeth.started")),
      c('[Pour the cup out on the floor] "Wrong tavern, madam."', "spilled")),
    nar("spilled", '''{n}The deserter blinks, looks at the puddle, and asks who spilled his beer. Nobody answers him. The King is already calling for another round.{/n}''',
      c('"Another round."', abort=True)),
], requires=("trickster", "chapter_later", "fool_king.available"),
   forbids=("jerribeth.met", DEAD, MET_BY_TOAST, "fool_king.gone"), last=5, optional=True, Relationship="jerribeth",
   Chapters=[5], AnswerLists=[KING_HUB], NativeReturnCue=KING_RETURN, EntryMythic="PlayerIsTrickster"))

SCENES.append(scene("jerribeth.trickster.never_met.toast", "A toast at the evening rest", "Jerribeth", 5, "", [
    nar("tavern", '''{n}A sergeant of the Wintersun levy brings you a cup at the evening rest, because the men want a toast and you are the Commander.{/n}
{n}While you hold it he tells you the one they tell in Wintersun about the Lady of the Sun of the Ivory Sanctum: who served Baphomet for exactly as long as it paid, and then sold his Xanthir out to the crusade with a smile.{/n}''',
      c("Continue", "saw", requires=(WINTERSUN_IDEA,)),
      c('[Raise your cup to the Lady of the Sun] "To the Lady of the Sun, who\'ll betray whoever I\'m not."', "voice",
        forbids=(WINTERSUN_IDEA,), mythic="Trickster"),
      c('"Not tonight."', forbids=(WINTERSUN_IDEA,), abort=True)),
    nar("saw", '''{n}You were in Wintersun. You heard her explain the trick, in a voice inside your skull, and you never thought to ask how long an idea lasts once it is planted.{/n}''',
      c('[Raise your cup to the Lady of the Sun] "To the Lady of the Sun, who\'ll betray whoever I\'m not."', "voice",
        mythic="Trickster"),
      c('"Not tonight."', abort=True)),
    j("voice", '''{n}The sergeant's hand stops on the jug. His eyes go flat and bright at the same time, like a beetle's back.{/n}
''' + VOICE.replace("{what}", "carries cups"),
      c('"Then come and find out."', flags=(MET_BY_TOAST, TOAST, LEVY, "jerribeth.started"))),
], requires=("trickster", "chapter_later"),
   forbids=("jerribeth.met", DEAD, MET_BY_TOAST, "jerribeth.trickster.never_met.toast_king", "fool_king.available"),
   last=5, optional=True, Relationship="jerribeth", Remote=True, Chapters=[5], Areas=[DREZEN, NEXUS]))


# --- Epilogue: paragraphs on her registered endings, and the late commit (R2-6) --------------------------------------

TRICKSTER_PARAGRAPHS = (
    p("In the Commander's quarters a gilt idol of the Lady of the Sun kept its face turned toward the bed. The chaplains "
      "never did stop asking for the favour back.", requires=(STATUE,)),
    p("A locust lived for years under a glass on the Commander's desk, long past any locust's season. It cleaned its face "
      "whenever a letter was opened, and it read every one.", requires=(LOCUST,)),
    p("The man from the stockade served the Commander's household for the rest of his life, courteous and exact, and "
      "smiling. Nobody who had known him before would sit near him at supper.", requires=(HOST,)),
    p("The Commander's physicians recorded a curious symptom: on the first of each month the Commander laughed at nothing, "
      "high and abrasive, and afterwards could not remember one small thing. The Commander never complained. The rent was "
      "always paid.", requires=(LODGER,)),
    p("The lease had been signed late, over a seed that was already dying. She honoured it exactly as long as it amused "
      "her. It amused her for the rest of the Commander's life.", requires=(LATE,)),
    p("In the taverns of Drezen they still tell the toast. Nobody tells the ending: the Lady of the Sun never did betray "
      "the one who made it. She considered this the finest betrayal of her career.", requires=(TOAST,)),
    p("A sergeant of the Wintersun levy served in the Commander's household after the war, exact and courteous and "
      "smiling a little too widely. He never drank, and he never once poured a cup for anyone.", requires=(TOAST_HOST,)),
    p("The Commander could never remember the night of the toast, only that it had cost something. Jerribeth told it "
      "differently whenever she was asked, and always as the evening they had first met.", requires=(TOAST_MEMORY,)),
    p("She collected the forfeit on the first anniversary of the contract, without warning, as she had said she would. "
      "She took the Commander's first meeting with her: the voice in the head, the first bargain, all of it. Afterwards "
      "the Commander knew they had met only because she said so, and she told it differently every time, a little more "
      "flattering to herself with each telling. \"You cannot contradict me,\" she said, when the Commander objected. "
      "\"That was the point. Now I am the only one who remembers how we began, and I intend to improve it.\"",
      requires=(FORFEIT,)),
)
REFUSED_PARAGRAPH = p(
    "A crusade clerk later found, in the Commander's papers, a blank contract with a single line written in a small, neat "
    "hand: \"No forfeit, no signature.\"", requires=(NO_FORFEIT,))

SCENES.append(scene("jerribeth.trickster.epilogue.commit", "The guest who knocked", "Epilogue", 5, "", [
    nar("offer", '''{n}The war ended before the lease did. Jerribeth came to the Commander's door the first spring after the Worldwound closed, in a guise the guards did not question, with the clause she had been saving.{/n}
"The forfeit is one memory, of my choosing, when I choose. I have already read your answer, Commander. Show me whether I read it right."''',
      c('[Give her your hand.]', "signed"),
      c('[Keep your hands folded in your lap.]', "torn")),
    nar("signed", '''{n}The Commander held out a hand. She turned it palm up and read it twice, the way she read small print, as if checking it for a trick, and did not find one, and seemed disappointed and pleased in exactly equal measure.{/n}
{n}She collected a year later to the day, over breakfast, between one sentence and the next. She took the war: not the Commander's deeds, which were written down everywhere, but the having been there. The Commander put down the cup and could not say why the tea tasted of smoke.{/n}
"There," she said. "Now I am the only one at this table who remembers how we met, and I intend to improve it."
{n}Afterwards the Commander read about the crusade like a stranger reading a history, and Jerribeth, who had not been there either, told it back over supper, with herself in it.{/n}
{n}At the first Drezen muster after the war, a grey sergeant who had carried the Commander off the wall at Iz came up to clasp arms, and the Commander asked his name. He stood there with his hand out until Jerribeth, at the Commander's elbow, told him the story of that day, better than he could have told it himself, with a detail in it that had not happened. He never came to a muster again. The Commander never once caught her in a lie, which was, she said, the whole point.{/n}''',
      c(), paragraphs=TRICKSTER_PARAGRAPHS),
    nar("torn", '''{n}The Commander kept both hands folded in their lap, where she could see them.{/n}
{n}She studied the hands, then the face above them. Then she laughed, high and abrasive, loud enough to bring the guard running.{/n}
"No forfeit, no lease. And still you open the door to me." {n}She sat down anyway, uninvited, at the Commander's own table.{/n} "You are very bad at this, Commander. I shall come back tomorrow, and the day after, until one of us learns to write a better one."
{n}She did. Neither of them ever did. Whatever else she took, the Commander kept the war, including the parts worth losing.{/n}''',
      c())],
    requires=("trickster.ever", "jerribeth.commission", LATE_COMMITTED),
    forbids=("jerribeth.committed", "jerribeth.closed", DECLINED, DEAD), last=99, Relationship="jerribeth",
    ForbidOverrides={DEAD: RETURNED}))


# --- Reactions (05 section 3.1: exactly Camellia and Woljif) --------------------------------------------------------

REACTIONS = [
    reaction("Camellia", "jerribeth.trickster.reaction.camellia", (RETURNED,),
             '''{n}Camellia is arranging the dried flowers in her room. She does not look up.{/n}
"At the Sanctum I called her pinning a repugnant spectacle. And useful. Now she pins things in you."
{n}She snips a stem, considers it, and throws it away.{/n}
"Which did you want, Commander: the spectacle, or the use?"''',
             answer_list=CAMELLIA_HUB, forbids=("camellia.killed", "camellia.dead", "camellia.kicked_out", HOST),
             chapter=3, last=5, entry='"The Lady of the Sun is back."'),
    reaction("Camellia", "jerribeth.trickster.reaction.camellia_host", (RETURNED, HOST),
             '''{n}Camellia is arranging the dried flowers in her room. She does not look up.{/n}
"At the Sanctum I called her pinning a repugnant spectacle. And useful. Now she pins things in you. And you fed her a man."
{n}She snips a stem, considers it, and smiles at it.{/n}
"I would have chosen someone more interesting. Next time, ask me."''',
             answer_list=CAMELLIA_HUB, forbids=("camellia.killed", "camellia.dead", "camellia.kicked_out"),
             chapter=3, last=5, entry='"The Lady of the Sun is back."'),
    reaction("Woljif", "jerribeth.trickster.reaction.woljif", (MET_BY_TOAST,),
             '''"Chief. You drank to a demon's loyalty in front of the whole court of the crown, and now my ears itch."
{n}He scratches one, hard, and looks at his fingers as if he expects something to be on them.{/n}
"Tell me that's a coincidence. Go on. Lie to me, I'll feel better."''',
             answer_list=WOLJIF_HUB, forbids=("woljif.dead", "woljif.kicked_out", LEVY), chapter=5, last=5,
             entry='"About that toast..."'),
    reaction("Woljif", "jerribeth.trickster.reaction.woljif_levy", (MET_BY_TOAST, LEVY),
             '''"Chief. You drank to a demon's loyalty in front of half the Wintersun levy, and now my ears itch."
{n}He scratches one, hard, and looks at his fingers as if he expects something to be on them.{/n}
"Tell me that's a coincidence. Go on. Lie to me, I'll feel better."''',
             answer_list=WOLJIF_HUB, forbids=("woljif.dead", "woljif.kicked_out"), chapter=5, last=5,
             entry='"About that toast..."'),
]
SCENES.extend(REACTIONS)


# --- The registered route (jerribeth.py and its continuations) ----------------------------------------------------

JER08_DEFERRED = ("jerribeth.offered_signature", "jerribeth.borrowed_sun", "jerribeth.small_print",
                  "jerribeth.unsold_evening", "jerribeth.purchaser_answer", "jerribeth.counterfeit_guest",
                  "jerribeth.counterfeit_hinge", "jerribeth.counterfeit_clerk", "jerribeth.counterfeit_audience",
                  "jerribeth.counterfeit_spoil", "jerribeth.counterfeit_after")
# G6(b): lifted once she has returned. fate_envelope is not: it is her living body at Vellexia's manor.
RETURNING = ("jerribeth.ending_together", "jerribeth.ending_ascended", "jerribeth.ending_apart",
             "jerribeth.ending_unfinished", "jerribeth.counterfeit_guest", "jerribeth.counterfeit_hinge",
             "jerribeth.counterfeit_clerk", "jerribeth.counterfeit_audience", "jerribeth.counterfeit_spoil",
             "jerribeth.counterfeit_after", "jerribeth.fate_letter")
EXAMINE = '[Examine the charm, then deliberately invite a conversation.]'

INVITATION_NODES = [
    j("voice_tenant", '''{n}You do not remember wrapping the frame. The knot is yours. So, when you look closer, is the handwriting on the note: your own hand, slanted the way hers would slant it.{/n}
"You will write to me at the usual address, Commander. It is behind your left eye."
{n}A narrow, insectile silhouette gathers inside the dark surface, the shape she remembers having.{/n}
"The charm shows the form I wore. Do not be sentimental about it. I borrowed your hands for an hour last night to buy it, and you slept through the whole transaction."''',
      c('[Turn the frame over, wait, then invite her again.]', "test"),
      c('"Why seek my company?"', "why")),
    j("voice_toast", '''{n}The deserter from the tavern brought it himself, at dawn, and would not say who had sent him. He looked as if he did not know.{/n}
{n}A narrow, insectile silhouette appears inside the frame. The voice that reaches your thoughts is high and lightly buzzing, and you have heard it once before, out of the wrong mouth.{/n}
"You drank to me. Now I am writing to you. That is how debts begin, Commander."
"Try the cloth if you like. I would rather you knew the door works. A captive audience fidgets, and I do not waste my evenings on fidgeting."''',
      c('[Turn the frame over, wait, then invite her again.]', "toast_price"),
      c('"Why seek my company?"', "toast_price")),
    j("toast_price", '''"Before anything else. Strangers who drink to me pay for the privilege, and you are a stranger, Commander. We have never met. I have only been toasted."
{n}The silhouette tilts, reading you.{/n}
"The man who poured your cup lent me his mouth for a moment. He found it roomy. I should like to borrow him properly: a body that walks your halls when I cannot. Give me his name. Or give me something of yours instead: the night you drank to me. I shall keep it, and you will have toasted a stranger for nothing."''',
      c('[Give her the man\'s name] "Sergeant of the levy. He poured. He\'s yours."', "toast_given",
        alignment=("Evil", 1), flags=(TOAST_HOST,)),
      c('[Offer the night instead] "Take the toast. Leave him out of it."', "toast_paid", flags=(TOAST_MEMORY,)),
      c('[Refuse] "Nobody\'s name, and not my memories. I drank. That\'s all you get."', "toast_refused")),
    j("toast_given", '''"Thank you. He will not mind. He will not be in there to mind."
{n}The next morning the sergeant salutes you in the yard with a smile that is two finger-widths too wide. Nobody else notices. You will, every time.{/n}''',
      c('[Turn the frame over, wait, then invite her again.]', "test"),
      c('"Why seek my company?"', "why")),
    j("toast_paid", '''"Done."
{n}Something goes out of you, neatly, like a page cut from a ledger. You remember that there was a toast. You no longer remember raising the cup, or whose face was across the table, or why it seemed a good idea.{/n}
"Now we are even strangers. It is a better place to begin."''',
      c('[Turn the frame over, wait, then invite her again.]', "test"),
      c('"Why seek my company?"', "why")),
    j("toast_refused", '''"A toast for free. How very mortal."
{n}The silhouette turns, as if to go. Then it stops.{/n}
"No. I shall charge it to the future instead, with interest, and I shall decide the interest later. You may keep your sergeant and your memories, Commander. I shall keep a grudge. They are cheaper to store."''',
      c('[Turn the frame over, wait, then invite her again.]', "test"),
      c('"Why seek my company?"', "why")),
]

REFUGE_NODES = [
    j("left_need", '''"I left the manor. I am looking for another patron. You may spare me an expression of surprise that losing a powerful protector is inconvenient."''',
      c("Continue", "need")),
    j("left_anger", '''"I left the manor. I am looking for another patron. You may spare me an expression of surprise that losing a powerful protector is inconvenient."''',
      c("Continue", "anger")),
]
REFUGE_START = '''{n}Jerribeth answers from an image of bare darkness. She has made no effort to hide her irritation.{/n}
"Vellexia's protection has become a story people tell when deciding how much danger I am worth."
{n}Her voice buzzes harshly.{/n}
"Protection is a lease, Commander, and patronesses read their own small print. I read it too. I always do."'''

PRICE_NODES = [
    j("trust_tenant", '''"Trust. From a lodger."
{n}She says it inside your head, which is worse than the frame. Then she says something else: the name of your first friend, the smell of the kitchen where you grew up, the thing you said to yourself on the walls of Kenabres and have never repeated to anyone. Each one precise. Each one set down in front of you like a coin on a counter.{/n}
"You should not trust it. I have the run of the house, and I have been through every drawer. I could make you very unhappy with what I found, and I have not. Yet. Consider that my interest, stated in the only currency I respect."''',
      c('"Then stay out of the rooms I haven\'t rented you."', "terms_tenant", flags=("jerribeth.claimed_limit",)),
      c('"I want you out."', "evict")),
    j("terms_tenant", '''{n}The thought that is not yours goes very still.{/n}
"A clause. At last. You are learning."
{n}Something closes, softly, the way a door closes in a house at night. You could not say which door.{/n}
"The rooms you have not rented me stay shut. I will know if you lie to me about which ones those are."''',
      c("Continue", "terms")),
    j("evict", '''"You cannot. That is the whole beauty of a lease."
{n}The buzzing drops to something you feel in your teeth.{/n}
"But you may stop inviting me to talk. I will stay where I am, and pay my rent, and be quiet. You will find that the quiet is worse."''',
      c('[End the private relationship.]', flags=("jerribeth.closed",))),
]


def _evening_nodes():
    steps = [
        ("ev_host", (HOST,), _variant("ev_host", '''"I have hands now, of a sort. His hands. They are clumsy, and they are warm, and I have been practising what they can do with a cup, a knife and a lock. I thought you should know that before you decide what you want tonight."''')),
        ("ev_lodger", (LODGER,), _variant("ev_lodger", '''"You laughed in council this morning. That was me. The magister thought it was at him. It was not; it was at the magister's hat."''')),
        ("ev_vessel", (TENANT,), _variant("ev_vessel", '''"I have been sitting very still in my new house, looking out, and finding the view improves when you are in it. I dislike that it does."''')),
        ("ev_late", (LATE,), _variant("ev_late", '''"And do not think I have forgotten the terms. A lease signed that late I may void whenever it stops amusing me. Tonight it amuses me. Tomorrow is another rent day."''')),
    ]
    entry, nodes = ladder(steps, "want")
    head = j("tenant_evening", '''"You have it. Of course you have it. I live in it."
{n}The circle of lamplight in the frame is only for your benefit. The voice does not come from the frame at all.{/n}''', *entry)
    return [head, *nodes]


FUTURE_NODES = [
    j("her_terms", '''"Before you promise me anything."
{n}She lets the scenery go dark before you can admire it.{/n}
"I read contracts, Commander. Yours has a clause missing. What do I get if you break it?"''',
      c('[Name a forfeit] "One memory. Your choice of which, and when."', "start", flags=(FORFEIT,)),
      c('"Nothing. You have my word."', "blank"),
      c('"I cannot promise you a future together."', "part")),
    j("her_terms_short", '''"Before you promise me anything, even a short one."
{n}She lets the scenery go dark before you can admire it.{/n}
"I read contracts, Commander. Yours has a clause missing. What do I get if you break it?"''',
      c('[Name a forfeit] "One memory. Your choice of which, and when."', "short_future", flags=(FORFEIT,)),
      c('"Nothing. You have my word."', "blank"),
      c('"I cannot promise you a future together."', "part")),
    j("blank", '''{n}For a moment you hear only the hum of the charm.{/n}
"A Trickster's word. Keep it. It is the one thing of yours I will not take."
{n}Her antennae fold flat.{/n}
"You do know that making deals with demons is a losing game, yes? I have always known which side of it I sit on. There is no contract, Commander. I do not sign blank pages."''',
      c('[Let the silence stand.]', flags=("jerribeth.closed", NO_FORFEIT))),
]

# The forfeit is named, so the contract exists, and she collects on it in person the same night (Directive 12: the cut
# lands at the start of the act). Alive or toasted, she comes through the door by the road demons use; the tenant has no
# body to bring, so she builds one in the house she rents.
_KEEP = ('[Keep the next evening for her.]',)
IN_PERSON = [
    nar("arrival", '''{n}The frame goes dark and stays dark. You are reaching to turn it over when someone knocks at the door: three knocks, precisely spaced, the way a clerk knocks.{/n}
{n}She is on the threshold when you open it. Not an image. The lamplight finds the edges of her carapace and does not slide off them. She is taller than the frame ever let her look, and she smells of cold stone and something sweet and spoiled, like fruit left on an altar.{/n}''',
      c("Continue", "arrival_terms")),
    j("arrival_terms", '''"A forfeit is collected in person. I have come to see what I bought."
{n}She lifts her hand into the light: long, jointed, clawed at the tips, very still.{/n}
"The road demons use is short, if you do not mind what it smells of. I shall not stay the night; the Abyss notices when I am absent, and so will your guards. But I do not collect at a distance. Which face do you want across the table, Commander?"''',
      c('"Your own. All of it."', "own"),
      c('"The guise. I know who is wearing it."', "guise")),
    j("own", '''{n}She lets the last of the pretence fall away and steps inside, and the room is suddenly too small for her. Her antennae brush the lintel. Her wings, folded, rasp against the doorframe like pages turning.{/n}
"Most people close their eyes, the first time."
{n}You do not. She comes closer, one deliberate step at a time, and stops when there is no more room to stop. Her clawed fingers find the fastenings at your collar and undo them one by one, with the care she gave the locusts, and she watches your face the whole time to see what each one costs you.{/n}''',
      c("Continue", "ask")),
    j("guise", '''{n}The elven woman who steps inside is exactly the one the frame showed you, down to the seam of light along her jaw that she has left there on purpose, so that you will not forget.{/n}
"I made her for you. It seemed only fair that you should unwrap her."
{n}She takes your hands and sets them at her waist, where the illusion is warm and the thing beneath it is hard and ridged and moving under your palms. She watches you feel the difference. She enjoys it far more than the face would suggest.{/n}''',
      c("Continue", "ask")),
    j("ask", '''{n}She takes both your wrists, loosely, the way she once held a locust she had not yet decided to pin, and does not close her hand.{/n}
"I collect things that hold still, Commander. The ones that hold still for me, I keep. Let us find out which you are."''',
      c('[Give her your wrists.]', "threshold"),
      c('[Keep your hands, and pull her down to you.]', "threshold_free")),
    nar("threshold_free", '''{n}You take your hands back and put them on her instead: the ridge of her carapace, the cold hinge of a wing. She goes very still, and then the buzzing starts again, lower, and you realise it is a laugh.{/n}
"Oh," {n}she says.{/n} "You are going to be difficult. Good."
{n}She lets you pull her down. Her wings open over you both and shut out the lamp, and the sound you have only ever heard in your skull is in your skin now, everywhere she touches, and she lowers herself onto you.{/n}''',
      c("Continue", "morning_free")),
    nar("morning_free", '''{n}She is gone before the watch changes. Your wrists are unmarked. On the pillow lies one sliver of chitin, dark and glossy, prised from the edge of a wing by a hand that was not careful.{/n}
{n}Behind your left eye, something neat and patient is thinking very hard.{/n} "You kept your hands. Nobody keeps their hands. I shall have to find out why, and I shall enjoy the finding out. Keep the scale. It is the only one I have ever given away."''',
      c(_KEEP[0], "end", forbids=("jerribeth.short_future_chosen",), flags=("jerribeth.chosen_future",)),
      c(_KEEP[0], "short_end", requires=("jerribeth.short_future_chosen",))),
    nar("threshold", '''{n}You hold out your wrists. She takes them as if you had handed her something breakable and rare, and walks you backwards to the bed without once tightening her grip. Her mouth, or what serves her for one, is at your throat, and the buzzing you have only ever heard in your head is in your skin now, low and continuous, so that you cannot tell where the sound stops and the shiver starts.{/n}
{n}When your knees meet the edge of the mattress she lets you fall, and follows, and settles over you with her weight on her elbows and her wings half open, shutting out the lamp. Her claws close lightly round your wrists and press them into the blanket.{/n}
"Terms accepted," {n}she says, very softly, against your ear, and lowers herself onto you.{/n}''',
      c("Continue", "morning")),
    nar("morning", '''{n}She is gone before the watch changes. The sheets smell of cold stone. There are small crescents on your skin where her claws rested, very precise, as if she had counted them. You press a thumb to one. It stings, exactly as much as she meant it to, and you find you are in no hurry for it to heal.{/n}
{n}Tucked into the frame, where the image should be, is one dry locust wing, veined like a leaf and folded exactly in half. When you touch it, a voice that is not quite a memory arrives behind your left eye: "The forfeit stands. I have not decided which memory. You will be the second to know."{/n}''',
      c(_KEEP[0], "end", forbids=("jerribeth.short_future_chosen",), flags=("jerribeth.chosen_future",)),
      c(_KEEP[0], "short_end", requires=("jerribeth.short_future_chosen",))),
    j("tenant_room", '''"You cannot open a door to me, Commander. I live on the wrong side of it."
{n}The frame goes dark. The voice does not. It moves, instead: from behind your left eye to the back of your skull, and then, impossibly, down.{/n}
"So I shall do what I did in Wintersun. I shall build a room, and make you believe in it, and this time I shall be in it too."''',
      c("Continue", "tenant_host", requires=(HOST,)),
      c("Continue", "tenant_body", forbids=(HOST,))),
    j("tenant_host", '''"I could have come to you in the man from the stockade. His body is mine now; I stole it fairly, the way I steal everything. But then it would have been his face under your hands, and I have never once let a stolen thing take the credit for my work."''',
      c("Continue", "tenant_body")),
    nar("tenant_body", '''{n}The room she builds is your own, exactly, down to the crack in the ceiling. The only thing in it that is not yours is her, sitting on the edge of the bed in her own form, her carapace catching the light of a lamp that is not lit.{/n}
{n}You know she is not there. Your body does not. When her claws trace your jaw you feel every point of them, and when she leans down the buzzing is in your skin as well as your skull, low and continuous, so that you cannot tell where the sound stops and the shiver starts.{/n}
"I know where every nerve in this house runs," {n}she says.{/n} "I have been reading the plans for months."
"I shall not take your hands in here unless you give them. In this house, that is the only rule I keep."''',
      c('[Give her your wrists.]', "tenant_pinned"),
      c('[Reach for her instead.]', "tenant_free")),
    nar("tenant_pinned", '''{n}She pushes you back into a pillow that does not exist, settles her weight over you, pins your wrists where you offered them, and lowers herself onto you.{/n}''',
      c("Continue", "tenant_morning")),
    nar("tenant_free", '''{n}You reach for her, and she lets you find her, ridge and hinge and the cold edge of a wing, in a room that is only real because you both agree it is. She lowers herself onto you with a sound in your skull like pages turning very fast.{/n}''',
      c("Continue", "tenant_morning_free")),
    nar("tenant_morning_free", '''{n}You wake alone, as you went to sleep. Your hands still remember the shape of something that was never in the room.{/n}
{n}Behind your left eye, something neat and patient is unusually quiet. Then: "You reached. Tenants are not supposed to be reached for. I shall have to renegotiate."''',
      c(_KEEP[0], "end", forbids=("jerribeth.short_future_chosen",), flags=("jerribeth.chosen_future",)),
      c(_KEEP[0], "short_end", requires=("jerribeth.short_future_chosen",))),
    nar("tenant_morning", '''{n}You wake alone, as you went to sleep. There are no marks on your wrists. You can still feel exactly where they would be.{/n}
{n}Behind your left eye, something neat and patient is very pleased with itself.{/n} "Rent received. The forfeit stands. Pay on time, Commander. I have been told I am a very demanding landlady, and I intend to prove it."''',
      c(_KEEP[0], "end", forbids=("jerribeth.short_future_chosen",), flags=("jerribeth.chosen_future",)),
      c(_KEEP[0], "short_end", requires=("jerribeth.short_future_chosen",))),
]

# JER-08 (rest budget, Trickster full roster): the purchaser/counteroffer campaign (offered_signature and the ten letters
# that chain from it) does not open on a Trickster run; a save already inside it continues. A Commander who met her only
# through the Chapter 5 toast has one chapter left: the courtship ends at the promise, and the endings take it from there.
TRICKSTER_CAMPAIGN_ENTRY = "jerribeth.offered_signature"
LATE_ENTRY_CUT = ("jerribeth.ordinary", "jerribeth.farewell_review", "jerribeth.another_evening", "jerribeth.farewell",
                  # these read things only a Commander who met her in Chapters 3-4 has seen (her Xanthir, her refuge)
                  "jerribeth.collection", "jerribeth.refuge", "jerribeth.patron")


def _scene(by_id, id):
    if id not in by_id:
        raise ValueError("Jerribeth Trickster integration missing scene: " + id)
    return by_id[id]


def _node(scene_, id):
    return next(x for x in scene_["Nodes"] if x["Id"] == id)


def _gate(choice, forbids=(), requires=()):
    choice["Forbids"] = [*choice["Forbids"], *[f for f in forbids if f not in choice["Forbids"]]]
    choice["Requires"] = [*choice["Requires"], *[r for r in requires if r not in choice["Requires"]]]


def integrate(payload):
    """Save-safe edits to the registered route: no id, node or choice is renamed, removed or reordered. New choices are
    appended; the choices they replace on a Trickster run are gated off."""
    rel = payload["Relationships"]["jerribeth"]
    rel.setdefault("UnavailableOverrides", {}).update(RELATIONSHIP_PATCH["UnavailableOverrides"])
    rel["TricksterAccess"] = {k: dict(v) for k, v in RELATIONSHIP_PATCH["TricksterAccess"].items()}
    rel["Guidance"] += (" On the Trickster path, a Jerribeth killed in the Ivory Sanctum may keep a lease in the "
                        "Commander's head; a Commander who never met her may still drink to her.")
    for key, cues in SEEN_CUES.items():
        payload.setdefault("SeenCues", {})[key] = list(cues)
    for key, answer in SELECTED_ANSWERS.items():
        payload.setdefault("SelectedAnswers", {})[key] = answer
    for key, groups in DERIVED.items():
        payload.setdefault("Derived", {})[key] = [list(g) for g in groups]
    payload["PermanentEtudes"] = sorted(set(payload.get("PermanentEtudes", [])) | set(PERMANENT))
    by_id = {s["Id"]: s for s in payload["Scenes"]}

    # Edit 1: the invitation opens for a Commander who met her at the Sanctum or drank to her.
    invitation = _scene(by_id, "jerribeth.invitation")
    invitation["Requires"] = [r for r in invitation["Requires"] if r != "jerribeth.met"]
    invitation["RequiresAny"] = ["jerribeth.met", MET_BY_TOAST]
    start = _node(invitation, "start")
    _gate(start["Choices"][0], forbids=(RETURNED, MET_BY_TOAST))
    start["Choices"].append(c(EXAMINE, "voice_tenant", requires=(RETURNED,)))
    start["Choices"].append(c(EXAMINE, "voice_toast", requires=(MET_BY_TOAST,), forbids=(RETURNED,)))
    invitation["Nodes"].extend(INVITATION_NODES)

    # Edit 2 (COX, G5): the refuge gates on her own evidence; Vellexia's fate is a node variant.
    refuge = _scene(by_id, "jerribeth.refuge")
    refuge["Requires"] = [r for r in refuge["Requires"] if r != "jerribeth.patron_lost"]
    start = _node(refuge, "start")
    start["Text"] = REFUGE_START
    need, anger = start["Choices"]
    _gate(need, forbids=("jerribeth.patron_lost",))
    _gate(anger, forbids=("jerribeth.patron_lost",))
    start["Choices"].append(c(need["Text"], "left_need", requires=("jerribeth.patron_lost",)))
    start["Choices"].append(c(anger["Text"], "left_anger", requires=("jerribeth.patron_lost",)))
    refuge["Nodes"].extend(REFUGE_NODES)

    # Edit 3 (R2-1): on a Trickster run she names her terms before any promise; a promise without a forfeit is her no.
    future = _scene(by_id, "jerribeth.future")
    entry = _node(future, "future_entry")
    long_, short = entry["Choices"][0], entry["Choices"][1]
    _gate(long_, forbids=("trickster.ever",))
    _gate(short, forbids=("trickster.ever",))
    entry["Choices"].append(c(long_["Text"], "her_terms", requires=(*long_["Requires"], "trickster.ever"),
                              forbids=tuple(f for f in long_["Forbids"] if f != "trickster.ever")))
    entry["Choices"].append(c(short["Text"], "her_terms_short", requires=(*short["Requires"], "trickster.ever"),
                              forbids=tuple(f for f in short["Forbids"] if f != "trickster.ever")))
    future["Nodes"].extend(FUTURE_NODES)
    # The committing answers of a Trickster contract (a named forfeit) lead to her visit; the originals serve every
    # other run.
    promise = _node(future, "promise")
    for choice in list(promise["Choices"]):
        _gate(choice, forbids=(FORFEIT,))
        promise["Choices"].append(c(choice["Text"], "arrival", requires=(FORFEIT,), forbids=(RETURNED,), flags=tuple(choice["Set"])))
        promise["Choices"].append(c(choice["Text"], "tenant_room", requires=(FORFEIT, RETURNED), flags=tuple(choice["Set"])))
    short_future = _node(future, "short_future")
    keep = short_future["Choices"][0]
    _gate(keep, forbids=(FORFEIT,))
    short_future["Choices"].append(c(keep["Text"], "arrival", requires=(FORFEIT,), forbids=(RETURNED,), flags=tuple(keep["Set"])))
    short_future["Choices"].append(c(keep["Text"], "tenant_room", requires=(FORFEIT, RETURNED), flags=tuple(keep["Set"])))
    future["Nodes"].extend(IN_PERSON)
    _scene(by_id, TRICKSTER_CAMPAIGN_ENTRY)["Forbids"].append("trickster.ever")
    for id in LATE_ENTRY_CUT:
        _scene(by_id, id)["Forbids"].append(MET_BY_TOAST)

    # Edit 4: price and evening know what she is to the Commander now.
    price = _scene(by_id, "jerribeth.price")
    start = _node(price, "start")
    for choice in start["Choices"]:
        _gate(choice, forbids=(TENANT,))
    start["Choices"].append(c('"Why should I trust the interest you show me?"', "trust_tenant", requires=(TENANT,)))
    price["Nodes"].extend(PRICE_NODES)
    evening = _scene(by_id, "jerribeth.evening")
    start = _node(evening, "start")
    _gate(start["Choices"][0], forbids=(TENANT,))
    start["Choices"].append(c('"You have it."', "tenant_evening", requires=(TENANT,)))
    evening["Nodes"].extend(_evening_nodes())

    # Edit 5 (JER-08): the Chapter 3 letters are the eight that carry the courtship; the rest wait for Chapter 4.
    for id in JER08_DEFERRED:
        s = _scene(by_id, id)
        s["Chapters"] = [4, 5]
        s["MinChapter"] = 4

    # G6(b), the late commit, and the Trickster paragraphs on the endings that close her story.
    for id in RETURNING:
        _scene(by_id, id).setdefault("ForbidOverrides", {})[DEAD] = RETURNED
    unfinished = _scene(by_id, "jerribeth.ending_unfinished")
    unfinished["Forbids"].append(LATE_COMMITTED)
    for id in ("jerribeth.ending_together", "jerribeth.ending_ascended", "jerribeth.ending_apart"):
        for node in _scene(by_id, id)["Nodes"]:
            if all(ch.get("Next") is None for ch in node["Choices"]):
                node.setdefault("Paragraphs", []).extend(dict(x) for x in TRICKSTER_PARAGRAPHS)
                if id == "jerribeth.ending_apart":
                    node["Paragraphs"].append(dict(REFUSED_PARAGRAPH))
