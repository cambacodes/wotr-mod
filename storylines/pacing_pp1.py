"""Pacing pass PP1 (Writer/handoffs/13-PACING-PASS.md sections 2, 4 and 7): Anevia, Irabeth and Seelah.

Early beats (Prologue to Chapter 2) and Seelah's Chapter 4 night, each a single native moment with a real choice for her,
plus the later scene in her merged route that reads it (the consequence, appended here; choices are append-only).
Every beat is path-neutral (N-all): no Trickster gate, no romance promise, no native key set. Ids are save references.

Hosts (every list is referenced by one dialog only; blueprint reference scan, 2026-10-01):
  anevia.early.watch   Prologue, Neathholm, the evening before the first sleep: HorgusAnevia AnswersList_0006 65395d82,
                       pinned by FreeTime ec82016f Playing (the native "How did you sleep?" needs it Completed, and her
                       answer, Cue_0030 691df61c "slept like a log... with a covering", then plays as the morning after).
                       Return Cue_0032 3103585f (narrator: the argument goes on); retcheck OK.
  seelah.early.pack    Prologue caves, after Seelah finished the lift herself: MeetSeelahAnevia AnswersList_0018 da6ca505,
                       pinned by SeenCues Cue_0013 deb9827d / Cue_0054 d94978ee. Return Cue_0017 843c7cf2; retcheck OK.
  irabeth.early.hands  Chapter 1, Defender's Heart lost: AfterAttackIrabeth AnswersList_0006 4c756b62 (only on the DHLost
                       branch). Return-to-list: Cue_0004 5687ef84 is UNSAFE (it continues).
  irabeth.early.hook   Chapter 2, Lost Chapel, after the hooks: IrabethRegill AnswersList_0019 b6f91435. Return-to-list:
                       Cue_0015 16cbc0b4 is UNSAFE; Cue_0027 1b0741f2 is safe but would be heard twice.
  seelah.early.drill   Chapter 1, Defender's Heart party: SeelahMeetsFriends AnswersList_0007 f1e7b7a6. Return-to-list:
                       Cue_0006 a3d0b31d would replay the mug and the introduction.
  seelah.abyss.night   Chapter 4, after "How are you holding up?" (Answer_0119 829801b1, SelectedAnswers): Seelah companion
                       AnswersList_0118 73260c45. Return-to-list: Cue_0123 1b5f5780 would repeat the line she just said.
Anevia's Prologue ankle beat (13 section 2) is dropped: canon has her splint it herself (MeetSeelahAnevia Cue_0015, Cue_0039),
its host list a55fc20c is shown while she is still pinned, and the Neathholm night carries the leg with a native payoff.
"""
from story_format import c, n, scene

SCENES = []

NEATHHOLM_LIST = "65395d8277d3b9b4f82f068616de8a56"   # HorgusAnevia/AnswersList_0006
NEATHHOLM_RETURN = "3103585f1550def4c98fbc731ccb3ebc"  # HorgusAnevia/Cue_0032
NEATHHOLM_AREA = "61fcf2a352daa394ebae399b1348ba62"    # World/Areas/Act_0_Prologue/Prologue_Neathholm (FreeTime's area)
CAVES_LIST = "da6ca50574b6c714f9166f37b64b7b59"       # MeetSeelahAnevia/AnswersList_0018
CAVES_RETURN = "843c7cf25f27714439e8dbb6cab06074"     # MeetSeelahAnevia/Cue_0017
HEART_LOST_LIST = "4c756b62bc1fcda42b8122f215a9ddd4"  # AfterAttackIrabeth/AnswersList_0006 (DHLost only)
CHAPEL_LIST = "b6f914354ceddbf4db19747f12ea4f0d"      # IrabethRegill/AnswersList_0019
PARTY_LIST = "f1e7b7a6740caaa44a3762033c5f0a5a"       # Ch1_SeelahMeetsFriends/AnswersList_0007
ABYSS_LIST = "73260c45aa315c0419fc625f6fcb957d"       # Companions/CompanionDialogues/Seelah/AnswersList_0118

ANEVIA_PROLOGUE = "ea562adea1736874c9c5616d140fe773"  # Units/.../Prologue_Neathholm/AneviaTirabade
HORGUS = "c02e641bf8cf0984fb49604afa224563"           # Units/.../DefendersHeart/Horgus (his Neathholm cues)
SEELAH = "54be53f0b35bf3c4592a97ae335fe765"           # Units/Companions/Seelah/Seelah_Companion
IRABETH_DH = "48cc2d6daf65f014781f6ea76c2565bc"       # Units/.../DefendersHeart/IrabethTirabade_DH
IRABETH_CHAPEL = "758596d3dbc112d40aa1a2fc64991076"   # Units/.../LostChapel/IrabethTirabade_LostChapel
REGILL = "68d4a5b150c7c2c42aeea6f24044113a"           # Units/.../HellknightVsGargoyles/Regill_HellknightVsGargoyles
JANNAH = "588418cb0dfd7cb45b6e6d370ef42bea"           # Units/.../DefendersHeart/DH_SeelasFriend_DeserterJanna

