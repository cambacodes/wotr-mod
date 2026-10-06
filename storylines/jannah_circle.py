"""Jannah: the spine between her return and her challenge (the forms, Houndheart, the wall), and the optional beats around it.

Every physical scene is at her presence in the last cell of the old Drezen gaol (jannah_trickster PRESENCE); the wall is a
night alarm on the watch she asks for there (Q6 follow-up: no spine scene depends on the mod's book). Each beat engages a canon anchor of hers:
- the Aldori swordlords and Mivon: "To earn the right to stay, the applicant must pass a series of increasingly
  difficult duels" (glossary cbbb769f); the Aldori "focuses on avoiding damage and disarming foes" (e6df7926); "I'm an
  apprentice of a famous fencing master from Mivon... My father would say that's no accident. Fate brought me here."
  (Seelah Q1 3f001f86); "I wonder if they miss me back home in Mivon..." (c85ab91e);
- Houndheart: the League of the Inspiring Cart (2f96db80), Elan's ring and the raid on the Houndhearts' camp (909ca452,
  cf0cdc7e), "No glory without risk!" and "It was my first real battle against actual demons" (Deserter/Cue_0019
  35f2823a, Cue_0015 423ff883), and the flight north toward Numeria (78c0efc7);
- Seelah: "I thought you'd never want to see me again..." (ktc_DeserterJoins/Cue_0006 2cd7cc44); "When we were in the
  Molten Scar, Jannah told me that I was the reason she deserted" (5096ed4d); Seelah told of her death: "That is not
  justice!" (CompanionDialogues/Seelah/Cue_0105 166223b5); Elan's death at the jeweller's (ElanDying/Cue_0014 3246cb05);
- the vrocks who caged her (Deserter/Cue_0002 ef6fcb8d, Cue_0005 fe9fa40a);
- "Am I lucky, or what?" (52169bb4), used once, bitterly, when the Commander earns it.
Acknowledgments of other women are in Jannah's voice only; no scene between partners.
"""
from story_format import c, scene
from storylines.jannah_trickster import (CAUGHT, CLOSED, COMMITTED, CONDEMNED, DEAD_KNOWN, DEAD_L, DREZEN, ELAN_DEAD, FORMS,
                                         FREE, GONE, HH_HONEST, HH_LUCKY, HH_STAND, HOUNDHEART, JOINED, LIED, MIVON_LEGEND,
                                         MIVON_TRUTH, NAMELESS, NIGHT, POSTING, PRESENCE, PRISON, PUBLIC_YIELD, REL, RETURNED,
                                         SCAR, SEELAH_BACK, SEELAH_DEAD, SEELAH_FOR_HER, SEELAH_GONE, SEELAH_HERSELF,
                                         SEELAH_KEPT, SHE_FIRST, STORY_LOST, STRANGER, UNIT, WALL_SALUTE, WALL_SHIELD, WALL_WATCHED, WALLS, YOU_FIRST, FIRST_LOSS, SWORD_GIVEN, SEELAH_KILLED_AT_CAGE,
                                         jan, nar)

SCENES = []
C = "jannah.circle."

BLADE = C + "blade"
SEELAH = C + "seelah"
MIVON = C + "mivon"
KENABRES = C + "kenabres"
WATCH = C + "the_watch"
SPARRING = C + "measure"
SALT = C + "salt"
FORD = C + "ford"
YOUR_TALE = C + "your_part"
RIDE = C + "houndhearts_camp"
IRABETH = C + "one_question"
YIELD_CIRCLE = C + "yielding_the_circle"
TAUGHT = C + "eyes_open"
REPLY = C + "fate_again"
AFTER_WALL = C + "anything_but_wings"
BLADE_HELD = C + "blade.held"
SPAR_KISSED = C + "measure.kissed"
TALE_SPENDS = C + "your_part.spends_people"
RIDE_BESIDE = C + "houndhearts_camp.beside"
YIELDED_CIRCLE = C + "yielded_the_circle"
CURL = C + "curl"
SOULS_HOME = "seelah.souls_returned"   # Q6 r2 (CAN): Curl came home with the souls (SeelahInDoubt/Cue_0005, Cue_0038)
VROCKS = C + "the_ritual"
MASTER = C + "the_old_man"
RECRUITS = C + "recruits"
TRACE = C + "once"
SONG = C + "the_song"
BOARD = C + "the_board"
DOOR = C + "the_door"
STAIRS = C + "the_stairs"
PAPER = C + "the_answer"
NOTCH = C + "the_right_way"
LAST_MUSTER = C + "before_the_last_road"
MEASURE_FLIRT = C + "forms.flirted"
TOLD_PLANNED = C + "forms.told_planned"
WATCH_STOOD = C + "watch.stood"


def meet(id, title, entry, nodes, requires=(RETURNED,), forbids=(), delay=24, optional=True, **extra):
    """A physical beat at her cell; each happens once."""
    SCENES.append(scene(id, title, "Jannah", 5, entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, GONE, id, *forbids))), delay=delay, last=5,
                        optional=optional, Relationship=REL, Chapters=[5], ContactUnit=UNIT, Areas=[DREZEN],
                        InteractionHub=PRESENCE, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=24, optional=True, **extra):
    """A night in which she is there in person, delivered at a rest."""
    SCENES.append(scene(id, title, "Jannah", 5, "", nodes, requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, GONE, id, *forbids))), delay=delay, last=5,
                        optional=optional, Relationship=REL, Remote=True, Kind="visit", Chapters=[5], ManualOnly=True, **extra))   # Q6 r2 (COX)


# --- 1. The forms (spine): what she keeps like a faith, taught properly. ---------------------------------------------------

meet(FORMS, "The forms", '"You\'re drawing circles again."', [
    nar("open", '''{n}She has begged a stick of chalk off the quartermaster's clerk, and the circle on the cell floor is white now, and exact. She is standing in the middle of it in her stockings, running a sequence against nobody: three steps, a turn of the wrist, a recovery, over and over, slow enough to count.{/n}''',
        c("Continue", "scar", requires=(SCAR,)),
        c("Continue", "story", forbids=(SCAR, STORY_LOST)),
        c("Continue", "story_won", requires=(STORY_LOST,), forbids=(SCAR,))),
    jan("story_won", '''"If you're going to keep coming down here, you're going to learn them properly." {n}She finishes the sequence before she looks at you.{/n}
"You lost to me with your mouth. Don't take that to mean you know what losing to me in a circle feels like. You don't. Yet."''',
        c('"Then teach me."', "salute")),
    jan("scar", '''"If you're going to keep coming down here, you're going to learn them properly." {n}She finishes the sequence before she looks at you.{/n}
"You knew Mivon, in the Scar. Its founding, its duels, the Aldori way. You asked me how the old man ended his bouts, and then you used his answer on me. So tell me: where did you learn Mivon?"''',
        c('"From a book. A very dull one."', "book"),
        c('"I read you through the bars before I opened my mouth. The rest I learned standing there."', "planned", flags=(TOLD_PLANNED,)),
        c('[Lie] "I\'ve crossed blades with Aldori before."', "lie")),
    jan("story", '''"If you're going to keep coming down here, you're going to learn them properly." {n}She finishes the sequence before she looks at you.{/n}
"You caught me in a story. That isn't the same as catching me in a circle, and I'd hate for you to get the two confused. It could be fatal."''',
        c('"Then teach me."', "salute")),
    jan("book", '''"A book." {n}She looks personally offended.{/n} "Somebody wrote Mivon down. In a book. For anybody to read." {n}She shakes her head.{/n}
"My master would have had him flogged with the binding. Well. It saved my life, so I suppose the flogging can wait."''',
        c("Continue", "salute")),
    jan("planned", '''"Through the bars." {n}She stops moving.{/n}
"You stood outside that cage and read me. My feet. My hands. The way I hold my head when I'm frightened. Then you said the forms back to me in my master's words, and made the challenge he'd have made, and I rose to it like a trout to a fly."
{n}Something moves behind her eyes, and she doesn't let it out.{/n} "That's either the most flattering thing anybody has ever done for me, or the most frightening. I'll decide when I know you better."''',
        c("Continue", "salute")),
    jan("lie", '''"No, you haven't." {n}She doesn't even break the sequence.{/n}
"You hold a blade like someone who has fought everything except a fencer. Demons, cultists, things with teeth. You go in hard and you trust your armour. An Aldori would have your sword out of your hand in two passes and be bored by the third."
"Don't lie to me in a circle, Commander. Out there, lie all you like. In here the forms can tell."''',
        c("Continue", "salute")),
    jan("salute", '''"The salute first." {n}She brings the flat of the blade to her brow and holds it.{/n}
"It means: I see you. I know what you are. I mean to hurt you anyway. You never skip it, not with a friend, not with a bandit on a river road. The day you skip it you're not fencing any more, you're just fighting."''',
        c("Continue", "measure")),
    jan("measure", '''"Then measure." {n}She takes one long step toward you and stops with the point a finger's width from your collarbone.{/n}
"This. The distance at which I can touch you with one step. Outside it, you're safe. Inside it, you're mine. The old man taught us never to stand inside measure unless you mean to finish something."
{n}She doesn't step back.{/n}''',
        c('[Step inside her measure.]', "inside", flags=(MEASURE_FLIRT,)),
        c('"And the yield?"', "yield")),
    jan("inside", '''{n}You take the step. The point of her blade slides past your shoulder, and now there is nothing between you but the width of a breath.{/n}
"That," {n}she says, not quite steadily,{/n} "is exactly what they tell you not to do." {n}She doesn't step back either. After a while she remembers she's holding a sword and lowers it.{/n}
"Let's do the yield. Before I forget what I was teaching."''',
        c("Continue", "yield")),
    jan("yield", '''"The yield is the hard one." {n}She lies down on her back inside the chalk, lays the blade beside her, and fixes her eyes on the ceiling.{/n}
"My master made us practise it. An hour at a time, on the salle floor, while the senior students stepped over us to get to the wine. You don't close your eyes, you don't wipe your face, you don't move until the victor's gone. I hated it more than anything else he taught me."''',
        c("Continue", "yield_scar", requires=(SCAR,)),
        c("Continue", "yield_never", forbids=(SCAR,))),
    jan("yield_scar", '''"It saved my life." {n}She says it to the ceiling.{/n} "In the Scar, with my face full of my own blood and the vrocks coming back, the only thing in my head was an old man in Mivon telling me not to blink. I didn't blink. That's all I did. I didn't blink, and I'm here."''',
        c("Continue", "grip")),
    jan("yield_never", '''"I've never had to use it in earnest. Seven years, forty-one bouts, and I never once lay in the chalk because I had to." {n}She says it to the ceiling.{/n}''',
        c("Continue", "yield_caught", requires=(CAUGHT,)),
        c("Continue", "yield_caught", requires=(LIED,), forbids=(CAUGHT,)),
        c("Continue", "yield_won", forbids=(CAUGHT, LIED))),
    jan("yield_caught", '''"Not until your cell. I lay on that bunk and told you a story about myself, and you caught me in it, and I've never felt flatter on my back in my life."''',
        c("Continue", "grip")),
    jan("yield_won", '''{n}She sits up.{/n} "I still haven't. I won in the cell, remember. You yielded. I'm the one who should be teaching you how to lie still. Get up here."''',
        c("Continue", "grip")),
    nar("grip", '''{n}She gets you on your feet with a blunted practice blade in your hand, frowns at the way you're holding it, and comes round behind you to fix it. Her hands close over yours on the hilt. Her breath is on your ear.{/n}''',
        c("Continue", "grip_her")),
    jan("grip_her", '''"Loose. Like you're holding a bird. Grip it like that and I'll take it off you, and you'll thank me for the lesson." {n}Her thumb moves your thumb along the grip, a finger's width, and stays there.{/n}
"There. Feel that? That's where it wants to be."''',
        c('[Flirt] "Is this part of the forms?"', "flirt"),
        c('"Show me the sequence again."', "again")),
    jan("flirt", '''"No." {n}She doesn't let go.{/n} "This part's mine."
{n}Then she does let go, and steps away, and picks up the chalk as if it had been the chalk she'd been thinking about.{/n} "Same time tomorrow. You're dreadful. I'll make something of you."''',
        c("[Leave her to the chalk.]")),
    jan("again", '''"Three steps, the wrist, recover. Slower than you think. The quick part comes later, when you've stopped thinking about it." {n}She runs it beside you, and then again, and then again, until you're both breathing hard in a cold cell and neither of you has looked at the door.{/n}
"Same time tomorrow. You're dreadful. I'll make something of you."''',
        c("[Leave her to the chalk.]")),
], optional=False)


# --- 2. Houndheart (spine): the one thing she is ashamed of, told whole. -------------------------------------------------

