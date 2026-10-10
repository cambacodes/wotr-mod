"""Jerribeth cloud voice-owner layer (villain-route-jerribeth, 2026-10-08).

Design-first pass, see tools/route_packs/redesign/jerribeth/cloud-review.md. Runs in
jerribeth_round2.integrate right after jerribeth_scaffolding.integrate (voice fill, install_slots),
so every node and copied answer it names already exists. Text only, plus flag-gated paragraphs that give earned
outcomes a reader (D1 widow's supper, D3 Wintersun study) and stage the footstool (D6). Ids,
Next, Set, Requires/Forbids, checks and answer order are untouched. Every key must resolve.

Canon used (enGB): 0b920731 (planted ideas), b323e4a8 (travellers killed at Wintersun's walls),
eb28ad3b (the needle), de70b6ee, ecc42853 (she will choose a side against her patron).
Authored, no canon claim: the widow Aldane, the Kenabres fortune-teller's face, the moth test.
"""
from story_format import p

TITLES = {
    "unsold_evening": "The face she kept",
}

NODES = {}
CHOICES = {}
PARAS = {}


def text(scene, node, body=None, *choices, paras=()):
    if body is not None:
        NODES[(scene, node)] = body
    for index, choice in choices:
        CHOICES[(scene, node, index)] = choice
    if paras:
        PARAS[(scene, node)] = list(paras)


# ---- borrowed_sun: the study is a memory of the killings, not a diorama with no one in it ----------
NO_FACE = '"Give him no face. Let him be no one."'
HOW = '"Show me how you made them so certain."'
ALL_OF_IT = '"Turn it round. I want to see how it is done. All of it."'
KEPT = '"Because I want you. That does not mean I will watch this with you. Keep those apart."'
RESERVED = '"Because I wanted to see what you would do when I did not applaud. I have not decided what that makes me."'
FINISHED = '"I am not. We are finished."'
POWER = '"Because I understand it. A whole people seeing what you choose. I want to know how that feels."'

text("borrowed_sun", "start", '''{n}Tonight the frame shows snow. A palisade of sharpened trunks, torches along its top, and a gate standing open on the dark. Nothing moves. The flakes hang where they were falling when she stopped them.{/n}
"A study. Not for sale. I keep it the way you keep a letter from home."
{n}Halfway between the treeline and the gate a figure is frozen in mid-stride: a traveller in a crusader's cloak, one arm flung out toward the torches, running. Where the face should be there is nothing at all.{/n}
"You know the place. I can hear how carefully you are waiting."''',
     (0, '"Wintersun. Why bring it into this room?"'),
     (1, '[Ask her to cover it until another evening.]'))
text("borrowed_sun", "shape", '''"Because it is the best thing I ever made, and I have never had anyone to show it to who understood it."
{n}She lets the scene run for a heartbeat. On the palisade a clansman lifts his spear, and the frame lets you see what he sees: something grey and horned and long in the arm, coming at the gate out of the snow.{/n}
"Every traveller who found my little oasis ran at those walls hoping. Every one of them died on them, and the clan sang over the bodies for killing a demon. I watched the clan, always. I never once looked at the travellers. So I cannot remember a single face."
{n}The figure hangs in the snow, arm out, faceless.{/n}
"I should like to finish him. I should like him to have yours. Then I should like to run it, and watch you watch it."''',
     (0, NO_FACE), (1, HOW), (2, ALL_OF_IT),
     (3, '"You want me to watch them kill him and call it art."'),
     (4, '"You want to see whether I still admire it."'))
text("borrowed_sun", "shape.reply.1", '''"Yes. Both. Do not pretend they are different questions."
{n}She does not cover the study. The torches stand frozen in mid-flare. She waits beside the faceless man as if he were a guest she has seated badly.{/n}''',
     (0, NO_FACE), (1, HOW), (2, ALL_OF_IT))
text("borrowed_sun", "empty", '''"No face. How fastidious."
{n}She lets the scene go. The traveller runs the last yards with nothing where his face should be, and the first spear takes him under the collarbone, and a second in the belly while he is still trying to understand. He goes down at the foot of the gate. The wall cheers. Someone throws a torch onto him, to make sure.{/n}
"There. He dies exactly the same. All you have spared is yourself the trouble of looking at him."''',
     (0, '[Watch the snow cover him.]'),
     (1, '"You did that to make my answer look foolish."'))
