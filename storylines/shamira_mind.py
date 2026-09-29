"""Shamira behind the Commander's eyes: the nights before the body, the theft of the shell, and the waking
(shamira_trickster holds the device and the hooks).

Every beat engages her canon: the dream-sower who fell because "A dream is a bird, not a horse" (Shamira_dialogue/
Cue_0076 4439415b), Nocticula who "came for me and shrouded me in her shadows" (Cue_0077 06b5cce2), the throne-light that
"blinds, withers, makes a person burn with fever" (Cue_0100 fb749b1a), the mind she strips "as efficiently and ruthlessly
as a hunter dressing a carcass" (Cue_0106 43bb7ca8), her contempt for Arueshalae's new friends (Cue_0188 fbf3ccca), and
the Fleshmarkets where she courted Hepzamirah (Cue_0080 76485a33).

Delivery: rest-delivered pages. While she lives in the Commander's head she speaks as she always has, inside the mind
(Cue_0157 817101b5), so those pages are sendings; the theft is the Commander's own night out through Socothbenoth's
closets (with her behind the Commander's eyes, a sending; alone, before the kill, an event); the waking ends with her in
the room, a visit. The pivotal choice is the fuel: the Commander's dreams, or the Commander's and a barracks' (her evil
demand, a Ledger secret), or none, and then she stays locked in the back of the Commander's head or is thrown out of it.
The cost the waking sets is the Commander's: the body lives on the Commander's dreams, and she must walk into them every
night, so the Commander never dreams alone again.
"""
from story_format import c
from storylines import household
from storylines.shamira_trickster import (BARRACKS, CAST_OUT, CLOSED, CRYSTALS, DREAM2, EMBODIED, FOUND, FUEL,
                                           HANDED, KEPT, KILLED, MASSACRE, NEVER_ALONE, NIGHT1,
                                           NOCT_KNOWS, P, PRIMED, RAMISA_FOOLED, RAMISA_STORY, READ_ALL, REFUSED_BARRACKS, RETURNED, SECRET, SHELL,
                                           SOCOTH_GONE, STEALTH1, TASTED, TORN, VEIL, WHISPER, nar, sh)
from storylines.shamira_trickster import page as _page

SCENES = []


def page(*args, **kw):
    _page(*args, into=SCENES, **kw)


SAW_ARUESHALAE = "shamira.saw_arueshalae"   # SeenCue Shamira_dialogue/Cue_0188: she mocked Arueshalae in her throne room
SEEN_CUES = {SAW_ARUESHALAE: ["fbf3cccaa03787d49a882efa0cfe5c5b"]}
WANT_STEWARD = P + "want.steward"
WANT_HER = P + "want.her"
WANT_NOTHING = P + "want.nothing"
CHOSE_ALONE = P + "shell_chosen_alone"
BURNED = P + "dream_burned"
KEPT_DREAM = P + "dream_kept"
LAST_HOME = P + "last_dream.home"
LAST_PEACE = P + "last_dream.peace"
LAST_HER = P + "last_dream.her"
SPY_HANGED = P + "spy.hanged"
SPY_TURNED = P + "spy.turned"
SPY_FED = P + "spy.fed"

LIVE = (CLOSED, KEPT, CAST_OUT)

household.secret("shamira_barracks", "A barracks that stopped dreaming",
                 "I let Shamira walk the sleep of a Mendevian barracks by the north gate, to give her back some of her fire. "
                 "The men woke dull. Some of them are not all right. Nobody knows why, except her, and me.",
                 portrait="Shamira", witnesses=("seelah", "irabeth", "targona"), risk="high")


# --- The first night: what she is without her fire ------------------------------------------------------------------

page(P + "mind.first_night", "The first night", [
    nar("start", '''{n}You sit at the camp table, among the maps and the dirty cups, and for a while the second heartbeat behind your eyes only keeps time with yours. Outside, the sentries change. Somebody laughs too loudly by the cookfires and is told to shut up.{/n}
{n}Then the air in the tent goes warm and close, the way it does before a storm.{/n}''',
        c("Continue", "look")),
    sh("look", WHISPER + '''"Look at this." {n}You feel her looking: through your eyes, around the tent, with a disgust so intimate it itches.{/n} "A tent. A cot. Maps with wine on them. All my long existence, and I am spending my first night of death behind the eyes of a clown, in a tent that smells of feet."
"In my Harem there are forty rooms. I have never once slept in the same one twice. Do you know why?"''',
        c('"Because you don\'t sleep."', "sleep", forbids=(READ_ALL,)),
        c('"Because someone might be waiting."', "sleep", forbids=(READ_ALL,)),
        c("Continue", "drowned", requires=(READ_ALL,))),
    sh("drowned", '''"Don't answer. I know what you'd say. I know everything you'd say." {n}The voice is flat and tired and very sure.{/n} "I went through every room in your head while I was drowning. Every drawer. I know who you were before the war and what you did to stop being it. I know which of your friends you'd sell, and for how much, and which you wouldn't sell for the Worldwound closed and a crown." {n}A pause.{/n} "I know what you haven't told a single living soul. Don't worry. Neither will I. It's the most valuable thing I own."''',
        c("Continue", "sleep")),
    sh("sleep", '''"Because there is always someone in my court who wants my chair, and a demon who can be found can be killed." {n}A small, bitter pause.{/n} "It turns out I should have worried about the clowns."
"You haven't asked me how it feels. They all ask, the ones who kill people. How does it feel. They want to know if it hurt." {n}The heat behind your eyes gathers itself.{/n} "Ask me something better."''',
        c('"What are you, now, without the fire?"', "without"),
        c('"What do you want?"', "want")),
    sh("without", '''"Less." {n}She says it flatly, the way a surgeon names what he has cut off.{/n} "The fire was the part of Heaven I stole when I left. It was what made my light wither the fools who looked at me too long. It kept me warm in the Abyss every day since I fell." {n}Silence.{/n} "Now I am only a demon, and I have never in my existence been only anything. I can still get into your head. That, they can't pull out of me with a cauldron. But I am cold, Golarian. I am so cold."''',
        c("Continue", "want")),
    sh("want", '''"A body, since you asked. And after that, everything I had, and after that, everything I didn't." {n}A glimmer of the old, vast arrogance.{/n} "But you have not told me what you want. And you do want something. Nobody murders a woman on an errand and then keeps her behind their eyes for company. Tell me what you kept me for, and choose your words."''',
        c('"A steward for Alushinyrra who owes me her life."', "steward", flags=(WANT_STEWARD,)),
        c('"You. You got into my head once, in your Harem. I\'ve been waiting for you to come back."', "you", flags=(WANT_HER,)),
        c('"Nothing. I told you: I don\'t like waste."', "nothing", flags=(WANT_NOTHING,))),
    sh("steward", '''"Owes you." {n}She rolls it round, and something like respect comes into her voice at last, the respect one merchant has for another's cheek.{/n} "You think I will sit on a dead woman's cushion in Alushinyrra and send you the city's secrets in thanks. That is almost a Nocticula thought. She used to have them about me." {n}The warmth flickers.{/n} "I will owe you, Golarian. I will hate every hour of it. You may find that more useful than gratitude."''',
        c("Continue", "noct", requires=(NOCT_KNOWS,)),
        c("Continue", "sleep_now", forbids=(NOCT_KNOWS,))),
    sh("you", '''"You..." {n}For a heartbeat she has nothing to say, and you feel her feel it, a small blank like a missed stair.{/n}
"You don't mean it the way they mean it in my court. I would taste it if you did. You mean it the way a child means it when it points at a fire." {n}Her voice drops, warm and wary together.{/n} "Children who point at fires get burned, Golarian. I am going to enjoy watching you learn that."''',
        c("Continue", "noct", requires=(NOCT_KNOWS,)),
        c("Continue", "sleep_now", forbids=(NOCT_KNOWS,))),
    sh("nothing", '''"Liar." {n}But she is laughing, a thin cold laugh with nothing to breathe it.{/n} "No. Not a liar. That's worse. You truly believe it. You killed me and kept me the way a miser keeps string: in case." {n}The laugh stops.{/n} "Very well. I am your string. Mind I don't end up round your throat."''',
        c("Continue", "noct", requires=(NOCT_KNOWS,)),
        c("Continue", "sleep_now", forbids=(NOCT_KNOWS,))),
    sh("noct", '''"She knew, you know." {n}The voice has gone thin again.{/n} "My lady. She knew I wanted her chair; I think she has always known. She let me want it for years the way you let a cat want the canary: because it is pretty to watch." {n}A long silence.{/n}
"And when you brought me to her behind your eyes she said hello, and she thanked you. That is all I was, at the end. A thing to thank someone for." {n}The heat behind your eyes flares, very suddenly, and then cools.{/n} "I will make her regret that. Not today. I have no hands today."''',
        c("Continue", "sleep_now")),
    sh("sleep_now", '''"Sleep now. You look terrible." {n}The warmth softens into something almost lazy.{/n} "And when you sleep, I'm coming in. Don't bother to argue. Your head is the only warm room for a thousand miles, and I have been cold for an entire day."''',
        c("Continue", "in_again", requires=(TASTED,)),
        c("Continue", "in", forbids=(TASTED,))),
    nar("in_again", '''{n}You dream of Kenabres. She is sitting on the lip of the dry fountain again, exactly where she sat in the Harem's dream, a lifetime ago, when she was alive and it was a game.{/n}
{n}This time the ash falls on her. This time she shivers. She does not look at the dragon. She holds her hands out to the burning city the way a traveller holds them out to a hearth.{/n}''',
        c("[Sit down beside her.]", flags=(NIGHT1,))),
    nar("in", '''{n}You dream of Kenabres. You always dream of Kenabres. And tonight there is a red-haired woman on the lip of the dry fountain in the square, where nobody has ever sat before.{/n}
{n}She does not look at the falling dragon. She holds her hands out to your burning city the way a traveller holds them out to a hearth, and when the ash falls on her, she shivers.{/n}''',
        c("[Sit down beside her.]", flags=(NIGHT1,))),
], requires=("trickster.ever", RETURNED, FOUND), forbids=(NIGHT1, EMBODIED) + LIVE, delay=12)


