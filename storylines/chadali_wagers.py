"""Chadali: the wagers that turn a coin on its edge into a courtship (before the commit).

Every scene is in the Council hall, on her own private list (Council_Chadali/AnswersList_0003), after the orange or the
standing coin has opened the relationship (chadali_trickster). Every beat is a wager or a question of chance, never a
motion. Each engages a canon anchor of hers:
- the cookies she bakes herself, and their taste "like a gentle, sunny morning" (Council_Chadali/Cue_0001 f674c7cf,
  Cue_0009 40cd3274);
- her birth "because of a lucky chance, when a yellow aurora, a lunar eclipse, and a meteor shower happened
  simultaneously on Elysium" (Cue_0008 0f9a7d13) and her worshippers: "I heal some, make some stronger... But truth be
  told, I can't compete with the gods!" (Cue_0007 0d35409a);
- "our lucky charm" (Council_1/Cue_0025 866558d6; Council_2/Cue_0013 bd0307cf; Cue_0034 6b4e5052);
- Cobblehoof, "the old fellow" (Cue_0026 bc2cf777), or "It's decided - I must stop him! For his own good." (Cue_0025
  921b93e6); Alichino, "just joking" (Cue_0028 169e409d) or "What a scoundrel!" (Cue_0027 b0fc5d4f);
- "cleaning up after oneself is mandatory" (Cue_0016 d9f3da57), "stop asking me these odious questions!" (Cue_0017
  12bb8e9a), "Accidents happen too, it's not your fault" (Cue_0019 054852ef);
- "sending you my good thoughts and positive vibrations" (Council_3/Cue_0032 15dee189);
- "A terrible calamity. It is our duty to fix it!" (Cue_0010 5b9e9b2b) and "A free space, through which happy
  vibrations flow... Luck - to each and every one, for free" (Cue_0031 2889c1e9);
- "How can you be so gloomy? ... We will definitely win... I just don't know how yet." (Council_1/Cue_0021 5c08817d).
Everything she says about Elysium, her worshippers and her past is her own telling in her own voice; nothing here states
it as fact.
"""
from story_format import c, scene
from storylines.chadali_trickster import CLOSED, COMMITTED, DECLINED, LIST, LOST, STARTED, WAGERED, ch, nar

SCENES = []
W = "chadali.wagers."

# Canon moments this module reads (SeenCues).
COBBLE_STOPPED = "chadali.cobblehoof_stopped"      # Cue_0025: "It's decided - I must stop him! For his own good."
COBBLE_SPARED = "chadali.cobblehoof_spared"        # Cue_0026: "Don't be so harsh on the old fellow."
DEVIL_EXPOSED = "chadali.alichino_exposed"         # Cue_0027: "What a scoundrel! And I trusted him..."
DEVIL_EXCUSED = "chadali.alichino_excused"         # Cue_0028: "Old Alichino is just joking."
ODIOUS = "chadali.odious_questions"                # Cue_0017: "And stop asking me these odious questions!"
FREE_SPACE = "chadali.free_space"                  # Cue_0031: "A free space, through which happy vibrations flow"

SEEN_CUES = {
    COBBLE_STOPPED: ["921b93e6b98730c4cb9d82309fa7c0d2"],
    COBBLE_SPARED: ["bc2cf777c4d435a4284bf1a3fe6813d7"],
    DEVIL_EXPOSED: ["b0fc5d4fcc70a8841b694c0a4826ac9d"],
    DEVIL_EXCUSED: ["169e409dbf64fc14cbaa4fb3ad2121a7"],
    ODIOUS: ["12bb8e9afd0788c4a864e29d4add775f"],
    FREE_SPACE: ["2889c1e9b792f2c4e95a8cc551971063"],
    "chadali.aid_regretted": ["30f2736de45fe584f95ef461b91db9ef"],                                       # Council_2/Cue_0031
    "chadali.lexicon_found": ["805e49b56b678a145891d30f5a5b30f6", "331665d02ccb36a4ba8ad2568a333947"],   # Council_3/Cue_0005, Cue_0016
}

RECIPE = W + "the_recipe"
BORN = W + "born_lucky"
PRAYERS = W + "her_worshippers"
CHARM = W + "a_lucky_charm"
OLD_FELLOW = W + "the_old_fellow"
DEVIL = W + "just_joking"
QUESTIONS = W + "odious_questions"
KNUCKLEBONES = W + "knucklebones"
WOUND = W + "a_free_space"
GLOOMY = W + "so_gloomy"
LOADED = W + "loaded_dice"
REAL_WAGER = WAGERED

# Outcomes other scenes and the epilogue read.
GUESSED = W + "guessed_the_spice"
PRAYER_ANSWERED = W + "prayer_answered"
PRAYER_LEFT = W + "prayer_left_to_her"
NOT_A_CHARM = W + "not_a_charm"
CHARMED = W + "a_charm_gladly"
COBBLE_MENDED = W + "cobblehoof_mended"
COBBLE_CURSED = W + "cobblehoof_left_cursed"
TOLD_BRICK = W + "the_brick"
CHEATED_OPENLY = W + "cheated_openly"
LOST_FAIRLY = W + "lost_fairly"
DICE_CONFESSED = W + "dice_confessed"
DICE_DENIED = W + "dice_denied"
HOPED_ALOUD = W + "hoped_aloud"
BET_ON_HER = W + "bet_her"
WILL_TELL = W + "will_tell_her"
DREAM_WANTED = W + "wanted_the_dream"
CHEATED_SMOOTHLY = W + "cheated_smoothly"


def wager(id, title, entry, nodes, requires, forbids=(), delay=24, chapters=(3, 5)):
    """A physical sitting on her own private list in the Council hall (while it is open)."""
    SCENES.append(scene(id, title, "Chadali", min(chapters), entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=True,
                        Relationship="chadali", Chapters=list(chapters), AnswerLists=[LIST]))


# --- 1. The recipe. ---------------------------------------------------------------------------------------------------

