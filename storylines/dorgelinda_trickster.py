"""Dorgelinda Stranglehold on the Trickster path: "Nothing's missing" (Writer/handoffs/trickster/dorgelinda-stranglehold.md;
family F16, "Spend it again, unnoticed").

Canon: the chair of the Logistics Council, a middle-aged dwarf with a black eye patch, claw scars and a hand "withered to
the bone" (Logistics_Officer/Cue_0001 b847706a, Cue_0013 4145e730). She tolerates "some skimmin' here and there, within
reason ... bless their grubby hands" (Logistics_2/Cue_0079 d723cd2d), and in Chapter 5 plans her own quiet theft: "just a
weight discrepancy here, some cargo that must have dried out or fallen off in transit there" (Logistics_6/Cue_0025
7ccd16a9). The Fellows of the Crusade run a black market (Logistics_3/Cue_0008 c3e25690), "lose" carts to vrocks
(Logistics_4/Cue_0001 10ccdfab) and are tried in Corporal Nickeld Bartley (Logistics_5/Cue_0001 7c5855fd), who stashed "a
whole warehouse worth of stolen goods ... near the city walls" (Cue_0074 753c00e6). Logistics_5 is Chapter 3.

F16 root: TricksterUseMagicDeviceTier2Feature 1383f215 "Reuse Magic Device": "use items so delicately that their use is
completely unnoticed." The Commander never conjures anything: a signature, witnessed, in her own ledger, makes the
missing stores the Commander's issue. She has no fate etude; the device makes an opportunity, and she prices it herself.
The route opens only through the Trickster audit; the continuation that makes it a full courtship is dorgelinda_ledger.
"""
from story_format import c, n, p, reaction, scene

SCENES = []
P = "dorgelinda.trickster."
UNIT = "8692bff6041c47a0b13158d5977f291b"      # RankUpOfficer_Logistics
DREZEN = "2570015799edf594daf2f076f2f975d8"
HUB = "fa57cf97ea01bf34e9a30f6ad444381e"       # Logistics_Officer/AnswersList_0003 (after Cue_0001 b847706a)
CARAVAN_LIST = "1f5aae1aab3b5b34ea3a0cbb1d0ca0b9"    # Logistics_4/AnswersList_0015 (the verdict list)
CARAVAN_RETURN = "3de8c946e5e8fca46bfd39dfd4f9aa61"  # Logistics_4/Cue_0029 "So which option are you going for?"
TRIBUNAL_LIST = "cba15a10b7929e44ca32745529948d0c"   # Logistics_5/AnswersList_0002 (the verdict list)
TRIBUNAL_RETURN = "647f755c8107d404a9ed894923d1d732" # Logistics_5/Cue_0029 "So what should we do?"
LANN_HUB = "66385ad77fa743e4bb1234078dbd804c"        # CompanionDialogues/Lann/AnswersList_0003
REGILL_HUB = "2366a8db6481070439fee222c0c52e45"      # CompanionDialogues/Regill/AnswersList_0002
KONOMI_HUB = "0dc8b8604bb33c846a63f3eb62443674"      # Crusade/RankUps/Diplomacy/Diplomacy_Officer/AnswersList_0003

STARTED = "dorgelinda.started"
CLOSED = "dorgelinda.closed"
COMMITTED = "dorgelinda.committed"
PRESENT = "dorgelinda.present"
CARAVANS = "dorgelinda.caravans_known"
TRIBUNAL = "dorgelinda.fellows_tribunal"
HANGED_LANN = "dorgelinda.verdict_hanged_lann"
HANGED_WENDUAG = "dorgelinda.verdict_hanged_wenduag"
PRISON = "dorgelinda.verdict_prison"
HUSHED = "dorgelinda.verdict_hushed"
REDEEMED = "dorgelinda.verdict_redeemed"
HARD_MEASURES = "dorgelinda.hard_measures"
CONSCIENCE = "dorgelinda.conscience_kept"
PRIMED = P + "primed"
RETURNED = P + "returned"
COUNTED = P + "counted"
METHODS = P + "methods_heard"
CLEAN = P + "hands_clean"
DIRTY = P + "hands_dirty"
DECLINED = P + "declined"
CARTS = P + "cost.carts_signed"
LATE = P + "cost.late"
AUDIT = P + "cost.audit"
ABYSS = P + "cost.abyss_signed"
CONFESSED = P + "cost.confessed"
BOOTS_OWED = P + "cost.boots_owed"
HOSTILE = P + "cost.audit_hostile"
TWICE = P + "cost.twice_weekly"
LINE_OPEN = P + "cost.line_open"
BOOTS_PAID = P + "cost.boots_paid"
TOLD_ALL = P + "cost.told_all"