# Native keys read (bound in trickster_world.BINDINGS).
EVENING = "neathholm.evening"                  # FreeTime Playing
SEELAH_LIFTED = "prologue.seelah_finished_lift"  # SeenCues Cue_0013 / Cue_0054
HOLDING_UP = "seelah.abyss_holding_up"         # SelectedAnswers Answer_0119

# Outcome flags: every terminal path sets exactly one; every first-node choice sets the beat's .seen.
WATCH = "anevia.early.watch."
WATCH_OUT = tuple(WATCH + v for v in ("splinted", "fumbled", "covered", "horgus", "waved"))
PACK = "seelah.early.pack."
PACK_OUT = tuple(PACK + v for v in ("tipped", "lifted", "kept", "returned"))
HANDS_OUT = ("irabeth.early.steadied", "irabeth.early.dismissed_help")
HOOK = "irabeth.early.hook."
HOOK_OUT = tuple(HOOK + v for v in ("shouldered", "thanked_regill"))
DRILL = "seelah.early.drill."
DRILL_OUT = tuple(DRILL + v for v in ("floored", "landed", "deferred"))
NIGHT = "seelah.abyss.night."
NIGHT_OUT = tuple(NIGHT + v for v in ("listened", "drilled", "halved"))

BEATS = {"anevia.early.watch": WATCH_OUT, "seelah.early.pack": PACK_OUT, "irabeth.early.hands": HANDS_OUT,
         "irabeth.early.hook": HOOK_OUT, "seelah.early.drill": DRILL_OUT, "seelah.abyss.night": NIGHT_OUT}


def seen(beat):
    return beat + ".seen"


def beat(id, title, owner, chapter, entry, nodes, relationship, outcomes, **extra):
    extra.setdefault("forbids", ())
    extra["forbids"] = tuple(extra["forbids"]) + (seen(id),) + tuple(outcomes)
    forbids = extra.pop("forbids")
    requires = extra.pop("requires", ())
    SCENES.append(scene(id, title, owner, chapter, entry, nodes, requires=requires, forbids=forbids, last=chapter,
                        optional=True, Relationship=relationship, Chapters=[chapter], **extra))


