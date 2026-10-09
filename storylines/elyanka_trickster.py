"""Elyanka Camilary on the Trickster path: "Mourner at your own wake" (Writer/handoffs/trickster/elyanka-camilary.md for the
canon research; the binding plan is 11-ROSTER-PLAN-2 §2, Elyanka block and build sheet, rewritten 2026-09-30 (R5) after the
canon re-check. It supersedes the spec's Fye hub, the royal joke, the own-tomb notice, the feast test and the priced first
stone. Her voice citations stay).

Canon (KTC_ElyankaComing, Elyanka_MainDialogue; all of it native to the Lich path only):
- "priestess of Urgathoa and noblewoman of the Immortal Principality of Ustalav. I also represent the secret society of the
  Whispering Way" (KTC_ElyankaComing/Cue_0001 959e379e); "According to Mendevian law, we have the right to be here. All of us
  have taken the crusader oath" (Cue_0021 53e0aa66); "Our undead warriors will serve you well... They know no fear or
  fatigue" (Cue_0008 dee31f90); hatemongers "who abhor the very thought of necromancy" (Cue_0008, Cue_0015 0956c293);
- her youth: the priests in the Camilary woods, the asylum near Caliphas, the poisoned lamb (Cue_0016-0018 acd0453b,
  1f16966e, d97939bc); "One day I will become the daughter of Urgathoa, her adopted child... for now the goddess wants me
  to remain mortal... this grubby, sweat-reeking, disgusting mortal life" (Elyanka_MainDialogue/Cue_0093 836b4983);
  mortals "are just dumb cattle, fit only for food" (Cue_0062 e5ab07dc); the Way's teaching "cannot be written, only told"
  (Cue_0061 98312252); "Our services to honor her are more luxurious than the most lavish feasts, the wildest orgies...
  there isn't a single nation in Avistan where worshiping Urgathoa is legal now" (Cue_0055 335273ed); Pharasma, "that gray
  prison warden" (KTC_ElyankaComing/Cue_0025 2d1bf405); "strong white teeth" (Cue_0073 4af8f198); "unblinking, bird-like
  eyes... a royal equanimity at odds with the gray rags she is wearing" (Cue_0071 87d34364).

The door (canon on every path, and the only one): Drezen declared the Commander dead and held a funeral feast
(AneviaDrezenPartisans/Cue_0007 59ac2148 and Cue_0017 04923e59; VendorDangerousTavern/Cue_0040 c76a1e61; on Trickster the
Fool King's own "threw you a fine funeral", FoolKing_Tavern/Cue_0059 d1c14400). Authored premise, labelled on the page as
her belief and her errand: the news reached Ustalav, and the Whispering Way sent its envoy with a hearse to buy the corpse.
Nothing reads a Lich key; nothing is hosted on the King's or Fye's list (the King appears in node text only).

Device ("Mourner at your own wake"): the Commander receives her veiled, as the executor of the late Knight Commander, and
haggles over the body, to learn what a lich-cult pays for a mythic corpse, and why, before it learns the corpse is
listening (CheckBluff DC 26, 22 with the Fool King's court hired as weeping mourners). No mythic power solves anything.
Commit: an exchange of claims; she whispers her own corpse to the Commander in return (her bargains are whispered, like the Way's teaching).
Cost: the Commander's body, bequeathed to the Whispering Way in her keeping, due at death (Evil 1); the soul stays
Pharasma's. A Ledger debt to a live power: Last Call's bottle cheats it by the letter; without the bottle it stands unpaid
while the Commander lives, and the Wound leaves her nothing to collect if it takes the Commander.

Path fit (ROUTE-BRIEF-R, v1): every scene is T. Her native arc is Lich; v2 may open the same funeral door on the Demon and
Swarm-That-Walks paths (14-PATH-FIT). No non-Trickster commit or ending is written yet.
"""
import copy

from story_format import c, n, p, reaction, scene
from storylines import household

SCENES = []
REL = "elyanka"
E = "elyanka.trickster."

DREZEN = "2570015799edf594daf2f076f2f975d8"           # DrezenCapital: the dead-house, the gate, the Commander's quarters
UNIT = "68bc27eb628a7584b96e901f4b4c4071"             # MythicLich_KTC_Elyanka (no dialog; not spawned: every scene is remote)
PORTRAIT_GUID = "db50a1cef98b4c0798982836f0af09cb"    # the unit's m_Portrait (BCT_ElyankaHuman), fallback until custom art
DAERAN_HUB = "4d978cbd2aa780d46874255282039f3f"       # CompanionDialogues/Daeran/AnswersList_0003
SEELAH_HUB = "417fa384f3250634bb71859fbc913453"       # CompanionDialogues/Seelah/AnswersList_0003
REGILL_HUB = "2366a8db6481070439fee222c0c52e45"       # CompanionDialogues/Regill/AnswersList_0002

STARTED = "elyanka.started"
CLOSED = "elyanka.closed"
COMMITTED = "elyanka.committed"

# Native reads: the funeral, heard of in any of its canon tellings (SeenCues), with the Iz fallback (it happened in every
# Chapter 5). One latch records the first of them; the door counts its delay from it.
FUNERAL_KING = "elyanka.funeral.king"            # FoolKing_Tavern/Cue_0059 "We sang songs, threw you a fine funeral"
FUNERAL_PA = "elyanka.funeral.partisans_a"       # AneviaDrezenPartisans/Cue_0007 "You were declared dead, see..."
FUNERAL_PB = "elyanka.funeral.partisans_b"       # AneviaDrezenPartisans/Cue_0017 (the other Wardstone branch)
FUNERAL_FYE = "elyanka.funeral.fye"              # VendorDangerousTavern/Cue_0040 "a grand old time at your funeral feast"
FUNERAL = E + "funeral.latched"
IZ_DONE = "iz.done"
KING_HERE = "fool_king.available"
KING_GONE = "fool_king.gone"
DAERAN_GONE = ("daeran.dead", "daeran.kicked_out")

# The route.
DOOR_SEEN = E + "door_seen"
REFUSED_VEILED = E + "refused.veiled"              # the wake refused before the veil came off
REFUSED_UNVEILED = E + "refused.unveiled"          # the wake refused after the unveiling and her laughter
REFUSED_CAUGHT = E + "refused.caught"              # the owner, caught, would not sell (she took the jug)
REFUSED_SUPPER = E + "refused.supper"              # the corpse came to supper bare-faced and would not sell
ESCORTED = E + "escorted"                        # the door refused: escorted back to the Ustalav road
EXECUTOR = E + "executor"                        # the Commander will receive her as the executor, veiled
STRAIGHT = E + "straight"                        # the Commander will receive her bare-faced
MOURNERS = E + "mourners"                        # the Fool King's court hired to weep at the wake (Bluff DC 22)
OWNED = E + "owned"                              # the sale is made: the Way owns the Commander's corpse, due at death
BEQUEATHED = E + "cost.corpse_bequeathed"        # the cost (Evil 1): the Ledger debt to the Whispering Way
BLUFFED = E + "bluffed"                          # the con held: she named her purpose to the executor, and laughed
EXPOSED = E + "exposed"                          # the con failed: she never trusts the Commander's face again
TESTED = E + "tested"                            # she asked for the Iz dead, and had her answer
GAVE_DEAD = E + "gave_dead"                      # Evil 2: the unclaimed dead of Iz, given to her
CARRION = E + "gave_carrion"                     # the demon carrion offered instead
REFUSED_DEAD = E + "refused_dead"                # "You guard what is owed. Good."
DECLINED = E + "declined"                        # the soft no: asked what she would do with the Commander's corpse
LEFT_FREE = E + "left_free"                      # sent home after her move (also sets the ClosedFlag)
LOCK = E + "lock_taken"                          # took the lock of grey hair bound in black thread
BIER = E + "bier_seen"                           # the night in her hearse
DAERAN_ALLY = E + "daeran_ally"                  # Daeran's reaction: he sends her wine on the funeral's anniversary
HORSES = E + "horses_balked"                     # the hearse door frightened her mares
SECRET_DEAD = "trickster.secret.elyanka_siege_dead"
SECRET_RITES = "trickster.secret.elyanka_rites"
# Read from elyanka_hearse (the courtship beats), declared here so the pages can read them.
TABLE_SAT = E + "table.sat"
TABLE_DOOR = E + "table.kept_door"
TABLE_LEFT = E + "table.left"
WRIT_UPHELD = E + "writ.upheld"
WRIT_LIED = E + "writ.lied"
WRIT_HERS = E + "writ.hers"
AT_RIFT = E + "collateral.at_rift"
IN_DREZEN = E + "collateral.in_drezen"
# No late romance: late_committed is the real commit (design review r5, BEL): eligibility, the Table and Last Call read a
# yes she actually gave. A route that ends before the claims were exchanged ends as a debt, not a romance.
LATE_COMMITTED = E + "late_committed"

RELATIONSHIP = dict(
    Title="The Executor",
    Description=("A priestess of Urgathoa came up the Ustalav road with a hearse to buy the corpse of the late Knight "
                 "Commander. I was not as late as she had been told. I bequeathed it to the Way instead, without payment."),
    Objective="See what the Whispering Way's envoy does with the claim I gave her",
    Guidance=("On the Trickster path, once Drezen has held its funeral feast for you and the fighting at Iz is over, an "
              "envoy of the Whispering Way arrives at the gate asking for the executor of the late Knight Commander. "
              "Receive her, as yourself or as your own executor."),
    StartedFlag=STARTED, ClosedFlag=CLOSED, CommittedFlag=COMMITTED,
    UnavailableFlags=[LEFT_FREE], FailureFlags=[], UnavailableOverrides={},
)

SEEN_CUES = {FUNERAL_KING: ["d1c14400d70bf0d4b947283f16f65009"],
             FUNERAL_PA: ["59ac2148b08ee7a47912253362ab0b27"],
             FUNERAL_PB: ["04923e59ebb21f943b7a2a330a6a8820"],
             FUNERAL_FYE: ["c76a1e617bcba114c9c726ba2363c98f"]}
LATCHES = {FUNERAL: [FUNERAL_KING, FUNERAL_PA, FUNERAL_PB, FUNERAL_FYE, IZ_DONE]}
DERIVED = {
    LATE_COMMITTED: [["trickster.ever", COMMITTED]],
    # 05 §2.5 voice note: she joins as a creditor who has already been paid in advance, and means to collect.
    "elyanka.harem.voice.creditor": [[COMMITTED]],
}

# Path fit (ROUTE-BRIEF-R 2026-09-29, v1): T = device or Trickster-only; N-all = any path; N-fit = the fitting paths.
PATH_FIT = {}


def tag(scene_id, fit):
    PATH_FIT[scene_id] = fit


def el(id, text, *choices, **kw):
    """Elyanka on a rest-delivered page (her portrait)."""
    return n(id, "Elyanka", text, *choices, portrait="Elyanka", **kw)


def nar(id, text, *choices, **kw):
    return n(id, "Narrator", text, *choices, **kw)


def visit(id, title, nodes, requires, forbids=(), delay=24, last=6, optional=False, kind="visit", owner="Elyanka",
          **extra):
    """A remote visit in Drezen (she keeps her hearse in the dead-house yard by the south gate, and comes and goes from it):
    delivered only at a rest in the capital, where the dead-house is."""
    SCENES.append(scene(id, title, owner, 5, "", nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, *forbids), delay=delay, last=last, optional=optional, Relationship=REL,
                        Remote=True, Kind=kind, Areas=[DREZEN], **extra))
    tag(id, "T")


def bluff(text, success, failure):
    """The executor's lie: DC 22 with the Fool King's court weeping in the corner, 26 otherwise."""
    return (
        c(text, check=dict(Skill="CheckBluff", DC=22, Success=success, Failure=failure, CommanderOnly=True),
          requires=(MOURNERS,)),
        c(text, check=dict(Skill="CheckBluff", DC=26, Success=success, Failure=failure, CommanderOnly=True),
          forbids=(MOURNERS,)),
    )


# --- 1. The door (T, Chapter 5): a hearse at the south gate. -------------------------------------------------------------

