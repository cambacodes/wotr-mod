"""Jerribeth base layer: Claude voice pass (edge-fix job 10, jerribeth-rebuild.md §5-§7).

Text only. Ids, Next, Set, Requires/Forbids, checks, costs and choice order belong to
the source modules and to jerribeth_scaffolding; this layer replaces player-visible
text on nodes that already exist and adds flag-gated paragraphs. Every key must
resolve: a missing scene, node or choice index is an error, never a silent skip.

revoice() runs in jerribeth_round2.integrate before the scaffolding (existing nodes);
fill() runs at the end of jerribeth_scaffolding.integrate (its new nodes and its
appended choices). Scenes written here are locked in tools/route_packs/voice_locks.json.

Canon used (enGB): 0b920731, 66d1f6a4, de70b6ee, eb28ad3b, c4630d76, 8ef95ea9,
b003e047, 74d54b7a, 31c32623. Authored, no canon claim: the gate-yard trick, the
caged cultist, the footstool courtier, the widow Aldane and her supper, Vardess as a
cambion in Drezen, Lieutenant Petrik, the Drezen cabinet room, the chancery clerk.
"""
from authoring.generation_errors import record, overlay_item, overlay_node
from story_format import p

PENDING = "[PROSE PENDING:"

PLANT = dict(requires=("jerribeth.marhevok_in_sanctum",),
             forbids=("jerribeth.marhevok_dead", "gesmerha.marhevok_rules", "jerribeth.trickster.returned"))

TITLES = {
    "commission": "Wintersun in one yard",
    "offered_signature": "The widow's supper",
    "room_measure": "Her cabinet in Drezen",
    "farewell": "The parting gift",
    "parting": "The frame turned to the wall",
}

# --------------------------------------------------------------------------
# Existing nodes (applied before the scaffolding runs).
# --------------------------------------------------------------------------
NODES = {}
CHOICES = {}
PARAS = {}


def text(scene, node, body, *choices, paras=()):
    NODES[(scene, node)] = body
    for index, choice in choices:
        CHOICES[(scene, node, index)] = choice
    if paras:
        PARAS[(scene, node)] = list(paras)


# ---- invitation ------------------------------------------------------------
text("invitation", "start", '''{n}Among the messages waiting for you is a small lacquered frame wrapped in paper. Where a portrait should be, a dark surface reflects nothing. A note lies against it.{/n}
{n}The handwriting is fine and rather impatient: I have acquired a correspondence charm. You attend to this side; I attend to the other. It carries a chosen image and spoken thoughts. Turning it over will stop you seeing me. It will not stop me seeing you. The charm looks both ways, and I have always preferred the better view.{/n}
{n}Below the instructions is a name: Jerribeth.{/n}''')

COURTESY = '"I will even let your companions hear us, if you like. As a courtesy. You see how eminently reasonable I am."'

text("invitation", "voice", '''{n}A narrow, insectile silhouette appears inside the frame. The voice that reaches your thoughts is familiar, high and lightly buzzing.{/n}
"At last. I began to suspect you were waiting for somebody to explain whether accepting a letter was a heroic act."
{n}One delicate hand lifts inside the image.{/n}
''' + COURTESY)

text("invitation", "voice_toast", '''{n}The Wintersun deserter from the Fool King's tavern brought it himself, at dawn, and would not say who had sent him. He looked as if he did not know.{/n}
{n}A narrow, insectile silhouette appears inside the frame. The voice that reaches your thoughts is high and lightly buzzing, and you have heard it once before, out of the wrong mouth.{/n}
"You drank to me. Now I am writing to you. That is how debts begin, Commander."
''' + COURTESY)

text("invitation", "voice_toast_levy", '''{n}The sergeant of the Wintersun levy who poured your toast brought it himself, at dawn, and would not say who had sent him. He looked as if he did not know.{/n}
{n}A narrow, insectile silhouette appears inside the frame. The voice that reaches your thoughts is high and lightly buzzing, and you have heard it once before, out of the wrong mouth.{/n}
"You drank to me. Now I am writing to you. That is how debts begin, Commander."
''' + COURTESY)

text("invitation", "test", '''{n}The image and voice cease. When you turn the charm back and invite her again, Jerribeth is exactly where she was, her hands linked together.{/n}
"Did you enjoy that? I did. You stared at the back of a frame for a count of thirty, and I watched you do it. Now, if you have finished testing the furniture, you might try being interesting."''')

text("invitation", "why", '''"Because you have a talent for changing arrangements that other people consider permanent. Because I would like to know what you want before somebody else learns how to offer it."
{n}The outline of an antenna trembles.{/n}
"And because I have been wondering whether you are as difficult to entertain as you are to predict. That part is personal."''',
     paras=(p('''"And because I offered you my mark once, so that my subjects would take you for one of our own. I remember everyone I have offered it to. There are not many, and most of them are on pins."''',
              requires=("jerribeth.mark_seen",)),))

text("invitation", "reject", '''{n}You wrap the charm again and send it back unopened. It makes no difference. For one moment, as the paper folded over it, the dark surface was facing your room, and you have the unpleasant conviction that she has already seen everything in it worth seeing.{/n}''')

# ---- question / guise --------------------------------------------------------
text("question", "answer", '''{n}For several moments she does not answer.{/n}
"I dislike being predictable. I dislike it more when someone is right about me."
{n}Her voice takes on an airy lightness.{/n}
"And I like it, a little, when they are. It makes me want to take them apart and see how they managed it. You may consider that a confidence. I have not decided whether you deserve a second one."''')

text("guise", "start", '''{n}The frame shows a furnished room, bright with reflected lamplight. Jerribeth waits within it. A slim elven figure stands where her insectile shape appeared before, but a deliberate shimmer along the edges reveals the projection.{/n}
"A room for you. I dressed it myself. And a face. Do you know why faces like this worked so well on Wintersun? I made them see demons as elves and dwarves and men, and they were so grateful to see something familiar that not one of them asked why it smiled so much."
{n}The elven image smiles.{/n}
"This one is also deliberate. Does knowing spoil it?"''')

# ---- price ---------------------------------------------------------------------
text("price", "refuse", '''{n}The silence lasts long enough for the projected room to fade at its edges.{/n}
"You want a confession. You will not get one. I would only perform it, and you would know, and then we should both be bored."
{n}Her next words are colder.{/n}
"I will give you something better than a confession. Your head stays yours. The charm shows what you invite, and nothing else. In exchange, you keep inviting me. Stop, and all of that lapses, and you have seen what I do in Wintersun when I have nothing better to amuse me. You are something better to amuse me. Do not stop being it."''')

text("price", "evict", '''"You cannot. That is the whole beauty of a lease."
{n}The buzzing drops to something you feel in your teeth.{/n}
"I will stay where I am, and pay my rent, and be quiet. You will find that the quiet is worse."''')

XANTHIR_OPEN = '''{n}She is working while she talks: one of Xanthir's locusts held between two delicate clawed fingers, a needle in the other hand. She pushes the needle in slowly, and watches the legs convulse, and does not look up until they stop.{/n}
"A lot of work, to preserve this beauty. You are looking at me as though you have remembered something unpleasant."
{n}She sets the locust on its card.{/n}
"Xanthir, perhaps. I wondered when you would bring him into one of our evenings."'''

text("price", "x_start", XANTHIR_OPEN)

# ---- evening ---------------------------------------------------------------------
text("evening", "late", '''"I remember everything, Commander. It is my worst habit and my best stock in trade."
{n}She stays. There is no image to admire now, and neither of you asks for one. She asks you questions she already knows the answers to, only to hear how you answer them, and she laughs, high and abrasive, each time you notice.{/n}
{n}When you finally part, she names the evening she wants next, and the hour, as though it were already pinned to a card and only you were missing from it.{/n}''')

# ---- patron ----------------------------------------------------------------------
text("patron", "personal", '''"If anyone breaks you, Commander, it will be me. Not Vellexia's boredom. She would lose interest halfway through and leave you lying where she dropped you, and I cannot abide unfinished work."
{n}She appears to consider leaving it there, and does not.{/n}
"Beware of her boredom. Do not let her lose interest in you. I have watched what happens to the things she stops looking at."''')

text("patron", "end", '''"Do not look so touched. I said break, not keep safe. I am particular about who handles my things."
{n}The irritation in her voice is almost affectionate, which is worse.{/n}
"Now listen carefully. I am going to tell you something useful, and I expect you to remember it when being foolish would make a better story."''')

# ---- collection -------------------------------------------------------------------
text("collection", "start", XANTHIR_OPEN)

# ---- refuge ----------------------------------------------------------------------
text("refuge", "start", '''{n}Jerribeth answers without showing herself. She has turned the frame outward, away from her face, so that you look where she is looking.{/n}''',
     paras=(
         p('''{n}It is a hall in Vellexia's house: lamps in coloured glass, guests reclining in their own smoke, music from somewhere you cannot see. The view drifts down to the floor beside a couch. A man in good clothes is there on his hands and knees, perfectly still. A wine cup stands on the small of his back. A succubus leans over and sets a second cup beside it without looking down.{/n}
"Vellexia gave me protection. People have been pricing me by what they think remains of it. This one priced me aloud, at her table. He told the whole room my protection had worn through and I would be easy to collect."
{n}The man's eyes roll up toward the frame. He cannot lift his head.{/n}
"Now he believes he is a footstool. He knows he is not; that is the delicate part. He simply cannot make his body agree. Vellexia was not bored for an entire evening. You have no idea what that is worth in this house. She keeps me for entertainments exactly like this one."''',
           forbids=("jerribeth.patron_lost",)),
         p('''{n}It is not Vellexia's hall. Bare walls, a borrowed couch, one lamp. On the floor beside the couch a man in good, ruined clothes kneels on his hands and knees with a wine cup balanced on the small of his back.{/n}
"I left the house. I did not leave my furniture. This one priced me aloud at Vellexia's table. He told the whole room my protection had worn through and I would be easy to collect."
{n}The man's eyes roll up toward the frame. He cannot lift his head.{/n}
"Now he believes he is a footstool. He knows he is not; that is the delicate part. He simply cannot make his body agree. I have lost a patron, Commander. I have not lost my touch."''',
           requires=("jerribeth.patron_lost",)),
     ))

text("refuge", "anger", '''"Among other things. I am capable of more than one thought, even when every thought is unpleasant."
{n}She rests one clawed foot on the kneeling man's shoulder while she talks, the way you might rest it on a fender. He does not make a sound.{/n}
"I chose refuge among dangerous people. I knew what could happen. That does not oblige me to enjoy discovering which possibility has occurred. It does oblige other people to watch me take it out on someone."''',
     (1, '[Set your cup down on the edge of the frame, where his back would be.] "Keep him."'),
     (2, '"Let him up."'))

text("refuge", "need", '''"Names. Introductions, if you have them. Information I can use without discovering that it has been sold to somebody else first."
{n}Under her foot, the footstool's cups tremble and do not spill.{/n}
"And an evening with the one creature in two planes who is not working out what I am worth tonight. I find that refreshing. I am also deeply suspicious of it."''',
     (2, '[Set your cup down on the edge of the frame, where his back would be.] "Keep him."'),
     (3, '"Let him up."'))

text("refuge", "stay", '''"Good. I have had enough reassuring inventions for one day."
{n}She begins with the practical problems: who has stopped answering her letters, who has started, who smiled at her yesterday with too many teeth. Halfway through an explanation she grows angry again, and lets you hear it without correcting herself into a more attractive performance.{/n}''',
     paras=(
         p('''{n}Every so often she shifts her foot on the kneeling man's back, and his arms shake, and the cup you gave him rattles once and is still.{/n}''',
           requires=("jerribeth.refuge_footstool_kept",)),
         p('''{n}The floor beside her couch is empty now. Her eyes keep going to it, the way a tongue goes to the gap where a tooth was.{/n}''',
           requires=("jerribeth.refuge_footstool_freed",)),
         p('''"I watched you, you know. While you decided what to do about my evening. You took longer than you think, and your face did several things you would not approve of. I enjoyed all of them more than the hall."'''),
     ))

# ---- the Marhevok answer shared by price, evening, patron and refuge ----------
# (marhevok_early_unknown is produced by jerribeth_round2.disclosure; one text.)
MARHEVOK_UNKNOWN = '''"Marhevok, the Wintersun chief. He loves me so passionately, so blindly. Where he is now, I have not troubled to learn."
{n}She watches your face with open interest.{/n}
"I could give you news, if you wanted it. I could make it any news you liked: dead, gone, married to a goat. You would believe me and sleep better. I would rather you did not sleep."'''
for _scene in ("price", "evening", "patron", "refuge"):
    text(_scene, "marhevok_early_unknown", MARHEVOK_UNKNOWN)