wager(RECIPE, "The recipe", '"What is actually in these cookies?"', [
    nar("open", '''{n}There is always a parcel. You have stopped noticing when she hands it over; it is simply there, warm, wrapped in yellow silk, as if the Council hall produced it the way other rooms produce draughts.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Oh, you want the recipe!" {n}She presses both hands to her cheeks.{/n} "Everybody wants the recipe. Socothbenoth offered me a province for it. Alichino offered me a contract, with footnotes. Shyka said they already knew it, which they don't, because I haven't decided what it is yet."
"I'll make you a bet instead. Guess the spice. One guess. If you're right, I'll tell you a secret. Any secret you like. If you're wrong, you eat three more and say they're wonderful."''',
      c('"Cardamom."', "wrong"),
      c('"Honey isn\'t a spice. But it\'s honey from somewhere that isn\'t here."', "close"),
      c('[Trickster] "Luck. You put luck in them."', "right")),
    ch("wrong", '''"Wrong!" {n}She is delighted.{/n} "There is cardamom. It isn't the spice. Three more, and you have to mean it."
{n}She watches you eat all three with the fierce attention of a grandmother at a wedding. When you finish she nods, satisfied, as if something important has been settled.{/n}''',
      c('"...They are wonderful."', "wonderful")),
    ch("close", '''"Ooh." {n}She squints at you.{/n} "That isn't a guess, that's a clever person's way of not guessing. The honey is from Elysium, yes. From the meadows by the river, where the bees have never once been stung by anything."
"But honey isn't the spice, and you knew it, and you wriggled." {n}She wags a plump finger with a white-gold ring on it.{/n} "Half a secret, then. Only half, for half a guess."''',
      c('"Which half?"', "half")),
    ch("right", '''{n}Chadali goes very still. Then she laughs, and covers her mouth, and laughs through her fingers.{/n}
"How did you know? Nobody knows! Eritrice thinks it's nutmeg. She wrote it down!"
{n}She lowers her voice to a whisper, although there is nobody in the hall.{/n} "Every batch, I hold my breath over the bowl and think of something lucky that happened to somebody. That's all. That's the spice. It doesn't do anything, really. It just makes them taste like mornings."''',
      c('"And the secret I won?"', "secret", flags=(GUESSED,))),
    ch("secret", '''"A secret. A real one." {n}She thinks about it for a long time, turning a bracelet round and round her wrist.{/n}
"I burn them. Sometimes. A whole tray, black as a demon's boots. And I don't throw them away, because that would be unlucky, so I eat them all myself, alone, in the kitchen, and I tell everyone the next batch is the good one." {n}Her dimples come back.{/n} "Nobody knows that. Not even my priests. Now you do. You're the only one."''',
      c("[Promise to keep it.]", "close_out")),
    ch("half", '''"The second half." {n}She leans in.{/n} "The first half is that I'm not very good at baking. The second half is that it doesn't matter, because I believe very hard that I am, and so far that's worked every single time."
{n}She sits back, pleased with herself.{/n} "That's how everything works, really. You believe in it very hard, and then you check the oven."''',
      c("[Take another cookie.]", "close_out")),
    ch("wonderful", '''"You meant it! I could tell. Your ears went pink." {n}She beams.{/n}
"You see? A bet is the nicest way to get people to tell the truth. Nobody lies about cookies when they've got their mouth full of them."''',
      c("[Brush the crumbs off your armour.]", "close_out")),
    ch("close_out", '''"Come back tomorrow. I'll bake again." {n}She says it as if it were the most ordinary promise in the multiverse, and it occurs to you that for her, it probably is.{/n}''',
      c("[Go.]")),
], requires=(STARTED,), forbids=(RECIPE,))


# --- 2. Born lucky. ---------------------------------------------------------------------------------------------------

wager(BORN, "Born lucky", '"You said you were born by chance."', [
    ch("start", '''"Oh, yes!" {n}Chadali claps.{/n} "A yellow aurora, a lunar eclipse and a meteor shower, all at once, over Elysium. Do you know how rarely that happens? Nobody knows! That's the whole point!"
{n}She spreads her hands, bracelets sliding down to her elbows, as if the sky were still up there doing it.{/n} "And there I was. I opened my eyes and I thought, oh, how lovely, I exist. And I liked it so much that I decided the only thing worth doing was to share it."''',
      c('"So you\'re an accident."', "accident"),
      c('"What were the odds?"', "odds"),
      c('"What did you see, when you opened your eyes?"', "saw")),
    ch("accident", '''{n}The dimples vanish. Her lower lip does something that would be alarming on a creature of lesser power.{/n}
"That is a horrid way to put it." {n}She turns her face away, chin up, and sniffs.{/n} "An accident is when a cart tips over. I'm when everything in the sky lines up at once and something wonderful comes out of it. There's a difference, and you know there is, and you said it anyway to see what I'd do."
"...What I'll do is sulk. For a little while. Then I'll forgive you, because I always do, and you'll have to live with that."''',
      c('"I\'m sorry. That was mean."', "sorry"),
      c('"Isn\'t that what I am to you? Everything lining up at once?"', "lined_up")),
    ch("odds", '''"I asked Cobblehoof once. He said 'Phrr', which I think means he tried to work it out and gave up." {n}She giggles.{/n}
"Eritrice worked it out properly. She has it written down somewhere. It's a number with so many noughts in it that she had to turn the scroll sideways." {n}She leans forward.{/n} "Do you know what I said to her? I said, 'But I'm here anyway.' And she wrote that down too. She writes everything down."''',
      c("Continue", "here_anyway")),
    ch("saw", '''{n}Her face goes soft and far away.{/n}
"Colours. So many colours. The aurora was yellow, and the moon was going dark, and the stars were falling, all of them, like somebody had tipped the sky over to see what was underneath." {n}She hugs herself.{/n}
"And there were people. Azata, dancing, because the sky was doing something silly and they always dance when it does. Nobody was waiting for me. I just arrived in the middle of the party. I think that's the best way to arrive anywhere."''',
      c("Continue", "here_anyway")),
    ch("sorry", '''"You are, a bit." {n}She peeks at you sideways, and the chin comes down.{/n} "All right. The sulk is over. That was a short one. You should feel very honoured."''',
      c("Continue", "here_anyway")),
    ch("lined_up", '''{n}She stops sniffing and looks at you properly, and the look goes on for longer than you expect.{/n}
"That's very clever," she says slowly. "And you said it so I'd stop sulking." {n}A pause.{/n} "...It worked. I hate that it worked. You're a horrible lucky charm."''',
      c("Continue", "here_anyway")),
    ch("here_anyway", '''"That's all luck is, really. Things lining up, and somebody noticing." {n}She picks a crumb off the table and eats it.{/n}
"You don't like it, do you? Being lined up for. You'd rather line things up yourself." {n}Her eyes are bright and quite shrewd.{/n} "That's all right. I noticed you. That's my part. What you do about it is yours."''',
      c("[Leave her with the crumbs.]")),
], requires=(STARTED,), forbids=(BORN,))


# --- 3. Her worshippers. -----------------------------------------------------------------------------------------------

