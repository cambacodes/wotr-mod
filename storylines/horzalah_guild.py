"""Horzalah, Chapter 5 and after: the courtship on her presence by the Storyteller's shelves in Drezen, and her letters,
which never come by courier (11-ROSTER-PLAN-2 §2 build sheet; horzalah_trickster holds the device chain and the commit).

She comes to Drezen through no door at all, stands where she likes, and the soldiers step off the path. Every beat is
optional and opens from her presence (or arrives pinned to the Commander's pillow by a knife): her name (Horzalah, not
Hepzamirah), the blind Storyteller, her father's seals and his verdict on the weaker branch, her sister's cell, Yozz and his
leash, the Guild's notice board and her agents in Drezen, the Lady in Shadow's city, the dwarf who betrayed her, a knife
lesson, the ear, the Threshold and Deskari's army, the ribbon, a crusader who spits at her, and the collar she stops
wearing. The possessive voice stays hers; nothing here is settled as exclusive fact.

Every scene is Trickster-only (T in PATH_FIT): it follows the device.
"""
from story_format import c, n, scene
from storylines.horzalah_trickster import (ALLY, CANARY, FREED, CHAMBER, CLOSED, COMMITTED, DECLINED, DREZEN, GREY_IN, HEPZ_BACK,
                                            LATE, LEFT_FREE, MET_A, MET_B, MET_Q2, NAMED, P_KNIFE, P_PIPE, P_RIBBON, PRESENCE, REL,
                                            SCAR_NOTED, TESTED, UNIT, WANTS, H, hz, nar, tag)

SCENES = []

NAME = H + "beat.name_said"
TOLD = H + "beat.storyteller_heard"
FATHER = H + "beat.father_heard"
STRONGER = H + "beat.told_stronger"
SISTER = H + "beat.sister_heard"
YOZZ = H + "beat.yozz_heard"
BOARD = H + "beat.board_heard"
AGENT = H + "beat.agent_asked"
LADY = H + "beat.lady_heard"
DWARF = H + "beat.dwarf_heard"
KNIFE = H + "beat.knife_lesson"
NICKED = H + "beat.knife_nicked"
EAR_SEEN = H + "beat.ear_seen"
WAR = H + "beat.threshold_heard"
SPIT = H + "beat.crusader_seen"
BARE = H + "beat.collar_bare"
LETTER1 = H + "letter.first_read"
HUNGER = H + "beat.fed"
THOUSANDS = H + "beat.thousands_heard"
LABYRINTH = H + "beat.labyrinth_heard"
HEAD = H + "beat.head_given"
RAMPARTS = H + "beat.ramparts_walked"
HAT = H + "beat.hat_worn"
CUP = H + "beat.cup_drunk"
QUESTION = H + "beat.question_asked"
SECOND_NIGHT = H + "beat.second_night"
SENTRIES = H + "beat.sentries_walked"
USED = H + "beat.used_heard"
MASTERS = H + "beat.masters_heard"
STOOD = H + "beat.stood_heard"

GREY_DEAD = "greybor.dead"
GREY_KICKED = "greybor.kicked_out"


def beat(id, title, entry, nodes, requires, forbids=(), delay=24):
    """An optional beat on her presence by the Storyteller (Chapter 5)."""
    SCENES.append(scene(id, title, "Horzalah", 5, entry, nodes,
                        requires=("trickster.ever", WANTS, *requires), forbids=(CLOSED, LEFT_FREE, *forbids), delay=delay,
                        last=5, optional=True, Relationship=REL, Chapters=[5], Areas=[DREZEN], ContactUnit=UNIT,
                        InteractionHub=PRESENCE))
    tag(id, "T")


def letter(id, title, nodes, requires, forbids=(), delay=72, chapter=5):
    """A letter pinned to the Commander's pillow, tent pole or map by a knife nobody heard arrive."""
    SCENES.append(scene(id, title, "Horzalah", chapter, "", nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, *forbids), delay=delay, last=chapter, optional=True, Relationship=REL,
                        Chapters=[chapter], Remote=True, Kind="letter"))
    tag(id, "T")


# --- 1. Horzalah, not Hepzamirah. ------------------------------------------------------------------------------------------

beat(H + "beat.name", "Not Hepzamirah", '"You look like you want to kill someone."', [
    hz("start", '''"I always look like that. Today I mean it." {n}She jerks her chin at the street, where a sergeant is marching a file of recruits past the Storyteller's shelves as quickly as their legs will carry them.{/n}
"That one pointed at me this morning and told his boys to keep their distance from *Hepzamirah*. Loudly. So that I would hear." {n}Her fingers drum on her folded arm.{/n} "I have been called Hepzamirah by Yozz's guests, by my father's priests, by a nalfeshnee in a bathhouse and by one of my father's own priests. I did not expect it from a mortal with his helmet on backwards."''',
       c("Continue", "sister_here", requires=(HEPZ_BACK,)),
       c("Continue", "choice", forbids=(HEPZ_BACK,))),
    hz("sister_here", '''"And the insult is worse here, because *she* is here." {n}She does not look toward the smith's yard. She does not need to; you can see her not looking.{/n} "Two streets away, eating onions on a quenching trough, in a body some butcher grew her. Your soldiers look from her to me and think: two of the same. Two horned things of Baphomet's, one broken and one whole."
"We are not the same. We were never the same. That was the whole trouble."''',
       c("Continue", "choice")),
    hz("choice", '''"Well, mortal? You are the one they salute. Tell me what you mean to do about it, and I will tell you whether it is enough."''',
       c('"Sergeant! The lady\'s name is Horzalah. Learn it."', "sergeant"),
       c('[Tease her] "Hepzamirah? I thought you were taller."', "tease"),
       c('"Horzalah." [Say her name, and nothing else.]', "name")),
    nar("sergeant", '''{n}The sergeant stops dead. So do his recruits, in a pile. He looks at you, and at her, and at the side of your head where your ear used to be, and something works itself out behind his eyes that he will be telling in the barracks for a month.{/n}
"Horzalah, Commander," {n}he says, very loudly.{/n} "Yes, Commander. Won't happen again, Commander." {n}He goes up the street at a pace just short of a run.{/n}''',
        c("Continue", "sergeant2")),
    hz("sergeant2", '''"There." {n}She sounds almost disappointed.{/n} "That is the trouble with you, mortal. I had three very good ways to make him remember my name, and you have used the dullest one, and it worked." {n}She watches the recruits scramble after him.{/n} "He will teach it to the others. By tonight your whole citadel will know how to say it. I suppose I should thank you. I will not."''',
       c("[Let her not thank you.]", flags=(NAME,))),
    hz("tease", '''{n}The knife is out of her belt and resting against the soft place under your jaw before you have finished the word *taller*. She is smiling. It is not a nice smile.{/n}
"Say it again, mortal. With the one ear you have left, I want to hear you say it again."''',
       c('"Horzalah."', "tease2"),
       c('"Hepz..."', "tease3")),
    hz("tease2", '''"Better." {n}The knife goes away, slowly, the way a cat withdraws a claw it has not quite decided not to use.{/n} "My sister was dumber than me, and weaker, and our father liked her better because she crawled under walls instead of breaking them. If you ever mix us up again, you will find out which of us I take after."''',
       c("[Rub your jaw.]", flags=(NAME,))),
    hz("tease3", '''{n}The point of the knife goes in exactly far enough to draw a single bead of blood, and stops.{/n}
"Finish that name," {n}she says, very softly,{/n} "and I will take the other ear, and I will not put this one in a box." {n}She waits. When you say nothing, she lowers the blade and wipes the bead off it with her thumb, and looks at the thumb, and licks it.{/n} "You are either very brave or very stupid. I have decided I do not mind which."''',
       c('"Horzalah."', "tease2")),
    hz("name", '''{n}She turns and looks at you properly, as though she had heard something unexpected from a direction she had not been watching.{/n}
"Say it again."''',
       c('"Horzalah."', "name2")),
    hz("name2", '''{n}Her mouth does something complicated.{/n} "Nobody says it like that. They say it like a warning, or like an apology for getting it wrong the first time. You said it like... like the name of a thing that is simply there, and is not going anywhere."
"Do it again when the sergeant comes back. Loudly. I want him to hear how it is supposed to sound."''',
       c("[Promise.]", flags=(NAME,))),
], requires=(), forbids=(NAME, ALLY), delay=12)


# --- 2. The blind Storyteller. ---------------------------------------------------------------------------------------------

beat(H + "beat.storyteller", "The only man who does not look", '"Is he bothering you?"', [
    hz("start", '''"Him?" {n}She glances back at the old elf, who is running his fingers along a row of spines as if reading them, which he is.{/n} "He is the only man in this city I can stand. He is blind. He has never once looked at my throat." {n}She says it without any softening at all.{/n}
"He tells stories. I have made him tell me stories about you. He knows a great many, and he tells them badly, with far too much about courage and not nearly enough about what anybody was paid."''',
       c('"What does he say about me?"', "me"),
       c('"Has he told you any about yourself?"', "herself")),
    hz("me", '''"That you came up out of the ground under Kenabres with a shard of the Wound in your chest, and a crowd of fools behind you, and did not die when anyone sensible would have." {n}She shrugs.{/n} "That you laugh at the wrong things. That you walked into the Abyss and came back out of it, which nobody does. That a king of fools in this very city drinks to your health every night." {n}A glance at the side of your head.{/n}
"There was nothing in any of his stories about an ear. I told him to put it in. He said it was not his story to tell. I said it was mine, and he could have it for nothing. He is thinking about it."''',
       c("Continue", "storyteller")),
    hz("herself", '''"One." {n}Her mouth thins.{/n} "The daughter of the Lord of Beasts who was locked in a cell by her sister and waited there for her father to come, and he did not come. He tells it as a story about patience. It is not. It is a story about waiting, which is a different thing, and very much worse."
"I told him so. He said he would tell it differently next time. I said next time he would tell it about a woman who got out on her own, and he agreed very quickly."''',
       c("Continue", "storyteller")),
    nar("storyteller", '''{n}Behind her, the Storyteller clears his throat. He has turned his blind face toward the two of you, as polite as a man at a funeral.{/n}
{n}"There was an ear," he says mildly, "in an old story of the Isles. A tyrant's ear, sent in a box to his rival, to say: I heard everything you said of me. It started a war that lasted three hundred years." He smooths the page under his hand. "I only mention it."{/n}''',
        c('"This one\'s supposed to end one."', "end_peace"),
        c('"Who won the war?"', "end_war")),
    hz("end_peace", '''{n}She looks at the old elf, and then at you, and then she laughs, low and short, and for once there is nobody's death behind it.{/n}
"You see? Too much about courage," {n}she says to him.{/n} "Put that in, then. That the Knight Commander gave away an ear to stop a war in a Guild of assassins. Nobody will believe it. That is how you will know it is a good story."''',
       c("[Leave them to argue.]", flags=(TOLD,))),
    hz("end_war", '''"The tyrant," {n}says the Storyteller, before she can answer.{/n} "He had the other ear."
{n}Horzalah considers him. Then she reaches out, very gently, and turns the book on his table round the right way up for him, though he cannot see it.{/n} "I like him," {n}she says to you.{/n} "Do not let anything happen to him. I would have to be upset, and I am very bad at it."''',
       c("[Leave them to argue.]", flags=(TOLD,))),
], requires=(NAME,), forbids=(TOLD, ALLY), delay=24)