DOOR_CHOICES = (
    c('[Go as your own executor] "Lodge her in the dead-house by the south gate. Nobody tells her I\'m alive. Tomorrow night the executor receives her."',
      "plan", mythic="Trickster"),
    c('[Go as yourself] "Tell her the late Knight Commander will see her tomorrow. Let her make of that what she likes."',
      flags=(STRAIGHT, DOOR_SEEN)),
    c('[Have her escorted to the Ustalav road] "Give her back her card and an escort to the border. Drezen has dead enough."',
      "escort"),
)

SCENES.append(scene(E + "door.hearse", "A hearse at the south gate", "Elyanka", 5, "", [
    nar("start", '''{n}The sergeant of the south gate has been standing outside your door since the change of watch, and he has not once put down the card in his hand, as if it might go off. It is heavy grey paper edged in black, sealed with black wax and a pressed white flower, and it is addressed in a tall, sloping hand:{/n}
{n}*To the executor of the estate of the late Knight Commander of the Fifth Crusade. Elyanka Camilary, of the Immortal Principality of Ustalav, under the crusader's oath, asks leave to treat for the remains. Payment in hand.*{/n}''',
        c("Continue", "sergeant")),
    n("sergeant", "Gate sergeant", '''"Came up the Ustalav road at noon, Commander. A hearse. Black lacquer, glass sides, four black horses in plumes, and six of hers walking behind in grey without a word out of any of them. She has the oath right enough. Sworn at Nerosyan on her way north, not a month back; I read it twice. By law she can come in, and she knows it. She told me so before I asked."
{n}He turns the card over, and back.{/n} "She asked for your executor, Commander. Not for you. I didn't tell her you were alive. I didn't tell her anything. I don't think she'd have heard me if I had."''',
      c("Continue", "king", requires=(FUNERAL_KING,)),
      c("Continue", "anevia", requires=(FUNERAL_PA,), forbids=(FUNERAL_KING,)),
      c("Continue", "anevia", requires=(FUNERAL_PB,), forbids=(FUNERAL_KING, FUNERAL_PA)),
      c("Continue", "fye", requires=(FUNERAL_FYE,), forbids=(FUNERAL_KING, FUNERAL_PA, FUNERAL_PB)),
      c("Continue", "plain", forbids=(FUNERAL_KING, FUNERAL_PA, FUNERAL_PB, FUNERAL_FYE))),
    nar("king", '''{n}So that is where the story went. The Fool King told it to you himself, with his mouth full: while you were in the Abyss his court lived life to the fullest, sang songs, and threw you a fine funeral, and you would have loved it. Somewhere between his tavern and Caliphas the feast was carefully remembered and the guest of honour's return was not.{/n}''',
        c("Continue", "choice")),
    nar("anevia", '''{n}You were declared dead while you were in the Abyss. You remember Anevia telling you at the barricades: a big funeral feast and everything. You remember Beth among the mourners in her account. Somebody at that feast must have written home, and home must have been somewhere on the Ustalav road.{/n}''',
        c("Continue", "choice")),
    nar("fye", '''{n}Fye told you about it when you came back: a grand old time at your funeral feast, he said, and an even better one to come at your homecoming. The first party seems to have been better advertised than the second.{/n}''',
        c("Continue", "choice")),
    nar("plain", '''{n}You were declared dead once, while you were in the Abyss. Drezen held a feast in your name, and wept, and drank, and went back to the walls. The news went south faster than the correction.{/n}''',
        c("Continue", "choice")),
    nar("choice", '''{n}A priestess of the Pallid Princess has come a very long way, with the law on her side and a hearse at your gate, to buy your corpse. She has never seen your face. By tonight half the lower town will have told her you are alive.{/n}
{n}Unless nobody does. What does a cult of necromancers pay for a mythic corpse, and what does it want one for? Nobody has ever asked them with the corpse in the room.{/n}''',
        c("[First go up on the gate tower, and look at her.]", "tower"),
        *DOOR_CHOICES),
    nar("tower", '''{n}From the gate tower you can see into the yard where the watch has made her wait. The hearse stands in the middle of it with its four black mares, plumed and perfectly still, which horses never are. Her six stand behind it in a row, in grey, and you watch for the length of a hundred heartbeats without seeing one of them shift his weight, or scratch, or breathe a cloud into the cold.{/n}
{n}She walks round the hearse slowly, running one gloved finger along the lacquer, the way a woman checks a dining table for dust. Then she stops and looks straight up at the tower, at your window, though you are standing back from it in the shadow. She does not wave. She looks at it as she might look at a door she intends to open later, and goes back to her inspection.{/n}''',
        *DOOR_CHOICES),
    nar("plan", '''{n}You give the orders yourself, quietly, to the sergeant and nobody else. The Ustalavic lady is to be lodged in the dead-house by the south gate, which she will like: it has a yard big enough for a hearse and nobody inside who can gossip. Until you summon her to the wake, the gate watch is to call you the executor. Nobody who knows your face goes within a street of her. Her meals come from the garrison kitchen; her six can carry them. If you keep her waiting, these orders stand.{/n}
{n}Then you walk down to Fye's for the crepe. There is plenty left over from your funeral. He finds you a veil of it that hangs to the breastbone and a pair of black gloves, and he does not ask a single question, which is why you went to Fye.{/n}''',
        c('[Hire mourners] "Majesty, how would your court like to weep at a wake? The crusade pays for the drink."', "mourners",
          requires=(KING_HERE,), forbids=(KING_GONE,)),
        c('[Go alone] "An executor grieves in private."', flags=(EXECUTOR, DOOR_SEEN))),
    nar("mourners", '''{n}Thaberdine is delighted. He has been to a great many funerals, he says, and never once been paid to cry at one, which is a scandal he will put right tonight.{/n}
"Real weeping, mind. None of your thin stuff. I'll have the jugglers wail, and the fire-eater can beat his chest, he's got the chest for it. Whose wake is it? Yours? Ha! Again! I knew you'd make a habit of it."
{n}He crowns a sausage in your memory and eats it, for luck.{/n}''',
        c("[Stand the court its drink.]", flags=(EXECUTOR, MOURNERS, DOOR_SEEN), crusade=("Finances", -50))),
    n("escort", "Gate sergeant", '''{n}The sergeant looks relieved, and then, for some reason, not.{/n} "Yes, Commander. Border escort. Twelve men."
{n}He comes back at dusk to report. She read the order twice, as he had read her oath, and handed it back to him, and got into the hearse without a word. At the edge of the camp she put her head out of the window and asked him whether the Knight Commander had been buried with the eyes open or shut. He did not know. She said it did not matter, and that she would ask again another time.{/n}''',
      c("Continue", flags=(CLOSED, DOOR_SEEN, ESCORTED))),
], requires=("trickster", FUNERAL, IZ_DONE), forbids=(DOOR_SEEN, CLOSED), delay=72, last=5, Relationship=REL, Remote=True,
    Kind="event", Chapters=[5], Areas=[DREZEN]))
tag(E + "door.hearse", "T")


# --- 2. The wake (T): the executor haggles over the body. The device. -----------------------------------------------------

SOLD = (OWNED, BEQUEATHED, STARTED)