# ---- commission: Wintersun in one yard --------------------------------------------
text("commission", "start", '''{n}The lacquered frame wakes on your table without being asked. It does not show her. It shows the lower gate yard of the citadel at the change of the evening watch, seen from a little above and a little crooked, the way a tired man holds his head.{/n}
{n}A picket stands at the inner gate with his spear levelled. Across the yard, something horned and grey-skinned is walking toward him in your coat, with your walk.{/n}
"You carried my frame through that gate this morning, Commander. It looks wherever it is carried. I took the opportunity."
{n}The picture tilts down, through a grate, into the cells. A man in a Baphomet cultist's rags stands at the bars with his chin up. The turnkey is unlocking the door for him and saluting.{/n}
"The sergeant sees a demon in your coat. The turnkey sees you, and you have just ordered the postern opened. I merely planted a few ideas in their heads. It is elegant in its simplicity."
{n}Her laughter arrives inside your skull, high and abrasive, like a buzzing insect.{/n}
"He will reach the postern by the time the bell stops. Your sergeant will put his spear through the demon well before that. Which do you think will make the better story in the mess tomorrow?"''',
     (0, '"Undo it. Now."'),
     (1, '[Go down to the yard.]'))

text("commission", "ask", '''"Undo it? I have only just finished."
{n}In the frame, the cultist steps out into the passage. The turnkey holds the lamp for him.{/n}
"Very well. Undoing is work. Give me the man in the cell. He served my old master, and I served that master exactly as long as it profited me more than it cost me. I should like something of Baphomet's on my shelf. He will be alive. He will be awake. He simply will not be yours."
{n}A pause, savoured.{/n}
"Or keep him, and give me something of yours instead. Tell me what it is like to watch your own soldiers level a spear at you because they see a monster. Tell it truly. I shall know if you dress it."''',
     (0, '[Go down and break it yourself.]'),
     (1, '"Take the cultist. End it."'),
     (2, '"Keep your hands off him. I will pay the other price."'))

text("commission", "beauty", '''{n}The yard is colder than the picture. The bell has begun. Sergeant and picket stand shoulder to shoulder at the inner gate, and both of them look at you with the white-eyed hatred soldiers keep for demons.{/n}
"Stand there, fiend!" {n}the sergeant shouts. His voice cracks on the last word.{/n}
{n}Across the yard the postern bar is already lifting. The man lifting it wears rags and an expression of perfect obedience to an order you never gave.{/n}
{n}Jerribeth speaks inside your skull, close and pleased.{/n}
"Look at them. Not one of them doubts their eyes. Mortals never do; it is the most generous thing about you. Now, Commander. Show me what you do with a yard that sees you as it sees me."''',
     (0, '[Persuasion DC 24] [Talk in your own voice and trust the words to get through the face.] "Sergeant. Lower that spear and listen to what I am telling you."'),
     (1, '[Perception DC 20] [She always leaves a seam. Find it, and make the sergeant look at it.]'))

text("commission", "keep", '''"There. Now you have seen what I did to Wintersun, done small, done in your own yard to your own people. Every one of them was perfectly certain. That is the part I love. Not the lie. The certainty."
{n}The frame on your table cools. For a moment you see her own narrow shape inside it, hands linked, antennae trembling with satisfaction.{/n}
"You may tell me it was cruel. I shall agree. You may tell me it was beautiful. I shall agree with that as well, and enjoy it more."''',
     (0, '"It was beautiful. Next time, let me watch it from your side."'),
     (1, '"It was beautiful. Save the next one for after the war, and tell me then what it will cost me."'))

# ---- offered_signature: the widow's supper ---------------------------------------
text("offered_signature", "start", '''{n}The frame is waiting on your table with a letter pinned to it by a single long needle. The paper smells of orange water. The hand is round and careful and very old.{/n}
{n}The widow Aldane, of the upper town, begs the honour of an evening in the Commander's private company at her supper table. She names the sum she has already paid to "the Commander's intimate acquaintance" for arranging it. She has underlined "private" twice.{/n}
"I accepted," {n}Jerribeth says inside your head.{/n} "In your name. Weeks ago. Do not look at me like that; you were busy."
{n}In the frame, her narrow shape tilts, delighted with you.{/n}
"Tonight I shall sit at the head of her table wearing your face, and eat nothing, and charm her daughters. You will come too. I have made you a face of your own: some minor cousin of the house, dull enough to be seated below the salt. You will watch yourself dine. Making deals with demons is a losing game; she ought to have known. Lucky for her, I so enjoy playing at mortals that I will keep up the act all evening."''',
     (0, '"Show me this supper."'),
     (1, '[Let the widow wait for another night.]'))

text("offered_signature", "offer", '''{n}The widow's house is narrow and tall and too warm, and everything in it that can be gilded has been. You come in at the tail of the guests under the face Jerribeth lent you. Nobody looks at you twice. Nobody is meant to.{/n}
{n}At the head of the table sits the Commander of the crusade.{/n}
{n}It is a very good likeness. It has your scar and your way of holding a cup. It is warmer than you are and smiles more, and the widow, a small woman in mourning silk thirty years out of fashion, cannot take her eyes off it. The Commander's plate stays full all evening. Nobody notices but you.{/n}
"Do you like it?" {n}Jerribeth asks inside your head, while your face at the head of the table tells the widow's eldest daughter a story about Kenabres.{/n} "I have improved your manners. Not your face. Your face I would not touch."''',
     (0, '[Watch the widow.]'),
     (1, '[Listen to what the table says she paid.]'))

text("offered_signature", "impression", '''{n}The widow does not eat either. She watches the false Commander lift a cup, set it down, laugh. She receives each small movement as if it were addressed to her alone, and when your face turns her way and says her name, she closes her eyes for a moment like a woman in church.{/n}
"Look at her. Thirty years of suppers in this house and never anyone at the head of the table she wanted. She does not want you, you understand. She wants to be the woman the Commander came to. I am giving her exactly that, and she will never, ever be able to give it back."''',
     (0, '[Wait for the end of the night.]'))

text("offered_signature", "price", '''{n}Two merchants' wives below the salt are discussing it behind their napkins. Forty crowns, says one. Sixty, says the other, and a set of silver from her husband's brother, and the deed to a house in Kenabres that is not there any more. Neither of them says to whom.{/n}
"Sixty, and the silver," {n}Jerribeth supplies.{/n} "Paid in advance, to a gentleman she has never met, who does not exist. She sold her husband's spoons to sit across a table from you for three hours. You should be flattered. I am."''',
     (1, '"You took her money."'))

text("offered_signature", "price.reply.1", '''"Of course I took her money. I am a demon. What did you think I would take, her gratitude? I have that as well. I have taken everything she offered, and before the candles go out I shall take one thing more."''',
     (0, '"What thing?"'))

text("offered_signature", "ownership", '''{n}The candles are down to their sockets. The daughters have gone up. The widow walks the false Commander to the door herself, her hand on its sleeve, and you stand in the passage behind them with your borrowed face and your hat in your hands like any poor relation.{/n}
{n}At the threshold, your face bends and kisses the widow's knuckles. She makes a small sound.{/n}
"Now," {n}Jerribeth says.{/n} "The part I came for."''',
     (2, '"What are you going to do to her?"'))

WIDOW_CALL = (
    (0, '"Let her have her evening. All of it."'),
    (1, '"Not my face. If she must see someone in that doorway, give her her husband\'s."'),
)
text("offered_signature", "ownership.reply.1", '''"One idea. Only one; I am not greedy. For the rest of her life, every man who comes through that door will be you. The baker's boy. Her sons-in-law. The priest who comes to bury her. Each time she will look up, and her heart will stop, and a moment later she will know that it is not you and never was, and that she paid for this."
{n}At the door, the widow is still holding your face's hand.{/n}
"She will be awake for all of it. That is what makes her a specimen and not merely a ruin. I shall come and look at her now and then. Well, Commander? You were her guest as well."''',
     *WIDOW_CALL)

text("offered_signature", "performance", '''{n}Nothing visible happens. Your face straightens from the widow's hand, puts on its hat and goes out into the street. The widow stays in the doorway after it has gone, smiling at the dark.{/n}
{n}Then her porter comes up the steps behind her with the lamp, and she turns and looks at him, and her whole small body goes still with joy. A breath later it goes still with something else.{/n}
"There. Pinned. She will hold that pose for twenty years if her heart lasts, and I think it will. Hearts like hers are tough. They have had so much practice at wanting."''',
     (1, '"You enjoyed that."'))

text("offered_signature", "performance.reply.1", '''"Enormously. So did you, a little. I felt it."
{n}Somewhere you cannot see, she weighs the widow's purse; you hear the coins shift inside your head.{/n}
"Sixty crowns, and the spoons. Shall I give you half? You did sit through the soup."''',
     (0, '"Keep it. Let us go."'))

text("offered_signature", "design", '''"Her husband's face? Oh. Oh, Commander."
{n}At the door the false Commander straightens from the widow's hand, and is not you any longer. It is a heavy man of sixty in an old-fashioned coat, with a soldier's moustache and a soft, ruined look about the eyes. The widow's hand stays on his sleeve. She has stopped breathing.{/n}
{n}He says her name in a voice nobody has heard in this house for eleven years. He takes her back in, and at the head of the cleared table, by the last candle, he sits with her for one supper more, and eats nothing, and listens. Then he puts on his hat and goes down the steps and away, and she stands in the door and watches him leave her a second time.{/n}
"That is better than mine. That is much better than mine. I would have given her a lifetime of disappointment. You gave her one supper and then took him back. She will never know whether to thank you."''',
     (0, '"Take me home."'))

text("offered_signature", "send", '''{n}You walk out together, the false Commander a pace ahead, into the cold of the upper town. Two streets on, under a lamp, your face turns round and looks at you with Jerribeth's attention behind it, and smiles a smile you have never once used.{/n}
"Thank you for a lovely evening. You were a very dull cousin. I was a magnificent you."''',
     (1, '"Take my face off. Now."'))

text("offered_signature", "send.reply.1", '''{n}The face goes out like a lamp. There is only the street, and your own breath, and her voice in your head, very pleased.{/n}
"You say the most encouraging things when you stop trying to improve me. Go home. I want to think about her for a while."''',
     (0, '[Go home.]'))

# ---- unsold_evening -----------------------------------------------------------------
text("unsold_evening", "start", '''{n}The projected room is bare tonight: a table, two chairs, one lamp, and nothing on the table at all. Jerribeth has made the emptiness conspicuous.{/n}
"I considered putting flowers there. Then I imagined you asking who they had belonged to."''',
     paras=(
         p('''"This is the widow's evening. She paid sixty crowns and her husband's spoons for an evening of yours, and I collected it. I could sell it again. I find I would rather spend it."''',
           forbids=("jerribeth.sale_withdrawn",)),
         p('''"This is the evening the widow paid for. You would not let her have it, so now you owe it to me instead, and I am collecting. I could have sold it again. I find I would rather spend it."''',
           requires=("jerribeth.sale_withdrawn",)),
     ))

text("unsold_evening", "start.reply.1", '''"An even more dangerous question."
{n}She reaches toward the empty space beside her, then stops short of furnishing it.{/n}
"I can show you the room while we talk. Or we can dispense with the scenery, and you can look at me."''')

text("unsold_evening", "after.reply.3", '''"Then I have brought it. I expect you to be extravagantly pleased."
{n}Her next laugh is high and short and entirely satisfied.{/n}
{n}When another obligation draws near, you tell her how much time remains.{/n}
"Spend it here. I have ruined a perfectly good lamp for you. Your officers may have the next watch."
{n}She ends it herself, when she has had enough of you, which is a good while after you would have.{/n}''')

# ---- borrowed_sun ---------------------------------------------------------------------
text("borrowed_sun", "start", '''{n}The room Jerribeth projects tonight contains a small unfinished landscape on a table. A pale disc hangs above it, casting light without warming the painted roofs.{/n}
"A study. Not for sale. Not for anyone, until tonight."
{n}As you look, a doorway acquires a standing figure. Its face is blank.{/n}
"You recognise the problem already. I can hear how carefully you are waiting."''')

text("borrowed_sun", "remain", '''{n}For several breaths she offers neither an excuse nor a new display. Then she brings the altered model closer to the charm.{/n}
"Look at it once more. This version. Tell me whether the light reaches the far side."
{n}You lean toward the frame. She follows your gaze, moving the pale disc by a small amount until its light reveals the changes you asked for.{/n}
"There," {n}she says.{/n} "I changed it for you. Remember that I can. Remember also that I can change it back, and that I liked it better the first way. Now come closer. I want to watch you look."
{n}She leaves the model where you can both see it for the rest of the conversation.{/n}''')

