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
# Authored F16 extension: a witnessed issue signature assumes responsibility for supplies.
# Reuse Magic Device supplies the analogy, not legal acquittal or compelled affection.
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
REVIEW = P + "cost.tribunal_books"     # Q9 (Sol INT): the Ch5 signing under the closed tribunal's shortfall (recount missed)
HANGED = "dorgelinda.verdict_hanged"   # derived: either hanging verdict

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
COLD_UNMENDED = "dorgelinda.ledger.cold_unmended"
COMMITMENT_FORBIDS = ["dorgelinda.ledger.quarrel_unmended", COLD_UNMENDED]
DERIVED_FORBIDS = {
    COLD_UNMENDED: ["dorgelinda.ledger.quarrel_mended"],
    "dorgelinda.outcome.accepted": COMMITMENT_FORBIDS,
    P + "late_committed": COMMITMENT_FORBIDS,
    "dorgelinda.harem.eligible": COMMITMENT_FORBIDS,
}

# Commitment records history; current readers withhold intimacy while the seal quarrel stands.
DERIVED = {COLD_UNMENDED: [["dorgelinda.ledger.quarrel_cold"]],
           P + "late_committed": [["trickster.ever", COMMITTED, "dorgelinda.outcome.accepted"]],
           "dorgelinda.outcome.accepted": [[COMMITTED]], HANGED: [[HANGED_LANN], [HANGED_WENDUAG]]}
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
    [d("sign", '''{n}Her eye stays on you, red-rimmed from nights on the job, while she works out what this will cost her. Then she turns the ledger round and pushes the pen across the table, as if the council could not see her do it.{/n}
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
         c("[Watch the clerk turn back to the caravan pages.]", "count_prepared", requires=(CARTS,)),
         c("[Take the pen out of the clerk's hand.]", "count_late", forbids=(CARTS,))),
     nar("count_prepared", '''{n}The clerk comes back with the ledger open at the caravan pages, weeks back. Between two caravan manifests, in your hand, is the line about the lost carts, and under it the rider no clerk ever read to the end: "...and all stores that follow them: issued to the Commander, for operations." Every crate in the warehouse by the city walls followed them.{/n}''',
         c("[Turn the ledger toward her.]", "read_prepared")),
     d("read_prepared", '''{n}She reads it with her finger under the words, the way a child reads, the way a quartermaster reads a thing she has already signed off.{/n}
"I read every line in that book. Twice. I read that one. I never thought what you'd shove under it."''',
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
    d("start", '''"Your party's Abyss issue. Arrowheads and salt pork. No receipt." {n}She opens the ledger at the week you left. A clerk sets the current council returns alongside it; she pushes them aside to expose the unexplained issue.{/n} "The war's losses are in those returns. This line's yours. Account for it."''',
      c('[Sign under the Abyss issue: "Received, and used, quietly. All of it."]', "sign")),
    d("sign", '''{n}She watches your hand move under the line, past the arrowheads, past the pork, down the whole long column of what is not there. Her grip tightens on the edge of the book.{/n}
"...So that's where it all went. Into the Abyss. Quietly. Nobody can audit the Abyss, and you know it."
{n}She draws a line under your signature and freezes the column.{/n} "Nothin' leaves my stores on your seal till I've counted you. I'll want to see how, anyway."''',
      c("[Leave her to her ledger.]", flags=(PRIMED, AUDIT, ABYSS), crusade=("Materials", -100))),
], requires=("trickster", PRESENT), forbids=(TRIBUNAL, PRIMED), chapters=(5,),
   EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1))


# --- State 1b (Chapter 5): the tribunal sat in Chapter 3 and the recount was never asked for. The Fellows' books are
# closed on a verdict; what they sold is still a hole with no name under it. The Commander signs under it, late. ------

BOOKS_VERDICT = [
    c("Continue", "hanged", requires=(HANGED,)),
    c("Continue", "prison", requires=(PRISON,), forbids=(HANGED,)),
    c("Continue", "hushed", requires=(HUSHED,), forbids=(HANGED, PRISON)),
    c("Continue", "redeemed", requires=(REDEEMED,), forbids=(HANGED, PRISON, HUSHED)),
    c("Continue", "sat", forbids=(HANGED, PRISON, HUSHED, REDEEMED)),
]

office(P + "office.tribunal_books", "The Fellows' books",
    '[Ask after the Fellows\' accounts] "The tribunal\'s books, Quartermaster. Did they ever balance?"', [
    d("start", '''"Balance?" {n}She bends, grunting, and hauls a crate out from under the desk with her good hand. Ledgers, tally boards, a corporal's pay book with the cover torn off.{/n} "That's the Fellows of the Crusade, Commander. All of 'em I could find. It's been sittin' under my feet since the tribunal, waitin' for Nerosyan to ask."''', *BOOKS_VERDICT),
    d("hanged", '''"We executed the ones the tribunal wanted dead. I saw it done. And the salt pork they sold off to the sutlers is still sold. An execution doesn't buy back a single barrel."''',
      c("Continue", "hole")),
    d("prison", '''"Bartley's lot are on the road to Nerosyan or past it, in the chains I asked for. And the salt pork they sold off to the sutlers is still sold. Chains don't buy back a single barrel."''',
      c("Continue", "hole")),
    d("hushed", '''"Bartley's lot are at some fort at the end of the world, and Woljif's still tellin' the ranks they escaped. And the salt pork they sold off to the sutlers is still sold. A good story doesn't buy back a single barrel."''',
      c("Continue", "hole")),
    d("redeemed", '''"Bartley's diggin' latrines by the east wall and his lads are carryin' crates for nothin'. Fine. And the salt pork they sold off to the sutlers is still sold. A shovel doesn't buy back a single barrel."''',
      c("Continue", "hole")),
    d("sat", '''"The tribunal sat, and said its piece, and went off to its supper. And the salt pork the Fellows sold off to the sutlers is still sold. Talk doesn't buy back a single barrel."''',
      c("Continue", "hole")),
    d("hole", '''{n}She opens the top ledger at a page ruled in red: what the warehouse by the walls gave back, and under it, longer, what it did not.{/n}
"Nerosyan wants a name at the foot of that. I'll give 'em the Fellows'. Thieves, it'll say, and that's the last word anybody writes about men who fought on the walls." {n}She holds the pen over the page and does not write.{/n} "Unless somebody's got a better name."''',
      c('[Take the pen. Before her clerks, write under the red column: "Issued to the Commander, for operations. Used, quietly."]', "sign"),
      c('"Write the Fellows. It\'s what they did."', "leave")),
    d("leave", '''"Aye. It is." {n}She writes nothing yet. She shoves the crate back under the desk with her boot.{/n} "It'll keep till Nerosyan asks. Most things do, down here."''',
      c("[Leave her to it.]", abort=True)),
    d("sign", '''{n}Three clerks stop writing. The one by the door forgets to breathe. She watches your hand go down the whole red column, and does not stop it, and does not help.{/n}
"That's wet ink, Commander, and it's months late, and my clerks just watched you wet it." {n}She turns the book to the lamp and reads your line twice.{/n} "The tribunal's done. There's no neck on the end of this. So either you're lyin' for somethin' I can't see yet, or you ate the lot." {n}She shuts the ledger on your name.{/n} "I'll be findin' out which."''',
      c("[Leave her to her ledger.]", flags=(PRIMED, AUDIT, LATE, REVIEW), crusade=("Materials", -100))),
], requires=("trickster", TRIBUNAL, PRESENT), forbids=(PRIMED,), chapters=(5,),
   EntryMythic="PlayerIsTrickster", EntryAlignment=dict(Direction="Chaotic", Value=1))


