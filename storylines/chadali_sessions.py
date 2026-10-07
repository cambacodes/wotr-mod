"""Chadali: what the Council says about her, what she says about the Council, and the war between sessions.

Every scene is in the Council hall, on her own private list (Council_Chadali/AnswersList_0003). Canon anchors:
- the Commander's own words about her to the other lords: "Chadali doesn't belong on this Council. Her constant
  babbling keeps everyone else from focusing!" (Council_Alichino/Answer_0008 1e2f5008) and "Chadali isn't just flippant -
  she's crazy." (Council_Cobblehoof/Answer_0008 debb9862);
- "Chadali, surely you're not afraid to give up some of your essence?" (Council_5-1/Answer_0051 c9e89c3d) and her
  answer, "No, I wouldn't do that to my friends... Um, we are friends, right?" (Cue_0052 61537e58);
- Socothbenoth's introduction: "Eritrice, an agathion, is the patron of debate... Chadali, an azata, is the patron of
  serendipity." (Council_1/Cue_0033 c3cc0d39); Eritrice: "I think I agree with Chadali." (Council_1/Cue_0006 e416b518);
- the Lexicon: "What an amazing discovery! You really are our lucky charm!" (Council_3/Cue_0005 805e49b5) and "I didn't
  really understand any of it, but it's written in a very interesting way!" (Cue_0016 331665d0); the Council's proposal
  of the Commander as the key (Council_Lexicon2/Cue_0040 c4551626, Cue_0046 3d5645ec; bound by eritrice_minutes as
  `eritrice.proposed_key`); Shyka's "rather dull version of the future" (Council_Lexicon2/Cue_0054 1d1c4855);
- "You're a real hero! Just like the ones they sing about in drinking songs!" (Debrief_Council/Cue_0011 0a7679b5).
Her opinions of the other lords are her own, in her own voice.
"""
from story_format import c, scene
from storylines.chadali_trickster import CLOSED, COMMITTED, LIST, LOST, STARTED, ch, nar
from storylines.chadali_wagers import COBBLE_CURSED, COBBLE_MENDED, PRAYERS, BORN, CHARM
from storylines.chadali_fortunes import NIGHT, MORNING

SCENES = []
S = "chadali.sessions."

# Canon moments this module reads.
SAID_BABBLING = "chadali.called_babbling"     # SelectedAnswers Council_Alichino/Answer_0008
SAID_CRAZY = "chadali.called_crazy"           # SelectedAnswers Council_Cobblehoof/Answer_0008
PRESSED = "chadali.pressed_on_essence"        # SelectedAnswers Council_5-1/Answer_0051
PROPOSED_KEY = "eritrice.proposed_key"        # bound by eritrice_minutes (Council_Lexicon2/Cue_0040 or Cue_0046)

SELECTED_ANSWERS = {
    SAID_BABBLING: "1e2f5008f7b4dc44abbf18f6d01baad7",
    SAID_CRAZY: "debb9862514b9f344aa0c12b83503775",
    PRESSED: "c9e89c3d2d39ada4a85211f9be9733fd",
}

OVERHEARD = S + "what_you_said"
FORESEEN = S + "a_dull_future"
LEXICON = S + "an_interesting_way"
SONG = S + "a_drinking_song"
SHRINE = S + "a_parcel_for_the_shrine"
PATRONS = S + "two_patrons"
WISH = S + "what_chance_wishes"
BETTING_LIVES = S + "you_bet_with_people"
OLD_FELLOW_AGAIN = S + "the_old_fellow_again"
FRIENDS = S + "we_are_friends_right"
LAST_EVENING = S + "the_last_evening"

# Outcomes other scenes and the epilogue read.
SAID_IT_TO_USE_THEM = S + "said_it_as_a_trick"
MEANT_IT = S + "meant_it"
UNFORESEEN = S + "unforeseen"
KEY_TOLD = S + "key_told"
SANG = S + "sang_along"
CARRIED_PARCEL = S + "carried_the_parcel"
SURPRISED_HER = S + "surprised_her"
FELT_IT = S + "felt_the_cost"
COBBLE_FREED = S + "cobblehoof_freed_by_her"
COIN_TAKEN = S + "coin_taken_home"


def session(id, title, entry, nodes, requires, forbids=(), delay=24, chapters=(3, 5), **extra):
    """A physical sitting on her own private list in the Council hall (while it is open)."""
    SCENES.append(scene(id, title, "Chadali", min(chapters), entry, nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, LOST, *forbids), delay=delay, last=max(chapters), optional=True,
                        Relationship="chadali", Chapters=list(chapters), AnswerLists=[LIST], **extra))


# --- 1. What you said about me (to Alichino, or to Cobblehoof). -----------------------------------------------------