visit(E + "executor.haggle", "The executor", [
    nar("start", '''{n}The dead-house by the south gate is a long, low barn of a building that smells of lime and cold stone. Tonight it has been swept. Candles burn along the rafters in black iron cups, and in the yard behind it the hearse stands with its shafts down and its glass sides shining, like a carriage waiting outside a ball.{/n}
{n}You come in veiled to the breastbone in funeral crepe, gloved, in a borrowed black coat that does not fit. It is surprisingly hard to breathe in a veil. You had not considered that the dead never need to.{/n}''',
        c("Continue", "wake", requires=(MOURNERS,)),
        c("Continue", "her", forbids=(MOURNERS,))),
    nar("wake", '''{n}Behind you comes the wake. The Fool King's court has taken its commission to heart. A juggler sobs into his clubs. A woman in a paper crown keens like a widow of forty years. Thaberdine himself, draped in a velvet curtain, is carried in on a door, set down weeping in the corner where he can reach the wine, and waves the procession on with a drumstick.{/n}
{n}Nobody who saw this could imagine its object sitting up and breathing. That is rather the point.{/n}''',
        c("Continue", "her")),
    el("her", '''{n}She sits at the far end, at a trestle laid for two, with her back very straight: silver-grey hair drawn hard off a face as severe as the head on a coin, strong dark brows, pale eyes that do not blink often enough. Her robe is grey and plain, frayed at the hem, and she wears it the way a queen wears ermine.{/n}
"You are the executor." {n}It is not a question.{/n} "Elyanka Camilary, priestess of Urgathoa and noblewoman of the Immortal Principality of Ustalav. Sit down. You have walked a long way behind a coffin, I think. Grief is so tiring for the living."''',
       c("[Sit, and say nothing.]", "table"),
       c('"The estate thanks you for coming so far."', "table")),
    el("table", '''"Not so far. The Way has been walking toward Drezen since before either of us was born." {n}She pours wine into both cups. Hers she does not touch.{/n}
"Let us not pretend this is a condolence call. News came to Caliphas that the Knight Commander of the Fifth Crusade was declared dead, and feasted, and wept over. A mythic corpse, fresh, with no heir that anyone could name. Such a thing does not lie long unspoken for. I came to speak for it before the wrong people did."''',
       c('"The wrong people?"', "wrong"),
       c('"Then speak. What does Ustalav offer?"', "offer")),
    el("wrong", '''"Demons, who would wear it. A certain witch in the Wound, who made it what it is, they say, and would like it back." {n}Her mouth thins.{/n}
"And your priests. The priests are worst. They would wash it and mumble over it and put it in a hole to rot, for the grey old warden of the Boneyard, who never lifted a finger for it in life. Such waste." {n}To her, plainly, the word is a blasphemy.{/n}''',
       c("Continue", "offer")),
    el("offer", '''"The Way pays for what it values, executor, and it values very little. A mythic corpse is worth gold." {n}She counts on long fingers.{/n}
"For a corpse I can take away tonight, the estate will be paid. The remains leave in that carriage outside, under my escort, with no hand but mine touching them on the road. No demon or witch will get them, and your priests will not bury them. My six have sworn the crusader's oath. They answer to me."''',
       c("Continue", "estate")),
    el("estate", '''"But first tell me about the deceased, executor. The Way likes to know what it is buying. They say a great many things in Caliphas about the Knight Commander of the Fifth Crusade, and most of them contradict each other." {n}She folds her long hands on the table.{/n} "What was {mf|he|she} like?"''',
       c('"Vain. {mf|He|She} would have loved this wake."', "vain"),
       c('"Brilliant. The best commander the crusade ever had."', "brilliant"),
       c('"Unbearable. Nobody could stand {mf|him|her}."', "unbearable")),
    el("vain", '''"Vain. Good. Vanity keeps; it is a kind of preservative. The vain take care of their skin and their teeth." {n}Her eyes go to your gloves, and stay there a moment.{/n} "You speak of {mf|him|her} warmly, for an executor. One would almost think you knew {mf|him|her} well."''',
       c('"Generous, your offer. Generous people want something. What does your order want with it?"', "why")),
    el("brilliant", '''"Brilliant commanders make poor corpses. They are always full of holes, from all the people who could not bear to be outthought." {n}She tilts her head.{/n} "And yet you sound proud of {mf|him|her}. Executors are not usually proud. They are usually counting."''',
       c('"Generous, your offer. Generous people want something. What does your order want with it?"', "why")),
    el("unbearable", '''"Unbearable. Then {mf|he|she} and I would have got on. Nobody can bear me either; I have found it saves a great deal of time at dinner." {n}Something that is almost a smile.{/n} "You say it with feeling, executor. I suspect you were one of the people who could not stand {mf|him|her}."''',
       c('"Generous, your offer. Generous people want something. What does your order want with it?"', "why")),
    el("why", '''{n}Her pale eyes rest on your veil, on the place where your mouth would be.{/n}
"That is the one question an executor has no business asking. You are selling a body, not a destiny." {n}A dry twitch of the lips, like a smile that could not be bothered.{/n} "Name a price, or give me the key to the vault. You keep me waiting in this house, and I have still not been shown the deceased."''',
       *bluff('[Bluff] "The estate has two other offers, and one of them told me why. Tell me yours, or I sell elsewhere by morning."',
              "named", "pulse")),
    el("named", '''{n}She is quiet long enough for a candle to spit on the rafter above her. You watch her weigh the lie, and decide to believe it, and dislike believing it.{/n}
"Two other offers. In Drezen. For *that*." {n}The bird-bright eyes go hard.{/n} "Then let them hear the only answer that matters, and go home."
"My time will come, executor. One day I will become the daughter of Urgathoa, her adopted child, and have the immortality I was promised. For now she wants me mortal, and useful. I have been useful for a very long time." {n}Her lip curls on the word, as if it had gone off.{/n}''',
       c("Continue", "named2")),
    el("named2", '''"A mythic corpse laid at her table would be an offering the Pallid Princess could not ignore. The flesh of one who stood in the Worldwound and drank what came out of it, served whole. She would eat, and be pleased, and remember whose hand set the dish down." {n}She shows strong white teeth.{/n}
"The soul I do not want. Let the grey warden keep it; she keeps a dull house. My Lady eats meat."''',
       c("[Lift the veil.]", "unveil"),
       c('[Keep the veil on and stand] "Then the estate isn\'t selling. Good night, my lady."', "refuse_veiled")),
    nar("unveil", '''{n}You take off the gloves first. Then the veil, slowly, because she is watching and you have always had a sense of occasion.{/n}
{n}Elyanka Camilary looks at the face of the late Knight Commander of the Fifth Crusade: flushed from the crepe, sweating a little, and firmly attached to the rest of you. Her expression does not change at all. Then she begins to laugh.{/n}
{n}It starts low and gets away from her. She laughs until she has to hold the table with both hands, until she is coughing into her grey sleeve, until her eyes stream and the candles along the rafters shiver in their cups.{/n}''',
        c("Continue", "court", requires=(MOURNERS,)),
        c("Continue", "laughed", forbids=(MOURNERS,))),
    nar("court", '''{n}In the corner the wake falls silent all at once. Then the Fool King sits bolt upright on his door, flings off his curtain, points a drumstick at you and roars, "IT'S A MIRACLE! The deceased has risen! Somebody fetch more beer!", and the whole court goes from wailing to cheering without drawing breath, and the juggler throws his clubs in the air and forgets to catch them.{/n}
{n}Elyanka goes on laughing through all of it, helplessly, one hand pressed to her ribs.{/n}''',
        c("Continue", "laughed")),
    el("laughed", '''"You sat there." {n}She wipes her eyes with a knuckle.{/n} "You let me pour you wine at your own wake. Two other offers. There are no other offers, are there? There is only you, sweating under a curtain, wanting to know what you are worth to the dead."
"Well. Now you know." {n}The laughter goes out of her all at once, like a lamp turned down.{/n} "And I find I still want it."''',
       c("Continue", "terms")),
    el("terms", '''"I offered gold for a corpse, Commander. You have brought me a pulse." {n}She pushes her untouched cup across the table.{/n} "I will not pay to watch you grow old."
"Bequeath it instead. No gold, no favors. When you die, the body is the Way's, in my keeping, and it goes to my Lady's table whole. Until then do what you like with it, since you seem to like so much."''',
       c('[Bequeath it] "My body, at my death, to the Whispering Way, in your keeping. Done."', "sold"),
       c('"No. You came for a corpse. You\'ll go home without one."', "refuse")),
    el("sold", '''{n}She does not call for pen or paper. She leans across the table instead, close enough that you smell cloves and cold wine on her, and says the terms into your ear in a whisper, in a language older than the words she is using. Then she waits, her cheek almost against yours, until you have whispered them back.{/n}
"The Way's teaching cannot be written, Commander, only told. I keep my bargains the same way. What is whispered cannot be burned, or forged, or forgotten by anyone who heard it." {n}She sits back, and for a moment she looks almost pleased with you.{/n} "Not a copper, and still you whispered it back." "You are mine when you are dead. Try to make it an interesting death."''',
       c("[Put the veil back on for the walk home.]", flags=(*SOLD, BLUFFED), alignment=("Evil", 1))),
    el("refuse_veiled", '''{n}She looks at the veil for a while, as if she could see through it, and perhaps she can.{/n}
"You made me say it aloud," {n}she says softly,{/n} "to a curtain, in a barn, and now you will not sell. That was not grief, executor. That was curiosity." {n}She rises.{/n} "Tell the estate the Way does not forget who was curious about it. Good night."''',
       c("Continue", flags=(CLOSED, REFUSED_VEILED))),
    el("refuse", '''"Then I have laughed more tonight than in the last ten years, and that is worth something." {n}She stands, and she is taller than you expected.{/n}
"But you should not have let me say it. The Way does not like to be heard by people who will not deal. Go home, Knight Commander, and live as long as you like. I will not be there when you stop."''',
       c("Continue", flags=(CLOSED, REFUSED_UNVEILED))),
    el("pulse", '''{n}You press the lie too hard. The estate has other buyers; the estate will not wait; the estate will not have your remains haggled over like a side of beef in a barn. She lets you finish.{/n}
"*My* remains." {n}She says it back to you in your own cadence.{/n} "You said *my*, executor. Mourners grieve in the third person; it is the first thing an undertaker learns. Only one person at a wake ever says *my remains*." {n}She reaches across the table, quite unhurried, and lays two cold fingers against the side of your throat, just above the crepe, the way a physician does. Or an embalmer.{/n}
"And the deceased has a pulse, Commander. It is in the throat, and it is racing."''',
       c("Continue", "pulse2")),
    el("pulse2", '''"Did you think I had never seen a man sit at his own funeral in a borrowed coat? I have seen a dozen, all of them debtors. My order has hidden in plain sight for six hundred years, and you came to me in a *curtain*." {n}She takes her hand back and wipes her fingers on a napkin, one by one.{/n}
"I can guess why. You wanted to know what I would pay before I knew what you were. Take that off. The gold was for a corpse I could carry away tonight. Now I will hear what the living owner has to offer, bare-faced."''',
       c("[Take off the veil and hear her terms.]", "bare"),
       c('[See her out] "The owner isn\'t giving it away."', "seen_out")),
    el("bare", '''{n}She does not look at your face once you have uncovered it. She looks at your hands, and your throat, and the vein at your temple, as if those were the parts of you that could be trusted.{/n}
"No gold. No favors. Bequeath the body to the Way, in my keeping, whole, at your death. Until then it is yours. I do not tell the owner what I want it for; the executor lost that with the lie." {n}She pushes her untouched cup across to you.{/n} "And I will never believe your face again. Answer."''',
       c('[Bequeath it bare-faced] "Done. My body, at my death, to the Way. No payment."', "bare_sold"),
       c('[See her out] "The owner isn\'t giving it away after all."', "seen_out")),
    el("bare_sold", '''{n}No pen and no paper. She leans across the table and says the terms into your ear in a whisper, in words older than the language they are in, and waits until you have whispered them back. Her breath is cold, and smells of cloves.{/n}
"I do not put my bargains on paper, Commander. What is whispered cannot be burned or forged." {n}She sits back.{/n} "Nothing paid. Nothing due to you." "You are mine when you are dead, Commander. Until then I shall watch your hands. Your face is a liar."''',
       c("[Take the veil with you.]", flags=(*SOLD, EXPOSED), alignment=("Evil", 1))),
    el("seen_out", '''"As you like." {n}She rises, unhurried, and tucks the wine jug under her arm as though it were part of her fee.{/n}
"You dressed as your own mourner to see what you were worth, and would not accept the terms. That is the most honest thing a mortal has done in front of me in years." {n}At the door she turns.{/n} "Keep the veil. You will want it one day."''',
       c("Continue", flags=(CLOSED, REFUSED_CAUGHT))),
], requires=(EXECUTOR,), forbids=(OWNED,), delay=24, last=5)


# --- 3. Bare-faced (T): the corpse comes to supper. -------------------------------------------------------------------

visit(E + "straight.offer", "The corpse comes to supper", [
    nar("start", '''{n}The dead-house by the south gate smells of lime and cold stone. Candles burn along its rafters in black iron cups, and in the yard behind it a hearse stands with its shafts down and its glass sides shining. At a trestle laid for two, at the far end of the long room, a woman in grey sits waiting with her back very straight.{/n}
{n}The sergeant announces you in the doorway, the way you told him to: the late Knight Commander of the Fifth Crusade.{/n}''',
        c("Continue", "her")),
    el("her", '''{n}She looks at you for the space of three breaths: silver-grey hair drawn hard off a face as severe as a coin, strong dark brows, pale, unblinking, bird-like eyes. Then she wrinkles her nose, very slightly.{/n}
"They told me in Caliphas that you were dead. I came four hundred miles for a corpse, and the corpse comes to supper, sweating." {n}She does not rise.{/n} "Elyanka Camilary. Priestess of Urgathoa, of the Immortal Principality of Ustalav. Sit, since you are here. What are you doing alive?"''',
       c('"Mostly fighting demons. Occasionally eating."', "sit"),
       c('"I was about to ask what you want with me dead."', "sit")),
    el("sit", '''"Being useful," {n}she says, as if it were a disease she had caught from you.{/n}
"The Way heard that a mythic corpse lay unclaimed in Drezen, with no heir, and demons and witches and priests all circling. It sent me to speak for it first. The Pallid Princess would value such flesh above any prayer. I would value her gratitude." {n}She taps one long finger on the table.{/n} "And now I find there is nothing to speak for, only a warm {mf|man|woman} who smells of the stable, and will keep on smelling of it for years."''',
       c("Continue", "hands")),
    el("hands", '''"Give me your hand." {n}It is not a request. She takes it across the trestle before you have decided, and turns it over under the candle as a jeweller turns a stone: the calluses from the sword, the white seam of an old cut, the vein at the wrist. She presses two cold fingers into it and counts.{/n}
"Fast. Everything about you is fast. You will burn out and call it a life." {n}She lets go, and wipes her fingers on a napkin.{/n} "But the bones are good. The bones are very good. I should hate to see them wasted in one of your priests' holes."''',
       c("Continue", "terms")),
    el("terms", '''"If it were up to me, I would have left this grubby, sweat-reeking mortal life a very long time ago. You cling to it with both hands. Well." {n}She pushes her untouched cup across the table to you.{/n}
"I came to pay for a corpse I could take home. You are not one. Bequeath what you will leave instead. No gold, no favors; my escort stays mine. When you die, the body is the Way's, in my keeping, whole. Until then do as you like with it. You will anyway."''',
       c('[Bequeath it] "When I die, it\'s yours. No payment. Keep your carriage polished."', "sold"),
       c('"No. Nobody is waiting for my corpse, and nobody gets it."', "refuse")),
    el("sold", '''{n}She does not call for pen or paper. She rises, comes round the trestle, and bends to say the terms into your ear in a whisper, in words older than the language they are in. Then she waits, a hand on your shoulder as cold as a banister in winter, until you have whispered them back.{/n}
"Paper burns, Commander. I keep my bargains as the Way keeps its teaching: told, not written. What is whispered cannot be burned, or forged, or forgotten." {n}She straightens.{/n} "Nothing paid. Nothing due to you." "You are mine when you are dead. Do not dawdle."''',
       c("[Finish her wine.]", flags=SOLD, alignment=("Evil", 1))),
    el("refuse", '''"Everybody is waiting for your corpse, Commander. The Abyss, the witch who made you, the grey warden with her ledger. I am only the first who had the manners to ask." {n}She rises, and she is taller than you expected.{/n}
"But you have refused me, so I will go and wait somewhere more comfortable. Live as long as you please. I am told it is a great deal of work."''',
       c("Continue", flags=(CLOSED, REFUSED_SUPPER))),
], requires=(STRAIGHT,), forbids=(OWNED,), delay=24, last=5)


# --- 4. The Iz dead (T): her test, the evil pivot. ---------------------------------------------------------------------