# --- The return beat, shared by all three states: she opens the audit (48 h after the device). ----------------------

TALK = [
    c('"I lied. They were ours, and I wasn\'t going to hang them for bread."', "terms", flags=(CONFESSED,)),
    c('"It was used. Quietly. Audit me as long as you like."', "terms", flags=(BOOTS_OWED,)),
    c('[Intimidate] "You\'ll close that book, Quartermaster."',
      check=dict(Skill="CheckIntimidate", DC=30, Success="shut", Failure="refused", CommanderOnly=True)),
]
TALK_LATE = [
    c('"I signed for a shortage I never used. I\'d rather the blame sat on me than on them."', "terms", flags=(CONFESSED,)),
] + TALK[1:]
PATH = [
    c("Continue", "path_carts", requires=(CARTS,), forbids=(REVIEW, ABYSS)),
    c("Continue", "path_late", requires=(LATE,), forbids=(REVIEW,)),
    c("Continue", "path_abyss", requires=(ABYSS,)),
    c("Continue", "path_plain", forbids=(CARTS, LATE, ABYSS)),
    c("Continue", "path_review", requires=(REVIEW,)),
]

office(P + "audit.open", "A thorough audit", '"You said you\'d be findin\' out."', [
    d("start", '''"I counted it again. Slowly. Then I counted the Commander's boots, rations, blankets and bottles, and you've drawn about enough for {mf|a man|a woman} and a half."
{n}She lays the ledger open between you, one hand flat on the page. The other lies in her lap where it always lies, the fingers curled like dry roots.{/n}
"So where's it gone? One eye, one good hand, a lifetime of hard postin's. I don't tear up paperwork, Commander."''',
      c("Continue", "verdict_hanged", requires=(HANGED_LANN,), forbids=(REVIEW,)),
      c("Continue", "verdict_hanged", requires=(HANGED_WENDUAG,), forbids=(HANGED_LANN, REVIEW)),
      c("Continue", "verdict_prison", requires=(PRISON,), forbids=(HANGED_LANN, HANGED_WENDUAG, REVIEW)),
      c("Continue", "verdict_hushed", requires=(HUSHED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, REVIEW)),
      c("Continue", "verdict_redeemed", requires=(REDEEMED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED, REVIEW)),
      c("Continue", "path", forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED, REDEEMED, REVIEW)),
      c("Continue", "path", requires=(REVIEW,))),
    d("verdict_hanged", '''"You lied the stores clean for them and then had them executed anyway. I stood with the rest of the ranks and watched it done, Commander. I'd like to know what the lie was for, if it wasn't for their necks."''',
      c("Continue", "path")),
    d("verdict_prison", '''"You gave me the sentence I asked for. Chains to Nerosyan and no rope. Don't think that buys you a lighter audit. It buys you the chair you're sittin' in."''',
      c("Continue", "path")),
    d("verdict_hushed", '''"And then you shipped the lot of them off to some fort at the end of the world and let Woljif tell the ranks they 'escaped'. So now I've got a warehouse of stores that walked, and a dozen soldiers that walked after it. Tidy."''',
      c("Continue", "path")),
    d("verdict_redeemed", '''"And then you let them work it off. Bartley's diggin' latrines by the east wall and singin' while he does it, which I'll grant is a punishment for the rest of us."''',
      c("Continue", "path")),
    nar("path", '''{n}She taps the line in your name with one blunt fingernail, twice.{/n}''', *PATH),
    d("path_carts", '''"Your name was already in my book, under the carts a vrock 'carried off', and I read past it every mornin'. So you knew, before I knew how much those drivers had lost. Talk."''', *TALK),
    d("path_late", '''"You signed my ledger in front of a tribunal with the ink still wet. I've seen braver lies. Not many. Talk."''', *TALK),
    d("path_abyss", '''"You signed under my shortages like a {mf|man|woman} signs for {mf|his|her} own boots. Nobody signs for the Abyss. You did. Talk."''', *TALK_LATE),
    d("path_plain", '''"Your name's in my book over stores nobody else would touch. Talk."''', *TALK),
    d("path_review", '''"You signed under the Fellows' red column months after the tribunal was done, with my clerks gawpin', for no man's neck at all. I've seen braver lies. I've never seen a stranger one. Talk."''', *TALK_LATE),
    d("shut", '''{n}She closes the book. She stands, and salutes, and there is nothing in her face at all.{/n}
"Commander."''',
      c("[Leave her office.]", flags=(CLOSED,))),
    d("refused", '''"No." {n}The book stays open. Her hand stays on it.{/n}
"You can shout at the page if you like. It'll still be here when you've done. Paper's patient. So am I, when I'm owed."''',
      c("[Hear her out.]", "terms", flags=(HOSTILE,))),
    d("terms", '''{n}She listens without writing. When you have finished she sits for a while with her good hand flat on the page, looking at the line in your name as if it were a wagon with a cracked axle that might yet get where it is going.{/n}
"Right. Here's how it'll go. You come by the stores once a week, on your own feet, and you account for yourself. Boots, blankets, bottles, and whatever else you've drawn on my stores that week. I'll count it. You'll not argue."
{n}She taps the line.{/n} "If I like the accountin', maybe I'll let you buy me a drink out of what you owe." {n}One corner of her mouth moves, and she puts it back, and picks up the pen.{/n}''',
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
      c("[Drink with her.]", "toast")),
    d("toast", '''{n}It is the good stuff. It goes down like a lit fuse. She watches you take it and nods, as if a delivery has been signed for.{/n}
"There's a toast, in the supply service. You'll not have heard it; they don't teach it to officers." {n}She lifts her cup an inch off the table.{/n} "Armed, armoured and fed. Two out of three." {n}She drinks.{/n}
"We drink to the third one, whichever it was that didn't come. Tonight it's boots. Last week it was bread. You'd not believe how many men die in this war 'cause somebody somewhere wrote a number down wrong."''',
      c('"Armed, armoured and fed."', "toasted")),
    d("toasted", '''{n}She looks at you over the cup for a moment longer than she needs to.{/n}
"Two out of three." {n}She corrects you, without heat, and refills both cups, and writes nothing in the book, which she has never once done.{/n}
"Same time next week. Bring the boots back if you've still got 'em."''',
      c("[Finish your cup.]", flags=(COUNTED, P + "drank"))),
    d("no", '''"No." {n}She says it the way she says "two out of three": as a fact of supply.{/n}
"You don't get to buy your way out of my book, Commander. Coin's the easy part. The line stays open till I know where it went, and I close it, not you."
{n}She pours a drink anyway, one, for herself, and after a moment a second, for you.{/n} "That's not forgiveness. That's hospitality. Different column."''',
      c("[Take the refusal and the cup.]", flags=(COUNTED, LINE_OPEN))),
], requires=("trickster.ever", RETURNED), forbids=(COUNTED,), delay=48)