meet(HOUNDHEART, "Houndheart", '"You\'re quiet today."', [
    nar("open", '''{n}It is raining over Drezen, a cold grey rain off the Worldwound, and the last cell has a leak in one corner. She has put the bucket under it, and she's sitting on the bunk listening to it fill.{/n}''',
        c("Continue", "rain")),
    jan("rain", '''"It was a fine day at Houndheart." {n}She doesn't look up.{/n} "Sun on the tents. Birds. I'd have bet you anything it rained. I remember being angry about the birds afterwards, two miles north in the scrub, as if they'd done it on purpose."''',
        c("Continue", "told", requires=(CAUGHT,), forbids=(STRANGER,)),
        c("Continue", "told", requires=(LIED,), forbids=(STRANGER,)),
        c("Continue", "told", requires=(STORY_LOST,), forbids=(STRANGER,)),
        c("Continue", "untold", forbids=(CAUGHT, LIED, STORY_LOST)),
        c("Continue", "told_visitor", requires=(STRANGER,))),
    jan("told_visitor", '''"I told you the camp in the cell, the visitors' way, and you weren't even there. But blood and tale is about what you did. It isn't about what was going on in your head while you did it. Nobody gets that part. I'm going to give it to you anyway, so sit still."''',
        c("Continue", "league")),
    jan("told", '''"We told the camp in the cell, you and I, or started to. But blood and tale is about what you did. It isn't about what was going on in your head while you did it. Nobody gets that part. I'm going to give it to you anyway, so sit still."''',
        c("Continue", "league")),
    jan("untold", '''"You were there. You saw me go. You've never asked me why, and everyone else has asked me nothing else for a year, so I'm going to tell you, and you're going to sit there and let me."''',
        c("Continue", "league")),
    jan("league", '''"Seelah talked us into it. Elan's ring for his Kiana, left in his travelling chest when the demons hit the Houndhearts' camp on the edge of the Wound. The League of the Inspiring Cart, riding out to find a ring. It was going to be a story. We were going to tell it in the Defender's Heart for years."
"No glory without risk. That was Seelah's. I used to shout it louder than she did."''',
        c("Continue", "camp")),
    jan("camp", '''"Then a quasit came out of Elan's chest with the ring, and its colours put Elan and me face-down in the dirt. When we came round we chased it all over that camp like children after a hen. And then Curl was just there, snatching the ring out of its paws and calling things up out of the ground, and Elan swung at him and Seelah got in the way, and somebody was screaming who might have been me." {n}The bucket in the corner goes on filling.{/n}
"Everyone asks why I ran. I've been asking for a year. I've gone over it the way I'd go over a lost bout, stroke by stroke, looking for the moment I decided."''',
        c("Continue", "legs")),
    jan("legs", '''"There isn't one. I didn't decide. My legs decided, and I went with them, and I was two miles north through the scrub toward Numeria before I remembered I had a head."
{n}She looks at her hands.{/n} "I wasn't thinking at all. I was just gone. Do you know how stupid that feels? Seven years learning where to put my feet, and they took me two miles without asking."''',
        c("Continue", "blame")),
    jan("blame", '''"And then in that cage I blamed Seelah for it. Her heroics, her motto, all of it. I told the bars so, often enough." {n}Her mouth twists.{/n}
"It wasn't true. It was just the only thing I could reach from inside the cage."''',
        c('"You ran. That stays true. What you do next is true as well."', "honest", flags=(HH_HONEST,)),
        c('"Deserters hang in most armies. You got a cage, and then me. Count yourself lucky."', "lucky", flags=(HH_LUCKY,)),
        c('"Next time your legs want to decide, look for me. I\'ll be standing where you can see me."', "stand", flags=(HH_STAND,)),
        c('[Lie] "I ran from a fight once, too."', "lie")),
    jan("lie", '''"No, you didn't." {n}She says it without heat.{/n}
"You'd have told me in the cell, or in the chalk, when it would have won you something. You're kind to lie about it. Don't. I don't want company. I want to know what you actually think."''',
        c('"You ran. That stays true. What you do next is true as well."', "honest", flags=(HH_HONEST,)),
        c('"Deserters hang in most armies. You got a cage, and then me. Count yourself lucky."', "lucky", flags=(HH_LUCKY,)),
        c('"Next time your legs want to decide, look for me. I\'ll be standing where you can see me."', "stand", flags=(HH_STAND,))),
    jan("honest", '''"What I do next is true as well." {n}She tries it out, slowly, like a new sequence.{/n}
"I've spent a year going over the running. In the cage, in the cell, every night. I could draw you a map of it with my eyes shut."
{n}She gets up and empties the bucket out through the bars into the gutter.{/n} "Time I learned the other half."''',
        c("[Leave her with the rain.]")),
    jan("lucky", '''{n}She laughs. It's the old laugh, the tavern laugh from Kenabres, and there is nothing in it at all.{/n}
"Lucky. Four days in the Watch before the demons came. A cage in the Scar. And you." {n}She spreads her hands.{/n} "Am I lucky, or what?"
{n}She says it the way you'd say it over a grave.{/n} "Don't do that again, Commander. Not about this. About anything else you like."''',
        c("[Leave her with the rain.]")),
    jan("stand", '''"Where I can see you." {n}She looks at you, then at the bucket, then at you again.{/n}
"That's a stupid thing to promise a deserter. You'll be busy. You'll be in the Abyss, or the Wound, or up on a wall with your back to me."
{n}She is quiet a while.{/n} "Say it again anyway."''',
        c('"I\'ll be standing where you can see me."', "stand_again")),
    jan("stand_again", '''{n}She nods, once, as if a touch had been scored and she agreed with the judges.{/n}
"All right. I'll look." {n}She picks up the bucket, empties it through the bars and sets it back under the leak, precisely, the way she does everything.{/n} "Go on. It's only rain."''',
        c("[Leave her with the rain.]")),
], requires=(FORMS,), optional=False)


# --- 3. The wall (spine): vrocks, and whether her legs decide. -------------------------------------------------------------

# Q6 follow-up (INT): the spine's wall is asked for at her cell hub (she has the last watch), not read from the mod's book.
meet(WALLS, "Wings over the north wall", '"The Watch sergeant says you asked for the north wall."', [
    nar("open", '''{n}She has asked the Eagle Watch for the last watch on the north wall, the one before first light, which nobody else wanted. It is the hour things come down out of the Wound's glow to see what's soft, she says, oiling her blade without looking up, and if she is going to find out what her legs do, she would rather find out there than in a cell.{/n}
{n}You are on the wall walk that night when the alarm comes, an hour before first light: bells from the north wall, then shouting, then the sound every soldier in Drezen has learned to hate, wings the size of sails beating the dark. Vrocks. A raiding flight of them. The Eagle Watch are on the wall, and so is a half-elf in a gambeson with a long Aldori blade, who got there first.{/n}''',
        c("Continue", "freeze")),
    nar("freeze", '''{n}The first vrock lands on the parapet ten paces from her, a great filthy bird-shape with a man's arms, and screams. You see her stop. Not step back: stop, blade half raised, the way she must have stopped in a cage in the Molten Scar while things exactly like this one argued over what to do with her.{/n}
{n}Her legs haven't decided yet. They're thinking about it.{/n}''',
        c('[Call the salute] "Jannah Aldori! To the first blood!"', "salute", flags=(WALL_SALUTE,)),
        c("[Put yourself between her and the vrock.]", "shield", flags=(WALL_SHIELD,)),
        c("[Do nothing. Watch what she does.]", "watched", flags=(WALL_WATCHED,))),
    nar("salute", '''{n}Her blade comes up to her brow before her head understands why. Then she's moving: in under the vrock's reach, on the balls of her feet, the long blade low and quick and never where it is looking. It takes her three passes to open its throat. She doesn't stop to watch it fall. There are four more on the wall.{/n}''',
        c("Continue", "after_salute")),
    nar("shield", '''{n}You're between them before she can move, and the vrock's talons open your arm from shoulder to elbow instead of her face. Behind you she makes a sound you've never heard from her, furious and ashamed at once. Then she comes round you and puts her blade through the thing's eye.{/n}''',
        c("Continue", "after_shield")),
    nar("watched", '''{n}You stay where you are. Ten paces. The vrock screams again and comes for her, and for a heartbeat you are quite sure you have made a mistake.{/n}
{n}Then she moves. Not away: in. She takes it the Aldori way, under its reach, the blade low and quick, and it is a long, ugly fight on a narrow wall and she wins it alone, because nobody helped her.{/n}''',
        c("Continue", "after_watched")),
    jan("after_salute", '''{n}When it's over, and the sky above the Wound has gone from red to a dirty grey, she sits down on the wall walk with her back to the parapet and starts to shake, now that she can afford to.{/n}
"You called the salute. In the middle of a raid. On a wall. As if it were a yard in Mivon." {n}She wipes her blade on a dead thing's feathers.{/n} "I heard it and my arm knew what to do before my legs had an opinion. I don't know why that worked. Don't do it too often. I'll start to need it."''',
        c("Continue", "end")),
    jan("after_shield", '''{n}When it's over, she has both hands on your arm, pressing the torn sleeve shut, and she is so angry her voice shakes.{/n}
"I don't need a shield. I needed to find out whether I run. You just stood in front of the answer." {n}She ties off the bandage harder than she has to.{/n}
"...Thank you. Never again."''',
        c("Continue", "end")),
    jan("after_watched", '''{n}When it's over, she's sitting against the parapet with blood to the elbows, and she looks up at you.{/n}
"You watched. Ten paces, and you didn't move. You wanted to see if I'd run." {n}She wipes her blade on the dead vrock's feathers, slowly.{/n}
"I didn't. So now you know. I'd have liked it better if you'd found out some other way. That was a Commander's trick, not a friend's. I'll remember it."''',
        c("Continue", "end")),
    jan("end", '''{n}Down in the yard the Eagle Watch are hauling the carcasses off the wall with hooks. One of the sergeants looks up at the half-elf on the wall walk and, after a moment, lifts a hand to her. She lifts one back.{/n}
"I didn't run." {n}She says it to herself, trying the weight of it.{/n} "Put that down somewhere, Commander. With the rest."''',
        c("[Help her up.]")),
], requires=(HOUNDHEART,), delay=48, optional=False)   # hub: her cell presence (Q6 follow-up)


# --- Optional beats. -------------------------------------------------------------------------------------------------------