visit(E + "test.the_dead", "Sixty-one under canvas", [
    nar("start", '''{n}The message is a sprig of white flower pushed under your door, nothing more, and you know where to go. The dead-house is full tonight. The carts came back from Iz with more dead than the chaplains can bury in a week, and the named ones went into the ground first. The rest lie in rows along the long room under grey canvas, sixty-one of them, waiting for the Lady of Graves' rites.{/n}
{n}Elyanka walks between the rows with a lantern, lifting the canvas at the heads, one after another, reading each face and letting the canvas fall again.{/n}''',
        c("Continue", "exposed", requires=(EXPOSED,)),
        c("Continue", "bluffed", requires=(BLUFFED,)),
        c("Continue", "plain", forbids=(EXPOSED, BLUFFED))),
    el("bluffed", '''"Executor." {n}She does not look up. There is a smile in her voice, and it is not kind.{/n} "No veil tonight? I was growing fond of it. Come, stand here, where the lantern will not make you sweat."''',
       c("Continue", "rows")),
    el("exposed", '''"Commander." {n}She does not look up, and she does not look at your face when she does. She looks at your hands.{/n} "Keep them where I can see them. Come, stand here."''',
       c("Continue", "rows")),
    el("plain", '''"Commander." {n}She does not look up.{/n} "You are the only person in this room who is still sweating. Stand over there, by the door, where it does not carry."''',
       c("Continue", "rows")),
    el("rows", '''{n}She lifts the canvas from a young face with a split lip, looks, and lets it fall.{/n}
"Your chaplains are very slow. The ones with names went into the earth two days ago, with prayers and mothers. These have no names. Nobody has come for them. Nobody will." {n}She moves to the next row.{/n}
"In three days they go into a pit with lime on top, and the grey warden has sixty-one more souls in her queue, and the flesh rots in the dark for nothing. Nothing at all. It is the most wasteful custom in the world."''',
       c("Continue", "paladin", requires=("seelah.in_party",), flags=(E + "seelah_prayed",)),
       c("Continue", "ask", forbids=("seelah.in_party",))),
    el("paladin", '''"Your paladin was here this morning. The one with a thief's hands." {n}She lifts another canvas.{/n} "the paladin of Iomedae, kneeling to pray for Pharasma's dead, row by row, until her knees were grey with lime. She did not see me in the yard. I watched her the whole time."
"I would like to see her face when she learns what her Lady's crusade is built on. One day, perhaps. Not tonight."''',
       c("Continue", "ask")),
    el("ask", '''{n}She lets the canvas fall and turns, and the lantern puts her shadow up the wall to the rafters.{/n}
"Give them to me. My escort can have carts at the gate by midnight. They go south to Ustalav: some to my Lady's table, and the rest to the Way, who will stand them up again and teach them to serve. They will know no fear or fatigue, and no pit, and no lime. It is the kindest thing anyone will ever have done for them."
"You bequeathed me your own corpse for nothing. I want to see how freely you give somebody else's."''',
       c('[Give her the dead] "Take them. Nobody will count."', "give", alignment=("Evil", 2)),
       c('[Offer her demons instead] "There\'s a dead vrock in the south ditch. Take that, and anything else with horns."', "carrion"),
       c('[Refuse] "Those are owed to the Lady of Graves. Everything in this house is, except me."', "refuse")),
    el("give", '''{n}She does not thank you. She looks at you with her head a little on one side, the way she would look at a hound that had done something unusually clever.{/n}
"You did not even ask what the ones the Way stands up will remember." {n}She smiles, showing strong white teeth.{/n} "Nothing, since you wonder. Almost nothing."
{n}At midnight the carts come, as promised, and men in grey carry out the rows under their canvas one by one, without lanterns and without a word. By the second bell the long room holds nothing but lime dust and sixty-one rectangles where the floor is cleaner.{/n}''',
       c("Continue", "give2")),
    el("give2", '''"The chaplains will come in the morning with their prayers and their lime, and find a clean floor." {n}She dusts her hands.{/n} "Somebody will ask. Somebody always asks. You will have an answer ready, I expect; you are the kind who has one."
"Your chaplains will count the rows in their ledgers and find sixty-one fewer mouths to pray over. I doubt they will complain."''',
       c("Continue", "give3", requires=(E + "seelah_prayed",)),
       c("[Watch the carts go.]", flags=(TESTED, GAVE_DEAD, SECRET_DEAD), forbids=(E + "seelah_prayed",))),
    el("give3", '''"And that paladin of yours will count the rows in her head until she dies. She knelt by every one of them this morning. I would give a great deal to be there when she finishes counting."''',
       c("[Watch the carts go.]", flags=(TESTED, GAVE_DEAD, SECRET_DEAD))),
    el("carrion", '''{n}For a moment she only stares. Then her nostrils flare, as if you had put something rotten under her nose, which in a sense you have.{/n}
"Carrion." "You would send my Lady a vrock from a ditch. You would feed the queen of feasts on meat the crows turned down." {n}She looks at you for a long breath, and then, against her will, the corner of her mouth goes up.{/n}''',
       c("Continue", "carrion2")),
    el("carrion2", '''"Well. You are not squeamish, only stingy, and a stingy {mf|man|woman} guards {mf|his|her} larder. I can respect a larder." {n}She lets the canvas fall on the young face with the split lip.{/n}
"I will take the vrock's head. My wizards can do something with it, and it will amuse them. Your sixty-one may keep their pit." {n}A dry breath, not quite a laugh.{/n} "Carrion for cattle. I shall tell them in Caliphas that is how the Knight Commander haggles."''',
       c("[Let her have the head.]", flags=(TESTED, CARRION))),
    el("refuse", '''{n}She lowers the lantern. For a while she only looks at you, with those pale eyes that do not blink often enough.{/n}
"You guard what is owed." {n}Her voice has changed; there is no mockery in it at all.{/n} "Good. The grey warden is owed these, so you keep them for her, though she will never thank you. You have kept every one of these bodies out of my carts. I shall expect you to guard mine as closely."''',
       c("Continue", "refuse2")),
    el("refuse2", '''"I asked, Commander, because a {mf|man|woman} who would hand me sixty-one strangers for nothing would one day hand me to someone else for less." {n}She sets the lantern down on the nearest canvas, over a dead man's chest, as if it were a table.{/n}
"I do not care about your dead. I care what you do with things that are not yours. Now I know." {n}She almost smiles.{/n} "Go to bed. You smell of lime, and it does not suit you."''',
       c("[Leave her with the dead.]", flags=(TESTED, REFUSED_DEAD))),
], requires=(OWNED,), forbids=(TESTED,), delay=48, last=5)


# --- 5. The exchange of claims (T): the commit. -------------------------------------------------------------------------

WHISPERED = (
    c("Continue", "lied_secret", requires=(E + "whisper.lie",)),
    c("Continue", "true_secret", forbids=(E + "whisper.lie",)),
)

RITES_NOTE = '''"One thing more. While I am in your city my Lady's table will be laid in this house every seventh night, for those in Drezen who worship her and are careful. There are more of them than your priests would like." {n}Her eyes glitter.{/n} "You will know. You will say nothing. That is not a price, Commander. That is what it is to hold a claim on me."'''

visit(E + "commit.claims", "An exchange of claims", [
    nar("start", '''{n}The rows are gone from the long room, one way or another, and the trestle is back, laid for two. Tonight there is food on it: a haunch of venison seared black outside and red to the bone, a bowl of dark cherries, bread, a jug of wine thick enough to stain the cup. Elyanka is already eating. She eats the way she does nothing else, greedily, with her fingers, and the juice runs to her wrist.{/n}
"Sit," {n}she says, with her mouth full.{/n} "Eat. My Lady is the queen of the table as well as the grave. Nothing insults her like a guest who picks."''',
        c("[Eat with her.]", "story"),
        c('"Venison?"', "venison")),
    el("venison", '''"Venison." {n}She licks her thumb.{/n} "You have a suspicious mind, Commander. I like that in a debtor. It is a stag, from the woods north of your walls, shot without anybody's leave. That is how venison tastes best. I learned it when I was sixteen."''',
       c("[Eat with her.]", "story")),
    el("story", '''"When I was sixteen, strange people came to the Camilary woods and lit fires and sang, and ate stags my father's foresters had not given them. I followed the singing one night. They were priests of the Pallid Princess." {n}She tears the bread.{/n} "I went back every night after, to dance, and sing, and eat half-raw venison with the blood still in it. My father counted the deer we took. I counted the nights until I could go back."''',
       c("Continue", "story2")),
    el("story2", '''"My father's hunters followed me. They killed everyone at the fire except me. My father spared me, as he called it, and sent me to a house near Caliphas where they kept me in straps and starved me, to cure me of appetite. Three years. Then I walked home."
"That night we had lamb, baked with herbs, the way he liked it. He never noticed the bitterness. Mother, my three brothers, my six sisters: I gave them all my Lady's gift. Undeath." {n}She wipes her fingers, one by one.{/n} "All but him. Him I left in the ground, to rot like a peasant. He is still there. I visit."''',
       c('"And the Way? What does the Way want, in the end?"', "world"),
       c("Continue", "reason_gave", requires=(GAVE_DEAD,)),
       c("Continue", "reason_carrion", requires=(CARRION,)),
       c("Continue", "reason_refused", requires=(REFUSED_DEAD,)),
       c("Continue", "claim", forbids=(GAVE_DEAD, CARRION, REFUSED_DEAD))),
    el("world", '''"You have been too polite to ask until now. I wondered how long it would take." {n}She licks cherry juice from her thumb.{/n}
"Undeath is the truest and best form of existence. Eternity, and no fear of the end. Mortals, with their constant fear of dying, are cattle, fit for food and labour. Our dream is the death of the entire world, Commander. Purification. Life reviled by everyone who remains." {n}She says it as calmly as she would say the price of bread.{/n} "Not this year. Not while your demons are at the door. But one day."''',
       c('"And my corpse on your Lady\'s table helps it along."', "world_help"),
       c('"Then one day we\'ll be on opposite sides of the war."', "world_sides")),
    el("world_help", '''"A little. Everything helps a little." {n}She shrugs.{/n} "You gave me the claim anyway. You knew what I was when you whispered back the terms, and you whispered them. I have always thought that was the most interesting thing about you."''',
       c("Continue", "reason_gave", requires=(GAVE_DEAD,)),
       c("Continue", "reason_carrion", requires=(CARRION,)),
       c("Continue", "reason_refused", requires=(REFUSED_DEAD,)),
       c("Continue", "claim", forbids=(GAVE_DEAD, CARRION, REFUSED_DEAD))),
    el("world_sides", '''"One day." {n}She considers you, head a little on one side.{/n} "And on that day you will still be warm, and I will still hold your corpse, and you will have to decide whether to kill your creditor. I look forward to it. It will be the first honest quarrel anyone has had with me in years."''',
       c("Continue", "reason_gave", requires=(GAVE_DEAD,)),
       c("Continue", "reason_carrion", requires=(CARRION,)),
       c("Continue", "reason_refused", requires=(REFUSED_DEAD,)),
       c("Continue", "claim", forbids=(GAVE_DEAD, CARRION, REFUSED_DEAD))),
    el("reason_gave", '''"You gave me sixty-one strangers without asking what they would remember. A debtor as free with other people's bodies as that ought to know what it is to be handed one." {n}She wipes her fingers.{/n}''',
       *WHISPERED),
    el("reason_carrion", '''"You offered my Lady carrion from a ditch. You are stingy, Commander, and a stingy debtor guards the larder. So I will put something of mine in your larder, and see whether you guard it." {n}She wipes her fingers.{/n}''',
       *WHISPERED),
    el("reason_refused", '''"You kept the grey warden's dead from me, though she will never thank you for it. You pay your debts, even the ones nobody can collect. I have decided I want to be one of your debts." {n}She wipes her fingers.{/n}''',
       *WHISPERED),
    el("true_secret", '''"And in the dark you whispered me something true, and kept my secret after. Nobody keeps my secrets. They sell them to the Way, a whisper at a time."''',
       c("Continue", "claim")),
    el("lied_secret", '''"And in the dark you whispered me a lie, and I paid you a true secret for it anyway. You owe me one. Take the claim I am about to offer you, and I will call that debt paid. I want a creditor, not another confession."''',
       c("Continue", "claim")),
    el("claim", '''"I tell you this so you know what I do with a claim, Commander. You gave me a claim on your corpse. It is only good manners to give you mine."
{n}She leans across the table, as she did when you whispered the bequest, until her cheek is almost against yours.{/n} "When the Princess adopts me there will be nothing left of me to bury. She will take all of it, and I will never lie down anywhere. Take the claim anyway. Keep it. You will hold a claim on nothing at all." {n}Her breath is cold and smells of cherries.{/n} "I adore a bad bargain made with open eyes."''',
       c("[Take her claim] Whisper it back to her.", "yes"),
       c("[Kiss her instead of answering.]", "yes_kiss"),
       c('[Ask what she\'ll do with mine] "What will your Lady do with it, exactly? Mine."', "buyer")),
    el("yes", '''{n}You whisper it back into her ear, word for word, in the language older than its words. When you have finished she stays where she is a moment longer than the words require.{/n}
"There. Now each of us holds the other's corpse. Mine you will never collect; my Lady will leave nothing. Yours I will, one day, unless you cheat me." {n}She sits back and looks at you with open, hungry satisfaction, the way she looked at the venison.{/n} "How very Mendevian. Two debtors, and not a copper paid."''',
       c("Continue", "rites")),
    el("yes_kiss", '''{n}She catches the back of your neck with fingers sticky with cherry juice and draws you back to her mouth. Then she bites your lip, not gently, and pulls back.{/n}
"That is not how the Way seals anything," {n}she says, and licks the blood off her own mouth with evident enjoyment.{/n} "Say it properly." {n}And you whisper the claim back to her, word for word, with the taste of iron between you.{/n}
"There. Now each of us holds the other's corpse. Mine you will never collect. Yours I will, one day, unless you cheat me."''',
       c("Continue", "rites")),
    el("rites", RITES_NOTE,
       c("[Keep her secret.]", flags=(COMMITTED, SECRET_RITES)),
       c('"My priests have enough to pray about."', flags=(COMMITTED, SECRET_RITES))),
    el("buyer", '''{n}She draws back from you, not far, but completely, the way a cat steps back from a hand it has decided not to sniff.{/n}
"A buyer asks that." {n}Her voice is quite level.{/n} "{mf|A bridegroom|A bride} does not."
{n}She picks up her knife and goes back to the venison, and eats with the same appetite as before, as if you had already left.{/n} "You may finish your wine. I will think about what you are."''',
       c("[Finish your wine.]", flags=(DECLINED,))),
], requires=(TESTED, E + "beat.whisper"), forbids=(COMMITTED, DECLINED), delay=24, last=5)