RELATIONSHIP = dict(
    Title="A thorough audit",
    Description=("Dorgelinda Stranglehold has opened a line in her stores ledger in my name, for everything I claimed was "
                 "\"used, quietly\". She means to audit it until she knows where it went."),
    Objective="Account for yourself to Dorgelinda",
    Guidance=("On the Trickster path, sign for the Fellows' losses in Dorgelinda's own ledger: at the Logistics Council's "
              "caravan meeting, at Corporal Bartley's tribunal, or, if the tribunal never came, under her Chapter 5 "
              "shortages. Afterwards visit her office in Drezen and let her audit you. Leave a day or two between visits."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED, UnavailableFlags=["swarm"], FailureFlags=[],
    UnavailableOverrides={},
    TricksterAccess={
        CARAVANS: dict(detect=[CARAVANS], device=P + "caravans.countersign", returned=RETURNED),
        TRIBUNAL: dict(detect=[TRIBUNAL], device=P + "tribunal.recount", returned=RETURNED),
        PRESENT: dict(detect=[PRESENT, "chapter_later"], device=P + "office.stocktake", returned=RETURNED),
    },
)

# Keys only this route reads (the rest are bound on demand by trickster_world from the matrix).
SEEN_CUES = {
    HUSHED: ["76349e9bb678de3468e70c87c8e777ae"],        # Logistics_5/Cue_0045 (Woljif's verdict: hushed up, sent away)
    REDEEMED: ["75690b4f1e8fa734b8699b454c9137d2"],      # Logistics_5/Cue_0046 (Arueshalae's verdict: a chance to atone)
}
DERIVED = {P + "late_committed": [["trickster.ever", METHODS]]}
RENAMED = {"dorgelinda.weekly_count": P + "after.weekly_count", "dorgelinda.fellows_methods": P + "after.fellows_methods",
           "dorgelinda.commit": P + "after.commit", "dorgelinda.ending_committed": P + "epilogue.committed"}


def d(id, text, *choices, **kw):
    return n(id, "Dorgelinda", text, *choices, portrait="Dorgelinda", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, portrait="Dorgelinda", **kw)


def office(id, title, entry, nodes, requires, forbids=(), delay=0, chapters=(3, 5), **extra):
    """A physical scene at her own desk in Drezen: her Logistics_Officer answer list, with her unit present."""
    SCENES.append(scene(id, title, "Dorgelinda", min(chapters), entry, nodes, requires=requires,
                        forbids=(CLOSED, *forbids), delay=delay, last=max(chapters), optional=True,
                        Relationship="dorgelinda", Chapters=list(chapters), AnswerLists=[HUB], ContactUnit=UNIT,
                        Areas=[DREZEN], **extra))


# --- State 0: the lost carts (Chapter 3, Logistics_4). The primer, before the tribunal it answers. ----------------------

SCENES.append(scene(P + "caravans.countersign", "The lost carts", "Dorgelinda", 3,
    '[Sign for the lost carts yourself] "Enter every cart a vrock \'carried off\' to my account, Quartermaster. Issued to the Commander, for operations."',
    [d("sign", '''{n}Her eye stays on you a long moment, red-rimmed from nights on the job. Then she turns the ledger round and pushes the pen across the table, as if the council could not see her do it.{/n}
"Your account, your hand. I don't write other folks' debts. Bless their grubby hands, I've got enough of those already."
{n}Across the table someone laughs and turns it into a cough.{/n}''',
       c('[Write the line, and a rider under it: "...and all stores that follow them."]', "rider"),
       c('[Hand the pen back.] "On second thought, the vrock can keep them."')),
     d("rider", '''{n}She reads the rider aloud, flatly, the way she reads a manifest, and blots it with the heel of her bad hand.{/n}
"'...and all stores that follow them.' Your name. Your funeral, Commander." {n}She closes the book on it without reading it again.{/n}
"Now. Which of these fine plans are we doin'?"''',
       c("[Return to the council.]", flags=(CARTS,)))],
    requires=("trickster", CARAVANS), forbids=(TRIBUNAL, CARTS), last=5, Chapters=[3],
    AnswerLists=[CARAVAN_LIST], NativeReturnCue=CARAVAN_RETURN,
    EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1), Relationship="dorgelinda"))


# --- State 1: the Fellows' tribunal (Chapter 3, Logistics_5): "Nothing's missing". A preface to the native verdict. ----