# Anevia, Prologue: the evening in Neathholm. Her native morning line ("slept like a log... with a covering") is the payoff.
S = seen("anevia.early.watch")
beat("anevia.early.watch", "A covering for the night", "Anevia", 0,
     '"That rock floor will have your leg screaming by midnight."', [
    n("start", "Anevia", '''{n}Anevia has her splinted leg propped on a sack of something that clanks. Horgus Gwerm sits as far from her as the cave allows, which is not nearly far enough for either of them.{/n}
"Midnight? Generous. It's been screamin' since the rubble. I've just stopped answerin' it."
{n}She taps the twine she knotted round the splint after you got her out. One knot has already worked loose.{/n}
"The locals smeared somethin' on it that smells like a goat's last regret, and told me to wait a day. So I'm waitin'. Unless you've got a better offer than Mr. Gwerm's. His is complainin' on my behalf."''',
      c('[Lore (Nature) DC 14] "Let me redo the splint. Twine won\'t hold through a night on stone."', flags=(S,),
        check=dict(Skill="SkillLoreNature", DC=14, Success="splint", Failure="fumble")),
      c('"The villagers had a spare blanket. I asked for it before anyone else could."', "blanket", flags=(S,)),
      c('"Then I\'ll leave you to Mr. Gwerm\'s offer."', "waved", flags=(S,)),
      speaker_unit=ANEVIA_PROLOGUE, portrait="Anevia"),
    n("splint", "Anevia", '''{n}You cut the twine, reset the sticks so the break sits between them instead of under one, and pad the whole thing with a strip torn from the hem of your shirt. Anevia hisses once, when you straighten the foot, and then says nothing at all, which from her is a compliment.{/n}
"Huh."
{n}She flexes her knee. The splint stays where you put it.{/n}
"That's better than the chirurgeon in Kenabres managed last time. He tied it so tight my toes went blue, and then billed the Eagle Watch for the toes."
{n}She lowers the leg back onto the clanking sack, gingerly, and looks up from it at you.{/n}
"Where'd you learn that? No, don't tell me. Everybody's got a past. I'll find yours out the honest way, by pryin'."''',
      c('[Leave her to rest.]', flags=(WATCH + "splinted",)), speaker_unit=ANEVIA_PROLOGUE, portrait="Anevia"),
    n("fumble", "Anevia", '''{n}You cut the twine, tear a strip from the hem of your shirt for padding, and reset the sticks. The moment you let go, the whole arrangement slides sideways off her shin. Anevia catches it before it hits the floor.{/n}
"Right. Well. You've got good intentions and terrible knots. That's most of the crusade, to be fair."
{n}She ties it back herself, quick and practised, the way she did after you got her out, and holds up the strip of your shirt.{/n}
"I'll keep this, though. It's softer than the sack."''',
      c('"Keep it. Sleep, if you can."', flags=(WATCH + "fumbled",)), speaker_unit=ANEVIA_PROLOGUE, portrait="Anevia"),
    n("blanket", "Anevia", '''{n}You hold it out. It is not much of a blanket: grey, thin, and smelling powerfully of whatever lives in these caves. Anevia looks at it, and then past it, at Horgus.{/n}
"Give it to him."
{n}She says it loud enough for him to hear.{/n}
"Go on. If he's warm he might stop talkin'. I'd take a quiet Gwerm over a warm leg any night, and that's the truth."''',
      c('"It\'s yours. Mr. Gwerm has a mansion to go home to."', "covered"),
      c('[Give the blanket to Horgus.]', "horgus"), speaker_unit=ANEVIA_PROLOGUE, portrait="Anevia"),
    n("covered", "Anevia", '''"Had a mansion," {n}Anevia says, before Horgus can.{/n} "Last anybody checked."
{n}She takes the blanket anyway and pulls it up over her knees. Horgus opens his mouth, considers the blanket, considers her, and shuts it again. It will not last.{/n}
"There. Now I owe you for the bedding. Keep this up and I'll have to start a ledger."''',
      c('[Leave her to rest.]', flags=(WATCH + "covered",)), speaker_unit=ANEVIA_PROLOGUE, portrait="Anevia"),
    n("horgus", "Horgus", '''{n}Horgus receives the blanket the way he might receive a bill from a tradesman he suspects of padding it. He holds it at arm's length, sniffs it, and drapes it over his knees with an air of great sacrifice.{/n}
"I suppose it is better than nothing. Marginally."''',
      c('[Look at Anevia.]', "horgus_anevia"), speaker_unit=HORGUS),
    n("horgus_anevia", "Anevia", '''{n}Across the cave, Anevia grins at the ceiling.{/n}
"See? Quiet already. Give it a minute. He'll find somethin' else."''',
      c('[Leave them to it.]', flags=(WATCH + "horgus",)), speaker_unit=ANEVIA_PROLOGUE, portrait="Anevia"),
    n("waved", "Anevia", '''"Coward."
{n}She says it fondly, settling back against the wall and folding her arms.{/n}
"Go on, then. Somebody in this cave should get some sleep. Not before I've finished this argument, mind."''',
      c('[Leave her be.]', flags=(WATCH + "waved",)), speaker_unit=ANEVIA_PROLOGUE, portrait="Anevia"),
], "anevia", WATCH_OUT, requires=(EVENING,), Areas=[NEATHHOLM_AREA], AnswerLists=[NEATHHOLM_LIST],
     NativeReturnCue=NEATHHOLM_RETURN)