session(OVERHEARD, "What you said about me", '"You look like you\'ve been told something."', [
    nar("open", '{n}There is no parcel. Chadali sits at the table, her hands flat on the wood. She waits until you have stopped moving.{/n}',
        c("Continue", "alichino", requires=(SAID_BABBLING,)),
        c("Continue", "cobblehoof", requires=(SAID_CRAZY,), forbids=(SAID_BABBLING,))),
    ch("alichino", '''"Alichino left this for me. He said it was 'in my interest to be informed'." {n}She opens the little black book to a page marked with a cookie crumb and reads, in a careful, flat voice:{/n}
"'The Commander: Chadali doesn't belong on this Council. Her constant babbling keeps everyone else from focusing.'" {n}She closes it.{/n} "He's written the date. And the time. And that you said it with conviction."''',
      c("Continue", "question")),
    ch("cobblehoof", '''"Cobblehoof told me. Well. He said 'Phrr', and then he said it, all of it, very slowly, the way he does when he wants you to know he's been thinking about it for a week." {n}Her voice is quite flat.{/n}
"'Chadali isn't just flippant, she's crazy. She infiltrated the Council to infect everyone else with her insanity. Especially you.'" {n}She looks at her hands.{/n} "He said you said it. He doesn't lie. He hasn't got the imagination."''',
      c("Continue", "question")),
    ch("question", '''"So." {n}She lifts her chin, and the dimples are nowhere.{/n} "Did you mean it?"''',
      c('[Trickster] "I said what they wanted to hear, to see what they\'d give me for it."', "trick", flags=(SAID_IT_TO_USE_THEM,)),
      c('"I meant it. Then. I didn\'t know you."', "meant", flags=(MEANT_IT,)),
      c('"I\'m sorry. It was cruel, and I said it to get something."', "sorry", flags=(SAID_IT_TO_USE_THEM,))),
    ch("trick", '"To see what they\'d give you. You used me to buy them." {n}She holds your eyes.{/n} "Next time you want a distraction, ask me. I\'ll babble on purpose. I won\'t enjoy hearing afterwards that you called me mad."\n"And don\'t say that\'s how this Council works. I know how it works."',
      c("Continue", "close")),
    ch("meant", '{n}She takes that like a blow, and does not flinch, which is worse to watch than if she had.{/n}\n"Then." {n}A breath.{/n} "Then it was true, for you, then. And now you know me, and you don\'t mean it." {n}She thinks about it with visible effort.{/n}\n"I babble. I know I babble. I remember Eritrice marking the minutes with a little squiggle. I\'ve seen it." {n}Her mouth wobbles.{/n} "I\'d rather be babbling than frightened. That\'s all it is, mostly."',
      c('"I know that now."', "close")),
    ch("sorry", '''"Sorry." {n}She tastes the word.{/n} "It was cruel. You said it to get something. Those are both true." {n}She nods, slowly.{/n}
"Did you get it?" {n}Genuinely curious, through the hurt.{/n} "The thing you wanted. Was it worth it?"
{n}You tell her. She listens with her head on one side, and at the end she says, with great seriousness,{/n} "No. It wasn't. You could've just asked me. I'd have got it for you, and babbled the whole time."''',
      c("Continue", "close")),
    ch("close", '''{n}She picks the little black notebook up, turns to the page, and, with a stub of charcoal from her sleeve, draws a small, lopsided flower in the margin beside your words.{/n}
"There. Now he can't read it without seeing that." {n}She pushes it back across the table.{/n} "Give it back to him. Tell him I said thank you for the information. He'll hate that more than anything."''',
      c("[Take the notebook.]")),
], requires=(STARTED,), forbids=(OVERHEARD,), RequiresAnyGroups=[[SAID_BABBLING, SAID_CRAZY]])


# --- 2. A dull future: Shyka, fate and chance. ------------------------------------------------------------------------

session(FORESEEN, "A dull future", '"Does Shyka frighten you?"', [
    ch("start", '''"Shyka?" {n}She laughs, but she glances at the Eldest's empty chair as she does it.{/n} "No. Well. A little. Not the way Alichino's smile does. The way a very long corridor does."
"They talk about futures as if they'd been to them already and found them disappointing. Some are dull, they say. They say it kindly. Shyka is always kind when they're being horrible."''',
      c('"Are they right?"', "right"),
      c('"Futures are just odds. You\'re chance. You should be the one they\'re afraid of."', "afraid")),
    ch("right", '"They might be. That doesn\'t mean I have to help them be right." {n}She draws a cookie from her sleeve, then another.{/n} "I\'ve been changing the spice. Next time they visit, they can guess it. If they know everything already, let them say it before they bite."',
      c("Continue", "bet")),
    ch("afraid", '"I\'m chance. I haven\'t forgotten!" {n}She taps the cookie.{/n} "I\'ve been planning a test. A small one. They can know the end of the world and still get breakfast wrong."',
      c("Continue", "bet")),
    ch("bet", '"You bring the cookie to Shyka. I\'ll choose the spice." {n}She holds out her hand.{/n} "If they laugh, you win one of mine. If they don\'t, I get one of yours. That won\'t prove what they foresaw. It will prove whether they\'ll play."\n"And don\'t bring your cook\'s best. I want the one you made."',
      c('[Shake on it.] "Something they didn\'t see coming."', "shake", flags=(UNFORESEEN,)),
      c('"What if what they didn\'t see coming is me, here, with you?"', "here", flags=(UNFORESEEN,))),
    ch("shake", '''{n}Her hand closes on yours with surprising strength.{/n} "Done. Oh, I hope they laugh. I love it when Shyka laughs. It sounds like crockery falling down a very long staircase."''',
      c("[Let go of her hand.]")),
    ch("here", '"That\'s flirting in a bet\'s clothes." {n}She turns pink, then catches your hand herself.{/n} "I like it. Shyka can make their own guesses about us. I haven\'t asked them."',
      c("[Hold on.]")),
], requires=(BORN,), forbids=(FORESEEN,))


# --- 3. An interesting way: the Lexicon, and the key. -------------------------------------------------------------------
# PP6 (pacing, window only): the key branch answers the Chapter 4 session (Council_Lexicon2/Cue_0040, Cue_0046), and her hall list
# is live that night, so the sitting may open in Chapter 4 too: [3, 5] -> [3, 4, 5].