SCENES.append(scene(P + "tribunal.recount", "Nothing's missing", "Dorgelinda", 3,
    '[Count it again, slowly] "Quartermaster, count the stores again. Nothing\'s missing. It was used, quietly."',
    [nar("count", '''{n}Dorgelinda sends a clerk for the stores ledger. The tribunal waits. Bartley watches the door as if it might still be an exit.{/n}''',
         c("[Watch the clerk turn back three weeks.]", "count_prepared", requires=(CARTS,)),
         c("[Take the pen out of the clerk's hand.]", "count_late", forbids=(CARTS,))),
     nar("count_prepared", '''{n}The clerk comes back with the ledger open at a page three weeks old. Between two caravan manifests, in your hand, is the line about the lost carts, and under it the rider no clerk ever read to the end: "...and all stores that follow them: issued to the Commander, for operations." Every crate in the warehouse by the city walls followed them.{/n}''',
         c("[Turn the ledger toward her.]", "read_prepared")),
     d("read_prepared", '''{n}She reads it with her finger under the words, the way a child reads, the way a quartermaster reads a thing she has already signed off.{/n}
"I read every line in that book. Twice. I never read the end of that one."''',
       c("Continue", "audit")),
     nar("count_late", '''{n}The clerk comes back with the ledger and a different face. Nothing balances. You take the pen from his hand, in front of the whole tribunal, and write one line under today's date: "All stores unaccounted: issued to the Commander, for operations." The ink shines wet in the lamplight.{/n}''',
         c("[Turn the ledger toward her.]", "read_late")),
     d("read_late", '''{n}She does not touch the page. She looks at the ink, then at your hand, then at the tribunal watching your hand.{/n}
"That ink's wet, Commander. The whole tribunal watched you wet it."''',
       c("Continue", "audit")),
     d("audit", '''{n}Dorgelinda turns the ledger with her good hand and reads the line once more. Her one eye comes up slowly.{/n}
"Well. Either you're lyin' for these idiots, Commander, or you ate a warehouse. That leaves the beatin' of my quartermaster, and I can try a man for a beatin'."
{n}She shuts the book.{/n} "And the stores are struck off as issued. Your issue. When this is done, I'll be findin' out which it was."''',
       c("[Let her decide the rest with you.]", flags=(PRIMED, AUDIT), requires=(CARTS,), crusade=("Materials", -200)),
       c("[Let her decide the rest with you.]", flags=(PRIMED, AUDIT, LATE), forbids=(CARTS,), crusade=("Materials", -200)))],
    requires=("trickster", TRIBUNAL), forbids=(PRIMED,), last=5, Chapters=[3],
    AnswerLists=[TRIBUNAL_LIST], NativeReturnCue=TRIBUNAL_RETURN,
    EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1), Relationship="dorgelinda"))


# --- State 2: in office, no tribunal by Chapter 5: the stocktake. The object is her clerks' own Abyss issue. -----------

office(P + "office.stocktake", "Nothing's missing",
    '[Count it again, slowly] "Quartermaster, count the stores again. Nothing\'s missing. It was used, quietly."', [
    d("start", '''"Missin'? Commander, we're missin' the floor of the warehouse. Her Majesty squeezed Mendev dry to march on Iz, and what she left us, the Abyss had."
{n}The clerk counts anyway, aloud, while she drums the fingers of her good hand on the desk. Most of the shortage is the war's. One line is her clerks' own, dated the week your party left for the Abyss: four crates of cold-iron arrowheads and a wagon of salt pork, issued to the Commander's party, no receipt after.{/n}''',
      c('[Sign under the Abyss issue: "Received, and used, quietly. All of it."]', "sign")),
    d("sign", '''{n}She watches your hand move under the line, past the arrowheads, past the pork, down the whole long column of what is not there. Her grip tightens on the edge of the book.{/n}
"...So that's where it all went. Into the Abyss. Quietly. Nobody can audit the Abyss, and you know it."
{n}She draws a line under your signature and freezes the column.{/n} "Nothin' leaves my stores on your seal till I've counted you. I'll want to see how, anyway."''',
      c("[Leave her to her ledger.]", flags=(PRIMED, AUDIT, ABYSS), crusade=("Materials", -100))),
], requires=("trickster", PRESENT), forbids=(TRIBUNAL, PRIMED), chapters=(5,),
   EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1))


# --- The return beat, shared by all three states: she opens the audit (48 h after the device). ----------------------