# Seelah, Prologue: she finished the lift herself, and the pack is still on her back.
S = seen("seelah.early.pack")
beat("seelah.early.pack", "A pack mule's wages", "Seelah", 0,
     '"You moved most of that hillside yourself. Give me the pack."', [
    n("start", "Seelah", '''{n}Seelah is still breathing hard. She wipes her brow with the back of her wrist and leaves a streak of grit there.{/n}
"Me? I'm fine! I'm a paladin, not a pack mule."
{n}She hitches the pack higher on her shoulders, winces, and gives you a sidelong look.{/n}
"Though if you're volunteering to be one, I'm not going to stand in the way of your calling."''',
      c('[Athletics DC 12] "Hand it over. I\'ll carry it to the surface if I have to."', flags=(S,),
        check=dict(Skill="SkillAthletics", DC=12, Success="carried", Failure="dropped")),
      c('"Then keep it. I wouldn\'t want to rob a paladin."', "kept", flags=(S,)),
      speaker_unit=SEELAH, portrait="Seelah"),
    n("carried", "Seelah", '''{n}You take the pack. It is heavier than it looks: a whetstone, a prayer book, a coil of rope, and something wrapped in oilcloth that clinks. You shoulder it without a stumble.{/n}
"Look at you. A natural."
{n}Seelah rolls her freed shoulders with a groan of pure bliss. Then she fishes in a pocket and presses something small and cold into your palm: a brass button, embossed with a crest you don't recognise. You turn it over, and she answers before you can ask.{/n}
"Your wages. No idea whose it was. Some nobleman's. It came off a tavern floor a long time ago, when I was a different girl." {n}She winks.{/n} "I've been meaning to give it to somebody honest for years. You'll do."''',
      c('[Pocket the button.]', flags=(PACK + "tipped",)), speaker_unit=SEELAH, portrait="Seelah"),
    n("dropped", "Seelah", '''{n}You take the pack. It is heavier than it looks, and the cave floor is wet. Your boot goes one way and the pack goes the other, and Seelah catches it by the strap before it can roll into the dark.{/n}
"Whoa! Easy. That's the only prayer book I've got."
{n}She swings it back onto her own shoulders with a grin, and pats your arm. Something tugs at your belt as her hand moves away. She holds up the brass stud from your belt pouch between two fingers.{/n}
"There. Still got the fingers for it." {n}She is trying very hard not to look pleased with herself.{/n} "You'll want to watch your pockets down here. Not everyone's as nice as me."''',
      c('"Keep it. You can owe me a game for it."', "lifted"),
      c('"I\'ll have that back, thank you."', "returned"), speaker_unit=SEELAH, portrait="Seelah"),
    n("lifted", "Seelah", '''"A game! Done." {n}She tucks the stud into her own pocket and pats it.{/n} "I'll look after it. Better than you did, anyway."''',
      c('"Lead the way."', flags=(PACK + "lifted",)), speaker_unit=SEELAH, portrait="Seelah"),
    n("returned", "Seelah", '''{n}She drops it into your palm at once.{/n}
"Of course. I only borrow from friends to make a point." {n}A pause.{/n} "That was the point. Watch your pockets."''',
      c('"Lead the way."', flags=(PACK + "returned",)), speaker_unit=SEELAH, portrait="Seelah"),
    n("kept", "Seelah", '''"Good. I'd have had to fight you for it, and then where would we be? Two of us in a hole, and one of us sulking."
{n}She tightens the straps, rolls her neck until it cracks, and nods at the dark ahead.{/n}
"Thanks for asking, though."''',
      c('"Lead the way."', flags=(PACK + "kept",)), speaker_unit=SEELAH, portrait="Seelah"),
], "seelah", PACK_OUT, requires=(SEELAH_LIFTED,), AnswerLists=[CAVES_LIST], NativeReturnCue=CAVES_RETURN)


# Irabeth, Chapter 1: the Defender's Heart has fallen ("We... lost..."), and her sword hand will not stop shaking.
S = seen("irabeth.early.hands")
beat("irabeth.early.hands", "Five breaths", "Irabeth", 1,
     '"Irabeth. Your hands."', [
    n("start", "Irabeth", '''{n}Irabeth looks down as though the trembling belongs to somebody else. The battered sword shakes in her grip. She lowers it, and it goes on shaking against her greave.{/n}
"They are fine."
{n}Her jaw sets.{/n}
"Give me a report instead. What did you see outside? How many of ours are still standing out there?"''',
      c('[Take the sword out of her hand.] "Five breaths first. Then the report."', "breaths", flags=(S,)),
      c('"Fewer than we need. The survivors are gathering in the streets."', "report", flags=(S,)),
      speaker_unit=IRABETH_DH, portrait="Irabeth"),
    n("breaths", "Irabeth", '''{n}For a moment you think she will not let go. Then her fingers open, all at once, and the sword is in your hand: notched, sticky to the cross-guard, and heavier than it ought to be.{/n}
{n}Irabeth breathes. You count with her, under your breath, because she plainly will not let herself be seen counting. Somewhere around the third breath her hands stop shaking. By the fifth she has taken the sword back.{/n}
"That was insubordinate."
{n}She wipes the blade on her sleeve.{/n}
"Thank you. Now. Since you are so fond of giving instructions, you can see the wounded moved away from the doorway, in case they come back. Anevia would say I have just punished you for kindness. Anevia would be right."''',
      c('"Consider it done."', flags=("irabeth.early.steadied",)), speaker_unit=IRABETH_DH, portrait="Irabeth"),
    n("report", "Irabeth", '''{n}She takes it like a blow she expected, and then visibly puts it to use.{/n}
"Gathering. Good. Then they need somewhere to gather to."
{n}The shaking has not stopped. She sheathes the sword so you cannot see it.{/n}
"When we are done here, take the door. Whoever comes through it, I want to know before they are inside. I will manage."''',
      c('[Agree to take the door after the briefing.]', flags=("irabeth.early.dismissed_help",)), speaker_unit=IRABETH_DH, portrait="Irabeth"),
], "irabeth", HANDS_OUT, AnswerLists=[HEART_LOST_LIST], ReturnToList=True,
     ReturnText="{n}Irabeth turns back to the hall and the people left in it.{/n}")