# --- The Council, heard through glass (the primed road: she was on the belt at Council 5-2) -------------------------------

COUNCIL_HEARD = P + "council_heard"

page(P + "mind.council", "Through your eyes", [
    nar("start", '''{n}You go straight from Socothbenoth's closet to his Council, with the cauldron in your hands and her behind your eyes, and you sit through all of it: the speeches, the votes, the essences passed round the long table like a loving cup. You keep your thoughts on carpets. She does not need your thoughts to listen.{/n}
{n}That night the second heartbeat is loud long before you lie down.{/n}''',
        c("Continue", "heard")),
    sh("heard", WHISPER + '''"So that is his Council." {n}Contempt, and under the contempt, something like awe she would never admit.{/n} "I always wondered where he went when he vanished into wardrobes. I pictured something grand. It is a room full of has-beens voting on a joke." {n}A pause.{/n} "Your diamond is full of them now. I could feel them in it, the whole time, next to my fire. Axis and Elysium and Hell and my lady's Abyss, all in one stone, and my Nirvana in the middle, like the stone in a peach."''',
        c("Continue", "shyka")),
    sh("shyka", '''"And that thing. The one that is many people." {n}Her voice drops, as if Shyka might hear her across the planes.{/n} "It looked at me. Through your eyes, from the outside in. Nobody has looked at me like that since my masters in Heaven: as if it had already read the end of me and thought it was rather sweet." {n}The warmth in the crystal shrinks.{/n} "I did not like it. I do not want to talk about it."''',
        c('"It seemed to like you."', "liked"),
        c("[Leave it.]", "socoth")),
    sh("liked", '''"It seemed to like everything. That is what frightens me about it." {n}Curtly.{/n} "Stop thinking about it. I can see it in your head, all its faces at once, and it is looking at me again."''',
        c("Continue", "socoth")),
    sh("socoth", '''"And him. He was so pleased with himself. My fire in his cauldron, and me on your belt, and he kept winking at your forehead across the table as if we were all three in on something." {n}Venom, very pure.{/n} "He has no idea what he has done. He thinks he played a joke on his sister. He played a joke on me. I do not laugh at jokes, Golarian. I remember them."''',
        c("[Put out the lamp.]", flags=(COUNCIL_HEARD,))),
], requires=("trickster.ever", RETURNED, FOUND, PRIMED, HANDED), forbids=(COUNCIL_HEARD, NIGHT1) + LIVE, delay=4)


# --- Her lady's words (what Nocticula said, before or after) -------------------------------------------------------------

ASKED_LADY = P + "asked_lady"
PERMITTED = "noct.acq.shamira_permission"   # Nocticula/Answer_0010: "I'm here to kill Shamira." (read in node text only)
REPORTED = "noct.acq.shamira_reported"      # Nocticula/Answer_0020: "I killed Shamira." (read in node text only)
LADY_ENJOYED = P + "asked_lady.enjoyed"

page(P + "mind.her_lady", "What her lady said", [
    nar("start", '''{n}She is quiet for most of the evening. You have learned what her quiet sounds like: not absence, but a held breath, the second heartbeat slow and still behind your own.{/n}
{n}When she speaks, she does not bother with preamble.{/n}''',
        c("Continue", "ask")),
    sh("ask", WHISPER + '''"Tell me what she said. My lady. Before you killed me, or after. You went into her audience chamber at some point that night; I can see the room in you." {n}A pause.{/n} "Don't pretty it. I would know. I'd rather have the ugly thing than watch you polish it."''',
        c("Continue", "permitted", requires=(PERMITTED,)),
        c("Continue", "reported", requires=(REPORTED,), forbids=(PERMITTED,)),
        c("Continue", "silent", forbids=(PERMITTED, REPORTED))),
    sh("permitted", '''{n}She finds it before you can decide whether to say it. You feel her find it.{/n}
"You told her. Before. You walked into her chamber and told her you had come to kill me, and she said..." {n}Her voice goes very flat, reciting.{/n} "'I'll let you kill her. Or at least, I'll let you try. She covets my throne.'"
{n}Silence, for so long that the lamp gutters.{/n} "She gave you leave. Before. She knew where I was, three doors away, and she gave a mortal leave, and went back to her cushions."''',
        c("Continue", "crystals", requires=(CRYSTALS,)),
        c("Continue", "throne", forbids=(CRYSTALS,))),
    sh("reported", '''{n}She finds it before you can decide whether to say it.{/n}
"After. You told her after, and she thanked you. 'She coveted my throne. You've saved me the trouble of having to deal with her.'" {n}Her voice is very flat.{/n} "Trouble. All those years at her right hand, and I was trouble, and you saved her from it, and she let you walk out of her palace with my body still warm on her floor."''',
        c("Continue", "crystals", requires=(CRYSTALS,)),
        c("Continue", "throne", forbids=(CRYSTALS,))),
    sh("silent", '''{n}She looks for it. She does not find it.{/n}
"Nothing. You didn't speak to her of me at all, before or after." {n}Her voice is odd.{/n} "And she didn't ask. Her steward of all those years dies in her own bedchamber, and the thing she says to the killer's back is nothing. Not even a question."
{n}The heat behind your eyes goes out, nearly, and comes back.{/n} "I think I would rather she had thanked you."''',
        c("Continue", "crystals", requires=(CRYSTALS,)),
        c("Continue", "throne", forbids=(CRYSTALS,))),
    sh("crystals", '''"And the crystals." {n}Bitterly amused.{/n} "You gave me the secret of the crystals, in my Harem. I used it. It made me strong enough to nearly kill your friends in the boudoir. I remember the half-elf screaming." {n}A breath.{/n} "It did not make me strong enough to live. Nothing a mortal gives a demon ever does. Remember that, Golarian. You will be giving me things."''',
        c("Continue", "throne")),
    sh("throne", '''"I wanted her chair. You know that; you caught me at it. I wanted it the way you want water. But I loved her, too, in the way we do down here, with our teeth." {n}Her voice has gone very quiet, and very cold.{/n} "Now I only want the chair."
"Tell me one thing, and then I will stop talking about her for tonight. When you did it, the killing. Did you enjoy it?"''',
        c('"No."', "no", flags=(ASKED_LADY,)),
        c('"Yes."', "yes", flags=(ASKED_LADY, LADY_ENJOYED)),
        c('"I didn\'t think about it. I thought about carpets."', "carpets", flags=(ASKED_LADY,))),
    sh("no", '''"No." {n}She tastes it for the lie, and does not find one.{/n} "No. You did it the way you'd pull a tooth: because it had to come out, and because you'd already planned what to put in the hole." {n}A slow breath.{/n} "I have been killed by a planner. That is almost worse than a murderer. At least a murderer wants you."''',
        c("[Put out the lamp.]")),
    sh("yes", '''{n}She laughs, a real laugh, short and startled.{/n} "Yes. You did. I felt it, at the end, under the carpets: a little bright thing, like a boy stealing a pie." {n}Something warmer than it should be.{/n} "Good. I would have hated to be killed by somebody who did not enjoy it. It would have been such a waste of me."''',
        c("[Put out the lamp.]")),
    sh("carpets", '''"Carpets." {n}A long silence.{/n} "You know, in all my long life, I have been hated, feared, worshipped, desired and once, briefly, pitied. I have never before been beneath someone's notice while they killed me." {n}The crystal warms under your hand.{/n} "I will have your notice, Golarian. All of it. I'm going to take it off you piece by piece."''',
        c("[Put out the lamp.]")),
], requires=("trickster.ever", RETURNED, NIGHT1), forbids=(ASKED_LADY, EMBODIED) + LIVE, delay=36)


