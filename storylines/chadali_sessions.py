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
    nar("open", '''{n}There is no parcel. Chadali is sitting at the Council table with her hands flat on the wood, very straight, like a petitioner who has come to hear a verdict. In front of her lies a small black notebook that is not hers.{/n}''',
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
    ch("trick", '''"To see what they'd give you." {n}She repeats it slowly.{/n} "You used me as a coin. To buy them."
{n}For a moment she is very quiet. Then, to your surprise, she nods.{/n} "That's the Council. Everybody here trades everybody. I just thought I was the one thing nobody traded, because I'm so silly nobody would want me."
"You found a use for my silliness. That's clever. I hate it." {n}She pushes the black book away.{/n} "Tell me next time. Before. I'll babble on purpose. I'm very good at it."''',
      c("Continue", "close")),
    ch("meant", '''{n}She takes that like a blow, and does not flinch, which is worse to watch than if she had.{/n}
"Then." {n}A breath.{/n} "Then it was true, for you, then. And now you know me, and you don't mean it." {n}She thinks about it with visible effort.{/n}
"I babble. I know I babble. Eritrice has a special mark in her minutes for it: a little squiggle. I've seen it." {n}Her mouth wobbles.{/n} "I'd rather be babbling than frightened. That's all it is, mostly."''',
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
    ch("right", '''"Maybe!" {n}Brightly.{/n} "I bake. I send luck. I clap at meetings. It's not very exciting, if you're a thing that's seen the end of worlds."
{n}Then she looks at you, and her head tilts.{/n} "But you're not dull. I've watched Shyka watching you. They lean forward when you talk, and Shyka never leans forward for anybody. I think you make the dull futures interesting. I think you're the only reason they still come to our meetings."''',
      c("Continue", "bet")),
    ch("afraid", '''{n}She blinks at you. Then she sits up very straight, and her bracelets clink, and she looks, for a moment, genuinely formidable.{/n}
"Oh. Yes. I should be, shouldn't I?" {n}She considers the empty chair with new interest.{/n} "They see a page, and then I happen, and the page is wrong. That's what I'm for. That's what I've always been for."
"I forgot. Being on a Council with them makes you forget. They talk about the future as if it's already written, and you start to believe it's already written, and then you stop happening."''',
      c("Continue", "bet")),
    ch("bet", '''"Let's make a bet." {n}She leans across the table, eyes shining.{/n}
"Next time you see Shyka, do something they didn't see coming. Anything. Something small. Something silly. And if they laugh, you win." {n}She holds out her hand.{/n} "And if they don't laugh, it means they saw it, and then I win, and you owe me a very dull cookie."''',
      c('[Shake on it.] "Something they didn\'t see coming."', "shake", flags=(UNFORESEEN,)),
      c('"What if what they didn\'t see coming is me, here, with you?"', "here", flags=(UNFORESEEN,))),
    ch("shake", '''{n}Her hand closes on yours with surprising strength.{/n} "Done. Oh, I hope they laugh. I love it when Shyka laughs. It sounds like crockery falling down a very long staircase."''',
      c("[Let go of her hand.]")),
    ch("here", '''{n}She opens her mouth, and closes it, and goes pink all the way up to the white flowers in her hair.{/n}
"That's... cheating. That's not a bet, that's flirting in a bet's clothes." {n}She does not let go of your hand.{/n}
"...They didn't see it. I know they didn't. I didn't see it either." {n}Very quietly:{/n} "That's the most interesting future I've ever been in."''',
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
{n}And then, with sudden fury, she slaps the table so hard the coin on it jumps and, somehow, lands on its edge again.{/n} "But don't make it a joke! Not this one! You can joke about everything else, I'll laugh at everything else, but not this."''',
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
    ch("start", '''{n}She is holding out a parcel, bigger than her usual ones, wrapped in yellow silk and tied with far too many knots.{/n}
"For my shrine. In Drezen. There's a little one, by the grain market, with a crack in the step. Three priests and a dog." {n}She presses it into your arms.{/n}
"I can't take it myself. I don't go down there; it'd frighten them, having me turn up, and they'd feel they had to cook." {n}She looks at the parcel, not at you.{/n} "Would you? You walk past it every day. I've seen you."''',
      c('"Of course."', "yes", flags=(CARRIED_PARCEL,)),
      c('"What\'s in it?"', "what")),
    ch("what", '''"Cookies. And a letter. And a new bowl for the dog." {n}She counts on her fingers.{/n} "And a little bit of luck, knotted into the string. Not much. Just enough so the step doesn't crack any further."
"And..." {n}She hesitates.{/n} "And a note that says the parcel came by way of the Commander. So they know you walked it down. I want them to know you."''',
      c('"I\'ll take it. And I\'ll knock."', "yes", flags=(CARRIED_PARCEL,)),
      c('"I\'ll send a runner. I can\'t be seen at a shrine."', "runner")),
    ch("yes", '''{n}Her whole face lights up.{/n} "You'll knock! Oh, they'll faint. Brother Anand will faint, and the dog will bark, and Sister Mira will try to give you tea."
"Drink the tea. It's terrible. It's the worst tea in Drezen." {n}She squeezes your arm.{/n} "Tell them it came from me. Tell them I'm well. Tell them I think about them every morning, all three of them, and the dog."''',
      c("Continue", "close")),
    ch("runner", '''"Oh." {n}She takes that in, and nods, and her smile goes a little crooked.{/n}
"No, you're right. You're the Commander. You can't go knocking on little doors with cracks in the steps." {n}She pats the parcel.{/n}
"A runner, then. A fast one. Tell them to knock loudly; the dog's a bit deaf." {n}She lets go of it slowly.{/n} "It'll still get there. That's what counts. Mostly."''',
      c("Continue", "close")),
    ch("close", '''"Thank you." {n}She says it very simply, without any flourish.{/n} "I'm usually the one carrying things. It's very nice to watch somebody else do it badly."''',
      c("[Carry it.]")),
], requires=(PRAYERS,), forbids=(SHRINE,))


# --- 6. Two patrons: Eritrice. ---------------------------------------------------------------------------------------

session(PATRONS, "Two beautiful ladies", '"You and Eritrice..."', [
    ch("start", '''"Socothbenoth calls us 'two beautiful ladies'." {n}She giggles.{/n} "It makes Eritrice furious. She says it's irrelevant to the agenda. She writes it down anyway."
"The patron of debate and the patron of serendipity. We're opposites. She plans everything and I plan nothing. She writes everything down and I forget everything. She never lies and I..." {n}She stops.{/n} "Well. I tell very small lies. About cookies. Mostly."''',
      c('"Are you friends?"', "friends"),
      c('"She agreed with you once. In the first session."', "agreed")),
    ch("agreed", '''"She did!" {n}Chadali sits up, delighted.{/n} "She said, 'I think I agree with Chadali.' In front of everyone. I nearly fell off my chair. I've never been agreed with by Eritrice before or since."
"I think she was so surprised she wrote it down twice." {n}She sighs happily.{/n} "It was the best day."''',
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
    ch("start", '''"Me?" {n}She is honestly startled, a cookie halfway to her mouth.{/n} "Nobody asks me that. I'm the one people wish to. It'd be like asking a well what it wants to throw a coin into."
{n}She puts the cookie down and thinks about it, properly, for so long that the lamp needs trimming.{/n}
"I wish to be surprised." {n}She says it slowly, as if finding it out.{/n} "I'm chance. I've seen every way a coin can land and every way this Council can argue. Very little surprises me any more. You do. You keep happening sideways."''',
      c('[Trickster] [Make a flower appear from behind her ear. One of hers, stolen earlier.]', "flower", flags=(SURPRISED_HER,)),
      c('[Tell her something you\'ve never told anyone.]', "secret", flags=(SURPRISED_HER,)),
      c('"I can\'t surprise you on purpose. That\'s not how it works."', "purpose")),
    ch("flower", '''{n}You reach behind her ear and bring back a white flower, one of her own, that you took from her hair an hour ago while she was talking about oranges.{/n}
{n}She gasps, and snatches at her hair, and finds the gap, and bursts out laughing.{/n} "You stole it! When? I didn't feel a thing! Nobody touches my flowers without my noticing!"
{n}She holds the flower as if it were a jewel.{/n} "That's a good surprise. A very good one. Stealing something and giving it back. That's the nicest kind of trick."''',
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
    ch("tell", '''{n}She leans close and whispers it. It is about a meteor shower, and a party, and an azata who was there when she opened her eyes and whom she has never been able to find again.{/n}
"I still look," {n}she says.{/n} "Every time the sky does something silly. That's the only thing I've ever looked for. Until you."''',
      c("[Hold her.]")),
    ch("stay", '''"That isn't a wish, that's just asking." {n}But she is already pulling the cushions out from under the table, where she has apparently been keeping them.{/n} "Granted. Obviously. Wish for something harder next time."''',
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
    ch("job", '''"Then do it slower." {n}Instantly.{/n} "Or do it worse. I don't care. Win by a bit less. Nobody will write you a song about the feint."
{n}She stands up.{/n} "I'm going to go and be sad about them, since you won't. That's my job, then. Somebody has to." {n}She takes the unopened parcel with her. At the door she stops.{/n} "Come back tomorrow. I'll have finished being sad. I'll need you to have started."''',
      c("[Let her go.]")),
    ch("refuse", '''"...Oh." {n}She looks at the unopened parcel as if it had done something surprising.{/n} "It will cost you. A longer march. More of the other kind of dying, the slow kind, in the snow, where nobody writes the names down at all."
"I don't know if that's better. I'm chance; I never know if it's better." {n}She unties the ribbon.{/n} "But you looked at it, here, where I could see, and you decided it yourself. That's all I wanted. Eat a cookie. You're going to need your strength for the long way round."''',
      c("[Eat one.]")),
    ch("felt", '''{n}She holds your hand on the table between you, tightly, and does not say it is all right, because it is not.{/n}
"They were lucky, you know. In a way." {n}Very quietly.{/n} "Their Commander knew their faces. Most soldiers don't get that much luck."''',
      c("[Hold on.]")),
], requires=(MORNING,), forbids=(BETTING_LIVES,))


# --- 9. The old fellow, again (after the curse was kept, and the yes). -----------------------------------------------

session(OLD_FELLOW_AGAIN, "The old fellow, again", '"You\'ve been watching Cobblehoof\'s chair."', [
    ch("start", '''"He's still unlucky." {n}She says it to the empty chair.{/n} "Every morning I don't send him any luck, and every morning he trips on something. He's started to walk very carefully. It looks so tiring."
"You told me to keep it up. For the Council. Because he votes against you." {n}She turns.{/n} "I have. For you. And I'm going to stop now. I'm not asking."''',
      c('"Stop, then. You were right to want to."', "stop", flags=(COBBLE_FREED,)),
      c('"He still votes against me."', "votes"),
      c('"You\'re not asking. Then why tell me?"', "why")),
    ch("votes", '''"Then out-argue him!" {n}Fierce, sudden, bracelets clashing.{/n} "You out-argue everybody! You out-argued Eritrice about a coin!"
"I made an old fellow miserable for weeks because my lucky charm told me to, and it was the easiest thing I've ever done, and that's what frightens me." {n}She takes a breath.{/n} "I'm stopping. You can be cross. I'll bake you something anyway."''',
      c('"...Stop. You\'re right."', "stop", flags=(COBBLE_FREED,)),
      c('"Then I\'ll be cross."', "cross", flags=(COBBLE_FREED,))),
    ch("why", '''"Because we're... because I'm yours." {n}She says it plainly.{/n} "And you should know when I've decided to do something you won't like. That's fair. I'd want to know."
"But I'm still chance. I'm not your chance. I'm just... near you." {n}Her chin lifts.{/n} "He gets his mornings back. Starting tomorrow."''',
      c('"Starting tomorrow."', "stop", flags=(COBBLE_FREED,))),
    ch("stop", '''{n}Her shoulders come down, a whole inch, as if she had been carrying something up a flight of stairs for weeks.{/n}
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