# --- 6. Her move (T): the delayed return. No price. --------------------------------------------------------------------

visit(E + "commit.her_move", "A lock of grey hair", [
    nar("start", '''{n}She comes to your quarters after dark, alone, without her escort and without knocking, and nobody on your door saw her pass. When you look up she is standing by the table in her grey robe, turning your inkwell in her fingers as if pricing it.{/n}''',
        c("Continue", "hair")),
    el("hair", '''"Since that supper I have been deciding what you are." {n}She sets the inkwell down.{/n} "A buyer, I thought. A clerk with a sword, who wants to know where his goods will be kept. I kept telling myself that."
{n}From her sleeve she takes something small: a lock of silver-grey hair as long as your forearm, bound from end to end in black thread wound tight and knotted at every finger's width.{/n}''',
       c("Continue", "custom")),
    el("custom", '''"In my part of Ustalav, when a body is promised, the one who promises it cuts a lock and binds it in black, and gives it to the one who will bury it. So the grave knows whose it is to be." {n}She holds it out, not quite to you.{/n}
"I have never cut it for anyone. Not for my Lady, who will not need it. Not for the Way. Not for the priests in the woods, who were killed before I thought of it. I cut it this morning, for a debtor who asked me the wrong question at supper." {n}Her mouth twists.{/n} "I have decided not to care that you asked it. You will never be the one to bury me. Keep it anyway."''',
       c("[Take the lock of hair.]", "take"),
       c('[Send her home] "Go home to Ustalav, Elyanka. My body\'s yours when I die. Nothing else is."', "home")),
    el("take", '''{n}It is heavier than hair ought to be. The thread is waxed, and cold, and smells faintly of cloves.{/n}
"Good." {n}She watches you close your hand on it with the look she gave the venison.{/n} "Keep it somewhere you will see it, so you remember what you are holding. Now we each have a claim on the other. Mine on you will fall due one day; yours on me never will. You asked what I would do with your corpse. Now you have mine to worry about."''',
       c("Continue", "take_rites")),
    el("take_rites", RITES_NOTE,
       c("[Keep her secret, and the hair.]", flags=(COMMITTED, SECRET_RITES, LOCK))),
    el("home", '''{n}She puts the lock back into her sleeve without any hurry, as if she had only been showing you something in a shop.{/n}
"Your body is mine when you die, and nothing else is." {n}She repeats it slowly, tasting it.{/n} "Yes. That is all I offered you, too. How precise we both are."
{n}At the door she stops.{/n} "I will go home. The Way will keep the claim you gave it. And one day I will stand beside a hole with your name on it, Commander, and I will not weep, and nobody will ever know I once cut my hair for you."''',
       c("[Let her go.]", flags=(LEFT_FREE, CLOSED))),
], requires=(DECLINED,), forbids=(COMMITTED, LEFT_FREE), delay=48, last=5)


# --- 7. The hearse (T): desire, the threshold, the cut, and the morning. --------------------------------------------------

visit(E + "visit.hearse", "The velvet in the hearse", [
    nar("start", '''{n}The yard behind the dead-house has been lit with mourning candles, fat and black, set in the mud in a ring around the hearse like the flames around a bier. The horses are stabled. The glass sides of the carriage are misted from within.{/n}
{n}She is waiting at its open door, and she does not greet you. She looks you up and down, slowly, from your boots to your hair, in a way nobody has looked at you since the quartermaster measured you for armour.{/n}''',
        c("Continue", "inside")),
    el("inside", '''"It was built for you," {n}she says.{/n} "In Caliphas, from ebony and Varisian glass, at the Way's expense, the day we heard. Inside it is lined with velvet, so the body would not be bruised on the road. It has never carried anything." {n}She steps up and in, and holds the door.{/n}
"Get in, Commander. I want to see how you fit."''',
       c("[Climb in.]", "velvet"),
       c('"Do I have to lie still?"', "still")),
    el("still", '''"You could not if you tried. That is the whole trouble with you." {n}She takes you by the front of your coat and pulls you up the step.{/n}''',
       c("Continue", "velvet")),
    nar("velvet", '''{n}Inside it is close and dark and smells of cloves and new lacquer. The velvet is black, deep enough to sink a hand into, and the candles outside come through the misted glass as a ring of soft gold. There is just room for two, if one of them is lying down.{/n}
{n}She pushes you down into it with one hand flat on your chest, and kneels over you, and unlaces your collar as though she were dressing a body she means to keep: slowly, reading every scar with her thumbs.{/n}''',
        c("Continue", "scars")),
    el("scars", '''"This one will show well under the lamps of Ustalav." {n}Her thumb follows a line along your ribs.{/n} "This one I shall have to paint. This one," {n}lower,{/n} "is new. You have been careless since Iz."
{n}Her hands are cold. Your skin jumps under them. She draws her hand back, wrinkles her nose at the sweat, then lays it on you again. Her thumb presses beside the hammering pulse at your throat. She bends closer, watching your mouth.{/n}''',
       c('"You could wait until I\'m dead."', "wait"),
       c('"Is this what your Lady wants of you?"', "queen"),
       c("[Pull her down to you.]", "down")),
    el("queen", '''"My Lady is the queen of pleasure. Do you imagine I lit all those candles to pray over you?" {n}Her thumb stops on the pulse at your throat. She wrinkles her nose, but her knee presses closer against your hip.{/n}
"Warm. Sweating. And still looking at me as if you mean to eat. Very well, Commander. Let us see whether you have any manners."''',
       c("Continue", "down")),
    el("wait", '''"I could." {n}She bends until her mouth is at your ear, where she whispered the terms of the bequest.{/n} "I have waited for everything else in my life. I waited three years in straps. I have waited all these years for my Lady to take me." {n}Her teeth close on the lobe of your ear, hard enough to sting.{/n} "I am not waiting for this."''',
       c("Continue", "down")),
    nar("down", '''{n}She kisses the way she eats: greedily, without manners, her fingers knotted in your hair to hold your head where she wants it. She tastes of cold wine and cloves. She strips your shirt off you as if it had offended her, and your belt, and the rest, and throws it all into the dark end of the hearse where the feet of the dead would go.{/n}
{n}Then she sits back on her heels and unpins her grey robe at the shoulder, and lets it fall to her waist, and lower. The candlelight through the glass lays gold on her, on the long pale body she despises and feeds so well, and she lets you look at it as if it were a dish she had set down in front of you.{/n}''',
        c("Continue", "threshold")),
    nar("threshold", '''{n}She reaches for your belt to pull you down into the velvet, finds it gone, and laughs at herself, low, against your mouth, and pulls you down by the hips instead. Her body is cool everywhere yours is hot. She drags her nails down your chest to learn how fast you mark, and bites your throat where the pulse is loudest, and says into it, "Mine. Later. All of it." Then she rises over you in the gold light and kneels astride you, her knees sunk in the velvet on either side of your hips, and catches your mouth again.{/n}
{n}Her hands are everywhere at once, cold and dry and strong and entirely without shame: your chest, your thighs, the hard heat of you in her fist, which she studies with a connoisseur's greedy attention and a curl of her lip. "Revolting," she breathes. "Look at it. All that blood and nothing in its head." She laughs, high and cracked, and does not let go. When you reach up for her she slaps your hand away and then, on a second thought, puts it between her own thighs, where she is slick and rocking, and holds it there with her eyes narrowed, making you work.{/n}
"Do it properly. My Lady will hear of it if you do not." {n}She grinds against your fingers until her breath saws, then drags them away, shoves you flat against the velvet, braces both hands on your chest and rises on her knees, reaching down between you to take what she means to take.{/n}''',
        c("Continue", E + "visit.hearse.explicit.1")),
    nar("morning", '''{n}You wake late, alone in the velvet, stiff in places you did not know could stiffen, with a mourning candle guttering on the step. She is sitting outside on the shaft of the hearse in her grey robe, winding a length of black cord around her hand.{/n}
{n}It is knotted every finger's width, and there are a great many knots.{/n}''',
        c("Continue", "cord")),
    el("cord", '''"Your measurements," {n}she says, without looking up.{/n} "I took them in the night. Length, shoulders, the span of the hands, the girth of the chest breathing in and breathing out. You did not wake. You sleep like the dead, Commander; it is the most promising thing about you."
"For the claim." {n}She tucks the cord into her sleeve, beside the place where she keeps her knife.{/n} "The Way's joiners in Caliphas will want to know what they are building for. I will not have you arriving at my Lady's table in a box that pinches."''',
       c("Continue", "horses"),
       c("Continue", "horses", requires=(HORSES,)),
       c('"And last night?"', "last_night"),
       c("[Take your clothes back from the feet of the hearse.]", "clothes")),
    el("last_night", '''"Last night I did something disgusting with a living thing in a hearse, and I would do it again." {n}She finally looks at you, and the pale eyes are perfectly calm.{/n}
"Do not let it go to your head. You are still a sack of warm meat that smells of the stable. You are simply my sack of warm meat, and I intend to be there when it cools."''',
       c("[Go back to the war.]", "morning_exit", flags=(BIER,))),
    el("clothes", '''"You will find your shirt under the pillow. It is not a pillow; it is where the head rests." {n}She watches you dress with the professional attention of an undertaker, and something under it that is not professional at all.{/n}
"Go back to your war. Try not to lose any pieces I have measured."''',
       c("[Go back to the war.]", "morning_exit", flags=(BIER,))),
    nar("horses", '''{n}Her grooms bring the horses round to be harnessed, four black mares with plumes nodding. As you step down, the heavy glass door slips from your hand and bangs against the carriage. The nearest mare shies into her neighbour. All four rear and pull against the traces, dragging two grooms through the candles.{/n}
{n}It takes the men in grey half an hour to calm them. Nobody in the yard speaks to you while it happens. A groom catches the swinging door and holds it still. One mare keeps flinching from the glass whenever the harness rings.{/n}''',
        c("Continue", "horses2")),
    el("horses2", '''"They will get used to you," {n}Elyanka says, as the last mare is led away, still shivering,{/n} "or I will have them killed and buy horses who do not mind." {n}She considers you, standing half-dressed among the overturned candles.{/n}
"I find I mind less than they do. That is very inconvenient of me. Go back to your war."''',
       c("[Go back to the war.]", flags=(BIER, HORSES))),
    nar("morning_exit", '''{n}The grooms bring the harness out into the yard. Elyanka tucks the cord away and watches you step down.{/n}''',
        c("Continue", "horses"),
        c("Continue", "horses", requires=(HORSES,)),
        c("Continue", "horses", requires=(HORSES,)),
        c("[Go back to the war.]", flags=(BIER,), requires=(HORSES,), forbids=(*DAERAN_GONE, "daeran.plot_absent"))),
    # Slot brief: her chosen first night in the hearse; return to the existing morning.
    nar(E + "visit.hearse.explicit.1", '''{n}She catches your mouth again and draws you into the black velvet. Outside, the sentry calls the watch. Before dawn, the mourning candles burn down to their sockets.{/n}''',
        c("Continue", "morning")),
], requires=(COMMITTED,), forbids=(BIER,), delay=24, last=5)