# Seelah (must-acknowledge): the friend she failed, from Jannah's side only.
meet(SEELAH, "The League of the Inspiring Cart", '"Tell me about Seelah."', [
    nar("open", '''{n}She is turning a battered pewter tankard over in her hands, the kind the Defender's Heart used to hang behind its bar. Someone has scratched a little cart on the side with a knife point, and four stick figures pushing it.{/n}''',
        c("Continue", "mourn", requires=(SEELAH_DEAD,), forbids=(SEELAH_BACK, SEELAH_KILLED_AT_CAGE)),
        c("Continue", "gone", requires=(SEELAH_GONE,), forbids=(SEELAH_DEAD, SEELAH_BACK)),
        c("Continue", "living", forbids=(SEELAH_DEAD, SEELAH_GONE)),
        c("Continue", "living", requires=(SEELAH_BACK,)),
        c("Continue", "mourn_saw", requires=(SEELAH_DEAD, SEELAH_KILLED_AT_CAGE), forbids=(SEELAH_BACK,))),
    jan("mourn_saw", '''"Seelah's dead. I didn't hear it in a gaol; I was there. She broke my lock because you wanted me punished, and you cut her down for it, and I walked out of that cage past her." {n}She turns the four figures to the wall.{/n}
"Don't tell me what you'd do differently. I've had a long time to work out what I'd have done, and none of it was anything."''',
        c("[Sit with her, and say nothing.]", "mourn_quiet")),
    jan("living", '''"The League. Seelah, Elan, Curl and me. Elan, Curl and I found a lost cart of beer in the ruins of Kenabres the week the world ended, and Seelah made a party of it, and we thought that made us heroes." {n}She sets the tankard on the bunk.{/n}''',
        c("Continue", "known", requires=(DEAD_KNOWN,)),
        c("Continue", "unknown", requires=(DEAD_L,), forbids=(DEAD_KNOWN,)),
        c("Continue", "q3", requires=(JOINED,), forbids=(DEAD_L,)),
        c("Continue", "cage_seen", forbids=(DEAD_L, JOINED), requires=(FREE,)),
        c("Continue", "cage_seen", forbids=(DEAD_L, JOINED, FREE), requires=(PRISON,)),
        c("Continue", "cage_seen", forbids=(DEAD_L, JOINED, FREE, PRISON), requires=(CONDEMNED,)),
        c("Continue", "not_seen", forbids=(DEAD_L, JOINED, FREE, PRISON, CONDEMNED))),
    jan("known", '''"Seelah thinks I'm dead. Worse: she thinks you killed me, because you told her so, and she told you it wasn't justice. The chaplain heard her say it, and the turnkey heard it from the chaplain." {n}Her mouth twists.{/n}
"She was right. It wasn't justice. It was the forms, which is something else, and she'd never have understood the difference."''',
        c("Continue", "decide")),
    jan("unknown", '''"Seelah doesn't know anything. As far as she knows I ran at Houndheart, and nobody ever saw me again. Nobody told her about the cage. Nobody told her about you." {n}Her mouth twists.{/n}
"It's the kindest thing that's happened to her all year, and I'm about to ruin it."''',
        c("Continue", "decide")),
    jan("q3", '''"Seelah smiled at me. In front of the citadel, in front of Elan, after everything. As if I hadn't failed her."
"I asked her how she could do that. She said she'd give me a piece of her mind once we were in private. She did, too. Then she bought me a drink."''',
        c("Continue", "elan", requires=(ELAN_DEAD,)),
        c("Continue", "elan_lives", forbids=(ELAN_DEAD,))),
    jan("elan", '''"Elan's dead." {n}She says it flatly, the way she says everything that matters.{/n}
"He saw the jeweller with the souls and ran after him, alone, and the door was trapped, and he opened it. Seelah got to him first. I got there after, from the mouth of the cave where he'd told me to wait. I didn't run, Commander. I didn't do anything useful either." {n}She looks at the four stick figures on the tankard.{/n} "His soul came back with the rest, they say. Curl's too. Nobody's told me what becomes of Curl now. So that's the League: Seelah, and me, and a question."''',
        c("Continue", "q3_end")),
    jan("elan_lives", '''"Elan's alive, and still furious with me. At least he's alive to be. Curl's soul came back with the rest; nobody's told me yet what becomes of him. Seelah is Seelah." {n}She turns the tankard so the cart faces you.{/n}
"Four out of four, near enough. For a League that started with a barrel of beer, that's a better record than mine."''',
        c("Continue", "q3_end")),
    jan("q3_end", '''"She's the reason I'm still standing, and for a whole winter I told myself she was the reason I ran. I've taken it back since. I'm not sure it's the kind of thing you can take back." {n}She puts the tankard down.{/n}
"I don't want you telling her anything about us. I'll tell her. When there's something to tell."''',
        c('"Then it\'s yours to tell."', "end")),
    jan("cage_seen", '''"Since Houndheart I haven't once stood in front of her as anything but a deserter." {n}She turns the tankard a quarter-turn.{/n}
"She'd tell me it was all right before I'd finished. And I'd let her, because I want it to be, and it isn't. Not yet."''',
        c("Continue", "decide")),
    jan("not_seen", '''"I haven't faced her about Houndheart. I've seen her every night in my head, though, standing in the middle of that camp, shouting that motto of hers, looking round for me."
"I wasn't there. I'm never there, in that dream. I've been gone a long time."''',
        c("Continue", "decide")),
    jan("decide", '''"I could go and find her today. Walk up those steps and go looking, and be in front of her before the bell." {n}She doesn't move.{/n}
"Demons aren't what frighten me about this. It turns out I'm a coward about exactly one thing, and it's a paladin being kind to me."''',
        c('"Go and see her. Today."', "go", flags=(SEELAH_HERSELF,)),
        c('"I\'ll tell her for you."', "for_her", flags=(SEELAH_FOR_HER,)),
        c('"Leave Seelah out of it for now."', "kept", flags=(SEELAH_KEPT,))),
    jan("go", '''"Today." {n}She stands up, puts the tankard in her belt, and goes, before she can think better of it.{/n}
{n}She's gone most of the afternoon. When she comes back down the gaol steps she has a red handprint on her left cheek and her eyes are swollen, and she's grinning like a fool.{/n}
"She hit me. Open hand. Then she held on so long the turnkey came to see if it was a fight. Then she bought me a drink, and made me tell her everything, and hit me again."''',
        c('"How was the drink?"', "go_end"),
        c('"Everything?"', "go_everything")),
    jan("go_end", '''"Terrible. We aren't at the Defender's Heart, and Drezen can't brew." {n}She touches the handprint as if it were a medal.{/n}
"Best I've ever had."''',
        c("[Leave her with it.]")),
    jan("go_everything", '''"Everything. Houndheart, the cage, and every place I've been since." {n}She touches the handprint.{/n}
"Not everything about you. She guessed that part. She said she'd hit you as well, but she's too well brought up to hit the Commander, so she's going to pray about it instead. I'd be worried, if I were you."''',
        c("[Leave her with it.]")),
    jan("for_her", '''"You'll tell her." {n}Relief and shame, both at once, and she lets you see both.{/n}
"Thank you. Tell her... No. Tell her nothing from me. Tell her what happened and let her decide what she thinks of it. She'll come down those steps and hit me, and I'll let her."''',
        c("[Leave her with the tankard.]")),
    jan("kept", '''"For now." {n}She nods slowly, the way she'd note a change in the wind.{/n}
"You're a cold one, Commander. That's probably the right call, and I don't like you for making it so easily." {n}She puts the tankard back on the shelf, facing the wall.{/n}''',
        c("[Leave her with the tankard.]")),
    jan("end", '''{n}She puts the tankard back on the shelf above the bunk, with the cart facing out.{/n}''',
        c("[Leave her with it.]")),
    jan("mourn", '''"Seelah's dead." {n}She turns the tankard so the four little figures face the wall.{/n}
"I heard in the gaol. Nobody thought to tell me properly; why would they? I was nobody to her, by the end. A friend who ran." {n}Her jaw works.{/n}
"For a whole winter I told myself she was the reason I ran. I never told her properly that I'd stopped."''',
        c('"She\'d have forgiven you."', "mourn_forgive"),
        c("[Sit with her, and say nothing.]", "mourn_quiet")),
    jan("mourn_forgive", '''"I know. That's the worst part. She'd have forgiven me before I'd finished asking." {n}She presses the heels of her hands into her eyes, hard, and takes them away.{/n}
"No glory without risk. She used to shout it at the tavern ceiling. I'm going to shout it at a demon one of these days, and mean it, and then I'll have paid for something."''',
        c("[Leave her with it.]")),
    jan("mourn_quiet", '''{n}You sit on the bunk beside her. After a while she leans, very slightly, until her shoulder is against yours, and stays there while the lamp gutters.{/n}
"Thank you," {n}she says eventually.{/n} "For not saying she'd have forgiven me. Everybody says that."''',
        c("[Leave her with it.]")),
    jan("gone", '''"Seelah's gone. The turnkey says you sent her away." {n}She looks at you over the tankard, and she doesn't hide what she thinks.{/n}
"She was the best of us. The whole League. Better than Elan, and Elan was a knight. I don't know what she did to be put out, and I'm not going to ask, because I'd have to hear your side of it and I'd rather keep mine."
{n}She sets the tankard down.{/n} "If you ever see her, tell her Jannah's alive and hasn't run since. She'd want to know."''',
        c("[Leave her with it.]")),
], requires=(RETURNED,), delay=48)


# Mivon: her father, and what she writes home.
meet(MIVON, "Home", '"Is that a letter?"', [
    nar("open", '''{n}She is sitting on the bunk with a letter on her knee, sealed with river-green wax, the seal broken. The hand is large and old-fashioned and leans hard to the right, like a man walking into wind.{/n}''',
        c("Continue", "dead", requires=(SCAR,), forbids=(NAMELESS,)),
        c("Continue", "nameless", requires=(NAMELESS,)),
        c("Continue", "alive", forbids=(SCAR,))),
    jan("dead", '''"My father. The Eagle Watch wrote to Mivon in the winter, to tell him I'd died in the Molten Scar. So he wrote back, to the Commander of the crusade, asking where my body was buried and whether I'd died well." {n}Her mouth twitches.{/n}
"The clerk didn't know what to do with it, so he brought it down here. I suppose he thought I'd know where I was buried."''',
        c("Continue", "father")),
    jan("nameless", '''"My father. The Eagle Watch wrote to Mivon in the winter, to tell him I'd died in the Molten Scar. He wrote back asking where I was buried." {n}She doesn't look at you.{/n}
"The clerk brought it to me because I'm nobody, and nobody's post goes to nobody. I can't answer it. I'm dead on your rolls, by your word. So I've been reading it."''',
        c("Continue", "father")),
    jan("alive", '''"My father. The Eagle Watch sends notices home when a recruit deserts. So he knows I ran; everybody on our street in Mivon knows I ran. It's taken him until now to decide what to say about it."
{n}She turns the page over, and back.{/n}''',
        c("Continue", "father")),
    jan("father", '''"He says..." {n}She reads it aloud, flat, in his words.{/n} "'Fate brought you to Mendev, and fate does not make mistakes, only daughters do. Come home, or do not; but write, and tell me whether my girl is still the best blade on the river.'"
{n}She folds it.{/n} "He used to say that about everything. Fate brought me here. It's why I went. I thought if fate brought me to the crusade then fate would bring me glory, and all I'd have to do was stand in the right place and wait for it."''',
        c('"Does he miss you?"', "miss"),
        c('"What will you write back?"', "write")),
    jan("miss", '''"I used to wonder that. On watch in Kenabres, before the demons, I used to wonder if they missed me back home in Mivon." {n}She laughs quietly.{/n}
"He misses the daughter he sent. The best blade on the river, who never lost. I don't know if he'd miss this one. He's never met her."''',
        c("Continue", "write")),
    jan("write", '''"That's the question." {n}She puts the letter on the bunk between you, as if it were a blade laid down between two fencers.{/n}
"I can write him the truth: I ran, I was caged, I'm in a cell in Drezen. Or I can write him a hero. He'd believe the hero. He'd tell the whole street. He'd die happy." {n}She looks at you.{/n} "What would you do?"''',
        c('"Write him the truth. He asked about his daughter, not about a legend."', "truth"),
        c('"Let him keep the daughter he believes in. The truth is yours; the legend is his."', "legend"),
        c('"It\'s your letter, and your father. I won\'t choose it for you."', "yours")),
    jan("truth", '''"The truth." {n}She takes a sheet of paper from under the bunk and a pencil stub from her boot.{/n}
"He'll hate it. He'll write back and tell me fate had a plan, and I'll write back and tell him fate can go and drown in the river. We'll argue about it for years." {n}She starts writing.{/n} "Good. I've missed arguing with him."''',
        c("[Leave her to her letter.]", flags=(MIVON_TRUTH,))),
    jan("legend", '''"The legend." {n}She considers it a long time.{/n}
"All right. He's old. He buried my mother on the strength of a story about how she'd died, and he was happier for it. I'll give him one about me." {n}She takes out paper and a pencil stub.{/n} "I'll never tell anyone else it. Just him."''',
        c("[Leave her to her letter.]", flags=(MIVON_LEGEND,))),
    jan("yours", '''"Coward." {n}But she's almost smiling.{/n} "No. You're right. It's mine."
{n}She is quiet a while, turning the pencil in her fingers the way she turns a blade.{/n} "The truth. If I'm going to stop running, I might as well stop in front of him too. He'll send four pages telling me off. Fine. I'll answer every one."''',
        c("[Leave her to her letter.]", flags=(MIVON_TRUTH,))),
], requires=(FORMS,), delay=48)


# The blade: her Aldori sword, her record, and one notch cut the wrong way.
meet(BLADE, "Forty-one", '"That isn\'t a practice sword."', [
    nar("open", '''{n}She has a long blade across her knees, a plain one, and she's working the old leather off its grip with the point of a knife to wind it again for her own hand.{/n}''',
        c("Continue", "ash", requires=(SCAR,)),
        c("Continue", "stores", forbids=(SCAR, SWORD_GIVEN)),
        c("Continue", "given", requires=(SWORD_GIVEN,), forbids=(SCAR,)),
        c("Continue", "given", requires=(SWORD_GIVEN,), forbids=(SCAR, "chapter_later"))),   # retired (Q6 r6)
    jan("given", '''"Not mine. The vrocks tossed mine down outside my cage at the Scar, and I told you to take it for the crusade. Keep it. I meant that." {n}She keeps working the leather.{/n} "The turnkey found me this one in the gaol stores, under a sack of turnips. It'll do."''',
        c("Continue", "master")),
    jan("ash", '''"The one you passed me through the bars." {n}She keeps working the leather.{/n} "I lay on it in the ash for an hour, and carried it through the Wound, and guarded salt with it all winter, and it never once asked me what I thought I was doing."''',
        c("Continue", "master")),
    jan("stores", '''"Not mine. Mine's somewhere in the Molten Scar, or on some demon's belt. The turnkey found me this one in the gaol stores, under a sack of turnips, which is where they put the weapons of people they don't expect to see again."
"It'll do. It'll have to."''',
        c("Continue", "master")),
    jan("master", '''"My own blade, the one I lost, my master gave me the day I left Mivon. He'd never said a kind word to me in seven years. He put it in my hands at the river stairs and said, 'Don't come back with it dirty.'" {n}Her mouth quirks.{/n}
"I think that was the kind word. Well. I didn't come back with it at all."''',
        c("Continue", "scabbard")),
    jan("scabbard", '''{n}She turns the scabbard over and shows you the inside of its throat. The leather there is cut with tiny, neat notches, every one of them fresh.{/n}
"Forty-one. I cut them in last night, from memory. One for every bout I fought in earnest. Tournaments, quarrels, the bandits on the river roads. I stopped counting at forty-one because I'd have kept going, and nobody can stand a girl who counts out loud. I know. I tried."''',
        c("Continue", "wrong_way", requires=(SCAR,)),
        c("Continue", "wrong_way", requires=(CAUGHT,)),
        c("Continue", "wrong_way", requires=(LIED,)),
        c("Continue", "right_way", forbids=(SCAR, CAUGHT, LIED))),
    jan("wrong_way", '''{n}She puts her thumb on one more notch, cut the other way, across the grain.{/n}
"And that one. For you." {n}She says it lightly. It isn't light.{/n}
"The first one I lost. I cut it the wrong way so I'd never mistake it for the others."''',
        c('[Flirt] "I\'m honoured to be the exception."', "flirt"),
        c('"Will you ever cut another?"', "another")),
    jan("right_way", '''{n}She puts her thumb on one more notch, set a little apart from the others, cut the right way.{/n}
"Forty-two. The cell. You." {n}She says it lightly.{/n} "I wasn't sure it counted, a bout of stories. I decided it did. I'm the one who keeps the scabbard."''',
        c('[Flirt] "Keep the scabbard. I\'ll keep trying."', "flirt"),
        c('"Will you ever cut another?"', "another")),
    jan("flirt", '''"You would." {n}She looks up from the scabbard and lets her eyes linger on you.{/n}
"Here." {n}She puts the blade in your hands, hilt first, and folds your fingers round the bare wood.{/n} "Feel the balance? I'll wind the grip tighter here. My old one sat just so."''',
        c("[Hold it.]", "held", flags=(BLADE_HELD,))),
    jan("another", '''"Of course." {n}She runs her thumb along the notches.{/n} "I didn't come back to stop fencing."
{n}She puts the blade in your hands, hilt first.{/n} "Here. Feel the balance. It's a turnip-sack sword, but it'll do."''',
        c("[Hold it.]", "held", flags=(BLADE_HELD,))),
    jan("held", '''{n}It is lighter than it looks, and it wants to move. Jannah watches you hold it the way she'd watch you hold something alive.{/n}
"Good." {n}She takes it back and starts winding the new leather on, tight and neat.{/n} "You didn't grip it. I'll make a fencer of you yet."''',
        c("[Leave her to her grip.]")),
], requires=(FORMS,), delay=24)