# --- 3. Her father: the seals, the collar, and the verdict on the weaker branch. --------------------------------------------

beat(H + "beat.father", "The weaker branch", '"Do you ever hear from your father?"', [
    hz("start", '''{n}She is quiet long enough that you think she is not going to answer. When she does, she keeps her eyes on the street.{/n}
"You do not *hear* from my father, mortal. He hears from you. You pray, or you fail, or you offer him something, and then, if he pleases, he answers, and his answer is a seal." {n}Her hand moves toward her own arm, where there is nothing now but skin.{/n} "I had eleven. Did you count them, in Yozz's hall? Most people did."''',
       c('"I didn\'t count them."', "count", requires=(SCAR_NOTED,)),
       c('"I never saw them."', "never", forbids=(SCAR_NOTED,)),
       c('"What were they for?"', "seals")),
    hz("count", '''"No. You looked at the collar." {n}She says it the way another woman might mention a debt that has not been paid.{/n} "The seals were for the things I did. The collar was for the thing I am. His. That is the difference, and it is the whole difference, and you saw it with one look and I have been trying to explain it to demons for a hundred years."''',
       c("Continue", "seals")),
    hz("never", '''"Lucky you. They were very fine work. Demons came from other layers to admire them." {n}Her mouth twists.{/n} "My father lifted every one of them when my sister died, as if they had been lent to me. He left the collar. That was never lent."''',
       c("Continue", "seals")),
    hz("seals", '''"There are seals that grant power, and seals that bring delight, and seals that hurt, and seals that simply mark a body as his. I had the ones that hurt. They drain you. They make you so eager to atone that you would crawl to him on broken knees to be told what for."
"He took my powers when he gave me to Yozz. He gave them back when you killed my sister, because then I was the only one left." {n}She smiles, thinly.{/n} "Do you know what that is called, in the Abyss? Being promoted."''',
       c('"He told me you were the stronger in a fight."', "stronger", requires=(NAMED,)),
       c('"And now he says nothing."', "silence")),
    hz("stronger", '''{n}Her head turns, very slowly.{/n} "He said that."
{n}You tell her the rest of it, since you have started: that she bet everything and lost, and he did not answer; that she was stronger in a fight, and her sister more cunning and more vicious, and that was why her sister prevailed; that he did not care to nourish the weaker branch.{/n}''',
       c("Continue", "stronger2")),
    hz("stronger2", '''{n}She listens to all of it without moving. At the end she lets out a breath through her teeth.{/n}
"*Stronger in a fight.*" {n}She turns the words over as if they were a coin she had found in the street and did not trust.{/n} "A hundred years I have waited for him to say one good thing of me, and he said it to you. In passing. On his way to calling me a weed."
"I should hate you for telling me." {n}She looks at you.{/n} "I am going to keep it instead. It is mine now. I took it off you. That is how I know it is real."''',
       c("[Let her keep it.]", flags=(FATHER, STRONGER))),
    hz("silence", '''"Now he says nothing." {n}She nods, slowly, as if agreeing with a verdict.{/n} "I called his name at the end, you know, when I was on my back. Everyone does. He did not answer, and I thought that was the worst thing that could happen to me."
"It was not. The worst thing would have been if he had answered, and taken back the Guild, and put the collar back on. Silence I can live in." {n}She touches the high leather at her throat.{/n} "I have lived in worse."''',
       c('"You live in it well."', "end"),
       c('"You don\'t have to live in it alone."', "end_alone", forbids=(ALLY,))),
    hz("end", '''"I live in everything well, mortal. It is my great talent. I lived in a cell, and in a gilded leash, and in my sister's shadow, and I came out of all of them better dressed than I went in." {n}She jerks her chin at the street.{/n} "Go on. Your war is waiting. I have a great deal of silence to get through today."''',
       c("[Leave her to it.]", flags=(FATHER,))),
    hz("end_alone", '''{n}She looks at you with an expression you cannot read at all, and then away.{/n}
"Do not say things like that in the street," {n}she says.{/n} "Somebody will hear, and then I will have to kill them, and your soldiers get so upset." {n}But she does not move away, and when you go, she watches you all the way to the corner.{/n}''',
       c("[Go.]", flags=(FATHER,))),
], requires=(), forbids=(FATHER,), delay=24)


# --- 4. Her sister: the cell, the canary. ----------------------------------------------------------------------------------

beat(H + "beat.sister", "The belch of Lamashtu", '"Tell me about Hepzamirah."', [
    hz("start", '''"Must I?" {n}She sighs, theatrically, and then she tells you anyway, because it is clear she has been waiting for someone to ask.{/n}
"She was older. She was dumber. She was weaker; everyone knew it. And she hated me from the day I was spawned, because Father looked at me, once, for about as long as it takes to count to three, and he never looked at her that long in her life."''',
       c("Continue", "cell")),
    hz("cell", '''"So she lured me into a trap. She was always good at traps; that is what cunning is, in the end, being good at the ground. She had me put in the Ivory Labyrinth, in a cell, with my powers bound. And I waited for Father." {n}Her fingers tighten on her arm.{/n}
"He knew. Everything in that Labyrinth is his; he knew exactly where I was. He let her keep me. He let her bind me. He was, I think, curious to see how long I would last."''',
       c('"How long did you last?"', "last"),
       c('"How did you get out?"', "out")),
    hz("last", '''"Long enough to be sold." {n}She says it flatly.{/n} "When Yozz came to make his deal, Father needed something to pay in advance, and there I was, already bound and gift-wrapped. It saved him the trouble. He likes it when things save him the trouble."''',
       c("Continue", "canary")),
    hz("out", '''"I did not get out. I was taken out, by a buyer, on a leash. It is not the same thing." {n}Her lip curls.{/n} "Yozz thought he was very clever, getting Baphomet's daughter for an advance payment. He did not know that Father was clearing a shelf."''',
       c("Continue", "canary")),
    hz("canary", '''"You carried my gift to her." {n}Her eyes go bright and hard.{/n} "In Colyphyr, in the mines. The dead canary. I put a little of my voice in its beak and a spear of fire in its heart, and I wrapped it in white ribbon, the way you wrap a present for someone you love."
"I wish I had seen her face. Tell me. Did she scream?"''',
       c('"She laughed, actually."', "laughed", requires=(CANARY,)),
       c('"I didn\'t carry it."', "didnt", forbids=(CANARY,)),
       c('"She was too busy trying to kill me."', "busy", requires=(CANARY,))),
    hz("laughed", '''{n}She stares at you. Then, to your surprise, she laughs too, harshly, a sound like a cough.{/n}
"Of course she did. She always laughed when I hurt her. It was how she told me I had not hurt her enough." {n}She shakes her head.{/n} "Belch of Lamashtu. I miss hating her properly. It kept me warm."''',
       c("Continue", "now")),
    hz("busy", '''"Good." {n}She sounds genuinely pleased.{/n} "I hope it distracted her. I hope it was the thing she was thinking about when you killed her. A dead bird from her little sister, in her face, with a ribbon on it."''',
       c("Continue", "now")),
    hz("didnt", '''"No?" {n}Her eyes narrow.{/n} "Then somewhere in the Abyss there is a box with a dead canary in it and my voice in its beak, waiting for my sister, who is dead anyway." {n}She considers it.{/n} "That is almost better. Let it wait. Let it wait for a thousand years."''',
       c("Continue", "now")),
    hz("now", '''"She is dead, and I have what she wanted: his regard, such as it is, and all of his silence." {n}A pause.{/n} "It is not as nice as she thought it would be. I should like to tell her so. It would make her furious."''',
       c("Continue", "back", requires=(HEPZ_BACK,)),
       c("[Leave it there.]", flags=(SISTER,), forbids=(HEPZ_BACK,))),
    hz("back", '''"And then, of course, I can tell her so. Because she is not dead. Because somebody went into Father's Labyrinth and stole her back out of it." {n}She looks at you, long and level.{/n}
"I know it was you. I do not ask how. I will say this once, mortal. What is between her and me is ours. You will not make us sit at one table and smile. You will not try to settle it. If she ever comes near my box, I will kill her again myself, and this time I will do it properly."''',
       c('"Understood."', flags=(SISTER,)),
       c('"You might find you have things to say to each other."', "back2")),
    hz("back2", '''"We have things to say to each other." {n}Her smile is all teeth.{/n} "We have been saying them for a hundred years, mostly with spears. Do not meddle, mortal. You would lose more than an ear."''',
       c("[Leave it, for now.]", flags=(SISTER,))),
], requires=(FATHER,), forbids=(SISTER, ALLY), delay=24)


# --- 5. Yozz, and the leash. -----------------------------------------------------------------------------------------------

beat(H + "beat.yozz", "Property", '"What became of Yozz?"', [
    hz("start", '''"Yozz?" {n}Her face goes still with a kind of distaste, the way a cat's face goes still when you mention a bath.{/n} "Yozz is not a subject for the street, mortal. If he is alive, he is wishing he were not. If he is dead, he is still mine. Either way he is exactly where I put him."
"Why do you ask? Did you want him? You could have killed him in his hall, you know. I would have let you. I was standing in the projection circle, hoping."''',
       c('"I wanted to know what you did with the leash."', "leash"),
       c('"I wanted to know what you do with things you own."', "own")),
    hz("leash", '''"The leash." {n}She is quiet for a moment.{/n} "Gold links, each one as long as a finger. Yozz had my name engraved on the clasp so that his guests could read it while he walked me past their tables. *Horzalah.* The one time anybody spelled it right."
"When he became mine, I had him wear it. Around his neck, clasp at the front, so that my name was under his chin. He wore it for a month. Then I had the dresser melt it down." {n}She touches the high collar.{/n} "The buckles on this are made from it. I wear it every day. It is the only piece of that year I kept."''',
       c('"Why keep any of it?"', "keep"),
       c('"It suits you better than it suited him."', "suits")),
    hz("own", '''"I keep them." {n}She says it as if it were obvious.{/n} "That is what owning is. You keep a thing. You do not throw it away when it is dull, or give it away when it is inconvenient, or leave it in a cell while you are curious how long it will last." {n}Her voice goes very even.{/n}
"My father owns things the way a fire owns a house. I own them the way a miser owns a coin. I know which I prefer."''',
       c("Continue", "leash")),
    hz("keep", '''"So that I remember." {n}Her fingers find the buckle under her jaw.{/n} "Everything I own, I took. The Guild, from Yozz. My power, back from my father. My name, off my sister. If I throw away the leash, I forget that I took this too. And then one day someone will come with another one, and I will not know what it is."''',
       c("[Leave her with it.]", flags=(YOZZ,))),
    hz("suits", '''{n}Her eyes narrow, and for a moment you think you have made a mistake. Then her mouth curves at one corner.{/n}
"Everything suits me better than it suited him. His Guild. His dresser. His chair." {n}She looks at the side of your head.{/n} "His bounty on you. I wore that very well, until you took it off me."''',
       c("[Leave her with it.]", flags=(YOZZ,))),
], requires=(TESTED,), forbids=(YOZZ,), delay=24)


# --- 6. The notice board, and her people in Drezen. ------------------------------------------------------------------------