text("borrowed_sun", "part", '''"Then go and be good somewhere else."
{n}She moves the study beyond the frame. Her own face remains until you reach for the charm.{/n}
"I learned exactly where you would leave. It was where I expected. How very disappointing of you."
{n}The connection ends under your hand. Nothing in Wintersun changes with it.{/n}''')

# ---- counterfeit_guest -------------------------------------------------------------
text("counterfeit_guest", "start", '''{n}Inside the frame, Jerribeth has a little puppet theatre: real lacquered wood and gilt, sent to her as a gift. Its curtain rises on a figure in an absurd crown. The face is a guess at yours. The figure kneels to a tall insect figure in a black gown, and holds the kneel until it looks painful.{/n}
"May I be useful?" {n}Jerribeth says, in a dreadful imitation of a soldier's voice.{/n} "May I conquer something small enough to fit beneath your chair?"
{n}She stops working the strings. The puppet's smile remains.{/n}
"Somebody has sent me this. He means to perform it at his salon, here in Drezen, as 'the demon and her crusader'. He believes I shall be delighted."''',
     (0, '"Who does he think he is?"'),
     (1, '[Leave the theatre until you have time for it.]'),
     (2, '"Did the widow\'s supper bring him to you?"'),
     (3, '"Is this about what I did at the widow\'s table?"'))

text("counterfeit_guest", "previous_buyer", '''"Of course it is. The upper town has talked of nothing else. Half of them say the Commander dined at the widow Aldane's, and half say a demon did, and both halves are right. That is the kind of gossip that travels."
{n}She makes the little crowned figure bow.{/n}
"He heard. He put two and two together and made a theatre."''',
     (1, '"So he wants a performance."'),
     (2, '"Then the widow\'s supper has bought us a guest."'))

text("counterfeit_guest", "previous_buyer.reply.1", '''"He wants a great deal more than a performance. Let me introduce him."''')

text("counterfeit_guest", "maker", '''"Vardess. He buys other people's inventions and shows them at his own table as though he had dreamed them himself. He keeps the best salon in Drezen: officers, merchants' wives, a priestess or two. He has wanted me at it for some time."
{n}She turns the card that came with the theatre so you can read it. The hand is elegant and pressed too hard.{/n}
"Someone told Vardess where I spend my evenings, and with whom. Vardess offers me a Commander who kneels. Such solicitude."''',
     (2, '"What does he really want?"'))

text("counterfeit_guest", "maker.reply.1", '''"To show it with my approval. The Commander at my feet. Me at his table, acknowledging that he has supplied something I wanted. Everyone in the room beneath someone else. He will consider the arrangement elegant."
{n}She makes the crowned figure straighten. Its head turns toward her with the same fixed smile.{/n}
"The face is poor. The obedience is worse."''',
     (0, '"Send it back with that opinion."'),
     (1, '"He wants to show you what he thinks you want. What will you show him instead?"'))

text("counterfeit_guest", "return", '''"And let him put it on without me? He would, with a sorrowful little speech about my absence."
{n}She closes one wing against her back. The other catches the edge of the theatre and pushes it aside.{/n}
"No. I am going to his salon. I have a better entertainment in mind than his."''',
     (1, '"He is counting on you being offended."'))

text("counterfeit_guest", "return.reply.1", '''"Yes. I would find this easier if he were entirely stupid. He is not. He is only vain, and vanity always leaves something showing."
{n}She tilts the theatre to the light. Under the crowned puppet's crown, the carver has left a shallow ridge on each side of the brow, as though the model had once worn something there and had it filed down.{/n}
"Now why would a man carve horns on my crusader and then file them off?"''',
     (0, '[Look closer.]'))

text("counterfeit_guest", "appetite", '''"His own face, perhaps. Begging the room to admire an invention he could not make."
{n}Her amusement buzzes against the last word. Then she stops, considering the puppet.{/n}
"Too obvious. He will have prepared for that. He might even enjoy seeing himself at the centre of the evening."''',
     (1, '"Then take the centre away from him."'))

text("counterfeit_guest", "appetite.reply.1", '''{n}Jerribeth looks up. The motion is quick enough to disturb the image around her antennae.{/n}
"Now you are being helpful."
{n}She lifts the crowned puppet out by its strings. Under the crown the carver has left a shallow ridge on each side of the brow, filed smooth.{/n}
"Look. He has carved himself into my crusader without meaning to. Men always do."''',
     (0, '[Look closer.]'))

text("counterfeit_guest", "lining", '''{n}She turns the little theatre round. Behind the painted backdrop the maker has fitted a second, smaller figure on its own rod: a gentleman in a tall fashionable cap, who bows to the audience in the same instant the crusader kneels. When she works the rod the cap tilts, and for an instant there is something under it that is not hair.{/n}
"Vardess," {n}Jerribeth says.{/n} "He put himself in the play. He could not resist. And he carved himself honestly, because he never imagined anyone would look behind the backdrop."
{n}She tips the little cap back with one claw. Two filed stumps of horn.{/n}
"A cambion. Living in your city in a mortal's coat, under a fashionable hat. I do so love a guise worn badly."''',
     (0, '"Then let him wear it to his own salon one last time."'),
     (1, '"I want to see his face when his guests see what is under that cap."'))

text("counterfeit_guest", "square", '''"So do I. But I should like to be sure before I spend an evening on him. Fashionable caps are not proof. Filed horns can be a carver's joke."
{n}The frame shows you a street through her eyes: a tall house below the citadel, lamps at the door, servants carrying chairs in for tonight.{/n}
"His house is a quarter of an hour from where you are sitting. Go and look at him. I want to know what you see, Commander."''',
     (2, '"I trust your eyes. No need to look."'),
     (3, '[Perception DC 30] [Go and watch him come and go from his own door.]'),
     (4, '[Knowledge (World) DC 30] [Go and ask after him along the merchants\' street, and test his story against what you know of Drezen.]'))

text("counterfeit_guest", "square.reply.1", '''"You trust my eyes. How reckless of you. Then we shall both be surprised together."''',
     (0, '"Then I will come as your guest."'),
     (1, '"I will come. Do not mistake that for approving everything you will do there."'))

text("counterfeit_guest", "judgment", '''"I had not mistaken you for an admirer of every use I make of anything. Your conversation has made that difficult."
{n}She leaves the theatre turned toward you.{/n}
"You may dislike the work and still enjoy the evening. Most of my guests manage it."''',
     (1, '"You invited me."'))

text("counterfeit_guest", "judgment.reply.1", '''"And you have become very pleased about it. I should never have taught you to notice."''',
     (0, '[Agree to come.]'))

text("counterfeit_guest", "keep", '''{n}Jerribeth lifts the crown from the puppet and sets it on the empty chair beside her in the frame. It fits there better.{/n}
"He has kept a chair for me at the head of his salon tonight. An empty chair, for the mistress of the evening; it is how he advertises that I am coming without having to produce me. Sit near it. I shall be in it, in my fashion."''',
     (1, '"Will he know you are there?"'))

text("counterfeit_guest", "keep.reply.1", '''"Tonight, then. He will not know I am there until I want him to. Then he will know all at once, and so will everyone else."
{n}She works the strings one last time. The crusader kneels. Behind the backdrop, the little gentleman in the cap bows.{/n}
"Bring whatever face you wear when you mean to make someone regret underestimating you. I have become rather fond of it."''',
     (0, '[Go to Vardess\'s salon tonight.]'),
     paras=(p('''"And Commander: if your inquisitors trample my evening, I shall remember whose boots they were."''',
              requires=("jerribeth.vardess_reported",)),))

# ---- counterfeit_audience -------------------------------------------------------------
UNMASK = '''{n}Vardess straightens from his bow, and every mirror in the room shows him as he is.{/n}
{n}Not much has changed. That is the horror of it. The same handsome face, the same high collar. But in the glass the velvet cap is gone, and from his brow rise two thick horns, filed to stumps and grown back an inch, red at the root; and the eyes are wrong; and the hand resting on the theatre has too many joints.{/n}
{n}The room sees it a heartbeat before he does. A merchant's wife drops her glass. Then Vardess looks up into the great mirror over the hearth and sees himself, and sees his guests seeing him: a demon, in front of everyone he has spent years making into friends.{/n}'''

GRAB = '''{n}Vardess does not scream. He moves. He has young Lieutenant Petrik by the collar before anyone else has moved at all, a knife out of his sleeve and at the boy's throat, and he is dragging him backward toward the tall doors.{/n}'''

text("counterfeit_audience", "start", '''{n}Vardess's salon takes up the whole first floor of his house, and every wall of it is mirror. Officers of the crusade in their good coats, merchants' wives, a priestess of Iomedae with her hands folded, a very young lieutenant named Petrik showing off his new sword: all of them doubled and redoubled into a crowd ten times its size. At the head of the room stands a gilded chair with nobody in it.{/n}
{n}You take a place near the chair. The air beside it is colder than the rest of the room.{/n}
"Good evening, Commander," {n}Jerribeth says inside your head.{/n} "Do sit down. The show is about to begin, and I have been looking forward to this one all week."''',
     (0, '[Watch for Vardess.]'))

text("counterfeit_audience", "entrance", '''{n}He makes the entrance he has rehearsed. The tall doors at the end of the room open on darkness. His voice reaches the guests before he does, and then the lamps behind him flare so that every head must turn. Vardess walks out of the light in a high collar and a tall velvet cap, carrying the little theatre in both hands like a reliquary.{/n}
"Friends. Tonight, by the gracious leave of a lady who cannot be with us in the flesh..." {n}He bows to the empty chair. The room laughs, delighted and a little frightened.{/n} "The demon and her crusader."
{n}He sets the theatre on its stand. The crowned puppet kneels to the insect queen. Behind the backdrop, the little gentleman in the cap bows.{/n}
"He would like the room to believe I am his guest," {n}Jerribeth murmurs.{/n} "Shall I let him finish his bow?"''',
     (0, '"Let him finish. Then take it away from him."'),
     (1, '"Now."'),
     (2, '[Regill is watching the mirrors, not the stage.]'),
     (3, '[Lann has started grinning.]'),
     (4, '[Wenduag has leaned forward.]'))

text("counterfeit_audience", "challenge", UNMASK + '''
"I make people see demons as men," {n}Jerribeth says, very softly, inside your head,{/n} "and men as demons. Tonight I am only letting them see a demon as a demon. It is almost honest of me. Commander, look. Look at his face."
''' + GRAB,
     (0, '[Shout for the room to look at the mirrors.]'),
     (1, '[Make him look at himself.]'),
     (2, '[Cut him off from the doors.]'))

text("counterfeit_audience", "testimony", '''{n}"Look at the mirrors!" Every guest in the room obeys, and in the mirrors there is nowhere for him to go: a hundred horned Vardesses dragging a hundred lieutenants toward a hundred doors, all of them watched. He falters, dazzled by himself. It is enough. You are on him, and the knife is on the floor, and Petrik is crawling clear.{/n}''',
     (0, '[Pin him where the room can see.]'))

text("counterfeit_audience", "replay", '''{n}Jerribeth hears you. Every mirror in the room turns its face toward Vardess at once, so that wherever he looks he meets himself, horned and frightened. He stops dead, staring, the knife forgotten at Petrik's throat. You take it out of his hand the way you would take it from a child, and put him on the floor.{/n}''',
     (0, '[Keep him down.]'))

text("counterfeit_audience", "missing", '''{n}You do not chase him. You go round him, three long strides to the tall doors, and you are standing in them when he arrives. He has nowhere to go but through you. He tries. It goes badly for him. Petrik gets clear with a cut collar and a story he will tell for the rest of his life.{/n}''',
     (0, '[Hold him there.]'))

text("counterfeit_audience", "leverage", '''{n}The salon is silent except for Vardess's breathing. In the mirrors the crowd looks from the thing under your knee to you, and back.{/n}
"Well," {n}says Jerribeth.{/n} "Now there is the small matter of what to do with him."''',
     (2, '"What do you want with him?"'))

text("counterfeit_audience", "leverage.reply.1", '''{n}He looks up at you from the floor. Without the cap he is younger than you thought, and much more frightened.{/n}
"Commander. Commander, please. I have done nothing in this city but sell pictures..."
{n}Inside your head, Jerribeth's voice is warm and close.{/n}
"This can end two ways. Give him to your crusade: the inquisitors take him out of here in chains, there is a trial, then the square and the smell. Everyone in this room will say for years that they were here the night the Commander unmasked a demon. Or give him to me. Tell them it was a masque. My masque. They will be delighted to believe it, and Vardess will leave with his guests, and nobody in Drezen will ever see him again."
"He is unique, you know. A cambion who wanted so badly to be a man that he made himself one out of a hat. I cannot allow such a creature to disappear entirely."''',
     (0, '"Give him to the Inquisition."'),
     (1, '"Tell them it was a masque. He is yours."'),
     paras=(p('''{n}Downstairs someone is hammering on the street door. You told the Inquisition. They have come.{/n}''',
              requires=("jerribeth.vardess_reported",)),))