# --- The theft of the shell: through Socothbenoth's closets to Ramisa's hothouse -----------------------------------------

def heist(with_her):
    """The theft. With her behind the Commander's eyes she guides (and chooses); alone (before the kill, on Socothbenoth's
    veil) the Commander chooses. Every road ends with a shell hanging in the Commander's wardrobe.

    Canon: Ramisa Sloughed Skin, "a true artist of the slave trade" who takes "a custom order" (HologramSlaver/Cue_0003
    dad3c081), trades only as a projection because "the allies, lovers, and masters of those I turned into fertilizer are
    still searching for me", and grows mandragoras by watering a weed with demon blood "or if you plant it in a demon's
    corpse" (Cue_0012 fe57b714, Cue_0013 11789a3f); her mandragora shrieks (Cue_0001 91c7dcb9); she thanks a Commander who
    put the Fleshmarkets to the sword for two-thirds of the market (Cue_0002 c4eae284). Socothbenoth's closet goes from his
    city to his Council (SocotAlush/Cue_0023 79a1910c). Authored: her hothouse, where the unclaimed custom orders grow."""
    def her(id, text, *choices):
        return sh(id, text, *choices) if with_her else nar(id, text, *choices)

    start = nar("start", ('''{n}She tells you the way herself, in the small hours, as if she were giving directions to a tailor.{/n} ''' + WHISPER +
            '''"Your wardrobe. His Council. His house. The Fleshmarkets. I have seen him use those doors a hundred times; I read them out of his head one night he came sniffing at my lady's bedchamber. He dragged a closet round my city for years and thought nobody noticed."''') if with_her else
            '''{n}Socothbenoth's veil is still on you. You can feel it when you move: a coolness at the edge of things, like walking in the shade of a building that is not there. The cauldron is not full yet. The boudoir is still ahead of you. But a body takes stealing, and stealing takes a night, and you have a night.{/n}''',
        c("Continue", "wardrobe"))
    wardrobe = nar("wardrobe", '''{n}You step into the wardrobe in your quarters in Drezen, between a coat and a spare cloak, and close the door on yourself, and open it again onto the Council chamber: the long table, the empty chairs, the smell of old wine and older schemes. Nobody is there. The candles are burning anyway.{/n}
{n}Behind the chair where Socothbenoth sits there is the other door, the one he came through from Alushinyrra with his closet on his back: lacquered in purple, with a handle shaped like a lady's hand. You take the hand. It squeezes back.{/n}''',
        c("Continue", "house_gone", requires=(SOCOTH_GONE,)),
        c("Continue", "house", forbids=(SOCOTH_GONE,)))
    house = nar("house", '''{n}Socothbenoth's house in Alushinyrra is all wardrobes. They stand in every room, in rows, like soldiers, and every one of them is full of silk, and every one of them has a keyhole at exactly the height of a curious eye. Something in one of them sighs as you pass. You do not stop to find out what.{/n}
{n}Out through a side door, and the city takes you: hot purple night, a sky with no stars, the smell of incense and blood and sugar.{/n}''',
        c("Continue", "market"))
    house_gone = nar("house_gone", '''{n}Socothbenoth's house in Alushinyrra is all wardrobes, and all of them are shut. Dust sheets over the chairs. A bowl of fruit gone to black liquor on a sideboard. Wherever the Silken Sin is tonight, and whoever he is a guest of, he has not been home, and his closets have gone on opening without him.{/n}
{n}Out through a side door, and the city takes you: hot purple night, a sky with no stars, the smell of incense and blood and sugar.{/n}''',
        c("Continue", "market"))
    market = nar("market", '''{n}The Fleshmarkets never close. At this hour the auction blocks are empty and the pens are full, and the traders sit on their stools drinking something that steams and counting coin by the light of the cages. A dretch is being sold for scrap. A pair of succubi argue over the price of a man's voice, which is apparently something you can buy here separately.{/n}''',
        c("Continue", "remembered", requires=(MASSACRE,)),
        c("Continue", "street", forbids=(MASSACRE,)))
    remembered = nar("remembered", '''{n}The market has been rebuilt since you last came through it with your sword out. The new stalls are cleaner, the new guards more numerous, and on the post by the gate somebody has nailed a crude drawing of your face with an obscene suggestion scratched underneath. It is not a bad likeness.{/n}
{n}Half the new stalls fly the same small banner: a green shoot, sprouting from a skull. The marilith who thanked you for the massacre has been busy.{/n}''',
        c("Continue", "street"))
    street = her("street", ('''"Ramisa's." {n}Her voice is brisk now, almost cheerful: a woman back in her own city, even if it is only through your eyes.{/n} "Sloughed Skin. The marilith who sells you a projection and delivers afterwards. Everyone thinks her goods are kept somewhere far away. They're kept under the bone-carvers' stalls, in a hothouse, growing. I know, because she grew two bodies for my court when they got bored of their faces." {n}A pause.{/n} "She was a gardener, once. She still is."''') if with_her else
            '''{n}Socothbenoth's directions bring you to the back of the market, where the bone-carvers work, and to a trapdoor under the last stall that smells of wet earth and something sweet gone bad. "Ramisa's hothouse," he said. "She sells you a projection and grows the goods to order, darling, in the dark, the way she used to grow her little screaming plants. I buy my silks next door."{/n}''',
        c("[Stealth: slip in under Socothbenoth's veil.]", requires=(VEIL,),
          check=dict(Skill="SkillStealth", DC=22, Success="inside", Failure="woken", CommanderOnly=True)),
        c("[Stealth: slip into shadow, the way the Trickster does.]", requires=(STEALTH1,), forbids=(VEIL,),
          check=dict(Skill="SkillStealth", DC=26, Success="inside", Failure="woken", CommanderOnly=True)),
        c("[Stealth: go in quietly.]", forbids=(VEIL, STEALTH1),
          check=dict(Skill="SkillStealth", DC=32, Success="inside", Failure="woken", CommanderOnly=True)))
    inside = nar("inside", '''{n}The hothouse is long and low and lit green. Down both walls, in beds of black earth, the orders grow: bodies, half-buried, their roots going down into the soil and into whatever is rotting under it. Men, women, things that are neither. Some are only a pale shape in the dirt. Some are finished, sitting up to the waist in the earth, eyes shut, chests still. None of them has ever been anybody. They were planted in something dead, and watered, and they grew.{/n}
{n}Along the aisle, in pots, stand Ramisa's mandragoras, wrinkled and asleep. You do not step near them.{/n}''',
        c("Continue", "choose"))
    choose = her("choose", ('''"Not that one. Not that one; look at the knees. That one was pulled early." {n}She is shopping, you realise, with the unhurried contempt of a woman who has shopped here before, and despite everything she is enjoying it.{/n}
"There. The tall one, at the end, with the long hands. Somebody ordered her and never paid; you can tell by the weeds. The skin is good. The bones are better. It will do, until I can afford something worthy of me."''') if with_her else
            '''{n}You walk the beds like a buyer. You do not know what she would want. You know only what she was: tall, on her throne, burning, her hand long and white against the red of her hair when she waved you away.{/n}
{n}At the end of the row, up to her hips in the black earth, sits a tall woman with long hands, faceless as a dressmaker's dummy, the weeds grown high round her as if nobody has come for her in a long time. You choose her.{/n}''',
        c("[Thievery: cut her roots without waking the house.]",
          check=dict(Skill="SkillThievery", DC=24 if with_her else 30, Success="clean", Failure="shriek", CommanderOnly=True),
          flags=() if with_her else (CHOSE_ALONE,)))
    shriek = nar("shriek", '''{n}The root is warded. Of course it is. It parts under your knife and, as it parts, every mandragora in the aisle wakes and screams: a thin, high, furious sound like a kettle left on in hell.{/n}''',
        c("Continue", "woken"))
    woken = nar("woken", '''{n}Between one scream and the next the aisle is full of marilith: a translucent, towering shape, six arms and a long coiled tail, lit from inside like a lantern, with a shriveled mandragora clutched to her breast. She is not here. She never is. It makes her no less frightening.{/n}
"A thief," {n}says Ramisa Sloughed Skin, delighted.{/n} "In my garden. Among my orders. At this hour."''',
        c("Continue", "recognised", requires=(MASSACRE,)),
        c("Continue", "caught", forbids=(MASSACRE,)))
    recognised = nar("recognised", '''{n}The projection leans down to look at your face, and her smile widens.{/n} "Oh. Oh, it's you. My {mf|benefactor|benefactress}. You cleared the worms out of my market with your sword and made me mistress of two-thirds of it, and now you come back at night to rob me." {n}She sounds moved.{/n} "That's not theft. That's a story."''',
        c("Continue", "caught"))
    caught = her("caught", ('''"You can't kill her. She isn't here." {n}Her voice in your head is perfectly calm.{/n} "Lie to her. She is vain and she trades with Socothbenoth; his name will open her like a clam. Or pay her in the only coin she likes: tell her what the body is for. She collects stories. Or run, and tear the body on the way out, and I will wear the tear for the rest of my life. Choose, Golarian. She's working up to calling her hunters."''') if with_her else
            '''{n}She is working up to calling her hunters. You can see it in the way the mandragora in her arms has stopped screaming and started to smile.{/n}''',
        c("[Tell her the truth about what the body is for.]", "story"),
        c('[Bluff] "Easy. Socothbenoth sent me. He likes them fresh, and he doesn\'t like waiting."',
          check=dict(Skill="CheckBluff", DC=26, Success="fooled", Failure="run")),
        c("[Tear the body out of the earth and run.]", "run"))
    story = nar("story", ('''{n}You tell her. A dead woman behind your eyes, a demon lord's errand, a body for the rest of her. The projection listens with all six hands pressed together under her chin, and the mandragora listens too.{/n}
"A shell for a ghost, stolen from my garden by the one who made her a ghost." {n}Ramisa sighs, the way a patron of the arts sighs at a good play.{/n} "Take her. The body is paid for. The story is mine now, and I shall tell it at every sale for a hundred years. With names."''') if with_her else
            '''{n}You tell her. A woman you have not yet killed, a demon lord's errand, a body for what will be left of her. The projection listens with all six hands pressed together under her chin.{/n}
"You've come shopping for a corpse that isn't dead yet." {n}Ramisa sighs, the way a patron of the arts sighs at a good play.{/n} "Take her. The body is paid for. The story is mine now, and I shall tell it at every sale for a hundred years. With names."''',
        c("[Lift the shell out of the earth.]", "home", flags=(SHELL, RAMISA_STORY)))
    fooled = nar("fooled", '''{n}At the Silken Sin's name the projection's whole towering length relaxes, coil by coil.{/n} "Ohhh. Him. At this hour, always at this hour." {n}Two of her six hands wave, and the mandragoras fall silent, and the tall woman comes up out of the earth on her own, roots and all, and folds into your arms like washing.{/n} "Tell him it's on account. Tell him I want the last one back; he never returns them."''' + (
        ''' ''' + WHISPER + '''"I could kiss you. I will not, because you don't have a body worth it yet. But I could."''' if with_her else ""),
        c("[Carry her out.]", "home", flags=(SHELL, RAMISA_FOOLED)))
    run = nar("run", '''{n}You tear the body out of the earth. The roots do not want to let go; the last of them rips through the white skin at the collarbone with a sound like wet canvas, and then you are up through the trapdoor with a naked woman's weight over your shoulder, and the mandragoras' scream and Ramisa's laughter coming up behind you like smoke.{/n}
{n}The Fleshmarkets see a Golarian running with a body. The Fleshmarkets see that every night. Nobody stops you.{/n}''' + (
        ''' ''' + WHISPER + '''"My collarbone. You tore my collarbone. I haven't even got it yet and you've torn it."''' if with_her else ""),
        c("Continue", "home", flags=(SHELL, TORN)))
    clean = nar("clean", '''{n}The root parts with a sigh, not a scream. You lift the body out of the black earth, and it is heavier than you expected, and colder, and it hangs over your shoulder as limp as wet washing. Along the aisle the mandragoras sleep on.{/n}''' + (
        ''' ''' + WHISPER + '''"Gently. Gently! That's my hip you're holding."''' if with_her else ""),
        c("Continue", "home", flags=(SHELL,)))
    home = nar("home", '''{n}Back up through the trapdoor. Back through Socothbenoth's side door, past the rows of listening wardrobes. Through the purple door behind his chair, through the empty Council with its candles burning for nobody, and out of your own wardrobe in Drezen, into your own quarters, a little before morning.{/n}
{n}You hang her in the wardrobe, between your good coat and your spare cloak, and close the door on her. She looks, in there, like the best thing you own.{/n}''' + (
        ''' ''' + WHISPER + '''"Between your coats." {n}A long pause.{/n} "Socothbenoth would weep with joy."''' if with_her else
        '''
{n}There is nobody in her yet. There is nobody anywhere, yet. You still have a woman to kill.{/n}'''),
        c("[Close the wardrobe.]"))
    return [start, wardrobe, house, house_gone, market, remembered, street, inside, choose, shriek, woken, recognised,
            caught, story, fooled, run, clean, home]