# Kenabres: the girl who laughed too loud, and what's left of her.
meet(KENABRES, "Four days", '"You used to laugh louder."', [
    nar("open", '''{n}She is sitting in the cell doorway with her back against the frame, eating an apple with a knife, a slice at a time, the way somebody eats who has been hungry and doesn't mean to be again.{/n}''',
        c("Continue", "start")),
    jan("start", '''"I did, didn't I." {n}She considers the apple.{/n}
"In Kenabres. With the cart. 'I signed up four days before the demon attack!' And then that thing I used to say after it, every time, to anybody." {n}She does her own voice from a year ago, loud and bright, and it's a good imitation, and it's horrible.{/n}
"I used to think that was funny. Four days. I thought it meant I was meant to be there."''',
        c('"It sounds funny. You must have made the whole table laugh."', "funny"),
        c('"Who were you, before Kenabres?"', "before")),
    jan("funny", '''"I made them laugh because I was frightened, and laughing loud is what frightened people from the river do." {n}She cuts another slice.{/n}
"Seelah laughed because she was kind. Elan laughed because he was embarrassed. Curl laughed because... I don't know why Curl laughed. I never knew anything about Curl."''',
        c("Continue", "before")),
    jan("before", '''"Before? A girl from Mivon who'd never lost. I fought in tournaments, in the squares, in the duelling yards. Twice against real marauders on the river roads, and I won both times, and I thought that meant I knew what fighting was." {n}She eats the slice.{/n}
"In Mivon, strangers earn the right to stay by winning duels, one after another, each harder than the last. I was born there, so I never had to. I fought them anyway, to prove I'd have earned it. Then I got bored and went looking for something that would be hard."''',
        c("Continue", "found")),
    jan("found", '''"I found it." {n}She holds up the apple and looks at it as if it had said something.{/n}
"The girl in Kenabres was all loud laughing and a borrowed tabard. She'd have made a terrible crusader. She did make a terrible crusader. I don't miss her." {n}A pause.{/n} "I miss her laugh a bit. She could fill a room."''',
        c('"I\'d like to hear it again one day. A real one."', "laugh"),
        c('"I like this one better."', "better")),
    jan("laugh", '''"Would you." {n}She considers you over the apple.{/n}
"You'll have to earn it, then. That girl laughed at everything. This one's much harder to please." {n}The corner of her mouth goes up, and stays up a moment longer than she means it to.{/n}''',
        c("[Leave her to her apple.]")),
    jan("better", '''"Do you." {n}She stops cutting.{/n}
"Most people don't. Most people liked the loud one. She was easy." {n}She offers you a slice of apple on the flat of the knife, the way you'd offer a salute.{/n} "Take it before I change my mind."''',
        c("[Take it.]")),
], requires=(FORMS,), delay=48)


# The Watch: a sergeant's hand on the wall, and the question of her tabard.
meet(WATCH, "The blue tabard", '"The Watch sergeant was asking about you."', [
    nar("open", '''{n}There is a folded tabard on the end of the bunk, Eagle Watch blue, clean and pressed, with a recruit's eagle sewn on the breast. She's sitting as far from it as the cell allows.{/n}''',
        c("Continue", "start")),
    jan("start", '''"He brought it himself. The sergeant from the wall, the one who waved. He said the Watch is short of blades who don't run, and he'd sooner have one who ran once and came back than ten who never had the chance." {n}She doesn't touch it.{/n}
"He said the Watch would put me back on its rolls if I asked. He said he'd already asked for me."''',
        c('"Will you take it?"', "take"),
        c('"You earned it on the wall."', "earned")),
    jan("earned", '''"On the wall I earned not running. That's all I earned." {n}She looks at the tabard.{/n}
"A tabard is a promise. I made that promise once, four days before the demons came, and I broke it at Houndheart. I don't know if I get to make it twice."''',
        c("Continue", "take")),
    jan("take", '''"I want it." {n}She says it as if confessing to a theft.{/n}
"I want it more than I've wanted anything since Mivon. That's the problem. The last time I wanted something that much, I ran from it the first time it bit me."''',
        c('"Then put it on, and don\'t run."', "on", flags=(WATCH_STOOD,)),
        c('"Then leave it folded until you know."', "folded"),
        c('"You don\'t need their blue. You fight for me."', "mine")),
    jan("on", '''{n}She looks at you for a slow breath. Then she shakes out the tabard, pulls it over her head and stands in the last cell in Eagle Watch blue.{/n}
"It's too big. It was always too big." {n}She tugs the hem straight.{/n} "Don't stare. I only wanted to try it on."''',
        c("[Leave her in the blue.]")),
    jan("folded", '''"Until I know." {n}She nods, and puts the tabard on the shelf above the bunk, folded, badge out.{/n}
"It'll be there. That's the good thing about a tabard; it waits. It's more patient than I am."''',
        c("[Leave her with it.]")),
    jan("mine", '''"For you." {n}Her ears go pink, and she scowls to make up for it.{/n}
"You can't just say that. Not with the door open. The turnkey hears everything, and he tells the cook." {n}She puts the tabard on the shelf, folded, and doesn't look at you.{/n} "...Say it again some time. When the door's shut."''',
        c("[Leave her with it.]")),
], requires=(WALLS,), forbids=(COMMITTED,), delay=24)


# Measure: the first bout with blades, in the empty practice yard (heat, and a line she won't cross in private).
meet(SPARRING, "Measure", '"The yard\'s empty this time of night."', [
    nar("open", '''{n}She has taken two blunted blades from the rack in the practice yard behind the barracks and hung a lantern on the pump. When you come round the corner she tosses you one, hilt first, without a word, and you catch it more or less.{/n}''',
        c("Continue", "start")),
    jan("start", '''"The forms in a cell are one thing. Chalk on stone, nobody moving. Now we find out whether you can move."
{n}She salutes. You salute. She is inside your guard before your blade has come down from your brow, there is a small, precise pressure at your wrist, and your sword is lying on the sand three paces away.{/n}
"That's the Aldori way. Why hurt someone, when you can simply take away the thing they'd hurt you with?"''',
        c('"Again."', "again"),
        c('[Flirt] "You\'re enjoying this."', "enjoy")),
    jan("enjoy", '''"Enormously." {n}She doesn't pretend otherwise.{/n}
"I haven't crossed blades with anyone for the joy of it since Mivon. The Watch drilled; demons don't fence; a cage doesn't count. It turns out I missed this more than I missed my father." {n}She nudges your fallen sword toward you with her toe.{/n} "Pick it up. Again."''',
        c("[Pick up the blade.]", "again")),
    nar("again", '''{n}She takes it twice more, once with a bind and once with a flick of the wrist you never see, and each time she fetches it and hands it back hilt first and waits. The third time she comes in, you feel the pressure at your wrist begin.{/n}''',
        c("[Mobility] Turn with her, the way she turned in the cell sequence, and keep your grip loose.",
          check=dict(Skill="SkillMobility", DC=20, Success="kept", Failure="lost")),
        c("[Let it go, and watch how she does it.]", "watched")),
    jan("kept", '''{n}Your wrist turns with hers instead of against it, the grip loose as a bird in the hand, and the blade stays where it is. She stops dead.{/n}
"You held on." {n}She sounds delighted, which she clearly hadn't planned to sound.{/n} "Most people let go when I do that. Their own wrist does it for them. You listened."''',
        c("Continue", "close")),
    jan("lost", '''{n}It goes anyway, spinning off into the dark past the pump. She fetches it herself and gives it back hilt first.{/n}
"Everybody loses it the first night. I lost mine to the old man forty times before I kept it once. He used to count out loud, so the whole salle could hear."''',
        c("Continue", "close")),
    jan("watched", '''"Watching's cheating." {n}But she slows down and does it again, all of it, at half speed, her hand over yours on the grip, guiding your wrist through the turn.{/n}
"Here. And here. Feel it go? That's the moment. Don't fight it. Go with it, and it's yours instead of mine."''',
        c("Continue", "close")),
    nar("close", '''{n}By the time the lantern starts to gutter you are both sweating in the cold and her hair has come down. She has stopped taking your sword. The last pass ends with the blunted blades crossed between you and her face a hand's breadth from yours, and neither of you steps back.{/n}''',
        c("Continue", "measure_line")),
    jan("measure_line", '''"This is inside measure." {n}She doesn't move.{/n} "This is where the forms say you finish something."
"Not yet." {n}Her eyes go to your mouth and come back.{/n} "Not here, with a lantern and a pump. I want people to see it. I want the whole yard to see it, and gossip, and be jealous."''',
        c('"Then I\'ll wait for a better audience."', "wait"),
        c("[Close the hand's breadth.]", "kissed", flags=(SPAR_KISSED,))),
    jan("wait", '''"You'd better." {n}She steps back out of measure, very deliberately, the way you'd step back from a drop.{/n}
"Put the blade back on the rack, point down. And if anyone asks what we were doing out here, tell them you lost your sword four times to a deserter. They'll believe that."''',
        c("[Put the blade back on the rack.]")),
    jan("kissed", '''{n}She lets you. For the length of one held breath she lets you, and her free hand comes up into your hair; and then it is flat on your chest and she's pushed you back out of measure, not hard.{/n}
"Cheat." {n}She's grinning, and her ears have gone pink to the points.{/n} "I said not here. I didn't say you couldn't try. Put the blade on the rack, point down, before I stop being an Aldori about it."''',
        c("[Put the blade back on the rack.]")),
], requires=(FORMS,), delay=24)


# Salt (killed worlds): the winter under a made-up name, and what she learned about being watched.
meet(SALT, "Salt", '"What was it like, being nobody?"', [
    nar("open", '''{n}She is sitting cross-legged on the bunk, darning the elbow of her gambeson with coarse thread and the concentration of someone who was never taught to sew and refuses to be beaten by it.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Cold." {n}She bites off the thread.{/n}
"I don't remember the first days well. Walking south along the lava channels at night, mostly. Then a village I never learned the name of, and a carter hauling salt to Nerosyan who needed another sword and didn't ask questions. That's the part I remember clearly: nobody asking questions."''',
        c("Continue", "master")),
    jan("master", '''"The carter's wife stitched my head by the fire. She asked who did it, and I said I'd lost a bout, and she said good, the ones who've never lost are no use to anyone." {n}She touches the seam.{/n}
"That's why it's so ugly. She had gut, and a needle for harness, and no patience."''',
        c('"What name did you give her?"', "vesh"),
        c('"Did nobody recognise you?"', "nobody")),
    jan("vesh", '''"The name of my father's horse. I'm not telling you what it was; you'd laugh." {n}Something close to a smile.{/n}
"I was bad at answering to it. Half the winter, people had to say it twice."''',
        c("Continue", "night")),
    jan("nobody", '''"A deserter, walking south with a dead woman's face? Nobody looks. That's the thing I learned on the salt road, Commander. Nobody is looking at you half as hard as you're looking at yourself."''',
        c("Continue", "night")),
    jan("night", '''"Once, one night on the road, something came out of the snow at the wagons. Cultists, I think, and something with them that wasn't a man any more. There were four of us with swords. I was one of them."
{n}She puts the gambeson down.{/n} "I didn't run. Nobody on that caravan had ever heard of Houndheart, so nobody was expecting me to, so I didn't. I've thought about that a lot since. Whether I only run when somebody is waiting to see me do it."''',
        c('"Or you only stand when you\'ve lost so much there\'s nothing left to run for."', "lost"),
        c('"Maybe you\'d changed."', "changed"),
        c('[Flirt] "I\'m always watching you. Try not to run."', "watching")),
    jan("lost", '''"...Maybe." {n}She considers it the way she'd consider a cut she hadn't seen coming.{/n}
"That's a nasty thing to say, and it might be true. On that road I had nothing. No name, no record, no Seelah, no Watch. I'd already lost everything a person could run to keep. So I stood." {n}She picks the darning back up.{/n} "Now I've got things again. I'd better be careful."''',
        c("[Leave her to her darning.]")),
    jan("changed", '''"Changed." {n}She touches her temple, the ugly seam of it, and scowls.{/n}
"I was cold and I was hungry and the carter owed me four coppers. That's why I stood. Don't you dare make it a sermon." {n}She stabs the needle back in.{/n} "...I did look round, after. To see if anyone had noticed. Nobody had. I was a bit disappointed."''',
        c("[Leave her to her darning.]")),
    jan("watching", '''{n}She looks up from the darning, slowly.{/n}
"That's either the sweetest thing anybody has said to me since Mivon, or a threat." {n}She goes back to the needle.{/n} "I've decided it's both. I like it better that way."''',
        c("[Leave her to her darning.]")),
], requires=(SCAR, FORMS), delay=48)