beat(H + "beat.board", "The notice board", '"How does your Guild work, exactly?"', [
    hz("start", '''"You want to know how to hire a knife." {n}She seems pleased by the question, the way a craftsman is pleased when somebody asks about the tools.{/n}
"There is a board at our door. Anyone may post a contract there, if they can pay the posting fee, which is high, and the Guild's share, which is higher. Anyone may take a contract down, if they are a member, which is hard. The contract says who, and how, and how much. It never says why. We do not care why."
"That is the whole secret of the Guild, mortal. We do not care why."''',
       c('"Who posted the contract on me?"', "who"),
       c('"How many are on the board right now?"', "how_many")),
    hz("who", '''"I did." {n}She says it without a flicker.{/n} "Through a third party, so it would look as if I were only the Guild. And before that Yozz posted one, and before that somebody in Mendev whose name I am not going to tell you, and there is one from a cult of Deskari that was posted in Kenabres before the Wardstone fell and has been paying interest ever since."
"They are all down now. I took them down myself. I pinned your ear over them." {n}A thin smile.{/n} "If anyone posts another, it will be refused at the door. I have not told the masters why. We do not care why."''',
       c("Continue", "agent")),
    hz("how_many", '''"Forty-one this morning. Three of them in your crusade." {n}She smiles at your face.{/n} "No, not you. Not any of your companions either; I looked. A quartermaster in Nerosyan who has been selling boots with paper soles. A Mendevian lord whose wife is very tired of him. A priest." {n}She shrugs.{/n} "Do you want their names? You may have them. It will cost you nothing. I only want to watch you decide."''',
       c('"Tell me."', "names"),
       c('"No. Your business is your business."', "agent")),
    hz("names", '''{n}She tells you. The quartermaster you have heard of; the lord you have met twice; the priest you know by sight. She watches your face the whole time, as if every flicker on it were a coin being counted.{/n}
"There. Now you know, and now you have to decide whether to do anything about it, and every one of them is your problem and not mine." {n}She looks delighted.{/n} "That is the other secret of the Guild, mortal. Knowing is a knife too."''',
       c("Continue", "agent")),
    hz("agent", '''"And you have been wondering, all this time, who in your city writes to me." {n}She has not stopped smiling.{/n} "The dwarf worked out there was someone. He was right. There is more than one."''',
       c('"Tell me who."', "agent_who"),
       c('"Keep them. As long as they only watch."', "agent_keep")),
    hz("agent_who", '''"No." {n}There is nothing coy in it at all.{/n} "You may have the names on the board. You may have my Guild's rates, and its history, and the name of every master who ever tried my chair. You may not have my people." {n}She holds your eyes.{/n}
"Everything in Drezen that is mine stays mine, mortal. Including the one who watches your ear. If you ever find them, and you might, you will leave them where they are. Or you will find out how I am when I am robbed."''',
       c('"Fair."', flags=(BOARD, AGENT)),
       c('"I\'ll find them."', flags=(BOARD, AGENT))),
    hz("agent_keep", '''{n}She tilts her head, as if she had expected an argument and been denied it.{/n} "Only watch. Yes. They only watch. It would be very bad manners for a guest to kill the host's servants." {n}A beat.{/n} "I am a very well-mannered guest."''',
       c("[Take that for what it's worth.]", flags=(BOARD,))),
], requires=(TESTED,), forbids=(BOARD,), delay=24)


# --- 7. The Lady in Shadow's city. -----------------------------------------------------------------------------------------

beat(H + "beat.lady", "Her city", '"Does the Lady in Shadow know what you do in her city?"', [
    hz("start", '''"Nocticula knows everything that is done in Alushinyrra, mortal, and a great deal that is only thought about." {n}She says the name carefully, the way people in the Isles say it: politely, and not too often.{/n}
"The Guild exists because she allows it to. It is very simple. We keep our knives pointed outward, at the rest of the Abyss and at fools like you, and never at her court. We pay our taxes to her treasurers on the day. And when her court wants someone dead who cannot be seen to die by her hand, a contract appears on our board, and nobody asks who posted it."''',
       c('"And if she ever wants you dead?"', "dead"),
       c('"Have you met her?"', "met")),
    hz("dead", '''"Then I am dead, and my masters will fight over the chair, and she will choose the winner by watching which of them looks most frightened of her." {n}She shrugs.{/n} "Everyone in Alushinyrra lives at her pleasure. The difference between us is that I know it. Yozz did not. He thought he was clever enough to be tolerated. Nobody is clever enough. You are only useful enough, or you are not."''',
       c("Continue", "end")),
    hz("met", '''"Once. Across a hall, at a reception, when I was on Yozz's leash." {n}Her voice goes very flat.{/n} "She looked at me for about as long as my father ever did. Then she said something to the incubus beside her, and he laughed, and she went on to the next thing." {n}A pause.{/n} "I have spent a great deal of time wondering what she said. I think it was: *Baphomet's leftovers.* I think I would have said the same."''',
       c("Continue", "end")),
    hz("end", '''{n}She looks at you sidelong.{/n} "They say she has taken an interest in you. That you went into her palace and came out with all your fingers. That she talks about the crusader who makes her laugh." {n}Her eyes go to the side of your head.{/n}
"If you are her toy, mortal, I will not be jealous. One does not envy the Lady in Shadow; one only gets out of her way. But I will know. And I will keep my box somewhere she cannot find it."''',
       c('"Keep it wherever you like."', flags=(LADY,)),
       c('"I\'m nobody\'s toy."', "toy")),
    hz("toy", '''"Everyone is someone's toy in the Isles, mortal. The trick is choosing whose." {n}She almost smiles.{/n} "You chose badly, of course. You chose the one who cuts."''',
       c("[Let her have that.]", flags=(LADY,))),
], requires=(BOARD,), forbids=(LADY,), delay=24)


# --- 8. The dwarf. ---------------------------------------------------------------------------------------------------------

beat(H + "beat.dwarf", "The dwarf", '"You\'re watching Greybor."', [
    hz("start", '''{n}She is. Across the street, by the tavern door, a dwarf with a pipe is watching her back, with exactly the same expression.{/n}
"I am watching the dwarf," {n}she agrees.{/n} "The dwarf is watching me. It is a professional courtesy. If either of us stopped, the other would take it as an insult."''',
       c("Continue", "betrayed", requires=(MET_A,)),
       c("Continue", "betrayed_b", requires=(MET_B,), forbids=(MET_A,)),
       c("Continue", "never", forbids=(MET_A, MET_B))),
    hz("betrayed", '''"He took my contract on you, and my gold, and my confidence, and he led me to the Dry Crossroads by the nose, and at the end of it he stood over me filling his pipe and told me my three mistakes, in order, like a schoolmaster." {n}Her teeth show.{/n} "I have never been so humiliated in my life, and my life has been one long humiliation. I want his head, mortal."''',
       c("Continue", "demand")),
    hz("betrayed_b", '''"He sold you to me, and then he sold me to you, and he did it all without once raising his voice." {n}Something like admiration moves across her face, and she smothers it.{/n} "I have hired a great many knives. That one I should have hired properly. I want his head anyway, mortal. It is a matter of principle."''',
       c("Continue", "demand")),
    hz("never", '''"We have never met, the dwarf and I. But every knife in the Abyss knows his name, and his rates, and that he has never once broken a contract he did not mean to break." {n}Her lip curls.{/n} "An assassin with a reputation to protect, standing at the Knight Commander's back. There is nothing in the Abyss more tiresome. I want his head, mortal, for the principle of the thing."''',
       c("Continue", "demand")),
    hz("demand", '''"Give me the dwarf." {n}She says it lightly, as if asking for the salt.{/n} "He is not one of your precious crusaders. He is a sellsword who would sell you tomorrow for a better offer; he has said so to your face. Give him to me, and I will make it quick, and I will think better of you for the rest of your short life."''',
       c('"No. He\'s under my protection."', "no"),
       c('"Take it up with him. He\'ll enjoy that."', "him"),
       c('[Trickster] "I\'ll give you something better. His pipe."', "pipe")),
    hz("no", '''"Under your protection." {n}She lets the words sit in the air for a while, examining them.{/n} "A dwarf who would sell you. Under the protection of the {mf|man|woman} he would sell." {n}She shakes her head.{/n}
"You are the strangest owner I have ever met, mortal. Very well. He keeps his head. I keep watching it. And I will think, occasionally, about how much I would have enjoyed taking it."''',
       c("[Leave them watching each other.]", flags=(DWARF,))),
    hz("him", '''{n}She looks across at Greybor. Greybor, who has heard every word, raises his pipe to her in a small salute.{/n}
"He would enjoy it." {n}She sounds almost wistful.{/n} "That is the trouble. He would enjoy it, and I would probably lose, and then he would charge you for the cleaning." {n}She turns back to the Storyteller's shelves.{/n} "Another time. When I am less tired and he is less smug."''',
       c("[Leave them watching each other.]", flags=(DWARF,))),
    nar("pipe", '''{n}Greybor's pipe is on the step beside him while he refills his pouch. You walk across the street to ask him about the weather in the Worldwound, which he tells you at some length, and when you come back the pipe is in your sleeve and he has not yet noticed that his hand is closing on nothing.{/n}
{n}Horzalah takes it from you with two fingers, as if it were something dead she had been given to identify.{/n}''',
        c("Continue", "pipe2")),
    hz("pipe2", '''"His pipe." {n}She turns it over. Then she laughs, properly, loud enough that Greybor looks up, looks at his empty hand, looks at her, and goes very still.{/n}
"You stole the dwarf's pipe for me. In the street. In front of him." {n}She puts it inside her collar, against her throat.{/n} "It is the stupidest gift anyone has ever given me, and I would not trade it for his head. He will be looking for it for a week. He will know exactly where it is, and he will never ask for it back, because then he would have to admit I have it."''',
       c("[Leave before Greybor crosses the street.]", flags=(DWARF, P_PIPE))),
], requires=(GREY_IN,), forbids=(DWARF, GREY_DEAD, GREY_KICKED), delay=24)


# --- 9. A knife lesson. ----------------------------------------------------------------------------------------------------