page(P + "mind.heist", "The hothouse", heist(True),
     requires=("trickster.ever", RETURNED, FOUND, NIGHT1), forbids=(SHELL, EMBODIED) + LIVE, delay=24)

page(P + "mind.heist_alone", "The hothouse", heist(False),
     requires=("trickster", "trickster.ever", PRIMED, VEIL), forbids=(SHELL, KILLED), delay=12, kind="event")


# --- The second night: where the Commander sleeps -------------------------------------------------------------------------

page(P + "mind.dream", "Where you sleep", [
    nar("start", '''{n}You dream of Kenabres, and she is already there.{/n}
{n}She has not waited on the fountain tonight. She is walking the square as if she owns it, stepping over the dead with her skirts lifted, reading the burning buildings the way a scholar reads a shelf. The ash still falls on her. She has stopped shivering.{/n}''',
        c("Continue", "tour")),
    sh("tour", '''"Every night. The same dragon, the same square. You have the most repetitive head I have ever been inside, Golarian." {n}She stops by a collapsed cart and pokes a burning wheel with her toe.{/n} "Do you know what this is? This is a man who dreams with his reins on. Something bad happened to you here, and every night you ride it round the same ring, so it can't get loose."''',
        c('"It did get loose. That\'s the problem."', "loose"),
        c('"Show me what you\'d do with it, then."', "show")),
    sh("loose", '''"No. It got loose once, and you have been catching it every night since." {n}She comes close. In the dream she smells of cinnamon and something burnt.{/n} "I told you in my Harem. A dream is a bird, not a horse. You can't restrain it. You can only hurt it with your reins." {n}Her mouth curls.{/n} "Let me show you what I used to do with birds."''',
        c("Continue", "show")),
    nar("show", '''{n}She lifts her hands, and Kenabres comes apart.{/n}
{n}Not burning: opening. The square unfolds like the petals of an enormous flower, and underneath it there is sky, a sky so blue and so high that it hurts, and falling down it, slow as snow, are sparks. Thousands of them. Every one of them a dream: a song, a city, a face, a kiss. You watch them drop away beneath you towards a world you cannot see.{/n}''',
        c("Continue", "heaven")),
    sh("heaven", '''"That was my work." {n}She is standing beside you on nothing, and she has wings in the dream, great wings of fire, and she does not seem to know it.{/n} "Every night, for longer than I can count. A dream for a baker's girl who would never be anything. A dream for a king who needed to be frightened. Some of them I made too hot. Some of them lit fires that burned cities down." {n}She shrugs, and the fire on her shoulders shrugs with her.{/n} "It was beautiful. I would do it again."''',
        c('"You would?"', "again"),
        c('"You\'ve got your wings back."', "wings")),
    sh("again", '''"Every one." {n}She looks at you, and in the blue light her face is younger and very much worse.{/n} "My masters wanted me to dream small. Safe dreams, with reins on. I wanted to see how high they would fly. When one of them flew high enough to burn a world, I watched it all the way to the top, and I have never been sorry." {n}Then, softer:{/n} "And afterwards there was nowhere to go home to, and she came out across the black water for me."''',
        c("Continue", "noct")),
    sh("wings", '''{n}She looks at her shoulders, and for a heartbeat her whole face is naked with longing. Then the wings are gone, and there is only a woman in a red dress, standing on nothing.{/n}
"In your head. Only in your head." {n}Her voice has gone flat.{/n} "It's a memory, Golarian, and it is mine, and you are not to touch it." {n}A pause.{/n} "She came out across the black water for me, after. My lady. And she put the fire out, very gently, and I let her."''',
        c("Continue", "noct")),
    sh("noct", '''"Nocticula never dreams. She never has. She paints nightmares into murderers' heads for sport, but she has never had one of her own, and so she keeps people who do." {n}The sky has begun to darken at the edges, the way paper browns before it catches.{/n} "I was the thing in her Harem that dreamed. That is what a chosen lover is, in the Abyss. A window."
"And now I am a draught behind a clown's eyes, walking through the clown's dreams, because they are the only fire I have left."''',
        c("Continue", "fire_start")),
    nar("fire_start", '''{n}And then she does something you did not ask for.{/n}
{n}The sparks stop falling and start rising. Your Kenabres comes back, but not as it was: taller, stranger, the cathedral a spire of glass, the dragon not falling but climbing, and in the square below every soul who ever died there is standing with their faces upturned, burning with a terrible joy. It is the most beautiful thing you have ever dreamed. It is a dream for which somebody, somewhere, would burn a city.{/n}''',
        c("Continue", "arueshalae", requires=(SAW_ARUESHALAE,)),
        c("Continue", "choice", forbids=(SAW_ARUESHALAE,))),
    sh("arueshalae", '''"Oh, and there's your succubus." {n}At the edge of the burning square, in the dream, a winged figure is watching you. She is holding a flower.{/n} "Desna's little convert, dreaming of flowers. I told her in my own throne room that she had fallen low, and she did not even answer me. She was always dull." {n}Something in the voice does not quite match the words.{/n} "She's the only other one of us I ever met who got out of the city. I did not like it then. I dislike it now."''',
        c("Continue", "choice")),
    sh("choice", '''"There." {n}She is breathing hard, in the dream, as if she has been running.{/n} "That is what I am, Golarian. That is what you let in. Let me finish it. Let the bird go. You will wake up with it in you, and for a month you will see everything a little brighter, and do things you would never have done. That is my gift. It is the only one I ever gave."''',
        c("[Let the dream burn.]", "burn", flags=(DREAM2, BURNED)),
        c("[Take the reins back. Kenabres, as it was.]", "kept", flags=(DREAM2, KEPT_DREAM))),
    nar("burn", '''{n}You let it go. The dragon climbs. The dead sing. Something in you that has been held tight since Kenabres comes loose and goes up with the sparks, and you do not try to catch it.{/n}
{n}You wake with tears on your face and a laugh in your throat, and for the whole of the next day the sky over the camp looks unbearably high, and you give three orders that make your officers stare, and all three of them are right.{/n}''',
        c("Continue", "morning_burned")),
    sh("morning_burned", WHISPER + '''"There." {n}She sounds exhausted, and very pleased with herself.{/n} "That was a good one. That was one of mine. I had forgotten what it felt like, to throw one." {n}A pause.{/n} "Don't thank me. You'll regret it in a month, or somebody will."''',
        c("[Get up.]")),
    nar("kept", '''{n}You take hold of the dream the way you would take a horse by the bridle, and pull. The spire shrinks back to a cathedral. The dragon falls, slowly, the way she always falls. The dead lie down. Kenabres, as it was: grey and burning and yours.{/n}
{n}Beside you, she lets go all at once, and the fire goes out of her like water out of a cracked jug.{/n}''',
        c("Continue", "morning_kept")),
    sh("morning_kept", WHISPER + '''"Reins." {n}She says it without heat. That is worse than heat.{/n} "You would rather dream the same bad thing every night than one beautiful thing once. Every mortal I ever gave a dream to was like you, in the end. They all took the reins back." {n}The crystal cools a little.{/n} "Keep them, then. It's your head. For now."''',
        c("[Get up.]")),
], requires=("trickster.ever", RETURNED, NIGHT1), forbids=(DREAM2, EMBODIED) + LIVE, delay=24)