# --- The pivotal beat (Chapter 5): the Fellows' second book. ------------------------------------------------------------

office(P + "after.fellows_methods", "The second book", '"Shut the door. No, all the way."', [
    nar("door", '''{n}She waits for the latch and the clerks' footsteps to fall silent. Outside, the sergeant orders a carrier to unload a crate at the boot-issue bench. Dorgelinda spreads the day's returns across her desk.{/n}''',
        c("Continue", "measures", requires=(HARD_MEASURES,), forbids=(CONSCIENCE,)),
        c("Continue", "conscience", requires=(CONSCIENCE,)),
        c("Continue", "crumbs", forbids=(HARD_MEASURES, CONSCIENCE))),
    d("measures", '''"The requisitions filled the warehouses. The folk we took it from haven't forgotten." {n}She touches her own signature on a return.{/n} "This one wasn't your order. It was mine."''',
      c("Continue", "start")),
    d("conscience", '''"You were right, at the council. You wouldn't turn us into the Fellows of the Crusade, and the donations came in after, and the warehouses are near full. I hate it. I've never been so wrong and so fed in the same month. Hear me anyway."''',
      c("Continue", "start_surplus")),
    d("start_surplus", '''{n}The second book is in her own hand. She puts a depot return beside it: a crate written off in transit, now waiting at her issue bench. Through the open hatch you see the sergeant lift out sound boots. A bottle lies beneath them.{/n}
"Mine. Boots for the lads. Bottle for me." {n}She takes the bottle herself and sets it apart.{/n} "They'll sign for every pair. I'll not pretend they drank my share."
"These are my connections and my figures. The donations cover this month. This is for the reserves. Do we keep the book, or burn the scheme while we can afford to?"''',
      c('"Burn the scheme. I\'ll stand behind my own issues."', "clean"),
      c('"Do it. Their methods. Your books."', "dirty")),
    d("crumbs", '''"There's still companies waitin' for their issue. I've been callin' in old debts across Mendev." {n}She pulls a thin book from beneath the returns.{/n} "Here's what came of it. Not all of it goes in the council minutes."''',
      c("Continue", "start")),
    d("start", '''{n}The second book is in her own hand. She puts a depot return beside it: a crate written off in transit, now waiting at her issue bench. Through the open hatch you see the sergeant lift out sound boots. A bottle lies beneath them.{/n}
"Mine. Boots for the lads. Bottle for me." {n}She takes the bottle herself and sets it apart.{/n} "They'll sign for every pair. I'll not pretend they drank my share."
"These are my connections and my figures. Do we keep this book, or burn the scheme before I use it again?"''',
      c('"Burn the scheme. I\'ll stand behind my own issues."', "clean"),
      c('"Do it. Their methods. Your books."', "dirty")),
    d("clean", '''"Carry your own issue, Commander. You don't get to rub my name off mine." {n}She removes the signed returns before putting the thin book in the stove.{/n} "No second account, then. The boots still go to the lads. Their receipts stay with my signature."
{n}She watches the pages catch, then puts the bottle on her shelf.{/n} "I'm savin' that. Come back when the carts are in. If you want a drink with me."''',
      c("[Leave it there.]", flags=(METHODS, CLEAN))),
    d("dirty", '''"My book. My hand." {n}She writes the recovered crate into the reserve account, then pins the soldiers' issue receipts to the original return.{/n} "Your name covers what you drew. Mine covers this. Nerosyan can ask us both."
{n}She closes the book and puts the bottle on her shelf.{/n} "Come back after the carts. I'd like to drink that with you. Not as payment, mind."''',
      c("[Leave it there.]", flags=(METHODS, DIRTY), crusade=("Materials", 150), alignment=("Evil", 1))),
], requires=("trickster.ever", COUNTED), forbids=(METHODS,), delay=24, chapters=(5,))