session(LEXICON, "Written in a very interesting way", '"Did you understand the Lexicon?"', [
    ch("start", '''"No!" {n}Cheerfully.{/n} "I didn't really understand any of it, but it's written in a very interesting way! If I told Eritrice so she'd write it down with the little squiggle."
"But I clapped. When you found the way in. I said, what an amazing discovery, you really are our lucky charm." {n}She hesitates.{/n} "Will you explain it to me? Slowly? Alichino explains things to me in a voice for children, and I clap to annoy him."''',
      c('"The Worldwound needs a key. The Council thinks it could be me."', "key", requires=(PROPOSED_KEY,)),
      c('"It says how the Wound was made, and how it might be closed."', "how", forbids=(PROPOSED_KEY,))),
    ch("key", '''{n}She stops smiling. You watch her work through it, slowly, the way she asked.{/n}
"A key. That's you. They talked about it at the table as if it were good news, and I sat there and smiled, because everyone looked so pleased, and I didn't understand what they were pleased about." {n}Her voice has gone very small.{/n}
{n}Her hands are shaking.{/n} "I smiled at you dying."''',
      c('"You didn\'t know."', "didnt_know", flags=(KEY_TOLD,)),
      c('"At worst. Not certainly. I\'m good at avoiding the worst."', "worst", flags=(KEY_TOLD,))),
    ch("how", '''{n}You explain it: the rift, the old experiments, what was torn and what might be sewn. She listens with enormous concentration, her lips moving occasionally as if repeating the hard words.{/n}
"So it's not a door. It's a cut. And cuts don't close because you're nice to them." {n}She frowns.{/n} "They close because somebody stitches them. And stitching hurts."
"Will it hurt you?" {n}She asks it very directly.{/n} "Don't be clever. Just say."''',
      c('"It might. I don\'t know yet."', "didnt_know", flags=(KEY_TOLD,))),
    ch("didnt_know", '''"I should have known." {n}Fiercely.{/n} "I should have asked. Instead I said 'how interesting' and ate a cookie." {n}She wipes her eyes, angrily, with the heel of her hand.{/n}
"I'm going to listen properly now. At every session. Even the boring parts. Even Alichino's footnotes." {n}She looks at you.{/n} "And if anybody talks about you like a key again, I'm going to throw a cookie at them. A hard one. From last week."''',
      c("Continue", "close")),
    ch("worst", '''"You're good at avoiding things." {n}She nods, too many times.{/n} "Yes. That's true. You'll have to avoid this one too. You'll have to be better at it than you've ever been at anything."
{n}And then, with sudden fury, she slaps the table so hard the reports slide off the far end.{/n} "But don't make it a joke! Not this one! You can joke about everything else, I'll laugh at everything else, but not this."''',
      c('"Not this one. I promise."', "close")),
    ch("close", '''{n}She takes your hand and turns it over and looks at the palm, the way fortune-tellers do in the markets, though she does not pretend to read anything there.{/n}
"I'll send you luck every morning. Double. I'll take it from Alichino's share. He won't notice; he never uses his."''',
      c("[Let her keep your hand a moment.]")),
], requires=(STARTED, "chadali.lexicon_found"), forbids=(LEXICON,), chapters=(3, 4, 5))


# --- 4. A drinking song. -----------------------------------------------------------------------------------------------

session(SONG, "A drinking song", '"Are you... singing?"', [
    ch("start", '''{n}She is. Loudly, tunelessly, and with enormous confidence, alone at the Council table with a cup of something that smells of honey and cinnamon and something considerably stronger.{/n}
"I'm writing you a song!" {n}She waves the cup.{/n} "A drinking song! The kind they sing about heroes. You're a hero, so you need one, and nobody's written one yet, which is a disgrace, so I'm doing it."''',
      c('"How does it go?"', "how"),
      c('"Please don\'t."', "please")),
    ch("please", '''"Too late! It's already written! Well. Half." {n}She clears her throat, magnificently.{/n}''',
      c("Continue", "how")),
    ch("how", '''{n}She sings. It is about a coin that would not fall down, and a Commander who "never once left a thing to chance, and never once lost a single dance". It rhymes "Drezen" with "reason" and "treason" and, at one point, "pleasin'". It has eleven verses, and she forgets the fourth and makes up a new one on the spot about Cobblehoof.{/n}
{n}It is the worst song you have ever heard. By the ninth verse, somehow, you know the chorus.{/n}''',
      c("[Sing the chorus with her.]", "sing", flags=(SANG,)),
      c("[Listen, and laugh.]", "laugh")),
    ch("sing", '''{n}She shrieks with delight when you join in, and sings louder, and gets the words wrong on purpose to see if you'll follow, and you do.{/n}
"You sing like a sergeant!" {n}She is laughing so hard she has to put the cup down.{/n} "That's the best kind! Sergeants are the only ones who sing drinking songs properly: like they're giving orders to the tune."
{n}She raises the cup.{/n} "To the Commander! Who never left a thing to chance!"''',
      c("Continue", "close")),
    ch("laugh", '''{n}She pretends to be offended for exactly one verse, and then she is laughing too, and cannot finish the tenth verse at all.{/n}
"It's terrible, isn't it? It's so terrible." {n}She wipes her eyes.{/n} "I wrote it terrible on purpose. A good drinking song has to be bad enough that everybody sings louder to drown it. My cookies are perfect, so somebody has to suffer somewhere."''',
      c("Continue", "close")),
    ch("close", '''"I'll teach it to your soldiers. Every tavern in Drezen, by the end of the month." {n}She beams, pink-cheeked.{/n} "And when they sing it, you'll have to stand there and pretend you don't know the words."''',
      c("[Finish her cup for her.]")),
], requires=(CHARM,), forbids=(SONG,))


# --- 5. A parcel for the shrine. --------------------------------------------------------------------------------------