beat(H + "beat.knife", "Hold it like this", '"Show me how you do it."', [
    hz("start", '''"Do what?" {n}She is cleaning her nails with a knife so thin you can see the light through the edge.{/n}
"Oh. That." {n}She follows your eyes to the side of your head.{/n} "You want to know how I took it without taking half your scalp with it. You want a lesson." {n}She flips the knife over and holds it out, hilt first.{/n} "Very well. Take it. Not like that. You hold it like a quill. You are going to cut someone, mortal, not write them a letter."''',
       c("[Hold it the way she shows you.]", "hold")),
    nar("hold", '''{n}She stands behind you and corrects your grip with her own fingers over yours, one knuckle at a time. Her claws rest on the backs of your hands, very lightly, and her breath is warm on the scar where your ear was.{/n}
"Wrist loose," {n}she says.{/n} "Loose. You are not holding a sword. A sword is a promise that you will hurt somebody. A knife is a secret." {n}Her hand closes over yours and moves it in a short, flat arc through the air.{/n} "There. That is an ear. Now take mine."''',
        c("Continue", "take")),
    hz("take", '''{n}She steps round in front of you, and draws a second knife from somewhere in her collar, and holds it loosely at her side.{/n}
"Take my knife off me. Not my ear, mortal; I am fond of my ears. My knife. If you get it, I will tell you a secret. If you do not, I will leave a mark somewhere you will have to explain to your quartermaster."''',
       c("[Go for her knife.]", check=dict(Skill="SkillThievery", DC=24, Success="won", Failure="lost")),
       c('"I\'ll pass on the mark."', "pass")),
    hz("won", '''{n}It is half luck and half something she taught you a minute ago. Your hand goes low, as if for her wrist, and when she turns the blade to meet it your other hand is already closing on the hilt, and then the knife is yours and she is looking at her own empty fingers.{/n}
{n}She does not look angry. She looks as if someone had set a very good dish in front of her.{/n} "Again," {n}she says.{/n} "No. Not again. Keep that one. It was a secret; you took it; it is yours."''',
       c('"And my secret?"', "secret")),
    hz("secret", '''{n}She leans in, close enough that her mouth is at your scar, and says very quietly:{/n}
"I cut your ear with that knife. I have not cleaned it since." {n}She steps back and watches your face with enormous satisfaction.{/n} "Now you are carrying a piece of you around with a piece of me. That is how it is done, in my family. We are very romantic."''',
       c("[Put the knife in your belt.]", flags=(KNIFE, P_KNIFE))),
    hz("lost", '''{n}You are quick. She is quicker, by rather more than you would like. Her blade flicks across the back of your hand, from the knuckle almost to the wrist, a line so shallow it does not bleed until you look at it.{/n}
"There." {n}She is smiling.{/n} "Explain that to your quartermaster. Tell him a woman did it while you were trying to rob her. He will believe you; they always believe the true stories. It is the lies they check."''',
       c('"Next time."', "lost2")),
    hz("lost2", '''"Next time," {n}she agrees, and puts both knives away, and pats your cut hand as if it were a dog that had done its best.{/n} "You nearly had it, mortal. You went for the wrist. Everyone goes for the wrist. Next time go for the thing I am not looking at."''',
       c("[Nurse your hand.]", flags=(KNIFE, NICKED))),
    hz("pass", '''"Coward." {n}She says it fondly, which is somehow worse.{/n} "Very well. You may keep your hands pretty. Some of us like to have a few things about us that nobody has marked yet." {n}She takes her knife back, hilt first, the way she gave it.{/n}''',
       c("[Keep your hands pretty.]", flags=(KNIFE,))),
], requires=(TESTED,), forbids=(KNIFE, ALLY), delay=24)


# --- 10. The ear. ----------------------------------------------------------------------------------------------------------

beat(H + "beat.ear", "Hers", '"Stop staring at my head."', [
    hz("start", '''"I will stare at whatever I like. It is mine." {n}She reaches up without asking and pushes your hair back from the scar with two fingers, and studies it the way a jeweller studies a setting.{/n}
"It is healing better now. The edge was ragged at first; your surgeon has no idea what he is doing. I sent him a note." {n}She lets your hair fall back.{/n} "He will not trouble you again. No, I did not hurt him. I only told him whose it was."''',
       c("Continue", "late", requires=(LATE,)),
       c("Continue", "road", requires=(MET_A,), forbids=(LATE,)),
       c("Continue", "road", requires=(MET_B,), forbids=(LATE, MET_A)),
       c("Continue", "room", forbids=(LATE, MET_A, MET_B))),
    hz("late", '''"Your soldiers talk about it, you know. The night the demon came through the wall. They make me much taller in the telling, and give me more teeth." {n}She sounds pleased.{/n} "In the barracks by the east gate there is a new game with dice, where the one who loses has to go to bed with one ear covered. They call it *Horzalah's*."''',
       c("Continue", "ask")),
    hz("road", '''"The dwarf tells it in the tavern, sometimes, when he has been drinking. How the beaten demon took a piece of the Knight Commander off with a knife, on the road, and the Knight Commander thanked her for it." {n}She shakes her head.{/n} "He tells it very badly. He makes me sound grateful."''',
       c("Continue", "ask")),
    hz("room", '''"Your guards tell it in the barracks, the night a demon came through the wall and took a piece of the Knight Commander home with her. They argue about which ear. Half of them say the right." {n}She sounds offended on your behalf.{/n} "I have had a note sent to the barracks. They say the left now."''',
       c("Continue", "ask")),
    hz("ask", '''"Does it hurt?" {n}She asks it abruptly, as if the question had got out before she could stop it.{/n}''',
       c('"Only when you look at it like that."', "flirt"),
       c('"Every day. I don\'t mind."', "honest"),
       c('"I don\'t hear as well on that side."', "hear")),
    hz("flirt", '''"Like what?" {n}Her eyes narrow.{/n} "Like I own it? I do." {n}And then, before you can answer, she puts her mouth to the scar, briefly, in the middle of the street, and is gone back to her shelves before the soldier coming up the road has decided what he saw.{/n}''',
       c("[Stand there for a while.]", flags=(EAR_SEEN,))),
    hz("honest", '''{n}She is quiet.{/n} "Good. It should. Things that are given should hurt a little; it is how you know they were not stolen." {n}She touches the edge of it, very lightly.{/n} "I will think of that. Every day, when it hurts you, I will think of that, in my hall, among my contracts. It will be very distracting. You are a terrible influence."''',
       c("[Let her touch it.]", flags=(EAR_SEEN,))),
    hz("hear", '''"Then stand on my left," {n}she says, as if it were obvious.{/n} "I will be on your deaf side, and no one else will be able to get there without going round me. It is a very good place for a knife." {n}She moves, as she says it, so that she is standing exactly there.{/n} "See? You did not even hear me do it."''',
       c("[Leave her where she is.]", flags=(EAR_SEEN,))),
], requires=(TESTED,), forbids=(EAR_SEEN, ALLY), delay=24)


# --- 11. The Threshold, and Deskari's army. --------------------------------------------------------------------------------

beat(H + "beat.threshold", "The rest of the Abyss", '"The crusade marches on the Threshold soon."', [
    hz("start", '''"I know. Everyone in the Abyss knows. There are bets being placed in my own hall on how many days you will last." {n}She says it without any particular feeling.{/n} "I have not placed one. It would be a conflict of interest."''',
       c('"Will you come?"', "come"),
       c('"Will you still want Deskari\'s army when he\'s gone?"', "army")),
    hz("come", '''{n}She looks at you as if you had asked her to dance at a funeral.{/n}
"To the Threshold? To fight Deskari's rabble in the mud beside a thousand crusaders who would rather put a sword in me than in him?" {n}She laughs, not unkindly.{/n} "No, mortal. I am an assassin, not a soldier. I do not stand in lines. I will be in my hall, with your ear, listening to the bets."
"And when you come back, I will come and look at the rest of you, to see what the war took. Do not let it take anything of mine."''',
       c("Continue", "promise")),
    hz("army", '''{n}That surprises a real laugh out of her.{/n} "You remember that. I shouted it at you on the road, when I thought I had you: that I would rout the armies of Alushinyrra and cut down Deskari's lackeys and take his army for myself."
"Yes. I still want it. I want everything. Wanting is free." {n}Her eyes glint.{/n} "If you kill the Locust Lord, mortal, his rabble will scatter across half the Abyss looking for a master. Some of them will come to Alushinyrra. Some of them will come to my board. I will be very busy after your war, and very rich. You may consider it a gift to myself, from you."''',
       c("Continue", "promise")),
    hz("promise", '''{n}She reaches out and straightens the collar of your coat, as if you were a door she was checking on her way out.{/n}
"Come back with everything else attached, mortal. I have one piece of you. I want the rest to stay where I can come and take it when I choose."''',
       c('"I\'ll come back."', flags=(WAR,)),
       c('"And if I don\'t?"', "if")),
    hz("if", '''"Then I will go to the Worldwound myself and look for what is left, and I will be very angry about it." {n}Her voice is flat and completely certain.{/n} "I do not lose things, mortal. I am Baphomet's daughter. We lose everything else, but we do not lose what is ours."''',
       c("[Believe her.]", flags=(WAR,))),
], requires=(COMMITTED,), forbids=(WAR,), delay=24)


# --- 12. The ribbon. -------------------------------------------------------------------------------------------------------

beat(H + "beat.ribbon", "The bow", '"Teach me to tie that bow."', [
    hz("start", '''"The bow?" {n}She glances at the white ribbon threaded through her collar today, a thin band of it, tied at the side of her throat in a perfect bow with the ends cut on the slant.{/n} "Why?"''',
       c('"So I can send you something back."', "back"),
       c('"Because you tie it every morning, and I want to know how it goes."', "morning")),
    hz("back", '''"Send me something." {n}She looks at you with suspicion, and then with something that is not suspicion at all.{/n} "Nobody sends me things. They send me contracts, and heads, and debts. My sister sent me a cell." {n}She pulls the ribbon loose from her collar in one movement and holds out the end.{/n} "Very well. Hold it. No, like a knife: loose."''',
       c("Continue", "tie")),
    hz("morning", '''{n}Her eyes narrow.{/n} "You watch me dress." {n}It is not a question.{/n} "In Yozz's house there were people whose whole work was to watch me dress, and make sure I did it the way he liked." {n}She pulls the ribbon loose from her collar in one movement.{/n} "You are the first who wanted to learn how it goes. Hold it. No, like a knife: loose."''',
       c("Continue", "tie")),
    nar("tie", '''{n}She shows you. It takes longer than it should, because your fingers are clumsy and hers keep taking them and moving them where they ought to go, and neither of you hurries. The loop, the turn, the loop again. A pull that must be exactly as hard as it needs to be and no harder.{/n}
{n}At the end she takes a small knife from her collar and cuts both ends on the slant, one stroke each, so they will not fray.{/n}''',
        c("Continue", "tied")),
    hz("tied", '''{n}She looks at the bow you have made. It is lopsided. She does not retie it.{/n}
"Terrible," {n}she says.{/n} "I am going to wear it anyway. In my hall. On the collar. Every master in the Guild will see that the ribbon is tied badly, and none of them will dare to mention it, and they will all wonder who did it, and I will not tell them." {n}She threads it back through her collar, lopsided bow and all.{/n} "Get better at it. I intend to make you practise."''',
       c('"Every morning?"', flags=(P_RIBBON,)),
       c("[Straighten the bow a little.]", flags=(P_RIBBON,))),
], requires=(CHAMBER,), forbids=(P_RIBBON,), delay=24)


# --- 13. A crusader who spits. ---------------------------------------------------------------------------------------------