# --- The commit (Chapter 5), with her refusal reachable on every branch. ------------------------------------------------

ASK = (
    c('[Flirt] "You, Dorgelinda. I\'d come back with nothing to account for."', "yes", forbids=(BOOTS_OWED,)),
    c('[Set the last pair of boots on her desk.] "Debt paid. I\'m here for you, Dorgelinda."', "yes_boots",
      requires=(BOOTS_OWED,)),
    c('"Before you answer: you still don\'t know where it all went."', "not_yet"),
)

office(P + "after.commit", "The open line", '"Sit. I\'ve got your column open."', [
    nar("open", '''{n}Dorgelinda checks the week's issues and closes the ledger. She leaves the pen beside it. After sending the sergeant to the yard, she brings out a bottle and sets two cups on the desk.{/n} "That's the stores done. Sit a bit."''',
        c("Continue", "recall_clean", requires=(CLEAN,)),
        c("Continue", "recall_dirty", requires=(DIRTY,), forbids=(CLEAN,)),
        c("Continue", "recall", forbids=(CLEAN, DIRTY))),
    d("recall_clean", '''"No second book. My originals are still there, and so are yours. I'm glad you didn't try to take mine off me."''',
      c("Continue", "confessed", requires=(CONFESSED,)), c("Continue", "ask", forbids=(CONFESSED,))),
    d("recall_dirty", '''"The reserve's entered. The lads signed for their boots. If Nerosyan asks, it'll have my figures as well as yours."''',
      c("Continue", "confessed", requires=(CONFESSED,)), c("Continue", "ask", forbids=(CONFESSED,))),
    d("recall", '''"You've been through my stores like weather, Commander. I've written every bit of it down."''',
      c("Continue", "confessed", requires=(CONFESSED,)), c("Continue", "ask", forbids=(CONFESSED,))),
    d("confessed", '''"You told me the truth once, the day I opened the audit. I wrote it down. It's still in here, at the back. Unsent."''',
      c("Continue", "ask")),
    d("ask", '''"You come here and listen. Even when I'm tellin' you no." {n}She rolls her dented cup between her palm and the desk, then sets it down.{/n} "I've started watchin' the door for you. Hammer and tongs. As if I hadn't enough to do."
{n}She looks at you squarely.{/n} "Is it me you're comin' for, Commander? Or have you got another damned shortage?"''', *ASK),
    d("yes", '''{n}She reaches across the desk and catches your hand. Her grip is firm; when you lean closer, she kisses you hard enough to leave you tasting the drink on her lips.{/n} "Then stay. I want you at my table. And in my bed when the carts'll bloody well let us."
{n}She fills her dented cup and pushes it toward you.{/n} "Armed, armoured and fed. Tonight it's three. Cup's yours. Drink. My rooms are behind the stores. Come after the last cart."''',
      c("[Take her cup and stay.]", flags=(COMMITTED,))),
    d("yes_boots", '''{n}She checks the boots and writes them as paid. Then she sets the pen down, takes your hand and pulls you close for a hard kiss.{/n} "Debt's done. This isn't part of it."
{n}She fills her dented cup and stands it inside the left boot.{/n} "Armed, armoured and fed. Three out of three. Cup's yours now. Drink, then bring those to my rooms after the last cart. I want you there."''',
      c("[Take her cup and stay.]", flags=(COMMITTED, BOOTS_PAID), crusade=("Materials", -200))),
    d("not_yet", '''"No, I don't." {n}She shuts the book, gently, which is worse than hard.{/n}
"And I'm not sayin' yes to a line I can't balance, Commander. Not today. Come back when you'll tell me where it went. All of it. Then ask me again."''',
      c("[Leave the ledger with her.]", flags=(DECLINED,))),
], requires=("trickster.ever", METHODS), forbids=(COMMITTED, DECLINED), delay=48, chapters=(5,))