# --- 8. Reactions (named companions with a stake: Daeran, a noble who buried his whole line; Seelah, who prayed over the
# Iz dead; Regill in elyanka_hearse). ------------------------------------------------------------------------------------

SCENES.append(reaction("Daeran", E + "react.daeran_door", ("trickster.ever", OWNED),
    '''{n}Daeran is examining his fingernails, as usual, and does not look up.{/n}
"There is a hearse in the yard of the dead-house by the south gate, Commander, lacquered, with glass sides, and a woman from Ustalav who tells anyone who asks that you have bequeathed her your corpse. In advance. For nothing. An excellent price, from her side of the table." {n}He turns his hand over and examines the other side.{/n}
"My family crypt is full of Arendaes who died without ever being worth a copper to anyone. Not one of them was ever made an offer. I find that I resent it on their behalf. If she wants a second body for the carriage, you will tell her I am available, and considerably better preserved."''',
    answer_list=DAERAN_HUB, chapter=5, last=5, entry='"About the hearse at the south gate."', portrait="Daeran",
    forbids=(*DAERAN_GONE, "daeran.plot_absent", BIER)))
tag(E + "react.daeran_door", "T")

SCENES.append(reaction("Daeran", E + "react.daeran_after", ("trickster.ever", BIER),
    '''{n}Daeran regards you for some time over the rim of his cup before he speaks.{/n}
"You slept in a hearse." {n}He says it slowly, savouring it.{/n} "With the undertaker. Who is a priestess of the Pallid Princess and has measured you for the table." {n}He sips.{/n} "After Heaven's Edge my family required rather a lot of funeral arrangements at once, Commander, and I learned the one rule of the funeral carriage that every Arendae kept to the letter: one does not get into it before the service. It is considered pushing."
"She will have no idea what to drink at a funeral that has not happened yet. Tell her the cellars of my house are at her disposal. I have ordered the first bottle sent to her yard. Every year, on the day they feasted you dead in Drezen, I shall send her a bottle older than she is. I want to watch her taste it and pretend she is above such things."''',
    answer_list=DAERAN_HUB, chapter=5, last=6, entry='"You\'re staring, Daeran."', portrait="Daeran",
    flags=(DAERAN_ALLY,), forbids=(*DAERAN_GONE, "daeran.plot_absent")))
tag(E + "react.daeran_after", "T")

SCENES.append(reaction("Seelah", E + "react.seelah_rows", ("trickster.ever", GAVE_DEAD, E + "seelah_prayed", "seelah.in_party"),
    '''{n}Seelah's knees are grey with lime. She does not seem to have noticed.{/n}
"The dead from Iz, Commander. The ones without names. I prayed over them the other morning, row by row, all sixty-one; I counted, because nobody else was going to." {n}She swallows.{/n} "Yesterday the chaplains went to bury them, and the dead-house was swept clean. Nobody saw carts. Nobody saw anything."
"Dead people don't get up and walk off. Not on our side of the wall." {n}Her jaw sets.{/n} "I'm going to find out who took them. I'd like you to help me. You're good at finding things out."''',
    answer_list=SEELAH_HUB, chapter=5, last=6, entry='"You look like you\'ve been kneeling in lime."', portrait="Seelah",
    forbids=("seelah_dead", "seelah_gone")))
tag(E + "react.seelah_rows", "T")


# --- 9. Secrets (the household's Ledger). -----------------------------------------------------------------------------

household.secret(
    "elyanka_siege_dead", "Sixty-one under canvas",
    "The unclaimed dead of Iz lay in the dead-house by the south gate, waiting for the chaplains, and I gave them to a "
    "priestess of Urgathoa to take to Ustalav or stand up again. The floor was swept clean by morning. Sooner or later "
    "somebody will count the rows. Seelah prays for the nameless dead; Targona can smell a necromancer's work from the "
    "other end of a street.",
    portrait="Elyanka", witnesses=("seelah", "targona"), risk="high")

household.secret(
    "elyanka_rites", "Her Lady's table",
    "While Elyanka is in Drezen, her goddess's table is laid in the dead-house every seventh night, for the Pallid "
    "Princess's worshippers in my own city. The worship of Urgathoa is legal nowhere in Avistan. I know, and I say "
    "nothing. Seelah and Targona would not forgive either of us.",
    portrait="Elyanka", witnesses=("seelah", "targona"), risk="high")


# --- 10. Epilogue pages (Owner ElyankaEpilogue, Chapter 6; read-only; no page Requires another). -------------------------
# The debt has a state for every ending: the bottle cheats it by the letter (Last Call: her coda and the Collectors page);
# without the bottle it stands unpaid while the Commander lives; the Wound leaves her nothing if it takes the Commander.

EPI = "ElyankaEpilogue"
ACTIVE = "lastcall.active"
BACK = "trickster.commander_back"


def page(id, title, text, requires, forbids=(), paragraphs=(), survived=True):
    """survived: the page waits for the Commander to have lived (or cheated death); lastcall adds its own Forbid to every
    epilogue that Requires the sacrifice."""
    extra = dict(ForbidOverrides={"sacrifice": BACK}) if survived else {}
    SCENES.append(scene(E + "epilogue." + id, title, EPI, 6, "", [nar("page", text, paragraphs=paragraphs)],
                        requires=("trickster.ever", *requires), forbids=tuple(forbids) + (("sacrifice",) if survived else ()),
                        last=6, Relationship=REL, **extra))
    tag(E + "epilogue." + id, "T")


# The claim, while the Commander lives: unpaid without the bottle; with it, Last Call's pages tell the rest.
UNPAID = (
    p('''{n}The claim never fell due. The Commander went on living, stubbornly and at length, and every year Elyanka came to look at the collateral as a moneylender looks at a ship that will not sink. "Unpaid," she would say, inspecting the Commander from across the table. "Still unpaid. You are the worst investment the Way has ever made."{/n}''',
      forbids=("sacrifice", ACTIVE, BACK)),
    p('''{n}The claim never fell due. The Commander had walked out of the end of the world laughing, and went on living, stubbornly and at length, and every year Elyanka came to look at the collateral as a moneylender looks at a ship that will not sink. "Unpaid," she would say. "Still unpaid. You are the worst investment the Way has ever made."{/n}''',
      requires=(BACK,), forbids=(ACTIVE,)),
)

COMMON = (
    p('''{n}In Caliphas, where the Way's teaching is passed by word of mouth, they still tell the story of the executor who sat through an entire wake in borrowed crepe to learn what the deceased was worth, and the envoy who laughed until she coughed. It is told in a whisper. It is never told the same way twice.{/n}''',
      requires=(BLUFFED,)),
    p('''{n}She never once looked at the Commander's face when a question mattered. She watched the hands, and the pulse at the throat, and on the rare nights she was pleased with what she saw, she said so to the hands.{/n}''',
      requires=(EXPOSED,)),
    p('''{n}The sixty-one unnamed dead of Iz were never buried. They went south to Ustalav in the Way's carts, some to a table and some to stand again in grey. The chaplains asked after them for a year, and were told nothing.{/n}''',
      requires=(GAVE_DEAD,), forbids=(E + "seelah_prayed",)),
    p('''{n}The sixty-one unnamed dead of Iz were never buried. They went south to Ustalav in the Way's carts, some to a table and some to stand again in grey. The Commander remembered Seelah counting them, row by row, before the carts went.{/n}''',
      requires=(GAVE_DEAD, E + "seelah_prayed")),
    p('''{n}The sixty-one unnamed dead of Iz went into the ground with lime and prayers. Elyanka attended the burial, at the back, in grey, and ate an apple all through the service, and told the Commander afterwards that it was the only honest debt she had ever seen a crusade pay.{/n}''',
      requires=(REFUSED_DEAD,)),
    p('''{n}The head of a vrock hung for years in a certain house in Caliphas, above a fireplace, with a card beneath it in no hand at all. Visitors from the Way who asked about it were told it was the Knight Commander's idea of an offering, and that the Knight Commander was not squeamish, only stingy.{/n}''',
      requires=(CARRION,)),
    p('''{n}She kept a drawing of the Commander's face, done in charcoal from everything about the Commander except the face, rolled in her sleeve. When she needed to know what the Commander really thought, she unrolled it and asked it. She said it had never once lied to her.{/n}''',
      requires=(E + "face.drawn",)),
    p('''{n}Once, in the dead-house, she had looked the Commander in the face for as long as it takes a candle to gutter and steady, and never again. She went on treating the Commander's face as a liar to the end, on principle, and the Commander went on letting her.{/n}''',
      requires=(E + "face.looked",)),
    p('''{n}There were men in the old granary by the north wall who died smiling, that winter, with a name on their lips the chaplains did not recognize. The Commander had let her in.{/n}''',
      requires=(E + "wards.let",)),
    p('''{n}The boy with one arm from the fever ward lived to be a baker in the lower town of Drezen. He never knew who had sat with him the night he did not die, or who had been sent away from his bed before she could win his prayers.{/n}''',
      requires=(E + "wards.stopped",)),
    p('''{n}She kept her word in the fever ward: the eleven, and not one more. The chaplains never learned why seven of their hopeless died so quietly. The Commander never told them.{/n}''',
      requires=(E + "wards.hopeless_only",)),
    p('''{n}She had cut a Deskari cultist open on a trestle to show the Commander what the Abyss does to meat, and the Commander had held the knife. She said afterwards that it was the most intimate thing she had ever done with a living person with her clothes on.{/n}''',
      requires=(E + "anatomy.knife",)),
    p('''{n}Once, in the dark end of the dead-house, a debtor and a creditor had whispered each other a secret, and neither of them ever repeated it. The Commander kept the Way's custom to the letter.{/n}''',
      any_groups=((E + "whisper.fear", E + "whisper.wake"),)),
    p('''{n}Once, in the dark end of the dead-house, the Commander had whispered her a lie, and she had heard it. She had given her own secret anyway. The Commander could still remember the cold of her cheek and the whisper: "You owe me one."{/n}''',
      requires=(E + "whisper.lie",)),
    p('''{n}The Commander remembered Seelah hearing the truth about the sixty-one from the mouth that had ordered their removal. The count went to the chaplains; a witness stood at the dead-house door. Elyanka had stayed out of the paladin's road.{/n}''',
      requires=(E + "inquiry.told_seelah",)),
    p('''{n}A resurrection man hanged at the south gate of Drezen for sixty-one bodies he never touched. The Commander remembered Seelah blocking the gallows steps with the carters' testimony, and the watch forcing her down under the Commander's seal. The Commander's order had kept her from stopping the carts, not from recording who sent them. The chaplains received the testimony; a witness stood at the dead-house door.{/n}''',
      requires=(E + "inquiry.misled",)),
    p('''{n}Elyanka told the paladin the truth about the sixty-one herself, in the dead-house yard, without one lie. The Commander remembered Seelah refusing the excuse that the dead could not suffer. She had taken the names and count to the chaplains and put a witness at the dead-house door. Neither culprit had received her forgiveness.{/n}''',
      requires=(E + "inquiry.hers",)),
    p('''{n}After the morning the hearse door banged, her black mares shied whenever its glass rattled. She sold them in the second spring and bought four grey ones. She made the Commander stand beside the door while she tried them, opening and shutting it until she was satisfied.{/n}''',
      requires=(HORSES,)),
)