# The ford (the posted world): the Condemned, a housebreaker, and what she came back to say.
meet(FORD, "The ford", '"Tell me about the ford."', [
    nar("open", '''{n}She has the strip of leather from under her sword's grip unwound across her knee, and she is reading it. There are names on it in charcoal, small and square. Eleven of them.{/n}''',
        c("Continue", "start")),
    jan("start", '''"The Condemned are what you'd think. Thieves. A man who burned his landlord's barn with the landlord still in it. Deserters. Two priests who'd said the wrong thing to the wrong inquisitor. Our sergeant was a Mendevian who'd been flogged so often his back looked ploughed, and he was the kindest man in the company."''',
        c("Continue", "hold")),
    jan("hold", '''"They put us on a ford a morning's march up the north road and told us to hold it till the relief came. Things came over the water in the dark, low, with too many legs, and every time the moon came out there were fewer of us." {n}She runs her thumb down the names.{/n}
"Some time after midnight one of them got into our line right beside me, and I felt my legs start to decide."''',
        c('"And?"', "and"),
        c("[Wait for her.]", "and")),
    jan("and", '''"And the man on my left, a housebreaker from Nerosyan called Pim, who'd never held a sword before that week, put his shoulder against mine and said, 'Don't you dare, Aldori. I've heard about you.'" {n}She laughs, very quietly.{/n}
"He'd heard about me. Everybody had. So I stayed, because a housebreaker told me not to go."''',
        c("Continue", "names")),
    jan("names", '''"He's the fourth name. He died at dawn, on the far bank, pulling a boy out of the water. I wound them all under my grip, so that when I hold the sword I'm holding them."''',
        c('"You\'d won in the cell. Why come back at all?"', "why"),
        c("[Say nothing, and read the names with her.]", "read")),
    jan("why", '''"Because I'd won. Because the forms say the winner says the end, and I sat on that ford all night thinking about what I'd say."
"In Mivon I won forty-one bouts and never once had anything to say at the end of one. I'd just salute and walk off. This time I had something." {n}She winds the leather back on, tight and neat.{/n} "It was you. Don't make me say it twice."''',
        c("[Leave her to her grip.]")),
    jan("read", '''{n}You read them with her, one by one, in the lamplight. She says a word or two about each: a cook, a card-sharp, the boy's father. At the fourth she stops.{/n}
"Pim," {n}she says, and says nothing else. She winds the leather back over his name. It takes her a long time to get it tight enough.{/n}''',
        c("[Leave her to her grip.]")),
], requires=(POSTING,), delay=24)


# Your part: blood and tale runs both ways; the Commander's own worst, and what a callous planner owes a deserter.
meet(YOUR_TALE, "Your part", '"You look like you\'re about to ask me something."', [
    nar("open", '''{n}She has moved the bunk so she can sit in the corner and see the whole cell, the steps and you. There are two tin cups beside her and a jug of the gaol's thin beer.{/n}''',
        c("Continue", "start")),
    jan("start", '''"I've told you my worst. Houndheart, and my legs. Blood and tale works both ways, Commander, even when it isn't a bout." {n}She pours, and pushes a cup across.{/n}
"Tell me yours. The one you go over at night. The one where you look for the moment you decided."''',
        c('"The cage. Striking you, not knowing whether the forms would hold."', "cage", requires=(SCAR,)),
        c('"I spend people. Soldiers, on purpose, to buy something bigger. I learn their names first."', "spend", flags=(TALE_SPENDS,)),
        c('"Kenabres. The ones I couldn\'t get to."', "kenabres"),
        c('"I don\'t go over things at night."', "nothing")),
    jan("cage", '''"Not knowing." {n}She weighs the cup as if it were a blade.{/n}''',
        c("Continue", "cage_planned", requires=(TOLD_PLANNED,)),
        c("Continue", "cage_plain", forbids=(TOLD_PLANNED,))),
    jan("cage_planned", '''"You told me you read me through the bars before you said a word. So you knew where to put the question. You didn't know me. You didn't know whether I'd take them, or whether my pride had died in there with everything else."
"And you swung anyway."''',
        c("Continue", "cage_end")),
    jan("cage_plain", '''"You knew the words. You didn't know me. You didn't know whether I'd take them, or whether my pride had died in that cage with everything else."
"And you swung anyway."''',
        c("Continue", "cage_end")),
    jan("cage_end", '''{n}She drinks.{/n} "That's the difference between us. At Houndheart I didn't know, so I ran. In the Scar you didn't know, so you swung."
"I'm not going to thank you for it. If I'd been less proud, you'd have killed me. But I'd rather be struck by somebody who wasn't sure than saved by somebody who was."''',
        c("[Drink the gaol's terrible beer with her.]")),
    jan("spend", '''{n}She doesn't answer at once. She looks at you over the rim of the cup the way she looked at the vrock on the wall, before her legs had decided anything.{/n}
"That's the thing I ran from." {n}Her voice is quite level.{/n} "Not demons. That. Somebody in charge who knows my name and has worked out what I'm worth." "You'd spend me, if I bought enough."''',
        c('"Yes."', "yes"),
        c('"Not you."', "not_you")),
    jan("yes", '''"Good." {n}She sets the cup down.{/n}
"No, I mean it. Good. At least you'd know my name when you did it, and you told me first. I can fight somebody who tells me first. It's the smiling ones I can't stand."''',
        c("[Drink the gaol's terrible beer with her.]")),
    jan("not_you", '''"Not me?" {n}She sets the cup down, hard.{/n}
"Tell me why. And don't say it's because I'm sitting here, or I'll pour the rest of this over your head."''',
        c("[Drink the gaol's terrible beer with her.]", forbids=("chapter_later",)),   # retired by gating (Q6 follow-up, VOI); index kept
        c('"Because I want you standing next to me when it\'s over. That\'s all. It isn\'t clever."', "not_you_want"),
        c('"Because you\'re the best blade I have. Spending you on anything less than the end would be waste."', "not_you_waste")),
    jan("not_you_want", '''{n}She looks at you for a long breath, ears going pink, and then picks the cup back up so she has something to do with her hands.{/n}
"That's a stupid reason." {n}She drinks.{/n} "Say it again some time when I'm not sitting in a gaol. I want to hear if it sounds the same."''',
        c("[Drink the gaol's terrible beer with her.]")),
    jan("not_you_waste", '''"Waste." {n}She laughs, too loud, the old tavern laugh.{/n} "Well. That's honest, at least. You'd spend me at the end, then. At the big one."
{n}She clinks her cup against yours.{/n} "Good. That's where I'd want to be spent. Just make sure I'm in the front rank when you do it, where I can see it coming."''',
        c("[Drink the gaol's terrible beer with her.]")),
    jan("kenabres", '''"Everybody has Kenabres." {n}She says it gently, for her.{/n}
"I was there too. I was carrying beer through the streets while people burned, laughing too loud, and thinking I was a hero because we'd found a cart." {n}She refills your cup.{/n} "Tell me one of them. One name. I'll drink to them."''',
        c("[Tell her one.]", "one")),
    jan("one", '''{n}You tell her one. She listens the way she listens to a telling in blood and tale, without interrupting, watching for the lie and not finding one.{/n}
"All right," {n}she says at the end, and drinks.{/n} "Now drink your beer."''',
        c("[Drink the gaol's terrible beer with her.]")),
    jan("nothing", '''"Then you're either lying, or you're the most frightening person in Drezen." {n}She studies you over the cup.{/n}
"I'll assume lying. It's kinder to both of us, and you'll tell me the truth eventually. Everyone does, in a cell, if you pour them enough of this."''',
        c("[Drink the gaol's terrible beer with her.]")),
], requires=(HOUNDHEART,), delay=24)


# The Houndhearts' camp: standing where she ran, until she wants to leave.
visit(RIDE, "The Houndhearts' camp", [
    nar("open", '''{n}Your road back from Kenabres passes within a mile of the place, and she knows it; she has not said a word since the last milestone. When you rein in without being asked, she gets down and walks off the road into the scrub.{/n}''',
        c("Continue", "camp")),
    nar("camp", '''{n}There is nothing left of the Houndhearts' camp. Wind and weather have taken the tents and the broken chests, and the scrub has grown back over the trampled ground. On a leaning pole at its edge hangs a strip of cloth that was a banner once, the Houndhearts' hound bleached almost to nothing.{/n}''',
        c("Continue", "here")),
    jan("here", '''"Here." {n}She stops in the middle of nowhere in particular.{/n}
"Elan's chest was here. The runes there, where we chased the quasit. Curl there, where Seelah stood between him and Elan's sword. I was here." {n}She turns, slowly, until she is facing north, toward Numeria.{/n} "And that's where my legs went."''',
        c("[Stand beside her.]", "beside", flags=(RIDE_BESIDE,)),
        c("[Go back to the horses and leave her to it.]", "horses"),
        c('"You don\'t have to do this."', "dont")),
    jan("dont", '''"Yes, I do." {n}She doesn't look round.{/n}
"Go and hold the horses, or stand there. I don't care which. Just don't tell me I don't have to."''',
        c("[Stand beside her.]", "beside", flags=(RIDE_BESIDE,)),
        c("[Go back to the horses.]", "horses")),
    nar("beside", '''{n}You stand beside her, on her right. She notices. She doesn't say anything about it.{/n}''',
        c("Continue", "circle")),
    nar("horses", '''{n}You go back to the road and hold the horses, and watch her from a hundred paces off: a half-elf alone in the scrub with her face to the north.{/n}''',
        c("Continue", "circle")),
    nar("circle", '''{n}She draws her sword and scores a circle in the wet earth around herself, three paces across, one stroke. Then she stands in it, facing north, blade lowered, and doesn't move.{/n}
{n}The wind comes off the Wound. A crow lands on the Houndhearts' pole and looks at her. An hour goes by, or near enough.{/n}''',
        c("Continue", "after_beside", requires=(RIDE_BESIDE,)),
        c("Continue", "after_horses", forbids=(RIDE_BESIDE,))),
    jan("after_beside", '''{n}When she finally sheathes and turns, her boots are soaked through and her face is calm.{/n}
"I stood there until I wanted to leave. Not until my legs did. I wanted to leave ten minutes in, and I stayed another fifty to make sure it was me."
"You stood on my right." {n}She holds up a hand before you can answer.{/n} "Don't. I'd rather not know whether you did it on purpose. I'll decide you did."''',
        c("Continue", "end_pre", forbids=(COMMITTED,)),
        c("Continue", "end_post", requires=(COMMITTED,))),
    jan("after_horses", '''{n}When she finally sheathes and walks back to the road, her boots are soaked through and her face is calm.{/n}
"I stood there until I wanted to leave. Not until my legs did. I wanted to leave ten minutes in, and I stayed another fifty to make sure it was me."
"You went back to the horses. Good. I didn't want an audience."''',
        c("Continue", "end_pre", forbids=(COMMITTED,)),
        c("Continue", "end_post", requires=(COMMITTED,))),
    jan("end_pre", '''{n}She takes her horse's reins from you and doesn't mount straight away.{/n}
"Take me back to Drezen. I've got a bout to arrange, and I've wasted a year not arranging it."''',
        c("[Take her back to Drezen.]")),
    jan("end_post", '''{n}She takes her horse's reins from you and doesn't mount straight away. She leans on the saddle and looks at you across it.{/n}
"Take me back to Drezen. Somewhere with a roof, and you under it." {n}Then, as she mounts:{/n} "And a fire. My feet are ruined."''',
        c("[Take her back to Drezen.]")),
], requires=(HOUNDHEART,), delay=72)


# The Knight-Commander's question (Irabeth, from Jannah's side: her old commander, whose Watch she ran from).
meet(IRABETH, "One question", '"Someone\'s been down here. There\'s a second stool."', [
    nar("open", '''{n}There is a second stool in the cell that wasn't there yesterday, and on it a folded sheet of the Eagle Watch's good paper, with nothing written on it.{/n}''',
        c("Continue", "start", forbids=("irabeth_dead",)),
        c("Continue", "start", requires=("irabeth_dead", "irabeth.trickster.returned")),
        c("Continue", "sergeant", requires=("irabeth_dead",), forbids=("irabeth.trickster.returned",))),
    jan("start", '''"Irabeth. She brought her own stool; I don't think she trusted ours." {n}She picks up the blank sheet.{/n}
"She was my commander. I ran from her Watch. I've been dreading her more than I ever dreaded you, and I was right to."''',
        c("Continue", "appeal", requires=(CONDEMNED,)),
        c("Continue", "rolls", requires=(DEAD_L,), forbids=(CONDEMNED,)),
        c("Continue", "question", forbids=(CONDEMNED, DEAD_L))),
    jan("appeal", '''"She spoke for my appeal once, when I asked to serve in the Condemned instead of rotting in here. The Queen approved it, and Irabeth put her name behind it. I never thanked her. I didn't know how to thank someone for sending me to the worst place in Mendev."''',
        c("Continue", "question")),
    jan("rolls", '''"She signed me onto the roll of the dead in the winter. She told me that first, standing right there. She said she had never had to sign anyone back off it before, and that she disliked the precedent."''',
        c("Continue", "question")),
    jan("question", '''"Then she asked me one question. Not why I ran. Not whether I was sorry. Just: 'Will you run again?'"''',
        c('"What did you tell her?"', "told")),
    jan("told", '''"I told her I didn't know." {n}She turns the paper over.{/n}
"She looked at me for a while, and then she said, 'Good. A promise I can't check is worth nothing to me. Don't know, I can use.' And she left the paper, and went."''',
        c('"Why the blank paper?"', "paper"),
        c('"Irabeth doesn\'t forgive easily."', "forgive")),
    jan("paper", '''"For my answer, when I have one. She said the Watch keeps records, and it'll keep mine, and I can write it in myself when I know." {n}Her mouth twists, not unhappily.{/n}
"She's the only officer I've ever met who'd trust a deserter with her own paperwork. I think it's the cruellest thing she could think of."''',
        c("[Leave her with the paper.]")),
    jan("forgive", '''"She isn't letting me off with a promise." {n}She scowls at the blank sheet.{/n} "And she asked it in front of the sergeant, which was low. 'Will you run again.' Like a quartermaster asking if a boot leaks."
"I'm not writing on her paper until I've got something better than 'don't know' to put on it. She can wait. She's good at waiting. So am I, now."''',
        c("[Leave her with the paper.]")),
    jan("sergeant", '''"The Watch sergeant. The one from the wall." {n}She picks up the blank sheet.{/n}
"He said Commander Irabeth used to do this, before Iz, when someone came back to the Watch who shouldn't have: bring her own stool, ask one question, leave a sheet of paper. He said somebody ought to keep doing it, and he'd drawn the short straw."
"He asked me whether I'd run again. I told him I didn't know. He said that was what she'd have wanted to hear, and left the paper."''',
        c("[Leave her with the paper.]")),
], requires=(RETURNED,), delay=48)