wager(PRAYERS, "A prayer in Drezen", '"Do people in Drezen pray to you?"', [
    nar("open", '''{n}She has a scrap of paper in front of her, smoothed flat and weighted with a cookie at each corner, and she is frowning at it with great concentration, her tongue between her teeth.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Some do. Mortals say I'm an empyreal lord, and some even worship me, and I try as best I can not to disappoint them." {n}She taps the paper.{/n}
"This one's from a soldier in your army. A crossbowman. She scratched it on the inside of her helmet and I heard it, because I always hear the ones that are scratched into something; they're the ones people mean." {n}She reads it aloud, carefully.{/n} "'Chadali, let my brother come back from the walls.'"''',
      c('"Will he?"', "will")),
    ch("will", '''"I don't know." {n}She says it very simply.{/n}
"I heal some. I make some stronger. But truth be told, I can't compete with the gods, and I can't see the walls from here, and the demons on them don't care what I want." {n}She smooths the paper again, though it is already flat.{/n}
"So I'll make you a bet. You can see the walls. You're the Commander. You could put her brother somewhere safe tomorrow with one word, and she'd think I did it." {n}Her eyes come up.{/n} "Would you? And would you let me have the credit?"''',
      c('[Trickster] "I\'ll move him. You keep the credit. She\'ll never know it was me."', "moved", flags=(PRAYER_ANSWERED,)),
      c('"No. I don\'t move soldiers because someone prayed. I move them because the war needs it."', "refused", flags=(PRAYER_LEFT,)),
      c('"I\'ll move him. And I\'ll tell her it was me."', "told", flags=(PRAYER_ANSWERED, W + "prayer_credited"))),
    ch("moved", '''{n}She claps, and then catches herself, and looks at the paper with sudden, sharp unease.{/n}
"That's a trick, isn't it. That's you making it true, and me getting thanked." {n}She is quiet.{/n} "She'll pray to me harder next time. For the next brother. And next time you won't be there."
{n}She folds the paper into a very small square.{/n} "I'm going to let you do it. And I'm going to remember that I let you. Both of those are true."''',
      c("Continue", "close")),
    ch("refused", '''"No?" {n}The word is small. Then, to your surprise, she nods.{/n}
"No. That's right. That's fair. If you moved every brother somebody prayed for, you wouldn't have any walls." {n}She looks at the paper for a long time.{/n}
"I'll send her luck anyway. It's all I've got. It's not nothing." {n}Her mouth wobbles, and firms.{/n} "Sometimes it's not nothing."''',
      c("Continue", "close")),
    ch("told", '''"You'd tell her?" {n}She blinks.{/n} "But then she'd stop praying to me. She'd pray to you."
{n}You watch her turn it over. It takes a while, and it is not entirely comfortable to watch; for a moment she looks, very distinctly, like someone deciding whether to be jealous.{/n}
"...Good," she says at last. "Yes. Good. People should know who to thank. It's only polite." {n}And then, much smaller:{/n} "Even if it isn't me."''',
      c("Continue", "close")),
    ch("close", '''"You're a strange lucky charm." {n}She tucks the folded prayer into her sleeve.{/n} "Most of them just sit there and are lucky. You keep getting up and doing things about it."''',
      c("[Leave her with the prayer.]")),
], requires=(BORN,), forbids=(PRAYERS,))


# --- 4. A lucky charm. -----------------------------------------------------------------------------------------------

wager(CHARM, "Our lucky charm", '"You keep calling me your lucky charm."', [
    ch("start", '''"Because you are!" {n}She says it the way other people say the sky is up.{/n}
"The very first time you walked into this hall, I said, 'Just look how cute they are! They'll be our lucky charm,' and everyone laughed, and I was right. You walk into a room and things start going well. You make things go well just by standing near them."
{n}She reaches over and pats your cheek, twice, as if you were a very good dog.{/n}''',
      c('"I\'m not a charm. I\'m a person. I bleed, and I choose."', "person"),
      c('"I don\'t mind being cute. I mind being an ornament."', "ornament"),
      c('[Flirt] "Whose charm, exactly?"', "whose")),
    ch("person", '''{n}The hand stops on your cheek. She takes it back, slowly, and folds it with the other in her lap.{/n}
"I know you bleed." {n}Her voice has gone quiet.{/n} "I've seen the lists. Eritrice reads them out. I cover my ears, and she reads them louder."
"I call you lucky because if I stop calling you lucky, I'll have to think about you bleeding. And I don't want to. I'm chance; I make the odds better, I heal what I can reach, I make people stronger, and I can't do any of it while I'm counting your wounds." {n}She looks at her hands.{/n} "Is it very rude? It feels rude, now you've said it."''',
      c('"It\'s rude. Keep doing it anyway."', "anyway", flags=(CHARMED,)),
      c('"Think about it. The bleeding. I need you to."', "think", flags=(NOT_A_CHARM,))),
    ch("ornament", '''"An ornament!" {n}She is scandalised.{/n} "Ornaments sit on shelves! You've never sat on anything in your life except a horse and my good chair, which you didn't ask about."
{n}Then she hears herself, and has the grace to look a little embarrassed.{/n} "...I did pat your cheek. In front of Alichino. Twice."
"All right. Not an ornament. A charm is something you carry with you because it helps. That's different. That's much better." {n}She peers at you.{/n} "Isn't it?"''',
      c('"A charm doesn\'t get a say."', "think", flags=(NOT_A_CHARM,)),
      c('"It\'s better. Carry me, then."', "anyway", flags=(CHARMED,))),
    ch("whose", '''"Whose?" {n}She opens her mouth, and closes it, and the dimples come and go and come again.{/n}
"The Council's," she says firmly. "Obviously." {n}A pause.{/n} "Mostly the Council's." {n}Another pause, longer.{/n} "Eritrice says you can't own a lucky charm, you can only be lucky enough to have one nearby. She says it's in the rules. I think she made that rule up to stop me buying one."''',
      c('"Then stay nearby."', "anyway", flags=(CHARMED,))),
    ch("think", '''"You want me to think about it." {n}She takes a long breath through her nose, the way you might before diving into cold water.{/n}
"All right. I'll think about it. I'll think about you bleeding and choosing and being a person who might not come back." {n}Her hands are fists in the yellow silk.{/n} "I'll hate it. I'll do it anyway. I'll still bake for you. I'll just bake knowing."''',
      c("Continue", "close")),
    ch("anyway", '''"Good." {n}Her dimples are back, deep enough to lose a coin in.{/n}
"Then I'll keep saying it, and you'll keep being it, and we'll both pretend it's the reason things go well, when really it's you getting up very early and being clever." {n}She taps your nose.{/n} "I know that, you know. I just prefer my way of saying it."''',
      c("Continue", "close")),
    ch("close", '''"Lucky charm." {n}She says it once more, gently, as if testing whether it still fits.{/n} "Yes. Still. Go on, then."''',
      c("[Go.]")),
], requires=(STARTED,), forbids=(CHARM,))


