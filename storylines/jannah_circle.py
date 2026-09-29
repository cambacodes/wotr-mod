"""Jannah: the spine between her return and her challenge (the forms, Houndheart, the wall), and the optional beats around it.

Every physical scene is at her presence in the last cell of the old Drezen gaol (jannah_trickster PRESENCE); the wall is a
night alarm, delivered at a rest. Each beat engages a canon anchor of hers:
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
                                         MIVON_TRUTH, NAMELESS, POSTING, PRESENCE, PRISON, REL, RELEASED, RETURNED, SCAR,
                                         SEELAH_BACK, SEELAH_DEAD, SEELAH_FOR_HER, SEELAH_GONE, SEELAH_HERSELF, SEELAH_KEPT,
                                         STORY_LOST, UNIT, WALL_SALUTE, WALL_SHIELD, WALL_WATCHED, WALLS, jan, nar)

SCENES = []
C = "jannah.circle."

BLADE = C + "blade"
SEELAH = C + "seelah"
MIVON = C + "mivon"
KENABRES = C + "kenabres"
WATCH = C + "the_watch"
BLADE_HELD = C + "blade.held"
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
                        optional=optional, Relationship=REL, Remote=True, Kind="visit", Chapters=[5], **extra))


# --- 1. The forms (spine): what she keeps like a faith, taught properly. ---------------------------------------------------

meet(FORMS, "The forms", '"You\'re drawing circles again."', [
    nar("open", '''{n}She has begged a stick of chalk off the quartermaster's clerk, and the circle on the cell floor is white now, and exact. She is standing in the middle of it in her stockings, running a sequence against nobody: three steps, a turn of the wrist, a recovery, over and over, slow enough to count.{/n}''',
        c("Continue", "scar", requires=(SCAR,)),
        c("Continue", "story", forbids=(SCAR,))),
    jan("scar", '''"If you're going to keep coming down here, you're going to learn them properly." {n}She finishes the sequence before she looks at you.{/n}
"You knew the words in the Scar. Knowing the words isn't knowing the forms. And nobody in Mendev knows the words. So tell me: where did you get them?"''',
        c('"From a book. A very dull one."', "book"),
        c('"I made it my business to know them before I ever came to that cage."', "planned", flags=(TOLD_PLANNED,)),
        c('[Lie] "I\'ve crossed blades with Aldori before."', "lie")),
    jan("story", '''"If you're going to keep coming down here, you're going to learn them properly." {n}She finishes the sequence before she looks at you.{/n}
"You caught me in a story. That isn't the same as catching me in a circle, and I'd hate for you to get the two confused. It could be fatal."''',
        c('"Then teach me."', "salute")),
    jan("book", '''"A book." {n}She looks personally offended.{/n} "Somebody wrote the forms down. In a book. For anybody to read." {n}She shakes her head.{/n}
"My master would have had him flogged with the binding. Well. It saved my life, so I suppose the flogging can wait."''',
        c("Continue", "salute")),
    jan("planned", '''"Before you ever came to the cage." {n}She stops moving.{/n}
"You knew there was a deserter in the Molten Scar. You knew she was an Aldori. You went and found out what an Aldori would do with a blade in her hand and her pride in her throat, and then you walked in and did it."
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
"This. The distance at which I can touch you with one step. Outside it, you're safe. Inside it, you're mine. In Mivon they teach you never to stand inside measure unless you mean to finish something."
{n}She doesn't step back.{/n}''',
        c('[Step inside her measure.]', "inside", flags=(MEASURE_FLIRT,)),
        c('"And the yield?"', "yield")),
    jan("inside", '''{n}You take the step. The point of her blade slides past your shoulder, and now there is nothing between you but the width of a breath.{/n}
"That," she says, not quite steadily, "is exactly what they tell you not to do." {n}She doesn't step back either. After a while she remembers she's holding a sword and lowers it.{/n}
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
    jan("rain", '''"It rained at Houndheart." {n}She doesn't look up.{/n} "That's the thing nobody tells you about the worst day of your life. It has weather."''',
        c("Continue", "told", requires=(CAUGHT,)),
        c("Continue", "told", requires=(LIED,)),
        c("Continue", "told", requires=(STORY_LOST,)),
        c("Continue", "untold", forbids=(CAUGHT, LIED, STORY_LOST))),
    jan("told", '''"We told the camp in the cell, you and I, each other's parts. But blood and tale is about what you did. It isn't about what was going on in your head while you did it. My master said that part belonged to nobody but the fencer. I'm going to give it to you anyway."''',
        c("Continue", "league")),
    jan("untold", '''"You were there. You saw me go. You've never asked me why, and everyone else has asked me nothing else for a year, so I'm going to tell you, and you're going to sit there and let me."''',
        c("Continue", "league")),
    jan("league", '''"Seelah talked us into it. Elan's ring for his Kiana, lost in the mud at the Houndhearts' camp on the edge of the Wound. The League of the Inspiring Cart, riding out to find a ring. It was going to be a story. We were going to tell it in the Defender's Heart for years."
"No glory without risk. That was Seelah's. I used to shout it louder than she did."''',
        c("Continue", "camp")),
    jan("camp", '''"Then the camp was full of demons, and Curl was... whatever Curl was that day, and there was the rain, and the fire, and somebody screaming who might have been me." {n}The bucket in the corner goes on filling.{/n}
"Everyone asks why I ran. I've been asking for a year. I've gone over it the way I'd go over a lost bout, stroke by stroke, looking for the moment I decided."''',
        c("Continue", "legs")),
    jan("legs", '''"There isn't one. I didn't decide. My legs decided, and I went with them, and I was two miles north into the rain toward Numeria before I remembered I had a head."
{n}She looks at her hands.{/n} "That's what I can't live with. Not that I was afraid; everyone's afraid. That I wasn't there when it happened. I'd understand a coward. I don't understand a pair of legs."''',
        c("Continue", "blame")),
    jan("blame", '''"And then in the Scar I blamed Seelah for it. Her heroics, her motto, all of it. I'd have said it to anybody who stood still long enough." {n}Her mouth twists.{/n}
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
"My master used to say a lost bout has two halves: the losing, and what you do with your sword afterwards. I've spent a year practising the first half. Over and over. I'm very good at it now."
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

visit(WALLS, "Wings over the north wall", [
    nar("open", '''{n}The alarm comes an hour before first light: bells from the north wall, then shouting, then the sound every soldier in Drezen has learned to hate, wings the size of sails beating the dark. Vrocks. A raiding flight of them, come down out of the Wound's glow to see what's soft.{/n}
{n}By the time you reach the wall walk the Eagle Watch are already on it, and so is a half-elf in a gambeson with a long Aldori blade, who isn't on anyone's roster and got there first.{/n}''',
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
], requires=(HOUNDHEART,), delay=48, optional=False)


# --- Optional beats. -------------------------------------------------------------------------------------------------------

# Seelah (must-acknowledge): the friend she failed, from Jannah's side only.
meet(SEELAH, "The League of the Inspiring Cart", '"Tell me about Seelah."', [
    nar("open", '''{n}She is turning a battered pewter tankard over in her hands, the kind the Defender's Heart used to hang behind its bar. Someone has scratched a little cart on the side with a knife point, and four stick figures pushing it.{/n}''',
        c("Continue", "mourn", requires=(SEELAH_DEAD,), forbids=(SEELAH_BACK,)),
        c("Continue", "gone", requires=(SEELAH_GONE,), forbids=(SEELAH_DEAD, SEELAH_BACK)),
        c("Continue", "living", forbids=(SEELAH_DEAD, SEELAH_GONE)),
        c("Continue", "living", requires=(SEELAH_BACK,))),
    jan("living", '''"The League. Seelah, Elan, Curl and me. We found a lost cart of beer in the ruins of Kenabres the week the world ended, and we thought that made us heroes." {n}She sets the tankard on the bunk.{/n}''',
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
    jan("q3", '''"Seelah smiled at me. In front of the citadel, in front of Elan, after everything. As if I hadn't failed her." {n}She turns the tankard a quarter-turn.{/n}
"I asked her how she could do that. She said she'd give me a piece of her mind once we were in private. She did, too. Then she bought me a drink."''',
        c("Continue", "elan", requires=(ELAN_DEAD,)),
        c("Continue", "elan_lives", forbids=(ELAN_DEAD,))),
    jan("elan", '''"Elan's dead." {n}She says it flatly, the way she says everything that matters.{/n}
"He saw the jeweller with the souls and went in after him alone. He told me to stay and watch the door and wait for you. So I did. I didn't desert my post, Commander. I kept it. And he died anyway, on the other side of it." {n}She looks at the four stick figures on the tankard.{/n} "Two of us left out of four. That's the League."''',
        c("Continue", "q3_end")),
    jan("elan_lives", '''"Elan's alive, and furious with me, which is how Elan says he's fond of you. Curl's gone, or whatever was wearing Curl is. Seelah is Seelah." {n}She turns the tankard so the cart faces you.{/n}
"Three out of four. For a League that started with a barrel of beer, that's a better record than mine."''',
        c("Continue", "q3_end")),
    jan("q3_end", '''"She's the reason I'm still standing, and I told her once, in a cage, that she was the reason I ran. I've taken it back since. I'm not sure it's the kind of thing you can take back." {n}She puts the tankard down.{/n}
"I don't want you telling her anything about us. I'll tell her. When there's something to tell."''',
        c('"Then it\'s yours to tell."', "end")),
    jan("cage_seen", '''"The last time I saw her was the Scar. She said she was sorry. She had nothing in the world to be sorry for, and I stood there and let her say it." {n}She turns the tankard a quarter-turn.{/n}
"She'd forgive me. That's the trouble with Seelah. She'd forgive me before I'd finished asking, and then I'd have to live with it."''',
        c("Continue", "decide")),
    jan("not_seen", '''"I haven't seen Seelah since Houndheart. I've seen her every night in my head, though, standing by the fire in the rain, shouting that motto of hers, looking round for me." {n}She turns the tankard a quarter-turn.{/n}
"I wasn't there. I'm never there, in that dream. I've been gone for a year."''',
        c("Continue", "decide")),
    jan("decide", '''"She's in Drezen. I could walk up those steps and cross the square and be in front of her before the bell." {n}She doesn't move.{/n}
"I'm not afraid of demons any more. I found that out on the wall. It turns out I'm a coward about exactly one thing, and it's a paladin who'd forgive me."''',
        c('"Go and see her. Today."', "go", flags=(SEELAH_HERSELF,)),
        c('"I\'ll tell her for you."', "for_her", flags=(SEELAH_FOR_HER,)),
        c('"Leave Seelah out of it for now."', "kept", flags=(SEELAH_KEPT,))),
    jan("go", '''"Today." {n}She stands up, puts the tankard in her belt, and goes, before she can think better of it.{/n}
{n}She's gone most of the afternoon. When she comes back down the gaol steps she has a red handprint on her left cheek and her eyes are swollen, and she's grinning like a fool.{/n}
"She hit me. Open hand. Then she held on so long the turnkey came to see if it was a fight. Then she bought me a drink, and made me tell her everything, and hit me again."''',
        c('"How was the drink?"', "go_end"),
        c('"Everything?"', "go_everything")),
    jan("go_end", '''"Terrible. The Defender's Heart is gone and Drezen can't brew." {n}She touches the handprint as if it were a medal.{/n}
"Best I've ever had."''',
        c("[Leave her with it.]")),
    jan("go_everything", '''"Everything about the cage, the ash, Houndheart, the salt road." {n}She touches the handprint.{/n}
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
"The last thing I ever said about her, out loud, was that she was the reason I ran."''',
        c('"She\'d have forgiven you."', "mourn_forgive"),
        c("[Sit with her, and say nothing.]", "mourn_quiet")),
    jan("mourn_forgive", '''"I know. That's the worst part. She'd have forgiven me before I'd finished asking." {n}She presses the heels of her hands into her eyes, hard, and takes them away.{/n}
"No glory without risk. She used to shout it at the tavern ceiling. I'm going to shout it at a demon one of these days, and mean it, and then I'll have paid for something."''',
        c("[Leave her with it.]")),
    jan("mourn_quiet", '''{n}You sit on the bunk beside her. After a while she leans, very slightly, until her shoulder is against yours, and stays there while the lamp gutters.{/n}
"Thank you," she says eventually. "For not saying she'd have forgiven me. Everybody says that."''',
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
"I can write him the truth: I ran, I was caged, I lost my first bout, I'm in a cell in Drezen by choice. Or I can write him a hero. He'd believe the hero. He'd tell the whole street. He'd die happy." {n}She looks at you.{/n} "What would you do?"''',
        c('"Write him the truth. He asked about his daughter, not about a legend."', "truth"),
        c('"Let him keep the daughter he believes in. The truth is yours; the legend is his."', "legend"),
        c('"It\'s your letter, and your father. I won\'t choose it for you."', "yours")),
    jan("truth", '''"The truth." {n}She takes a sheet of paper from under the bunk and a pencil stub from her boot.{/n}
"He'll hate it. He'll write back and tell me fate had a plan, and I'll write back and tell him fate can go and drown in the river. We'll argue about it for years." {n}She starts writing.{/n} "That's how you know you're still somebody's daughter."''',
        c("[Leave her to her letter.]", flags=(MIVON_TRUTH,))),
    jan("legend", '''"The legend." {n}She considers it a long time.{/n}
"All right. He's old. He buried my mother on the strength of a story about how she'd died, and he was happier for it. I'll give him one about me." {n}She takes out paper and a pencil stub.{/n} "I'll never tell anyone else it. Just him."''',
        c("[Leave her to her letter.]", flags=(MIVON_LEGEND,))),
    jan("yours", '''"Coward." {n}But she's almost smiling.{/n} "No. You're right. It's mine."
{n}She is quiet a while, turning the pencil in her fingers the way she turns a blade.{/n} "The truth. If I'm going to stop running, I might as well stop in front of him too. He'll hate it. We'll argue about it for years. That's how you know you're still somebody's daughter."''',
        c("[Leave her to her letter.]", flags=(MIVON_TRUTH,))),
], requires=(FORMS,), delay=48)


# The blade: her Aldori sword, her record, and one notch cut the wrong way.
meet(BLADE, "Forty-one", '"That isn\'t a practice sword."', [
    nar("open", '''{n}She has the long Aldori blade across her knees, and she's working the old leather off the grip with the point of a knife. Underneath, the wood is dark and smooth with years of her hand.{/n}''',
        c("Continue", "ash", requires=(SCAR,)),
        c("Continue", "stores", forbids=(SCAR,))),
    jan("ash", '''"The one you passed me through the bars." {n}She doesn't look up.{/n} "I lay on it in the ash for an hour, and carried it through the Wound, and guarded salt with it all winter, and it never once asked me what I thought I was doing."''',
        c("Continue", "master")),
    jan("stores", '''"Mine. The turnkey found it in the gaol stores under a sack of turnips, which is where they put the weapons of people they don't expect to see again." {n}She doesn't look up.{/n}
"The vrocks threw it outside my cage in the Scar. Somebody carried it all the way back to Drezen and then put it under a sack of turnips. I don't know whether to thank them or challenge them."''',
        c("Continue", "master")),
    jan("master", '''"My master gave it to me the day I left Mivon. He'd never said a kind word to me in seven years. He put this in my hands at the river stairs and said, 'Don't come back with it dirty.'" {n}Her mouth quirks.{/n}
"I think that was the kind word."''',
        c("Continue", "scabbard")),
    jan("scabbard", '''{n}She turns the scabbard over and shows you the inside of its throat, where the leather is cut with tiny, neat notches.{/n}
"Forty-one. One for every bout I fought in earnest. Tournaments, quarrels, the bandits on the river roads. I stopped counting at forty-one because counting started to feel like bragging, and my master said bragging is a feint you use on yourself."''',
        c("Continue", "wrong_way", requires=(SCAR,)),
        c("Continue", "wrong_way", requires=(CAUGHT,)),
        c("Continue", "wrong_way", requires=(LIED,)),
        c("Continue", "right_way", forbids=(SCAR, CAUGHT, LIED))),
    jan("wrong_way", '''{n}She puts her thumb on one more notch, newer than the others, and cut the other way, across the grain.{/n}
"And that one. For you." {n}She says it lightly. It isn't light.{/n}
"The first one I lost. I cut it the wrong way so I'd never mistake it for the others."''',
        c('[Flirt] "I\'m honoured to be the exception."', "flirt"),
        c('"Will you ever cut another?"', "another")),
    jan("right_way", '''{n}She puts her thumb on one more notch, newer than the others, cut the right way.{/n}
"Forty-two. The cell. You." {n}She says it lightly.{/n} "I wasn't sure it counted, a bout of stories. I decided it did. I'm the one who keeps the scabbard."''',
        c('[Flirt] "Keep the scabbard. I\'ll keep trying."', "flirt"),
        c('"Will you ever cut another?"', "another")),
    jan("flirt", '''"You would." {n}She looks at you properly, from the scabbard up, not quickly.{/n}
"Here." {n}She puts the blade in your hands, hilt first, and folds your fingers round the bare wood where the old leather used to be.{/n} "Feel that? That's seven years of my hand. Nobody else has held it since Mivon."''',
        c("[Hold it.]", "held", flags=(BLADE_HELD,))),
    jan("another", '''"One more, maybe." {n}She runs her thumb along the notches, one by one, like a rosary.{/n}
"There's a bout I want. I haven't decided when. When I do, you'll know, because everybody will know." {n}She puts the blade in your hands, hilt first.{/n} "Here. Feel the balance. It's the last thing my master ever got right."''',
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
"In Kenabres. With the cart. 'I signed up four days before the demon attack!' And then that thing I used to say after it. You remember." {n}She does her own voice from a year ago, loud and bright, and it's a good imitation, and it's horrible.{/n}
"I used to think that was funny. Four days. I thought it meant I was meant to be there."''',
        c('"It was funny. You made the whole table laugh."', "funny"),
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
"He said Irabeth would sign it if I asked. He said he'd already asked her for me."''',
        c('"Will you take it?"', "take"),
        c('"You earned it on the wall."', "earned")),
    jan("earned", '''"On the wall I earned not running. That's all I earned." {n}She looks at the tabard.{/n}
"A tabard is a promise. I made that promise once, four days before the demons came, and I broke it in the rain at Houndheart. I don't know if I get to make it twice."''',
        c("Continue", "take")),
    jan("take", '''"I want it." {n}She says it as if confessing to a theft.{/n}
"I want it more than I've wanted anything since Mivon. That's the problem. The last time I wanted something that much, I ran from it the first time it bit me."''',
        c('"Then put it on, and don\'t run."', "on", flags=(WATCH_STOOD,)),
        c('"Then leave it folded until you know."', "folded"),
        c('"You don\'t need their blue. You fight for me."', "mine")),
    jan("on", '''{n}She looks at you for the length of a slow breath. Then she picks up the tabard, shakes it out, and pulls it over her head, and stands there in the last cell of the gaol in Eagle Watch blue.{/n}
"It's too big. It was always too big." {n}Her voice isn't steady.{/n} "Don't look at me like that. I'll take it off before the muster. Tonight I just want to know what it feels like when you haven't broken it yet."''',
        c("[Leave her in the blue.]")),
    jan("folded", '''"Until I know." {n}She nods, and puts the tabard on the shelf above the bunk, folded, badge out.{/n}
"It'll be there. That's the good thing about a tabard; it waits. It's more patient than I am."''',
        c("[Leave her with it.]")),
    jan("mine", '''"For you." {n}She tilts her head.{/n}
"That's a dangerous thing to say to an Aldori. In Mivon, a fencer who fights for one person and not a city is called a sellsword, or a lover, and they're both a bit of a scandal." {n}She puts the tabard on the shelf, folded.{/n} "I'll think about which one you meant."''',
        c("[Leave her with it.]")),
], requires=(WALLS,), forbids=(COMMITTED,), delay=24)