text("borrowed_sun", "empty.reply.1", '''"I did it because that is what happened. Your answer only decided whose face I am not thinking about."
{n}She runs it again, slower. You see now that the clan's faces are perfectly clear, every one of them: joy, righteousness, a boy weeping with relief.{/n}
"I remember all of theirs. Shall I name them for you?"''',
     (0, '"No. Stop it there."'))
text("borrowed_sun", "empty.reply.2", '''{n}She stops it with the torch still in the air.{/n}
"Stopped. Not gone. I can stop anything. I cannot be made to forget it, and I would not want to."
{n}She draws one claw across the snow below the gate, and where she drags it the white comes up dark, as though something underneath had been waiting to be uncovered.{/n}
"There were a great many before your crusade came along. I counted the clan's songs, not the bodies."''',
     (0, '"And you kept none of their faces."'))
text("borrowed_sun", "empty.reply.3", '''"Not one. I kept the songs. You may decide which of us that says more about."''',
     (0, '[Watch her let the snow fall again.]'))
text("borrowed_sun", "expose", '''"How I made them certain? Oh, that I can show you."
{n}She turns the whole scene, gate and palisade and frozen torchlight, the way a child turns a doll's house, until you are standing among the clan on the wall, looking out. From here the traveller is not a man at all. He is grey and horned and long in the arm, and the word he is screaming sounds like a war-cry.{/n}
"The face I gave them. That part is easy; any hedge-illusionist could do it. The art is the rest. They had to want it. A clan that has buried sons wants a demon to kill very badly. I gave them one at the gate whenever they were hungry."''',
     (0, '[Let her turn it back to the gate.]'),
     (1, '"And when one of them hesitated?"'))
text("borrowed_sun", "expose.reply.1", '''"Then his neighbours saw him hesitate, and I let them see something in his face as well. They are a very loyal people. They never needed telling twice."
{n}On the wall, a young man lowers his spear a hand's width. The man beside him looks at him for a long moment, and the frame shows you what the neighbour sees: the boy's eyes have gone yellow, and there is something wrong with his teeth.{/n}''',
     (0, '"Stop. I have seen enough of how."'))
text("borrowed_sun", "expose.reply.2", '''"You have not. Nobody has. That is why I keep it."
{n}She lets the neighbour's spear go into the boy, and the traveller at the gate falls a moment later, and the wall cheers both.{/n}
"Two for one, that night. They sang longer than usual."''',
     (0, '"You loved that night."'))
text("borrowed_sun", "expose.reply.3", '''"I adored that night. I would have shown it to Baphomet, but he never had an eye for detail."''',
     (0, '[Let her turn the scene back to the gate.]'))
text("borrowed_sun", "account", '''{n}She steps back from the study. Snow begins to fall again on the dead at the gate, quite gently.{/n}
"Before you say something decent: nothing you say tonight reaches them. They are dead, the clan is whatever your crusade and I have left of it, and this is mine. Do not tell yourself later that you rescued anybody from a memory."''',
     (0, KEPT), (1, RESERVED), (2, FINISHED), (3, POWER), (4, '"I know."'))
text("borrowed_sun", "account.reply.1", '''"Good. And do not wait for me to say I remember it with regret. I remember it the way you remember a good meal."''',
     (0, '"They ran at those walls because they thought they had found people. I remember that part."'))
text("borrowed_sun", "account.reply.2", '''{n}Her antennae quiver once.{/n}
"Then why are you still at my frame?"''',
     (0, KEPT), (1, RESERVED), (2, FINISHED), (3, POWER))
text("borrowed_sun", "remain", '''{n}For several breaths she offers neither an excuse nor a new display. Then she reaches into the study and, very carefully, the way she sets a pin, gives the dead man at the gate a face.{/n}
{n}It is not yours. It is nobody's yet: young, ordinary, frightened, the mouth open on a word you will never hear.{/n}
"There. I changed it for you. Remember that I can. Remember that I can change it back, that I liked it better the other way, and that the snow falls on him whenever I care to look."
"Now come closer. I want to watch you look at him."''',
     (0, '[Look at him with her.]'))