# --- The one priced second ask after her soft no. -----------------------------------------------------------------------

office(P + "after.second_ask", "Where it went", '"You came back. Sit. Talk."', [
    d("price", '''"Where did it go. All of it. Every line in your name, from the first." {n}The pen is already in her hand. She has turned to a clean page, which in her office is the closest thing to a courtesy.{/n}''',
      c("[Tell her everything, and let her strike it from the stores.]", "told", flags=(TOLD_ALL,), crusade=("Materials", -100)),
      c('"Not all of it. Anything else."', "no")),
    d("told", '''{n}You tell her. She writes all of it down, and strikes a hundred's worth of stores that were never really there. When you finish, the page balances, which it has not done since the day you first signed it.{/n}
"There. Was that so hard." {n}She puts the pen down, takes her own dented cup off the shelf, and stands it on the balanced page, empty.{/n} "Now ask."''',
      c('"The account\'s settled. I still want you, Dorgelinda."', "accepted"),
      c("[Leave her to her work.]", forbids=("trickster.now",), abort=True)),
    d("no", '''"Then we're done, Commander." {n}She rules a line under your column, the only line she has ever drawn in anger.{/n}
"I'll keep the book. Not you."''',
      c("[Go.]", flags=(CLOSED,))),
    d("accepted", '''"Aye. I want you at my table. Come here." {n}She catches your collar with her good hand and kisses you. Then she fills the dented cup and puts it in your hand.{/n} "That's yours. My rooms, after the last cart. I'll be waitin'."''',
      c("[Take the cup and stay.]", flags=(COMMITTED, TOLD_ALL))),
], requires=("trickster.ever", DECLINED), forbids=(COMMITTED,), delay=72, chapters=(5,))