# --- The third night: almost (desire, in a dream, refused by her) ----------------------------------------------------------

ALMOST = P + "almost"

page(P + "mind.almost", "Almost", [
    nar("start", '''{n}You do not dream of Kenabres tonight. You dream of nowhere: a warm dark, like the inside of a closed hand, and the sound of water somewhere, running over stone.{/n}
{n}She is there before you are. She is sitting on the edge of a pool you cannot quite see, with her feet in the water and her red hair down, and she is not wearing anything at all, because in a dream there is no reason to.{/n}''',
        c("Continue", "look")),
    sh("look", '''"Don't pretend you're not looking. I can see you looking. I can see it from the inside, which is so much better." {n}She leans back on her hands, and the dark around her takes on the colour of her skin, warm, like light through a lampshade.{/n}
"This is my Harem's bathing room, as I remember it. I have not been able to remember a room properly since I died. I remembered this one in your head tonight. You were thinking of it without knowing." {n}A slow smile.{/n} "You were thinking of me in it."''',
        c('"You put it there."', "put"),
        c('[Step into the water.]', "water")),
    sh("put", '''"I put nothing there. I haven't the fire to put things anywhere, any more. I only turn up the lamps on what I find." {n}She tilts her head.{/n} "And I found this. It was under the war and the dragon and the barley, where you keep the things you would rather nobody found. Right at the bottom. Warm as a stove."''',
        c('[Step into the water.]', "water")),
    nar("water", '''{n}The water is warm, blood-warm, and it smells of cinnamon and something burnt. She watches you come, and does not move to meet you, and does not move away. When you are close enough to touch her she puts one long hand flat on your chest, the way a physician feels for a heartbeat, and holds you there.{/n}
{n}Her hand is hot. It is the first hot thing about her since the boudoir.{/n}''',
        c("Continue", "almost")),
    sh("almost", '''"Your heart is going like a rabbit's." {n}She sounds delighted, and very close, and her mouth is an inch from yours and not closing the inch.{/n} "I could have you here. Now. As many times and ways as you have ever imagined and a great many you haven't; I have done it for thousands, in their sleep, in their own beds, beside their wives. It is the easiest thing in the world."
{n}Her hand stays flat on your chest. It does not push. It does not pull.{/n}''',
        c("[Close the inch.]", "no"),
        c("[Wait.]", "no")),
    sh("no", '''"No." {n}She says it against your mouth, so close you feel the word more than hear it, and then she takes her hand away and the warmth goes with it.{/n}
"Not in a dream. I have had a thousand lovers in dreams, and I remember none of them. It is like eating in your sleep. You wake up hungry." {n}Her eyes are very bright.{/n} "I want the one with teeth, Golarian. With a floor under it and a morning after. Find me a body, and I'll show you the difference."''',
        c("Continue", "wake")),
    nar("wake", '''{n}You wake in the grey before morning, sweating, with the blanket on the floor and the taste of cinnamon in your mouth. Behind your eyes a second heartbeat is going fast, and it is not yours.{/n}
{n}Neither of you says anything about it all day. At dusk, very quietly, in your head:{/n} "Rabbit."''',
        c("[Get up.]", flags=(ALMOST,))),
], requires=("trickster.ever", RETURNED, DREAM2), forbids=(ALMOST, EMBODIED) + LIVE, delay=24)