# Irabeth, Chapter 2: off the hook, swaying; the Paralictor's hand on her bracer, and his verdict that nobody would come.
S = seen("irabeth.early.hook")
beat("irabeth.early.hook", "The other arm", "Irabeth", 2,
     '[Get your shoulder under her other arm.]', [
    n("start", "Narrator", '''{n}The gnome's hand is still clamped on Irabeth's bracer. It is the only thing keeping her upright, and it is not enough. You get your shoulder under her other arm a moment before her knees go.{/n}
{n}She is heavier than she looks, all armour and wet mail. The wound the hook left is still bleeding.{/n}''',
      c('[Hold her up.]', "her", flags=(S,))),
    n("her", "Irabeth", '''"Don't... mind the wound. Don't touch it. I'm..."
{n}She gets her feet under her on the second try and turns her head, slowly, to look at you, and then at the Hellknight on her other side.{/n}
"He said you would not come. He said it would be... the correct decision."''',
      c('"He was wrong. Lean on me."', "wrong"),
      c('"He caught you when I took you down. Thank him."', "thanks"), speaker_unit=IRABETH_CHAPEL, portrait="Irabeth"),
    n("wrong", "Irabeth", '''{n}Irabeth leans. It costs her, and she does it anyway, one gauntleted hand fisted in your cloak.{/n}
"You were wrong, Paralictor."''',
      c('[Wait for Regill.]', "wrong_regill"), speaker_unit=IRABETH_CHAPEL, portrait="Irabeth"),
    n("wrong_regill", "Regill", '''{n}Regill does not look at either of you. He is examining the bite on his neck with clinical disinterest.{/n}
"My prediction was incorrect. My assessment of the risk was not." {n}He lowers his hand.{/n} "We will see which of us the rest of this campaign agrees with, Commander."''',
      c('[Keep her steady.]', flags=(HOOK + "shouldered",)), speaker_unit=REGILL),
    n("thanks", "Irabeth", '''{n}Irabeth turns to the gnome. It takes her a while.{/n}
"Thank you, Paralictor. You held me when I would have fallen."
{n}A wet breath, and the ghost of something like humour.{/n}
"You may thank me for the healing when we are outside."''',
      c('[Wait for Regill.]', "thanks_regill"), speaker_unit=IRABETH_CHAPEL, portrait="Irabeth"),
    n("thanks_regill", "Regill", '''{n}Regill looks at her as if she has handed him a form filled out in the wrong ink.{/n}
"Gratitude is noted. Stand, knight. You can thank people on level ground."''',
      c('[Keep her steady.]', flags=(HOOK + "thanked_regill",)), speaker_unit=REGILL),
], "irabeth", HOOK_OUT, AnswerLists=[CHAPEL_LIST], ReturnToList=True,
     ReturnText="{n}Irabeth draws a wet, careful breath, and stands between the two of you.{/n}")