beat(H + "beat.spit", "In the street", '"What happened here?"', [
    nar("start", '''{n}There is a knot of people in front of the Storyteller's shelves, and a young crusader in the middle of it with his sword half drawn and his face white, and Horzalah in front of him, perfectly still, with spit on her cheek.{/n}
{n}Nobody breathes. The crusader is shaking. He came from Kenabres, you learn later; his mother and sisters died when the Wardstone fell, under a sky full of demons. He did not choose which one to spit at. This was the one standing in the street.{/n}''',
        c("Continue", "her")),
    hz("her", '''"Your soldier has something to say to me, mortal." {n}She does not wipe her face. She does not take her eyes off him.{/n} "He has said it. I am waiting to find out whether he wants to say anything else, or whether he would like to keep his tongue."''',
       c('[Back her] "Soldier, sheathe that. She\'s here as my guest. You\'ll apologise, or you\'ll answer to me."', "backed"),
       c('[Let her handle it] "It\'s your face. Your answer."', "hers"),
       c('[Step between them] "Nobody is cutting anybody in my street."', "between")),
    nar("backed", '''{n}The boy looks at you as if you had struck him. Then he sheathes the sword, and says something that might be *sorry* to the cobbles, and goes, fast, with his friends around him.{/n}
{n}Horzalah wipes her cheek at last, with one knuckle, slowly.{/n}''',
        c("Continue", "backed2")),
    hz("backed2", '''"You shamed him for me. In front of his friends." {n}She studies the wet knuckle.{/n} "He will hate you for it now, and me twice as much, and one day he will try again, better armed." {n}She shrugs.{/n} "I know that face. I wore it for a hundred years, looking at my sister. It is a good face. It gets things done."
"Thank you. I will not say that again, so do not ask."''',
       c("[Don't ask.]", flags=(SPIT,))),
    nar("hers", '''{n}She moves once. The boy's sword is in the gutter, and the boy is on his knees in front of her, with her fingers under his chin, tipping his face up to hers. She has not drawn a knife. She does not need to.{/n}
"You lost your family to my kind," {n}she says, quite gently.{/n} "I can see it. I can smell it on you. So listen. Your family were not killed by me. Mine were not killed by you. Next time, find the right demon, and spit at that one, and do it with a better weapon than your mouth."''',
        c("Continue", "hers2")),
    hz("hers2", '''{n}She lets him go. He picks up his sword and does not look at her, and his friends take him away, and the street starts breathing again.{/n}
{n}Horzalah wipes her cheek with one knuckle.{/n} "That," {n}she says to you,{/n} "was the most mercy I have shown anybody in a hundred years. I did it because it was your street, and you would have been tiresome about blood on it. Do not count on it twice."''',
       c("[You won't.]", flags=(SPIT,))),
    nar("between", '''{n}You step in between them, and for a heartbeat both of them look at you with the same expression, the one people wear when they have been denied something they badly wanted.{/n}
{n}The boy sheathes his sword first. His friends take him away. Horzalah wipes her cheek with one knuckle.{/n}''',
        c("Continue", "between2")),
    hz("between2", '''"You stood in front of my knife for a boy you have never met." {n}She considers it.{/n} "And in front of his sword for a demon he has every reason to hate. You are a very strange sort of wall, mortal."
"Do not do it again. Next time one of us might not stop, and I would hate for it to be me."''',
       c("[Promise nothing.]", flags=(SPIT,))),
], requires=(), forbids=(SPIT,), delay=36)


# --- 14. The collar, afterwards. -------------------------------------------------------------------------------------------

beat(H + "beat.bare", "Bare", '"You\'re not wearing the collar."', [
    hz("start", '''{n}She is not. The high black leather is gone. The scar is there for anyone who passes to see: a band of pale, glossy skin all round her throat, two fingers wide, with the ghost of a buckle pressed into one side of it. The soldiers going by look at it and then, very quickly, at the cobbles.{/n}
"No," {n}she says.{/n} "I am not."''',
       c('"Why?"', "why"),
       c("[Say nothing. Look at her, not the scar.]", "look")),
    hz("why", '''"Because everyone in this street has seen it now. I let them. They looked, and they looked away, and nothing happened." {n}Her fingers move to her throat, and stop, and come down again.{/n}
"In Alushinyrra I wear it. There, it would be a weakness, and weaknesses are posted on the board with a price beside them. Here..." {n}She shrugs.{/n} "Here it is only a scar. On a woman who is standing in your street because she chooses to."''',
       c("Continue", "end")),
    hz("look", '''{n}You look at her. Her face, which is proud and bony and a little hungry, as it always is; her eyes, which are watching you watch her. Not the scar.{/n}
{n}After a while she lets out a breath through her nose, the kind that is almost a laugh.{/n} "You are still doing it," {n}she says.{/n} "In Yozz's hall, you looked at it and not at the seals. Now you look at me and not at it. You are a very contrary sort of mortal."''',
       c("Continue", "end")),
    hz("end", '''"The dresser is making me a new collar. For the Guild. It will have a ribbon on it, tied badly." {n}Her eyes glint.{/n} "But not here. You may tell your soldiers that. In Drezen, Baphomet's daughter goes about bare-throated, like a woman who has nothing left to be sold for."''',
       c("[Tell them.]", flags=(BARE,))),
], requires=(CHAMBER,), forbids=(BARE,), delay=36)


# --- 15. Hunger. -----------------------------------------------------------------------------------------------------------

beat(H + "beat.hunger", "Thin", '"When did you last eat?"', [
    hz("start", '''{n}She looks at you as if you had asked her when she last bled.{/n}
"Why?"''',
       c('"You were half-starved in Yozz\'s hall. You\'re not much better now."', "yozz"),
       c('[Hold out the bread and sausage you brought from the cookhouse.] "No reason."', "food")),
    hz("yozz", '''{n}Her mouth tightens.{/n} "Yozz liked his concubine thin. He said it showed off the seals. He said a daughter of Baphomet with meat on her bones would look like any other demon, and he had not paid for any other demon." {n}She shrugs, a sharp movement of sharp shoulders.{/n}
"So I was fed what the dogs did not want, and I learned to live on it, and I am still alive. Everything he did to me, I lived through. I do not need your cookhouse."''',
       c('[Hold out the bread and sausage anyway.]', "food"),
       c('"Then don\'t eat it for me. Eat it because he\'d hate it."', "spite")),
    hz("spite", '''{n}Something moves at the corner of her mouth.{/n} "Because he would hate it." {n}She considers that as if it were a contract with an unusually attractive clause.{/n} "He would. He would hate it very much. He would say I was spoiling the lines." {n}She holds out her hand.{/n} "Give it here."''',
       c("[Give it to her.]", "eat")),
    nar("food", '''{n}She looks at the bread and the sausage in your hand without moving. Then she takes them, not quickly, the way a cat takes something from a hand it does not trust, and turns her back on the street to eat.{/n}''',
        c("Continue", "eat")),
    nar("eat", '''{n}She eats the way people eat who have been hungry for years and will not let anyone see it: small bites, very fast, her shoulders hunched round the food, her eyes on the street the whole time in case someone comes to take it. The sausage goes first. Then the bread, all of it, down to the crumbs, which she picks off her leathers with a licked fingertip.{/n}
{n}When she turns back her face is perfectly composed, and there is a smear of grease at the corner of her mouth that she does not know about.{/n}''',
        c("[Tell her about the grease.]", "grease"),
        c("[Wipe it away with your thumb.]", "thumb", forbids=(ALLY,))),
    hz("grease", '''"Where?" {n}She wipes the wrong side, and then the right one, and glares at you as if it were your fault.{/n} "You will not mention this to anyone. Not the dwarf. Not the old elf. If my masters hear that Baphomet's daughter eats sausage off a crusader's hand in the street, I will have to kill all of them, and it will take a week."''',
       c('"Same time tomorrow?"', "tomorrow")),
    hz("thumb", '''{n}She goes absolutely still when your thumb touches her mouth. For a heartbeat you think you have made a mistake, and then her lips part, very slightly, and she lets you do it.{/n}
"You are very free with your hands for someone who was taught to wait," {n}she says, quietly.{/n} "I will allow it. This once. Because it was grease, and not my collar."''',
       c('"Same time tomorrow?"', "tomorrow")),
    hz("tomorrow", '''"Tomorrow." {n}She turns the word over.{/n} "Bring more sausage. And none of that grey bread your soldiers eat; it tastes of the barracks." {n}A pause.{/n} "And do not stand there watching me eat it. It is indecent."''',
       c("[Promise to look at the street.]", flags=(HUNGER,))),
], requires=(), forbids=(HUNGER,), delay=18)


# --- 16. One of thousands. -------------------------------------------------------------------------------------------------

beat(H + "beat.thousands", "One of thousands", '"How many brothers and sisters do you have?"', [
    hz("start", '''"Nobody knows. Father least of all." {n}She says it lightly.{/n} "He spawns us the way a river spawns fish. Nephilim, cambions, beasts with his horns and a mortal's eyes. Some of us are born in his temples, to priestesses who asked for the honour. Some of us are made in his pens. Most of us die before we learn to talk, because the others eat them."
"Hepzamirah sacrificed our mother to him to get his attention. I suppose I should have thought of that first."''',
       c('"He told me he could spawn hundreds more."', "hundreds", requires=(NAMED,)),
       c('"How do you stand out, among so many?"', "stand_out"),
       c('"Do any of the others know you?"', "others")),
    hz("hundreds", '''"Hundreds. Thousands." {n}She nods.{/n} "Yes. He would say that. It is the truest thing he has ever said about us, and he says it to strangers, to make them understand how little his children cost him."
"When I was small I used to think that meant each of us was worth very little. Now I think it means something else." {n}Her eyes are hard and bright.{/n} "If he can make a thousand of me, then the one that is standing here is the one that got out of his hands. There is only one of *those*."''',
       c("Continue", "end")),
    hz("stand_out", '''"You do not stand out. You survive, and the ones who survive are the ones people remember, because there is nobody left to remember instead." {n}She shrugs.{/n} "Hepzamirah was the cleverest of us. I was the strongest. There was a boy with a bull's head and our father's eyes who was the kindest, and we all agreed that it was a shame about him, afterwards."''',
       c("Continue", "end")),
    hz("others", '''"Some. There are three or four of my brothers in the Abyss who send me assassins every few years, out of habit, and I send some back. There is a sister in Absalom who pretends to be a mortal and sells perfume. I sent her a canary too, once, and she sent me back a bottle of something that took the skin off my hands." {n}Her mouth curves.{/n} "I liked her for that. I still send her a card at the winter solstice."''',
       c("Continue", "end")),
    hz("end", '''{n}She looks down the street, at the soldiers and the carts and the ordinary noise of your city.{/n}
"You mortals have one mother and one father, most of you, and you think they owe you something. It must be very restful." {n}She glances at you.{/n} "Do not tell me about yours. I will only be jealous, and then I will be cruel about them, and you will stop bringing sausage."''',
       c("[Tell her nothing about your parents.]", flags=(THOUSANDS,)),
       c('"Mine are dead. You can be as cruel as you like."', "dead")),
    hz("dead", '''{n}She is quiet for a moment, which is not what you expected.{/n}
"Then we are both orphans, in our way. Yours died. Mine is only indifferent." {n}She tilts her head.{/n} "I think yours did better. At least they had the manners to go."''',
       c("[Let that stand.]", flags=(THOUSANDS,))),
], requires=(FATHER,), forbids=(THOUSANDS, ALLY), delay=24)


# --- 17. The Ivory Labyrinth. ----------------------------------------------------------------------------------------------