# --- Epilogue pages (Owner DorgelindaEpilogue; ordered siblings; no effects). ------------------------------------------

EP = dict(last=6, Relationship="dorgelinda")
SCENES.append(scene(P + "epilogue.committed", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}Dorgelinda Stranglehold sent the Logistics Council's final returns to Nerosyan. She kept the original receipts in the rooms behind the stores. The clerks still brought their requisitions before supper.{/n}''',
        paragraphs=(
            p("{n}The rider signed at the caravan council stayed with the original manifests. Any clerk copying the Commander's issues had to copy that clause as well.{/n}", requires=(CARTS,)),
            p("{n}The boots were entered as paid. She kept the last pair on a shelf in the stores, regulation, unworn, and would not issue them to anyone.{/n}", requires=(BOOTS_PAID,)),
            p("{n}A confession sat in the back of the book, in her hand, never sent to Nerosyan.{/n}", any_groups=[[CONFESSED, TOLD_ALL]],
              forbids=("dorgelinda.ledger.true_books_sent",)),
            p("{n}The confession in the back of the book went to Nerosyan with the rest of the true ledgers. She had not torn it out, and she never said whether she had thought about it.{/n}",
              any_groups=[[CONFESSED, TOLD_ALL]], requires=("dorgelinda.ledger.true_books_sent",)),
        ))],
    requires=("trickster.ever", COMMITTED), forbids=("sacrifice", CLOSED),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))