# Seelah, Chapter 1: the League's party at the Defender's Heart. She teaches the way she learned.
S = seen("seelah.early.drill")
beat("seelah.early.drill", "Not like a knight", "Seelah", 1,
     '"You fight like someone who learned it somewhere other than a tiltyard."', [
    n("start", "Seelah", '''{n}Seelah lowers her mug, delighted.{/n}
"You noticed! Most people see the armour and think I was born in it." {n}She is already on her feet, pushing the bench back with one boot.{/n} "Want to learn to fight like you mean it? Not like a knight. Like somebody who has to get home tonight."
{n}Elan raises his eyebrows. Curl starts clearing mugs out of the way with the speed of long practice.{/n}
"Watch. A knight comes straight at you." {n}She flicks her eyes to your face, drops her weight, and in the same breath she is not in front of you any more but at your left side, her shoulder an inch from your ribs.{/n} "I don't. Eyes high, feet low, and go where they aren't guarding. Now you. Slowly! I'm showing you, not killing you."''',
      c('[Ignore the feint. Go straight in.]', "floored", flags=(S,)),
      c('[Eyes high, weight low, and go for her off side, the way she just did.]', "landed", flags=(S,)),
      c('"Not tonight. Teach me when the city isn\'t on fire."', "deferred", flags=(S,)),
      speaker_unit=SEELAH, portrait="Seelah"),
    n("floored", "Seelah", '''{n}You go straight in. She is not there. Something hooks your ankle, a shoulder meets your chest, and the floor of the Defender's Heart arrives with great enthusiasm.{/n}
{n}Above you, Jannah winces on your behalf. "That isn't fencing, Seelah," she says. "That's a tavern."{/n}
"Correct! Tavern." {n}Seelah offers you her hand and hauls you up.{/n} "Lesson one: the other fellow has feet too. Look at them. Everyone looks at the sword."''',
      c('[Dust yourself off.]', flags=(DRILL + "floored",)), speaker_unit=SEELAH, portrait="Seelah"),
    n("landed", "Seelah", '''{n}You give her your eyes high and your weight low, the way she gave them to you a moment ago, and come in on the side she isn't guarding. Your shoulder catches hers. She staggers, laughing, into Curl, who saves the mugs.{/n}
"Oh! Who taught you that?" {n}She points at herself.{/n} "Me. Thirty heartbeats ago. I'm a wonderful teacher."
{n}Jannah applauds, slowly, with the air of a woman reserving judgement.{/n}''',
      c('[Take a bow.]', flags=(DRILL + "landed",)), speaker_unit=SEELAH, portrait="Seelah"),
    n("deferred", "Seelah", '''"Fair. Very fair." {n}She drops back onto the bench, though she does not stop grinning.{/n} "But I'm holding you to it. One lesson, when the city's not on fire. I'll remember. I always remember who owes me a lesson."''',
      c('"Deal."', flags=(DRILL + "deferred",)), speaker_unit=SEELAH, portrait="Seelah"),
], "seelah", DRILL_OUT, AnswerLists=[PARTY_LIST], ReturnToList=True,
     ReturnText="{n}Seelah sits back down and pushes your mug toward you again.{/n}")


# Seelah, Chapter 4 (in person): she wakes at night to screams that aren't there (Seelah Cue_0121). The beat stays in the
# present conversation: what is agreed or done now; the nights themselves are not narrated here.
S = seen("seelah.abyss.night")
beat("seelah.abyss.night", "Nothing out there", "Seelah", 4,
     '"Next time you wake up to it, wake me."', [
    n("start", "Seelah", '''"And say what? 'Commander, there's nobody screaming. Come and listen to it with me'?"
{n}She tries to make it a joke, and it nearly works. Then she rubs her eyes with the heels of her hands.{/n}
"You need sleep more than I do. You're the one everybody's following."''',
      c('"Then we listen now. Both of us. If there\'s nothing there, there\'s nothing."', "listen", flags=(S,)),
      c('"Or wake me and we drill, like you showed me at the Heart. Until you\'re too tired to dream."', "drill",
        flags=(S,), requires=("seelah.early.drill.seen",), forbids=(DRILL + "deferred",)),
      c('"You still owe me a lesson. Nothing here is on fire, exactly."', "drill",
        flags=(S,), requires=(DRILL + "deferred",)),
      c('"Then let me take half your watch tonight. You can sleep through the half that matters."', "halved", flags=(S,)),
      speaker_unit=SEELAH, portrait="Seelah"),
    n("listen", "Seelah", '''{n}She hesitates, then nods. The two of you step away from the others, out of earshot, and listen.{/n}
{n}The Abyss is not silent. Something far off grinds like a millstone. The air carries a smell of rot and hot copper. But there is no screaming. You listen together until she is sure of it.{/n}
"Nothing," {n}she says at last.{/n} "There's nothing."
{n}She doesn't sound relieved, exactly. She sounds like someone who has set down a weight and is still feeling the shape of it in her arms.{/n}
"All right. If it comes tonight, I'll wake you. And you'll come and hear nothing with me again. Promise?"''',
      c('"Promise."', flags=(NIGHT + "listened",)), speaker_unit=SEELAH, portrait="Seelah"),
    n("drill", "Seelah", '''{n}Seelah stares at you, and then gives a tired laugh.{/n}
"That's a terrible idea. That's the best idea anyone's had in days."
{n}She doesn't wait for night. She finds a patch of grey grit out of everyone's way and puts you on your back twice, dirty and fast, before you get anywhere near her. The third time you nearly have her, and she lets you see her notice.{/n}
"There. Now I'm tired. Ask me again tonight, if I'm up. I'll be up."''',
      c('[Get up and agree.]', flags=(NIGHT + "drilled",)), speaker_unit=SEELAH, portrait="Seelah"),
    n("halved", "Seelah", '''"Half." {n}She considers it like a merchant considering a coin she suspects of being clipped.{/n} "The first half. You'll be up before the screaming starts, if it starts, and if it doesn't, you'll tell me so in the morning."
{n}She points at you.{/n}
"And you'll wake me if you hear anything at all. Not the Abyss noises. The other ones. You'll know."''',
      c('"I\'ll know."', flags=(NIGHT + "halved",)), speaker_unit=SEELAH, portrait="Seelah"),
], "seelah", NIGHT_OUT, requires=(HOLDING_UP,), forbids=("inhuman",), AnswerLists=[ABYSS_LIST], ReturnToList=True,
     ReturnText="{n}Seelah straightens her shoulders and looks back at you, a little steadier.{/n}")