# After the war, while she and the Commander still meet: the partner's page only.
LATER = (
    p('''{n}Every year on the day Drezen had feasted the Commander dead, a bottle arrived from the Arendae cellars, older than she was, with Daeran's compliments. She sneered at every one of them, and never once left a drop.{/n}''',
      requires=(DAERAN_ALLY,), forbids=(*DAERAN_GONE, "daeran.plot_absent")),
    p('''{n}A grey granite stone stood under the east wall of Drezen for many years, with the Commander's name on it and nothing under it. A woman in grey sat on it in the evenings and read, and the chaplains learned not to ask her why.{/n}''',
      requires=(E + "grave.stone_kept",)),
    p('''{n}Once, very early in the morning, a sentry on the east wall saw two people lying side by side on the grass of the burying ground, on an empty grave, with their hands folded, looking at the sky. He reported it. Nobody believed him, and he did not insist.{/n}''',
      requires=(E + "grave.lay",)),
    p('''{n}The stone the garrison of Drezen raised for the Commander was broken out of the ground by the crusade's own masons and went south in the hearse, wrapped in grey cloth. It stands now in a clearing in the Camilary woods, in the hills north of Caliphas, with the grass cut short around it and the hole beneath it dug and waiting.{/n}''',
      requires=(E + "grave.stone_down",)),
    p('''{n}There is a clearing in the birch woods north of Caliphas where the grass never grew back. She took the Commander there once, alive and walking and sweating up the hill, and was refused bread in three villages on the way, and said it was the best journey of her life, and made the Commander swear never to repeat that she had said so.{/n}''',
      requires=(E + "ustalav.promised",), forbids=("sacrifice",)),
    p('''{n}Some nights the Commander woke with the smell of cloves in the room, and a white flower on the pillow, and never saw who had left it. The sentries swore that nobody had passed.{/n}''',
      any_groups=((E + "night.feigned", E + "night.woke"),)),
)

HER_PARAGRAPHS = COMMON + LATER + UNPAID + (
    p('''{n}Somewhere north of Drezen, in the crooked woods above the walls, there is a clearing where two people once ate the heart of a stag that nobody had given them leave to kill. She went back to it every autumn. She never said whether she went alone.{/n}''',
      any_groups=((E + "hunt.ate", E + "hunt.sang"),)),
    p('''{n}She never sang again where anyone could hear. Once, a long time after the war, the Commander heard her humming in the dead-house yard, rough and tuneless, in the tongue they speak in the woods north of Caliphas, and stood very still in the gateway until she had finished, and never told her.{/n}''',
      requires=(E + "hunt.sang",)),
    p('''{n}A master of the Whispering Way went into a ditch on the Ustalav road, the season she held the Commander's claim, and did not come out of it. The next envoy came with armed attendants. She received them beside the hearse built for the Commander and refused to advance the collection by a single day. After that, every journey south needed an escort. She cursed the expense and kept her claim.{/n}''',
      requires=(E + "master.killed",)),
    p('''{n}A master of the Whispering Way went home to Caliphas under an escort of twelve crusaders, and told the Way exactly what he had seen in Drezen. The Way never forgot that the Commander had protected the man who came to hurry the Commander's death. It found the whole thing extremely interesting, and she lived under that interest for the rest of her life.{/n}''',
      requires=(E + "master.escorted",)),
    p('''{n}A master of the Whispering Way came to Drezen to hurry a debt and was never seen in Caliphas again. The Commander had given the matter to her. The Commander never asked what she did with it, and she never said.{/n}''',
      requires=(E + "master.hers",)),
    p('''{n}The Way's joiners in Caliphas finished the true table in ebony, carved with fruit and vines and little bones. It waited in a cellar there for the Commander, empty, year after year. The practice piece, the one the Commander had lain in, she kept in the dead-house, and ate from on her Lady's nights.{/n}''',
      requires=(E + "fitting.lay",)),
    p('''{n}The Commander never forgot her lying in her Lady's table with her hands folded, rigid on the red cloth, her silver hair spread beneath her. She never forgave the Commander for having seen it.{/n}''',
      requires=(E + "fitting.her_first",)),
    p('''{n}On certain nights she took out a flat wooden case of six painted girls with strong dark brows, and let the Commander sit with her while she looked at them, and did not say which was which.{/n}''',
      any_groups=((E + "sisters.asked", E + "sisters.let_be"),)),
    p('''{n}What she had whispered to the Commander about the Tyrant's seals, over wine, under a map, stayed where the Commander had put it. Some years it seemed to her that the Commander was saving it for something. She found that she did not mind being the thing that was saved for.{/n}''',
      requires=(E + "tyrant.kept",)),
    p('''{n}A knight of Lastwall rode for Gallowspire in the spring after the war, with a letter in a plain hand in his saddlebag, and questioned travellers about the Way. The warning named no attack and no weakness in the seals; it gave him a priestess's hopes to investigate. When word of the knight's questions reached her, she locked her map away and accused the Commander of spoiling her evenings.{/n}''',
      requires=(E + "tyrant.lastwall_warned",)),
    p('''{n}The Fool King of Drezen kept an old black coin in his paper crown, stamped with a skull and a crown, and told everyone it had been paid him by a lady for weeping. She came to his tavern exactly once, on a festival night, and stood at the back holding a napkin to her nose, and left before he could offer her the post of Royal Undertaker a second time.{/n}''',
      requires=(E + "king.bill_hers",)),
    p('''{n}Every year, a case of wine came from the Arendae cellars, and every year she sent back the same message, word for word, by a man in grey: *mediocre; did not finish it; send the rest.*{/n}''',
      requires=(E + "daeran.bottle_tasted",), forbids=(*DAERAN_GONE, "daeran.plot_absent")),
    p('''{n}A man in grey came up the Ustalav road from time to time with a message in her voice. Once it said only *come back hungry*, which the Commander had sent her first. She never explained why she had sent it back.{/n}''',
      requires=(E + "courier.come_back_hungry",)),
    p('''{n}The lock of silver-grey hair bound in black thread stayed where the Commander kept it. She never asked where that was. She was sure, she said, that it was somewhere the Commander would see it every day, because otherwise she would have to be angry, and she was too patient a creditor to waste anger on a debtor's drawer.{/n}''',
      requires=(LOCK,)),
    p('''{n}Her Lady's table was laid in the dead-house by the south gate every seventh night for as long as she was in Drezen, for the Pallid Princess's worshippers in a crusader city, and nobody in authority ever came to the door. When somebody did at last, years later, the Commander's name was the reason they went away again, and the lower town knew it, and said so in the taverns.{/n}''',
      requires=(SECRET_RITES,), forbids=(E + "inquiry.told_seelah", E + "inquiry.misled", E + "inquiry.hers", WRIT_UPHELD, WRIT_LIED, WRIT_HERS)),
    p('''{n}The Commander sat at that table more than once, and ate what was put on it, and never asked. She said it was the most romantic thing a living person had ever done for her, and that if it were repeated to anyone she would poison them.{/n}''',
      requires=(TABLE_SAT,)),
    p('''{n}On her Lady's nights the Commander kept the door of the dead-house, and nobody went in or out who had not been let. She called it the first useful thing she had ever seen a crusader do with a sword.{/n}''',
      requires=(TABLE_DOOR,)),
    p('''{n}The chaplains who came with a writ to put her out of Drezen went home again with her crusader's oath read aloud to them in full, and the Commander's name on the reason. They never forgave either of them.{/n}''',
      any_groups=((WRIT_UPHELD, WRIT_HERS),)),
    p('''{n}The chaplains who came with a writ to put her out of Drezen were told she was the Commander's embalmer and nothing more. She never forgave the Commander that lie. She had never been anybody's anything.{/n}''',
      requires=(WRIT_LIED,)),
    p('''{n}A bottle dispatched from the Arendae cellars during the crusade reached her with the funeral compliments still tied to its neck. She sneered at the card and never left a drop. She kept the empty bottle beside the measurement cord.{/n}''',
      requires=(DAERAN_ALLY,), any_groups=(("daeran.dead", "daeran.kicked_out", "daeran.plot_absent"),)),
    p('''{n}She kept the cork from the wine they had tasted in Drezen. When the Commander asked about it she repeated her verdict: *mediocre; did not finish it; send the rest.* She never threw it away.{/n}''',
      requires=(E + "daeran.bottle_tasted",), any_groups=(("daeran.dead", "daeran.kicked_out", "daeran.plot_absent"),)),
)

page("claim", "A claim, held", '''{n}Elyanka Camilary did not go home to Ustalav when the war was over. The Way had sent her to collect, she said, and a creditor who goes home before the debt falls due does not deserve to be paid. She kept the dead-house by the south gate of Drezen, and the hearse in its yard, and her Lady's appetites, all of them.{/n}
{n}The Pallid Princess did not adopt her that year, or the next. She stayed mortal, and useful, and furious about it, and she whispered her reports to Caliphas into the ears of couriers who forgot them by morning, all but the parts meant for the Way.{/n}
{n}When the Commander came to the dead-house she met them in the yard, kicked the hearse door shut on the two of them and tore the coat from their shoulders with the speed of a creditor unwrapping an overdue parcel. She wrinkled her nose at the smell of warm living skin, every time. She raked her nails down the Commander's chest to watch the red come up, cackled, bit the throat where the pulse was loudest, and whispered what she meant to do with their corpse and what she meant to do with the rest of them first. She shed the grey robe, hauled the Commander down across the velvet, straddled them, and pulled the Commander close anyway, every time. What each of them held of the other stayed where it was, whispered and unwritten.{/n}''',
     requires=(COMMITTED,), paragraphs=(
         p('''{n}Hers was a claim on a corpse that would one day be hers; the Commander's, a claim on a corpse that would never be anybody's.{/n}''',
           forbids=(ACTIVE,)),
         p('''{n}The death in the flask had not yet made a corpse payable. Elyanka kept the bequest, and the Commander kept hers. Two claims, neither surrendered. She said it was the most honest marriage she had ever seen.{/n}''',
           requires=(ACTIVE,)),
     ) + HER_PARAGRAPHS)

page("debt", "A claim, outstanding", '''{n}The war ended before Elyanka Camilary had finished deciding what the Commander was, beyond a debtor. She did not give the Commander her own claim. She did not need to; she already held the only one that mattered to her.{/n}
{n}She went back to Ustalav in the hearse that had been built for the Commander's corpse, empty, with the curtains open. Every spring after that it came up the road to Drezen again, and stood in the dead-house yard for a week, and she inspected the collateral from across a table, and wrinkled her nose at it, and went home.{/n}''',
     requires=(OWNED,), forbids=(COMMITTED, DECLINED, CLOSED), paragraphs=COMMON + UNPAID + (
         p('''{n}Once, in the fourth spring, she stayed a second week. Nobody could say why, least of all the Commander. She did not explain.{/n}''',
           requires=(TESTED,)),
         p('''{n}Once, late, over the dregs of a bottle, she said that she had meant to give the Commander her own claim, in the spring of the Threshold, and that the war had simply ended too soon. Then she said she had been joking, and wrinkled her nose at the smell of the Commander's life, and left the next morning as usual.{/n}''',
           requires=(TESTED,)),
         p('''{n}The terms were never repeated aloud. They did not need to be. On the day the Commander died, whenever that was, a woman in grey would be at the graveside, and would collect what the Commander had bequeathed.{/n}''',
           forbids=(ACTIVE,)),
         p('''{n}The terms were never repeated aloud. They did not need to be. The Commander's death was in a flask, and the flask was in the Commander's pocket, and she inspected the collateral every spring anyway, in case the cork had slipped.{/n}''',
           requires=(ACTIVE,)),
     ))