session(SHRINE, "A parcel for the shrine", '"You want me to carry something?"', [
    ch("start", '{n}Two messages lie beside a parcel: the provisioner\'s demand for a seized cache, and a petition from Chadali\'s shrine by Drezen\'s grain market. She has untied the yellow silk to show you the goods.{/n}\n"The army wants its rations. My priests want relief for the people coming off those walls. They\'ve both claimed the whole lot. There isn\'t a whole lot twice."\n"Look with me. Before somebody calls it a miracle and sends everybody home hungry."',
      c('"Of course."', "yes", flags=(CARRIED_PARCEL,)),
      c('"What\'s in it?"', "what")),
    ch("what", '"Dry rations, flour and honey. The provisioner lent me a little oven and a tray to see what could be cooked. He wants them back before the next ration issue."\n{n}She opens the messages.{/n} "Your seal is on the cache. My priests know that. Don\'t pretend these sacks fell out of Elysium."',
      c('"I\'ll take it. And I\'ll knock."', "yes", flags=(CARRIED_PARCEL,)),
      c('"I\'ll send a runner. I can\'t be seen at a shrine."', "runner")),
    ch("yes", '{n}You open the sacks together. The dry rations meet the army\'s stated claim; the flour and honey remain. You answer each message as though its objection has forced precisely this division. Chadali watches, then takes the pen.{/n}\n"Very clever. Now put the actual amounts in both letters. Neither gets to think they own the other\'s share."\n{n}She knots the relief parcel.{/n} "I\'ll bake the surplus. You take this to the shrine. Tell them who sent it. And knock!"',
      c("Continue", "close")),
    ch("runner", '"A runner, then." {n}She writes the division herself: rations to the army, flour and honey to the shrine. Both letters name the Commander\'s cache.{/n} "The borrowed oven and tray come back after I\'ve baked. Tell the provisioner I said so. No luck in place of his equipment."',
      c("[Send the runner.]")),
    ch("close", '{n}She tests the parcel\'s knot, then gives it back.{/n} "There. Both claimants know what they\'re getting. And I have honey left. Come tomorrow. I want you here when I open the oven."',
      c("[Carry it.]")),
], requires=(PRAYERS,), forbids=(SHRINE,))


# --- 6. Two patrons: Eritrice. ---------------------------------------------------------------------------------------

session(PATRONS, "Two beautiful ladies", '"Tell me about Eritrice."', [
    ch("start", '"Socothbenoth calls us \'two beautiful ladies\'." {n}She giggles.{/n} "I remember Eritrice protesting that it was irrelevant to the agenda. She wrote it down anyway."\n"The patron of debate and the patron of serendipity. We\'re opposites. She plans everything and I plan nothing. She writes everything down and I forget everything. She never lies and I..." {n}She stops.{/n} "Well. I tell very small lies. About cookies. Mostly."',
      c('"Are you friends?"', "friends"),
      c('"She agreed with you once. In the first session."', "agreed")),
    ch("agreed", '"She did!" {n}Chadali sits up, delighted.{/n} "She said, \'I think I agree with Chadali.\' In front of everyone. I nearly fell off my chair. I hadn\'t heard her agree with me before that."\n"I think she was so surprised she wrote it down twice." {n}She sighs happily.{/n} "It was the best day."',
      c('"Are you friends?"', "friends")),
    ch("friends", '''{n}She thinks about it for a long time, turning her bracelet.{/n}
"She thinks I'm silly. I think she's lonely. We're both right." {n}Softly.{/n} "She's been at this table longer than anyone, holding it together with her claws. Nobody brings her anything. So I bring her cookies, and she says she doesn't eat sweet things, and then they're gone."
"I'd do anything for her. Don't tell her. She'd minute it."''',
      c('"Does she know you think that?"', "know"),
      c('"And if we both... if I sat at her side of the table too?"', "side")),
    ch("know", '''"No! And she mustn't." {n}Horrified.{/n} "If Eritrice knew somebody would do anything for her, she'd feel she had to do something back, and she'd make a list, and it'd be very long, and she'd never sleep again."
"Some things are better as a nice surprise. Kept for later." {n}She taps her nose.{/n} "That's the azata way. We keep good things in our sleeves until the right moment. Then: surprise!"''',
      c("Continue", "close")),
    ch("side", '''{n}The bracelet stops turning. She looks at you for a while, and the look is not jealous, and not anything else you can put a name to either.{/n}
"That isn't a cookie question." {n}Quietly.{/n} "That's a whole-parcel question, and I haven't baked it. Don't ask it at this table while there's a war eating everybody's evenings. I'll know what I think when there's time to think it. So will she."
{n}And then, a little too brightly:{/n} "Anyway, she'd minute it. With a motion. Probably against."''',
      c("Continue", "close")),
    ch("close", '''"Two patrons. Debate and serendipity." {n}She pops a cookie into her mouth.{/n} "Between us we've got the whole Council covered. She makes sure it's true, and I make sure it's lucky. Somebody else can worry about whether it works."''',
      c("[Leave her smiling.]")),
], requires=(STARTED,), forbids=(PATRONS,))


# --- 7. What chance wishes for (after the commit). ---------------------------------------------------------------