# --- The fuel: what wakes a body (the pivotal choice, her evil demand) ------------------------------------------------------

page(P + "mind.fuel", "What wakes a body", [
    nar("start", '''{n}You open the wardrobe, and there she hangs between your coats: the stolen body, pale and faceless, long-handed, still smelling faintly of black earth. You put your hand on its chest, where a heart would be, and for a while you both look at it: you with your eyes, and she with them too.{/n}''',
        c("Continue", "torn", requires=(TORN,)),
        c("Continue", "chosen", requires=(CHOSE_ALONE,), forbids=(TORN,)),
        c("Continue", "good", forbids=(TORN, CHOSE_ALONE))),
    sh("torn", WHISPER + '''"Look at my collarbone." {n}There is a long white seam there where the last root tore it, like a split in fine leather.{/n} "I shall be able to shape the face, and the hair, and everything else a succubus can shape. That, I can already tell you, I shall not be able to shape away. You put it there. It's yours. I'll wear it for you every day, to remind you."''',
        c("Continue", "fire")),
    sh("chosen", WHISPER + '''"You chose this." {n}She is looking at it the way a woman looks at a dress somebody else has bought her.{/n} "Alone, before you had even killed me, you went down into Ramisa's garden and walked the beds and picked a body for a woman you had spoken to twice. Tall. Long hands." {n}A strange pause.{/n} "It's the right one. I'd have chosen it. I have not decided whether that flatters me or frightens me."''',
        c("Continue", "fire")),
    sh("good", WHISPER + '''"Good bones." {n}She says it the way a horse-trader says it, but her voice is not steady.{/n} "Good skin. The hands are right. Ramisa always did grow hands well." {n}A pause.{/n} "It's empty, Golarian. It has never been anyone. When I go into it, it will be the first thing that ever happened to it."''',
        c("Continue", "fire")),
    sh("fire", '''"Now listen, because I will say this once and I will not soften it." {n}The voice in your head is very clear, very cold.{/n} "A body that has never been anyone does not wake because a soul walks into it. It is a cold hearth. You can put all the wood you like in a cold hearth; you still need a spark. Once, I was my own spark. The cauldron has my spark now."
"I need fire. Dreams are fire. They are the only fire I know how to carry."''',
        c('"Mine."', "mine"),
        c('"Why mine?"', "why")),
    sh("why", '''"Because you took the body with your own hands, and you let me in with your own mind, and I have lain in your sleep for nights now, soaking in it like a stone in a stream." {n}Something that is almost gentleness.{/n} "It will only answer to your dreams now. Anyone else's would be like pouring wine into a lamp."''',
        c("Continue", "mine")),
    sh("mine", '''"Yes. Yours." {n}She lets that sit.{/n} "And understand what that means. I cannot carry a fire out of your head and keep it. It burns down. Every night, for as long as this body lasts, I will have to walk back into your sleep to warm it at yours." {n}A pause.{/n} "You will never dream alone again, Golarian. Not of Kenabres, not of your bread, not of anything. Every dream you have from tomorrow, I will be sitting in it. Some nights I will talk. Some nights I will not. I will always be there."''',
        c("Continue", "demand")),
    sh("demand", '''{n}Then her voice changes. It goes low and sweet and reasonable, the voice of the woman on the throne explaining to a mortal how the world works.{/n}
"And yours alone will make me a small fire. A candle in a big cold house. I was a bonfire, Golarian." {n}You feel her smile.{/n} "There is a barracks by the north gate. Two hundred Mendevians, sleeping in rows, dreaming of home and girls and glory. Let me walk through them once, on the way out. One night. They'll wake a little duller. Nobody will ever know why."''',
        c("Continue", "demand_fed", requires=(SPY_FED,)),
        c("Continue", "demand_burned", requires=(BURNED,), forbids=(SPY_FED,)),
        c("Continue", "demand_plain", forbids=(BURNED, SPY_FED))),
    sh("demand_fed", '''"You gave me a captain, at your war table, with a hand on his shoulder. You did not even blink." {n}The heat behind your eyes is almost unbearable.{/n} "One man was a mouthful. This is a meal. I could be something again, Golarian. Something worth standing next to."''',
        c("Continue", "choose")),
    sh("demand_burned", '''"You let one of my birds go, the other night. You felt what it is to be lit. Imagine two hundred of them." {n}The heat behind your eyes is almost unbearable.{/n} "I could be something again. Something worth standing next to."''',
        c("Continue", "choose")),
    sh("demand_plain", '''"You took the reins back, the other night. You liked your bad dream better than my good one. Fine. Keep yours tame." {n}The heat behind your eyes presses outward.{/n} "But you cannot want me tame. Nobody has ever wanted me tame. Give me the barracks."''',
        c("Continue", "choose")),
    nar("choose", '''{n}The wardrobe is very quiet. Somewhere outside a sentry calls the hour. Two hundred men in the north barracks are asleep, and one of them, probably, is dreaming of a girl, and one of him, probably, is dreaming of you.{/n}''',
        c('"Mine. Only mine. You\'ll burn small."', "only_mine", flags=(FUEL, REFUSED_BARRACKS)),
        c('"Mine, and the barracks. One night."', "barracks", flags=(FUEL, BARRACKS, SECRET), alignment=("Evil", 2)),
        c('"Not my dreams. There has to be another way."', "no_way")),
    sh("only_mine", '''{n}For a moment she is silent, and you feel her anger go all through you like a fever, and pass.{/n}
"A candle, then." {n}Very quietly.{/n} "You would rather keep two hundred strangers' sleep than have me blaze. That is either very good of you, or you simply don't want to share me with a barracks." {n}A breath.{/n} "I have not decided which. I think I prefer the second. Tomorrow night, Golarian. Lie down beside me, and dream me awake."''',
        c("[Close the wardrobe.]")),
    sh("barracks", '''{n}The heat behind your eyes flares so hot that the wardrobe swims.{/n}
"There," {n}she breathes.{/n} "There it is. That's the thing under the barley. I knew there was something under there." {n}She is laughing, low and delighted and entirely without mercy.{/n} "One night. I'll go through them like a wind through wheat, and in the morning your sergeants will wonder why the men are so quiet at breakfast. Then tomorrow, you. And I will be myself again."''',
        c("Continue", "north")),
    nar("north", '''{n}That night you do not sleep. You stand in the doorway of the north barracks with your eyes open while two hundred men snore in rows, and you feel her go out of you and along the rows like a draught along a floor, and come back, and go out again.{/n}
{n}Here and there a man sighs, or smiles, or stops smiling. That is all. In the morning your head aches as if you had drunk the whole night, and at breakfast the north barracks eats in silence, and nobody can say why.{/n}''',
        c("[Go back to the wardrobe.]")),
    sh("no_way", '''"There is no other way." {n}Flat. Final.{/n} "You think I have not looked? I have been looking for days, in the dark, with nothing to do but look. Your dreams or nothing. Burn, or I stay behind your eyes for good." {n}A pause, and the voice goes dangerous.{/n} "And you want your head back, don't you. I've seen it in you. You want to be alone in there again."''',
        c('"...All right. Mine."', "only_mine", flags=(FUEL, REFUSED_BARRACKS)),
        c('[Push her into the back of your head and shut the door] "Then stay back there."', "kept", flags=(KEPT, CLOSED), alignment=("Evil", 1)),
        c('[Throw her out of your head] "Then go."', "cast")),
    nar("kept", '''{n}You push, and shut the door. The voice stops. The second heartbeat goes on at the back of your head, faster, then slower, then very slow, like a fist on a door that has decided to wait.{/n}
{n}You leave the body in the wardrobe. After a week you stop noticing it there, and after a month you start again.{/n}''',
        c("[Close the wardrobe.]")),
    sh("cast", '''"You wouldn't." {n}But she knows you would. She has been in your head for days.{/n} "You would. For what? For a quiet head? You are going to throw me into the Abyss's mouth so that you can sleep alone?"
{n}Her voice cracks, and it is not anger underneath any more. It is terror.{/n} "Golarian. Don't. Not the mouth. I know what's in the mouth."''',
        c("[Throw her out.]", "cast_out", flags=(CAST_OUT, CLOSED), alignment=("Evil", 2)),
        c('"...No. Mine, then. Take them."', "only_mine", flags=(FUEL, REFUSED_BARRACKS))),
    nar("cast_out", '''{n}You push, with everything you have, all at once, the way you would throw open a window on a room full of smoke.{/n}
{n}What goes out of you is a heat, and a smell of cinders and cinnamon, and a voice that says your name once, very clearly, and then goes down through the floorboards the way water goes down through sand. For a moment the whole wardrobe smells of her. Then it smells of your coats.{/n}
{n}Your head is quiet. It has not been quiet in days. The body hangs between your coats, and will go on hanging there, empty, until you think of something to do with it.{/n}''',
        c("[Close the wardrobe.]")),
], requires=("trickster.ever", RETURNED, DREAM2, SHELL), forbids=(FUEL, EMBODIED) + LIVE, delay=24)