# Yielding the circle (after a rematch the Commander won): the public yield the Commander never paid, given anyway.
meet(YIELD_CIRCLE, "Yielding the circle", '"The muster\'s in an hour."', [
    nar("open", '''{n}She has new notches on the inside of her scabbard, cut the wrong way, and she is looking at them as if they belonged to someone she didn't much like.{/n}''',
        c("Continue", "start", requires=(CAUGHT,)),
        c("Continue", "start_one", forbids=(CAUGHT, LIED, SCAR)),
        c("Continue", "start", requires=(LIED,), forbids=(CAUGHT,)),
        c("Continue", "start", requires=(SCAR,), forbids=(CAUGHT, LIED))),
    jan("start", '''"Two." {n}She runs a thumbnail along them.{/n} "Forty-one bouts in Mivon, and then two, both to you, both the wrong way. I'll get used to it. I'm getting used to a lot of things."''',
        c('[Yield the circle] "At the muster today I\'m going to walk into your chalk and lay my blade down before the salute."', "warn"),
        c('"They were fair bouts. You lost them fairly."', "fair")),
    jan("start_one", '''"One." {n}She runs a thumbnail along it.{/n} "Forty-one bouts in Mivon, and a cell where I won with my mouth, and then one, to you, the wrong way, in front of everybody. I'll get used to it. I'm getting used to a lot of things."''',
        c('[Yield the circle] "At the muster today I\'m going to walk into your chalk and lay my blade down before the salute."', "warn"),
        c('"It was a fair bout. You lost it fairly."', "fair")),
    jan("fair", '''"I know. That's the worst part. If you'd cheated I could hate you for it." {n}She puts the scabbard down.{/n} "Go on. The muster won't wait for either of us."''',
        c("[Leave her with her notches.]", abort=True)),
    jan("warn", '''"Don't." {n}She's on her feet.{/n} "If you're about to tell me you'll throw a bout of mine..."''',
        c('"Not throw it. Yield the circle, by the forms. Before anyone lifts a blade."', "explain")),
    jan("explain", '''{n}She stops.{/n} "Yield the circle." {n}She says it the way you'd say a saint's name.{/n}
"The old man said nobody had done it in his salle in forty years. You walk into the chalk and lay your blade down before the salute and lie back, in front of everyone. It isn't losing. It isn't throwing. It's saying out loud that you won't fight, because you've already decided the other one's the better blade."
"It's the most shameful thing a fencer can do in public. Or it's the other thing. Depends who's watching."''',
        c('"At the muster, then."', "yielded", flags=(PUBLIC_YIELD, YIELDED_CIRCLE), crusade=("Favors", -100)),
        c('"You\'re right. I won\'t."', "not")),
    jan("not", '''"No." {n}She sits back down, slowly.{/n} "No, you'd better not. But you thought about it, and you said it out loud to me. That'll do. That'll do very well."''',
        c("[Leave her with her notches.]")),
    nar("yielded", '''{n}At the fourth bell the whole muster is there, because the whole muster is always there now when Jannah Aldori has chalk in her hand. She draws the circle. You walk into it, and before she has lifted her blade to her brow you lay yours down on the sand at her feet and lie back beside it with your eyes on the sky.{/n}
{n}The yard goes so quiet you can hear the lantern chains on the barracks wall. Somebody on the smithy roof says, "What's the Commander doing?" and somebody else says, "Shut up. It's Mivon."{/n}''',
        c("Continue", "yielded_her")),
    jan("yielded_her", '''{n}Jannah stands over you with her sword still lowered, and her face is doing something very complicated.{/n}
"The Commander yields the circle," {n}she says, not loudly. Then, because the old man would have wanted it said properly, loud enough for the gate:{/n} "The Commander of the crusade yields the circle to Jannah Aldori, of Mivon!"
{n}She quits the circle, as she must. Then she turns on her heel, walks straight back in and lies down in the sand beside you, which is not in any of the forms at all.{/n}''',
        c("Continue", "sand")),
    jan("sand", '''"I'm not cutting a notch for that," {n}she says to the sky.{/n} "It doesn't count. It's the best thing anybody's ever done for me in public, and it doesn't count."
{n}Four hundred soldiers stand around a chalk circle in which their Commander and a deserter are lying on their backs in the sand, and nobody says a word.{/n}''',
        c("[Lie there with her.]")),
], requires=(COMMITTED, YOU_FIRST), forbids=(PUBLIC_YIELD,), delay=72)


# Eyes open: she teaches the yield properly, after the night.
visit(TAUGHT, "Eyes open", [
    nar("open", '''{n}She has chalked a circle on the floor of the last cell, small, just wide enough for one person lying down. She's sitting on the bunk beside it with her boots off and the lamp turned low.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Lie down in it." {n}A pause.{/n} "On your back. Eyes open. You've learned the yield. Tonight you're going to hold it, properly, because I won't have anybody in my circle who can't."''',
        c("[Lie down in the chalk.]", "down"),
        c('[Flirt] "Is this a lesson or an invitation?"', "invite")),
    jan("invite", '''"Yes." {n}She doesn't elaborate.{/n} "Lie down."''',
        c("[Lie down in the chalk.]", "down")),
    nar("down", '''{n}The stone is cold through your shirt. She stands over you with one bare foot either side of the chalk and looks down.{/n}
"Eyes open. Don't blink if you can help it. Don't move. Not until the victor quits the circle."
{n}She walks round the circle, slowly, once. Then again. Her bare foot touches your hand on the second pass and moves on. You don't move.{/n}''',
        c("Continue", "hard")),
    jan("hard", '''"Hard, isn't it? Not moving. Everything in you wants to get up and do something." {n}She kneels at the edge of the chalk, outside it, and her fingertips come down along your jaw to your collar, and stop there.{/n}
"The old man made us lie like this for an hour while the senior students stepped over us to get to the wine. I used to count the ceiling beams. I'm not stepping over you."''',
        c("[Don't move.]", "still"),
        c("[Move.]", "moved")),
    jan("still", '''"Good." {n}Her voice has dropped.{/n} "Now I quit the circle."
{n}She stands, steps back, and waits a long breath. Then she comes back in and lies down in the chalk beside you, pressed close, because there is only room for one, and looks at the ceiling with you.{/n}
"That's the yield. And that's what comes after it, if you're lucky. Nobody teaches that part."''',
        c("Continue", "future")),
    jan("moved", '''{n}You reach up and pull her down into the chalk with you. She comes down laughing against your neck.{/n}
"You moved. You broke the forms. The old man would have thrown you down the stairs." {n}She doesn't get up.{/n} "Luckily, he isn't here."''',
        c("Continue", "future")),
    jan("future", '''{n}After a while, lying there, she says:{/n} "After the war I'm going to chalk a circle in a yard somewhere and teach the forms. Not to make anybody unbeaten. To teach them how to lose and get up again without panicking. And the yield, or the old man would haunt me."
"You could come and lie in it sometimes. Once they've seen the Commander of the crusade lie still in chalk, not one of them will dare to fidget."''',
        c('"I\'ll come."', "end"),
        c("[Say nothing, and stay where you are.]", "end")),
    jan("end", '''{n}The lamp gutters out. Neither of you gets up to see to it.{/n}''',
        c("[Stay in the chalk.]")),
], requires=(NIGHT,), delay=24)


# Fate, again: her father's answer.
meet(REPLY, "Fate, again", '"Your father wrote back?"', [
    nar("open", '''{n}The second letter has the same river-green wax and the same hand leaning into the wind. It is three times as long as the first.{/n}''',
        c("Continue", "truth", requires=(MIVON_TRUTH,)),
        c("Continue", "legend", requires=(MIVON_LEGEND,))),
    jan("truth", '''"He's furious." {n}She sounds delighted.{/n}
"Four pages. Page one: how dare I run. Page two: how dare I let myself be caged. Page three: fate brought me to Mendev, and fate doesn't make mistakes, only daughters do, and he'll go on saying so until one of us is dead."''',
        c("Continue", "truth_end")),
    jan("truth_end", '''"Page four is his mother's recipe for a poultice for scars. He's underlined 'crooked' twice." {n}She folds the letter very carefully along its old creases.{/n}
"He's never written me four pages in my life. Not when I left home, not when I won my first bout. I had to run, and nearly die, and tell him the truth, to get four pages out of him."''',
        c("[Leave her with her father.]")),
    jan("legend", '''"He read it out in the square." {n}She doesn't sound delighted.{/n}
"The whole street. The best blade on the river, holding the walls of Drezen single-handed against a demon lord. He's added the demon lord; I never wrote a demon lord. He's added a great many things."''',
        c("Continue", "legend_end")),
    jan("legend_end", '''"He's happy. He says fate brought me to Mendev and fate doesn't make mistakes. He's having it painted on the salle wall." {n}She puts the letter down on the bunk.{/n}
"I gave him that, and I'd do it again. But I'm going to have to become a very great fencer now, so that it isn't all a lie by the time he dies."''',
        c("[Leave her with her father.]")),
], requires=(MIVON,), delay=96, RequiresAnyGroups=[[MIVON_TRUTH, MIVON_LEGEND]])


# Anything but wings: the night after the raid, at the Commander's door.
visit(AFTER_WALL, "Anything but wings", [
    nar("open", '''{n}Near midnight there is a knock at your door: two short and one long, like a fencer's tempo. It's Jannah, in her shirt, barefoot, with her sword belt over one shoulder because she has clearly forgotten she's carrying it.{/n}''',
        c("Continue", "start")),
    jan("start", '''"I can't sleep. Every time I shut my eyes something lands on a wall." {n}She doesn't come in.{/n} "Talk to me. About anything at all that isn't wings."''',
        c('"Tell me about Mivon, then."', "mivon"),
        c('"Come in. I\'ll talk; you listen."', "you_talk"),
        c('[Flirt] "You could stay."', "stay")),
    jan("mivon", '''{n}She sits down on your floor with her back against the wall, as close to the fire as she can get without being in it.{/n}
"The river in the morning, when the dyers let the colours out and the water goes red, and then blue, and then yellow. The duelling yards on the stairs down to the water; you fight with the whole street leaning off the balconies, throwing fruit at whoever's losing."
"I used to think it was the most beautiful place in the world. Then I came here, where everything's grey and burning, and found out it was just the only place I knew."''',
        c("Continue", "asleep")),
    nar("you_talk", '''{n}She sits down on your floor with her back against the wall, and you talk: about nothing, the small things there's never time for in a war. Food you miss. A song whose ending you can't remember. An animal you remember from before the war. She asks questions in all the wrong places, and laughs at one of your answers, the real laugh, quieter than the Kenabres one.{/n}''',
        c("Continue", "asleep")),
    jan("stay", '''"I could." {n}She looks at you for the space of a breath.{/n}
"I'm not going to. Not like this, frightened, with the wall still in my hands. When I come to you I want to come the way I go into a circle: knowing exactly what I'm doing." {n}She sits down on your floor anyway.{/n} "Talk to me instead."''',
        c("Continue", "you_talk")),
    nar("asleep", '''{n}Somewhere past the second bell she falls asleep sitting up, the sword belt still over her shoulder and her head tipped back against the wall. You put a blanket over her. She doesn't wake.{/n}
{n}In the morning she's gone, and the blanket is folded on the end of your bed with a stick of chalk on top of it.{/n}''',
        c("[Keep the chalk.]")),
], requires=(WALLS,), forbids=(COMMITTED,), delay=12)