# --- 5. The old fellow: Cobblehoof (the route's pivotal moral choice). ------------------------------------------------

wager(OLD_FELLOW, "The old fellow", '"How is Cobblehoof?"', [
    nar("open", '''{n}Across the empty hall, in Cobblehoof's place, a single grey feather lies on the floor beside his chair. Chadali has not looked at it once since you came in, which is how you know she has been looking at nothing else.{/n}''',
        c("Continue", "stopped", requires=(COBBLE_STOPPED,)),
        c("Continue", "spared", requires=(COBBLE_SPARED,), forbids=(COBBLE_STOPPED,)),
        c("Continue", "never", forbids=(COBBLE_STOPPED, COBBLE_SPARED))),
    ch("stopped", '''"He's been very unlucky lately." {n}She says it brightly, and her bracelets do not clink at all.{/n}
"He tripped on the stairs to the hall. Twice. His purse strings broke in session and all his coins rolled under Socothbenoth's chair. His quill split at the vote." {n}She folds her hands.{/n}
"You told me he brings bad luck to the Council. You said you felt negative vibrations coming from him. I said it was true, and that I must stop him, for his own good." {n}A small, stubborn smile.{/n} "So I did. A little. It's for his own good. He'll thank me."''',
      c('"Undo it. I said that to see what you\'d do. I was wrong."', "mend", flags=(COBBLE_MENDED,)),
      c('[Evil] "Keep it up. He\'s been voting against me."', "curse", flags=(COBBLE_CURSED,), alignment=("Evil", 1)),
      c('"What exactly did you do to him?"', "what")),
    ch("what", '''"Nothing!" {n}Too quickly. Then, looking at the feather:{/n} "I stopped wishing him well. That's all. I used to send him luck every morning with the rest of them. Now I send it to everyone but him."
"You don't know what that's like, for someone at this table. We're all so used to it. Everyone stands in someone's luck. He's standing in the rain now." {n}Her chin lifts.{/n} "He was standing in our way. You said so."''',
      c('"Undo it. I said that to see what you\'d do. I was wrong."', "mend", flags=(COBBLE_MENDED,)),
      c('[Evil] "Keep it up. He\'s been voting against me."', "curse", flags=(COBBLE_CURSED,), alignment=("Evil", 1))),
    ch("mend", '''{n}She stares at you. The smile holds for a moment, and then it goes, all at once, like a candle in a door.{/n}
"You said it to see what I'd do." {n}Very quietly.{/n} "And I did it. To the old fellow. Because you're our lucky charm and you said so."
{n}She stands up, and goes across the hall, and picks up the feather, and holds it in both hands.{/n} "I'll send it back to him tomorrow, all of it, all the mornings I missed. And I'll bake him something. He'll say 'Phrr'. He'll mean thank you." {n}She does not look at you.{/n} "You're so mean. Don't do that to me again."''',
      c("Continue", "close")),
    ch("curse", '''{n}Chadali looks at you, and her face, which has always been open, is carefully closed.{/n}
"All right," she says. "For the Council. For his own good." {n}She puts the feather in her sleeve, beside the prayers.{/n}
"I'll keep it up. I'm very good at wishing. People forget that I can stop." {n}And then, more softly, not to you:{/n} "Poor old fellow."''',
      c("Continue", "close")),
    ch("spared", '''"Grumpy." {n}She smiles warmly.{/n} "He's always grumpy. Somebody told me he brings bad luck to the Council, and I said, don't be so harsh on the old fellow. He's gloomy sometimes, but that will hardly cause us any trouble."
"You were the somebody." {n}She wags a finger.{/n} "I remember. I remember everything anyone says about my friends. I just don't always believe it."''',
      c('"And if I\'d meant it?"', "meant")),
    ch("meant", '''{n}She thinks about it seriously, which you did not expect.{/n}
"Then I'd have been very sad. And I might have listened. I listen to you more than I should." {n}A plump finger comes up, the ring gleaming.{/n} "That's why you have to be careful what you say to me, lucky charm. I'm a lot of luck, and I'm not very good at telling when I'm being aimed."''',
      c("Continue", "close")),
    ch("never", '''"Grumpy. Snorting. Counting his coins." {n}She laughs.{/n} "Everyone thinks he's a stick in the mud. He's the only one who remembers my birthday. Well, the day I call my birthday, which moves, because the sky doesn't do it on a schedule."
"People tell me things about him. That he's gloomy, that he brings bad luck. I never believe them." {n}She glances at you.{/n} "Nearly never. Be careful what you tell me about my friends. I'm a lot of luck, and I don't always notice when I'm being aimed."''',
      c("Continue", "close")),
    ch("close", '''{n}She looks at the empty chair, and at you, and back at the chair.{/n} "Luck isn't soft, you know. Everybody thinks it is, because of the cookies. It's just that I'm usually pointing it the nice way."''',
      c("[Leave.]")),
], requires=(STARTED,), forbids=(OLD_FELLOW,))


# --- 6. Just joking: Alichino. ------------------------------------------------------------------------------------------