TALK = [
    c('"I lied. They were ours, and I wasn\'t going to hang them for bread."', "terms", flags=(CONFESSED,)),
    c('"It was used. Quietly. Audit me as long as you like."', "terms", flags=(BOOTS_OWED,)),
    c('[Intimidate] "You\'ll close that book, Quartermaster."',
      check=dict(Skill="CheckIntimidate", DC=30, Success="shut", Failure="refused", CommanderOnly=True)),
]
PATH = [
    c("Continue", "path_carts", requires=(CARTS,)),
    c("Continue", "path_late", requires=(LATE,)),
    c("Continue", "path_abyss", requires=(ABYSS,)),
    c("Continue", "path_plain", forbids=(CARTS, LATE, ABYSS)),
]

office(P + "audit.open", "A thorough audit", '"You said you\'d be findin\' out."', [
    d("start", '''"I counted it again. Slowly. Then I counted the Commander's boots, rations, blankets and bottles, and you've drawn about enough for {mf|a man|a woman} and a half."
{n}She lays the ledger open between you, one hand flat on the page. The other lies in her lap where it always lies, the fingers curled like dry roots.{/n}
"So where's it gone? One eye, one good hand, a lifetime of hard postin's. I don't tear up paperwork, Commander."''',
      c("Continue", "verdict_hanged", requires=(HANGED_LANN,)),
      c("Continue", "verdict_hanged", requires=(HANGED_WENDUAG,), forbids=(HANGED_LANN,)),
      c("Continue", "verdict_prison", requires=(PRISON,), forbids=(HANGED_LANN, HANGED_WENDUAG)),
      c("Continue", "verdict_hushed", requires=(HUSHED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON)),
      c("Continue", "verdict_redeemed", requires=(REDEEMED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED)),
      c("Continue", "path", forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED, REDEEMED))),
    d("verdict_hanged", '''"You lied the stores clean for them and then hanged them anyway. I stood under that gallows with the rest of the ranks, Commander. I'd like to know what the lie was for, if it wasn't for their necks."''',
      c("Continue", "path")),
    d("verdict_prison", '''"You gave me the sentence I asked for. Chains to Nerosyan and no rope. Don't think that buys you a lighter audit. It buys you the chair you're sittin' in."''',
      c("Continue", "path")),
    d("verdict_hushed", '''"And then you shipped the lot of them off to some fort at the end of the world and let Woljif tell the ranks they 'escaped'. So now I've got a warehouse of stores that walked, and a dozen soldiers that walked after it. Tidy."''',
      c("Continue", "path")),
    d("verdict_redeemed", '''"And then you let them work it off. Bartley's diggin' latrines by the east wall and singin' while he does it, which I'll grant is a punishment for the rest of us."''',
      c("Continue", "path")),
    nar("path", '''{n}She taps the line in your name with one blunt fingernail, twice.{/n}''', *PATH),
    d("path_carts", '''"Three weeks. Your name sat in my book for three weeks, under the carts a vrock 'carried off', and I read past it every mornin'. So you knew. Before the tribunal, before Bartley, before any of it. Talk."''', *TALK),
    d("path_late", '''"You signed my ledger in front of a tribunal with the ink still wet. I've seen braver lies. Not many. Talk."''', *TALK),
    d("path_abyss", '''"You signed under my shortages like a {mf|man|woman} signs for {mf|his|her} own boots. Nobody signs for the Abyss. You did. Talk."''', *TALK),
    d("path_plain", '''"Your name's in my book over stores nobody else would touch. Talk."''', *TALK),
    d("shut", '''{n}She closes the book. She stands, and salutes, and there is nothing in her face at all.{/n}
"Commander."''',
      c("[Leave her office.]", flags=(CLOSED,))),
    d("refused", '''"No." {n}The book stays open. Her hand stays on it.{/n}
"You can shout at the page if you like. It'll still be here when you've done. Paper's patient. So am I, when I'm owed."''',
      c("[Hear her out.]", "terms", flags=(HOSTILE,))),
    d("terms", '''"Right. Here's how it'll go. You come by the stores once a week, on your own feet, and you account for yourself. If I like the accountin', maybe I'll let you buy me a drink out of what you owe."
{n}It is not a smile. It is where one would go.{/n}''',
      c("[Agree to be audited.]", flags=(RETURNED, STARTED), forbids=(LATE,)),
      c("[Agree to be audited. Twice a week.]", "twice", requires=(LATE,))),
    d("twice", '''"Twice a week, for you. Wet ink costs extra."''',
      c("[Agree.]", flags=(RETURNED, STARTED, TWICE))),
], requires=("trickster.ever", PRIMED, PRESENT), forbids=(RETURNED,), delay=48)


# --- The test beat: the weekly count, the grudging drink and her one refusal. -----------------------------------------