# --- The waking: dreams for a body -------------------------------------------------------------------------------------

page(P + "mind.waking", "Dreams for a body", [
    nar("start", '''{n}You take the body down off its hook and lay it on the floor of the wardrobe, among your boots, with its head on a folded cloak. It is lighter than it was in the earth. It is very cold. Its face is smooth and blank, a sketch of a face, waiting.{/n}
{n}You lie down beside it, and put your hand on its cold chest, and close your eyes.{/n}''',
        c("Continue", "walk")),
    nar("walk", '''{n}She goes out of you like heat goes out of an oven door: you cannot see it, but the dark behind your eyes shivers, and your face goes hot, and the smell of cinders and cinnamon fills the wardrobe until your eyes water. The second heartbeat that has lived beside yours since the boudoir falls quiet, a little at a time, like a bell after it has been struck.{/n}
{n}The body does nothing. It lies there, with her inside it, cold as a stone.{/n}''',
        c("Continue", "cold")),
    sh("cold", WHISPER + '''{n}Her voice comes from very close now. Not from behind your eyes. From the floor.{/n} "It's dark in here. It's so dark. It's like being buried in snow." {n}Something that would be a shudder, if she could move.{/n} "Go to sleep, Golarian. Here, beside me, on your own boots, like a dog. Dream. Dream anything. Dream as loud as you did in my Harem, and I will come and fetch the fire."''',
        c("Continue", "last")),
    nar("last", '''{n}The wardrobe floor is hard, and your coats hang over you like the walls of a tent, and she is a cold shape against your side. You lie there a long while, listening to the city outside. Then you understand, the way you understand things in the moment before sleep, that this is the last time you will dream alone.{/n}
{n}After tonight, every dream you have will have her in it. You may as well choose this one.{/n}''',
        c("[Dream of home, as it was before the war.]", "dream_home", flags=(LAST_HOME,)),
        c("[Dream of the war won, and of nothing after it.]", "dream_peace", flags=(LAST_PEACE,)),
        c("[Dream of her, on her throne, burning.]", "dream_her", flags=(LAST_HER,))),
    nar("dream_home", '''{n}You dream of home. Not the home it became, but the one before: a door you knew the sound of, a kitchen, bread, somebody calling your name up a stair to tell you it was late. It is so ordinary that it hurts.{/n}
{n}Then the kitchen door opens, and she comes in, in a red dress, and sits at the table, and looks around at it all, and for once she does not say anything clever. She eats a piece of your bread. She holds her hands out to your hearth. She will be back tomorrow. She will always be back.{/n}''',
        c("Continue", "taken")),
    nar("dream_peace", '''{n}You dream of the war won. The Wound shut like an eye. The crusade going home, singing, dusty, in no order at all. The fields north of Drezen green again, and nothing waiting at the edge of them.{/n}
{n}Then she is walking beside you up the road, in a red dress, and looks at the green fields, and at you, and for once she does not say anything clever. She holds her hands out to the sun on the road as if it were a hearth. She will be back tomorrow. She will always be back.{/n}''',
        c("Continue", "taken")),
    nar("dream_her", '''{n}You dream of her. Of course you dream of her. The Harem, the throne, the red hair, the light around her so fierce that it withers the courtiers at her feet and does not touch you at all.{/n}
{n}And then she is there too, the real one, standing at the foot of the dais, looking up at herself in your dream. For once she does not say anything clever. Her face does something you have never seen it do. She holds her hands out to the light of her own throne as if it were a hearth.{/n}''',
        c("Continue", "taken")),
    nar("taken", '''{n}It does not hurt. That is the strange thing. It is like watching someone warm themselves at your fire, and then carry a coal of it away in their hands, cupped, into another room, and hearing the door close.{/n}
{n}And then you wake, and the wardrobe is grey with morning, and you are lying on your own boots, and there is only one heartbeat behind your eyes.{/n}''',
        c("Continue", "risen")),
    nar("risen", '''{n}She is standing in the doorway of the wardrobe, wearing your good coat and nothing else, with one long hand on the frame to keep herself up.{/n}
{n}The body has a face now. Her face: the one from the throne, sharp and proud and made for contempt, with the red hair falling over it in a heavy wave. She has shaped it in the night, the way a succubus shapes anything she wants to be. Only the eyes are new. They blink too often, as if the light in the room is a surprise.{/n}''',
        c("Continue", "risen_barracks", requires=(BARRACKS,)),
        c("Continue", "risen_torn", requires=(TORN,), forbids=(BARRACKS,)),
        c("Continue", "risen_small", forbids=(BARRACKS, TORN))),
    nar("risen_barracks", '''{n}There is light around her. Not the old light, not the throne-light that withered the courtiers where they knelt, but a glow, low and hot, like embers under ash. It makes the coats on either side of her steam faintly. It makes your eyes ache to look at her, and you look anyway.{/n}''',
        c("Continue", "first_words")),
    nar("risen_torn", '''{n}Where the coat falls open at the throat, you can see the seam: a thin white line across the collarbone where the last root tore her on the way out of the earth. Everything else about her she has made perfect. That, she has left.{/n}''',
        c("Continue", "first_words")),
    nar("risen_small", '''{n}There is no light around her. There is only a woman in a coat, a tall red-haired woman with long hands, standing in a wardrobe door in the grey of the morning. She looks, as she never has since you met her, like something that could be killed. She looks as if she knows it.{/n}''',
        c("Continue", "first_words")),
    sh("first_words", '''{n}She speaks aloud. Her voice is her voice, low and rich and contemptuous, and it cracks in the middle like a girl's.{/n}
"I have it." {n}She touches her own chest, where your hand lay.{/n} "Your fire. A coal of it, in here, keeping me warm. It will last until tonight." {n}She looks down at you, lying on your boots.{/n} "And tonight I will be back in your sleep for another. And tomorrow. Do you understand what you've done?"''',
        c('"I understand."', "understand"),
        c("[Say nothing. Let her read it.]", "understand"),
        c('"Rabbit."', "rabbit", requires=(ALMOST,))),
    sh("rabbit", '''{n}Her mouth twitches.{/n} "Rabbit." {n}She crouches, awkwardly, in a body that does not yet know how to crouch, and puts one long hand flat on your chest, exactly where she put it in the dream by the water. It is warm. It is the first warm thing about her.{/n}
"Still going like one. Good." {n}Then she reads the rest of you, and her face changes.{/n}''',
        c("Continue", "understand")),
    sh("understand", '''"No. You don't." {n}She is reading it off you, and whatever she finds there makes her close her eyes.{/n}
"I have walked into ten thousand sleepers' dreams and out again, and never once gone back to the same one. You have given me a hearth. Nobody has ever given me a hearth. I shall sit at it every night until one of us is dead, and you will never again close your eyes and be alone." {n}When she opens them again they are hard.{/n} "It is a terrible thing to have done to you. I did it. I'd do it again. Get up off the floor, Golarian. You look like a corpse, and I have had enough of those."''',
        c("Continue", "go")),
    sh("go", '''"Now. My city thinks I'm dead. My court will have eaten each other by now, trying to sit in my chair." {n}She pulls your coat tighter, and it does not suit her, and she wears it as if it were ermine.{/n} "I am going home to find out who. I can still walk between worlds. Barely. It will hurt."
{n}She steps back into the wardrobe, among your coats, and closes the door on herself. When you open it again, there is nobody in it, and your good coat is gone.{/n}''',
        c("[Close the wardrobe.]", flags=(EMBODIED, NEVER_ALONE))),
], requires=("trickster.ever", RETURNED, FUEL, SHELL), forbids=(EMBODIED,) + LIVE, delay=24, kind="visit")