text("counterfeit_audience", "expose", '''{n}They take him out in chains. He does not fight. He keeps turning his head toward the mirrors as they lead him past them, as if to check, and each time the glass shows him the same thing.{/n}
{n}Within the week there is a trial. Within two, a fire in the square below the citadel. Half the guests from his salon come to watch, and tell each other they always knew.{/n}
"You have robbed me," {n}Jerribeth says.{/n} "He was mine. I found him, I unmasked him, I brought you to him, and you handed him to men with torches. Do not imagine I shall forget it."
"I think I shall come and look at the ashes. One should pay one's respects to a lost specimen."''',
     (0, '[Leave the house.]'))

text("counterfeit_audience", "archive", '''{n}You stand up. You straighten your coat. You tell the room, in the voice you use for victories, that the Commander's friends have been honoured tonight by a masque from a very old acquaintance of the Commander's, and was it not good?{/n}
{n}A heartbeat. Then the priestess begins to clap. Then everyone does. In the mirrors the horns are already gone, and Vardess, white to the lips, is bowing.{/n}''',
     (1, '"Now take him."'))

text("counterfeit_audience", "archive.reply.1", '''{n}He leaves with his guests. That is what everyone says afterward: that Vardess saw the last of them down the steps himself, cap and collar and all, laughing at his own masque. Nobody saw him go back in. His servants wait up for him until dawn.{/n}
"Thank you, Commander," {n}Jerribeth says, in a voice like a needle sliding home.{/n} "I have him. He is perfectly safe. He will never be anywhere else."''',
     (0, '[Leave the house.]'))

text("counterfeit_audience", "departure", '''{n}Outside, the street is cold and very ordinary. The crowned puppet lies on the steps where someone dropped it in the crush, face up, still smiling. You pick it up without quite meaning to.{/n}
"He spent years making Drezen believe he was a man," {n}Jerribeth says.{/n} "I undid it in one evening, with a roomful of mirrors. That is the whole of my art, Commander. Everything else is waiting."''',
     (1, '"You enjoyed that."'))

text("counterfeit_audience", "departure.reply.1", '''"I still am. It has improved my week considerably."
{n}The puppet's head turns in your hand to look at you. Its smile stays where it is.{/n}
"Keep that. I shall send for it. Go home, Commander, and wash that parquet off your knees."''',
     (0, '[Go home.]'))

# ---- counterfeit_spoil (frame) -----------------------------------------------------------
text("counterfeit_spoil", "start", '''{n}Jerribeth is at her worktable. A long, shallow drawer stands open beneath it, lined with black velvet. She closes it as you open the connection, then draws it out again, slowly, so that you can watch it come.{/n}
"I promised to show you what I keep in here. I always keep my promises when they are cruel enough."''',
     (0, '"Show me."'),
     (1, '"Show me."'),
     (2, '[Look into the drawer.]'),
     (3, '[Look into the drawer.]'))

# Old-save paths (parked after the retired counterfeit_clerk): short, converge on price.
text("counterfeit_spoil", "return", '''{n}In the drawer: Vardess's tall velvet cap, folded flat, and a card in his overpressed hand. Nothing else.{/n}
"His leftovers. The rest is in the next drawer down. I am savouring this."''',
     (0, '[Wait for the next drawer.]'))

text("counterfeit_spoil", "circles", '''{n}In the drawer: Vardess's tall velvet cap, folded flat, and a card in his overpressed hand. Nothing else.{/n}
"His leftovers. Patience, Commander."''',
     (1, '"Show me the rest."'))

text("counterfeit_spoil", "circles.reply.1", '''"Patience. I have waited all week to watch you look."''',
     (0, '[Wait for the next drawer.]'))

text("counterfeit_spoil", "work", '''{n}She draws out the next drawer beneath it, inch by inch.{/n}''',
     (2, '[Look.]'))

text("counterfeit_spoil", "work.reply.1", '''"Go on. I made it for you to see."''',
     (0, '[Look.]'),
     (1, '[Look.]'))

text("counterfeit_spoil", "account", '''{n}It is empty: black velvet, a row of bare pins, a hollow pressed into the nap where something was meant to lie.{/n}
"That is where he would have gone. Your inquisitors have him now. Had him. There were ashes."''',
     (1, '"And?"'))

text("counterfeit_spoil", "account.reply.1", '''"And I have a hole in my velvet, and you put it there."''',
     (0, '"You will get over it."'))

text("counterfeit_spoil", "account.reply.2", '''"I never get over anything, Commander. I collect it."''',
     (0, '[Let her close the drawer.]'))

text("counterfeit_spoil", "catalogue", '''{n}Vardess is in it, small on the velvet, pinned through below the breastbone, his horns polished. His eyes move. They find the frame, and you.{/n}
"I cannot allow such a unique creature to disappear entirely. So I have preserved him. In some form."''',
     (1, '"He is awake."'))

text("counterfeit_spoil", "catalogue.reply.1", '''"Of course he is awake. What would be the point of him otherwise?"''',
     (0, '[Let her close the drawer.]'))

text("counterfeit_spoil", "price", '''"There. Now you have seen it."''',
     (3, '"What now?"'))

text("counterfeit_spoil", "price.reply.1", '''{n}She leaves the drawer half open, so that only its edge catches the light.{/n}''',
     (0, '"I am glad he can never do it again. I am not glad of the rest."'),
     (1, '"He was more interesting loose than he is pinned. You know that."'),
     (2, '"You were very good at frightening him. I enjoyed watching."'),
     paras=(
         p('''"He hears everything we say, you know. I leave the drawer open a crack in the evenings, so that he can listen. Shall I let him speak to you? Once. Or would you rather I took his eyes, so that you never again have to wonder whether he is watching you?"''',
           requires=("jerribeth.counter_private_archive",)),
         p('''"Do not imagine the debt is a figure of speech. I shall come for it. If you refused it just now, that was charming of you, and I shall enjoy collecting all the more."''',
           requires=("jerribeth.counter_public_account",)),
         p('''"Now. Tell me what you thought of my evening."'''),
     ))

text("counterfeit_spoil", "object", '''"You need not lay a wreath. I watched your face when I unmasked him. It was not grieving, Commander."
{n}She turns the lamp down. The drawer's brass handle vanishes into shadow.{/n}
"You looked at me differently afterward. I noticed. I am still noticing."''',
     (1, '"Good."'))

text("counterfeit_spoil", "object.reply.1", '''{n}A brief chitter breaks the silence.{/n}
"Good. I should dislike becoming easy to admire through inattention."''',
     (0, '"Then show me what else you made tonight."'))

text("counterfeit_spoil", "interest", '''"A dangerous argument. You are asking me to consider whether something might be more entertaining if I leave it loose."''',
     (1, '"You leave things loose sometimes."'))

text("counterfeit_spoil", "interest.reply.1", '''"Never on purpose."''',
     (0, '"Then start."'))

text("counterfeit_spoil", "interest.reply.2", '''{n}Her hands separate. She considers the empty space between them.{/n}
"Loose things run. Loose things go to inquisitors. Loose things say no to me."''',
     (0, '"I am loose."'))

text("counterfeit_spoil", "interest.reply.3", '''"Yes," {n}she says.{/n} "I had noticed. Do not spoil an agreeable thought by explaining it to me."''')

text("counterfeit_spoil", "complicit", '''{n}The antennae lift.{/n}
"I liked having you there when he understood. He meant me to kneel in his little play. Instead he knelt in his own salon, in front of all his friends, and you were the one holding him there."''',
     (1, '"You made him suffer longer than you needed to."'))

text("counterfeit_spoil", "complicit.reply.1", '''"Much longer. I enjoyed how politely you neglected to stop me. I shall remember the expression you brought for it."''',
     (0, '"Show me what else you saved for tonight."'))

text("counterfeit_spoil", "complicit.other_reply", '''"I did. He meant to make me kneel. Instead he knelt in front of everyone he had ever fed. I shall remember the expression you brought for that."''',
     (0, '"Show me what else you saved for tonight."'))

text("counterfeit_spoil", "end", '''{n}She sets a little crowned figure on the table beside the drawer. It is Vardess's crusader, with the face sanded away to bare wood.{/n}
"The original was a bad likeness. I have made an improvement."''')

text("counterfeit_spoil", "end.reply.1", '''"By admitting I do not know what you will do next. I had you kneeling in his play. You did not kneel."''',
     (0, '"It is still a bad likeness."'))

text("counterfeit_spoil", "end.reply.2", '''{n}She makes the faceless figure bow, and lays it in the drawer on the velvet, beside whatever else is there.{/n}
"Then come and sit for a better one. I have begun to want your face where I can see it every evening, Commander, and I do not mean on a puppet."''',
     (0, '[Accept the invitation.]'))

# ---- room_measure: her cabinet in Drezen ---------------------------------------------------
text("room_measure", "start", '''{n}The note comes by an agent you have never seen and will not see again: an address in the upper town, a key, and one line in her fine, impatient hand. Come up. Bring whoever you like. I am here.{/n}
{n}Here. Not in the frame.{/n}
{n}The room is at the top of a narrow house, rented, by the smell of it, from someone who left in a hurry. The shutters are closed. Lamps burn in glass. Every wall from floor to ceiling is shelving, every shelf is glass-fronted, and on the far side of the room, in a chair she has turned to face the door, Jerribeth sits in her own narrow, insectile form with her hands linked in her lap, close enough to touch.{/n}
"You came. And you brought your friends. Good; I wanted witnesses."
{n}Her voice is still inside your head, though her antennae are a pace from your face. It is a difficult thing to get used to.{/n}
"I came by the road demons use. Do not ask. You would only want to close it, and then I should only have to open another. Come in. I have put everything where you can see it."''',
     (0, '[Look at the shelves.]'),
     (1, '[Look at the shelves.]'),
     (2, '[Come back another night.]'))

text("room_measure", "public_result", '''{n}The first case by the door holds a little heap of grey ash in a glass dish, labelled in her hand with a date and the name of the square below the citadel.{/n}
"Vardess. What your inquisitors left of him. I bought him from the man who swept the square. He thought I was mad. He was well paid for thinking it."''',
     (0, '[Look at the next case.]'),
     (1, '[Look at the next case.]'),
     (2, '[Look at the next case.]'),
     (3, '[Walk along the shelves.]'))

text("room_measure", "private_result", '''{n}The first case by the door holds Vardess.{/n}
{n}He is small on his velvet, pinned through below the breastbone, horns polished. The drawer has become a case, and the case has been given the best place in the room, at eye height, where the lamp falls.{/n}''',
     (0, '[Look at the next case.]'),
     (1, '[Look at the next case.]'),
     (2, '[Look at the next case.]'),
     (3, '[Walk along the shelves.]'),
     paras=(
         p('''{n}His eyes follow you across the threshold.{/n}''', forbids=("jerribeth.vardess_blinded",)),
         p('''{n}He has no eyes now. He turns his face toward the sound of your step.{/n}''', requires=("jerribeth.vardess_blinded",)),
         p('''"I moved him up from the drawer. He deserved a window."'''),
     ))

OLD_SHELF = '''{n}The next case: a row of locusts on needles, each one still, each one perfect. Then a jar of grey Wintersun earth. Then a child's shoe. Then, alone on a shelf, a little gilded theatre with nothing on its stage.{/n}
"My cabinet. Smaller than the one in the Sanctum. I travel light."'''
for _node, _choices in (("public_visible", ((1, '[Keep looking.]'),)),
                        ("public_refused", ((1, '[Keep looking.]'),)),
                        ("private_play", ((1, '[Keep looking.]'),)),
                        ("private_declined", ((1, '[Keep looking.]'),))):
    text("room_measure", _node, OLD_SHELF, *_choices)
text("room_measure", "public_removed", OLD_SHELF, (0, '[Keep looking.]'))
text("room_measure", "private_comedy", OLD_SHELF, (0, '[Keep looking.]'))
for _node in ("public_visible.reply.1", "public_refused.reply.1", "private_play.reply.1", "private_declined.reply.1"):
    text("room_measure", _node, '''"You are looking for something you recognise. Keep looking. I have put you in here somewhere."''',
         (0, '[Turn back to her.]'))

text("room_measure", "floor", '''{n}She sits down again in her chair and links her hands and waits, with all of it around you: the pins, the glass, the eyes.{/n}
"You are the Commander of this city, and I have brought a cabinet into it. I know what your crusade does with cabinets like mine. So. Decide. I want to watch you do it."''',
     (0, '"Keep it hidden. Nobody climbs those stairs but me."'),
     (1, '"Not inside my walls. Take it out of Drezen."'))