text("borrowed_sun", "power_reply", '''{n}Her attention sharpens until you can feel it, a pressure behind the eyes, as if she had leaned her whole weight on the frame.{/n}
"How it feels." {n}She tastes the words.{/n} "Like being the only one awake in a house full of sleepwalkers, and choosing their dreams. Like being their god, Commander, without the tedium of being prayed to."
"I could show you a little of it. One gate. One night. You would never want to stop."''',
     (0, '[Look at the gate without letting her in.]'))
text("borrowed_sun", "power_reply.reply.1", '''"No. You have offered your eyes and kept your head. I noticed. I always notice where people keep the locks."
{n}She taps the faceless man at the gate with one claw. He rocks in the snow, frozen mid-stride.{/n}
"So we look from outside the glass. For now. The dead do not mind which side of it we stand on."''',
     (0, '[Look at it with her, from outside the glass.]'))

# D3: the study's last state stands in her Drezen cabinet.
text("room_measure", "floor", paras=(
    p('''{n}On the shelf beside her chair stands the Wintersun study from the frame: the palisade, the snow, the torches. The man at the foot of the gate has a face again. It is not the one she gave him for you. She has changed it back.{/n}''',
      requires=("jerribeth.sun_reworked",)),))

# ---- unsold_evening: the first evening after the widow's supper -----------------------------------
ROOM = '[Ask her to show the room she prepared.]'
BARE = '[Keep the frame bare and talk.]'
LATER = '[Ask to keep the evening for another time.]'
KISS = '"Tell me how you would kiss me if we were in the same room. I want to hear you say it."'
TALK = '[Put your hand flat on the frame and make her talk instead.]'
GO_ON = '[Keep going, and stay at the frame afterwards.]'
STOP = '[Stop there, and make her talk instead.]'
LEAVE_IT = '[Let it lie, and tell her what you want from her instead.]'
EVENING = '[Leave her the evening. Promise nothing about the next.]'

text("unsold_evening", "start", '''{n}When the frame wakes, your own face looks out of it.{/n}
{n}It is the likeness from the widow's table: your scar, your way of holding a cup, a little warmer than you are and smiling rather more. It lifts the cup to you. Then the smile stays a moment too long, and you know who is wearing it.{/n}
"I have been practising. I am better at you than you are. You should hear what the upper town has been saying about your manners since that supper."''',
     (0, ROOM), (1, BARE), (2, LATER),
     (3, '"Take my face off. I want to see yours."'),
     # D1: the supper's actual outcome is read here, by its semantic flags, never by offer_design.
     paras=(
         p('''"The widow Aldane has stopped receiving. Her porter told the baker's boy, who told the whole street: every man who comes to her door, she looks up as though the Commander had come back, and then she sees who it is. She has taken to sitting in the hall so as not to miss one. I go and look at her on Thursdays. She holds the pose beautifully."''',
           requires=("jerribeth.widow_pinned",)),
         p('''"The widow Aldane had her husband back for one supper and lost him twice. She sets his place every evening now and sits beside it, and does not eat. You did that, Commander. I only lent you the face."''',
           requires=("jerribeth.widow_husband",), forbids=("jerribeth.widow_pinned",)),
         p('''"They call her the demon's widow in the upper town. Her daughters have taken the silver and gone looking for husbands who never heard the story. You shamed her to save her, and nobody will ever sit at her table again. I could not have done it better. I did not have to."''',
           requires=("jerribeth.widow_exposed",)),
         p('''"Half the upper town says the Commander raved at a widow's table about demons. The other half says it was the wine. I have been helping both halves. You would be astonished how little help they need."''',
           requires=("jerribeth.sale_withdrawn",), forbids=("jerribeth.widow_exposed",)),
         p('''"And you still have two of her husband's spoons. I like to think of you eating with them."''',
           requires=("jerribeth.widow_fee_shared",)),
     ))
text("unsold_evening", "start.reply.1", '''"Yours is the only face I ever wore that I did not want to give back."
{n}It comes away in her claws like wet paper. Under it is her own narrow head, antennae laid back, very pleased.{/n}
"I can make you a room to go with it. Or nothing at all, and you can simply look at me."''',
     (0, ROOM), (1, BARE), (2, LATER))