session(WISH, "What chance wishes for", '"What do you wish for, Chadali?"', [
    ch("start", '"Me?" {n}She puts down the cookie.{/n} "Usually there\'s a petition under that question. Let me see your hands."\n{n}She turns them over, smiling.{/n} "A surprise. A small one. The Council\'s been arguing about the Wound all afternoon. I\'d like something they can\'t argue about."',
      c('[Trickster] [Palm a flower while she studies your other hand, then bring it from behind her ear.]', "flower", flags=(SURPRISED_HER,)),
      c('[Tell her something you\'ve never told anyone.]', "secret", flags=(SURPRISED_HER,)),
      c('"I can\'t surprise you on purpose. That\'s not how it works."', "purpose")),
    ch("flower", '{n}As Chadali inspects one hand, the other slips a flower from the loose strand beside her cheek. You bring it round behind her ear and offer it. She feels the gap, catches your wrist, and laughs.{/n}\n"Just now! While I was watching the wrong hand." {n}She takes the flower.{/n} "Do it again. No, wait. I\'ll watch both this time."',
      c("Continue", "close")),
    ch("secret", '''{n}You tell her. It does not matter what; it is something you have not said aloud to anyone, not to your companions, not to yourself in the dark. It is not a large thing. It is a true one.{/n}
{n}Chadali listens without clapping. When you finish, she is very still.{/n} "Oh," {n}she says.{/n} "Oh. I didn't know that." {n}Wonderingly:{/n} "I didn't know that. I'm chance, and I didn't know."''',
      c("Continue", "close")),
    ch("purpose", '''"Ha!" {n}She points at you, triumphant.{/n} "You just did! You said you couldn't, and you're the one person who always can, and you gave up! That's the most surprising thing you've ever said!"
{n}She laughs so hard she has to hold on to you.{/n} "Oh, that's wonderful. Say it again. No, don't, it'll be less surprising."''',
      c("Continue", "close", flags=(SURPRISED_HER,))),
    ch("close", '''"There. I got my wish." {n}She leans back, satisfied.{/n} "You can have one back. That's the rule. Wish for something. Not a big thing. Something I could do."''',
      c('"Bake me something you\'ve never baked before."', "bake"),
      c('"Tell me a secret you\'ve never told."', "tell"),
      c('"Stay the night."', "stay")),
    ch("bake", '''"Something new!" {n}She claps.{/n} "Oh, that's dangerous. I'll probably burn it. You'll have to eat it anyway." {n}She is already muttering about spices.{/n}''',
      c("[Leave her plotting.]")),
    ch("tell", '{n}She speaks close to your ear, of the party beneath the meteor shower and an azata who danced beside her when she first opened her eyes.{/n} "I never found that one again. I still look when I go home. There were so many people dancing."\n{n}She leans against you, her bracelets resting on your arm.{/n}',
      c("[Hold her.]")),
    ch("stay", '"Granted." {n}She pulls the familiar cushions out from under the table and catches your sleeve.{/n} "I\'ve been waiting for you to ask. Help me with these, then come here."',
      c("[Stay.]")),
], requires=(NIGHT,), forbids=(WISH,))


# --- 8. You bet with people (after the commit): a quarrel about the war. -----------------------------------------------

session(BETTING_LIVES, "You bet with people", '"You\'ve heard about the feint."', [
    nar("open", '''{n}She has heard. You can see it before she says a word: the parcel on the table is unopened, and she is sitting on the far side of it, with the width of the Council table between you, which she has never done since the night of the honey.{/n}''',
        c("Continue", "start")),
    ch("start", '''"Your captains want to send a company out ahead, in plain sight, so the demons go after them and the rest of the army can go round. It's on your war table. Alichino told me; he called it 'sound'." {n}Her voice is very level.{/n} "They know what would happen to that company. So do you."
"I'm chance. I know about odds. I know somebody has to decide." {n}Her hands are fists.{/n} "So decide. Here, where I can see. Will you sign it?"''',
      c('"Yes. I\'ll sign it. I bet with people. That\'s what command is. I won\'t pretend otherwise."', "command"),
      c('"I\'ll sign it. I didn\'t come here for a cookie. I came for you."', "wanted"),
      c('[Say nothing. Sign it in front of her.]', "silent"),
      c('"No. We go the long way round."', "refuse")),
    ch("command", '''"Don't pretend otherwise." {n}She nods, sharply.{/n} "Good. I'd hate you if you pretended. I don't hate you."
"But you'll know their names. Every one of them, not the number on Alichino's sheet. I don't care if it slows you down." {n}Her eyes are wet and hard.{/n} "Learn their names, and I'll forgive you for winning. I won't forgive you for not minding."''',
      c('"I\'ll learn them. Every one."', "felt", flags=(FELT_IT,)),
      c('"If I stopped for every name, I couldn\'t do the job."', "job")),
    ch("wanted", '''{n}That stops her. For a moment the hard face wavers.{/n}
"That's worse," {n}she says finally.{/n} "That's worse and better at once. You're about to do a terrible thing, and you came to me with it first, instead of to a cookie."
{n}She pushes the parcel across the table.{/n} "Tell me their names. The company's. Some of them. Then eat one. Then I'll come round to your side of the table."''',
      c("[Tell her names.]", "felt", flags=(FELT_IT,))),
    ch("silent", '''{n}You say nothing. You do not take a cookie. You sit, on your side of the long table, and let the silence be as long as it needs to be.{/n}
{n}After a long time she gets up and comes round, and sits down next to you, and does not touch you, and then does.{/n} "Names," {n}she says.{/n} "Tell me their names. If you're going to bet their lives, you can remember whom you're betting."''',
      c("Continue", "felt", flags=(FELT_IT,))),
    ch("job", '"Then I\'m still angry." {n}She takes the unopened parcel.{/n} "You don\'t have to sit here. You do have to know whom you sent. Until you do, don\'t ask me to make you feel better about it."',
      c("[Let her go.]")),
    ch("refuse", '''"...Oh." {n}She looks at the unopened parcel as if it had done something surprising.{/n} "It will cost you. A longer march. More of the other kind of dying, the slow kind, in the snow, where nobody writes the names down at all."
"I don't know if that's better. I'm chance; I never know if it's better." {n}She unties the ribbon.{/n} "But you looked at it, here, where I could see, and you decided it yourself. That's all I wanted. Eat a cookie. You're going to need your strength for the long way round."''',
      c("[Eat one.]")),
    ch("felt", '{n}You open the company roll between you. Sergeant Venn, spearman Oris, scout Dessa: you read each name aloud, all the way to the last. Chadali repeats the names she catches herself stumbling over. Then she holds your hand beside the signed order.{/n}\n"Now you know whom you\'re sending. So do I. Bring this back afterwards. I want to know who returned."',
      c("[Hold on.]")),
], requires=(MORNING,), forbids=(BETTING_LIVES,))