wager(DEVIL, "Just joking", '"About Alichino..."', [
    ch("start", '''"Old Alichino!" {n}She claps.{/n} "Did you know he takes the cookies home in a little box? He says they're for 'analysis'. He's analysed every single one. There are never any crumbs."''',
      c("Continue", "exposed", requires=(DEVIL_EXPOSED,)),
      c("Continue", "excused", requires=(DEVIL_EXCUSED,), forbids=(DEVIL_EXPOSED,)),
      c("Continue", "wager", forbids=(DEVIL_EXPOSED, DEVIL_EXCUSED))),
    ch("exposed", '''{n}And then the smile falters, because she remembers.{/n}
"You told me he isn't my friend. That he said out loud he's only here for his own profit. I thought he was joking. I thought everybody here was joking, a little, all the time." {n}She clenches her little fists.{/n}
"What a scoundrel. And I trusted him." {n}The fists open again, slowly.{/n} "I still give him cookies. I don't know how to stop. Isn't that silly?"''',
      c('"It\'s kind. Kind isn\'t silly."', "kind"),
      c('"Stop. He\'ll use it against you."', "stop")),
    ch("excused", '''{n}She waves a hand, bracelets clinking.{/n} "You said once that he isn't my friend. Oh, don't listen to him, I said. He might be a devil, but that doesn't mean he's without a conscience."
"I still think so." {n}She tilts her head.{/n} "You don't. You look at him the way Eritrice looks at a badly drafted motion. That's all right. Somebody has to look at him like that. I'll look at him the nice way, and between us he'll come out even."''',
      c("Continue", "wager")),
    ch("kind", '''"Kind." {n}She tries the word, and seems to like it better than her own.{/n}
"All right. I'll keep giving him cookies, and I'll count them. Eritrice taught me to count things. She says it's the first step to not being robbed." {n}A small, fierce smile.{/n} "I'll be kind with a list."''',
      c("Continue", "wager")),
    ch("stop", '''"Use cookies against me? How?" {n}She genuinely wants to know.{/n}
{n}You explain. It takes some time. By the end she is very quiet and has eaten four cookies without appearing to notice.{/n}
"That's horrible," she says. "Devils are horrible. I knew that. I just didn't want to know it about Alichino." {n}She sighs.{/n} "Fine. Only one cookie a session. He can analyse that."''',
      c("Continue", "wager")),
    ch("wager", '''"I'll make you a bet." {n}She leans across the table, eyes shining.{/n}
"Next session, Alichino doesn't come. He'll send a note saying he's detained by urgent business in Hell. I bet you a whole tray he does." {n}She holds out her hand.{/n} "And you have to bet he comes. Otherwise it isn't a bet, it's just agreeing."''',
      c('[Shake on it] "He comes. A whole tray."', "shake"),
      c('[Trickster] "I\'ll make sure he comes. Then you owe me."', "rig")),
    ch("shake", '''{n}Her hand is small and warm and dusted with flour, and she shakes on it as if it were a treaty.{/n}
"Done! Oh, I love a bet. Everyone at this table is so serious about everything except bets. Then they're serious about the bets too."''',
      c("[Let go of her hand.]")),
    ch("rig", '''"You can't make a devil come to a meeting!" {n}She is scandalised and thrilled in equal parts.{/n}
"Can you? No. Don't tell me. I'll find out." {n}She shakes your hand anyway, hard.{/n} "But if you do it by a trick, it doesn't count, and you owe me two trays. That's the rule. I just made it."''',
      c("[Let go of her hand.]")),
], requires=(STARTED,), forbids=(DEVIL,))


# --- 7. Odious questions. -------------------------------------------------------------------------------------------

wager(QUESTIONS, "Odious questions", '"Are you still cross about my questions?"', [
    ch("start", '''"Which questions?" {n}Her eyes narrow above a cookie.{/n}''',
      c("Continue", "asked", requires=(ODIOUS,)),
      c("Continue", "fresh", forbids=(ODIOUS,))),
    ch("asked", '''"Oh. Those questions." {n}She chews furiously for a moment, exactly the way she did the first time.{/n}
"You asked if you didn't have to take responsibility any more, because chance would clean up after you." {n}She swallows.{/n} "You ruined my mood. It came back. It usually does."
"Then I started on a worse one, all by myself. If a brick falls on a child, whose luck was that? I've been thinking about the brick one."''',
      c('"And?"', "brick")),
    ch("fresh", '''"You never asked me the horrible ones. Other people do. Eritrice, mostly, in session, when she wants to make a point." {n}She makes a face.{/n}
"'If chance helps everyone, does chance help the demons?' 'If a brick falls on a child, whose luck was that?'" {n}She puts the cookie down.{/n} "I've been thinking about the brick one."''',
      c('"And?"', "brick")),
    ch("brick", '''{n}She is quiet for so long that the lamp gutters.{/n}
"There was a girl in Kenabres. Before the fall. She used to leave me honey on a windowsill, a spoonful, every morning, on a saucer with a crack in it." {n}Her voice is very even.{/n}
"The day the city fell, a wall came down on that street. Just an ordinary wall. The demons didn't even do it. It was old, and it was shaken, and it fell." {n}She turns her bracelet.{/n} "I felt the saucer break."''',
      c('"That wasn\'t your fault."', "fault"),
      c("[Say nothing. Take her hand.]", "hand", flags=(TOLD_BRICK,)),
      c('"Then what good is luck?"', "good")),
    ch("fault", '''"No." {n}The flat no, the finger raised with its ring.{/n} "Accidents happen too, it's not anybody's fault. The world wants to help you, it just isn't always able to. I say that to everybody. I say it all the time."
{n}The finger comes down.{/n} "It's true. It's also not enough. Both. That's the thing nobody tells you about being chance: you're right, and it doesn't help."''',
      c("[Take her hand.]", "hand", flags=(TOLD_BRICK,))),
    ch("good", '''{n}Her head comes up fast, and for a moment the empyreal lord looks out of the plump, sweet face, and it is not sweet at all.{/n}
"What good is a sword? It doesn't save everyone either." {n}Her eyes are wet and furious.{/n}
"You hope for the best anyway. You bake anyway. You leave the honey out anyway, even when the saucer's broken. That's what good it is." {n}She scrubs at her eyes with a yellow sleeve.{/n} "Don't you ever ask me that again. Ask me something easy. Ask me about cookies."''',
      c("[Take her hand.]", "hand", flags=(TOLD_BRICK,))),
    ch("hand", '''{n}Her fingers close on yours at once, tight, sticky with honey. She does not look at you. She looks at the lamp until it steadies.{/n}
"I don't tell anyone that. They'd feel sorry for me, and then they'd feel sorry for themselves for feeling sorry, and it goes round and round." {n}A shaky breath.{/n}
"You just held on. That's better. That's the best thing." {n}She squeezes, once, hard.{/n} "Cleaning up after oneself is mandatory. So is letting someone help you do it."''',
      c("[Hold on a while longer.]")),
], requires=(STARTED,), forbids=(QUESTIONS,))


# --- 8. Knucklebones: a real game of chance. ------------------------------------------------------------------------