text("unsold_evening", "room", '''{n}The frame fills with a room you know: the widow's dining room, the candles down to their sockets, the long table cleared. She has kept it. She sits at the head, where your likeness sat, and the chair beside her has been pulled out.{/n}
"I liked the room. I disliked the company. Tonight I have improved the company."''',
     (1, '"Wear a face you enjoy. Tell me why you like it."'))
text("unsold_evening", "guise", '''{n}The change takes place in full view. The woman at the head of the widow's table has a broad mouth, fine lines beside her eyes and an expression that is entirely Jerribeth's. She turns one hand, watching the candlelight lie along its ordinary knuckles.{/n}
"This one smiles very well. People expect a creature with this mouth to have something pleasant to say. I disappoint them on purpose."''',
     (0, '[Ask her to bring the image nearer.]'))
text("unsold_evening", "guise.reply.1", '''"No. A fortune-teller's, in Kenabres, the week the walls came down. She was lying in the street and had no further use for it. I improved the symmetry. Then I liked her better crooked."
{n}She smiles to demonstrate. It is a very good smile, and it was somebody's.{/n}''')
text("unsold_evening", "true", '''{n}She lets the widow's room dim around her own narrow silhouette. The antennae move as she watches you; a little candlelight stays caught along the edges of her wings.{/n}
"You are allowed to look pleased. Examining specimens is my side of the glass."
{n}You tell her which movement made you smile. Her hands separate, and she brings one to the very edge of the image.{/n}''')
text("unsold_evening", "near", '''{n}Her image comes right up to the edge of the frame, close enough that the lacquer seems to warm under your fingers.{/n}
"I sat at that table for three hours with your face on and a widow eating me with her eyes, and all I could think about was what you would do with your hands if they were mine. I want to find out. Tonight. As near as this wretched frame will let me."''',
     (0, KISS), (1, TALK))
text("unsold_evening", "near.reply.1", '''"I pretend for a living. Tonight I want the thing itself, or as much of it as the glass lets through."
{n}Her hand turns palm upward inside the frame.{/n}''',
     (1, TALK))
text("unsold_evening", "kiss", '''{n}Her image draws so close the candles behind her go out. She hooks a claw under the edge of her carapace at the throat and lifts it, a fraction, so that you see the pale seam beneath, the one place on her that is not armoured.{/n}
"Here. Your mouth here. I would not let you be gentle about it. Mine would already be inside that aggravating collar of yours, and I would be counting every sound you made, and making you make them again until I had them right."
{n}Her image opens the collar of her carapace the rest of the way, and her breath fogs the glass between you. One claw drags down the surface where your chest is, and you feel it anyway, a cold line from throat to belt.{/n}
{n}She watches your face. She is not imagining it; she is studying it, the way she studied the widow's.{/n}
"Now say something. I want to hear what this does to your voice."''',
     (0, GO_ON), (1, STOP))
text("unsold_evening", "jerribeth.unsold_evening.explicit.1", None, (0, GO_ON), (1, STOP))
text("unsold_evening", "frame", None, (0, '"Tell me."'))
text("unsold_evening", "story", None, (2, '"I have a war to run. I answer when I answer."'))
text("unsold_evening", "story.reply.2", None, (2, '"I have a war to run. I answer when I answer."'))
text("unsold_evening", "joke_disputed", '''{n}The amusement thins.{/n}
"A war. Yes, I have heard of it. It keeps taking you away from me."
{n}She considers you through the glass the way she considered the widow across her own table.{/n}
"Then I shall have to find out what in it is more interesting than I am, and take that away from you instead. Do not look alarmed. I have not decided which."''',
     (0, LEAVE_IT), (1, '"Leave my war alone."'))
text("unsold_evening", "joke_disputed.reply.1", '''"Tonight I will. Tonight is not every night."
{n}Her antennae move again.{/n}
"I can wait. I would like you to know that I am waiting, and what I am waiting with."''',
     (0, LEAVE_IT))
text("unsold_evening", "after", '''{n}She lets the widow's room go dark around her. Her hands stay pressed flat to her side of the glass, where yours were.{/n}''',
     (0, EVENING))