text("room_measure", "loop", '''{n}She laughs, high and abrasive, and it is strange to hear it with your ears as well as inside your head.{/n}
"Hidden. In the middle of your city, a quarter of an hour from your bed, and only you with a key. Oh, Commander. You have made yourself my accomplice and called it discretion."
{n}She draws the shutters closer. The lamps go down. The eyes in the cases go on shining.{/n}''',
     (1, '"And if someone finds it?"'))

text("room_measure", "loop.reply.1", '''"Then they will find it. And they will find out whose key opened the door."''',
     (0, '"Then they had better not."'))

text("room_measure", "loop.reply.2", '''{n}She considers you with her head on one side, as though you were behind glass.{/n}
"They will not. I shall see to it. I am very good at making people see an empty room."''',
     (0, '"Then come here."'))

text("room_measure", "terrace", '''"Out of your walls? How fastidious."
{n}She does not argue. That is worse. She simply looks round at her shelves, and you understand that by morning there will be nothing in this room but dust and a smell of camphor.{/n}
"I shall take it a day's ride out, somewhere with a cellar and no neighbours. And you will pay me for the trouble, Commander. A toy for the move. I shall choose it."''',
     (1, '"What toy?"'),
     paras=(p('''"And since you still owe me a specimen for the hole in my velvet, I shall take that at the same time. One toy for both debts. I am being generous, because I already know which one I want."''',
              requires=("jerribeth.specimen_owed",)),))

text("room_measure", "terrace.reply.1", '''"You will know it when it goes missing."''',
     (0, '"That is not an answer."'))

text("room_measure", "terrace.reply.2", '''"It is the only kind I give before I collect."''',
     (0, '"Then come here."'))

text("room_measure", "private", '''{n}She turns her head toward your companions, and the high voice is in all your heads at once.{/n}
"Out. All of you. Wait in the street. Your Commander is quite safe; I have never once damaged a thing I meant to keep."
{n}They look at you. You let them go. The door shuts, the stairs creak, and then there is only the lamp and the glass and her.{/n}
"There. I have wanted to be in a room with you since the yard. Not a frame. A room."
{n}She rises. She is taller than you remembered, and closer. Her delicate clawed fingers find your wrist and close on it, not hard.{/n}
"Hold still. No. Stiller than that."''',
     (2, '"Like this?"'))

text("room_measure", "private.reply.1", '''"Like that. Oh, like that."
{n}She looks at you the way she looks at the things in her cases, and you understand that she is not pretending otherwise.{/n}
"Everything in this room holds still for me. You never have. Tonight I want you to. Choose, Commander, and choose quickly, because I am about to stop asking."''',
     (0, '"Then stop asking."'),
     (1, '"Not tonight. Sit with me instead."'))

text("room_measure", "desire", '''{n}She does not ask again. She puts you in her chair, the one that faces the door and the shelves, and stands over you and arranges you: your wrists on its arms, your chin lifted with one claw, your head turned a little toward the lamp, as if she were setting a specimen.{/n}
{n}Then she bends to you. Her claws open your collar and the front of your clothes one fastening at a time, watching to see what each one costs, until the air of the room is on your skin and her mouth is a hand's breadth from it. The buzzing starts low in her chest. She bends over the chair, wings half open to shut out the shelves, and her cool weight leans into you with a slow, deliberate pressure, her breath not quite as even as she would like it to be.{/n}
"Do not move. If you move, I stop. I want to see how long you can bear it."''',
     paras=(p('''{n}On the sill, Marhevok's eyes are open.{/n}''', **PLANT),))

text("room_measure", "quiet", '''"Sit with you? Instead?"
{n}She considers being offended. You watch her decide against it.{/n}''',
     (1, '"I like watching you decide."'))

text("room_measure", "quiet.reply.1", '''"An objectionable habit. I have cultivated it carefully."
{n}She sits on the arm of the chair beside you, which no mortal would find comfortable, and leans until her weight is against your shoulder. She is very light. Her hand stays on your wrist. You understand that it is not going to move.{/n}
{n}She tells you about each of the things in the cases, one by one: how she found it, what it cost, what it said when the pin went in. She watches your face for every one. When she decides you have grown tired, she tells you so, and is right, and is insufferable about it.{/n}''')

text("room_measure", "end", '''{n}Toward the end of the night she unlocks the door herself.{/n}
"Go back to your crusade. Your friends have been standing in the street for hours. They will be cold and suspicious, and I shall enjoy that from up here."
{n}At the door she takes your wrist one more time, briefly, as though checking that it is still where she left it.{/n}
"Come back. I have not finished with you. I have barely begun the label."''',
     (0, '[Go down to your companions.]'))

CHOICES[("room_measure", "jerribeth.room_measure.explicit.1", 0)] = '[Afterward.]'

# ---- future (hub; text only) ------------------------------------------------------------
text("future", "start", '''{n}Jerribeth answers without preparing a setting. The frame holds only her own form and the darkness around it.{/n}
"An arrangement like this ends so easily. A missed invitation. A changed allegiance. A crusader who decides, one morning, that a demon's voice in the evenings would look very bad before an inquisitor."
{n}Her antennae move once, then settle.{/n}
"Rules, laws, loyalty? Seek them in Hell and Heaven, anywhere but the Abyss. I served Lord Baphomet for as long as it benefited me more than it cost me. You know that. So understand what I am asking. Not what you will pay. What you will give me, and how much of it, and for how long. I want you kept, Commander. Tell me how."''')

text("future", "end", '''{n}She lets the answer stand without testing it, which for her is a considerable concession, and then tests it anyway.{/n}
"I shall hold you to every word. You should know that I have kept you; the words were only the pins. Tomorrow, then. If the world is still ending, it can spare us another evening."
{n}Before the image fades, the seam of the invented horizon appears behind her. She has kept that too.{/n}''')

text("future", "partner_unknown", '''"I have no news of him, and I have not gone looking for any. If I wanted to, I could give you news. I could make it whatever you liked best, and you would believe it, and thank me."
{n}Her laugh is dry and high.{/n}
"He may still want me. You have heard his name now. You will not be able to call that a surprise."''')

text("future", "partner_discovery_resume", '''{n}She leaves the frame open. Her hands stay on her side of it.{/n}
"You have heard what I kept, or what I lost. You are still here. How troublesome of you."
{n}She leaves her hands at her sides.{/n}
"Come here. No: there. I decide the distance tonight."''')

# ---- farewell: the parting gift ----------------------------------------------------------
DISCOVERY = '"You are very pleased with yourself tonight. Why?"'
text("farewell", "start", '''{n}The charm answers almost before you touch it. Jerribeth appears without a setting: only her own narrow shape, and the dark.{/n}
"I know. There are important things you must go and do, and this may be our last convenient evening for some time."
{n}Her hands are linked tightly together.{/n}
"Do not die out there. Not because I should miss you, though I might. Because I have not finished collecting you, and I will not have some cretin with an axe walk off with my best piece half pinned. And I have brought you a parting gift. You may have it before you go, or not at all."''',
     (0, '"Keep an evening for me. I will come back for it."'),
     (1, '"Tell me what you would like when I do."'),
     paras=(p('''"I listened to your confession again last night. The one from the yard, about being the monster in front of your own soldiers. You tell it beautifully. Go and be a monster somewhere useful."''',
              requires=("jerribeth.yard_confessed",)),))

text("farewell", "want", '''"An account of what happened. The interesting version first, then the one you have edited to make yourself sound less frightened."
{n}Her voice drops to a low vibration.{/n}
"And an evening when you hold still for me. I have been patient about it. I am very rarely patient."''',
     (0, '"Then keep it for me."'))

text("farewell", "return", '''"I will."
{n}She does not attach a clever qualification. It is so unlike her that it sounds almost like a threat.{/n}
"When you come back, invite me. I shall know what you mean. And if you take too long, I shall come and find you, and I shall not knock."
{n}She shuts the frame herself before you can, with a small, decisive click, like a case closing.{/n}''')

# ---- short path and logistics ------------------------------------------------------------
text("parting", "end", '''{n}Her hands remain still.{/n}
"Then go. Turn me to the wall. I shall still be on the other side of it."
{n}There is anger in her voice, and she does not trouble to hide it.{/n}
"You will not hear me again. That is not the same as my not watching. Remember it the next time you undress in front of a frame."''')

text("promise_revisited", "chosen", '''"I want you to see the room when it exists. If it takes longer than I expect, you will hear me complain while I find another wall."
{n}Her antennae lift toward the frame.{/n}
"Bring me your complaints too. I am excellent at finding out whom to blame, and very reasonable about what it costs to ruin them."''')

text("promise_revisited", "close", '''{n}For a moment the city remains behind her, much brighter than her face.{/n}
"I had meant to show you more."
{n}She removes the image herself.{/n}
"I heard you. I shall stop waiting for invitations. I never needed them, Commander; I only enjoyed them. Mind what you say in front of mirrors."''')

text("short_invitation", "short", '''"Then ask me for that, properly, and I shall name what it costs. We have had evenings I want repeated. I have not yet had the ones I want most."
{n}Her hands unlink.{/n}
"The work will keep. If you come back to it before you leave, so much the better for you. If you do not, I shall remember, and collect the difference later."''')

text("fate_letter", "work", '''"A room in which the distance between two doors depends on which one you wish to reach. No prisoners. They would make the result too easy to predict. I want someone to discover that the door they were rushing toward has become tiresome, turn around, and find the other farther away than before."
{n}A drawing occupies the lower corner. At first it appears to be two doorways. When you turn the paper, a narrow street becomes visible between them. She has fitted it into the space left by the address.{/n}
"You would tell me to let the visitor leave. I would like you to tell me where to put the exit without spoiling the interesting part. That is your next contribution, if you wish to make one."
{n}The last line has been added beneath a small, impatient blot.{/n}
"It is a design. I have not built it yet, or put anyone in it yet, or become grateful for your supervision at all. You may begin by looking at it."''')

text("fate_letter", "answer", '''{n}You write your answer beneath hers. For a moment your words appear on the outside of the fold, as though the paper has forgotten which side of a conversation it belongs to. Then they settle into place.{/n}
{n}One more sentence appears in her hand.{/n}
"That is enough for one experiment. An invitation need not become a prophecy merely because you have made its delivery impertinent."
{n}The writing stops. The letter remains a letter, for now.{/n}''')

text("fate_letter", "existing", '''{n}The frame lies where you left it, face down, which has never once stopped her.{/n}
{n}For now you have a drawing, a reply, and a small notch in the paper where Jerribeth tried to discover whether your trick would let her change her mind. She did. You have kept what she chose to send afterward.{/n}''')

# ---- endings (node text only; endings1-3 paragraphs are untouched) ---------------------------
for _ending in ("ending_together", "ending_ascended"):
    text(_ending, "settlement", '''{n}The cabinet in Drezen had begun with a salon full of mirrors, and with what the Commander chose to do about the thing on the floor.{/n}''',
         (0, '[Remember the ashes.]'),
         (1, '[Remember the pin.]'))
    text(_ending, "account", '''{n}Vardess burned in the square below the citadel. Jerribeth bought what was left from the man who swept it, and kept the ash in a glass dish on the shelf nearest her door, labelled in her own hand.{/n}
{n}She never forgave the Commander for the inquisitors. She brought it up at intervals, unprompted, with relish, as one might worry at a favourite scar.{/n}''')
    text(_ending, "catalogue", '''{n}Vardess remained on his pin, awake, in the case with the best light. He had been given a window, and later a chair at their table, which he could not leave and could not decline.{/n}
{n}Jerribeth talked to him in the evenings. She liked to tell Vardess what the Commander had said that day. She liked to watch him listen.{/n}''')
    text(_ending, "room", '''{n}The cabinet went on growing. It went where she went: a rented room in the upper town, a cellar a day's ride out, a hall nobody else could find. Wherever it stood, there was a chair in it turned to face the door.{/n}
{n}Their charm remained a way of speaking, and became, on certain nights, a way of arriving. She never pretended that the Commander was anything other than the best thing on her shelves. She never pretended that the Commander held still.{/n}''',
         paras=(
             p('''{n}On one shelf, alone, on velvet, lay a small thing that had belonged to the Commander, placed where she could see it from the bed. She dusted it herself.{/n}''',
               requires=("jerribeth.cabinet_token",)),
             p('''{n}Nobody in Drezen ever climbed the stairs to the room in the upper town but the Commander. Jerribeth saw to that. People who came close found an empty room and went away.{/n}''',
               requires=("jerribeth.cabinet_hidden",)),
         ))