SCENES.append(scene(P + "epilogue.committed_on_record", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}When the Commander failed to return, Dorgelinda checked the last issue herself. She kept the dented cup beside the receipt, and sent the Commander's remaining kit away under her own seal. No clerk was allowed to do it for her.{/n}''')],
    requires=("trickster.ever", COMMITTED, "sacrifice"), forbids=("trickster.commander_back", CLOSED), **EP))

SCENES.append(scene(P + "epilogue.commit", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}The spring after Threshold, Dorgelinda brought the Commander the last supply ledger and demanded an account of the disputed issues. She had put aside a bottle for the visit. It stayed corked until the work was done.{/n}''')],
    requires=("trickster.ever", METHODS), forbids=(COMMITTED, CLOSED, DECLINED, "sacrifice"),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, **EP))   # Q9 r3: the spring visit needs the Commander back

SCENES.append(scene(P + "epilogue.declined", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}Dorgelinda shipped the Logistics Council's ledgers to Nerosyan after the war, all but one. The Commander's unexplained issue stayed on her shelf. Her personal question had gone unanswered; she returned to supplying the soldiers still in Drezen.{/n}''')],
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
    answer_list=REGILL_HUB, forbids=(REVIEW, *REGILL_GUARD["forbids"]), chapter=3, last=5, portrait="Regill"))
SCENES.append(reaction("Lann", "dorgelinda.react.lann.recount", (PRIMED, TRIBUNAL, "lann.in_party"),
    '''"You lied a whole warehouse clean for them. Next time some hungry recruit asks me why he shouldn't steal, I'm sending him to you. You can explain the difference. I can't."''',
    answer_list=LANN_HUB, forbids=(REVIEW, *LANN_GUARD["forbids"]), chapter=3, last=5, portrait="Lann"))
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
    answer_list=KONOMI_HUB, chapter=3, last=5, portrait="Konomi",
    forbids=(REVIEW, *KONOMI_GUARD["forbids"]), ForbidOverrides=KONOMI_GUARD["ForbidOverrides"]))
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
    for key, forbids in DERIVED_FORBIDS.items():
        have = payload.setdefault("DerivedForbids", {}).setdefault(key, [])
        have.extend(flag for flag in forbids if flag not in have)


# Engine-q5: return/device producers use current power; earned-return consumers keep trickster.ever.
_LIVE_PRODUCERS = {
    'dorgelinda.trickster.audit.open',
}
for _q5_producer in SCENES:
    if _q5_producer["Id"] in _LIVE_PRODUCERS:
        _q5_producer["Requires"] = [*_q5_producer.get("Requires", []), "trickster.now"]