COUNT_CHOICES = (
    c("[Account for yourself.]", "drink"),
    c('"Close the line, Quartermaster. Name the sum and I\'ll pay it tonight."', "no"),
)

office(P + "after.weekly_count", "Weekly count", '"Right on time. Boots off the table."', [
    nar("door", '''{n}Her office smells of lamp oil, wet wool and the ink her clerks mix too thin. The ledger is already open.{/n}''',
        c("Continue", "count_cold", requires=(HOSTILE,)),
        c("Continue", "count_twice", requires=(TWICE,), forbids=(HOSTILE,)),
        c("Continue", "count", forbids=(HOSTILE, TWICE))),
    d("count_cold", '''{n}She does not look up at all today. The last time you were here, you told her to close the book, and the book is still open.{/n}
"Sit. Line thirty-one. Two pairs of boots drawn in a week. Either you're walkin' to the Worldwound twice or you're givin' them away. Which?"''', *COUNT_CHOICES),
    d("count_twice", '''"Second time this week. I've started keepin' your chair warm, which is a waste of a good chair."
{n}She counts your kit the way she counts a wagon: aloud, without looking up. Boots. Blankets. One flask, not regulation.{/n}
"Line thirty-one. Two pairs of boots drawn in a week. Either you're walkin' to the Worldwound twice or you're givin' them away. Which?"''', *COUNT_CHOICES),
    d("count", '''{n}She has your column open before you sit. She counts your kit the way she counts a wagon: aloud, without looking up. Boots. Blankets. One flask, not regulation.{/n}
"Line thirty-one. Two pairs of boots drawn in a week. Either you're walkin' to the Worldwound twice or you're givin' them away. Which?"''', *COUNT_CHOICES),
    d("drink", '''{n}You account for the boots, and the flask, and a blanket you cannot account for. She writes it all down. Then she reaches under the table for a bottle that has never appeared on any manifest in Drezen.{/n}
"On account." {n}She pours two, and pushes one across with the back of her bad hand.{/n} "Don't make a face. It's the good stuff. I found it, which is different from stealin' it, which I'd know."''',
      c("[Drink with her.]", flags=(COUNTED, P + "drank"))),
    d("no", '''"No." {n}She says it the way she says "two out of three": as a fact of supply.{/n}
"You don't get to buy your way out of my book, Commander. Coin's the easy part. The line stays open till I know where it went, and I close it, not you."
{n}She pours a drink anyway, one, for herself, and after a moment a second, for you.{/n} "That's not forgiveness. That's hospitality. Different column."''',
      c("[Take the refusal and the cup.]", flags=(COUNTED, LINE_OPEN))),
], requires=("trickster.ever", RETURNED), forbids=(COUNTED,), delay=48)


# --- The pivotal beat (Chapter 5): the Fellows' second book. ------------------------------------------------------------

office(P + "after.fellows_methods", "The second book", '"Shut the door. No, all the way."', [
    nar("door", '''{n}She waits until the latch has caught, then waits again until the footsteps in the corridor have gone past. Outside, a supply sergeant is shouting at a cart that will not shout back.{/n}''',
        c("Continue", "measures", requires=(HARD_MEASURES,)),
        c("Continue", "conscience", requires=(CONSCIENCE,), forbids=(HARD_MEASURES,)),
        c("Continue", "crumbs", forbids=(HARD_MEASURES, CONSCIENCE))),
    d("measures", '''"I put it to you at the council already. Requisitions. Donations for the war of faith." {n}Her voice goes flat on the word.{/n} "I'm puttin' something worse to you now, here, where nobody's takin' minutes."''',
      c("Continue", "start")),
    d("conscience", '''"You were right, at the council. You wouldn't turn us into the Fellows of the Crusade, and I hate that you were right, because it means I'm still the one short of everythin'. Hear me anyway."''',
      c("Continue", "start")),
    d("crumbs", '''"Her Majesty squeezed Mendev dry to march on Iz. There's nothin' left to buy honest. I checked. Twice. Then I stopped checkin', 'cause it was makin' me sick."''',
      c("Continue", "start")),
    d("start", '''{n}She lays a second ledger on top of the first. It is thinner, and older, and the hand in it is not hers.{/n}
"Bartley's lot kept this. Took it off his clerk. Two books, one for the Crusade and one for what the Crusade doesn't know it's got. A weight discrepancy here, some cargo that dried out there. I've read it three times. It's good work." {n}She taps the cover.{/n}
"You're the one person in Drezen I can say that to. You ate a warehouse and signed for it. So I'm askin' you. Do we keep a second book?"''',
      c('"Keep your hands clean. I\'ll keep mine dirty for both of us."', "clean"),
      c('"Do it. Their methods. Your books."', "dirty")),
    d("clean", '''{n}She looks at you for a long time with the one eye.{/n}
"That's a fool's bargain, Commander. You carry the dirt and I get to keep my hands." {n}She puts the thin book in the stove and watches it catch, the pages curling one after another like something that wants to live.{/n}
"I'll take it. Don't think I don't know what it cost."''',
      c("[Leave it there.]", flags=(METHODS, CLEAN))),
    d("dirty", '''"Their book. My hand." {n}She copies the first line into a fresh ledger, in a smaller script than her own. Her grip does not waver.{/n}
"Bless their grubby hands. They had a system. Now it's ours, and it'll be kept better than they ever kept it." {n}She does not look at you.{/n} "If this goes wrong, it's your name at the top. You're used to that."''',
      c("[Leave it there.]", flags=(METHODS, DIRTY), crusade=("Materials", 150), alignment=("Evil", 1))),
], requires=("trickster.ever", COUNTED), forbids=(METHODS,), delay=24, chapters=(5,))