wager(KNUCKLEBONES, "Knucklebones", '"You brought dice?"', [
    nar("open", '''{n}Five small bones, yellowed and smooth, lie in a row on the Council table. Beside them, a cup of dark wood with a sun carved on the bottom, and a heap of cookies divided with great precision into two piles.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Elysian knucklebones!" {n}She is bouncing, very slightly, in her chair.{/n} "You throw them, and you count the ones that land on their backs, and whoever has more wins a cookie. That's all. It's the silliest game in the multiverse. I love it more than anything."
"I've sent you good thoughts and positive vibrations every single time you rode out of Drezen. Now we find out if they worked." {n}She pushes the cup across.{/n} "You first. Don't do anything clever."''',
      c("[Throw them honestly.]", "honest"),
      c("[Trickster] [Load the throw. Openly, grinning, so she sees.]", "open_cheat"),
      c("[Trickster] [Load the throw so smoothly that nobody could see.]", "smooth", flags=(CHEATED_SMOOTHLY,))),
    ch("honest", '''{n}The bones clatter. Two backs. She claps, throws, and gets one, and gasps as if she had been told a wonderful secret.{/n}
"You won! First throw! You see? The vibrations worked!" {n}You play for an hour. You win eleven cookies and lose nine. She keeps count on her fingers, and gets it wrong in your favour twice, and when you point it out she says it was an accident, and it wasn't.{/n}''',
      c("Continue", "fair", flags=(LOST_FAIRLY,))),
    ch("open_cheat", '''{n}You make no secret of it: a flick of the wrist, a bone turned under a finger, a wink. Five backs.{/n}
{n}Chadali shrieks with laughter so loudly that something in the rafters takes flight.{/n} "Cheat! Cheat! You cheated right in front of me!" {n}She throws, and gets five backs too, and does not explain how.{/n}
"There. Now we're both cheats. Eritrice would have a stroke." {n}She is still giggling.{/n} "That's allowed. If you do it where I can see, it's a game."''',
      c("Continue", "fair", flags=(CHEATED_OPENLY,))),
    ch("smooth", '''{n}The bones fall. Five backs. It is a perfect throw, and perfectly invisible; you are rather proud of it.{/n}
{n}Chadali looks at the bones and, for once, does not clap.{/n} "Five," she says. "Five backs, first throw."
{n}She gathers them up and throws. They come down any old way. She looks at them, and then at you, and smiles, and the smile is completely friendly and does not reach her eyes.{/n} "Lucky you."''',
      c("Continue", "seen")),
    ch("seen", '''{n}You play on. You win every throw. She does not remark on it again. At the end of the hour she pushes your whole pile of cookies across the table to you and keeps none.{/n}
"You won," she says brightly. "All of them. Well done."
{n}She is still smiling when you leave. You are almost at the door before you realise that she has not once, the whole hour, called you her lucky charm.{/n}''',
      c("[Go.]")),
    ch("fair", '''"That," she says, sweeping the bones back into the cup, "is the best game I've had in a hundred years."
"You know why? Because I didn't know who'd win. Nobody at this table ever lets me not know. Alichino counts, Shyka knows, Eritrice writes it down before it happens." {n}She hugs the cup to her chest.{/n} "You let me not know. Or you let me see you cheat. Either's fine. Both's a present."''',
      c("[Take your cookies.]")),
], requires=(RECIPE,), forbids=(KNUCKLEBONES,))


# --- 9. A free space: her dream for the Worldwound. ------------------------------------------------------------------

wager(WOUND, "A free space", '"What would you do with the Worldwound, if we closed it?"', [
    ch("start", '''"Oh!" {n}She presses her hands together.{/n} "A terrible calamity. It is our duty to fix it! And then, afterwards..."''',
      c("Continue", "told", requires=(FREE_SPACE,)),
      c("Continue", "dream", forbids=(FREE_SPACE,))),
    ch("told", '''"I told you already, didn't I? And you listened! Nobody listens to the second half, they only listen to 'fix it'." {n}She glows.{/n}
"A free space, through which happy vibrations flow, permeating the entirety of existence. Luck, to each and every one, for free. The most amazing thing on Golarion!"''',
      c("Continue", "challenge")),
    ch("dream", '''"A free space. Where the wound was." {n}She draws a circle on the table with one finger, in cookie dust.{/n}
"The Abyss touches it now. That's why it hurts. But if the hurt came out, and the other planes could touch it too, then everybody could come and go, and good things could flow through, and luck. Luck, to each and every one, for free!"''',
      c("Continue", "challenge")),
    ch("challenge", '''{n}She beams at you, waiting for you to love it.{/n}''',
      c('"If everyone gets luck, nobody\'s lucky. Luck is being ahead of someone."', "ahead"),
      c('"Who decides who gets it? You?"', "who"),
      c('"It\'s beautiful. I don\'t believe it for a moment. I want it anyway."', "want")),
    ch("ahead", '''{n}The beam dims.{/n} "That's Alichino's kind of luck. That's winning. Winning isn't luck, it's just the other person losing."
"Real luck is when something good happens and nobody had to lose for it. A coin landing on its edge." {n}She looks at you pointedly.{/n}
"You're thinking like a general. That's all right, you have to. But you asked me what I'd do. I'd make the kind of luck nobody pays for." {n}She sniffs.{/n} "And you'd tell me it can't be done, and I'd do it anyway."''',
      c("Continue", "close")),
    ch("who", '''"Me?" {n}She laughs, and then stops laughing, because you are not.{/n}
"No. Well. Somebody has to... pour it." {n}She frowns at her cookie-dust circle.{/n} "Alichino wants to sell it. Socothbenoth wants something he won't say. If it isn't me, it's one of them."
"You're asking if I'd be a tyrant with a watering can." {n}A long pause.{/n} "I might. I think about Cobblehoof, sometimes. I'd need someone to tell me when I was doing it."''',
      c('"I\'ll tell you."', "close", flags=(WILL_TELL,))),
    ch("want", '''{n}She stares at you. Then she laughs so hard she has to hold on to the table.{/n}
"That's the nicest thing anyone has ever said about my plan! Eritrice said it lacked a mechanism. Cobblehoof said 'Phrr'. You said you don't believe it and you want it anyway!"
{n}She wipes her eyes.{/n} "That's how everyone should want things. That's how I want you to... well." {n}She stops, and goes rather pink, and eats a cookie very fast.{/n}''',
      c("Continue", "close", flags=(DREAM_WANTED,))),
    ch("close", '''"When it's done, you'll come and see it. You'll stand in the middle of it and something lucky will happen to you, and you'll pretend it didn't." {n}She wipes the circle away with her sleeve.{/n} "I'm betting on it."''',
      c("[Leave the dust where it fell.]")),
], requires=(PRAYERS,), forbids=(WOUND,))


# --- 10. So gloomy. ---------------------------------------------------------------------------------------------------