text("ending_together", "start", '''{n}Jerribeth remained a difficult person to describe to anyone who expected the Commander to keep reassuring company. She did nothing to make the explanation easier.{/n}
{n}The evenings continued. Sometimes she arrived with an elaborate illusion, sometimes with an ugly truth she had kept back for the pleasure of watching it land. She kept the visible seam in one impossible horizon, and only one person was ever allowed to find it.{/n}''')

text("ending_ascended", "start", '''{n}Jerribeth found several advantages to knowing a god personally, and admitted to most of them. The one she discussed least was that a god could still be made to sit for her.{/n}
{n}She tried to pin the Commander, in her fashion, for years. She never managed it. It remained the only piece in her collection that would not hold still, and she went back to it, evening after evening, with the patience of something that has decided to live forever out of spite.{/n}''')

text("ending_apart", "start", '''{n}The charm went dark. Jerribeth had other patrons to cultivate, and other toys.{/n}
{n}She kept one thing from the Commander, all the same. When a new acquisition grew tiresome, she would sit it down and play it a voice: a crusader's, describing what it had felt like to be the monster in their own yard. She found it improved almost anyone's posture.{/n}''')

text("ending_unfinished", "start", '''{n}For a time, Jerribeth kept the far side of the correspondence charm. The invitations grew less frequent. She stopped waiting for them sooner than anyone would have expected, and did not say so.{/n}
{n}Eventually the frame held something else: a new specimen, pinned where the Commander's face used to appear, so that she would have something to look at in the evenings. She never decided whether it was a better likeness.{/n}''')

text("ending_aeon", "start", '''{n}The history that might have joined Jerribeth and the Commander had no place in the world's new account of itself. Somewhere in the Abyss, an illusion acquired a narrow seam along its horizon.{/n}
{n}It was not a memory. She had no memory to keep. It was her signature, left where only one person in any version of the world would have known to look for it.{/n}''')

# --------------------------------------------------------------------------
# New nodes from jerribeth_scaffolding (applied at the end of its integrate).
# --------------------------------------------------------------------------
NEW_NODES = {}
NEW_CHOICES = {}
NEW_PARAS = {}


def new(scene, node, body, *choices, paras=()):
    NEW_NODES[(scene, node)] = body
    for index, choice in choices:
        NEW_CHOICES[(scene, node, index)] = choice
    if paras:
        NEW_PARAS[(scene, node)] = list(paras)


# Companion pages copy their host's choices; their text follows the host.
COMPANION_RESUME = {
    "commission": "beauty",
    "offered_signature": "ownership.reply.1",
    "counterfeit_audience": "challenge",
    "room_measure": "floor",
}

# ---- commission ------------------------------------------------------------------------
NEW_CHOICES.update({
    ("commission", "beauty", 2): '[Persuasion DC 22] [Play the demon they see.] "Run, little man."',
    ("commission", "beauty", 3): '[Seelah steps up beside you.]',
    ("commission", "beauty", 4): '[Regill is watching the picket.]',
    ("commission", "beauty", 5): '[Wenduag has started to laugh.]',
})

new("commission", "yard_talk_ok", '''{n}You do not raise your hands. You walk at the spear and talk, in the flat, tired voice you use at the end of a council, the voice every soldier in Drezen has heard read out a duty roster. Wherever the face fails, the words do not.{/n}
{n}The sergeant's spear dips. The picket blinks hard, as if something has gone into his eye. You point at the postern, and neither of them needs telling twice. They reach the cultist with the bar half raised and put him on the stones.{/n}
{n}The face you were wearing peels off you like wet paper. Inside your head, Jerribeth is laughing.{/n}
"Oh, well done. You broke it without paying me a copper and without spilling a drop. Do you know how rarely anyone manages that? Wintersun never did. I shall have to make the next one harder, and you will have only yourself to blame."''')

new("commission", "yard_talk_fail", '''{n}It does not work. Whatever comes out of your mouth, the sergeant hears it through a demon's teeth. He lunges.{/n}
{n}The spearhead opens your forearm from wrist to elbow. You get your other hand on the haft before he can draw back for a second thrust, and the two of you stand there chest to chest while your blood runs over his knuckles.{/n}
{n}He looks down at it. Red. Plain mortal red.{/n}
{n}Jerribeth sighs inside your head, like someone whose curtain has been pulled too soon.{/n}
"The blood. They always believe the blood. Very well; you have spoiled it, and in the least elegant way available."
{n}The illusion goes out of the yard all at once. The sergeant drops his spear and is sick against the gate. Across the stones the turnkey gapes at the man he was about to let go, and the cultist bolts for the postern and does not reach it. The picket brings him down.{/n}
"Have that arm bound. I prefer my things undamaged."''')

new("commission", "yard_seam", '''{n}You know where to look. She always leaves one.{/n}
{n}There, along the gatehouse roof: a hair of wrong light where the stones of the illusion do not quite meet the stones of the wall. You take the sergeant by the wrist, spear and all, and turn his eyes up to it.{/n}
"The roofline, Sergeant. Look at it. Does stone shimmer?"
{n}He looks. Once a man has seen the seam he cannot stop seeing it. The demon in your coat flickers, frays, and is you. The sergeant swears and bellows for the postern, and they have the cultist down before the bell stops.{/n}
{n}Jerribeth's voice comes slowly, savouring.{/n}
"You remembered my seam. You kept it for a moment like this. I left it there for you, Commander, and you have used it to rob me in front of your whole garrison. That is the most romantic thing anyone has ever done to me."''')

new("commission", "yard_demon", '''{n}You stop trying to be yourself. You let your shoulders roll forward under the borrowed horns, and you smile at the picket with all the teeth he thinks you have.{/n}
"Run, little man."
{n}He runs. The sergeant holds for a heartbeat longer and then follows him, and the inner gate stands empty. You cross the yard alone. The cultist at the postern has the bar on his shoulder when your hand closes on the back of his neck and puts his face into the door.{/n}
{n}Every window on the yard is full. The garrison has watched the Commander's demon catch a Baphomet cultist with its bare hands, and by morning the kitchens will have it that you did it with your teeth.{/n}
"Oh. Oh, that was the best performance anyone has given me in a century. Did you feel them watching? They will tell it for a week. They will wonder about you for much longer."
{n}The face comes off you at last. It does not, you suspect, come out of anyone's memory.{/n}''')

new("commission", "cell_given", '''"Done."
{n}In the frame the turnkey stops with the key in the lock. He blinks at the man in front of him, and the man is a cultist again, and the turnkey is shouting. Up in the yard the demon in your coat melts off the air, and the sergeant is left levelling his spear at an empty patch of evening.{/n}
{n}By the morning bell the cell is empty. The bolts are still shot. The turnkey swears he never left his stool, and there is no blood. Nobody can tell you where the man went. After a day or two, nobody much wants to.{/n}
"He is quite comfortable. Not happy. Comfortable. I have put him where he can watch me work. He keeps trying to pray to Baphomet, and finding the words come out in my order."
{n}For one breath the frame shows you a man pinned upright in a glass case by something too fine to see. His eyes move. They find you.{/n}
"Thank you, Commander. I do so like a gift that still blinks."''')

new("commission", "cell_refused", '''"No? You would rather keep a Baphomet cultist in your cells than let me have him? How possessive. Then pay."
{n}The frame waits. In it, the cultist has reached the stair.{/n}
{n}So you tell her. What it was like, the one glimpse you had of the yard through the picket's eyes: your own coat on a horned thing, and the sergeant who has saluted you every morning for a month ready to put a spear through your belly and be proud of it. How the hatred in his face was the honest kind. How part of you agreed with him.{/n}
{n}She does not interrupt once.{/n}
"There. That was not so difficult."
{n}The cultist stops on the stair as though he has walked into a wall. The turnkey stares at him, then roars, and the cells fill with boots. In the yard the demon is gone. The sergeant lowers his spear and cannot remember why his hands are shaking.{/n}
"I shall keep that. All of it, word for word, with the pauses. One day, when you are feeling heroic, I shall play it back to you."''')

new("commission", "companion_seelah", '''{n}Seelah does not draw. She steps in front of you, shield low, and plants herself between your borrowed horns and the spear.{/n}
"Sergeant. I know that walk under any face in the world. That's the Commander. Spear down."
{n}The sergeant wavers. Not enough.{/n}
"Oh, she is lovely," {n}Jerribeth says.{/n} "A paladin who trusts a walk over her own eyes. I should like to see what she would do if I gave her something truly convincing."''')

new("commission", "companion_regill", '''{n}Regill watches the picket with the flat attention he gives a column of figures that does not add up.{/n}
"The picket has broken under a visual deception. That is three lashes when this is over, whatever he believed he saw. And the object on your table, Commander, goes into the furnace tonight. I will say so once."
"Three lashes," {n}Jerribeth says, enchanted.{/n} "He has a gift. I would keep him if he were not so dull."''')

new("commission", "companion_wenduag", '''{n}Wenduag laughs, one short bark that turns the sergeant's head.{/n}
"Look at them. They'd gut you for your face and hold the door for a cultist. That's a good trick, Commander. That's a really good trick."
"I like her," {n}Jerribeth says.{/n} "She sees the joke without needing it explained. Most people need it explained, and then they cry."''')

# ---- refuge ----------------------------------------------------------------------------
new("refuge", "footstool_kept", '''{n}You set your cup down on the edge of the frame, where his back would be.{/n}
{n}Jerribeth's laugh scrapes the inside of your skull. She lifts a cup from somewhere out of sight and sets it on the kneeling man's back beside the others, very precisely, so that the wine trembles and does not spill.{/n}
"From the Commander of the crusade. Thank the Commander, furniture."
{n}The man's mouth works. What comes out is a whisper, and it is thanks. His eyes, above it, are screaming.{/n}
"There. You have made a friend. He will remember your cup longer than he remembers his name."''')

new("refuge", "footstool_freed", '''"Let him up?"
{n}For a moment nothing in the room moves. Then she lifts her foot from his shoulder, and the man unfolds all at once, as though a string had been cut, and crawls the first yard before he remembers that he can stand. He does not look back. He does not thank anyone.{/n}
{n}Then the voice comes, airy and otherworldly, from nowhere at all.{/n}
"Why are you mortals so fond of breaking other people's toys?"
{n}It is said lightly. It is not light.{/n}
"You owe me one, Commander. Not tonight. I shall choose it, and I shall collect it, and you will not enjoy the choosing."''')

# ---- offered_signature -----------------------------------------------------------------
NEW_CHOICES.update({
    ("offered_signature", "offer", 2): '[Regill has come as your escort.]',
    ("offered_signature", "offer", 3): '[Seelah has stopped at the door.]',
    ("offered_signature", "ownership.reply.1", 2): '"Not in my name. I am breaking this, here, in front of her guests."',
    ("offered_signature", "performance.reply.1", 1): '"Half. I sat through the soup."',
    ("offered_signature", "break", 0): '[Knowledge (Arcana) DC 32] [Find the seam in the false Commander and tear it open where they can all see.]',
    ("offered_signature", "break_ok", 0): '[Leave her to her guests.]',
    ("offered_signature", "break_fail", 0): '[Get out of that house.]',
})

new("offered_signature", "break", '''"Break it?"
{n}You are already moving: back down the passage, past the widow's porter, into the candlelight of the dining room, where the last of the guests are still at their wine.{/n}
"Oh, you are going to make a scene. In front of her friends. I approve of the impulse. I doubt your aim."''')

new("offered_signature", "break_ok", '''{n}You know illusion-work, and you know hers. There: where the false Commander's collar meets its throat, the light falls half a breath late. You take hold of it with both hands and pull.{/n}
{n}The face comes away like a mask, and there is nothing under it. Nothing but a narrow, insectile shadow that sways for one instant at the head of the widow's table, antennae trembling, and is gone.{/n}
{n}Somebody screams. The widow's eldest daughter is on her feet. The widow herself sits very still, looking at the empty chair where the Commander of the crusade was not, and at the real one standing over it, and by the faces round her table you can see the story already forming: the old woman who paid a demon to sup with her.{/n}
"Well," {n}Jerribeth says.{/n} "You have shamed her in front of everyone she has ever fed. That is crueller than anything I had planned, and you did it to rescue her."
"I withdraw. The evening she paid for was yours, however, and you did not spend it. I shall collect it from you instead."''')