# --- The commit (Chapter 5), with her refusal reachable on every branch. ------------------------------------------------

ASK = (
    c('"Keep the line open. And me in the book with it."', "yes", forbids=(BOOTS_OWED,)),
    c('[Set the last pair of boots on her desk.] "Keep the line open. And me in the book with it."', "yes_boots",
      requires=(BOOTS_OWED,)),
    c('"Before you answer: you still don\'t know where it all went."', "not_yet"),
)

office(P + "after.commit", "The open line", '"Sit. I\'ve got your column open."', [
    nar("open", '''{n}The ledger is open at your line. It has grown: carts, a warehouse, boots, a bottle that was never on any manifest. She has not closed it. She has not ruled it off.{/n}''',
        c("Continue", "recall_clean", requires=(CLEAN,)),
        c("Continue", "recall_dirty", requires=(DIRTY,), forbids=(CLEAN,)),
        c("Continue", "recall", forbids=(CLEAN, DIRTY))),
    d("recall_clean", '''"You kept your hands dirty so I didn't have to. I noticed. I notice everythin'. Eventually."''',
      c("Continue", "confessed", requires=(CONFESSED,)), c("Continue", "ask", forbids=(CONFESSED,))),
    d("recall_dirty", '''"And we kept their book. Better than they did. I don't know yet what that makes us, and I've stopped askin' at night."''',
      c("Continue", "confessed", requires=(CONFESSED,)), c("Continue", "ask", forbids=(CONFESSED,))),
    d("recall", '''"You've been through my stores like weather, Commander. I've written every bit of it down."''',
      c("Continue", "confessed", requires=(CONFESSED,)), c("Continue", "ask", forbids=(CONFESSED,))),
    d("confessed", '''"You told me the truth once, the day I opened the audit. I wrote it down. It's still in here, at the back. Unsent."''',
      c("Continue", "ask")),
    d("ask", '''"Every quartermaster I ever served under closed their books at the end of a campaign. Ruled it off, signed it, shipped it to Nerosyan. I've never once left a line open." {n}She turns the book so the line faces you.{/n}
"So. What d'you want me to do with it?"''', *ASK),
    d("yes", '''{n}She picks up the pen, and for a moment you think she will rule it off anyway. She writes the date instead, and under it, in her small hard hand: carried forward.{/n}
"Then it stays open. You'll account for yourself every week till one of us is dead, and I'll count every word."''',
      c("[Stay while she writes.]", flags=(COMMITTED,))),
    d("yes_boots", '''{n}She counts the boots: two, left and right, regulation, drawn today from the Crusade's own stores on your seal. She writes them in. The boots are paid.{/n}
"Paid in full. Took you long enough." {n}She does not rule the line off. She writes: carried forward.{/n} "Now there's nothin' left you owe me but yourself, and I'm not closin' that."''',
      c("[Stay while she writes.]", flags=(COMMITTED, BOOTS_PAID), crusade=("Materials", -200))),
    d("not_yet", '''"No, I don't." {n}She shuts the book, gently, which is worse than hard.{/n}
"And I'm not sayin' yes to a line I can't balance, Commander. Not today. Come back when you'll tell me where it went. All of it. Then ask me again."''',
      c("[Leave the ledger with her.]", flags=(DECLINED,))),
], requires=("trickster.ever", METHODS), forbids=(COMMITTED, DECLINED), delay=48, chapters=(5,))


# --- The one priced second ask after her soft no. -----------------------------------------------------------------------