wager(GLOOMY, "So gloomy", '"Not today, Chadali."', [
    nar("open", '''{n}You did not mean to come here. The field reports were bad, you took them to your chamber to be alone with them, and somehow you opened the closet instead of the shutters, and now you are standing at the end of the long table in the dark, with your gauntlets still on.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Oh." {n}She has seen your face. She gets up at once, cookies forgotten.{/n}
"How can you be so gloomy?" {n}It is the kind of thing she says across the Council table to tease. She does not say it like a tease now.{/n} "Who was it? Don't tell me the number. Tell me the name. One name."''',
      c("[Tell her a name.]", "name"),
      c('"There are too many names."', "many"),
      c('"I don\'t want to be cheered up."', "no_cheer")),
    ch("name", '''{n}You tell her. She repeats it, carefully, getting it right the second time.{/n}
"I'll remember that one. I'll send luck to wherever they went. I don't know if it gets there. I send it anyway." {n}She takes your gauntleted hand and starts, very carefully, to unbuckle it.{/n}
"You can't hold a cookie in this. Or anything else."''',
      c("Continue", "hope")),
    ch("many", '''"I know." {n}She sits down next to you, not across, and leans her whole warm weight against your arm.{/n}
"There are always too many. That's why I only ask for one. One I can carry. Too many, and you drop all of them, and then you're just a person standing in a hall in the dark with their gauntlets on." {n}She pokes the gauntlet.{/n} "Take it off."''',
      c("Continue", "hope")),
    ch("no_cheer", '''"I'm not going to cheer you up." {n}She says it firmly.{/n} "Cheering up is for when you've spilt something. This is different."
"I'm just going to sit here. You can be gloomy. I'll be here while you do it." {n}She sits. She does not offer a cookie. After a while, without any comment at all, she starts unbuckling your gauntlet.{/n}''',
      c("Continue", "hope")),
    ch("hope", '''{n}When your hands are bare she holds them between hers. Her palms are warm and a little floury.{/n}
"I always say we'll definitely win, I just don't know how yet. Socothbenoth rolls his eyes every time." {n}Her thumbs move over your knuckles.{/n}
"I need you to say something hopeful. Out loud. It doesn't have to be true. It just has to be said, by you, in here. I'll hold it for you until it is."''',
      c('"We\'ll win. I don\'t know how yet."', "hoped", flags=(HOPED_ALOUD,)),
      c('"I can\'t. Not tonight."', "cant")),
    ch("hoped", '''{n}She closes her eyes as if she were catching it.{/n}
"There. Got it." {n}She opens them.{/n} "I'll keep it in my sleeve with the prayers. When it comes true, I'll give it back, and you'll say, 'That was luck,' and I'll say, 'That was you.'"
{n}She lifts your bare knuckles and kisses them, once, lightly, as naturally as she hands out cookies, and then looks startled at what she has done, and does not let go.{/n}''',
      c("[Don't let go either.]")),
    ch("cant", '''"That's all right." {n}She does not let go of your hands.{/n}
"Then I'll say it. I'm good at saying it. I've had so much practice." {n}Softly, stubbornly, into the dark hall:{/n} "We'll win. I don't know how yet."
{n}She leans her forehead against your shoulder and stays there until the lamp needs trimming, and neither of you trims it.{/n}''',
      c("[Stay.]", flags=(HOPED_ALOUD,))),
], requires=(CHARM,), forbids=(GLOOMY,))


# --- 11. Loaded dice: she caught the smooth cheat. ------------------------------------------------------------------

wager(LOADED, "Loaded dice", '"You\'ve been quiet with me since the knucklebones."', [
    ch("start", '''"Have I?" {n}Bright, brittle, a cookie held out at arm's length.{/n} "I've been very busy. There's a great deal of luck to send. The Council is very unlucky this week."''',
      c("Continue", "cheated")),
    ch("cheated", '''{n}The cookie stays out, trembling a little.{/n}
"You loaded the throw." {n}She says it to the cookie, not to you.{/n} "Five backs. So smoothly nobody could see. Nobody but me. I'm chance. I felt it not happen."
"You didn't do it where I could see. That's the difference. If you do it where I can see, it's a game. If you hide it, it's a lie you told my luck." {n}Now she looks up.{/n} "Why?"''',
      c('"Because I could. I\'m sorry. It was a stupid thing to hide."', "confess", flags=(DICE_CONFESSED,)),
      c('"I wanted to win. I always want to win."', "confess", flags=(DICE_CONFESSED,)),
      c('[Lie] "I didn\'t. You\'re imagining it."', "deny", flags=(DICE_DENIED,))),
    ch("confess", '''{n}She puts the cookie down, finally, and sits back.{/n}
"I know you always want to win. It's one of the things I like best about you. It's also the thing that frightens me." {n}Her bracelets clink as she folds her arms.{/n}
"I don't mind you cheating. I mind you cheating me where I can't see. Everything you do to me, do where I can see. Promise." {n}She holds out her little finger, with great seriousness.{/n}''',
      c("[Link your finger with hers.]", "promise")),
    ch("promise", '''"There." {n}She shakes the linked fingers, once, firmly.{/n} "That's binding. That's older than contracts. Alichino can't even read it."
{n}The dimples come back, slowly, like the sun after a storm that has not quite decided to leave.{/n} "Now eat the cookie. It's the cross one. It's got raisins."''',
      c("[Eat the cross cookie.]")),
    ch("deny", '''{n}She looks at you for a long time. Then she nods, and smiles, and pushes the cookie into your hand.{/n}
"All right," she says. "I'm imagining it."
{n}She is perfectly pleasant for the rest of the audience. She talks about the weather in Elysium and the price of honey. When you leave, she says "Go on, lucky charm," exactly as she always does, and now it sounds like something she has decided to keep saying.{/n}''',
      c("[Go.]")),
], requires=(CHEATED_SMOOTHLY,), forbids=(LOADED,))


# --- 12. The real wager: the last beat before the question. --------------------------------------------------------