# Curl: the fourth of the League, and the one thing she might have seen before she ran.
meet(CURL, "The fourth of the League", '"You never talk about Curl."', [
    nar("open", '''{n}The pewter tankard is on the shelf above the bunk, turned so that the four stick figures on its side face the wall. She has been looking at it since before you came down.{/n}''',
        c("Continue", "start")),
    jan("start", '''"No. I don't." {n}She doesn't take her eyes off the tankard.{/n}
"Curl was the one I liked best, at first. A halfling thief with red hair and a laugh like a dropped tray, who'd stolen from everyone in Kenabres and paid most of them back. He said he wasn't cut out for war. He said he didn't want to die. I thought that was the most honest thing anybody in that city had said all year."''',
        c("Continue", "camp")),
    jan("camp", '''"At Houndheart Curl wasn't Curl. He came out of nowhere and snatched Elan's ring out of the quasit's paws, and called things up out of the ground, and Elan called him a traitor and swung at him, and Seelah threw herself in the way. She said afterwards they must have bewitched him." {n}She turns her hands over and looks at the palms.{/n}
"I was across the camp from him. I could see his face. I've gone over it a hundred times. Whether I saw his face change before I ran."''',
        c('"Did you?"', "did"),
        c('"It wouldn\'t matter if you had."', "matter")),
    jan("did", '''"I don't know." {n}She says it the way a fencer admits a touch she can't feel yet.{/n}
"Some nights I'm sure I saw him smile at me across the camp, and it wasn't his smile, and that's what my legs understood before I did. Other nights I'm sure I made that up afterwards, in the cage, because it's easier to have run from a demon wearing a friend than from a fight."''',
        c("Continue", "which", forbids=(SOULS_HOME,)),
        c("Continue", "which_home", requires=(SOULS_HOME,))),
    jan("matter", '''"It would to me." {n}She is quiet a moment.{/n}
"If I saw it, then my legs knew something my head didn't, and I ran from the right thing at the wrong time. If I didn't, I just ran. I'd give a great deal to know which."''',
        c("Continue", "which", forbids=(SOULS_HOME,)),
        c("Continue", "which_home", requires=(SOULS_HOME,))),
    jan("which_home", '''"And I could ask him. That's the worst part. When Seelah brought the souls back, his was among them, they say. I haven't heard what became of him after." {n}She reaches up and turns the tankard round, so the four figures face the room.{/n}
"I haven't gone. What would I say? 'You ran too'? At the camp it wasn't even him in there. I ran myself." {n}She scowls at the tankard.{/n} "I'll go. When I've got something to say that isn't that."''',
        c('"Keep him facing the room."', "room"),
        c("[Say nothing.]", "quiet")),
    jan("which", '''"The worst part is I can't ask him. I haven't spoken to him since the camp, and I don't know that there's anybody in there to ask."
{n}She reaches up and turns the tankard round, so the four figures face the room again.{/n} "I keep him facing the wall when I'm angry with him. I'm always angry with him. Then I remember he was frightened too, and he said so out loud, which is more than I ever did, and I turn him back."''',
        c('"Keep him facing the room."', "room"),
        c("[Say nothing.]", "quiet")),
    jan("room", '''"For now." {n}She looks at the tankard a while longer.{/n} "He'd have liked you. He liked anyone who got away with things. He'd have tried to pick your pocket and then apologised and given you back somebody else's purse."''',
        c("[Leave her with the League.]")),
    jan("quiet", '''{n}She lets the silence be, the way she'd let a blade rest in the chalk.{/n}
"Thank you," {n}she says eventually.{/n} "Everyone else tells me it wasn't my fault. I don't know that it wasn't. Neither do they."''',
        c("[Leave her with the League.]")),
], requires=(HOUNDHEART,), delay=48)


# What the vrocks wanted: the cage from the inside, after the wall woke it up.
meet(VROCKS, "The ritual", '"You were shaking on the wall. Before."', [
    nar("open", '''{n}She is sitting on the floor of the cell with her back against the bunk and her sword across her knees, unsheathed. The lamp is turned up as far as it will go.{/n}''',
        c("Continue", "start")),
    jan("start", '''"I was." {n}She doesn't pretend otherwise.{/n}
"You want to know why vrocks, and not demons in general. Everybody on the wall was frightened of demons. I was frightened of those."''',
        c('"Tell me about the cage."', "cage"),
        c('"You don\'t have to."', "dont")),
    jan("dont", '''"I know I don't. That's why I'm going to." {n}She sets the sword flat on the stones beside her.{/n}''',
        c("Continue", "cage")),
    jan("cage", '''"There were two crusaders in the cages next to mine when they caught me. Knights. The vrocks did something to them. A ritual. Dancing, and chanting, and a smell like hot copper, and then the knights weren't knights any more." {n}She says it very evenly.{/n}
"They told me I'd be next. Then they didn't do it. Not the next day, or the day after. I just had to watch the knights, and wait. They liked that I was waiting. I could tell."''',
        c("Continue", "waiting")),
    jan("waiting", '''"That's what I was afraid of on the wall. Not the claws. The waiting. Standing there while something decides what it's going to do to you, and knowing you'll let it, because you let the last one."
{n}She picks the sword back up.{/n} "Then I moved. That's all. I moved, and it stopped being a cage."''',
        c('"You moved. Remember that part."', "remember"),
        c('[Sit down on the floor beside her.]', "beside")),
    jan("remember", '''"I'm trying to. It's shorter than the other part. The waiting went on for weeks. The moving took about a minute." {n}Her mouth twists.{/n}
"My master would say a minute is plenty. Most bouts are over in less."''',
        c("[Leave the lamp turned up.]")),
    jan("beside", '''{n}You sit down on the cold floor beside her. After a while she leans until her shoulder is against yours, and puts the sword back in its sheath without looking at it.{/n}
"Leave the lamp up," {n}she says.{/n} "I know it's a waste of oil. Leave it up anyway."''',
        c("[Leave the lamp turned up.]")),
], requires=(WALLS,), delay=24)


# The old man: her master, the Aldori, and why Mivon.
meet(MASTER, "The old man", '"Tell me about your master."', [
    nar("open", '''{n}She is sitting on the bunk rewinding a strip of leather round the hilt of a practice sword, not because it needs it but because her hands want something to do.{/n}''',
        c("Continue", "start")),
    jan("start", '''"The old man." {n}She says it with enormous affection and no warmth whatsoever.{/n}
"He was an Aldori from a family that came down from Rostland when Choral the Conqueror took it, a long time ago. The swordlords who wouldn't bend fled south to Mivon, and taught there, and never stopped talking about it. He talked about Choral's dragons as if he'd fought them personally. He was seventy."''',
        c("Continue", "salle")),
    jan("salle", '''"His salle was above the dye-works, so everything smelt of indigo and piss, and the floor was stained blue where the old boards had soaked it up. He took twelve students a year and threw out ten. He never said well done. He said 'less bad' when he was pleased, and 'again' when he wasn't, and 'again' was most of what he said."''',
        c('"Why did he keep you?"', "keep"),
        c('"Did he know you\'d left for the crusade?"', "left")),
    jan("keep", '''"Because I was quick, and proud, and I hated losing more than I loved anything else. He said that was the only thing that couldn't be taught." {n}She tightens the leather.{/n}
"He also said it would get me killed. He said it about once a week, usually while I was bleeding."''',
        c("Continue", "now")),
    jan("left", '''"He gave me the sword at the river stairs. He'd never said a kind word to me in seven years. He put it in my hands and said, 'Don't come back with it dirty.'"
{n}She tightens the leather.{/n} "I thought he meant with blood. I think now he meant with running."''',
        c("Continue", "now")),
    jan("now", '''"He'd be ashamed of Houndheart. He'd be ashamed of the cage. He'd be ashamed of the cell, and of a Commander of the crusade who learned the forms from a deserter, in a cell, on the wrong side of the bars."
{n}She holds the practice sword up and sights along it.{/n} "And then he'd say 'again'. That's the thing about the old man. He never once said you were finished. He just said again, until you stopped being bad at it."''',
        c('"Again, then."', "again"),
        c('"I\'d like to have met him."', "met")),
    jan("again", '''{n}She laughs, surprised into it.{/n} "Again." {n}She tosses you the practice sword, hilt first, and stands.{/n} "Get up. Three steps, the wrist, recover. You'll be less bad by midnight."''',
        c("[Get up.]")),
    jan("met", '''"No, you wouldn't. He'd have told you your grip was an insult to his ancestors and thrown you down the stairs." {n}She considers.{/n}
"And then he'd have asked me who you were, very quietly, when you'd gone. He always asked about the ones he threw down the stairs. Those were the ones he liked."''',
        c("[Leave her to the leather.]")),
], requires=(FORMS,), delay=48)


# Recruits: she drills the Eagle Watch's new blood in the yard, including the ones who sang about her.
meet(RECRUITS, "Again", '"I hear you\'ve been drilling the Watch recruits."', [
    nar("open", '''{n}She isn't in the cell. The turnkey points you up the steps to the practice yard, where twelve Eagle Watch recruits in new blue are standing in a line of chalk circles, sweating, and Jannah Aldori is walking along the line with her hands behind her back like a very young, very unforgiving old man.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Again." {n}She says it to the whole line without raising her voice, and twelve recruits go through the sequence again: three steps, the wrist, recover.{/n}
{n}When she sees you she doesn't stop. She comes and stands beside you and watches them.{/n} "The sergeant asked. Half of them are from Kenabres. Half of them have never held anything but a pitchfork. Two of them sang that song about me in the tavern last week."''',
        c('"Which two?"', "which"),
        c('"How are they?"', "how")),
    jan("which", '''"The third and the ninth." {n}She doesn't point.{/n} "I haven't said anything. I've just made them demonstrate the yield in front of the others, lying in the chalk with their eyes open, for a quarter of an hour. Each. Twice."
{n}Her face is perfectly grave.{/n} "It's a very important part of the forms."''',
        c("Continue", "how")),
    jan("how", '''"Bad. Less bad than yesterday." {n}She catches herself saying it and her mouth twitches.{/n} "Gods. I sound like him."
"The girl on the end is good. Quick. Proud. Hates losing more than she loves anything. I'm going to have to be very careful with her." {n}She watches the girl go through the sequence, fast and clean and a little too hard.{/n} "Somebody should have been careful with me."''',
        c('"You\'re good at this."', "good"),
        c('"Teach her the yield first."', "yield")),
    jan("good", '''"I'm not. I'm impatient and I'm unkind and I keep saying 'again'." {n}She watches the line a moment longer.{/n}
"But none of them is going to go into their first real fight thinking they've never lost. I'll have made sure of that. It's the only thing I know that the old man didn't."''',
        c("[Watch the drill.]")),
    jan("yield", '''"I already have." {n}She looks at you sidelong.{/n}
"First lesson, before the salute: how to go down and get up again. They'll all be on their backs one day, and I'd rather they didn't panic when they are."''',
        c("[Watch the drill.]")),
], requires=(COMMITTED,), delay=48)


# The scar (killed worlds, after the night): once, by lamplight, the mark the Commander made.
meet(TRACE, "Once", '"You keep touching it."', [
    nar("open", '''{n}She is sitting on the bunk with a small steel mirror propped against her knee, looking at the scar on her temple the way she looks at a bout she has lost: carefully, without mercy, and a little curious.{/n}''',
        c("Continue", "start")),
    jan("start", '''"It's knitting. The carter's wife's stitches are finally coming out on their own." {n}She tilts the mirror.{/n}
"It'll be white by the spring. Everyone who sees it will know somebody cut me there. Nobody will know it was first blood and not a killing blow, unless I tell them. I haven't decided whether to."''',
        c('"Tell them. It was a fair bout."', "tell"),
        c('"It\'s yours to tell or keep."', "keep")),
    jan("tell", '''"A fair bout in a cage." {n}She lowers the mirror.{/n} "You're very certain for somebody who had the only room to move."
{n}Then she puts the mirror down altogether.{/n} "Come here."''',
        c("Continue", "trace")),
    jan("keep", '''"Mine." {n}She tries the word, and seems to like it.{/n} "Yes. It is, isn't it. You made it, but it's on me, so I get to say what it means."
{n}She puts the mirror down.{/n} "Come here."''',
        c("Continue", "trace")),
    nar("trace", '''{n}She takes your hand and puts your fingers at her brow, where the scar begins, and lets you follow it: over the temple, along the line of the bone where the blade turned, up to above the ear where it stops. She keeps her eyes open the whole time and doesn't blink.{/n}''',
        c("Continue", "once")),
    jan("once", '''"Once," {n}she says, when you reach the end of it.{/n} "You get to do that once a year. On the day of the Scar. Not on any other day, and not because you're sorry."
{n}She holds your hand there a moment longer than she meant to.{/n} "I'm going to enjoy making you wait for it."''',
        c("[Take your hand back when she lets you.]")),
], requires=(SCAR, NIGHT), delay=24)


# The song: the Eagle Watch's verses about the muster, and her corrections.
visit(SONG, "Aldori, sorry", [
    nar("open", '''{n}There is singing in the tavern under the barracks when you pass it after the evening bell: a dozen Eagle Watch voices, loud and unmusical, and the tune is one every soldier in Drezen seems to know by now.{/n}
{n}Through the window you can see Jannah standing on a bench at the back of the room, with a mug in one hand, conducting.{/n}''',
        c("[Go in.]", "inside"),
        c("[Listen from the door.]", "door")),
    nar("inside", '''{n}Nobody stops singing when you come in, which tells you exactly how long they've been at it. Jannah sees you over the heads and, without missing a beat, points her mug at you, and the whole room turns and sings the next verse straight at the Commander of the crusade.{/n}''',
        c("Continue", "verse")),
    nar("door", '''{n}You stay out on the step with your hood up and let the song wash out into the street. It's a dreadful song. It rhymes 'Aldori' with 'sorry' and 'first blood' with 'worst mud', and someone has put a verse in about the Houndheart camp that makes the whole room go quiet for two lines before it picks up again.{/n}''',
        c("Continue", "verse")),
    jan("verse", '''{n}When it's over she climbs down off the bench and comes to you, flushed, with foam on her lip and her eyes very bright.{/n}
"They had the Houndheart verse wrong. They had me never going near the quasit. I made them change it." {n}She wipes her mouth with the back of her hand.{/n} "Now I run after I've had a go at the quasit, which is true, and I come back in the last verse, which is also true, and it doesn't rhyme at all, and I don't care."''',
        c('"You made them sing it right."', "right"),
        c('[Flirt] "Sing me the last verse."', "sing")),
    jan("right", '''"I made them sing it true. Right would take a better poet than a dozen Watch recruits and me." {n}She takes your arm, in front of the whole room, as if it were the most ordinary thing in the world.{/n}
"Walk me home. I've had four of these and I'm going to be unbearable about my drilling in the morning."''',
        c("[Walk her home.]")),
    jan("sing", '''"Absolutely not." {n}She is laughing.{/n} "I have a terrible voice. The old man used to make me hum while I fenced so I'd stop holding my breath, and every other student in the salle begged him to let me stop."
{n}Then, quietly, walking, when nobody else can hear, she sings it anyway: the last verse, the one that doesn't rhyme.{/n}''',
        c("[Walk her home.]")),
], requires=(COMMITTED,), delay=72)