# --- A war council with her behind the Commander's eyes: other people's heads ---------------------------------------------------------

page(P + "mind.war_table", "Other people's heads", [
    nar("start", '''{n}The council of war runs late. Baphomet's templars have been probing the walls for a week: a gate here, a postern there, never twice in the same place, always where the watch is thinnest. Your officers stand round the map table and argue about it with the particular bitterness of tired men who all suspect each other.{/n}
{n}The second heartbeat behind your eyes has quickened. You have learned to feel when she is paying attention.{/n}''',
        c("Continue", "tour")),
    sh("tour", WHISPER + '''"Oh, this is lovely. This is like my court on a feast night." {n}She is reading them through you, one after another, the way a woman runs a finger along a row of spines.{/n} "The fat one with the moustache is thinking about his supper. The young one is thinking about the fat one's wife. The one with the scar thinks you are a fool and would die for you anyway, which is the most Golarian thing I have ever tasted." {n}A pause.{/n} "And the one by the brazier is afraid."''',
        c('"Everyone is afraid. There\'s a siege on."', "afraid"),
        c('"Afraid of what?"', "afraid")),
    sh("afraid", '''"Not of the templars. Of you." {n}Her voice sharpens, the way it did in her Harem when she smelled a conspiracy.{/n} "Captain of the wall watch. Every time you touch the map near the north postern he thinks of a girl of nine in a cell under a goat-headed temple, and then of a list of hours, and then of your face, and then he tries very hard to think of nothing." {n}Something almost like admiration.{/n} "He's rather good at it. Not as good as you."''',
        c("Continue", "list")),
    sh("list", '''"He has been selling them the watch. Which gate, which hour, how many men. They have his daughter, and every list he sends buys her another week." {n}She is enjoying this, and she is not hiding that she is enjoying it.{/n} "My lady used me like this for years, you know. At her feasts. I would stand behind her chair and tell her which of her guests wanted her dead, and she would smile at them, and in the morning they would be gone."
"So. What does the clown do with his traitor?"''',
        c("[Have him taken now, and hanged at the next dawn.]", "hang", flags=(SPY_HANGED,), alignment=("Lawful", 1)),
        c('[Keep him. Let him keep selling, and make sure every hour he sells is a lie.]', "turn", flags=(SPY_TURNED,), mythic="Trickster"),
        c("[Put a friendly hand on his shoulder on the way out, and let her have his dreams.]", "feed", flags=(SPY_FED,), alignment=("Evil", 1))),
    sh("hang", '''{n}He does not fight when they take him. He looks at you across the map table, once, and he knows exactly how you knew, and he does not understand it at all.{/n}
"Dull." {n}The voice in your head is amused.{/n} "Correct. Dull. The templars will find another captain, and his girl will be dead by the end of the week, and you will never think about her, because you have a war." {n}A little silence.{/n} "I would have done the same. I would have enjoyed it more."''',
        c("Continue", "after")),
    sh("turn", '''{n}You let him go on standing by the brazier, afraid. You let the council end. And that night, with her in your ear, you sit up with the watch-rolls and write a new north postern: the hours, the men, the gate, all of it true for exactly one night.{/n}
"Oh." {n}She sounds genuinely delighted.{/n} "Oh, now that is a joke. He sells them a door, and they walk into a wall of your crossbows, and his daughter stays alive because they still think he's useful." {n}She laughs, low, in your skull.{/n} "My lady would never have thought of that. She only ever thought of mornings."''',
        c("Continue", "after")),
    sh("feed", '''{n}The council ends. The officers file out. You stop the captain at the door, and put your hand on his shoulder, and ask after his health, and while he stammers something about the cold you feel her go down your arm and into him like a draught under a door.{/n}
{n}He blinks. He says good night. His eyes, as he goes, are a little flatter than they were.{/n}
"There." {n}She sighs, warm again after days of cold.{/n} "He won't dream of his girl any more. He won't dream of anything. And he'll never sell you another list; he hasn't the imagination left." {n}A pause.{/n} "Neither has his daughter, now, a friend. You don't mind."''',
        c("Continue", "after")),
    sh("after", '''"You're good at this, you know." {n}Grudging, and not entirely grudging.{/n} "Most of the mortals who have ever had me at their ear either weep about it or make me into a trick at parties. You used me the way she did. Like a knife she kept in her sleeve."
{n}The heat behind your eyes is a little warmer than it needs to be.{/n} "Put your hand over your heart, Golarian. No, not to push me out. Just put it there. I have been nobody's knife for a whole week."''',
        c("[Put your hand over your heart.]")),
], requires=("trickster.ever", RETURNED, NIGHT1), forbids=(SPY_HANGED, SPY_TURNED, SPY_FED, EMBODIED) + LIVE, delay=24)


# --- The barracks, afterwards (her evil demand, met): what the Commander does about the secret ------------------------

BARRACKS_BLAMED = P + "barracks.blamed"
BARRACKS_COVERED = P + "barracks.covered"
BARRACKS_TOLD = P + "barracks.told"

page(P + "mind.barracks_after", "The north barracks", [
    nar("start", '''{n}The surgeon of the north barracks asks for you by name, which surgeons do not do. He is a thin Mendevian with ink on his cuffs and he will not sit down.{/n}
"A sergeant, Commander. Hanged himself in the tack room, three nights back. Good man. No debts, no woman, no drink to speak of." {n}He turns his cap in his hands.{/n} "And the rest of them... They eat. They drill. They do what they're told. But they've stopped talking in their sleep, Commander. All two hundred. I've been a barracks surgeon twenty years, and I've never heard a barracks go quiet like that."''',
        c("Continue", "chaplain")),
    nar("chaplain", '''"The chaplain's been asking questions." {n}He says it low.{/n} "Whether anything came through the north gate that night. Whether anybody saw a woman. One of the lads says he dreamed of a red-haired woman walking down the rows, and then he never dreamed again." {n}He looks at you, and he does not want to know, and he is going to ask anyway.{/n} "Commander. Do you know anything about this?"''',
        c('"Men break, surgeon. There\'s a war on. Write it up as the war."', "blame", flags=(BARRACKS_BLAMED,)),
        c("[Pay him to write it up as marsh fever, and move the barracks to the south wall where nobody asks.]", "cover",
          flags=(BARRACKS_COVERED,), crusade=("Favors", -150)),
        c('"Yes. It was me. Tell the chaplain he can come and ask me himself."', "told", flags=(BARRACKS_TOLD,))),
    nar("blame", '''{n}He writes it up as the war. He does not believe it, and he knows you know he does not believe it, and he goes back to his quiet barracks with his cap in his hands.{/n}
{n}The chaplain goes on asking questions. Nobody answers them. Not yet.{/n}''',
        c("[Let him go.]")),
    nar("cover", '''{n}Marsh fever, then. The surgeon's hand shakes as he signs it. The barracks goes south by the end of the week, to the far wall, where the watches are dull and nobody comes, and the chaplain finds, when he goes looking, that the men he wanted to question are three miles away and have forgotten what he wanted to ask.{/n}
{n}It is a good cover. It is also a debt you have put into the hands of a frightened man with ink on his cuffs.{/n}''',
        c("[Let him go.]")),
    nar("told", '''{n}He stares at you. Then he goes, fast, without his cap.{/n}
{n}The chaplain comes that evening. He stands in your doorway and you tell him, not all of it, but enough: a demon you owed a life to, a barracks' sleep, a price. He listens without a word. When you are finished he does not bless you. He does not curse you either. He only says that he will pray for the two hundred, since nobody else will, and goes.{/n}
{n}Word of it goes round the chaplains before the week is out. Nobody in the crusade who prays for a living looks at you quite the same way again.{/n}''',
        c("[Let him go.]")),
], requires=("trickster.ever", BARRACKS, EMBODIED), forbids=(BARRACKS_BLAMED, BARRACKS_COVERED, BARRACKS_TOLD), delay=72, kind="event",
    chapters=(5,))


def integrate(payload):
    """Her one native read here (the Chapter 4 Arueshalae cue), bound as a SeenCue."""
    for key, guids in SEEN_CUES.items():
        have = payload.setdefault("SeenCues", {}).get(key)
        if have is not None and have != guids:
            raise ValueError("Conflicting binding: " + key)
        payload["SeenCues"][key] = list(guids)