new("offered_signature", "break_fail", '''{n}You go for the false Commander's throat, looking for the seam. There is no seam. There is a face, your face, startled and hurt, and a room full of people watching the Commander of the crusade being seized by some shabby cousin with a wild look.{/n}
"Take your hands off me," {n}says your own voice, very reasonably.{/n}
{n}Then the face is gone, and so, at the worst possible moment, is the one she lent you. You are standing alone at the head of the widow's table with your hands round nothing, shouting about demons, as yourself. Nobody else saw anything at all.{/n}
{n}It will be all round the upper town by noon: the Commander, at a widow's supper, raving.{/n}
"I took your face back. I thought they ought to know who was shouting. Do not be angry; you were about to tell them yourself."
"I withdraw. The evening the widow paid for was yours, and you have wasted it. I shall collect it from you instead."''')

new("offered_signature", "widow_fee", '''"Half."
{n}In the morning a purse lies on your table beside the frame. The coins are the widow's own, old Kenabres mintings, some of them worn smooth by a dead man's thumb. Under them, folded small in a napkin, are two silver spoons engraved with a family crest.{/n}
"Your share. I kept the rest of the set. One should never break up a collection entirely."''')

new("offered_signature", "companion_regill", '''{n}Regill has come as your escort and has stood by the wall all evening without touching the wine. When the widow walks the false Commander to the door, Regill steps into the passage beside you.{/n}
"Impersonating the Commander of the crusade is treason, whatever the species of the impersonator. That woman paid for it. I will want this house searched and her correspondence read before the week is out."
{n}Inside your head, Jerribeth laughs.{/n}
"Search away; he will find sixty crowns' worth of nothing. Now hush, both of you. I have one idea left to plant. For the rest of her life, every man who comes through that door will be you, and she will know each time that it is not. Well, Commander? You were her guest too."''')

new("offered_signature", "companion_seelah", '''{n}Seelah would not sit at that table. She has stood in the widow's passage all through supper with her arms folded, and when the false Commander passes on its way to the door she looks at it the way she looks at a wound gone bad.{/n}
"That isn't you, and that woman's been robbed, and I'm not going to pretend I didn't see it. Commander, whatever that thing's about to do to her, stop it."
"The paladin wants me stopped," {n}Jerribeth says.{/n} "How lovely. I am only going to give the widow one idea, sweet thing: that every man who comes through her door for the rest of her life will be the Commander, and that it never is. Let us see whether the Commander agrees with you."''')

# ---- counterfeit_guest -----------------------------------------------------------------
NEW_CHOICES.update({
    ("counterfeit_guest", "scout_known", 0): '[Go back and decide how to go in.]',
    ("counterfeit_guest", "scout_unknown", 0): '[Go back and decide how to go in.]',
    ("counterfeit_guest", "attend", 0): '"As your guest. I want to watch."',
    ("counterfeit_guest", "attend", 1): '"I am telling the Inquisition first. A cambion in Drezen is their business."',
})

new("counterfeit_guest", "scout_known", '''{n}It takes you an hour between his doorstep and the merchants' street. The hatter who makes his caps lines them with buckram, twice as stiff as fashion needs. His cook buys meat for one and has never seen him eat bread. He came to Drezen after the city was retaken, with money and no family, and nobody you ask remembers him in Kenabres, where he says he was born.{/n}
{n}Then he steps out onto his own step to scold a servant: a lean, handsome man in a high collar and a tall velvet cap. He walks with his weight a little forward, like a man used to carrying something heavier on his head than a hat. When he turns, the cap does not move with him quite as cloth should.{/n}
"Yes," {n}Jerribeth breathes, delighted.{/n} "Oh, yes. And now you know it as well as I do, which means you could do something about it before I do. How exciting. What will you do with him?"''')

new("counterfeit_guest", "scout_unknown", '''{n}You spend an hour at it and learn nothing worth the hour. Vardess is a rich man with a good hatter and a high collar. His servants like him. The merchants' street calls him generous. If there is anything under his cap, he keeps it there.{/n}
"Nothing? You looked at him for an hour and saw a man. That is what he wants everyone to see; do not feel too stupid. I shall show you the rest tonight."''')

new("counterfeit_guest", "attend", '''"Now. How will you come in?"
{n}Her voice is patient in the way of something that knows exactly what it wants and is willing to let you pretend you are choosing.{/n}
"As my guest, you sit by my empty chair and watch. Or you can go to the Inquisition first, and turn his pretty salon into a raid. I warn you, I dislike an audience I did not choose."''')

# ---- counterfeit_audience ------------------------------------------------------------
NEW_CHOICES.update({
    ("counterfeit_audience", "challenge", 3): '[Athletics DC 30] [Go for him before he reaches the doors.]',
    ("counterfeit_audience", "leverage.reply.1", 2): '[Persuasion DC 32] [Meet the inquisitors on the stair and send them away.]',
})

new("counterfeit_audience", "chase_ok", '''{n}You go over the table. Glass and candles everywhere. He is fast, faster than a man, but he is dragging Petrik, and he cannot drag him and stare at the mirrors and run all at once. You hit him at the doors. The knife skitters away across the floor. Petrik rolls clear, and Vardess is under your knee on his own beautiful parquet, his horns grinding the wood, in front of everyone.{/n}
"Oh, beautifully done," {n}Jerribeth breathes.{/n} "Look at them all looking at you."''')

new("counterfeit_audience", "chase_fail", '''{n}You go over the table and you are one stride too slow. He reaches the doors. Petrik's boots skid, and Vardess's knife goes across the boy's face, cheekbone to jaw, a long ugly opening, before you get there and tear him off and put him on the floor.{/n}
{n}Petrik is screaming. He will live. He will wear that face for the rest of his life, and every time he looks in a mirror he will remember this room.{/n}
"A pity about the boy. He was pretty," {n}Jerribeth says.{/n} "Still. You have the cambion, and the cambion has learned what it is to be seen."''')

new("counterfeit_audience", "raid_dismissed", '''{n}You meet them on the stair: four of them, and a sergeant with a warrant in his fist. You tell him there has been a misunderstanding. You tell the sergeant the Commander's own friends were played a masque tonight, rather a good one, by an acquaintance of the Commander's, that a lieutenant had a fright, and that you will answer personally for anything more the sergeant cares to ask about in the morning.{/n}
{n}The sergeant looks past you up the stair, at the light and the laughter beginning again. He looks at you. He goes.{/n}
"You lied to your own Inquisition for me," {n}Jerribeth says.{/n} "To their faces. I have never been so flattered."''')

new("counterfeit_audience", "raid_kept", '''{n}They do not go. The sergeant hears you out, very politely, then shoulders past you up the stair with his warrant held high, and the salon fills with grey coats. Whatever you meant to say about a masque, nobody would believe it now. They can all see the horns.{/n}
"Your inquisitors," {n}Jerribeth says, and her voice in your head has gone cold and thin.{/n} "Whom you invited. Into my evening."''')

new("counterfeit_audience", "companion_regill", UNMASK + '''
{n}Regill does not look at Vardess at all. He is looking at the mirrors, at the guests in them, putting names to faces.{/n}
"A cambion has kept a salon in Drezen for a year and entertained officers of this crusade. That is a failure of the city watch, of the Inquisition and of every officer present. I will be writing to all three."
"Is he always like this?" {n}Jerribeth asks, delighted.{/n} "I adore him."
''' + GRAB)

new("counterfeit_audience", "companion_lann", UNMASK + '''
{n}Lann laughs out loud, the only person in the room who does.{/n}
"Look at his face. Look at it! Never thought I'd see somebody have a worse time with a mirror than me."
"The mongrel understands," {n}Jerribeth says.{/n} "How unexpected. I may have to like him."
''' + GRAB)

new("counterfeit_audience", "companion_wenduag", UNMASK + '''
{n}Wenduag's lips peel back from her teeth.{/n}
"Ha. All those years pretending to be something softer, and one trick and he's naked. That's what happens when you hide what you are, Commander. Somebody stronger takes the hat off."
"A philosopher," {n}Jerribeth says.{/n} "Keep her."
''' + GRAB)

# ---- counterfeit_spoil ----------------------------------------------------------------
NEW_CHOICES.update({
    ("counterfeit_spoil", "drawer_empty", 0): '"Fair. You will have one."',
    ("counterfeit_spoil", "drawer_empty", 1): '"I owe you nothing. He burned because he deserved to."',
    ("counterfeit_spoil", "price.reply.1", 3): '"Let him speak. Once."',
    ("counterfeit_spoil", "price.reply.1", 4): '"Take his eyes."',
})

new("counterfeit_spoil", "drawer_pinned", '''{n}Vardess is in the drawer.{/n}
{n}He has been made small. Not crushed: reduced, neatly, the way a moth is reduced to its wings, until a man fits on black velvet between a dried locust and a sprig of something with thorns. A pin as fine as a hair goes through him just below the breastbone. His cap is gone. His filed horns have been polished. His eyes move.{/n}
{n}They find the frame. They find you.{/n}
"I cannot allow such a unique creature to disappear entirely," {n}Jerribeth says.{/n} "So I have preserved him. In some form."
{n}She turns the lamp so that the light falls across his face.{/n}
"He is awake. He will be awake for a very long time. He spent his whole life wanting to be seen as something he was not, and now he is seen exactly as he is, by me, every evening. I think it is the kindest thing anyone has ever done for him."''')

new("counterfeit_spoil", "drawer_empty", '''{n}The drawer is empty: a long rectangle of black velvet, a row of pins with nothing on them, and in the middle, a hollow pressed into the nap where something was meant to lie.{/n}
"Look at it," {n}Jerribeth says.{/n} "Go on. Look at it properly."
{n}She waits until you have.{/n}
"That is where he would have gone. I made the hollow the night I found him. Then you gave him to men with torches, and they turned him into smoke and a smell in the square, and I have a hole in my velvet."
"You owe me a specimen, Commander. One. As good as he was, or better. I shall collect it when I choose."''')

new("counterfeit_spoil", "vardess_speaks", '''{n}Jerribeth draws the drawer out to its full length and bends over it, and does something with one claw that is too fine to see.{/n}
{n}A voice comes out of the velvet. It is very small and perfectly clear.{/n}
"Commander. Commander, I can see the lamp. She leaves the lamp. I can see the lamp all night. Tell her I'll be anything. Tell her I'll..."
{n}She slides the drawer shut on him. Gently.{/n}
"Once, I said. He spent it on begging. They always do. I had hoped he would say something about the hat."''')

new("counterfeit_spoil", "vardess_blinded", '''"His eyes? Oh, you are far more generous than I am."
{n}She bends over the drawer. You do not see what she does. You hear it: a sound like a seed husk splitting, twice.{/n}
"There. Now he cannot see you, or me, or the lamp. He can still hear. He will spend a long time wondering what we are doing. I think you have improved him. Thank you."''')

# ---- room_measure ----------------------------------------------------------------------
NEW_CHOICES.update({
    ("room_measure", "floor", 2): '[Persuasion DC 30] "Let one of them go. I choose which."',
    ("room_measure", "floor", 3): '"Put something of mine on your shelf."',
    ("room_measure", "floor", 4): '[Seelah has her hand on her sword.]',
    ("room_measure", "floor", 5): '[Regill has taken out a notebook.]',
    ("room_measure", "floor", 6): '[Wenduag is bent over the pins.]',
    ("room_measure", "floor", 7): '[Ulbrig has not come past the doorway.]',
    ("room_measure", "floor", 8): '[Greybor is looking at the locks.]',
    ("room_measure", "floor", 9): '[Arueshalae has gone very still.]',
})

new("room_measure", "shelves", '''{n}She walks you along the shelves as though this were a gallery and you a patron she means to rob.{/n}
{n}Most of it she does not explain: a moth the size of a hand, a key set in a block of amber, a child's shoe, a jar of grey Wintersun earth.{/n}''',
    paras=(
        p('''{n}A tall case holds the cultist from your cells, upright and pinned, his rags arranged like vestments. His lips are moving. Whatever he is praying, it comes out in her order.{/n}
"Your gift. He has been very good company. He tells me all about Baphomet, and I correct him."''',
          requires=("jerribeth.yard_prisoner_given",)),
        p('''{n}A small glass bottle, stoppered, that looks empty.{/n}
"Your confession from the yard. I keep it in there. Some evenings I take out the stopper and listen."''',
          requires=("jerribeth.yard_confessed",)),
        p('''{n}On a low shelf, a plain pewter wine cup with a ring of old red in the bottom.{/n}
"The cup you set on my footstool's back. He held it there for two days after you left. Then I let him put it down, and he wept."''',
          requires=("jerribeth.refuge_footstool_kept",)),
        p('''{n}A small portrait in an oval frame: a little woman in mourning silk, at a door. As you pass, her painted eyes turn to follow you, and her painted face lights up, and falls.{/n}
"The widow. I go and look at her sometimes. She is holding the pose beautifully."''',
          requires=("jerribeth.widow_pinned",)),
        p('''{n}On a stand, an old-fashioned hat with a soldier's cockade.{/n}
"The husband's. She left it on the step for him. I took it in before the rain."''',
          requires=("jerribeth.widow_husband",)),
        p('''{n}Under a bell jar, a single locust on a needle, its wings spread, the shell still faintly iridescent.{/n}
"Xanthir. A piece of him. The best piece; I brought it with me. It was a great deal of work."''',
          any_groups=(("jerribeth.collection", "jerribeth.xanthir_in_price"),)),
        p('''{n}On the sill, in a pot of black earth, a plant with leaves like charred skin turns slowly on its stem. Human eyes stare out of the bud. She has set it facing the chair by the bed.{/n}
"Marhevok came too. He would never have forgiven me for leaving him behind. I wanted him to see where you will sit."''',
          **PLANT),
        p('''"Well? Now you have seen what I keep."'''),
    ))