# --- 9. The old fellow, again (after the curse was kept, and the yes). -----------------------------------------------

session(OLD_FELLOW_AGAIN, "The old fellow, again", '"You\'ve been watching Cobblehoof\'s chair."', [
    ch("start", '''"He's still unlucky." {n}She says it to the empty chair.{/n} "Every morning I don't send him any luck, and every morning he trips on something. He's started to walk very carefully. It looks so tiring."
"You told me to keep it up. For the Council. Because he votes against you." {n}She turns.{/n} "I have. For you. And I'm going to stop now. I'm not asking."''',
      c('"Stop, then. You were right to want to."', "stop", flags=(COBBLE_FREED,)),
      c('"He still votes against me."', "votes"),
      c('"You\'re not asking. Then why tell me?"', "why")),
    ch("votes", '"Then out-argue him!" {n}Her bracelets clash.{/n} "You balanced that coin without my help. You can answer an old fellow without making him trip on every step."\n"Ever since you told me to, I\'ve kept this up. I\'m stopping now. He gets his mornings back."',
      c('"...Stop. You\'re right."', "stop", flags=(COBBLE_FREED,)),
      c('"Then I\'ll be cross."', "cross", flags=(COBBLE_FREED,))),
    ch("why", '''"Because we're... because I'm yours." {n}She says it plainly.{/n} "And you should know when I've decided to do something you won't like. That's fair. I'd want to know."
"But I'm still chance. I'm not your chance. I'm just... near you." {n}Her chin lifts.{/n} "He gets his mornings back. Starting tomorrow."''',
      c('"Starting tomorrow."', "stop", flags=(COBBLE_FREED,))),
    ch("stop", '''{n}Her shoulders come down, a whole inch, as if she had just set down a heavy sack.{/n}
"Oh, thank you." {n}She is almost crying.{/n} "I'd have done it anyway. But it's so much nicer when you say it too." {n}She wipes her eyes.{/n}
"I'm going to bake him an apology. He'll say 'Phrr'. I'll know what it means."''',
      c("[Let her go and bake.]")),
    ch("cross", '''"Be cross, then." {n}She nods, and her lip trembles, and she keeps her chin up anyway.{/n}
"Being cross with me is allowed. I'm cross with me too." {n}She picks up the grey feather she has kept in her sleeve all this time and lays it on Cobblehoof's chair.{/n} "There. Now it's done, and you can't make me undo it. I'm telling you no about this. His votes won't change it."
"...It felt terrible. I'm going to have a cookie."''',
      c("[Watch her have a cookie.]")),
], requires=(COBBLE_CURSED, COMMITTED), forbids=(OLD_FELLOW_AGAIN, COBBLE_MENDED))


# --- 10. We are friends, right? (Chapter 5: the Commander pressed her in session.) -----------------------------------

session(FRIENDS, "We are friends, right?", '"About what I asked you in session..."', [
    ch("start", '''"About whether I was planning to take someone else's essence instead of giving mine." {n}She says it quickly, to get it over with.{/n}
"You asked in front of everyone. I said no, of course not, I wouldn't do that to my friends. And then I said, 'Um, we are friends, right?'" {n}She looks at her hands.{/n} "I sounded so silly. Socothbenoth answered, very sweetly, and told you off for asking, and I could tell he was only being kind because it was me."
"So I'm asking again. Here. Just you." {n}She looks up.{/n} "Are we friends? Or am I a jar with some Elysium in it that you need?"''',
      c('"You\'re not a jar. You never were."', "not_jar"),
      c('"I needed to know if you\'d run. Everyone was watching you."', "watching"),
      c('"Both. I need what\'s in you. I also need you."', "both")),
    ch("not_jar", '''"But you asked." {n}Stubbornly.{/n} "In front of them. You made me say it out loud so I couldn't take it back."
{n}And then, slowly, she understands.{/n} "...Oh. You made me say it out loud so I couldn't take it back." {n}She sits back.{/n} "That was a trick. So I'd be brave in front of them. So I'd have to be."
"That's horrible," {n}she says, with something like admiration.{/n} "It worked."''',
      c("Continue", "close")),
    ch("watching", '''"Everyone's always watching me. I'm very watchable." {n}A flicker of the dimples, gone at once.{/n}
"And would I have? Run?" {n}She actually thinks about it, which you did not expect.{/n} "Maybe. If you hadn't asked. I'd have found a reason. I'm very good at finding reasons for things I want."
"So thank you. I think. For making me look brave before I was." {n}She sniffs.{/n} "It's a very rude kind of help."''',
      c("Continue", "close")),
    ch("both", '''{n}She stares at you. Then she laughs, a real laugh, surprised out of her.{/n}
"Both! Of course both. Heads and tails. You never answer a question with one side of the coin." {n}She shakes her head.{/n}
"All right. I'm a jar and a friend. I can live with that. Jars get carried carefully." {n}She points a floury finger at you.{/n} "Carry me carefully."''',
      c("Continue", "close")),
    ch("close", '''"We're friends." {n}She says it firmly, as a statement, the way she should have said it in session.{/n} "There. I said it without an 'um'. Write that down somewhere."''',
      c("[Promise to write it down.]")),
], requires=(STARTED, PRESSED), forbids=(FRIENDS,), chapters=(5,))