beat(H + "beat.labyrinth", "Her cell", '"I\'ve walked the Ivory Labyrinth."', [
    hz("start", '''{n}Her head turns, very slowly.{/n} "Have you." {n}It is not a question.{/n} "And come out again. Most people do not. Most people do not want to, after a while; that is what it is for."
"Did you see my cell? No. You would not know it. It is on the third turning from the jailers' hall, behind a wall that moves on the hour. It has a floor of bone and a ceiling you cannot see, and in the dark the walls tell you what you did wrong, in your father's voice, over and over, until you believe them."''',
       c('"How long were you there?"', "long"),
       c('"And he walked past it, while I was there. He\'s very much alive, and very busy."', "father")),
    hz("long", '''"Long enough to stop counting." {n}She says it without any particular feeling.{/n} "Hepzamirah came to visit, the first year, to tell me how she was doing. Then she stopped coming. I think she forgot I was there. I think that was the cruellest thing she ever did to me, and she did not even do it on purpose."''',
       c("Continue", "jailers")),
    hz("father", '''"Alive and busy." {n}She laughs, harshly.{/n} "Yes. He is always busy. The Labyrinth is his house and his ledger and his larder. Every soul in it is his: every jailer, every prisoner, every cultist who died on his altar. He walks its halls counting what he owns."
"And he walked past my cell for years, and counted me, and went on." {n}Her fingers find her collar.{/n} "He did not answer me on the road either. He is very consistent. It is the only virtue he has."''',
       c("Continue", "jailers")),
    hz("jailers", '''"The jailers grovelled to me when I first came, you know. Baphomet's own daughter, in their care; they did not know what they were allowed to do. Then my sister told them, and they found out, and they enjoyed finding out." {n}A thin smile.{/n}
"I have their names. I have had them for a long time. One day, when I am bored, I will post them on my board, one at a time, at a very low rate, so that everyone in Alushinyrra knows how little they are worth to me."''',
       c('"Why not now?"', "now"),
       c('"Leave them. They\'re nothing to you now."', "leave")),
    hz("now", '''"Because the waiting is the best part." {n}She says it as if she were explaining a recipe.{/n} "They know I am out. They know I have a Guild. They lie awake in Father's house and listen for my knives in every corridor. I would not take that away from them for anything."''',
       c("[Leave them to their waiting.]", flags=(LABYRINTH,))),
    hz("leave", '''"Nothing to me." {n}She considers it.{/n} "You say that as if it were a kindness. It is not, to them. To be nothing to someone who owns a Guild of knives is the safest thing in the Abyss." {n}She shrugs.{/n} "Very well. They are nothing to me. I will still keep the names. Nothing is a very changeable thing."''',
       c("[Let her keep them.]", flags=(LABYRINTH,))),
], requires=(SISTER,), forbids=(LABYRINTH,), delay=24)


# --- 18. A head in a box. --------------------------------------------------------------------------------------------------

beat(H + "beat.head", "Another gift", '"Is that another box?"', [
    hz("start", '''{n}It is. It sits at her feet on the cobbles by the Storyteller's shelves: bigger than the first, round, wrapped in black paper and tied with a white ribbon in a perfect bow. The ends are cut on the slant. Something inside it has soaked a dark patch through the bottom of the paper.{/n}
"For you," {n}she says.{/n} "Every suitor in the Abyss brings a head in the end. It is the custom. I did not want you to think I had been raised badly."''',
       c('"Whose head?"', "whose")),
    hz("whose", '''"The master who tried my chair. Old, from Yozz's time, very stupid; I told you about him." {n}She nudges the box with her boot.{/n} "He said, before the whole Guild, that a woman who came home from the crusade with an ear instead of a head had gone soft. So now there is a head in a box after all, and it is his, and everyone who heard him say it has stopped saying anything at all."
"Well, mortal? Do you like it?"''',
       c('[Take it] "It\'s very thoughtful. I\'ll have it buried."', "take"),
       c('[Refuse it] "Keep it. I don\'t collect heads either."', "refuse"),
       c('"Put it on your notice board. Let the Guild look at it."', "board")),
    hz("take", '''{n}She watches you pick up the box. It is heavier than you expect. Something rolls inside it, and settles.{/n}
"Buried." {n}She sounds faintly disappointed.{/n} "Mortals always bury things. We would have boiled the skull and put it on a shelf. But it is your gift; do with it what you like." {n}She tips her head.{/n} "You did not flinch when it rolled. I noticed."''',
       c("[Carry it off to the gravediggers.]", flags=(HEAD,))),
    hz("refuse", '''"You do not collect heads." {n}She looks at the box, and then at you, and her smile is the dangerous one.{/n} "You do not collect people either. What *do* you collect, mortal? Ears?" {n}She picks the box up herself, tucks it under one arm like a parcel from the market.{/n}
"Very well. I will put it back where it came from, which is the gutter. I only brought it so you would know it was done, and why." {n}A pause.{/n} "And so you would know what happens to people who call me soft."''',
       c("[Consider yourself warned.]", flags=(HEAD,))),
    hz("board", '''{n}For a heartbeat she only looks at you. Then she laughs, a real laugh, loud enough that the Storyteller jumps.{/n}
"On the board. Among the contracts. Where every master in the Guild walks past it twice a day on the way to their dinner." {n}She picks up the box, delighted.{/n} "You have a very nasty mind for a crusader, mortal. I am going to do it tonight. I am going to put it next to your ear."''',
       c("[Watch her go, very pleased with herself.]", flags=(HEAD,))),
], requires=(COMMITTED, MASTERS), forbids=(HEAD,), delay=24)


# --- 19. The ramparts at night. --------------------------------------------------------------------------------------------

beat(H + "beat.ramparts", "What you were", '"Walk the walls with me tonight."', [
    nar("start", '''{n}She comes to the walls after the last watch has changed, when the camp below is dark except for the forges and the Worldwound is a low red stain on the northern sky. She does not ask where you want to go. She walks, and you walk beside her, on her left, and she lets you.{/n}''',
        c("Continue", "ask")),
    hz("ask", '''"Everyone knows what I was," {n}she says, after a while.{/n} "A payment. A concubine. A prisoner. A projection in a dead man's hall. I have told you all of it, and you did not look at me differently once, and I have been waiting for you to do me the courtesy of telling me what *you* were."
"Before the crusade. Before the Wound put its hand in your chest. What were you, mortal?"''',
       c('"Nobody. That was the best part."', "nobody"),
       c('"A liar, mostly. It was good training."', "liar"),
       c('"Someone who never expected any of this."', "never")),
    hz("nobody", '''"Nobody." {n}She tries the word, as she tried *horzalah* in your mouth.{/n} "I have never been nobody. I was spawned somebody's daughter, with a price already on me. I would have liked, for one day, to be nobody." {n}She looks at the red sky.{/n} "It must have been very quiet."''',
       c("Continue", "end")),
    hz("liar", '''"A liar." {n}Her mouth curves.{/n} "Yes. I thought so, on the road, when you lay there bleeding and told me a better story than the one I was going to tell. Only a liar knows how much a good story is worth." {n}She glances at you.{/n} "The difference between us, mortal, is that I lie for a living. I have never been sure what you lie for."''',
       c('"For you, lately."', "end"),
       c("Continue", "end")),
    hz("never", '''"Nobody expects any of this." {n}She shrugs.{/n} "My father did not expect me to come back from Yozz's hall. My sister did not expect her gift. Deskari did not expect you. The whole Abyss runs on people not expecting things." {n}A pause.{/n} "I did not expect you either, if you want to know. I expected your head."''',
       c("Continue", "end")),
    hz("end", '''{n}At the corner tower she stops, and puts her back to the parapet, and looks at you in the red light, saying nothing, until the sentry on the next tower has turned his back twice.{/n}
"I am not going to tell you that I love you," {n}she says at last.{/n} "Baphomet's daughters do not have the word. We have *mine*, and we have *kept*, and we have *not for sale*. You may have all three."''',
       c('"I\'ll take them."', "take"),
       c("[Take her hand, and wait.]", "hand")),
    hz("take", '''"You will take them." {n}She laughs, very low.{/n} "Of course you will. You take everything I give you, mortal. You are the worst negotiator I have ever met."''',
       c("[Walk her back along the wall.]", flags=(RAMPARTS,))),
    nar("hand", '''{n}You hold out your hand and leave it there, between you, and do nothing else. She looks at it. Then she takes it, and puts it flat against her throat, under the collar, and holds it there, and the two of you stand on the wall with the Worldwound burning low in the north until the next watch comes up the stair and goes very quickly down again.{/n}''',
        c("[Stay until she lets go.]", flags=(RAMPARTS,))),
], requires=(COMMITTED,), forbids=(RAMPARTS,), delay=24)


# --- 20. A hat. ------------------------------------------------------------------------------------------------------------

beat(H + "beat.hat", "Wear a hat", '"You said I could wear a hat."', [
    nar("start", '''{n}You are wearing one. It is a good hat, broad-brimmed, pulled down over the ruined side of your head. It cost more than you meant to pay.{/n}''',
        c("Continue", "hatter", requires=(FREED,)),
        c("Continue", "dresser", forbids=(FREED,))),
    hz("hatter", '''{n}She looks at it the way she looks at a contract she has not written. Then she reaches out and turns the brim a little, to see the stitching inside, and her face goes very still.{/n}
"You bought this from the hatter by the west gate." {n}It is not a question. The stitching is perfect.{/n} "From my dresser. From the man I gave you, and you gave away, and who went off with my gold on his wrist to sell hats to crusaders."
"And now he has sold you something to cover the ear I took." {n}She takes her hand away.{/n} "Do you know, mortal, I think that is the most elegant insult anyone has ever paid me, and nobody even meant it."''',
       c('"Do you want me to take it off?"', "off"),
       c('"He sends his regards."', "regards")),
    hz("dresser", '''{n}She looks at it, and then she snaps her fingers, and the dresser steps out from behind the Storyteller's shelves with a parcel under his arm, and his eyes on the cobbles.{/n}
"Take that thing off. It was made by a man who has never seen a knife." {n}The dresser unwraps a hat: black felt, narrow-brimmed, cut a little higher over the left side than the right, so that the brim sits clear of the scar instead of hiding it. There is a thin white band round the crown, tied at the side in a bow, with the ends cut on the slant.{/n}''',
       c("[Put it on.]", "fitted")),
    hz("fitted", '''{n}She walks round you once, as she walked round her ear on the notice board, and nods.{/n}
"There. Now it shows. A hat that hides a mark is an apology. A hat that shows it off is a boast." {n}She flicks the ribbon with one claw.{/n} "You are not apologising for anything of mine, mortal. Wear it in the street. Wear it in front of your priests."''',
       c("[Wear it.]", flags=(HAT,))),
    hz("off", '''"No." {n}She says it sharply, and then, more quietly:{/n} "No. Keep it on. It suits you, and he made it well, and I will look at it and think about what I gave away, and it will do me good." {n}She turns back to the shelves.{/n} "Just do not wear it in my hall. My masters would laugh, and then I would have to buy a great deal of ribbon."''',
       c("[Keep it on.]", flags=(HAT,))),
    hz("regards", '''"Does he." {n}Her mouth twitches.{/n} "Tell him I have not forgotten him, and that he is the only free man in Drezen I would not bother to kill. He will understand. He always understood more than Yozz gave him credit for."''',
       c("[Keep the hat.]", flags=(HAT,))),
], requires=(TESTED,), forbids=(HAT, ALLY), delay=24)


# --- 21. The cup. ----------------------------------------------------------------------------------------------------------