# The board by the chapel (killed worlds): her own name on the roll of the dead.
meet(BOARD, "Spelled wrong", '"Show me the board."', [
    nar("open", '''{n}She takes you up out of the gaol and across the square to the chapel wall, where the crusade posts the names of its dead on long boards under a little roof. The paint on the older boards has run in the rain. Hers is on one of the newer ones, near the bottom: JANNA ALDORI, EAGLE WATCH, MOLTEN SCAR.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Without the aitch." {n}She stands with her hands behind her back, reading it the way other people read their horoscope.{/n}
"I come and look at it most days. It's a strange thing, reading your own name among the dead. You'd think it would frighten you. It doesn't. It's restful. Nobody expects anything of Janna Aldori. She's done."''',
        c("Continue", "nameless", requires=(NAMELESS,)),
        c("Continue", "named", forbids=(NAMELESS,))),
    jan("nameless", '''"And that's who I am now, by your word: nobody. Janna Aldori is dead on the board, and the one standing here doesn't have a name at all." {n}She doesn't look at you.{/n}
"I keep it. I said I would. But I come here to look at her, because at least she had a name, even if they spelled it wrong."''',
        c('"I could have it struck. Give you your name back."', "strike_nameless"),
        c('"Leave it. She\'s done. You aren\'t."', "leave")),
    jan("named", '''"Irabeth says she can have it struck. One line of ink, and I'm alive again on paper, and the Watch can stop being embarrassed."
{n}She tilts her head at the board.{/n} "I haven't let her. I don't know why. Maybe I like having somewhere to visit her."''',
        c('"Have it struck. You\'re not her any more."', "strike"),
        c('"Leave it. She\'s done. You aren\'t."', "leave")),
    jan("strike_nameless", '''{n}She turns and looks at you properly.{/n}
"You'd take it back. What you said over me." {n}A long breath.{/n} "No. Not yet. You said it, and I kept it, and I want to have kept it for a while longer before you undo it. Otherwise it wasn't worth anything, the keeping."
"Ask me again after the war."''',
        c("[Leave the board as it is.]")),
    jan("strike", '''"I'm not her any more." {n}She tries it out.{/n}
"No. I'm not, am I. She was the one who ran and the one who lay in the ash. I'm the one who walked out of it." {n}She reaches up and touches the painted name, lightly, the way you'd touch the shoulder of somebody you were leaving.{/n}
"All right. Tell Irabeth to strike it. But tell her to spell it right first, so the one she strikes is the right one."''',
        c("[Leave the board to Irabeth's ink.]")),
    jan("leave", '''"She's done. I'm not." {n}Something eases in her shoulders.{/n}
"Yes. I'll leave her there. Somebody ought to be on that board for the Molten Scar, and it might as well be the girl who deserved it." {n}She turns her back on it.{/n} "Buy me a drink. Being dead makes me thirsty."''',
        c("[Buy her a drink.]")),
], requires=(SCAR, FORMS), delay=48)


# The jeweller's door (Seelah's Q3 world): the post she kept while Elan went in.
meet(DOOR, "The door she kept", '"Tell me about the jeweller\'s."', [
    nar("open", '''{n}She is cleaning her blade with slow, even strokes, although it's clean already. She has been doing it since you came down.{/n}''',
        c("Continue", "start", requires=(ELAN_DEAD,)),
        c("Continue", "start_lives", forbids=(ELAN_DEAD,))),
    jan("start_lives", '''"Elan saw Sunhammer with the souls and wanted to go after him that minute. He didn't. He waited for you, the way you'd told him, and the two of us held the mouth of that cave with our backs to it while you went down." {n}The cloth goes down the blade and back.{/n}''',
        c("Continue", "elan_lives")),
    jan("start", '''"Elan saw Sunhammer with the souls and went after him. Alone. I begged him to wait for you; he told me to stay at the mouth of the cave, and I did." {n}The cloth goes down the blade and back.{/n}
"I've kept a lot of doors since Houndheart. His was trapped, and he opened it, because he was thinking about Kiana and not about doors."''',
        c("Continue", "elan_dead", requires=(ELAN_DEAD,)),
        c("Continue", "elan_lives", forbids=(ELAN_DEAD,))),
    jan("elan_dead", '''"And he was lying there when I came down, and Seelah got to him first, and I said something stupid about good people dying." {n}The cloth stops.{/n}
"I meant it. It's still stupid. I've gone over it more than Houndheart. Whether I'd have seen the trap if I'd gone in with him. Whether I'd have been fast enough. I'll never know. That's the thing about keeping your place in a file: you never find out what would have happened if you'd left it."''',
        c('"You kept your post. That\'s all a soldier gets to know."', "post"),
        c('"If you\'d gone in with him, you\'d be dead too."', "dead")),
    jan("elan_lives", '''"And everybody came out." {n}Something like a smile.{/n}
"I didn't do anything clever. I kept my place and I didn't run, and when you came back up I couldn't stop shaking. But everyone came out."''',
        c('"You kept your post. That\'s all a soldier gets to know."', "post"),
        c('"When it was over, you asked if you\'d won."', "won")),
    jan("post", '''"That's all a soldier gets to know." {n}She turns the blade so the lamplight runs down it.{/n}
"My master would hate that. He'd say a fencer always knows. But I wasn't fencing, was I. I was soldiering, badly, for the second time in my life, and the second time I didn't run."''',
        c("[Leave her to the blade.]")),
    jan("dead", '''"Probably." {n}She doesn't pretend it helps.{/n}
"Seelah says the same. Everybody says the same. And every one of them would have opened that door without thinking twice, for someone they loved, and I know it, and so do they." {n}She sheathes the blade.{/n} "I stayed in my place. That has to be enough. Most nights it is."''',
        c("[Leave her to the blade.]")),
    jan("won", '''{n}She laughs, caught out.{/n} "I did, didn't I. 'Wait, we won? We completed our mission?' Like a girl at her first tournament." {n}She shakes her head.{/n}
"I'd forgotten what winning felt like. Not a bout. The other kind, where everybody's on the same side and nobody's keeping score. I'd like more of that. I don't know if I'm allowed it."''',
        c("[Leave her to the blade.]")),
], requires=(JOINED, FORMS), delay=48)


# The duelling stairs: after the commit, what she'd show the Commander in Mivon.
meet(STAIRS, "The duelling stairs", '"You\'re planning something."', [
    nar("open", '''{n}She has a scrap of paper on her knee and is drawing on it with a stub of charcoal: a river, a flight of steps down to the water, balconies, little crosses that might be people or might be lanterns.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Mivon." {n}She turns the paper round so you can see.{/n}
"The duelling stairs, down to the river by the dye-works. After the war, if there's an after, I'm going to take you there, and walk you down them at noon on a market day, when every balcony on the street is full."''',
        c('"And what happens on the stairs?"', "what"),
        c('[Flirt] "In front of the whole street?"', "street")),
    jan("what", '''"I introduce you to my father. On the third step. Where everybody can hear." {n}She taps the drawing.{/n}
"He'll want to know if you can fence. He'll want to know which of us has drawn blood on the other, and how often, and I'm going to tell him the truth, whatever it is, and watch what his face does." {n}She's smiling now.{/n} "I think he'll challenge you. I think I'll let him."''',
        c("Continue", "end")),
    jan("street", '''"Everything worth doing in Mivon is done in front of the whole street. That's the point of the balconies." {n}She tucks the charcoal behind her ear.{/n}
"You've already stood in a chalk circle with me in front of four hundred soldiers. A street of dyers throwing fruit won't bother you."''',
        c("Continue", "end")),
    jan("end", '''{n}She folds the drawing in four and puts it inside her gambeson, over her heart, without apparently noticing she's done it.{/n}
"If there's an after," {n}she says again.{/n} "There might not be. But I've stopped planning for running, and I have to plan for something."''',
        c("[Leave her with her plans.]")),
], requires=(COMMITTED,), delay=96)


# Irabeth's paper: the answer she writes on the Watch's blank sheet, after the wall.
meet(PAPER, "The answer", '"You\'ve written something."', [
    nar("open", '''{n}The blank sheet of Watch paper is on the bunk, not blank any more. There are three lines on it in her upright, finished hand, and a great deal of crossing-out above them.{/n}''',
        c("Continue", "start")),
    jan("start", '''"For Irabeth. Or for the Watch, or whoever reads these." {n}She doesn't hand it over. She reads it to you herself, flatly, the way she'd read out a bout's result.{/n}
"'Will you run again? I don't know. I didn't, on the wall, with the vrocks. I didn't, at the muster, in front of everyone. That's two. I'll write again when it's three.'"''',
        c('"That\'s a good answer."', "good"),
        c('"What\'s under the crossing-out?"', "crossed")),
    jan("good", '''"It's a true one. I don't know about good." {n}She folds the sheet along a line she has clearly already folded several times.{/n}
"My master used to make us keep a tally of bouts. I've started keeping a different one. Not wins. Times I stayed." {n}She puts the sheet inside her gambeson.{/n} "Two is a very short tally. I'm going to make it longer."''',
        c("[Leave her with her tally.]")),
    jan("crossed", '''"Lies, mostly." {n}She doesn't seem embarrassed.{/n}
"'No, never.' That was the first one. Then 'Not while the Commander's watching', which was worse. Then a long bit about Houndheart that Irabeth doesn't need, and then a very rude line about the Watch's paper, which is too thin." {n}She folds it.{/n}
"The three lines at the bottom are what was left when I'd crossed out everything I couldn't stand behind. That's how the old man taught us to write up a bout, too."''',
        c("[Leave her with her tally.]")),
], requires=(IRABETH, WALLS, "jannah.trickster.challenge"), delay=24)   # Q6 (BEL): after the muster she counts


# Forty-two, the right way (after she drew first blood at the muster).
meet(NOTCH, "The right way", '"You\'re cutting a notch."', [
    nar("open", '''{n}She has her scabbard across her knees and the point of a small knife resting on the leather inside its throat, and she hasn't made the cut yet. She has been sitting like that for some time.{/n}''',
        c("Continue", "start")),
    jan("start", '''"Trying to." {n}The knife stays where it is.{/n}
"I drew first blood on the Commander of the crusade in front of four hundred soldiers. By the old man's reckoning that's a win, a clean one, and it goes in the scabbard the right way, next to the others." {n}The knife doesn't move.{/n} "I can't make myself cut it."''',
        c('"Why not?"', "why"),
        c('"You earned it."', "earned")),
    jan("earned", '''"I know I did. You didn't give it to me; I'd have known, and I'd have hated you." {n}She turns the knife.{/n}''',
        c("Continue", "why")),
    jan("why", '''"Because every other notch in here is somebody I beat and walked away from. I saluted, I quit the circle, and I never thought about them again. That was the point. That's what winning was, in Mivon."
{n}She lifts the knife off the leather.{/n} "You I didn't walk away from. I won, and then I stayed. It doesn't belong in there with the others. It isn't the same kind of thing."''',
        c('"Then cut it somewhere else."', "elsewhere"),
        c('"Then don\'t cut it."', "dont")),
    jan("elsewhere", '''{n}She considers that. Then she turns the scabbard over and, on the outside, near the mouth, where anyone who looked could see it, she cuts a small, neat circle with one stroke through it: her old salle's mark.{/n}
"There," {n}she says.{/n} "Not a notch. The other thing."''',
        c("[Leave her with it.]")),
    jan("dont", '''"No." {n}She puts the knife away.{/n}
"No, I won't. The right-way ones, and the wrong-way ones, and then nothing. Anybody who counts will think I stopped fencing." {n}She looks at you at last.{/n} "Let them think it. The ones who matter will know I only stopped counting."''',
        c("[Leave her with it.]")),
], requires=(COMMITTED, SHE_FIRST), delay=48)


# The last muster before the end: what she asks, and what she doesn't.
meet(LAST_MUSTER, "Before the last road", '"They say we march soon."', [
    nar("open", '''{n}Every forge in Drezen has been going since dawn, and the gaol is loud with the noise of it through the stone. She is packing: not much, a blanket, a whetstone, the pewter tankard wrapped in a shirt. Her sword is already at her hip.{/n}''',
        c("Continue", "start")),
    jan("start", '''"We do. I've asked the Watch sergeant for a place in the line. Not at the back, where they put people they're not sure of. In the front, where I can see what's coming." {n}She ties off the blanket roll.{/n}
"I want to ask you something before we go, and I want you to say yes without thinking about it, because if you think about it you'll say something sensible."''',
        c('"Ask."', "ask")),
    jan("ask", '''"If I run." {n}She says it steadily.{/n} "At the end, in front of whatever's waiting, if my legs decide. Don't come after me. Don't send anybody. Don't make it a story."
"Let me find out on my own whether I stop. The way I've found out since the wall. If I come back, I come back on my own feet. That's the only way it counts."''',
        c('"Yes."', "yes"),
        c('"No. I\'ll come after you. Every time."', "no")),
    jan("yes", '''"Thank you." {n}She lets out a breath.{/n}
"I don't think I'll run. I think I'm done with it. But I thought I was done with it before Houndheart, too, and I was a great deal surer then." {n}She shoulders the blanket roll.{/n} "Come on. The sergeant hates waiting, and so do I."''',
        c("[Go with her.]")),
    jan("no", '''{n}She stares at you. Then she laughs, and it isn't the tavern laugh or the bitter one. It's a new one, and it seems to surprise her.{/n}
"That's the least sensible thing you've ever said." {n}She shoulders the blanket roll.{/n} "All right. Come after me, then. I'll try very hard to make it a short walk."''',
        c("[Go with her.]")),
], requires=(COMMITTED, NIGHT), delay=120)