# --- 11. The last evening (Chapter 5, after the yes): she gives the coin away. ---------------------------------------

session(LAST_EVENING, "The last evening", '"The hall feels different tonight."', [
    nar("open", '''{n}It does. The other chairs have been pushed in more neatly than usual, as if someone had been tidying without meaning to. On the Council table, on a small cracked saucer, the coin you called in the air is standing on its edge, where she keeps it standing.{/n}''',
        c("Continue", "start")),
    ch("start", '''"The door won't open for much longer." {n}She says it lightly.{/n} "I can feel it. The Council's nearly done, one way or another. Everything's lining up. I know the feeling; I was born in it."
"So I want you to take the coin. Still standing. On the saucer. All the way to your quarters, without letting it fall." {n}She pushes the saucer across the table.{/n} "If it falls, I'll know. If it doesn't, I'll know that too."''',
      c('[Take the saucer. Walk very carefully.] "It won\'t fall."', "carry", flags=(COIN_TAKEN,)),
      c('"It\'s yours. You kept it. Keep it."', "keep")),
    ch("keep", '''"No. It's yours. It was always yours. You balanced it." {n}She folds her hands firmly in her lap.{/n}
"I kept it here so you'd have to come back for it. That was a trick, a little one. Now you don't have to come back. So you have to take it." {n}Her voice wobbles, very slightly.{/n} "That's how I'll know you'd have come back anyway."''',
      c('[Take the saucer.] "I\'d have come back anyway."', "carry", flags=(COIN_TAKEN,))),
    ch("carry", '''{n}You lift the saucer. The coin sways. You stop breathing. It holds.{/n}
{n}Chadali watches you with both hands pressed over her mouth, and when you turn toward the door, she makes a small sound, half laugh, half something else.{/n}
"Don't look back at me!" {n}Muffled, behind her hands.{/n} "You'll drop it! Look at the coin! Look at the coin all the way home!"''',
      c('"Come with me. Carry the other side."', "together"),
      c("[Walk, and don't look back.]", "walk")),
    ch("together", '''{n}She is at your side before you finish, her small warm hand under the saucer beside yours, her bracelets held carefully still.{/n}
"Together, then. Slowly. Oh, slowly." {n}She is laughing and whispering at once.{/n} "If it falls, it's your fault. If it doesn't, it's luck. That's the rule for tonight. I just made it."''',
      c("[Walk her home, slowly.]")),
    ch("walk", '''{n}You walk. You look at the coin all the way to the door, and through the closet portal, and out among your own coats into your own chamber. It does not fall. At your door you realise that you have been smiling like a fool the whole way.{/n}
{n}Behind you, very far away, somebody is singing a terrible drinking song.{/n}''',
      c("[Set the saucer down on the shelf.]")),
], requires=(COMMITTED,), forbids=(LAST_EVENING,), chapters=(5,), delay=48)


# --- Epilogue paragraphs on the committed page (chadali.trickster.epilogue.lucky_night). ------------------------------

EPILOGUE_PARAGRAPHS = [
    (SAID_IT_TO_USE_THEM, "{n}Alichino's little black notebook, returned to him with a lopsided flower in the margin, stayed on his shelf for the rest of his long existence. He never tore the page out. Nobody could decide whether that was spite or sentiment, and he declined to say.{/n}"),
    (UNFORESEEN, "{n}Years after the war, Shyka turned up uninvited at one of Chadali's dinners and laughed, once, at something the Commander did with a cookie. Chadali said it sounded like crockery falling down a very long staircase, that the Commander had won the bet fair and square, and that she would pay up as soon as she had baked a cookie interesting enough. She was still baking it, years later.{/n}"),
    (SANG, "{n}The drinking song about the coin was sung in every tavern in Drezen for a generation. It had eleven verses, or twelve, depending on who was drunk. The Commander was obliged to stand in several of those taverns and pretend not to know the chorus.{/n}"),
    (CARRIED_PARCEL, "{n}The little shrine by the grain market kept a plaque by its cracked step: \"The Commander knocked here.\" The step never cracked any further.{/n}"),
    (FELT_IT, "{n}In the war's last campaigns the Commander won a little less often and a little more slowly, and knew the names. She said that was the luckiest thing about any army.{/n}"),
    (COBBLE_FREED, "{n}Cobblehoof walked carelessly again within a month. He never knew why his luck had gone, or why it had come back. Every year a cake arrived for him with no card, and every year he said \"Phrr,\" and ate all of it.{/n}"),
    (COIN_TAKEN, "{n}The coin travelled from the Council hall to the Commander's quarters on a cracked saucer, standing on its edge, and never fell on the way. She always said that was the day she was sure.{/n}"),
]


def integrate(payload):
    """Bind this module's own reads, and give the committed page the sessions' consequences."""
    from story_format import p
    for key, answer in SELECTED_ANSWERS.items():
        have = payload.setdefault("SelectedAnswers", {}).get(key)
        if have is not None and have != answer:
            raise ValueError("Conflicting binding: " + key)
        payload["SelectedAnswers"][key] = answer
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    page = by_id["chadali.trickster.epilogue.lucky_night"]["Nodes"][0]
    page.setdefault("Paragraphs", []).extend(p(text, requires=(flag,)) for flag, text in EPILOGUE_PARAGRAPHS)