office(P + "after.second_ask", "Where it went", '"You came back. Sit. Talk."', [
    d("price", '''"Where did it go. All of it. The carts, the warehouse, the Abyss. Every line." {n}The pen is already in her hand. She has turned to a clean page, which in her office is the closest thing to a courtesy.{/n}''',
      c("[Tell her everything, and let her strike it from the stores.]", "told", crusade=("Materials", -100)),
      c('"Not the warehouse. Anything else."', "no")),
    d("told", '''{n}You tell her. She writes all of it down, and strikes a hundred's worth of stores that were never really there. When you finish, the page balances for the first time since the caravans.{/n}
"There. Was that so hard." {n}She writes: carried forward.{/n} "Now ask."''',
      c("[Ask.]", flags=(COMMITTED, TOLD_ALL))),
    d("no", '''"Then we're done, Commander." {n}She rules a line under your column, the only line she has ever drawn in anger.{/n}
"I'll keep the book. Not you."''',
      c("[Go.]", flags=(CLOSED,))),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED,), delay=72, chapters=(5,))


# --- Epilogue pages (Owner DorgelindaEpilogue; ordered siblings; no effects). ------------------------------------------

EP = dict(last=6, Relationship="dorgelinda")
SCENES.append(scene(P + "epilogue.committed", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}The Logistics Council's last ledger balanced to the copper, save one line in the Commander's name, marked "used, quietly" and carried forward. Dorgelinda Stranglehold audited it every week for the rest of the Commander's life. She never ruled it off. When clerks asked why, she said it was the only account in the Crusade she had never finished counting, and that she did not intend to.{/n}''',
        paragraphs=(
            p("{n}Under the first entry, in the Commander's hand, was a rider nobody but she had ever read to the end: \"...and all stores that follow them.\" She followed them.{/n}", requires=(CARTS,)),
            p("{n}The boots were entered as paid. She kept the last pair on a shelf in the stores, regulation, unworn, and would not issue them to anyone.{/n}", requires=(BOOTS_PAID,)),
            p("{n}A confession sat in the back of the book, in her hand, never sent to Nerosyan.{/n}", any_groups=[[CONFESSED, TOLD_ALL]]),
        ))],
    requires=("trickster.ever", COMMITTED), forbids=("sacrifice", CLOSED),
    ForbidOverrides={"sacrifice": "trickster.cheated_death"}, **EP))

SCENES.append(scene(P + "epilogue.committed_on_record", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}When the Commander was entered as dead, Dorgelinda Stranglehold refused to close the account. "Dead's a status, not a balance," she told the clerk from Nerosyan. The line stayed open in her book for as long as she kept books, which was a very long time.{/n}''')],
    requires=("trickster.ever", COMMITTED, "sacrifice"), forbids=("trickster.cheated_death", CLOSED), **EP))

SCENES.append(scene(P + "epilogue.commit", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}The war ended before the audit did. The spring after Threshold, Dorgelinda Stranglehold came to the Commander with the Logistics Council's final ledger under her arm and one line still open in it. "I don't ship a book to Nerosyan with a hole in it," she said. "So. Either you close it, or you stay in it." She had already written "carried forward". She was not asking, much.{/n}''')],
    requires=("trickster.ever", METHODS), forbids=(COMMITTED, CLOSED, DECLINED), **EP))