text("unsold_evening", "after.reply.3", '''"Then I have brought it. I expect you to be extravagantly pleased."
{n}Her next laugh is high and short and entirely satisfied.{/n}
{n}When another obligation draws near, you tell her how much time remains.{/n}
"Spend it here. I have wasted a perfectly good dining room on you. Your officers may have the next watch."
{n}She ends it herself, when she has had enough of you, which is a good while after you would have.{/n}''',
     (0, EVENING))

# ---- fate_envelope / fate_letter: the Trickster's letter, and what she wants to post with it ------
WRITE_ME = '"Then write to me. Nobody else. Me."'
UNRECALLABLE = '"I wanted a reply you could not take back."'

text("fate_envelope", "start", '''{n}Jerribeth's antennae rise. She glances toward the rest of Vellexia's house, where somebody behind a door is laughing much too loudly, before she gives you her attention.{/n}
"A less convenient answer. Everyone who says that to me expects to be applauded. What do you intend to make fate do?"
{n}You take a blank sheet, fold it once, and address it to yourself: not to a place, but to your next quiet evening, whenever and wherever that falls. There is no city beneath the name.{/n}
"You have forgotten where you live."''')
text("fate_envelope", "start.reply.1", '''{n}You fold the paper again. A second folded sheet presses against your fingers from inside the first, though there was no room for it. Its outer face bears the same address, in your hand.{/n}
{n}Jerribeth takes both out of your fingers before you can offer them, opens them, and compares their creases with the attention she gives a wing she means to pin.{/n}''')
text("fate_envelope", "test", '''"Two sheets. One reply. Let us see what travels."
{n}A pin appears between her claws. From the hem of the nearest curtain she plucks a moth, a fat grey one drunk on the lamp-heat, and drives the pin through it and through the first sheet together, slowly, watching its legs work.{/n}
{n}On the second sheet, in your hand, a small grey stain spreads where nothing has touched it. It twitches. Then it is still.{/n}
"Oh," {n}she says, very softly.{/n} "It carries."''',
     (0, WRITE_ME), (1, UNRECALLABLE), (2, '"It was meant to carry an answer. Not a death."'))
text("fate_envelope", "test.reply.1", '''"An answer, a death. You draw such fine distinctions, Commander."
{n}She writes a word inside the pierced sheet, shields it from you, and wipes it away with her thumb. For an instant the sheet in your hand darkens with it. Then it is blank again.{/n}
{n}Her amusement stops sounding polite.{/n}
"Do you understand what you have made? A letter the mistress of this house cannot open first. A letter that arrives before anyone under her roof could think to stop it. I could post a great many things to a great many evenings."''',
     (0, '"It has one address. Mine. The answer is yours to write."'))
text("fate_envelope", "test.reply.2", '''"For now."''', (0, WRITE_ME))
text("fate_envelope", "refused", '''{n}She tears her sheet through the address. The one in your hand loses its faint warmth.{/n}
"A reply I cannot take back? Commander, I gave a whole village new eyes, and I can take them back whenever I like. Nothing I give is past recall. That is why I am still alive in a house like this one."
{n}She drops the torn pieces into your palm, and the dead moth with them, and closes your fingers over all of it.{/n}
"Keep those. The experiment is finished. The moth was the interesting part."''')
text("fate_envelope", "purpose", '''"To me, then."
{n}She keeps the pierced sheet. You still hold the one with the stain. The two have stopped trying to resemble each other.{/n}
"What shall I write about? Be careful. I answer exactly the question I am asked, and I enjoy the gaps."''',
     (2, '"Take your time."'))
text("fate_envelope", "purpose.reply.1", '''"Oh, I shall. You have found a way to make waiting look clever. I should like to know whether answering will be worth my while."
{n}Her clawed hands close around the fold.{/n}
"I am not putting Vellexia's secrets in it. Not in a letter you can read before I have decided whose side I am on. Those cost more than you have offered."''')