beat(H + "beat.cup", "A cup of wine", '"Is that for me?"', [
    hz("start", '''{n}She has two cups of wine on the edge of the Storyteller's table, one in each hand, and she holds one out to you with perfect courtesy.{/n}
"It is. One of these is poisoned. Not enough to kill you; I am not a savage. Enough to make you very sorry for a day and a night." {n}She smiles.{/n} "It is a game we play in the Guild. The apprentices play it on each other. The masters play it on the apprentices. It teaches you to look."''',
       c("[Study both cups before you choose.]", check=dict(Skill="SkillPerception", DC=22, Success="spotted", Failure="guessed")),
       c('"I\'ll drink whichever you give me."', "trust"),
       c('"Swap them, then. You drink first."', "swap")),
    hz("spotted", '''{n}The wine in the cup she is holding out has a faint oily sheen at the rim, where it has touched the glaze, like a rainbow on a puddle. The other does not.{/n}
{n}You take the other one. She watches you do it, and then she drinks the poisoned cup herself, all of it, in one swallow, and sets it down.{/n}
"Good," {n}she says.{/n} "You looked. Nephilim do not mind that one; it only gives us bad dreams. I wanted to see whether you would look, or trust me, or be clever." {n}Her eyes glint.{/n} "Looking is the right answer. Always look, mortal. Especially at me."''',
       c("[Drink your wine.]", flags=(CUP,))),
    hz("guessed", '''{n}They look exactly the same. You pick one. She raises her eyebrows, and drinks the other, and waits.{/n}
{n}Half an hour later you are sitting on the Storyteller's step with your head in your hands and the street going round you slowly, like a wheel. She sits beside you, not touching you, reading one of his books upside down.{/n}
"You guessed," {n}she says.{/n} "Guessing is the wrong answer. It will pass by morning. Next time, look."''',
       c('"Next time I\'ll look."', flags=(CUP,))),
    hz("trust", '''{n}She holds the cup out a moment longer, and then, very deliberately, she pours it out on the cobbles, where it hisses faintly, and hands you the other.{/n}
"Never say that to me again." {n}Her voice has gone flat.{/n} "Never say *whichever you give me* to anyone in the Abyss, and least of all to me. Somebody will take you at your word one day, and it will not be a game."''',
       c("[Drink the other cup.]", flags=(CUP,))),
    hz("swap", '''"Clever." {n}She sounds pleased, and a little disappointed.{/n} "The clever answer. Yozz always gave the clever answer." {n}She swaps the cups without hesitation and drinks first, and then watches you drink the one she handed back.{/n}
"The trouble with the clever answer, mortal, is that I poisoned both. A little. We will both have bad dreams tonight." {n}She sets down the cup.{/n} "I will think of you in mine. You may think of me in yours."''',
       c("[Finish your wine.]", flags=(CUP,))),
], requires=(TESTED,), forbids=(CUP, ALLY), delay=24)


# --- 22. Her question. -----------------------------------------------------------------------------------------------------

beat(H + "beat.question", "What you want", '"You\'re frowning at me."', [
    hz("start", '''"I am thinking." {n}She does not stop frowning.{/n} "You asked me what I wanted. In your room, the night after my Guild bowed to the box. I told you. And you have never once told me what *you* want, and I have been trying to work it out, the way I would work out a contract, and I cannot."
"Nobody gives anything for nothing. You gave me an ear. So, mortal: what do you want from me?"''',
       c('"Nothing you have to sell."', "sell"),
       c('"To see what you do when nobody owns you."', "see"),
       c('"You."', "you")),
    hz("sell", '''"Nothing I have to sell." {n}She tastes it.{/n} "Everything I have is for sale, mortal. The Guild, my knives, my masters, the names on my board. Everything except me." {n}Her eyes narrow.{/n} "So you are telling me it is me you want, and you are too clever to say it. I have met a great many clever people. It never ends well for them."''',
       c("Continue", "end")),
    hz("see", '''{n}She says nothing at first.{/n} "What I do when nobody owns me." {n}Her fingers find the buckle under her jaw.{/n} "I do not know. I have never been nobody's. I was Father's, and then Yozz's, and then my sister's cell's, and then the Guild's, a little, because I had to be." {n}She lets go of the buckle.{/n}
"I will let you know. You may have to wait a long time. I am told that is a thing you are good at now."''',
       c("Continue", "end")),
    hz("you", '''{n}She looks at you as if you had put a knife on the table between you, hilt towards her.{/n}
"Me." {n}The word comes out flat.{/n} "People have wanted me before, mortal. Yozz wanted me. His guests wanted me. My father wanted me off his hands." {n}She leans closer.{/n} "Be very careful how you want me. I know every way there is, and I have hated all of them."''',
       c('"Then teach me one you won\'t hate."', "teach"),
       c("Continue", "end")),
    hz("teach", '''{n}Her breath goes out through her teeth, and for a heartbeat you are not sure whether she is going to kiss you or cut you. She does neither. She straightens your collar, very precisely, as if dressing a corpse for a funeral.{/n}
"I am already teaching you," {n}she says.{/n} "You are a slow student. Go away before I decide to be a strict one."''',
       c("[Go away, slowly.]", flags=(QUESTION,))),
    hz("end", '''"Go on, then. I have given you enough of my afternoon for nothing." {n}She turns back to the Storyteller's shelves.{/n} "You may come back tomorrow and give me another one."''',
       c("[Leave her to the shelves.]", flags=(QUESTION,))),
], requires=(TESTED,), forbids=(QUESTION, ALLY), delay=24)


# --- 23. A night in Drezen. ------------------------------------------------------------------------------------------------

beat(H + "beat.second_night", "Your turn", '"Come up tonight."', [
    hz("start", '''{n}She looks you up and down, as though pricing the offer.{/n} "Your rooms. In your citadel. With your guards at the door and your priests down the corridor, praying against my kind." {n}Her mouth curves.{/n} "Yes. I would like to see your sheets. I have seen enough of my own strongboxes."''',
       c("Continue", "night")),
    nar("night", '''{n}She comes after the midnight bell, through no door at all, as she always does. The room folds and unfolds, and she is standing by your bed in the dark with her collar already in her hand, and she drops it on your map table, across the Worldwound.{/n}
{n}She does not wait to be asked this time, and she does not ask. She pushes you back against the wall with one hand flat on your chest and holds you there, looking at you in the light of the one candle, as if memorising the place.{/n}''',
        c("Continue", "night2")),
    hz("night2", '''"On my side of the Abyss you were my guest," {n}she says, against your mouth.{/n} "Here I am yours. That is the custom, is it not, among you mortals? The host is responsible for the guest's comfort." {n}Her claws find the laces of your shirt and do not hurry.{/n} "Be responsible, then. Be very responsible."''',
       c("[Draw her down onto the bed.]", "draw"),
       c('"Your turn to wait."', "wait")),
    nar("draw", '''{n}You take her by the hips and turn her, and she lets herself be turned, which she has never done, and you walk her back to the bed with her mouth still on yours. Her leathers come apart under your hands a lace at a time. She is lean and hot and hard as a drawn bow, and when the backs of her knees meet the edge of the bed she sits, and pulls you down after her by the front of your open shirt.{/n}
{n}Her claws rake once, lightly, down your ribs. Her heels lock behind your thighs and draw you in against her.{/n}''',
        c("Continue", "cut")),
    nar("wait", '''{n}She stops. Her claws stop, halfway down your laces. She looks at you with an expression you have never seen on her: surprise, and then, slowly, something that is very nearly delight.{/n}
{n}"Oh," she says softly. "Oh, you learn." And she stands perfectly still, with her hands at her sides and her pale throat bare in the candlelight, and lets you undo her: every lace of the leathers, every buckle, the long line of her back under your palms, the scar under your mouth. She does not move. Her breath does. By the time the last of it is on the floor she is shaking with the effort of standing still.{/n}''',
        c("Continue", "wait2")),
    hz("wait2", '''"Enough," {n}she says, through her teeth, and it is not an order; it is a surrender, and she hates it, and she does not care.{/n} {n}She takes two fistfuls of your shirt and falls backwards onto the bed, and takes you with her, and rolls you under her, and settles her knees on either side of you in the candlelight.{/n}''',
       c("Continue", "cut")),
    nar("cut", '''{n}The candle gutters. Her breath catches in the dark, once, and then again, and her claws find your back, and the guards outside your door hear something that they will argue about in the barracks for a month.{/n}''',
        c("Continue", "after")),
    nar("after", '''{n}When the morning bell rings she is sitting on the edge of your map table in nothing but her scar, buckling on her collar, with the Worldwound pressed flat under her thigh.{/n}
"Your guards are very bad at pretending," {n}she says, without looking round.{/n} "The one on the left has been trying not to listen for three hours. Promote him. He has a gift for suffering." {n}She finishes the buckle, and the air begins to fold.{/n} "My turn next. I will send for you."''',
       c("[Watch her go.]", flags=(SECOND_NIGHT,))),
], requires=(CHAMBER,), forbids=(SECOND_NIGHT,), delay=48)


# --- 24. Your sentries. ----------------------------------------------------------------------------------------------------

beat(H + "beat.sentries", "Holes in the wall", '"You\'re laughing at my sentries."', [
    hz("start", '''"I am not laughing. I am counting." {n}She nods up the street, at the two soldiers on the gate, who are doing their best to look as if they had not seen her.{/n}
"Seven ways into your citadel between the midnight bell and the next. Four of them through walls your masons think are sound. Two through the kitchens. One through the chapel, which I find very funny, and which I will not explain." {n}She turns her thin smile on you.{/n} "My people use three of them. The rest are for guests."''',
       c('"Show my sergeants. All seven."', "teach"),
       c('"Tell me which three your people use."', "three"),
       c('"Keep your seven. I\'ll find them myself."', "find")),
    hz("teach", '''{n}She studies you as if you had offered to hand her the keys to your treasury, and then she laughs outright.{/n}
"You want a demon who came to your city to kill you to walk your walls with your sergeants and show them every hole in them." {n}She shakes her head.{/n} "You understand that I would know, afterwards, which holes they had filled and which they had not? That I would know your walls better than your masons?"''',
       c('"You know them already. This way, so do they."', "teach_yes"),
       c('[Callous] "Teach them. I\'ll have someone watch which holes you don\'t mention."', "teach_watch")),
    hz("teach_yes", '''"You are either very trusting or very lazy." {n}She pushes herself off the shelves.{/n} "Very well. I will teach your sergeants to see holes. They will be terrible at it, and they will be frightened of me the whole time, which will help them learn."
{n}She walks your walls with them for three nights. By the end of it the sergeants look ten years older and the masons are very busy, and the soldiers on the gate have stopped pretending they cannot see her.{/n}''',
       c("[Thank her.]", flags=(SENTRIES,))),
    hz("teach_watch", '''{n}Something like approval crosses her face.{/n} "Now that is how a master thinks." {n}She straightens.{/n} "Yes. Do that. Put your cleverest sergeant behind me and tell him to count what I leave out. He will count wrong, of course, but it will be very good for him."
{n}She walks your walls with them for three nights. On the fourth morning your sergeant brings you a list of the holes she named, and, underneath, in his own shaking hand, one more, which she did not. When you have it filled, a note arrives, pinned to the new mortar with a knife: "Well done. I was starting to worry about you."{/n}''',
       c("[Keep the note.]", flags=(SENTRIES,))),
    hz("three", '''"No." {n}Pleasantly.{/n} "You may have the four that are for guests, and the kitchens, and the chapel, which is still very funny. You may not have the three that belong to my people. I told you. What is mine in your city stays mine." {n}She tilts her head.{/n} "Fill the other four. It will make my people more careful. Careful people live longer, and I have spent a great deal of money on them."''',
       c("[Take the four.]", flags=(SENTRIES,))),
    hz("find", '''"You will not." {n}She sounds sorry for you.{/n} "But you will try, and your masons will fill a great many holes that were never there, and my people will laugh about it in their letters." {n}She shrugs.{/n} "That is also a kind of defence. A very expensive one. Crusades are made of those."''',
       c("[Send for the masons anyway.]", flags=(SENTRIES,))),
], requires=(TESTED,), forbids=(SENTRIES, ALLY), delay=24)