page("lock", "A lock of grey hair", '''{n}The war ended before Elyanka Camilary had decided what to do about a debtor who had asked her the wrong question at supper. She decided anyway, the spring after the Threshold, in the only way the Way knows how to decide anything: in person, and in a whisper.{/n}
{n}She came up the Ustalav road in the hearse, and walked into the Commander's rooms without knocking, and laid a lock of silver-grey hair on the table, bound from end to end in black thread and knotted at every finger's width. In Ustalav, she said, that is what you give to the one who will bury you. She had never cut it for anyone.{/n}
{n}What the Commander did with it, and what she did after, belongs to the years after the war.{/n}''',
     requires=(DECLINED,), forbids=(COMMITTED, CLOSED), paragraphs=COMMON + UNPAID)

page("left_free", "Sent home", '''{n}Elyanka Camilary went home to Ustalav with a whispered claim on the Commander's corpse and nothing else, and never came to Drezen again. The Way kept the claim the Commander had given it. It is patient; it has been waiting since the Tyrant fell for things far more interesting than one mortal's death.{/n}
{n}She never wrote to the Commander; what she had to say, she would not trust to paper. But once a year, on the day Drezen had feasted the Commander dead, a courier in grey came to the south gate and said, word for word, in Elyanka's voice: "Still unpaid. I have not forgotten where you are kept."{/n}''',
     requires=(LEFT_FREE,), paragraphs=COMMON + (
         p('''{n}The grey stone the garrison had raised for the Commander stayed under the east wall of Drezen, over nothing. She had asked for it once, and had it, and left it where it stood when she went. Nobody sat on it in the evenings after that.{/n}''',
           any_groups=((E + "grave.stone_kept", E + "grave.lay"),)),
         p('''{n}A grey Mendevian stone with the Commander's name on it went south in her hearse, and stands in a clearing in the Camilary woods over a hole dug and waiting. She never sent word of it. The Commander learned of it years later, from a pedlar, and did not know whether to laugh.{/n}''',
           requires=(E + "grave.stone_down",)),
         p('''{n}The claim never fell due while the Commander lived. She never came to look at the collateral. Once, at a crossroads inn in Ustalav, a traveller from Drezen mentioned the Knight Commander's name at the next table, and a woman in grey paid for his supper and left before it came.{/n}''',
           forbids=("sacrifice", ACTIVE)),
     ))

page("eaten", "The Wound ate my claim", '''{n}Word came to Drezen that the Commander of the Fifth Crusade had given everything at the Threshold, and that the Wound had closed on what was given. There was no body to carry home. The Wound had taken it with everything else.{/n}''',
     requires=(OWNED, "sacrifice"), forbids=(BACK,), survived=False, paragraphs=(
         p('''{n}Elyanka Camilary had watched it happen from the last ridge above the rift, where the Commander had told her to stand, with her hearse and her six. When it was over there was nothing to go down and fetch. She stood on the ridge for a day and a night without eating, which nobody who knew her would have believed. On the second morning she said, to nobody, "The Wound ate my claim," and turned the hearse that had been built for the Commander's corpse south, empty.{/n}''',
           requires=(E + "collateral.at_rift",)),
         p('''{n}Elyanka Camilary heard it in the dead-house by the south gate of Drezen, where she had waited with one candle, as the Commander had told her to. She sat on the shaft of the hearse for a day and a night without eating, which nobody who knew her would have believed. On the second morning she said, to nobody, "The Wound ate my claim," and harnessed the horses herself, and drove the hearse home to Ustalav, empty.{/n}''',
           requires=(E + "collateral.in_drezen",)),
         p('''{n}The claim the Commander had given the Way could not be collected. No body came back from Threshold.{/n}''', requires=(LEFT_FREE,)),
         p('''{n}Elyanka Camilary heard it in the dead-house by the south gate of Drezen, from a sergeant who did not know what else to do with the news. She sat on the shaft of the hearse for a day and a night without eating. On the second morning she said, to nobody, "The Wound ate my claim," and drove the hearse that had been built for the Commander's corpse home to Ustalav, empty.{/n}''',
           forbids=(E + "collateral.at_rift", E + "collateral.in_drezen", LEFT_FREE)),
         p('''{n}She did not weep. She was hungry, and she stayed hungry.{/n}'''),
         p('''{n}She asked for the lock of hair she had cut for the Commander back from the Commander's effects, and in Caliphas she laid it on her father's grave, where she visits, and left it there to rot, like a peasant. It was the only thing she ever buried.{/n}''',
           requires=(LOCK,)),
         p('''{n}Somewhere she kept a claim on her own corpse that nobody would ever collect. She said, once, that the Commander had got the better bargain after all: the only debtor she had ever heard of who cheated the Way by dying properly.{/n}''',
           requires=(COMMITTED,)),
         p('''{n}Nobody wrote it down. But in the Whispering Way's house in Caliphas they still say, in a whisper, that one mythic corpse was bequeathed to them in Drezen and never delivered, and that the envoy who held the claim never asked for another.{/n}''',
           forbids=(COMMITTED,)),
         p('''{n}The stone the garrison had raised for the Commander under the east wall of Drezen stayed where it was, over nothing, as it always had. Once a year a woman in grey came and sat on it for an afternoon, and read, and did not weep, and went away again.{/n}''',
           requires=(E + "grave.stone_kept",)),
         p('''{n}In a clearing in the Camilary woods, north of Caliphas, a grey Mendevian stone with the Commander's name on it stands over a hole that will never be filled. She had it filled in, in the end, with earth and nothing else, and planted a white flower on it, and never went back.{/n}''',
           requires=(E + "grave.stone_down",)),
     ))

page("turned_away", "A hearse on the Ustalav road", '''{n}A black hearse with glass sides came up the Ustalav road to Drezen once, in the year of the Fifth Crusade, to buy a corpse, and went back down it empty.{/n}
{n}The Whispering Way does not forget a door that was shut in its face. It simply waits for the house to fall down.{/n}''',
     requires=(DOOR_SEEN, CLOSED), forbids=(OWNED,), paragraphs=(
         p('''{n}It went back between twelve crusaders of the border escort. At the edge of the camp the woman inside asked the sergeant whether the Knight Commander had been buried with the eyes open or shut, and said she would ask again another time. She never did.{/n}''',
           requires=(ESCORTED,)),
         p('''{n}The woman inside had sat at a trestle in the dead-house by the south gate and told her order's purpose to a veiled executor who then would not sell. She never learned whose face was under the crepe. She said it did not matter; the Way would ask again another time.{/n}''',
           requires=(REFUSED_VEILED,)),
         p('''{n}The woman inside had sat at a trestle in the dead-house by the south gate, watched the late Knight Commander take off a veil, and laughed until she coughed, and then been refused. She did not laugh on the road home.{/n}''',
           requires=(REFUSED_UNVEILED,)),
         p('''{n}The woman inside had caught the Knight Commander at a wake in a borrowed coat, and been refused by the owner. She took the wine jug with her, and it was never seen again, and neither was she.{/n}''',
           requires=(REFUSED_CAUGHT,)),
         p('''{n}The woman inside had sat at a trestle in the dead-house by the south gate and watched the corpse she came for walk in to supper, sweating, and refuse to bequeath its remains. She wrinkled her nose at the memory for years.{/n}''',
           requires=(REFUSED_SUPPER,)),
     ))


# --- Registration --------------------------------------------------------------------------------------------------------

def _bind(payload, kind, table):
    for key, value in table.items():
        have = payload.setdefault(kind, {}).get(key)
        if have is not None and have != value:
            raise ValueError("Conflicting binding: " + key)
        payload[kind][key] = list(value) if isinstance(value, list) else value


def integrate(payload):
    """Register the funeral reads (SeenCues) and their latch, the Derived keys and the portrait fallback. Scenes are added by
    expansion.py; the verified world keys (iz.done, fool_king.*, daeran.*, seelah.*, regill.*) bind on demand in
    trickster_world."""
    _bind(payload, "SeenCues", SEEN_CUES)
    _bind(payload, "Latches", LATCHES)
    # Native current absence, not a historical promise: DaeranNotInParty_AccordingToThePlot.
    _bind(payload, "Etudes", {"daeran.plot_absent": "d80bdee55139ac24583f337a53878021"})
    for key, groups in DERIVED.items():
        have = payload.setdefault("Derived", {}).get(key)
        if have is not None and have != [list(g) for g in groups]:
            raise ValueError("Conflicting derived key: " + key)
        payload["Derived"][key] = [list(g) for g in groups]
    from storylines import trickster_world
    for key in sorted({IZ_DONE} | {k for groups in DERIVED.values() for g in groups for k in g}):
        if key in trickster_world.BINDINGS and not trickster_world._bound(payload, key):
            kind, guid, _ = trickster_world.BINDINGS[key]
            payload.setdefault(kind, {})[key] = [guid] if kind in trickster_world.LIST_KINDS and isinstance(guid, str) else guid
    payload.setdefault("PortraitFallbacks", {}).setdefault("Elyanka", PORTRAIT_GUID)

# NM1 item 10 (ideal-run C13): a returned Seelah coexists; her death/departure forbids lift on her return.
for _s in SCENES:
    if _s.get("Id") == E + "react.seelah_rows":
        _s.setdefault("ForbidOverrides", {}).update({"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"})


# Authored job-2 ending: departure leaves a creditor in Ustalav, not in Drezen.
page("left_free_mourned", "A claim without a body",
     '{n}The news reached Elyanka Camilary in Ustalav, months late, by a man in grey. '
     'She had gone home when she was sent, with a claim and nothing else. She heard him out, '
     'then said, "The Wound ate my claim." She did not eat for a day and a night. '
     'The Way kept the whispered account; there was no flesh to fetch.{/n}',
     requires=(LEFT_FREE, OWNED, "sacrifice"), forbids=(BACK,), survived=False)


# endings1: recorded death and available corpse are distinct under the bequest.
for _suffix in ("claim", "debt"):
    _ep = next(s for s in SCENES if s["Id"] == E + "epilogue." + _suffix)
    _nd = _ep["Nodes"][0]
    for _para in _nd.get("Paragraphs", []):
        if ACTIVE in _para["Requires"] and ("flask" in _para["Text"]):
            _para["Requires"].append("lastcall.bottled_held")
            _para["Forbids"].append("lastcall.dead_on_record")
    _nd["Paragraphs"].extend([
        p('{n}The death notice made Elyanka present her bequest. The returned body was living; possession was refused. She kept the claim contested, and watched the corked flask without pretending it erased the death.{/n}', requires=(ACTIVE, "lastcall.recovered_corked")),
        p('{n}Elyanka examined the stranger behind closed curtains. The flask was empty and the death remained in Pharasma\'s book. She had demanded her corpse; no corpse had been delivered. She kept the bequest contested and the stranger\'s name to herself.{/n}', requires=("iomedae.trickster.buried_alive",)),
    ])
# end endings1

# Authored round-3 consequence: the existing inquiry watch also sees the rites.
HER_PARAGRAPHS_WATCH = p('''{n}Her Lady's table was still laid every seventh night. The witness at the dead-house door counted the guests and took their names to the chaplains. Elyanka made him stand outside while her worshippers ate, and sent the bones out under his lamp. The Commander's protection kept her in Drezen; it did not silence the testimony.{/n}''', requires=(SECRET_RITES,), any_groups=((E + "inquiry.told_seelah", E + "inquiry.misled", E + "inquiry.hers"),))
next(s for s in SCENES if s["Id"] == E + "epilogue.claim")["Nodes"][0]["Paragraphs"].append(HER_PARAGRAPHS_WATCH)

# Round-4: prayer/counting alone does not establish the performed chalk inquiry.
for _ending in ("claim", "debt", "lock", "left_free"):
    next(s for s in SCENES if s["Id"] == E + "epilogue." + _ending)["Nodes"][0]["Paragraphs"].append(
        p('''{n}The Commander remembered the sixty-one chalk marks on the dead-house floor after the inquiry. Elyanka had swept around them; a witness had stood at the door.{/n}''',
          requires=(GAVE_DEAD,), any_groups=((E + "inquiry.told_seelah", E + "inquiry.misled", E + "inquiry.hers"),))
    )