KEEP_STAINED = '[Leave her the pierced sheet and keep the stained one for a quiet evening.]'
KEEP_ANSWER = '[Leave the answer with her and keep the stained sheet.]'
text("fate_envelope", "work", None, (0, KEEP_STAINED))
text("fate_envelope", "work.reply.1", None, (0, KEEP_STAINED))
text("fate_envelope", "company", None, (0, KEEP_ANSWER))
text("fate_envelope", "company.reply.1", '''"So you did. You may discover that I choose something which requires you to be interesting."
{n}She turns the pierced sheet over, considering the empty space around the pinhole.{/n}
"An evening without borrowing somebody else's room. That would be a promising start. I might wish to leave it halfway through. You might. We could discover whether either of us bothers."
{n}She folds the sheet and keeps it between two fingers.{/n}
"I will give you an answer when you are no longer watching me compose it. You may try to look less pleased about that. It is making me consider a deliberately tiresome one."''',
     (0, KEEP_ANSWER))

text("fate_letter", "start", '''{n}The stained sheet is no longer blank. The moth's mark is still there, a small grey ghost in one corner, and you find her words beside it while settling into a quiet evening, although no courier has come to ask where you meant to spend it.{/n}
{n}The first sentence sits at a sharp angle to the crease.{/n}
"I wrote this after you left. Your letter has been taking liberties with the order of events. I intend to make the next person who asks me to be impressed by that regret asking."
{n}Beneath it is a smaller line.{/n}
"If it arrived while you were busy, put it away. I decline to compete with a military emergency for the attention due to my handwriting."''')
text("fate_letter", "existing", '''{n}The frame lies where you left it, face down, which has never once stopped her.{/n}
{n}For now you have a drawing, a reply, and a small grey stain where a moth died on another sheet, a room away, to see whether your trick would carry it. It did. You have kept what she chose to send afterward.{/n}''')
text("fate_letter", "work",'''"A room with two doors. The one you run toward moves away while you run. The one you are running from comes closer. I want to put somebody in it who has disappointed me, and watch them learn which door to want. It will take them years. I have years."
{n}A drawing fills the lower corner: two doorways, and between them, very small, a figure in mid-stride. When you turn the paper over and back, the figure has turned too.{/n}
"You will want to tell me where to put a way out. Do. I should like to know where you think mercy goes in a room like this, so that I know exactly which wall to leave it off."
{n}The last line has been added beneath a small, impatient blot.{/n}
"I have not built it yet. I have a list of tenants."''',
     (0, '[Write back: give them a door they can see from the first step, and let the waiting be the cruelty.]'),
     (1, '[Write back: the way out is to stop running. Let them find that, or never.]'))
text("fate_letter", "answer", '''{n}You write your answer beneath hers. For a moment your words appear on the outside of the fold, as though the paper had forgotten which side of the conversation it belongs to. Then they settle.{/n}
{n}One more sentence appears in her hand.{/n}
"Do not post anything else on this paper. I have begun thinking of other things to send by it, and some of them would arrive before you could stop me."
{n}The writing stops. The letter remains a letter, for now.{/n}''')

# ---- refuge: D6, the footstool is staged before any branch leans on him -----------------------------
text("refuge", "start", '''{n}Jerribeth answers without showing herself. She has turned the frame outward, away from her face, so that you look where she is looking: a long room hung with silk, and in the middle of it a man in a courtier's coat on his hands and knees, perfectly still, with three full cups balanced along his back.{/n}
{n}He does not look up. He does not seem able to.{/n}''')


# --------------------------------------------------------------------------
def _node(scenes, scene, node):
    event = scenes["jerribeth." + scene]
    matches = [page for page in event["Nodes"] if page["Id"] == node]
    if len(matches) != 1:
        raise KeyError("jerribeth.%s/%s: expected one node, found %d" % (scene, node, len(matches)))
    return matches[0]


def apply(payload):
    scenes = {s["Id"]: s for s in payload["Scenes"] if s["Id"].startswith("jerribeth.")}
    for scene, title in TITLES.items():
        scenes["jerribeth." + scene]["Title"] = title
    for (scene, node), body in NODES.items():
        _node(scenes, scene, node)["Text"] = body.strip()
    for (scene, node, index), body in CHOICES.items():
        answers = _node(scenes, scene, node)["Choices"]
        if index >= len(answers):
            raise IndexError("jerribeth.%s/%s has no answer [%d]" % (scene, node, index))
        answers[index]["Text"] = body
    for (scene, node), extra in PARAS.items():
        _node(scenes, scene, node).setdefault("Paragraphs", []).extend(dict(x) for x in extra)