wager(REAL_WAGER, "The real wager", '"You wanted to make a proper bet?"', [
    nar("open", '''{n}There are no cookies tonight. The Council table is bare except for the coin, standing on its edge where she keeps it, and one white flower from her hair laid beside it.{/n}''',
        c("Continue", "start")),
    ch("start", '''"A proper one." {n}She has her hands folded in her lap, very still, which is not like her.{/n}
"We've made lots of little bets. Cookies and trays and devils coming to meetings. You win most of them, because you make them happen." {n}She looks at the coin.{/n}
"I want to make one you can't make happen. Something you can't balance or load or arrange. You have to bet on something that's only up to me."''',
      c('"What\'s the bet?"', "bet")),
    ch("bet", '''"You bet that when you ask me the question you've been not-asking, I'll say yes." {n}She says it all in one breath.{/n}
"If you win, you win. If you lose, you lose, and you can't do anything about it, and you just have to lose, like a mortal at a dice table." {n}Her chin lifts.{/n} "And you have to put something on it. Something that costs you. Otherwise it's just wishing."''',
      c('"My luck. All of it. Whatever you think I\'ve got."', "stake", flags=(BET_ON_HER,)),
      c('"The coin. I\'ll never balance anything for you again."', "stake", flags=(BET_ON_HER,)),
      c('"I don\'t bet on people."', "people")),
    ch("people", '''"Yes, you do." {n}Flat, with the finger raised.{/n} "You bet on your soldiers every day. You bet on the ones in your tent. You bet on that little witch with the fire in her hands. You just don't call it betting, because then you'd have to admit you might lose."
{n}The finger comes down.{/n} "Call it betting. For me. Once."''',
      c('"...My luck. All of it."', "stake", flags=(BET_ON_HER,)),
      c('"Not tonight."', "not_tonight")),
    ch("stake", '''{n}She lets out a long breath, and the stillness goes out of her all at once; she is bouncing again, very slightly, in her chair.{/n}
"Done! It's a bet! You can't take it back, and you can't cheat, and you can't make it happen." {n}She claps, once.{/n}
"Now you have to wait. And then you have to ask. And then you have to find out, like everybody else in the whole multiverse finds out things." {n}She picks up the white flower and tucks it behind your ear.{/n} "Isn't it wonderful? Isn't it terrifying?"''',
      c('"Both."', "both")),
    ch("both", '''"Both!" {n}She laughs, and the laugh wobbles at the end.{/n} "Heads and tails at once. Like the coin."
"Go away now. Come back with the question. I'll bake. I'll bake the best batch I've ever baked, and I won't burn a single one, and if I do I'll eat them all myself and never tell you."''',
      c("[Go, and come back.]")),
    ch("not_tonight", '''"Then not tonight." {n}She nods, as if this too were fair.{/n}
"The coin will keep standing. It's very patient. So am I, mostly." {n}She looks at the flower on the table, and leaves it there.{/n} "Come back when you'll bet."''',
      c("[Go.]", abort=True)),
], requires=(GLOOMY, WOUND), forbids=(REAL_WAGER, COMMITTED), delay=24)


# --- Her soft no: a coin lying flat. ------------------------------------------------------------------------------------

FLAT = W + "a_coin_lying_flat"

wager(FLAT, "A coin lying flat", '"Is the question still open?"', [
    nar("open", '''{n}The coin is lying flat on the Council table, and nobody has stood it back up. Heads up: the sun.{/n}''',
        c("Continue", "start")),
    ch("start", '''"I knocked it over." {n}She is not looking at it.{/n} "On purpose. I wanted to see if it would stand up again by itself, if I believed very hard. It didn't. I believed very hard for a whole night."
"That's how I know it was you. All of it. Every time." {n}She turns her bracelet.{/n} "I said no. Not today. I meant it. I still mean it today."''',
      c('"What would tomorrow take?"', "tomorrow"),
      c('"Then I\'ll wait."', "wait")),
    ch("tomorrow", '''"Something that isn't a trick." {n}She finally looks at you.{/n}
"I don't know what. That's the terrible part. I'm chance, and I don't know. You'll have to find it." {n}She picks up the coin and holds it out.{/n} "Don't stand it up. Just hold it."''',
      c("[Hold it, and don't stand it up.]", "wait")),
    ch("wait", '''"Good." {n}Her fingers brush yours as the coin changes hands, and stay a moment longer than they need to.{/n}
"I'm still cross. I'm also still here. Both." {n}A small smile.{/n} "Heads and tails."''',
      c("[Go.]")),
], requires=(DECLINED,), forbids=(FLAT, COMMITTED))


# --- Epilogue paragraphs on the committed page (chadali.trickster.epilogue.lucky_night). ------------------------------

EPILOGUE_PARAGRAPHS = [
    (GUESSED, "{n}The recipe was never written down. The Commander was the only mortal who knew what the spice was, and never told, and grew very tired of being asked.{/n}"),
    (PRAYER_ANSWERED, "{n}A crossbowman who had scratched a prayer inside her helmet named her first child Chadali. The child grew up lucky at cards and could not be persuaded that this was not a coincidence.{/n}"),
    (COBBLE_MENDED, "{n}Every year a grey feather arrived at the Commander's door with no note. Chadali said it was from Cobblehoof, and that it meant thank you, and that he would never admit it.{/n}"),
    # She later lifted the curse herself (chadali.sessions.the_old_fellow_again): then only the sessions' restored-luck paragraph shows.
    (COBBLE_CURSED, "{n}Cobblehoof's luck never came back. He said nothing about it, ever, to anyone. Chadali sent him cookies every year, and every year he sent them back, and every year she cried a little, and baked again.{/n}"),
    (TOLD_BRICK, "{n}On the anniversary of the fall of Kenabres she left a spoonful of honey on a cracked saucer on the windowsill, and the Commander never asked, and never moved it.{/n}"),
    (DICE_DENIED, "{n}She never again played knucklebones with the Commander. She never said why. Once, years later, she said \"Lucky you\" at a dice table, and the Commander heard it, and understood, and it was far too late to say anything.{/n}"),
    (DICE_CONFESSED, "{n}They played knucklebones on the first night of every month, and the Commander cheated openly, grinning, and she cheated back, and neither of them ever won anything but cookies.{/n}"),
    (HOPED_ALOUD, "{n}She gave back the hopeful thing the Commander had said out loud in the dark hall, the night the Wound closed, folded very small, from her sleeve. \"That was you,\" she said. The Commander said, \"That was luck.\" They argued about it happily for years.{/n}"),
]


def integrate(payload):
    """Bind this module's own reads, and give the committed page the wagers' consequences."""
    from story_format import p
    for key, cues in SEEN_CUES.items():
        have = payload.setdefault("SeenCues", {}).get(key)
        if have is not None and have != cues:
            raise ValueError("Conflicting binding: " + key)
        payload["SeenCues"][key] = list(cues)
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    page = by_id["chadali.trickster.epilogue.lucky_night"]["Nodes"][0]
    page.setdefault("Paragraphs", []).extend(
        p(text, requires=(flag,), forbids=(("chadali.sessions.cobblehoof_freed_by_her",) if flag == COBBLE_CURSED else ()))
        for flag, text in EPILOGUE_PARAGRAPHS)