# --- 25. "You served me well, Golarion..." ----------------------------------------------------------------------------------

beat(H + "beat.used", "You served me well", '"In Yozz\'s hall you nearly said something."', [
    hz("start", '''{n}She does not pretend not to understand. She only raises one eyebrow, very slightly, as if you had caught her with her hand in a strongbox that she happened to own anyway.{/n}
"*You served me well, Golarion.*" {n}She says it in exactly the voice she used over Yozz's body.{/n} "I stopped. You heard the half I said. Most people would have heard nothing; they were too busy looking at the corpses."
"Yes. I used you. Did you think it was an accident that a Guild contract came to your dwarf, and led you to Willodus, and Willodus led you to Yozz, and Yozz was stupid enough to try to cheat a crusader who had just walked through half the Midnight Isles?"''',
       c('"No. I thought it was very well done."', "admire"),
       c('"I thought you owed me for it."', "owed"),
       c('"And now?"', "now")),
    hz("admire", '''{n}She looks, for a moment, genuinely pleased, the way an artisan is pleased when someone notices the joint that nobody else noticed.{/n}
"It was very well done. It took me four years. I had to make Yozz believe he had thought of every step himself, and I had to do it while standing behind his chair in a collar." {n}She shrugs.{/n} "And then you came along and did it all in an afternoon, with a dwarf and a great many corpses. It was almost insulting."''',
       c("Continue", "now")),
    hz("owed", '''"Owed you." {n}She repeats it, amused.{/n} "I gave you Yozz's bounty, and his blades if he was stupid enough to offer them, and your life, which I could have taken in that hall with a word to the right assassin. That is a great deal of payment for a tool, mortal."
"But you are right. I never gave you anything you did not have to fight me for." {n}Her eyes go to the side of your head.{/n} "And then you gave me something without a fight. You see why that bothered me."''',
       c("Continue", "now")),
    hz("now", '''"Now?" {n}She considers you, head tilted.{/n} "Now I am wondering which of us is the tool. You lay bleeding on the ground and told me a story that saved my Guild, and I went home and told it, and it worked. I have been using your ear to rule my masters for weeks."
"And you have been using me to make a Guild of assassins decline every contract on your head in the Midnight Isles." {n}Her mouth curves.{/n} "It is a very good arrangement. It is the first one I have ever made where I cannot work out who is cheating whom."''',
       c('"Nobody\'s cheating."', "nobody"),
       c('"I am. A little."', "little")),
    hz("nobody", '''"Nobody is cheating." {n}She laughs, very low.{/n} "Mortal, that is the most frightening thing you have ever said to me."''',
       c("[Leave her laughing.]", flags=(USED,))),
    hz("little", '''"Good." {n}She sounds relieved.{/n} "I would not know what to do with you otherwise. Keep cheating a little. I will keep catching you, a little. It will keep us both sharp."''',
       c("[Leave her pleased.]", flags=(USED,))),
], requires=(YOZZ, MET_Q2), forbids=(USED,), delay=24)


# --- 26. What she tells in person: a master who tried her chair, and the masters who stood. ------------------------------

beat(H + "beat.masters", "A vacancy", '"You look pleased with yourself."', [
    hz("start", '''"I am." {n}She is cleaning under her claws with the point of a very thin knife, and she does not stop.{/n}
"One of my masters tried my chair the night before last. Not the one who got up when I came in with the box; that one is the most loyal knife I have ever owned. Another. An old one, from Yozz's time, who had decided that a woman who comes home with a piece of her enemy instead of his head has gone soft."''',
       c('"And?"', "and"),
       c('"Did you kill him?"', "kill")),
    hz("and", '''"And he was wrong." {n}She holds the knife up to the light and inspects the edge.{/n} "I will not describe what I did about it. You are squeamish, and it would spoil your dinner. I will only say that there is a vacancy on my council, and that the board at my door has one fewer contract on it, because the master who posted it is no longer in a position to pay."''',
       c("Continue", "you")),
    hz("kill", '''"Eventually." {n}She says it with the calm of a woman describing a long and satisfying afternoon's work.{/n} "There is a vacancy on my council now. The board at my door has one fewer contract on it, because the master who posted it is no longer in a position to pay. The others watched. That was the point."''',
       c("Continue", "you")),
    hz("you", '''"I thought you should know. It was, in its way, about you." {n}She puts the knife away.{/n} "Every master in that hall has now been reminded that the ear in the box was taken, not given, and that anyone who says otherwise will be joining it." {n}A thin smile.{/n} "It is a lie. You and I know it is a lie. I have just made it the most expensive truth in Alushinyrra."''',
       c('"Remind me never to call you soft."', flags=(MASTERS,)),
       c('"You enjoyed that."', "enjoyed")),
    hz("enjoyed", '''"Of course I did." {n}She looks at you as if you had remarked that water was wet.{/n} "I am Baphomet's daughter, mortal. I enjoy almost everything I do with a knife. If you were hoping I would stop, you should have let the dwarf have me on the road."''',
       c("[Let it go.]", flags=(MASTERS,))),
], requires=(TESTED,), forbids=(MASTERS, ALLY), delay=48)


beat(H + "beat.stood", "They stood", '"Your masters stood up."', [
    hz("start", '''"They did." {n}She says it as if she were still turning it over.{/n} "They have not stopped talking about it. They have never stood up for anyone. Not for Yozz. Not for me. Not for the Lady's own emissary, who was very offended and has written to complain."
"I asked the oldest of them why. He said that no one had ever walked out of my chamber by the front door before, and they had not known what else to do."''',
       c('"What did you tell him?"', "told")),
    hz("told", '''"That it was the correct response." {n}Her eyes glint.{/n} "That they will do it every time, and that I will have it written into the Guild's rules. Nobody will ask why. We do not care why." {n}She tilts her head.{/n}
"You understand what you have done, mortal? You have become a custom. In a Guild of assassins. They will be standing up for you when you are a hundred years dead and nobody remembers your name, and none of them will know the reason."''',
       c('"That\'s the best kind of custom."', flags=(STOOD,)),
       c('"I\'ll try to come down the stairs more slowly, then."', "slowly")),
    hz("slowly", '''"Do." {n}Her mouth curves.{/n} "Make them stand there. Make them wonder whether you are going to stop and speak to one of them. It will be the most frightening thing that happens in my hall all year, and I will be at the top of the stairs, enjoying it."''',
       c("[Promise to take your time.]", flags=(STOOD,))),
], requires=(CHAMBER,), forbids=(STOOD,), delay=24)


# --- 27. Letters, pinned by a knife (the worst branch reads two in Chapter 5, and none in Chapter 6). ----------------------

letter(H + "letter.first", "Pinned", [
    nar("start", '''{n}You wake with a knife in the post of your bed, a hand's breadth above your head, so thin you did not hear it go in. It pins a folded sheet of black paper. The hand is as sharp as a row of nails.{/n}''',
        c("Continue", "read")),
    hz("read", '''"Mortal.
You have gone off to your war without saying goodbye, which is rude, and without telling me where, which is sensible. I found you anyway. You will have noticed.
I do not write letters. I write contracts. This is not a contract. I have no idea what it is. I am sending it because I was standing in your street by the old elf's shelves and you were not in it, and I found that I minded, and I do not like minding things. It is very bad for business."''',
       c("[Read on.]", "board")),
    hz("board", '''"You will want to know that your name is no longer on any board in Alushinyrra. Not mine, not the two lesser Guilds by the docks, not the one the Lady's court keeps for itself and pretends it does not. I had them taken down. The lesser Guilds took some persuading. One of them no longer exists.
You are not safe. Nobody is safe. But nobody in my city will take gold to kill you, and that is a thing no crusader has been able to say since the Wound opened. Stop eating breakfast with your back to the door.
Still nothing from Father. I went down to the shrine in the Guild's cellar, where Yozz kept his offerings to the Lord of Beasts, and stood in front of it for an hour. I did not pray. I only wanted to see whether he would notice me standing there. He did not. I have never slept so well."''',
       c("[Pull the knife out of the bedpost.]", "knife")),
    nar("knife", '''{n}It comes out with difficulty. It is a very good knife, better than anything in your armoury, with no maker's mark anywhere, and the handle is hollow. When you unscrew the pommel, three small glass vials slide out into your palm, each stoppered with black wax and tied with a thread of white ribbon.{/n}''',
        c("Continue", "vials")),
    hz("vials", '''{n}There is a second sheet, rolled tight inside the handle.{/n}
"The Guild's own antidotes. One for the green, one for the black, one for the thing the Midnight Isles call *the lover's kiss*, which your priests do not know how to treat because they have never been kissed by anyone who meant it.
Deskari's rabble do not use poison; they are too stupid. But you have people around you who are not stupid, and some of them are not yours. Do not waste these on your soldiers. If I hear you gave one away, I will send you six more. Do not let anyone touch the side of your head. H."''',
       c("[Keep the knife, and the vials.]", flags=(LETTER1,))),
], requires=(WANTS,), forbids=(LETTER1, ALLY), delay=72)

letter(H + "letter.invoice", "An invoice", [
    hz("start", '''{n}It comes by an ordinary courier, a tiefling in the Guild's grey, who waits at your door with his hand out until you have paid. That is how you know what it is before you open it.{/n}
"To the Knight Commander of the Fifth Crusade, from the Assassins' Guild of Alushinyrra.
For services rendered this month, as retained: the watching of three doors in Drezen; one message carried into the Abyss and one answer carried out; one deserter returned to the crusade, alive, as specified. At the Guild's rates, which are high. Payment on receipt.
The dresser sends his respects, and asks whether the Knight Commander would like a new coat. He is very good. He does not look up. H., master."''',
       c("[Pay the courier.]", crusade=("Finances", -150))),
], requires=(ALLY,), delay=96)

letter(H + "letter.deciding", "Deciding", [
    hz("start", '''{n}The knife is in the lintel of your door, high up, where you have to stand on a chair to reach it. The note is very short, and the pen has gone through the paper twice.{/n}
"I am deciding. Do not come looking for me. Do not send anyone. Do not reach for anything.
If you are wondering whether I am angry, I am. If you are wondering whether that means no, it does not mean anything yet. It means I am deciding. H."''',
       c("[Get down off the chair.]")),
], requires=(DECLINED,), forbids=(COMMITTED, LEFT_FREE), delay=18)


def integrate(payload):
    """Nothing of its own to bind: the beats read the flags horzalah_trickster declares."""
    return payload