SCENES.append(scene(P + "epilogue.declined", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}Dorgelinda Stranglehold shipped the Logistics Council's ledgers to Nerosyan after the war, all but one. The Commander's column she kept, unbalanced, on her own shelf. She had said to come back when the Commander would tell her where it all went. She kept the shelf clear, in case.{/n}''')],
    requires=("trickster.ever", DECLINED), forbids=(COMMITTED, CLOSED), **EP))


# --- Reactions: exactly Konomi, Regill and Lann, each behind its reactor's availability guard. ------------------------

LANN_GUARD = dict(forbids=("lann.dead", "lann.kicked_out", "lann.plot_absent"))
REGILL_GUARD = dict(forbids=("regill.dead", "regill.kicked_out", "regill.plot_absent"))

SCENES.append(reaction("Lann", "dorgelinda.react.lann.countersign", (CARTS, "trickster", "lann.in_party"),
    '''"You put the thieves' losses on your own name? Where I come from, whoever owns the stolen food is the one they blame when it runs out." {n}He scratches at the back of his neck.{/n} "I hope you know what you're buying."''',
    answer_list=LANN_HUB, forbids=(TRIBUNAL, *LANN_GUARD["forbids"]), chapter=3, last=5, portrait="Lann"))
SCENES.append(reaction("Regill", "dorgelinda.react.regill.countersign", (CARTS, "trickster", "regill.in_party"),
    '''"You signed for goods a vrock is said to have eaten. A knight of the Order who signed for contraband he had not seized would be stripped of his armour by nightfall. You have no armour to strip. I will watch what they take instead."''',
    answer_list=REGILL_HUB, forbids=(TRIBUNAL, *REGILL_GUARD["forbids"]), chapter=3, last=5, portrait="Regill"))
SCENES.append(reaction("Regill", "dorgelinda.react.regill.recount", (PRIMED, TRIBUNAL, "regill.in_party"),
    '''"A commander who signs for thieves and a quartermaster who reads past the signature. In the Order I would have both flogged. Only one of you can be." {n}He does not smile.{/n} "Promote her."''',
    answer_list=REGILL_HUB, forbids=REGILL_GUARD["forbids"], chapter=3, last=5, portrait="Regill"))
SCENES.append(reaction("Lann", "dorgelinda.react.lann.recount", (PRIMED, TRIBUNAL, "lann.in_party"),
    '''"You lied a whole warehouse clean for them. Next time some hungry recruit asks me why he shouldn't steal, I'm sending him to you. You can explain the difference. I can't."''',
    answer_list=LANN_HUB, forbids=LANN_GUARD["forbids"], chapter=3, last=5, portrait="Lann"))
SCENES.append(reaction("Regill", "dorgelinda.react.regill.stocktake", (PRIMED, "trickster", "regill.in_party"),
    '''"Four crates of cold iron issued to your party, and your signature under every shortage since. In the Order we call that a confession with the crime left blank. Your dwarf will fill it in. I would."''',
    answer_list=REGILL_HUB, forbids=(TRIBUNAL, *REGILL_GUARD["forbids"]), chapter=5, last=5, portrait="Regill"))
SCENES.append(reaction("Lann", "dorgelinda.react.lann.stocktake", (PRIMED, "trickster", "lann.in_party"),
    '''"Cold iron doesn't come back out of the Abyss. Neither did the salt pork. Neither did half of what she's missing, apparently." {n}He counts on his fingers, and gives up.{/n} "Funny how all of it fits under one signature."''',
    answer_list=LANN_HUB, forbids=(TRIBUNAL, *LANN_GUARD["forbids"]), chapter=5, last=5, portrait="Lann"))

# Konomi reads the minutes. A reaction is one node, so her tribunal and stocktake lines are two siblings.
KONOMI_GUARD = dict(forbids=("konomi.dismissed", "konomi.retained_dead"),
                    ForbidOverrides={"konomi.dismissed": "konomi.trickster.returned"})
# konomi.retained_dead is runtime-derived (it clears when she is raised), so it takes a plain Forbid, as elsewhere.
SCENES.append(reaction("Konomi", "dorgelinda.react.konomi.ledgers", (PRIMED, TRIBUNAL, "konomi.in_office"),
    '''"Your quartermaster's shortfall walked into your personal account, I hear. A warehouse, before a tribunal." {n}She opens her fan one fold.{/n} "The minutes will be very short and very careful. Nerosyan will want the ledgers, Commander. I have not yet decided whether to tell them where to look."''',
    answer_list=KONOMI_HUB, chapter=3, last=5, portrait="Konomi", **KONOMI_GUARD))
SCENES.append(reaction("Konomi", "dorgelinda.react.konomi.ledgers_abyss", (PRIMED, "konomi.in_office"),
    '''"Your quartermaster's shortfall walked into your personal account, I hear. Arrowheads, into the Abyss, on your signature." {n}She opens her fan one fold.{/n} "I have minuted it as 'lost to the enemy'. The enemy has not objected. Nerosyan will want the ledgers, Commander. I have not yet decided whether to tell them where to look."''',
    answer_list=KONOMI_HUB, chapter=5, last=5, portrait="Konomi",
    forbids=(TRIBUNAL, *KONOMI_GUARD["forbids"]), ForbidOverrides=KONOMI_GUARD["ForbidOverrides"]))


def integrate(payload):
    """Register the new relationship's own keys. Scenes are added by expansion.py; world keys bind on demand."""
    for key, cues in SEEN_CUES.items():
        have = payload.setdefault("SeenCues", {}).get(key)
        if have is not None and have != cues:
            raise ValueError("Conflicting binding: " + key)
        payload["SeenCues"][key] = list(cues)
    for key, groups in DERIVED.items():
        payload.setdefault("Derived", {})[key] = [list(g) for g in groups]