# Actual orders and actual names are distinct receipts.
_bet = next(sc for sc in SCENES if sc["Id"] == BETTING_LIVES)
_bn = {nd["Id"]: nd for nd in _bet["Nodes"]}
for _choice in _bn["start"]["Choices"][:3]:
    _choice["Set"].append(S + "feint_signed")
_bn["start"]["Choices"][3]["Set"].append(S + "feint_refused")
_bn["start"]["Choices"][3]["Crusade"] = dict(Resource="Finances", Amount=-100)
_bn["start"]["Choices"].append(c('"Wait. I need the company roll before I decide."', abort=True))
for _id in ("command", "wanted", "silent"):
    _bn[_id]["Choices"][0]["Text"] = "[Read every name on the company roll aloud.]"
    _bn[_id]["Choices"][0]["Set"].append(S + "names_recounted")

# The reporter supplies either a book or spoken words, never both by inference.
_report = next(sc for sc in SCENES if sc["Id"] == OVERHEARD)
_rn = {nd["Id"]: nd for nd in _report["Nodes"]}
for _id in ("trick", "meant", "sorry"):
    _rn[_id]["Choices"][0]["Requires"].append(SAID_BABBLING)
    _rn[_id]["Choices"].append(c("Continue", "close_cobblehoof", requires=(SAID_CRAZY,), forbids=(SAID_BABBLING,)))
_rn["close"]["Choices"][0]["Set"].append(S + "notebook_returned")
_report["Nodes"].append(ch("close_cobblehoof", '"Tell the old fellow I heard him. And tell him I answered you myself." {n}She moves her chair back towards yours.{/n} "He can dislike my answer. He does not get to make it for me."', c("[Carry her answer back.]", flags=(S + "oral_reply",))))
EPILOGUE_PARAGRAPHS[:] = [(S + "notebook_returned" if flag == SAID_IT_TO_USE_THEM else flag, text) for flag, text in EPILOGUE_PARAGRAPHS]
ROUND2_PARAGRAPHS = [
    (S + "oral_reply", '{n}Cobblehoof received her answer in words, and answered "Phrr." Chadali kept visiting his chair to argue her own case.{/n}'),
    (S + "feint_signed", '{n}The company went out under the signed order. After the fighting Chadali brought the casualty roll to the Commander, and would not accept a victory toast in its place.{/n}'),
    (S + "feint_refused", '{n}The army took the longer road. The extra supplies cost a hundred crowns; the snow cost lives. Chadali helped the returning wounded and did not call the march lucky.{/n}'),
]
_shr = next(sc for sc in SCENES if sc["Id"] == SHRINE)
for _nd in _shr["Nodes"]:
    if _nd["Id"] in ("yes", "runner"):
        _nd["Choices"][0]["Set"].append(S + "cache_allocated")
_wish = next(sc for sc in SCENES if sc["Id"] == WISH)
# Explicit brief: later chosen night, familiar cushions, her impatient invitation.
_wish["Nodes"].append(ch(WISH + ".explicit.1", '{n}She loosens your collar, then pushes your coat off your shoulders. Her yellow silk joins it on the floor. She draws you down onto the cushions, her bracelets cold against your bare back, and pulls you closer.{/n} "You\'re staying."', c("[Stay.]")))
next(nd for nd in _wish["Nodes"] if nd["Id"] == "stay")["Choices"][0]["Next"] = WISH + ".explicit.1"


# endings1: coin_taken_home is produced by completed carriage, never intent.
_last_coin = next(sc for sc in SCENES if sc["Id"] == LAST_EVENING)
_last_coin["Forbids"].append("chadali.wagers.coin_lost")
for _nd in _last_coin["Nodes"]:
    for _answer in _nd["Choices"]:
        if COIN_TAKEN in _answer["Set"]:
            _answer["Set"].remove(COIN_TAKEN)
# Preserve the saved terminal exits. The actual arrival has an appended
# staging node, and produces the receipt before returning to the old exit.
for _nd in _last_coin["Nodes"]:
    for _answer in _nd["Choices"]:
        if _answer.get("Next") in ("walk", "together"):
            _answer["Next"] += "_home"
_last_coin["Nodes"].extend([
    nar("walk_home", '{n}You carry the saucer through the portal and into your quarters. At the shelf the coin is still standing. Only then do you breathe.{/n}', c("Continue", "walk", flags=(COIN_TAKEN,))),
    nar("together_home", '{n}Chadali keeps her hand beneath the saucer all the way through the portal. In your quarters she waits until you have set it down, the coin still upright, then laughs and takes your hand.{/n}', c("Continue", "together", flags=(COIN_TAKEN,))),
])
_sessions_integrate = integrate
def integrate(payload):
    _sessions_integrate(payload)
    for _sc in payload["Scenes"]:
        if _sc["Id"] == "chadali.trickster.epilogue.lucky_night":
            for _para in _sc["Nodes"][0].get("Paragraphs", []):
                if COIN_TAKEN in _para["Requires"]:
                    _para["Forbids"].append("chadali.wagers.coin_lost")
# end endings1


# endings1: the retained exits now follow the witnessed arrival above.
_coin_exits = {nd["Id"]: nd for nd in _last_coin["Nodes"]}
_coin_exits["walk"]["Text"] = '{n}The saucer rests on your shelf, the coin upright. Your hand is still cramped from carrying it. At the door you realize you have been smiling the whole way. Far off, beyond the portal, someone sings a terrible drinking song.{/n}'
_coin_exits["together"]["Text"] = '{n}Chadali leaves the saucer on the shelf and slides her warm hand into yours. Her bracelets chime as she starts laughing.{/n} "All the way! And you did not drop it. I was watching." {n}She looks from the coin to your face.{/n} "You would have come back anyway. I know now."'
# end endings1 coin arrival