# Consequences: one appended choice (and its node) in a named later scene of her merged route, per outcome family.
CONSEQUENCES = {
    # The Neathholm night, recalled in her first Drezen-hub sitting: she hands the Commander the fresh cup first.
    "a_cup": ("start", [
        (c('"I hope that cup is warmer than Neathholm."', "neath_splint", requires=(WATCH + "splinted",)),
         n("neath_splint", "Anevia", '''{n}Anevia laughs, and before you can sit she pours from the pot at her elbow and puts the fresh cup in your hands, keeping the cold one for herself.{/n}
"There. Fresh one's yours. I'll have the stewed. You knelt on a rock floor and reset my leg with a strip of your own shirt. That's worth the good cup."
{n}She stretches the leg out under the table, heel down, and turns the foot to show you.{/n}
"Healers here said whoever set it knew what they were about. I told 'em it was a stranger who wouldn't say where they'd learned it. They didn't believe me either."''',
           c('"Then tell me something I haven\'t rescued you from."', "bread"))),
        (c('"Do you still have that strip of my shirt?"', "neath_strip", requires=(WATCH + "fumbled",)),
         n("neath_strip", "Anevia", '''{n}Anevia grins, pours from the pot at her elbow and puts the fresh cup in your hands before you can sit. She keeps the cold one.{/n}
"Fresh one's yours. And no, I don't. I used it to tie up a cut on a guard's arm, and he bled on it, and that was the end of your shirt."
{n}She stretches the leg out, heel down, and turns the foot to show you.{/n}
"Terrible knots, good intentions. I told the healers about you. They said most of their patients come in with a friend like that."''',
           c('"Then tell me something I haven\'t rescued you from."', "bread"))),
        (c('"Warmer than a Neathholm blanket, I hope?"', "neath_cover", requires=(WATCH + "covered",)),
         n("neath_cover", "Anevia", '''{n}Anevia snorts into her cup, then pours from the pot at her elbow and puts the fresh one in your hands before you can sit. She keeps the cold one.{/n}
"Fresh is yours. Neathholm rates. I slept like a log that night, under that horrible grey thing, and woke up with my leg still attached and Gwerm still talkin'. Two miracles."
{n}She tips her head at you.{/n}
"You thought to fetch it. I noticed."''',
           c('"Then tell me something I haven\'t rescued you from."', "bread"))),
        (c('"Did Mr. Gwerm ever thank you for that blanket?"', "neath_gwerm", requires=(WATCH + "horgus",)),
         n("neath_gwerm", "Anevia", '''{n}Anevia snorts into her cup, then pours from the pot at her elbow and puts the fresh one in your hands before you can sit. She keeps the cold one.{/n}
"Fresh is yours. Neathholm rates. And thank me? He sent a note after. Three lines. Two of 'em were about the smell. The third said 'the Commander has peculiar notions of charity.'"
{n}She grins.{/n}
"From him, that's practically a love letter. I slept like a log that night, by the way. Best trade I ever made."''',
           c('"Then tell me something I haven\'t rescued you from."', "bread"))),
    ]),
    # The Defender's Heart, recalled in i_hands, the scene about her hands.
    "i_hands": ("start", [
        (c('"They\'ve stopped shaking, at least."', "dh_steady", requires=("irabeth.early.steadied",)),
         n("dh_steady", "Irabeth", '''{n}Irabeth's fingers go still on the glove. Then she flattens her hand on the table between you, palm down, and looks at it.{/n}
"They have."
{n}A pause.{/n}
"You took the sword out of my hand in the Defender's Heart and counted my breathing like a midwife. I have still not decided whether to thank you for it or put you on a charge."
{n}She takes up the needle again.{/n}
"Anevia says I should do both, in that order. She says it is how I show affection."''',
           c('"I can live with both."', "ordinary"))),
        (c('"No orders for me tonight? Last time you put me on the door."', "dh_wall",
           requires=("irabeth.early.dismissed_help",)),
         n("dh_wall", "Irabeth", '''{n}Irabeth's mouth tightens, and then, unexpectedly, softens.{/n}
"I did." {n}She pulls the thread through.{/n} "I remember thinking you had seen my hands and decided, very sensibly, not to mention them. I was grateful. I did not say so. I am saying so now."
{n}She holds up the glove, and the bead of blood on her fingertip.{/n}
"They still do it, sometimes. Not tonight."''',
           c('"Good."', "ordinary"))),
    ]),
    # The Lost Chapel, recalled in i_respite (Chapter 3), the first sitting where she brings nothing that can become a report.
    "i_respite": ("start", [
        (c('"You told a Hellknight he was wrong while you were bleeding on his boots."', "chapel_wrong",
           requires=(HOOK + "shouldered",)),
         n("chapel_wrong", "Irabeth", '''{n}Irabeth puts a counter down on the wrong square, and leaves it there.{/n}
"I did. Anevia has made a song of it. There are four verses. I have asked her to stop at three."
{n}She looks up.{/n}
"You came. He was quite certain you would not, and he is not often wrong about what people will do. I think that is why I said it. I wanted to be the one to tell him."''',
           c('"You don\'t have to solve anything here."', "still"))),
        (c('"Did Regill ever answer your thanks?"', "chapel_note", requires=(HOOK + "thanked_regill",)),
         n("chapel_note", "Irabeth", '''"He did." {n}Irabeth's mouth twitches.{/n} "In writing. One word. 'Received.' I keep it in my desk. Anevia wanted to frame it."
{n}She turns a button between her fingers.{/n}
"You were right to make me say it. He kept me from falling in that room, and I had spent the last of my healing on him, so perhaps we are even. He would never have mentioned either. Some debts are better paid in front of witnesses."''',
           c('"You don\'t have to solve anything here."', "still"))),
    ]),
    # The caves, recalled in the wager: one of her three buttons.
    "seelah.wager": ("start", [
        (c('"One of these is mine. The stud off my belt pouch, from the caves."', "button_mine",
           requires=(PACK + "lifted",)),
         n("button_mine", "Seelah", '''{n}Seelah looks at the two in your hand, and the brass stud among them, as if it has betrayed her.{/n}
"So it is. I said you could owe me a game for it, and here's the game." {n}She grins.{/n} "Hit the cup and it's yours again. I'll even sew it back on. Badly."''',
           c('"And if I miss?"', "terms"))),
        (c('"Is one of those your nobleman\'s button? I still have the one you paid me with."', "button_tip",
           requires=(PACK + "tipped",)),
         n("button_tip", "Seelah", '''"You kept it!" {n}She is ridiculously pleased.{/n} "Most people spend their wages." {n}She nods at the two she has given you.{/n} "No, these are honest buttons. Mostly. Put yours in with them. Three again, since one's under the crate. Winner chooses the evening."''',
           c('"What did you have in mind if you won?"', "terms"))),
    ]),
    # The Abyss night, recalled when the stolen souls have opened their eyes and she is counting them again.
    "seelah.souls": ("start", [
        (c('"In the Abyss you woke to screaming nobody else heard. Do you still?"', "abyss_night",
           requires=("seelah.abyss.night",)),
         n("abyss_night", "Seelah", '''{n}Seelah's hand goes still on the shield.{/n}
"Sometimes. Less than I did." {n}She almost smiles.{/n} "It helped, not being the only one awake for it."
{n}She sets the cloth down.{/n}
"When I learned what Sunhammer had done, I started wondering whether those cries I'd imagined were theirs. And now they're here, and they're breathing, and I'm still listening for them. Stupid."''',
           c('"Not stupid."', "hurt"))),
    ]),
}


def integrate(payload):
    """Append the consequence choices and nodes to their reading scenes (save-safe: new choices go last)."""
    scenes = {s["Id"]: s for s in payload["Scenes"]}
    for scene_id, (node_id, rows) in CONSEQUENCES.items():
        target = scenes[scene_id]
        nodes = {node["Id"]: node for node in target["Nodes"]}
        for choice, node in rows:
            if node["Id"] in nodes:
                raise ValueError("pacing_pp1: node %s already in %s" % (node["Id"], scene_id))
            nodes[node_id]["Choices"].append(choice)
            target["Nodes"].append(node)
            nodes[node["Id"]] = node
            if not node.get("Portrait") and node["Speaker"] in ("Anevia", "Irabeth", "Seelah"):
                node["Portrait"] = node["Speaker"]