new("room_measure", "cabinet_freed", '''"Which one?"
{n}You choose. She watches you do it, very closely, the way she would watch a locust choose which way to crawl.{/n}
{n}Then she opens the case and does something you cannot follow with one fine claw, and the thing you chose is let go. It does not thank you. It does not look at you. It goes out of the door and down the stairs as fast as whatever is left of it can go, and you hear the street door bang.{/n}
"Why are you mortals so fond of breaking other people's toys?"
{n}It is the same light voice as always. It is colder than you have ever heard it.{/n}
"I let it go because you talked me into it. You did talk me into it; I felt you do it. I shall remember that as well."''')

new("room_measure", "cabinet_refused", '''"No."
{n}She does not raise her voice. She has no need to.{/n}
"You talked very well. You talked better than anyone has talked to me in years. And the answer is no, because they are mine, and you are in my room."
{n}In the case nearest you, something behind the glass that had begun to hope stops hoping.{/n}''')

new("room_measure", "cabinet_token", '''"Something of yours?"
{n}For a moment she is entirely still. Then she holds out one delicate clawed hand, palm up, and waits.{/n}
{n}You give her something. It does not much matter what. It matters that it was yours and that you chose it. She takes it as though it might bite.{/n}''',
    paras=(
        p('''{n}She sets it on the sill beside the pot, square in front of Marhevok's eyes. The bud turns toward it, and the vine draws taut against the rim.{/n}
"There. He will look at it all night. So shall I."''',
          **PLANT),
        p('''"There. A part of you, on my shelf. I have wanted that since the yard."'''),
    ))

new("room_measure", "companion_seelah", '''{n}Seelah has her hand on her sword hilt and has not taken it off since the door.{/n}
"Commander, there are people in those cases. I don't care what she calls them. This gets burned tonight, all of it, and her with it if she gets in the way."
{n}Jerribeth looks at her for a long moment. Then the high voice comes, and Seelah flinches, because this time it is in her head as well.{/n}
"You burn things for your goddess and call it mercy. You wear a holy face over the thief who stole a paladin's helmet, and you wear it so very well. We are all playing at being something, paladin. I simply keep my collection behind glass."''')

new("room_measure", "companion_regill", '''{n}Regill has opened a small notebook and is writing in it, case by case, in a tidy hand.{/n}
"Case one, contents conscious. Case two, contents conscious. I am recording this as evidence, Commander, for whatever proceeding you will eventually be unable to avoid."
"How lovely," {n}Jerribeth says.{/n} "A fellow collector. Do spell my name correctly."''')

new("room_measure", "companion_wenduag", '''{n}Wenduag is bent so close to a case that her breath fogs the glass.{/n}
"Look how fine the pins are. You'd never get them out without killing it. That's clever. That's so clever." {n}She glances back at you, grinning.{/n} "Don't let the paladin burn it, Commander."
"I like her," {n}Jerribeth says.{/n} "Remind me to give her something small and alive before you go."''')

new("room_measure", "companion_ulbrig", '''{n}Ulbrig stands in the doorway, not in the room, and fills it.{/n}
"I'll not come further in, Commander. Something in here's watching me, and I don't care for it."
"Several things are," {n}Jerribeth says.{/n} "They cannot reach you. Not through the glass."''')

new("room_measure", "companion_greybor", '''{n}Greybor is looking at the locks on the cases, one after another, with a professional's sour interest.{/n}
"Cheap locks. Doesn't matter. Nobody's opening those without her say-so. That's what the pins are for."
"A dwarf who understands," {n}Jerribeth says.{/n} "I prefer the assassin to the paladin. He wastes less of my evening."''')

new("room_measure", "companion_arueshalae", '''{n}Arueshalae has stopped just inside the door with her wings drawn tight, and her face has gone very still.{/n}
"Commander... some of these are people. I knew demons who kept rooms like this. I..."
{n}Jerribeth turns her head, and Arueshalae flinches. This time you are allowed to hear it, as a courtesy.{/n}
"You should find all this very familiar. For you too are playing at being human, isn't that so, succubus? You simply do it with more weeping."''')

# ---- farewell ------------------------------------------------------------------------
NEW_CHOICES.update({
    ("farewell", "start", 2): '"You said you had a gift for me."',
    ("farewell", "want", 1): '"You said you had a gift for me."',
    ("farewell", "traitor", 0): '"Hang him. In the yard, where the garrison can see."',
    ("farewell", "traitor", 1): '"He is yours."',
    ("farewell", "traitor", 2): '[Knowledge (World) DC 30] "Leave him at his desk. We will feed him our lies."',
})
for _host, _first in (("start", 3), ("want", 2)):
    for _i in range(5):
        NEW_CHOICES[("farewell", _host, _first + _i)] = DISCOVERY

new("farewell", "traitor", '''"My gift. A name."
{n}She gives it to you: a clerk in your own chancery, a quiet young man who copies dispatches, and who has been copying them twice for a month.{/n}
"He sells the second copy to a buyer in the lower town, who sells it on to someone who sells it to the Abyss. I have known for weeks. I did not tell you because a secret you lack is worth very little to me, and a debt you owe me is worth a great deal. Now you owe me. Enjoy it."
{n}Her antennae tremble with pleasure.{/n}
"What will you do with him? Tell me now. I want to picture it while you are gone."''')

new("farewell", "traitor_hanged", '''"In the yard. Of course. Your yard is where all the best things happen."
{n}By noon he is on the rope in front of the garrison, who cheer. You find you can picture her watching through the frame on your table, antennae forward, delighted by every kick.{/n}
"Short, and very public. Not my style. I did appreciate the crowd."''')

new("farewell", "traitor_given", '''"Mine? Oh, Commander."
{n}At dusk the clerk puts down his pen in the middle of a word, gets up from his desk and walks out of the chancery without his coat. The gate picket sees him go. Nobody sees him again. His half-written word dries on the page.{/n}
"He is quite safe, and in very good company; you have met some of it. Thank you. You give the most thoughtful presents."''')

new("farewell", "traitor_fed", '''"Feed him lies? You want to do my work?"
{n}You do it properly. Over the next days the dispatches on the clerk's desk acquire small, careful errors: a column that will not be where it is said to be, a bridge that is not held, an illness in the Commander's staff that does not exist. He copies them twice, as always. Somewhere in the Abyss somebody pays for them, and believes them.{/n}
"Oh, that is elegant. That is my art in your hands, Commander. You have made a whole army see something that is not there. I have never been so jealous, or so pleased."''')

new("farewell", "traitor_failed", '''{n}You try. But the errors you plant are too clean, or too many, and the clerk is better at his trade than you thought. Within two days his desk is empty. He is gone, and so is the last true dispatch he copied.{/n}
"He smelled it. The good ones sometimes do. You put the lie where a liar would look for it."
{n}She sounds almost fond.{/n}
"Never mind. Next time let me plant it. I leave no seams where anyone but you would find them."''')

new("farewell", "discovery_plant", '''{n}She is smiling. On her face it is a slight thing, a parting of the mouthparts; you have learned to see it.{/n}
"I turned his pot last night. To face the bed. You were there, in a way: I had your voice through the frame, and I said your name the way I say it, and he looked."
{n}She tilts the frame, and there is Marhevok: the bud turned full toward the bed, the human eyes in it wide and raw, a vine dragged taut against the rim as if it had been trying to climb out.{/n}
"He knows. I wanted to see what his eyes would do. They did a great deal."
"You wanted it kept quiet. I enjoyed keeping it quiet. I enjoyed this more. Do not look at me like that, Commander. You knew what I was when you asked."''',
    (0, '"Then let him watch."'),
    (1, '"You did that to hurt me. We are finished."'))

new("farewell", "discovery_chief", '''"I wrote to Wintersun. My last letter to Marhevok. I put your name in it, all of it: your rank, and my bed, and the things you say in it."
{n}She holds up a letter bearing the Wintersun chief's mark. The hand is a strong man's hand gone unsteady.{/n}
"His answer came this morning. Shall I read it to you? 'My lady. My sun. I knew. I made myself not know. Do not write to me again.' He underlined 'sun'. He always does."
"You asked me to be discreet. I told you I would not be, if I found his jealousy more entertaining. I find it very entertaining. I find your face more entertaining still."''',
    (0, '"Then I hope you enjoyed it."'),
    (1, '"You did that to hurt me. We are finished."'))

new("farewell", "discovery_dead", '''"Marhevok is dead. You knew that. You wanted me to keep you quiet anyway, as though a dead man could be told."
{n}She leans close to the frame.{/n}
"I would have told him. If he had lived, I would have told him tonight, and watched. I want you to know that. And I want to watch your face now, while you understand that the only thing that stopped me was a corpse."
"There. That look. That is what I am taking with me tonight."''',
    (0, '"Take it, then."'),
    (1, '"You enjoy that too much. We are finished."'))

new("farewell", "discovery_distant", '''"Marhevok is in his pot in the Sanctum, where I left him when I lost my body. He cannot hear me from here. I tried. Last night, with your name: I said it over and over, as loudly as I can say anything, toward where he is. I do not know whether it reached him. I hope it did. I hope he is turning toward the sound right now, and cannot find it."
"You asked me to keep it quiet. I did not even try."''',
    (0, '"Then I hope he heard."'),
    (1, '"You did that to hurt me. We are finished."'))

new("farewell", "discovery_unknown", '''"I do not know where Marhevok is. Dead, perhaps. Somewhere, perhaps, still loving me."
{n}She leans close to the frame.{/n}
"If I find him, I shall tell him about you. Gladly. In detail. I want you to know that before you go. And I want to watch you be relieved that I have not found him yet. Your relief, Commander. That is what I am collecting tonight."''',
    (0, '"Collect it, then."'),
    (1, '"No. We are finished."'))


# --------------------------------------------------------------------------
def _scenes(payload):
    return {s["Id"].removeprefix("jerribeth."): s
            for s in payload["Scenes"] if s["Id"].startswith("jerribeth.")}


def _node(events, scene, node):
    return overlay_node(events, scene, node, scene_address="jerribeth." + scene)


def _apply(events, nodes, choices, paras, appended=False):
    for (scene, node), body in nodes.items():
        with overlay_item():
            _node(events, scene, node)["Text"] = body.strip()
    for (scene, node, index), body in choices.items():
        with overlay_item():
            answers = _node(events, scene, node)["Choices"]
            # Answers the scaffolding appends do not exist yet in revoice();
            # fill() writes them once they do, and fails if one never appears.
            if index < len(answers):
                answers[index]["Text"] = body
            elif appended:
                record("overlay.index_resolution", scene="jerribeth." + scene, node=node, detail=str(index))
    for (scene, node), extra in paras.items():
        with overlay_item():
            _node(events, scene, node).setdefault("Paragraphs", []).extend(dict(x) for x in extra)


def revoice(payload):
    events = _scenes(payload)
    for scene, title in TITLES.items():
        if scene not in events:
            record("overlay.scene_resolution", scene="jerribeth." + scene)
            continue
        events[scene]["Title"] = title
    _apply(events, NODES, CHOICES, PARAS)


def fill(payload):
    events = _scenes(payload)
    _apply(events, NEW_NODES, {**CHOICES, **NEW_CHOICES}, NEW_PARAS, appended=True)
    for scene, host in COMPANION_RESUME.items():
        with overlay_item():
            source = _node(events, scene, host)["Choices"]
            for page in events[scene]["Nodes"]:
                if page["Id"].startswith("companion_"):
                    for index, choice in enumerate(page["Choices"]):
                        if choice["Text"].startswith(PENDING):
                            choice["Text"] = source[index]["Text"]
    left = ["%s/%s" % (scene, page["Id"]) for scene, event in events.items()
            for page in event["Nodes"]
            if page["Text"].startswith(PENDING)
            or any(choice["Text"].startswith(PENDING) for choice in page["Choices"])]
    for address in left:
        scene, node = address.split("/", 1)
        record("overlay.placeholder", scene="jerribeth." + scene, node=node)
