"""Minagho and Chivarro base layer: Claude voice pass (edge-fix job 9, minachiv-rebuild.md §5).

Text only. Ids, Next, Set, Requires/Forbids, checks, costs and choice order belong to
minagho_chivarro_continuation, the round overlays and minachiv_scaffolding (Codex job 4);
this layer replaces player-visible text on nodes and answers that already exist, adds
flag-gated paragraphs, and retitles the rebuilt scenes. Every key must resolve: a missing
scene, node or answer index is an error, never a silent skip.

integrate() runs right after minachiv_scaffolding.integrate (minagho_chivarro_trickster),
so it also writes the answers the scaffolding copied or appended. Slot nodes take their
heated-cut default from the slot brief (tools/route_packs/explicit_slots/), followed by
the aftermath written here. Scenes written here are locked in
tools/route_packs/voice_locks.json.

Brand variants: paragraphs gated on minachiv.brand_live (live: it bleeds and wants the
Commander's blood, fe0c87ea/5b25901c) or forbidding it (healed: she misses the excuse).

Canon used (enGB): fe0c87ea, 5b25901c, 9428f5e9, 537c1e5e, 571a019d, 9fb4396d, 5f3f7055,
c151ae0f, bd9912ec, 165441c8, 66f981f6, 6c535864, d1bfd4e0, ffd1ba0b, 3cf9393f, 3a0074c4.
RanRomance: the illusion-piercing guards (RanRomMinaBook01Page004Cue0001), the tavern beer
(RanRomMinaBook03EndCue0001), the soldiers who train her (Legend) and the dragons (Golden
Dragon) (RanRomMinaSlide0006/0007). Authored, no canon claim: the cellar house under the
burned market, Sivane as house succubus, Orven, the horned rumour-broker's agent, the
lieutenant, the Kenabres survivor at the well, the forger, Nerath the wool-factor and his
clerk, the bouncers.
"""
import json
from pathlib import Path

from story_format import p

P = "minachiv."
PENDING = "[PROSE PENDING:"
BRAND = P + "brand_live"
SLOTS = Path(__file__).resolve().parents[1] / "tools/route_packs/explicit_slots"

TITLES = {
    "the_remaining_customers": "The list",
    "what_the_offer_bought": "The empty counting room",
    "minaghos_unfinished_sentence": "Mina in the street",
    "the_performer_and_the_key": "The house under the market",
    "the_price_of_her_name": "The forger",
    "the_first_small_audience": "Forever, if your pockets are deep enough",
    "when_the_door_opens": "Priced at the door",
}

NODES = {}
CHOICES = {}
PARAS = {}
# Slot node -> (brief directory, aftermath appended after the brief's default_text).
SLOT_TEXT = {}


def text(scene, node, body, *choices, paras=()):
    NODES[(scene, node)] = body
    for index, choice in choices:
        CHOICES[(scene, node, index)] = choice
    if paras:
        PARAS[(scene, node)] = list(paras)


def answers(scene, node, *choices):
    for index, choice in choices:
        CHOICES[(scene, node, index)] = choice


def live(body):
    return p(body, requires=(BRAND,))


def healed(body):
    return p(body, forbids=(BRAND,))


def when(flag, body, forbids=()):
    return p(body, requires=(flag,), forbids=forbids)


def always(body):
    return p(body)


SEELAH, REGILL = "seelah.in_party", "regill.in_party"
LANN, WENDUAG, GREYBOR = "lann.in_party", "wenduag.in_party", "greybor.in_party"

# ---------------------------------------------------------------------------
# two_answers (RE-VOICE)
# ---------------------------------------------------------------------------
S = "two_answers"
text(S, "start", '''{n}Minagho has sent word. She wants you somewhere nobody in the street can see in, and she has drawn a little skull on the message to make sure you come.{/n}''')

text(S, "native_meeting", '''{n}A folded note reaches you in Drezen, addressed in a name she wears better without its human face: Mina. Inside, Minagho has drawn a little skull beside an hour and an address in the burned quarter. Below it, in a smaller and much nastier hand, someone has added: "If this is her idea of a reassuring invitation, bring a knife."
The address is a room above a shuttered gaming house. You find Minagho there after dusk, in the blonde woman's shape she wears for your city. She lets it fall the moment the door is barred. The room has no window on the street. She chose it for that.{/n}
"She insisted on reading what I wrote. Then she insisted on making it worse. I nearly wept from nostalgia."
{n}She taps the second hand on the note.{/n} "She has answered, darling. She is coming by her own road, with a great deal more caution than my little skull suggests."
"I rented this for a few meetings. Do not infer that I have settled down and started collecting respectable neighbours. One of them tried to sell me a history of the siege. He had me sobbing with laughter over Staunton. I made Staunton sob. It is not the same thing."''',
     (0, '"What does Chivarro want from this meeting?"'),
     paras=(
         live('''{n}When she turns from the lamp, the mark on her forehead has opened again. A thin line of blood runs down the middle of her eyeless face. She wipes it with her thumb and licks the thumb clean.{/n}
"Don't stare. It has done this since Kenabres. It aches all day, and twice as much when you walk in. You know why, sweetie. You are the one who made me fail there, and the damned thing has a long memory."'''),
         healed('''{n}She touches her forehead where Baphomet's mark used to bleed. The skin is closed. She seems to resent it.{/n}
"Clean. Do you know how inconvenient that is? For years I had an excuse for my temper. Now I have to manage on character alone."'''),
     ))

text(S, "local_meeting", '''{n}Minagho has sent an address across Drezen: the room above a shuttered gaming house. Chivarro has scratched out the little skull on the invitation and written the hour twice, the second time underlined until the nib tore the paper. When you arrive, Minagho takes the sheet out of your hand.{/n}
"She knows the road. It is three streets from her room. This time she insists on meeting you with her clothes on and her temper intact. I give the clothes an hour."''')

text(S, "reply", '''"To see me. To find out whether winning has made you insufferable. And to discuss a man who owes her something. In that order, though she will swear the last is first."
{n}She unfolds a second sheet. The handwriting is small, savage and perfectly level.{/n}
"Listen to this. 'I shall not arrive as the grateful dependent in whatever version of me you have been peddling.' A whole line to tell me something I already knew. She always did charge by the word."
"Is she your dependent?"
"Ask her that, sweetie. Please. I want to watch her take your face off."
{n}For a moment the grin goes somewhere warmer, somewhere she never takes it in the street.{/n}
"She walked out of her own house to come and find me, and she will gut anyone who speaks softly around the holes in her life. So will I. We can have a perfectly vile evening without anyone pretending to be harmless."''')

text(S, "scrolls", '''"Yes. Those were ours. This one has you in it."
{n}She folds the smaller sheet along its old crease.{/n}
"She knows I have talked about you. I spared her the recitation. If she wants your version she will take it out of your head without asking, so I recommend the truth. It saves you remembering which of us you lied to first."
"You give that advice often?"
"Only when lying would make my evening more tedious."''')

text(S, "asking", '''"Very little. She has agreed to come. You may agree to come. It is an obscene quantity of agreement for people with our histories."
{n}She hooks the empty chair with one hoof and drags it round to her side of the table. Not opposite. Beside.{/n}
"Sit, darling."
"There is a man called Veyr who used to buy and sell introductions for her house. Not a friend. Friends cost less and lie less. He has heard she wants a new foothold and offered her one. He also knows she has found me, which is the part I mind."
"A threat?"
"He calls it an opportunity. Chivarro thinks it is both. I think he has discovered a lovely new way to get his throat opened. She wants to talk to him before I demonstrate."''',
     (2, '"I will meet her and hear what Veyr is selling."'))

text(S, "past", '''"Oh, I remember, darling. I remember how fast you came when I sent for you. How you begged to see me again. Don't make that face. You did."
{n}She leans in until her breath is on your mouth, and stops there, because stopping is crueller.{/n}
"But I am not sending Chivarro a place setting and announcing she has acquired a lover. She has opinions about surprises like that. Several of them are fatal."
"Do you want me there?"
"Yes. For reasons I have already been stupid enough to let you hear. And because the two of you will disagree about something, and I have missed enjoying a fight that doesn't end with an assassin in the window."
{n}She lays her hand over yours on the table and presses, only with the tips of her claws, until you can feel all five.{/n}
"Come, my pet. Or don't, and I'll tell her you were frightened of her."''')

text(S, "refusal", '''"I heard you the first time, Golarian."
{n}Too quick. She hears it herself, and bares her teeth at it.{/n}
"There are other uses for your company. You know what was done to me. Chivarro knows what was done to me before you. Veyr will find it much harder to sell each of us a different story if all three of us are sitting in the same room, looking at his face."
"And afterward?"
"Afterward we find out whether talk alone is as tedious as I remember. If you surprise me, I'll pretend I expected it."''')

text(S, "agreement", '''{n}Minagho writes the hour on the back of Chivarro's reply, folds it into a narrow packet and tucks it down her bodice.{/n}
"She comes by a road she chose. No procession, no escort, no grateful crowd. If one of your officers tries to show her off as a prize, I shall send you the pieces of the banner."
{n}At the door she catches your sleeve, and then the wrist under it.{/n}
"Thank you for coming, darling. There. That is the last agreeable thing I am saying tonight. Get out while you still believe it."''')

# ---------------------------------------------------------------------------
# the_remaining_customers (REBUILD: "The list")
# ---------------------------------------------------------------------------
S = "the_remaining_customers"
text(S, "start", '''{n}The factor is already at the table when you climb the stair: a mortal in a good grey coat, a flat case under one hand and a sealed letter under the other. Orven. Veyr's man. He has taken the chair that faces the door, which tells you he has sat in rooms like this before.
Minagho stands at the second door in Mina's blonde face, arms folded, as if she were the hired girl. Orven glances at her once, and then a second time, and his hand closes on the case.
Chivarro sits across from him with a cup she has not offered to share.{/n}
"Say it again for the Commander, honey. Slowly. I want to watch you try."
{n}Orven clears his throat.{/n} "Master Veyr wants six names. Six of the lady's old guests. Not the names they use at court; he has those. The names they used at her house, with what they asked for written beside them."
"So he can milk them," {n}Chivarro says.{/n} "Go on."
"Master Veyr has an underwriter for the venture. The underwriter has a client. The client is less interested in six old customers than in where a certain lady sleeps." {n}His glance goes to the second door again.{/n} "If the names are sold, the address stays off the market. If they are not, the client buys it instead. I am only the messenger."
"Liar." {n}Chivarro hasn't moved, but she is inside his head; you can see him feel it, like a draught.{/n} "You're paid twice, sweet. Veyr pays you to carry the letter. The client pays you to look at her face, so you can describe it. You've been looking at it since you sat down."
{n}Minagho smiles with Mina's pretty mouth.{/n}
"Sweetie, if you touch that seal again I'll bite your fingers off and make you watch me spit them out."
{n}Orven takes his hand off the seal.{/n}''',
     (0, '"Orven. Wait on the landing."'),
     paras=(
         when(REGILL, '''{n}Regill has followed you up the stair. He studies the factor as if measuring him for irons.{/n} "Extortion, traffic with agents of the Abyss, and a demon under a false face in a crusader city. Hold this man for the Order, Commander. The two lilitu I will discuss with you later. At length."'''),
         when(WENDUAG, '''{n}Wenduag leans in the doorway, delighted.{/n} "Look at him sweat. She hasn't even touched him."'''),
         when(LANN, '''{n}Lann watches the lilitu work the factor with the queasy fascination of a man at a dogfight.{/n} "Remind me never to owe her money."''', forbids=(WENDUAG,)),
     ))

text(S, "plans", '''{n}Orven goes out onto the landing. Minagho shuts the door on him with her hip and lets Mina's face drop off like a shawl.{/n}
"A convincing mistake. We give him an appointment. A false one, in a room I choose. The buyer's dog comes sniffing for my bed and finds me in it, awake. I want to know which of Baphomet's servants is still spending money on me. Then I want to make him stop."
"You promised me a meeting," {n}Chivarro says.{/n} "Not a war. I will not buy my way back into business by being the bait in your next private feud."
"He has already made you bait, sweetie. I only propose to choose the hook."
{n}Chivarro pulls a clean sheet toward her and writes six names down the side of it without looking at the pen. She knows them the way other women know prayers.{/n}
"A grain contractor who likes to be whipped by somebody's grandmother. A priest who paid to be told he was filth. Two brothers who never found out about each other. A judge. A man I still can't describe at table. They paid me to forget them. Veyr wants to sell them remembering."
"Then sell him the bastards," {n}Minagho says.{/n} "What do you owe them?"
"Nothing. That isn't the point. The point is whose house the knowing belongs to. Mine."
"You don't have a house."
{n}Chivarro's mouth goes thin. Neither of them looks at you. This is an argument they have had before, across a much larger room, and each knows exactly where the other bleeds.{/n}''',
     (0, '"Show me Veyr\'s letter."'),
     (1, '"Minagho. What are you putting at risk?"'),
     (2, '[Have Orven brought back in, and make him name the client\'s man and where he meets. Persuasion, DC 30.]'))

text(S, "stake", '''"My face. My neck. Whatever reputation I have left, which is mostly rumour and other people's corpses."
"Something you would mind losing," {n}Chivarro says.{/n}
{n}Minagho goes still. When she answers, it isn't a confession. She throws it.{/n}
"You. You stupid bitch. Do you think I spent all that time running the other way for my health? Every hunter Baphomet sent after me knew your name. I stayed away so they would have to work for it. And now you sit here haggling over six fat men's appetites while a buyer prices my bed."
{n}Chivarro's anger doesn't go anywhere. It only has to make room.{/n}
"Then don't decide for me that a clever trap is worth it."
"I'm telling you before I set it. You may consider that romance."
"I consider it an improvement. Barely."
{n}Minagho snorts and shoves the letter across the table at you.{/n}
"Read it, darling. If he's been careless, I want to know before she talks me into behaving."''',
     (0, '[Read Veyr\'s letter.]'))

text(S, "document", '''{n}Veyr's letter is short and smooth, which is the worst thing about it. It names the six as "the lady's remaining customers", offers Chivarro a share in a private gathering where they will be introduced to "new friends", and closes with a sentence about the underwriter's client so carefully worded it might as well have teeth.
Orven waits on the landing. You can hear him not moving.
Chivarro turns her cup in a slow circle.{/n}
"Well, Commander. You're the one with the army. I'm the one with the names. She's the one with the address. Somebody at this table has to say something stupid first."
"I've said mine," {n}Minagho says.{/n} "Bait."
"And I've said mine. I keep my house's secrets, or I sell them for a price that buys a house." {n}Chivarro tilts her head at you, the way she prices a guest on the stair.{/n} "So what are you paying for tonight, honey? Me, her, or the house?"''',
     (0, '"Sell him the names. Keep your house alive."'),
     (1, '"Give him an appointment. A false one, in a room she chooses."'),
     (2, '"Tell Veyr to go fuck himself."'),
     paras=(
         when(P + "source_found", '''{n}Orven's scrap of paper lies beside the letter: no name, only a horned mark; an empty counting room in the lower town; the second bell.{/n}'''),
     ))

text(S, "source_named", '''{n}You have Orven brought back in and seated where he can see Minagho's real face. Then you talk to him about the Inquisition, about what the crusade does to men who sell its Commander's guests to the Abyss, and about how little of that need happen if he is helpful.
He is very helpful.
The client's man has no name; he signs with a horned mark. He buys rumours for servants of Baphomet and sells them on. He meets his sellers in an empty counting room in the lower town after the second bell, alone, because he likes to believe nobody would dare.
Chivarro listens with her chin on her hand. When he's finished she reaches across the table and pats his cheek, twice, hard.{/n}
"There. Was that so terrible? Go and wait outside. If you run, she'll know before you reach the street."
{n}Minagho blows him a kiss.{/n}''',
     (0, '[Send him back to the landing.]'))

text(S, "source_hidden", '''{n}You have Orven brought back in and lean on him. He sweats, he stammers, he apologises, and he gives you nothing but Veyr's name, over and over, like a charm against the dark.
Chivarro leans into his head and takes a long, unhurried look round. Then she sits back, disgusted.{/n}
"He doesn't know, honey. Truly. They kept him stupid on purpose. It's the only clever thing Veyr has ever done."
"Let me have one finger," {n}Minagho says.{/n} "On principle."
"No. If he bleeds on my table, the price goes up."
{n}Orven goes back to the landing a great deal faster than he came in.{/n}''',
     (0, '[Let him go back out.]'))

# ---------------------------------------------------------------------------
# what_the_offer_bought (REBUILD: "The empty counting room")
# ---------------------------------------------------------------------------
S = "what_the_offer_bought"
COUNTING_ROOM = '''{n}The counting room is empty except for a desk, a cold brazier and three chairs.'''

text(S, "start", '''{n}Minagho meets you at the gaming house with her cloak already fastened and something long and thin underneath it. Chivarro is at the table counting a purse. She counts it once, closes it, and makes herself put it away.
The answers have come back. Nobody mistakes the evening for a visit.{/n}
"Before we go," {n}Minagho says,{/n} "tell me your plan again without the parts that make it sound pleasant."
"An unusual request, from you," {n}Chivarro says.{/n}
"I contain multitudes, sweetie. Most of them armed."''',
     (0, '"Veyr has his names. We go and watch him collect."'),
     (1, '"The false appointment. Let\'s go and meet her hunter."'),
     (2, '"Your gathering, without Veyr. Then we see who comes knocking."'),
     (3, '"I never gave you my answer. I\'m giving it now."'))

text(S, "late_plan", '''{n}Chivarro looks up from the purse.{/n}
"You left us with a letter and a factor on the landing, honey, and walked off to run a war. Veyr has been paid for his patience. He won't be paid twice. Choose."
{n}Minagho says nothing at all. She chose a long time ago, and she wants you to see what it costs her to let you.{/n}''',
     (0, '"Sell him the names."'),
     (1, '"The false appointment. Her room, her hook."'),
     (2, '"Veyr can go fuck himself."'))

text(S, "business", '''{n}Veyr's gathering is in a hired room above the market, all borrowed candlesticks and good wine. Chivarro's six come in under the names they used at her house. Each of them sees her and goes the colour of old cheese. She greets them by their appetites, quietly, one at a time, and watches each of them understand what Veyr has bought.
Orven moves among them with a list. Veyr himself does not come. He has the sense to be elsewhere.
Halfway through the evening a thin, horned stranger in gloves too fine for the dust on his coat slips in by the service door. He doesn't want the six men. He goes from guest to guest, asking quiet questions about a blonde woman called Mina, and where she sleeps.
Minagho, beside you in Mina's face, listens to him come closer, and closer.{/n}
"There he is," {n}she murmurs.{/n} "Bought and paid for with her names. Darling, I could kiss Veyr. I won't. But I could."
{n}When the agent reaches the back stair, Minagho is already through the door ahead of him. Chivarro takes your arm.{/n}
"The counting room," {n}she says.{/n} "Down the lane. She'll want an audience."''',
     (0, '[Follow them to the counting room.]'))

text(S, "business_end", COUNTING_ROOM + ''' The agent comes down the lane alone, thinking he is following a blonde girl to a cheap bed. He finds Minagho waiting with her own face on and the inner door at her back.
She shuts it behind him.{/n}
"I want you looking at me when you realize."
{n}He realizes. You watch it happen: the little horned man understanding all at once that the rumour he was paid to price is standing a foot away, smiling, and that she has been hunted by far better than him.
Minagho takes the coded list from his coat while he is still deciding whether to scream. She runs a claw down the marks, and starts to laugh.{/n}
"Oh, sweetie. Look at this." {n}She holds it up for Chivarro.{/n} "Six names, appetites beside them. Your hand. Your little marks. You sold them to Veyr, and then you sold them to him."
"Twice the price," {n}Chivarro says.{/n} "Veyr's money bought the gathering. His bought the guests. The Commander said sell them. The Commander never said to whom."
{n}Minagho isn't angry. That is the frightening part. She regards Chivarro the way she regards a well-made trap.{/n}
"And my cut?"
"You were the bait, honey. Bait doesn't get a cut."
"I'll remember that."
{n}She turns back to the agent and peels the fine gloves off his hands, one finger at a time.{/n}
"Run home. Tell your mistress I'm awake and I have her list. Tell her I'm wearing your gloves."
{n}He runs. Chivarro counts her purse again, and this time she lets herself enjoy it.{/n}''',
     (0, '[Walk back with the takings.]'))

text(S, "bait", COUNTING_ROOM + ''' Minagho checks behind the inner door. Chivarro lays the false invitation on the desk where a man coming in will see it first.
The agent comes alone, as promised: thin, horned, gloves too fine for the dust on his coat. He stops dead when he sees Minagho's real face. She shuts the inner door behind him.{/n}
"I want you looking at me when you realize."
{n}He realizes. She lets him take his time about it.{/n}
"Sit."
{n}He sits. His mistress, it turns out, is nobody much: a dealer in rumours who bought into the hunt when the last hunter failed, betting that someone in Baphomet's service will pay well, one day, for an address. He carries no orders. He carries a coded list.
Minagho reads it. Then she reads it again, slowly, and her grin goes very wide.{/n}
"Oh, sweetie," {n}she says, and not to him.{/n} "Six names. Six appetites. In your hand."
{n}Chivarro doesn't pretend.{/n}
"I sold them to him on market day." {n}She turns to you.{/n} "You chose bait, honey. Nobody said the names stayed in the drawer. You weren't paying for the house."
{n}Minagho isn't angry about the names. You can see exactly what she is angry about.{/n}
"And you didn't cut me in."
"You were the bait. Bait doesn't get a cut."
"I am going to remember that for a very long time."
{n}Then she turns back to the agent, and remembers she has one of those, too.{/n}''',
     (0, '"His life. He goes home to his mistress with your warning."'),
     (1, '"His list stays here. Then he can go."'),
     (2, '"He\'s yours."'),
     (3, '"The Inquisition gets him."'),
     paras=(
         live('''{n}The brand has opened. Blood runs from the mark on Minagho's forehead, down her eyeless face, into the corner of her mouth. She licks it away and leans close to the agent.{/n}
"Do you know what this is, sweetie? Baphomet's love-letter. It hurts all the time, and it will go on hurting until I spill the blood of the one who made me fail at Kenabres. Yours won't do. Yours is cheap." {n}She lifts her chin toward you, over his shoulder.{/n} "That one's would. That one is standing right behind you. Isn't it funny, the company I keep?"'''),
         healed('''{n}Minagho touches her forehead where the brand used to bleed, as if she misses having something to blame for her temper.{/n} "Pity. In the old days I could have told you this was Baphomet's fault. Now it's only me."'''),
         when(SEELAH, '''{n}Seelah has stopped in the doorway and will not come further in. Her hand is on her sword, and her attention is on you.{/n}'''),
         always('''"Well, Commander? He came for my bed. What does he leave this room with?"'''),
     ))

text(S, "warning", '''"You're letting him keep a great deal, darling."
"He came to buy an address. He can go home having bought nothing."
{n}Minagho strips the gloves off his hands, finger by finger, and pulls them on over her own claws.{/n}
"Tell her I'm awake. Tell her I'm wearing your gloves. Tell her the next one she sends, I keep."
{n}The agent leaves at a pace that becomes a run on the stairs. Minagho listens until his footsteps are gone, flexing the stolen leather.{/n}
"I could have learned so much more."
"Yes," {n}Chivarro says.{/n} "And I could have sold more. We both made sacrifices tonight."
{n}Minagho tears the false invitation down the middle and drops the halves in the cold brazier.{/n}
"His face, though. When he realized. I'm keeping that." {n}She takes Chivarro's arm, and then, after a moment, yours.{/n}''',
     (0, '[Leave the counting room with them.]'))

text(S, "list", '''{n}The agent lays his coded list on the desk and explains the marks, the ones for a buyer and the ones for a rumour, while Chivarro corrects his pronunciation of her own customers. Minagho folds the list and tucks it into her bodice. Then you let him go, and he goes as fast as a man can go without running.{/n}
"There are people in this city who deserve a nasty surprise," {n}Minagho says, patting the paper.{/n} "Now I know which of them are buying."
"Don't start a second war and call it the end of the first," {n}Chivarro says.{/n}
"Sweetie. When have I ever needed to call it anything?"
{n}She doesn't ask your leave to keep it. She doesn't pretend she'll leave it alone. Outside, Chivarro starts naming the customers Veyr will never supply again, and Minagho laughs at every one.{/n}''',
     (0, '[Walk back with them.]'))

text(S, "agent_killed", '''{n}"Thank you, darling," Minagho says, and means it, which is worse.
She doesn't hurry. She talks to him the whole time, sweetly, the way she must once have talked to Staunton: oh, sweetie, don't look away, you came all this way to see me. When she opens him from throat to crotch she holds his chin so he watches it happen. It takes him longer to die than it should. She sees to that.
Chivarro steps back out of the spreading puddle and lifts her hem.{/n}
"Not on the shoes. These were expensive."
{n}Afterwards Minagho wipes her claws on his good coat, takes the list, takes his gloves, and stands in the doorway looking happier than you have ever seen her.{/n}
"One of the sweetest spoils of war, darling, is gloating over your broken and humiliated enemy. Nobody lets me do it any more. You have no idea what you've given me."''',
     (0, '[Leave him for the rats.]'),
     paras=(
         when(SEELAH, '''{n}Seelah tried to stop it. She wasn't fast enough, and she has not said a word since. She isn't looking at the body. She is looking at you.{/n}'''),
     ))

text(S, "agent_handed_over", '''{n}You send for the watch. Two of your soldiers and a grey-faced inquisitor come down the lane at a run and take the agent in irons, list and gloves and all. The inquisitor thanks you. The crusade will be grateful; men like this are threads, and threads lead to rooms.
Minagho stands very still while they take him. She doesn't argue. She doesn't raise her voice. When the soldiers are gone she turns her face toward you, and for a moment there is no Mina anywhere in it.{/n}
"You took him off my plate, darling. Off my plate, in front of me, and handed him to your fucking priests."
"He'll talk to them."
"He'd have talked to me. Louder." {n}She smiles, very sweetly.{/n} "I'm going to remember this. Not tonight. Some night when you've forgotten it. I'll bring it out, and we'll look at it together."
{n}Chivarro takes her arm. Minagho lets herself be taken, but she walks the whole way home a little ahead of you, where you can see her back.{/n}''',
     (0, '[Let her walk ahead.]'))

text(S, "independent", '''{n}You told Veyr where to go, and Veyr went there. Chivarro holds her own gathering in the smaller room, with her own money: two old acquaintances, good wine, no Orven. She introduces them to each other and lets each decide what the other is worth.
In the middle of it, someone knocks at the gaming-house door below. Minagho goes down. When she comes back up she is smiling the smile she keeps for good news about other people's pain.{/n}
"There's a man in the street asking for Mina," {n}she says.{/n} "Horned. Lovely gloves. He has a list in his coat with six names on it, darling, and I know the hand."
{n}Chivarro goes on pouring.{/n}
"Shall we go and talk to him?" {n}Minagho says.{/n} "I've found an empty counting room down the lane. I've always wanted one."''',
     (0, '"Chivarro. Did you sell those names?"'))

text(S, "independent_end", '''"Of course I sold them."
{n}She says it in the counting room, with the agent in the third chair and Minagho holding his coded list up between two claws. The six names are in Chivarro's hand. Her little marks are beside them.{/n}
"You said not to sell them, honey. You weren't paying for the house. Veyr wanted them for a gathering. His buyer wanted them for a hunt. Only one of them paid in advance."
"You sold the names to the man hunting me," {n}Minagho says.{/n}
"I sold him six fat men. He bought a map to you. That's his mistake, not mine. And look where it's brought him."
{n}Minagho turns to the agent. The agent looks at the floor.{/n}
"You didn't cut me in," {n}Minagho says.{/n}
"You'd have spent it on knives."
"I'd have spent it on very good knives." {n}She leans over the agent, peels the gloves off his hands and pulls them on.{/n} "Go home, sweetie. Tell her I'm awake. Tell her I'm wearing your gloves."
{n}He goes. Chivarro counts her purse, and this time she enjoys it, and she doesn't care at all that you're watching her enjoy it.{/n}
"There. My first takings in your city, Commander. Don't scowl. You'll get used to me."''',
     (0, '[Leave the counting room with her takings.]'))

# ---------------------------------------------------------------------------
# minaghos_unfinished_sentence (REBUILD: "Mina in the street")
# ---------------------------------------------------------------------------
S = "minaghos_unfinished_sentence"
text(S, "start", '''{n}Dusk in Drezen. The street below the rented room's stair is full of Kenabres people: refugees who came north behind the crusade and stayed, because there was nothing left to go back to. Minagho comes down the stair in Mina's blonde face with a chipped cup of tavern beer, and stops on the last step to complain to you about it.{/n}
"It tastes like a paladin's bathwater. I keep drinking it. Don't tell Chivarro; she'll think it means something."
{n}A man at the well turns round. He is old for a soldier and missing two fingers, and he wears a cheap charm at his throat, a twist of silver wire no bigger than a thumbnail. Some of the guards in this city wear them, so they can see through a glamour.
He looks at Mina. He keeps looking. The cup stops halfway to her mouth.{/n}
"I know you," {n}he says. Quietly, at first.{/n} "I know you. You were on the walls. At Kenabres. You were on the walls, laughing."''',
     (0, '[Step down beside her.]'))

text(S, "history", '''{n}He says it again, louder, and this time the street hears him. Heads turn at the well, at the bread stall, in the tavern door. Kenabres faces, most of them: people who climbed out of that city with whatever they could carry and have been carrying it ever since.
Somebody throws a stone. It takes Minagho on the cheekbone, and Mina's face flickers over the wound like a candle in a draught.{/n}''',
     (0, '"She has worked for the crusade. Ask anyone in the citadel."'),
     (1, '[Watch the back of the crowd.]'),
     (2, '"The dragons speak for her. Leave her be."'),
     (3, '"She trains with my soldiers. Ask them."'),
     (4, '[Stand where the crowd can see you.]'),
     (5, '"She is bound in my service. Stand back."'),
     (6, '"Mina. Upstairs. Now."'),
     paras=(
         live('''{n}Then the brand opens. Blood comes out of the mark on her forehead straight through the glamour, as if the glamour were not there: a bright line down the middle of her eyeless face. The street sees it. Somebody screams. Minagho licks the blood off her lip and grins at all of them.{/n}
"Well? Which of you mangy rats was it? Which of you made me fail at Kenabres? Come here, sweetie. I'd love to bleed you."'''),
         healed('''{n}Then the glamour gutters and goes out. Under it there is no brand-blood: only her own eyeless face, grinning around the cut on her cheek. She spreads her arms so they can all get a good look.{/n}
"See? Not a drop from the mark. Doesn't that make you sick, you Golarian scum?"'''),
         always('''{n}The crowd is thirty strong now, and it has found its voice.{/n}'''),
         when(SEELAH, '''{n}Beside you Seelah has gone very still.{/n} "Commander. I know that laugh. I heard it in Kenabres."'''),
         when(REGILL, '''{n}Regill does not raise his voice.{/n} "Execute her, Commander, and the crowd goes home. That is the whole of the problem and the whole of its solution."'''),
     ))

text(S, "redemption", '''{n}"She's been working for the crusade!" somebody shouts, half pleading, as if it might still turn out to be true.
Minagho laughs out loud.{/n}
"Redemption. Do you hear that, sweeties? Your Commander thinks I've been redeeming myself." {n}She spits in the gutter.{/n} "I've been running errands. I fetched and carried and told your priests things, and they patted my head, and I wanted to bite every one of them. If that's redemption, you can keep it. I'd sooner throw myself off a tower. I've been invited to, you know. By people who meant it kindly."''',
     (0, '"You are not helping yourself."'))

text(S, "cult", '''{n}At the back of the crowd three men in plain coats have stopped watching Minagho. They are watching the people around them, the way guards do. One of them has a hand inside his coat. Then another. You catch the gleam of a blade.
Her people. Her congregation. Here.{/n}
"Oh, look," {n}Minagho says, delighted.{/n} "My little flock came to watch. Sweeties, put those away. If anyone is going to be gutted tonight, I want to do it myself." {n}She tilts her head toward you.{/n} "Or shall I let them, darling? They'd love it. They'd do anything I asked. That's rather the point of them."''',
     (0, '"Call them off. Now."'))

text(S, "training", '''{n}"Dragons!" someone jeers from a doorway. "The Commander says dragons speak for it!" Somebody laughs. Nobody in this street is impressed by dragons tonight.
Minagho isn't either.{/n}
"They do, you know. They sit me down and talk to me about my soul. There's gold in it, they say, buried under all the filth." {n}She wipes her face with the back of her hand.{/n} "I let them. It's restful, being lied to by something that big. But I'll tell you what my soul wants right now, sweeties. It wants whoever threw that stone. Go and ask a dragon what it would do about that."''',
     (0, '"Don\'t."'))

text(S, "legend", '''{n}"Leave her be!" A woman in a crusader's quilted coat shoves through the crowd, then another, then a third: soldiers off duty, the ones who spar with Minagho in the yard behind the barracks. "She's ours! She trains with us!"
"She killed my brother!" someone shouts back.
Minagho laughs at both of them.{/n}
"Both true. Isn't that lovely? I trained with them all morning and put every one of them on their backs. And I killed your brother, sweetie, or somebody very like him. I lose count." {n}She turns to the soldiers, almost fond.{/n} "Go home, little tin heads. Don't bleed for me. I'd only laugh."''',
     (0, '"Your friends are trying to help you."'))

text(S, "sanctuary", '''{n}"The Commander keeps it!" Someone has seen you. Heads turn your way. "Under the Commander's roof! The demon from the walls!"
Minagho grins at you over the crowd.{/n}
"There. Now they know. I live under your roof, darling, and eat your bread, and drink your appalling beer, and they'd like to know what you get for it." {n}She raises her voice, sweet as honey.{/n} "Shall I tell them? Shall I tell them all what I'm for?"''',
     (0, '"Don\'t you dare."'))

text(S, "service", '''{n}"Whose is it?" someone shouts. "Whose demon is that?"
Minagho turns to you, very slowly, and the whole crowd turns with her.{/n}
"Go on, Golarian. Tell them. I'm your pet. Bound in your service, signed and sealed." {n}She bares her teeth.{/n} "So leash me, or let me bite. Those are your choices. Everyone's watching."''',
     (0, '"She is under my command."'))

text(S, "freedom", '''{n}She doesn't move.
"Why is it still here?" A woman's voice, raw from crying. "Why is it still here, walking about, drinking our beer?"{/n}
"Because I like it," {n}Minagho says.{/n} "Because I could go anywhere in the world now, sweetie, and I chose your miserable city, and I'm going to stay until I'm bored of watching you choke on it."
{n}It isn't true, or not all of it. You know why she stays; it lives three streets away and is called Chivarro. But she would rather die in this street than say so to them.{/n}''',
     (0, '"Don\'t make this worse."'))

text(S, "morning", '''{n}The man with the charm has pushed to the front. He is shaking. He points at her with the hand that is missing two fingers.{/n}
"You should have learned. After Kenabres. After what we did to you there. You should have learned something—"
"An hour," {n}Minagho says.{/n} "One hour without somebody telling me what Kenabres ought to have taught me. I know what happened there. I was there. I watched your walls come down, and I laughed, and then I lost. I'm sorry I lost, sweetie. That's all I'm sorry for."
{n}A second stone. A third. Somebody has a cudgel. Somebody is shouting for rope.
Minagho doesn't run. She turns her face to you, in front of all of them, the way she might turn toward a door she isn't sure is locked.{/n}''',
     (3, '[Step in front of her.] "She is under my protection. Go home." [Persuasion, DC 31.]'),
     (4, '"Let her answer him."'),
     (5, '[Step back, and let the street have her.]'))

text(S, "protect_success", '''{n}You put yourself between her and the street, and you talk. About the crusade, and whose city this is, and what happens to people who riot in it. About Kenabres, too: you were there, you remember it, and you are telling them that this one is yours and that they will go home.
They go home. Slowly, sullenly, looking back. The man with the charm goes last. He spits at your boots on his way past, and nobody stops him, and neither do you.
By morning half of Drezen will know the Commander stood in the street for Baphomet's general. The crusade will not thank you for it.
Minagho waits until the street is empty. Then she wipes her face.{/n}
"Don't expect me to be grateful, darling. I hate owing. I hate owing you most of all. I'm going to hate it for weeks."''',
     (0, '[Let the street empty.]'),
     paras=(
         live('''{n}The brand is still bleeding. She is still grinning at the place where the crowd stood.{/n} "Do you know what's funny? The only blood that would have stopped this was standing in front of me the whole time, being noble."'''),
     ))

text(S, "protect_failure", '''{n}You put yourself between her and the street, and you talk, and it isn't enough. Kenabres is louder than you are tonight. A stone takes you on the shoulder. Someone gets close enough to rake Minagho's face with his nails before you knock him down.
The watch comes at a run, halberds levelled, and the crowd breaks only when there are spearpoints in it. By morning half of Drezen will know the Commander stood in the street for Baphomet's general, and lost the street anyway.
Minagho stands in the wreck of the bread stall with blood on her chin, laughing.{/n}
"Oh, that was magnificent. You were terrible. Darling, you were so terrible." {n}She stops laughing.{/n} "And now I owe you. I hate that. Don't you ever think I'll stop hating it."''',
     (0, '[Let the watch clear the street.]'))

text(S, "maim", '''{n}"Thank you, darling," Minagho says, and walks into the crowd.
It parts for her. Crowds do. She takes the man with the charm by the jaw, gently, the way you would take a lover's, and coos at him: oh, sweetie, you said my name so beautifully, say it again. When he opens his mouth to scream, she reaches in.
It is quick. It is not clean. She holds up what she took so the street can see it, and then she drops it down the well.
Nobody throws anything else. They melt away from her into doorways and alleys, dragging him with them, and the street empties as if a tide had gone out.{/n}
"There," {n}Minagho says, wiping her hand on Mina's skirts.{/n} "Now he can't name me to anyone. You see? I'm learning discretion."''',
     (0, '[Let the street empty.]'),
     paras=(
         when(SEELAH, '''{n}Seelah is white to the lips.{/n} "I'll be in the barracks, Commander. Don't send for me tonight." {n}She walks away without waiting to be dismissed.{/n}'''),
     ))

text(S, "abandon", '''{n}You step back. You fold your arms. You let the street have her.
It doesn't take long. Minagho fights, and she is still a demon, and two of them go down screaming. But there are thirty of them, with Kenabres in them. They get her down in the mud by the well. You hear the cudgels. You hear her laughing the whole time, through blood.
The watch breaks it up at last. When the street is empty she gets up on her own. She won't let anyone help her. She walks past you without stopping and says it very quietly, so only you can hear.{/n}
"You let them."
{n}Nothing else. She doesn't need anything else. You can tell she is putting it somewhere she will be able to find it again.{/n}''',
     (0, '[Follow her back to the stair.]'))

text(S, "street_after", '''{n}Later there is only the stair, the broken gutter, and rain beginning to tick on the cobbles where the crowd stood. Minagho sits on the third step in her own face, no glamour, the chipped cup between her palms. Somebody trod the beer into the street; she has refilled the cup from a bottle she stole from somewhere, and she drinks it as if it had insulted her.{/n}
"Chivarro was at the corner, on her way to look at some cellars under the old market. She heard the whole thing and didn't come back. That's how I know she loves me. She trusted me to enjoy it."''',
     (0, '[Take her hand.]'),
     (1, '"I can give you an hour and an opinion about that gutter."'),
     paras=(
         when(P + "street_protected", '''{n}She pats the step beside her. It isn't an invitation. It's an order.{/n} "Sit, my pet. You've earned a step. Don't let it go to your head."'''),
         when(P + "survivor_maimed", '''{n}There is still blood under her claws that isn't hers. She pats the step beside her with that hand.{/n} "Sit, darling. That was the best evening I've had since Drezen fell."'''),
         when(P + "street_abandoned", '''{n}She hasn't forgiven you. She hasn't decided whether she'll ever bother. She pats the step beside her anyway.{/n} "Sit, Golarian. I'm not finished hating you, but I'm cold."'''),
     ))

text(S, "hand", '''{n}She lets you take her hand. Then she turns it, so that it's her claws on your wrist and not the other way round.{/n}
"Chivarro asked me what you're like when you don't want an answer straight away. I told her to find out for herself."
"You could have told her."
"I could. I wanted her to have a reason to sit with you. Sit still, darling. I'm not finished."
{n}She leans in. Her breath smells of cheap beer and blood. When you turn your head she is already there, and she kisses you, not gently: she bites, and keeps biting, and laughs into your mouth when you flinch.
She pulls back just far enough to speak.{/n}
"Don't make this sensible. I've had enough sense tonight to last me a century."
{n}She stands, without letting go of your wrist, and tilts her head toward the room at the top of the stair.{/n}
"Well? The rain, or me?"''',
     (1, '[Let her drag you up the stair.]'))

answers(S, "hand_after", (0, '[Stay until the rain eases.]'))
answers(S, P + S + ".explicit.1", (0, "Continue"))
text(S, "hand_after", '''{n}Later the rain has eased and the room is dark. Minagho lies across you as if you were furniture she has paid for, one hoof hooked over your ankle so you can't leave without waking her.{/n}
"Don't move. You owe me for the street, and I'm collecting."''')

text(S, "roof", '''{n}Minagho accuses the absent roofer of theft, then sabotage, then an extravagant attempt to murder her personally by gutter. A ladder goes past in the street below. She stops, listens, and starts to laugh.{/n}
"Now I have to know which it was."
{n}Chivarro comes back up the street with a lamp in one hand and her account book in the other, smelling of cellar damp. Minagho lays out the theory as if it concerned the siege of Drezen. Chivarro sits on the step above to hear the evidence, and charges you for the lamp oil.{/n}''')


SLOT_TEXT[(S, P + S + ".explicit.1")] = ("minachiv", "")

# ---------------------------------------------------------------------------
# the_performer_and_the_key (REBUILD: "The house under the market")
# ---------------------------------------------------------------------------
S = "the_performer_and_the_key"
text(S, "start", '''{n}The old market burned in the siege. What is left of it is a black roof on charred posts, and under that a stair nobody repaired, and under that the cellars, which did not burn at all. Chivarro has taken them under a mortal name and a merchant's lease. There is a lamp at the bottom of the stair and a man beside it who is mostly shoulders.
Inside, the cellars run on further than the market above them ever did: vaults knocked through into vaults, curtains instead of doors, warm air, music from somewhere you cannot see, and the smell of wine and skin and lamp oil. A board by the entrance lists prices in chalk. Some of them are very high. One of them is only a question mark.
Chivarro meets you under the board, in her own face, in green silk, already pleased with herself.{/n}
"Welcome to my house, honey. Small. Damp. Mine. Don't touch the walls; the plaster's new and I haven't finished overcharging for it."
{n}A woman leans on the rail of the gallery above the main vault: a succubus, wings folded, wearing nothing she would describe as clothing and a great deal of contempt. She looks you over from boots to collar and makes no secret of the arithmetic.{/n}
"Our third opinion?"
"Our Commander," {n}Chivarro says.{/n} "Sivane, behave."
"I am behaving. I haven't bitten anyone in almost an hour."''',
     (0, '"Who is she, and what does she cost?"'))

text(S, "proposal", '''"More than you, sweetheart. Less than you'd hope."
{n}Sivane comes down the stair without hurrying. Up close she smells of cloves and something hotter underneath.{/n}
"I'm the house succubus. That means the men who come down that stair pay to be looked at by something that doesn't like them. I tell them what they are. I tell them what they smell like. Some nights I let one of them crawl. They queue for it." {n}She shrugs.{/n} "Mortals are very strange. I don't ask. I invoice."
"She wants a show," {n}Chivarro says.{/n} "Once a night, in the big vault, with the whole house watching her pick one fool and take him apart in front of his friends."
"Not wants. Will have. They'll pay double to watch, and triple to be picked."
"They'll pay what I say."
"Then say triple."
{n}Chivarro turns her face to you, delighted and pretending not to be.{/n}
"She's a bitch, honey. That's why I hired her. Come and see the rest before she asks for a raise."''',
     (0, '"Show me the house."'))

text(S, "room", '''{n}Chivarro walks you through it the way a general walks a captured fort.
The small vaults have curtains and a lamp each, and a number painted over the arch. The big vault has a low platform, benches, and a gallery where people who don't want to be seen can watch the people who do. There is a room that is only cushions. There is a room with a bath that someone has fed from a broken cistern above. There is a room with a locked door, and Chivarro does not open it, and does not explain.{/n}
"The locked one is for guests who know what they want," {n}she says.{/n} "Everyone else gets to find out."
{n}She stops by the third curtain. Behind it someone is making a noise that is not quite pleasure and not quite pain, and above it Sivane's voice, low and conversational, telling him exactly what she thinks of his mother.
Chivarro tilts her head, listening with more than her ears. Then she smiles, very slowly, at you.{/n}
"Oh, honey. You're going to love this one."''',
     (0, '[Pull back the curtain.]'),
     (1, '"Who\'s in there?"'))

text(S, "delay", '''{n}You pull back the curtain.
Sivane is sitting on a man's chest. He is naked except for a crusader's signet ring, and his shoulder is bleeding where she has bitten it, neatly, to the bone. He looks up past her hip at the lamp, and at you, and every drop of blood that is left in his face goes somewhere else.
You know him. He is one of your captains in the Drezen garrison. You signed his commission. Two days ago he stood in front of you and reported on the morale of the men.{/n}
"Commander," {n}he says, from under the succubus.{/n}
"Captain," {n}Chivarro says pleasantly, from behind you.{/n} "Don't get up. You've paid for another quarter of an hour."
{n}Sivane wipes her mouth with the back of her wrist and looks at Chivarro, then at you, then at the captain, and starts to laugh.{/n}
"He told me nobody important ever came down here."
"He was wrong," {n}Chivarro says.{/n} "That's going to cost him."''',
     (0, '[Let the curtain fall.]'),
     paras=(
         when(LANN, '''{n}Lann, behind you, has put his hand over his mouth. It is not, you suspect, to hide disgust.{/n} "I'm never going to be able to take an order from him with a straight face again. Ever."'''),
         when(GREYBOR, '''{n}Greybor regards the captain with professional interest.{/n} "Bitten clean. She knew where the artery wasn't. That's skill."''', forbids=(LANN,)),
     ))

text(S, "comparison", '''"One of yours."
{n}Chivarro doesn't open the curtain. She doesn't need to. She leans against the wall beside it and reads him through the cloth, the way you would read a sign over a shop.{/n}
"A captain. Garrison, not field. Married, and his wife thinks he is at prayers. He has come here four times. He asks Sivane to tell him he's a coward, and then he asks her to bite, and then he cries a little. He thinks nobody important ever comes down here." {n}She smiles.{/n} "You signed his commission, honey. He's thinking about that right now, because he heard my voice and he's wondering who I'm talking to."
{n}Behind the curtain, the noise stops. A man's voice, hoarse:{/n} "Who's out there?"
{n}Sivane answers for you, sweetly.{/n} "Nobody important, darling. Lie still. You're bleeding on my sheets."''',
     (0, '[Walk on before he sees you.]'))

text(S, "fee", '''{n}Afterwards, in Chivarro's counting alcove with a curtain drawn and a ledger open, she does the sums out loud.{/n}
"The captain bled on my sheets. That's extra. He bled on my sheets with the Commander of the Crusade in my house, which is a great deal extra, because I'm going to make sure he knows it, and then he'll never come back, and I'm charging him tonight for every night he won't." {n}She writes a number. You see it upside down. It is enough to buy a horse.{/n} "And Sivane is fined a week, because she bites the customers when I tell her to, not when she's bored."
"She'll pay that?"
"She'll pay it out of what he pays her to bite him again. They always come back, honey, whatever they swear on the stair." {n}She closes the ledger on her finger to keep the place.{/n}
"Now. You and I should talk business. He isn't the only one of yours who comes down my stair. There are eleven. Captains, quartermasters, a chaplain I'm very fond of. I know their names and I know what they ask for." {n}She holds out her hand, palm up.{/n} "Any of them can be yours for a price. A list. Every name, every appetite, every night they came. Wouldn't it be useful to know which of your officers are frightened of you for good reasons?"''',
     (2, '[Pay for the list] "Sell me the names."'),
     (3, '"No soldiers in this house. Not one."'),
     (4, '"It\'s your house. Run it."'))

text(S, "officer_names_bought", '''{n}She has the list already written. Of course she has. It comes out of the ledger on a single folded sheet, in a neat hand, with little marks beside the names that you are beginning to recognise.
She counts your coin twice and the list once.{/n}
"There. Eleven men who'll do anything you say, honey, as long as you never say it out loud." {n}She folds your hand over the paper.{/n} "Don't look so sour. They'd have sold you to me for less. Two of them tried."
"And you'll sell my name to someone else."
"Only if they pay better. Don't worry. Nobody pays better than the crusade."''',
     (0, '[Pocket the list.]'))

text(S, "soldiers_barred", '''{n}Chivarro considers you for a long moment. Then she laughs, picks up the chalk, and walks out to the price board at the entrance.
She writes, in letters a hand high: NO SOLDIERS. Then, without looking at you, she goes down the board and puts up every other price. Some of them by half. One of them she doubles.{/n}
"There. Your soldiers are barred, honey. Their money was a third of my takings. I'm going to collect that third from someone." {n}She dusts the chalk off her fingers.{/n} "Merchants. Priests. The kind of lord who comes north to see the crusade and stays to see the cellars. Your captains will go back to buying cheap girls in the lower town and catching cheap things from them. I hope you're proud."
{n}She is not angry. She is filing it. You will see this account again.{/n}''',
     (0, '[Let her keep her new prices.]'))

text(S, "house_tolerated", '''{n}Chivarro weighs you the way she weighed the captain's purse.{/n}
"It is, isn't it."
{n}She says nothing else for a moment. Then she leans across the ledger and pats your cheek, twice, hard, as if she were stamping a bill.{/n}
"That's the most expensive thing anyone's said to me since I came to Drezen. Don't think I won't hold you to it." {n}She sits back.{/n} "The captain pays double. Sivane pays her week. Your soldiers keep coming down my stair, and every one of them knows his Commander knows. You'll find them very obedient."''',
     (0, '[Leave her to her ledger.]'))

text(S, "pleasure", '''"I was. I could hear the moment he realised who was behind the curtain. It's a small sound. Usually the absence of breathing."
{n}She marks the ledger.{/n}
"Stand there. Yes. You're blocking the lamp; that's the point. I want every guest who comes down my stair to see somebody important first and wonder if it's them."''',
     (0, '[Keep the place she marked.]'))

text(S, "audience", '''"Watched. Priced. A little unsafe. They can be comfortable in their own beds."
{n}She walks to the curtain at the entrance and turns back with the welcome she gives a guest she means to empty.{/n}
"Come in. Never mind what you want, honey. I'll find out for myself."
{n}Then she drops it, and grins at your face.{/n}
"That one's free. The next one isn't."''',
     (0, '[Go back to the stair.]'))

# ---------------------------------------------------------------------------
# a_room_she_likes (RE-VOICE; hosts a slot)
# ---------------------------------------------------------------------------
S = "a_room_she_likes"
text(S, "start", '''{n}Chivarro's own room is above her house: up a ladder-stair from the counting alcove, through a trapdoor, into what used to be a spice merchant's loft under the market's burned roof. The beams are black. The floor is new. Through the boards you can hear the house working below: music, a laugh, someone begging Sivane for something and being refused.
She has hung the walls with red cloth bought from a quartermaster who should not have been selling it, and there is a couch, a chest with a lock, a table, and a bed behind a curtain. Nothing else. She has had a great many rooms with a great deal more in them.{/n}
"You may dislike it," {n}she says.{/n} "Out loud, if you like. I'll charge you for the opinion."
"The noise?"
"The noise is the best part, honey. That's money, coming up through the floor. I go to sleep counting it."''',
     (0, '"Why up here, and not down there with them?"'))

text(S, "choose", '''"Because down there I'm the house. Up here I'm only me, and nobody gets to buy that by the hour."
{n}She pours two cups of wine from a jug that came from a better cellar than this one.{/n}
"Minagho wanted to move in. All her knives, all her hatboxes, that terrible chair she stole from the citadel. I told her she could bring herself. The rest can stay in her room above the gaming house, where it offends nobody but the landlord."
{n}She hands you the cup with the unchipped rim.{/n}
"She called me a cold bitch. I kissed her until she forgot what she was saying. She'll be back to finish the sentence. She always is."''',
     (0, '"Show me the part you chose for yourself."'),
     (1, '"You wanted a door she has to knock on."'))

text(S, "notice", '''{n}Chivarro unlocks the chest and lifts out a single thing: a lamp of red glass, cracked, mended with wire.{/n}
"From the Delights. I took it when I left. Not the jewels, not the coin; this. It hung over my door, and I wanted the bastards to notice it was gone." {n}She sets it on the table.{/n} "They won't. Nobody in that house ever noticed anything they couldn't charge for."
{n}She lights it. The loft goes the colour of the inside of a mouth.{/n}
"There. Now it's a room. You may tell me it's vulgar."''',
     (0, '"It\'s vulgar. I like it."'))

text(S, "separate", '''"Of course I did. Do you know what happens when I share a bed with her every night? We fight. We fight about the rent, about knives on the pillow, about whether I'm too fond of my own house and whether she's too fond of being hunted. Then we fuck, and then we fight about that."
{n}She pours too much wine into your cup and doesn't apologise.{/n}
"This way she has to climb a ladder and knock on a trapdoor to start the fight. It slows her down. It gives me time to decide whether I want to win."
"And if she doesn't knock?"
"She knocks." {n}Chivarro smiles into her cup.{/n} "She'd sooner die than let me think she's sulking."''',
     (0, '"And tonight?"'))

text(S, "tea", '''"Tonight there's you, honey. I've been wondering what you'd cost."
{n}She sits on the couch and stretches her legs along it, so that there is no room beside her unless she moves them. She does not move them.
Below, Sivane's voice rises, sharp and amused, and a man's laughter cracks into something else. Chivarro listens, reading the room through the floor, and makes a small satisfied mark in the air with one finger.{/n}
"Another one who'll pay double. Do you know what I like best about my house? Every man who walks down that stair believes he's the first to want what he wants. I let him believe it. Then I charge him for it."
{n}She turns her face toward you and stops listening to the floor.{/n}
"You haven't asked me what you want. You're the only one who never does. It's very irritating."''',
     (1, '"Forget the floor. Come here."'),
     (2, '"Tell me something you\'ve done badly on purpose."'))

text(S, "close", '''{n}Chivarro moves her legs, finally, and lets you sit, and then puts them across your lap so you can't get up again.{/n}
"Took you long enough. I was beginning to think you'd come to inspect the beams."
{n}You kiss her. She catches your collar and holds you there, then loosens her grip enough to slide her hand inside your shirt.{/n}
"Stay. The house can rob its customers without me for one night."''',
     (0, '"I\'d like to stay here like this, and do nothing at all."'),
     (1, '"I\'m staying. All night."'))

text(S, "new_interest", '''{n}She doesn't make it easy. She weighs you up the way she weighs a new face at the bottom of her stair: pricing it, and enjoying the pricing.{/n}
"I've been wondering how long you'd sit there being tasteful."
{n}She holds out her hand, palm up, the gesture of a madam naming a sum.{/n} "Come and find out what I cost when I'm not charging."
{n}You take the hand and she pulls, not hard, only enough. The kiss begins as a negotiation and stops being one when she catches your lower lip between her teeth and doesn't let go until you make a sound she likes. Then she sits back, licks her lip, and leaves her hand on your thigh like a deposit.{/n}
"That's enough for tonight. I want you coming back up that ladder wondering what the rest of it costs."''',
     (0, '[Leave her wanting the rest.]'))

text(S, "warmth", '''{n}Chivarro stays against you while the house rises and falls under the floor. She tells you about a guest at the Delights who paid for an entire night of being ignored. She ignored him so well that he wept, and came back every month for three years, and left her a vineyard in his will. She sold it the same afternoon.
You ask why. She says she hates the countryside, and hated him, and liked the money, in that order.
Then she stops.{/n}
"That's a lie. I didn't hate him. He was the only one who never wanted anything from me but my back, and I charged him triple for it. Don't you dare repeat that."
{n}She kisses you to make sure you won't, and settles her head on your shoulder, and listens to her house making money until the lamp burns low.
At the trapdoor, later, she tells you to come back on a night when the house is full, so she can hear how much everyone below is envying you.{/n}''',
     (0, '[Promise to come back on a loud night.]'))

text(S, "later", '''{n}Chivarro sets your cup out of reach, deliberately, the way she would take a weapon off a guest at the door.{/n}
"First, your attention. All of it. You keep listening to the floor. Minagho would knock, honey. Once. For the pleasure of making me hear it."
{n}That amuses her until your hand finds her waist. For a heartbeat the clever answer goes out of her face. You've seen her recover from death threats faster.
She catches your wrist and pulls it tighter.{/n}
"There. You've found something useful to do with that. Do it again."
{n}You kiss her. The couch groans under the change in weight, and she glares at it with tremendous contempt.{/n}
"If you laugh, honey, I'll charge you for the couch."
{n}She drags you up, through the curtain, to the bed. She lights the red lamp and leaves the other dark. Her green silk goes over the chest; she stands over you in nothing but the red light and lets you look as long as you like, because she likes that more than you do.
Then she pushes you down, climbs over you, and finds your laces faster than you can find hers.{/n}''',
     (0, '[Stay until you are both ready to part.]'))

text(S, "friends", '''"Badly on purpose? Honey, half my career."
{n}She thinks about it, enjoying the choice.{/n}
"There was a duke at the Delights who explained my own house to me for an hour. How the girls should be arranged. What the music ought to be. So I gave him exactly what he asked for: the girl he described, the music he described, the room he described. He was bored out of his mind. He couldn't say so, because he'd designed it. He paid for a week of it, to prove he'd been right." {n}She laughs.{/n} "It was the worst work I've ever done. I've never been prouder."
{n}You trade stories of things done wrong on purpose: an order obeyed to the letter until it hanged the man who gave it; a letter written so politely it started a duel. Chivarro is less interested in why you did it than in how long it took the other fool to notice.
The house below quiets as the night goes on. When you get up to go, she catches your sleeve.{/n}
"Come up again. I like having someone up here who isn't trying to buy anything. It's so rare I don't know what to charge."''',
     (0, '[Leave her to the noise of her house.]'))

SLOT_TEXT[(S, P + S + ".explicit.1")] = ("chivarro", '''{n}Later, the red lamp has burned down to a smear of light. The house has gone quiet below; somebody downstairs is sweeping. Chivarro lies across you with one leg hooked over yours, listening to the broom.{/n}
"That's the last of them. Sivane made eleven tonight. I made more." {n}She turns her head.{/n} "You were free, honey. Don't let it go to your head. I'll find a way to charge you for it later."''')

# ---------------------------------------------------------------------------
# the_price_of_her_name (REBUILD: "The forger")
# ---------------------------------------------------------------------------
S = "the_price_of_her_name"
text(S, "start", '''{n}Minagho is waiting at the foot of Chivarro's ladder-stair in Mina's blonde face, with her arms folded, a handbill crushed in one fist and the glove on it split at the thumb. She has the look of a woman who has been insulted in a way she can't decide how to enjoy.{/n}
"How was her room?"
"Red."
"She loves that lamp more than she loves me. Never mind. Look at this."
{n}She smooths the handbill against the wall. It advertises private readings, this very evening, from "the captured correspondence of Baphomet's fallen general": the treachery at Drezen, the names of her secret worshippers, the men who bought her favour. Under the title a woodcut shows Minagho with a crown on, and enormous breasts, and an expression of tragic remorse.{/n}
"I never wore a crown. I'd have looked magnificent in one, but I never wore one. And that face." {n}She taps the woodcut's sorrowful little mouth.{/n} "Someone has drawn me sorry, darling. In my own city. For money."
{n}The reading is in a storeroom two streets away. She has found the door already. She has been standing here for an hour, waiting for you, so she would have someone to watch her be angry.{/n}''',
     (0, '"What do you want to do about it?"'))

text(S, "want", '''"Listen first. Then kill him. In that order, if you insist on order."
{n}She turns the handbill over. On the back someone has copied three lines in a cramped hand: an order for stores to be taken from a quartermaster who afterward disappeared.{/n}
"That one's mine. I wrote it. I remember the quartermaster; he squealed like a pig. But the date's been changed, and so has the buyer. Someone has given a dead man's stores to a buyer who's still alive and still rich, so the living one will pay to have his name left out."
"You're not offended by the forgery."
"Offended? Sweetie, I invented half of what's in that hand. I'm offended he's charging six coppers a head. Six. For me. I took this city. I'm worth a crown a seat and a fainting room." {n}Her lip curls.{/n} "And he's put words in my mouth. Little sorry words. I'll have them back, and his tongue with them."''',
     (0, '"Will this hurt the cult?"'),
     (1, '"You\'ve been working for the crusade. This will follow you."'),
     (2, '"What would the dragons tell you to do?"'),
     (3, '"Would the soldiers you train recognise you in these papers?"'),
     (4, '"You waited for me because you\'re bound to my service. Say so."'),
     (5, '"Let\'s hear what he thinks he owns."'))

text(S, "cult", '''"Hurt it? It'll feed it. Half my flock would pay a month's wages to hear my letters read aloud. The other half would pay to be named in them." {n}She considers.{/n} "I should have thought of it first. That's what's really eating me."
"And the living man he's named?"
"I have no idea what that man's bought, darling, and I don't care. He can buy his way out or hang. I want the forger's sources. Then I want the forger."
{n}She folds the bill small enough to disappear into her glove.{/n}''',
     (0, '[Go with her to the reading.]'))

text(S, "changed", '''"Oh, the crusade. Yes. I fetch for your priests and they pat my head." {n}Her grin is all teeth.{/n} "Do you think I care what follows me into that? Let it follow. Let them read every order I ever wrote out loud in the cathedral square. I'll stand at the back and correct the spelling."
"So you don't care."
"I care that he got it wrong. I care that he drew me sorry. I've never been sorry for anything in my life except losing, and I'll be damned if a copyist in a storeroom sells that to strangers for six coppers."
{n}She shoves the bill into your hand and starts walking.{/n}''',
     (0, '[Follow her to the reading.]'))

text(S, "dragon", '''"Something patient. They hoard patience the way they hoard gold. They'd tell me to let him live and learn from it." {n}She snorts.{/n} "I listen to them. It's restful, being lectured by something that big. Then I go and do what I like."
"And what do you like?"
"I'd like to see whether he bleeds ink."
{n}She tucks the bill away and turns her face down the street toward the storeroom, smiling the smile that the dragons have never managed to get off her face.{/n}''',
     (0, '[Go with her.]'))

text(S, "mortals", '''"Recognise me? Darling, they'd laugh themselves sick. Look at the tits on her." {n}She flexes one gloved hand; a seam by the thumb has split.{/n} "One of your tin heads did that this morning. I put him on his back six times and he caught my glove on his buckle on the seventh, and then he had the nerve to tell me to sew it myself."
"Did you?"
"I'm going to. With his hair." {n}She turns back to the bill.{/n} "I could walk in there as myself and watch the forger stop breathing. Or I could walk in as Mina and let him cheat me first. The second is much more fun. You get to see the moment they understand."''',
     (0, '[Go in with her.]'))

text(S, "service", '''"Bound, signed and sealed, my pet. So I'm asking." {n}The word comes out like something she has to cough up.{/n} "I'd like to kill a man tonight. Your enemies would love to see your demon accused in a crowded room. They'd love it even more if she gutted the accuser. Which amusement do you want me to supply?"
"Hear him first."
"Hear him first," {n}she repeats, sweetly, in your voice.{/n} "Of course. I'll hear him. And then I'll ask you again, and you'll have to say it out loud."''',
     (0, '[Attend the reading.]'))

text(S, "reading", '''{n}Six people sit on borrowed stools in a storeroom that smells of turnips. A narrow table holds a locked box, three copied pages and a cheap candle. The reader is a thin man in a good coat gone shiny at the elbows, with ink on his fingers and the voice of a priest at a wedding. He calls himself a salvager of important records.
Minagho pays her six coppers, in Mina's face, and sits in the front row.
His first reading is a real order. His second starts real and ends in a sentence no general ever wrote, all regret and heavy breathing. Then he reads out the living buyer's name, slowly, so the room can taste it.
Minagho leans in to your ear.{/n}
"He's mistaken a ration mark for a price. And he's made me sorry again. Twice now. I'm counting."
{n}One listener begins copying the buyer's name. The reader unlocks the box and lifts out an original order, holding it well away from the candle and well away from anyone who might know the ink.
Beside it lies a packet tied with faded cord. Minagho's fingers stop moving on your sleeve.{/n}
"That one was sealed when I sent it. He has more than a handbill, darling. He has my post."
{n}The reader asks whether anyone would care to pay extra for a closer look.{/n}''',
     (0, '[Compare the order with the copied page before he can hide it. Knowledge: World, DC 31.]'),
     (1, '"Buy him a closer look, Minagho. Make him keep the original on the table."'),
     (2, '"She knows this hand better than any of us. Let her ask the questions."'))

text(S, "proof", '''{n}The altered sum is not his only mistake. The date belongs to a week before the buyer held the office written under his name. You ask the reader, in front of his six customers, which record supplied that title.
He starts to explain the difficulties of wartime copies. Minagho interrupts him with the correct abbreviation, what it meant, and the name of the clerk whose hand he has been trying to imitate. The clerk is dead. She tells the room how.
The listener with the notebook stops writing. The forger reaches for the sheet. Minagho puts her hand flat on it.{/n}
"This part happened," {n}she says, and taps the real line.{/n} "That part, where I'm sorry? You made that up. I'd like it back."
{n}The room has gone very still. The reader looks from her to the woodcut and back. Recognition comes over him like a sickness, from the feet up.
He does not scream. He packs up his box with shaking hands, refunds the room, and goes out by the back door, fast.
Minagho listens to the door swing.{/n}
"He's going home, darling. Down a dark lane, alone, with my post under his arm." {n}She turns her blank, beautiful face to you.{/n} "Well?"''',
     (0, '[Let him crawl home.]'),
     (1, '[Follow him out.]'))

text(S, "price", '''{n}The reader names a price high enough to make the other listeners look up. You can't prove the forgery fast enough to keep the original on the table without paying for the time.
Minagho opens her purse and counts the coins out one by one onto his table, slowly, making him watch every one.{/n}
"I was going to buy gloves with this. You've become a personal disappointment."
{n}He takes the money. She lays the true order beside his copy and asks him the kind of questions only its author could ask. His answers get shorter. The room supplies a silence in which every short answer can be heard. At last he admits the buyer's name came from an unsigned note, and that he'll print a correction.
Then he packs his box and leaves by the back way, too fast, with her coins and her post.{/n}
"He took my money," {n}Minagho says, very quietly.{/n} "He drew me sorry, and he took my money, and now he's walking down a dark lane, alone." {n}She flexes the torn glove.{/n} "Darling. Please."''',
     (0, '[Let him crawl home.]'),
     (1, '[Follow him out.]'))

text(S, "question", '''"How kind of you to introduce me."
{n}Minagho lays the handbill on his table, crown up, and lets Mina's face slide off like a wet glove. The room sees her own eyeless face. Somebody's stool goes over.{/n}
"Who gave you the note about the buyer?"
"My sources are confidential."
"Then invent a braver one, sweetie. You're good at inventing."
{n}He looks at the door. She stays seated. The table between them suddenly looks very short.{/n}
"You know whose order this is. You've recognised the hand. You're wondering whether the Commander brought me here as a witness or a punishment. Keep wondering. It's good for you."
{n}He hands over the unsigned note. When she asks for the packet too, nobody in the room insists that she pay. The six listeners leave in a hurry, and the forger goes after them, out the back, without his box.{/n}
"There he goes," {n}Minagho says, tucking the packet into her sleeve.{/n} "Into the dark. Alone. With my words still in his mouth." {n}She stands.{/n} "Say the word, darling."''',
     (0, '[Let him crawl home.]'),
     (1, '[Follow him out.]'))

text(S, "alley", '''{n}He doesn't get far. Minagho has him by the collar before the end of the lane, and slams him into a wall hard enough that his teeth click, and holds him there with one hand while he paws at her wrist.
She is smiling. She has wanted this all evening.{/n}
"Six coppers," {n}she tells him, conversationally.{/n} "Six coppers for Minagho. For the woman who took Drezen. I have built a burial mound out of the tin heads of all the idiots I've killed or tricked, sweetie, and you'd have been at the very bottom of it." {n}She leans in.{/n} "And you made me sorry. In print. Say it. Say what you wrote."
{n}He can't. He's crying.{/n}
"Well, Commander?" {n}She doesn't turn round.{/n} "He's mine to break. Tell me how much."''',
     (0, '"Kill him."'),
     (1, '"His writing hand."'),
     (2, '"The gallows. Forging a general\'s orders in a crusade city hangs him."'),
     paras=(
         live('''{n}The brand on her forehead has opened. Blood runs down into the corner of her grin. She licks it, and laughs, and you can hear in the laugh that his blood won't stop it, and that she knows exactly whose would.{/n}'''),
     ))

text(S, "book", '''{n}The lane is narrow and dark, and he is still crying when you give her your answer.{/n}''',
     (0, '[Walk her home.]'),
     paras=(
         when(P + "forger_killed", '''{n}She does it with her hands. It isn't quick, because she doesn't want it to be quick, and she talks to him the whole time in Mina's sweet voice: there, sweetie, there, say sorry now. When he stops, she lets him slide down the wall and sits on her heels beside him, flushed and pleased, like a woman back from a good dance.{/n}
"That," {n}she says,{/n} "was worth six coppers."'''),
         when(P + "forger_maimed", '''{n}She takes his right hand. She does it slowly, finger by finger, then the rest, while he screams into her other palm. Then she drops what she took into the gutter and wipes her claws on his coat.{/n}
"There. Now you'll have to dictate. Find someone who spells better."'''),
         when(P + "forger_hanged", '''{n}You call the watch. They come at a run and take him in irons, papers and box and all, and a sergeant who has been at Kenabres looks at the forged orders and spits. He'll hang inside the week. The crusade does not love men who invent generals' commands.
Minagho listens to them drag him off. She doesn't say anything at all, which is worse than anything she could have said.{/n}
"You gave him a rope," {n}she says at last.{/n} "Quick. Clean. In front of a crowd. Darling, that's a gift. I'd have made him earn it."'''),
         always('''{n}Footsteps come down the lane: Chivarro, in a cloak over her house silks, with a lantern in one hand and a book in the other. She turns her face to Minagho, and to whatever is left of the evening, and reads all of it in a heartbeat.{/n}
"You went without me."
"You were busy robbing a captain."
"I'm always busy robbing a captain." {n}Chivarro holds the book out: red leather, cracked, very old.{/n} "You left this in my room. You should be more careful what you leave lying around in a city full of forgers."
{n}Minagho takes it, opens it, and laughs. It is a general's dispatch book. On the first page somebody, long ago, scratched out the general's name and wrote her own over it, in exactly the hand the forger tried to copy.{/n}
"Mine," {n}Minagho says.{/n} "That's my first forgery, darling. I was much better than him."
"You were much prettier than him," {n}Chivarro says.{/n} "Give me that glove."'''),
         when(P + "forger_killed", '''{n}They walk home with Minagho reading old dispatches aloud and Chivarro sewing the split seam of her glove by lantern light as they go, while the forger's blood dries brown on the leather.{/n}'''),
         when(P + "forger_maimed", '''{n}They walk home with Minagho reading old dispatches aloud and Chivarro sewing the split seam of her glove by lantern light as they go. There is blood on the leather. Neither of them mentions it.{/n}'''),
         when(P + "forger_hanged", '''{n}They walk home with Minagho reading old dispatches aloud, sulking between the pages, and Chivarro sewing the split seam of her glove by lantern light as they go.{/n}'''),
     ))

# ---------------------------------------------------------------------------
# the_first_small_audience (REBUILD: "Forever, if your pockets are deep enough")
# ---------------------------------------------------------------------------
S = "the_first_small_audience"
text(S, "start", '''{n}The private room is the one with the locked door. Tonight it is unlocked: a low vault hung with dark cloth, one long couch, one table, one good lamp, and a little grilled window high in the wall through which Chivarro can listen, and read, from the counting alcove without being seen. She puts you at the grille beside her.{/n}
"Nerath," {n}she says.{/n} "Wool. He came north with the crusade with two looms and a cousin in the commissary, and now he clothes half your army and owns a house in the upper town with glass in every window. He's been down here six times. He always takes the private room. He always brings his clerk."
{n}Through the grille you watch them come in: a heavy mortal in a beautiful coat, Mendevian by his vowels, with rings on every finger; and behind him a young man in ink-stained black, carrying a satchel of papers and looking at nothing.{/n}
"Tonight," {n}Chivarro says softly,{/n} "he wants to buy something. I can hear it on him like scent. Let's find out what."''',
     (0, '[Watch.]'))

text(S, "show", '''{n}Sivane comes in to them without knocking. She has dressed for the room, which means mostly that she has undressed for it, and she walks around Nerath once, slowly, sniffing, and tells him he smells of sheep and other people's money.
He laughs, delighted. He tips her before she has done anything at all.
For an hour she works him the way Chivarro said she would: insults, a slap, her heel on his chest, every humiliation priced and paid for on the nail. The clerk stands by the door the whole time with the satchel in his arms. Nerath never sends him out. Sometimes, when Sivane says something particularly vile, Nerath looks over at the clerk to see if he heard.
When it is over Nerath sits up, flushed, buttoning his coat, and asks Sivane to fetch the mistress of the house. He has a proposal.{/n}''',
     (0, '[Watch the clerk while Nerath waits. Perception, DC 31.]'),
     (1, '"Let\'s go in and ask him what he wants."'))

text(S, "noticed", '''{n}The clerk hasn't moved in an hour. His knuckles on the satchel are white. When Sivane passed him, he flinched, and Nerath enjoyed the flinch more than anything she did to him.
There is a paper folded in the inside pocket of Nerath's coat: you saw it when he took the coat off and saw where he put it, carefully, where he could reach it. A contract. The clerk's eyes went to it every time Nerath touched the pocket.
You tell Chivarro. She is already nodding.{/n}
"Debt," {n}she says.{/n} "The boy owes him. A great deal. The kind of debt a man inherits from his father with the shop. Nerath has bought it, and he's tired of owning it." {n}She smiles, not nicely.{/n} "He's going to try to sell it to me."''',
     (0, '[Go in with her to hear the offer.]'))

text(S, "unclear", '''{n}You watch the room, but there is too much to watch: Sivane, Nerath, the coat, the satchel, the boy by the door. You couldn't swear to any of it.
Chivarro doesn't need you to. She is leaning against the wall with her head tilted, reading through the stones the way other women read through a keyhole.{/n}
"The boy's terrified," {n}she says.{/n} "And Nerath's carrying something on paper that he thinks is worth a great deal to me. He's practising how to say it." {n}She pushes off the wall.{/n} "Come on, honey. Let's let him say it."''',
     (0, '[Go in with her to hear the offer.]'))

text(S, "direct", '''"Of course you'd rather ask. You're the only guest in this house who never does what I expect."
{n}Chivarro unlocks the private room with her own key, sweeps in, and sits on the end of the couch beside a half-dressed wool merchant as if she had been invited.{/n}
"Master Nerath. Sivane says you have a proposal. The Commander wants to hear it, and I want to price it."
{n}Nerath looks at you, and recognises you, and goes pale, and then, remarkably, recovers.{/n}
"Commander. An honour. I supply your cloaks." {n}He turns to Chivarro.{/n} "It concerns my clerk."''',
     (0, '[Listen.]'))

text(S, "proposal", '''"His name is Tam. His father owed me for a loom, and died owing, and Tam inherited it. He's been working it off for six years. He'll be working it off for another twenty." {n}Nerath takes the folded paper out of his coat and lays it on the table.{/n} "I'm tired of him. He looks at me. You understand."
{n}The clerk by the door has stopped breathing.{/n}
"I'd like to give the debt to the house," {n}Nerath says.{/n} "The whole of it, and I'll pay for the privilege. He stays here. He works it off here, in whatever way you find profitable. And I come down on my evenings, and I see him here." {n}He smiles at Chivarro.{/n} "Forever, if you like. I understand that's something you offer."
{n}Chivarro picks up the paper and reads it without unfolding it, which is to say she reads Nerath.{/n}
"Any of them can be mine for a night, Master Nerath," {n}she says.{/n} "Or forever, if your pockets are deep enough. Yours are. I'll take him for three hundred, and you'll pay the first year of his keep, because he'll eat."
{n}Nerath doesn't even haggle. Chivarro hears that too, and adds fifty.
Then she turns to you, the paper between two fingers.{/n}
"Well, honey? It's my house. But you look like you've got an opinion."''',
     (0, '"It\'s her house. Let her sell."'),
     (1, '"Arrest him. Selling a man to a demon\'s house is a hanging matter in my city."'),
     (2, '[Buy the debt yourself] "I\'ll outbid him."'),
     paras=(
         when(SEELAH, '''{n}Seelah has come down the stair behind you. She steps past you into the room before you can stop her.{/n} "He's a person. You can't sell a person, not here, not under the crusade's banner. Commander, tell her."
{n}Chivarro turns her face to Seelah and reads her, top to bottom, the way she read Nerath. Then she smiles.{/n} "A paladin. Brave, poor, and lonely. You'd fetch a fortune in the right room, sweet. Don't worry. Nobody's buying today."'''),
     ))

text(S, "counter", '''{n}Chivarro doesn't look surprised. She doesn't look pleased, either. She looks as if a coin has landed on the right side.
She names a price for the boy's upkeep, another for his room, and a third for "the house's trouble". Nerath pays all three from a purse he must have filled for the purpose. She counts it in front of him, every coin, and folds the debt into her bodice.{/n}
"There. He's mine." {n}She turns to the clerk.{/n} "Tam. Sit down before you fall over. Nobody's going to hurt you tonight. Tonight."
{n}The boy sits. Nerath watches him sit with an expression you would have to be very charitable to call fond, then bows to Chivarro, bows to you, and leaves whistling.
When he's gone Chivarro calls for Sivane.{/n}
"Take Tam downstairs. Feed him. Find him a bed in the back vault and show him the price board." {n}She doesn't turn her face to you.{/n} "He'll learn."
{n}Sivane takes the boy by the arm like a parcel. At the door he looks back at you, once. Then he is gone into the house, and the locked door is locked again, and Chivarro is counting.{/n}''',
     (0, '[Let the door lock.]'))

text(S, "end", '''{n}You call the watch.
They come down the stair into Chivarro's house with halberds and a sergeant who has never been anywhere so expensive, and they take Nerath out in his shirt, with his beautiful coat over the sergeant's arm. He shouts the names of men who owe him money all the way up the stair. The clerk stands by the door, shaking, with the debt in his hands; Chivarro has given it to him, and she did not like doing it.
When the stair is quiet she turns on you. She doesn't raise her voice.{/n}
"My house, honey. You can buy in it. You can't forbid in it. You just took three hundred and fifty crowns out of my fucking strongbox and the best customer I had and you did it in my private room in front of my staff." {n}She takes a breath.{/n} "I'm going to remember this. Not tonight. I'm going to bring it up on some night when you think you're winning, and I'm going to enjoy it."
{n}Behind her Sivane mouths, at you, a word in Abyssal that you don't know and can guess.{/n}''',
     (0, '[Leave her to count what she lost.]'))

text(S, "outbid", '''"Oh, honey."
{n}Chivarro turns slowly toward you. She is delighted. She is also, very visibly, raising the price.{/n}
"Four hundred, then. You don't get a discount for wearing a crown. Commander or cook, everyone pays the same in my house." {n}She holds out her hand.{/n} "And the boy's keep while I hold him, and a fee for the trouble, because Master Nerath is about to cry and I'll have to give him something for free to stop it."
{n}You pay. Nerath does cry, a little, and gets a glass of wine on the house, and leaves in a temper. Chivarro folds the debt in half and hands it to you, not to the boy.{/n}
"There. He's yours. You can tear that up and let him go, or keep him, or sell him back to me when you're tired of him looking at you." {n}She smiles.{/n} "They all do it eventually, honey. Look. Even at you."
{n}The clerk stands by the door with his satchel, staring at the paper in your hand as if it were a knife.{/n}''',
     (0, '[Keep the paper.]'))

# ---------------------------------------------------------------------------
# when_the_door_opens (REBUILD: "Priced at the door")
# ---------------------------------------------------------------------------
S = "when_the_door_opens"
text(S, "start", '''{n}The house has been trading quietly for a month. Tonight Chivarro opens it properly: the big vault's first show, the price board lit, the door thrown wide. The word has gone round Drezen in the way such words do, in barracks and bathhouses and the back pews of chapels, and by dusk there is a queue down the burned market's broken stair and out into the square: merchants, officers in plain coats, two priests who would swear they are here to preach, a lordling from the south with his friends, a scattering of women in veils.
Chivarro stands at the bottom of the stair under the lamp, in red, with the shoulders-man at her side and the price board behind her. She isn't letting anyone in. She is letting them in one at a time.{/n}
"Evening," {n}she tells the first in line, and tilts her head.{/n} "Forty. And the girl you're thinking of is called Ilse; ask for her by the bath. Next."
{n}You feel her find you, at the back of the queue. She doesn't wave. She grins.{/n}''',
     (0, '[Join the queue while Nerath\'s party is shown down to the private room.]'),
     (1, '[Join the queue.]'),
     paras=(
         when(P + "soldiers_barred", '''{n}The board still says NO SOLDIERS, a hand high. The officers in the queue have left their uniforms at home and are paying the new prices to pretend they never owned one. Chivarro charges them extra for the pretence.{/n}'''),
     ))

text(S, "private", '''{n}Nerath comes past the queue as if it weren't there, with two friends from the wool exchange, and Chivarro lets him through without a word or a price. He's paid in advance. He's paid for something that lives in the back vault now.{/n}
"Is Tam working tonight?" {n}he asks her, at the door.{/n}
"Everyone works tonight," {n}Chivarro says.{/n} "You'll get your evening, Master Nerath. Don't ask him to do anything he hasn't been taught yet; it's bad for the merchandise."
{n}Nerath laughs and goes in. The queue shuffles forward. Ahead of you a man you half recognise from the citadel pulls his hood lower.{/n}''',
     (0, '[Wait your turn.]'))

text(S, "open", '''{n}The queue moves slowly, because Chivarro is enjoying herself. She reads every guest before she prices them, and she says what she finds out loud.{/n}
"Thirty. You want to be tied up, and the woman at home ties a terrible knot. Next."
"Sixty, for being a priest. No, I don't care which god. Next."
"You've come to look and not buy. Ten for looking. Next."
{n}A lordling from the south tries to pull rank on her and is lifted out of the queue by the shoulders-man and set down in the square, gently, the way you would move a cat. His friends pay double to get in after him.
And then there is nobody in front of you but Chivarro.{/n}''',
     (0, '[Step up to the door.]'))

text(S, "first_scene", '''"Well, well. The Commander of the Crusade, in my queue, like a cobbler."
{n}Chivarro leans in the doorway with her arms folded and turns her face up to you, and the queue behind you goes quiet so it can listen. She takes her time. You feel her in your head like fingers going through a drawer.{/n}
"What are your preferences, honey? Never mind." {n}She smiles.{/n} "I'll find out for myself."
{n}She does. She doesn't say what she finds. She lets the queue watch her find it, and lets them watch her enjoy it.{/n}
"A hundred," {n}she says.{/n} "You don't get a discount for the army. Pay, or polish, or go back up those stairs."''',
     (2, '[Pay her price.]'),
     (3, '"I\'m not paying."'),
     (4, '"I am the Commander of this city. Stand aside."'),
     (5, '[Haggle in front of the whole queue. Persuasion, DC 32.]'),
     (6, '[Close your mind to her.]'),
     (7, '[Close your mind to her.]'),
     (8, '[Keep her out of your head. Persuasion, DC 34.]'),
     (0, '[Watch Chivarro deal with Nerath.]'),
     (1, '[Watch the show.]'))

text(S, "haggle_success", '''"A hundred? For a door? Fifty, and you can tell the whole city the Commander paid to come in."
{n}Chivarro considers you for a long moment. The queue holds its breath. Then she laughs, loud and genuine, and slaps the doorframe.{/n}
"Fifty. Done. I was never going to get more than fifty out of you; I was just haggling." {n}She holds out her hand for the coin and bites it.{/n} "And now every man in this queue knows the Commander haggles. Do you know what that's worth to me, honey? More than fifty."''',
     (0, '[Go in.]'))

text(S, "haggle_failure", '''"A hundred? For a door? Fifty, and you can tell the whole city the Commander paid to come in."
{n}Chivarro's grin goes very wide.{/n}
"Oh, honey. No. You've just told the whole queue you think my door's worth fifty. That's an insult, and insults cost. Two hundred." {n}She holds out her hand.{/n} "Or I can tell them what you were thinking about just now. I'd rather have the money. You'd rather I had the money too."''',
     (0, '[Pay the two hundred.]'))

text(S, "unread", '''{n}You close your mind, and keep it closed.
Chivarro's head tilts further, and further. You feel her come against it and stop, like a hand against a locked door. The smile goes off her face, and comes back as something else.{/n}
"You have an iron will," {n}she says slowly.{/n} "I'm almost offended."
{n}She steps back from the door. Not aside. Back.{/n}
"Go in. No charge. I want to know what's behind that, honey, and I'm going to find out, and it's going to cost you a great deal more than a hundred." {n}She turns to the queue.{/n} "Next! And the rest of you can stop gawping. You're all much easier."''',
     (0, '[Go in.]'))

text(S, "read", '''{n}You try. You might as well have tried to keep the tide out with a door.
Chivarro finds it. She finds all of it, and then she leans forward, and she tells the queue: not everything, only one thing, the one you would most like nobody in Drezen to know about you. She says it sweetly. She says it loud enough for the back of the line.
Somebody laughs. Then everybody does.{/n}
"There," {n}Chivarro says.{/n} "That was worth more than a hundred. Go in, honey. Tonight's on the house."''',
     (0, '[Go in, with your face burning.]'))

text(S, "door_callback", '''{n}Then you are past her, and down the stair, and into the noise and heat of her house on its first night.{/n}''',
     (0, '[Find the private room.]'),
     (1, '[Find the big vault.]'),
     paras=(
         when(P + "door_paid", '''{n}You paid. She counted it in front of the queue, then bit the last coin, as if your money might be forged.{/n} "There. The Commander pays like a cobbler. Isn't that nice?"'''),
         when(P + "door_polished", '''{n}You didn't pay. She smiled, as if you had done something lovely, and the shoulders-man handed you a bucket and a brush.
"I want that floor so clean I could eat a demon off it," Chivarro said, and the queue watched the Commander of the Crusade kneel on the bottom step and scrub her entrance, every flag of it, while she went on pricing the guests over your head. When you had finished she inspected it on her knees, sniffed it, and let you in. "Nearly. Come back tomorrow and I'll show you where you missed."{/n}'''),
         when(P + "door_barred", '''{n}You pulled rank. Chivarro's smile went out like a lamp.{/n}
"Don't you dare threaten me. This is my domain. I alone have the right to make threats here."
{n}Her bouncers stood up behind her. You walked in anyway, between them, and nobody in the house dared stop the Commander. But she followed you as far as the foot of the stair to her own room and said, for the whole vault to hear, that the Commander was welcome to everything in the house except upstairs. Tonight, upstairs is barred.{/n}'''),
         when(P + "clerk_sold", '''{n}Through the arch to the back vault you glimpse Nerath's clerk, Tam, scrubbed and dressed in house silk, carrying a tray. He doesn't look at anyone. Nerath, at the private room door, watches him go by with his tongue in his cheek.{/n}'''),
         when(P + "clerk_bought", '''{n}Nerath isn't here. He has taken his custom across the river to a cheaper house, Chivarro says, and good riddance; but she says it while she is pricing you for the clerk, whose debt you still have folded in your coat.{/n}'''),
         when(P + "nerath_arrested", '''{n}Nerath isn't here. He is in the citadel cells, and there is a gap at the front of the private room where he would have sat, and Chivarro has charged three other men for the privilege of filling it.{/n}'''),
     ))

text(S, "patron", '''{n}The private room is full tonight, and Nerath is in the best place. Sivane works the room from his lap outward: she tells each man what he is and what he smells like, and slaps one, and spits in another's wine and charges him for a fresh cup.
Then a young lordling at the end of the couch reaches for her when he hasn't paid to, and she bites him. Not playfully. She bites his hand to the bone and holds on, growling, while he shrieks, until Chivarro comes in and taps her on the shoulder.
Sivane lets go. She licks her lips. The room applauds.{/n}
"Add it to his bill," {n}Chivarro says.{/n} "And the floor."''',
     (0, '[Stay for the rest of the night.]'))

text(S, "heckler", '''{n}The big vault is packed to the walls. Sivane comes out onto the low platform at midnight in a cloak and nothing else, and walks along the front bench, and picks her man: a fat chandler with a loud voice who has been telling his friends all night what he'll do to her.
She does it to him instead. She takes him apart in front of the whole house: his breath, his wife, his prick, his business, all of it, while he goes red and then white and then, finally, gets on his knees on the platform because she tells him to. The house screams with laughter.
When he tries to grab her she bites his ear half off. The laughter doesn't stop. It gets louder.{/n}
"There," {n}Chivarro says beside you, delighted, watching the coins land on the platform.{/n} "That's a show."''',
     (0, '[Watch it end.]'))

text(S, "ending", '''{n}By the small hours the house is a wreck of overturned cups, spent lamps and men who have been parted from their money and are grateful for it. Sivane is asleep on the platform in her cloak with a purse under her head. The shoulders-man is putting the last of the drunks out into the square.
Chivarro walks the empty vaults with a candle and a ledger, adding as she goes.{/n}''',
     (0, '[Watch the house close.]'),
     (1, '[Watch the house close.]'),
     (2, '[Find her at the bottom of the stair.]'))

text(S, "winter", '''{n}Sivane picks the last man of the night out of the crowd and takes him through the curtain, and the house hears him begging until dawn. When he comes out he gives her his purse, his rings and his boots. Chivarro charges him for the boots.{/n}''',
     (0, '[Find her at the bottom of the stair.]'))

text(S, "host", '''{n}Sivane picks the last man of the night out of the crowd, looks him over, and throws him back. The house roars. He goes away up the stair without his dignity or his money, and the next night he is back in the queue.{/n}''',
     (0, '[Find her at the bottom of the stair.]'))

text(S, "after", '''{n}She sits on the bottom step of her own stair, her red skirts in the dust, and shakes the takings out onto her lap and counts them twice.{/n}
"Four hundred and eleven. Two bites, one broken nose, a priest who wept, and a lordling from Taldor who wants to marry Sivane." {n}She laughs.{/n} "The house is properly open, honey. Do you know how long I've waited to say that in a city that isn't burning?"
{n}She ties the purse shut and stands, and puts her hand flat on your chest, the way she prices a guest at the door.{/n}''',
     (0, '[Go up with her.]'),
     (1, '[You\'re barred from upstairs. Go home.]'),
     paras=(
         p('''"Come upstairs. I want to spread this on the bed and roll in it, and I want a witness."''', forbids=(P + "door_barred",)),
         when(P + "door_barred", '''"Not you, though. You're barred, remember? Go home, Commander. Sleep in your big cold bed and think about who makes the threats in this house."'''),
     ))

# ---------------------------------------------------------------------------
# after_the_last_lamp (RE-VOICE; hosts a slot)
# ---------------------------------------------------------------------------
S = "after_the_last_lamp"
text(S, "start", '''{n}The night after opening night. The house below is shut for once, and the loft above it is dark except for the red lamp. Chivarro opens the trapdoor herself, in a dressing robe, with her hair coming down and the takings ledger under her arm. She is tired. She looks it, and doesn't bother to hide it from you.{/n}''',
     (0, '"You asked me up. I came."'),
     (1, '"Am I still barred?"'),
     (2, '"I came to see what the house made."'),
     paras=(
         when(P + "door_barred", '''{n}She doesn't move out of the way.{/n}
"You. You pulled rank at my door, in front of my queue, and walked into my house over my bouncers like it was a captured town." {n}She weighs you up for a long moment. Then she steps aside.{/n} "Come up, then. I'm letting you. Understand that. Nobody makes me open this door. I chose this one."'''),
         when(P + "door_polished", '''{n}She is grinning before you're halfway up the ladder.{/n} "The Commander of the Crusade on their knees on my step with a scrubbing brush. Half Drezen saw it. The other half will have heard by noon. Honey, I could kiss you. I'm going to."'''),
         when(P + "door_unread", '''{n}She stops you on the top rung with a finger on your forehead, pressing, as if she might find a seam.{/n} "Still locked. Damn you. Come in. I'll have it open by morning."'''),
     ))

text(S, "promised", '''"You came. Good. I've had a whole house telling me how wonderful I am, and I want someone who'll say it properly."
{n}Chivarro takes your cloak and drops it on the floor and kicks the trapdoor shut.{/n}
"Some of them paid to be impressed. Some of them paid to prove they couldn't be. I charged both. Sit. I've kept the good wine up here, where Sivane can't steal it."''',
     (0, '"Then let\'s drink it."'))

text(S, "open", '''"No. Not tonight. Tomorrow you're barred again, and the night after, until I decide otherwise. Tonight's a gift." {n}She pulls you up the last rung by your collar.{/n} "Don't make me regret it, honey. I regret things in very expensive ways."
{n}She leaves the ledger shut on the chest and pours two cups, and sits, and doesn't make room. You have to move her feet.{/n}''',
     (0, '"I won\'t talk business."'))

text(S, "rest", '''{n}Chivarro drinks, and stretches, and lets the robe fall open at the throat. No glamour up here: only her own eyeless face, turned toward you in the red light.{/n}
"One guest last night asked me how I could see his purse. I told him I could hear how tightly he held it. He spent the rest of the night trying to walk without making a sound, and he still paid double." {n}She laughs.{/n} "Mortals. Stupid, horny bastards, every one. I love them. I love what they leave on the table."
{n}She puts her cup in your hand.{/n}
"Stay. I've had a whole house wanting things from me. I want an hour with somebody who wants the right thing."''',
     (0, '[Hold out your hand.]'),
     (1, '"Sleep. I\'ll stay, and I won\'t say a word."'),
     (2, '"If you could empty the whole house tonight, who would you leave in it?"'),
     paras=(
         when(P + "names_sold", '''{n}Under the ledger, you notice, is a second purse. Fatter. She hears you notice it.{/n} "The horned man's money, honey. I'm keeping it for the next house. Don't make that face. You know exactly what I did with the names."'''),
     ))

text(S, "affection", '''"Closer."
{n}She takes your hand and pulls you down beside her.{/n}
"You cost me a customer last night, honey. You did something stupid at the back of the vault and I laughed, and he thought it was at him. He left without paying for his second bottle." {n}Her mouth brushes yours, then stays. She breaks the kiss with her fingers still twisted in your collar.{/n} "There. That's the first thing tonight worth climbing a ladder for."''',
     (0, '"Then let tonight be quiet, and close."'),
     (1, '"I\'m staying the night."'))

text(S, "held", '''{n}You stay together on the couch. Chivarro tells you which of last night's guests will be back, and which will never come, and which will come back pretending they never came. She is never wrong. She can name your footsteps on the ladder, she says, and when you dispute it she imitates them, badly, and kisses you before you can complain.
The ledger stays shut. At the trapdoor, much later, she tells you to remember this hour when you're out killing demons, because she intends to send a bill for it.{/n}''',
     (0, '[Keep the quiet hour.]'))

text(S, "night", '''"Take that pin out before it puts a hole in one of us."
{n}She turns her shoulder to you. The pin at her robe resists; she guides your fingers to the catch and lets you finish. The robe slides off one shoulder as she takes your mouth.{/n}
"There. I knew I kept you for something."''',
     (0, '[Go with her behind the curtain.]'),
     paras=(
         when(P + "door_paid", '''{n}She goes to the chest first and comes back with a little cloth bag, and empties it onto the pillow: a hundred, in your own coin, the same coins you paid at the door. She can tell them apart.{/n}
"Yours. I don't get paid twice by the same fool. The door was business. This isn't."'''),
         when(P + "door_haggled", '''{n}She goes to the chest first and comes back with a little cloth bag, and tips your door money onto the pillow, every coin you haggled over.{/n}
"Take it back. The door was business, honey. Up here I don't sell. Up here I choose."'''),
     ))

text(S, "quiet", '''{n}Chivarro settles at one end of the couch and you at the other. Below, the shoulders-man is snoring in the doorway. She opens her mouth to say something, shuts it, laughs at herself, and pulls the blanket over her feet.{/n}
"Stay there. I like knowing somebody's minding the door who doesn't want paying for it."''',
     (0, '[Let her sleep.]'))

text(S, "empty", '''"Empty? My house?" {n}She thinks about it seriously, which is the worst of it.{/n} "Out go the drunks and the priests and the captain who cries. Out goes Sivane, after she's paid her fines. I'd keep the bouncer; he's restful." {n}She finishes her wine.{/n} "And Minagho, of course, sulking in the best room, complaining about the noise she isn't hearing. And you, I suppose, if you paid."
"And if I didn't?"
"Then you'd be polishing the floor, honey, and I'd keep you anyway."
{n}You build her imaginary empty house between you until it has a terrible staircase and a room nobody's allowed in and a door that Minagho would kick down out of spite before discovering she liked what was behind it. Chivarro sees you down the ladder still laughing.{/n}''',
     (0, '[Leave the empty house to her.]'))

SLOT_TEXT[(S, P + S + ".explicit.1")] = ("chivarro", '''{n}Near dawn a cart rattles across the market square overhead. Chivarro lifts her head from your chest as if considering having it arrested, then drops it again and hooks her arm over you.{/n}
"If you're leaving, lie well. I want another hour before I believe it."''')

# ---------------------------------------------------------------------------
# what_she_will_take (RE-VOICE)
# ---------------------------------------------------------------------------
S = "what_she_will_take"
text(S, "start", '''{n}Chivarro is packing. Not the house: the house stays, with its lease and its bouncer and its debts. She is packing the things that are hers, into one hard leather case on the loft floor: the red lamp wrapped in a shawl, the locked chest's contents, three knives, a ledger.
She isn't leaving yet. Packing is how she finds out what the next place will need to hold.{/n}
"Another season here," {n}she says.{/n} "Maybe two. Then I decide whether to keep squeezing this city, or take the business somewhere that hasn't heard of me yet and charge them for the surprise."
"Have you chosen?"
"Not a city. I want to see what a place will pay before I decide to conquer it. Every empty seat is still an insult, honey; I've merely learned to invoice it."
{n}She closes the case and tests the latch.{/n}
"I'm deciding what I take. Some of it doesn't fold."''',
     (0, '"Tell me what you\'re taking."'),
     paras=(
         when(P + "names_sold", '''{n}The fattest thing in the case is a purse. You know where most of it came from: six names.{/n} "Don't make that face. The takings come with me. They always come with me."'''),
     ))

text(S, "keep", '''"The work. Minagho, if she can go a week without telling everybody how much better she'd have run it. And you."
{n}She lifts the red lamp back out of the case and finds that the lid won't close over it; something underneath has shifted.{/n}
"There's my list. Help me shut this before I pack you in it."
{n}Under the lamp you find a folded handbill: the notice for the house's first show, with Sivane's price scrawled across it in Sivane's own hand, doubled. Chivarro smooths it flat with her thumb.{/n}
"I want you at the next one. Somewhere I'm still pleased to see you when the lamps are out and the money's counted."
{n}She tucks the bill into a side pocket and moves the case off the couch.{/n}
"So. What am I keeping this place for?"''',
     (0, '"Keep it for me. Wherever you go, I come back to it."'),
     (1, '"Keep it for visits. No house, no promises. The nights I can get."'),
     (2, '"Keep it for a friend. I won\'t leave you a promise I don\'t mean."'))

text(S, "lasting", '''{n}Chivarro goes very still.{/n}
"Yes."
{n}She shoves the case off the couch with her foot. It falls over. She doesn't look at it.{/n}
"I had something much more impressive prepared. You've ruined it. I'm going to charge you for the speech."
"Do you want time to remember it?"
"No. Come here before I do."
{n}Her hand closes over yours. She is smiling and furious about it.{/n}
"You realise I'll write you the most dreadful complaints about every room I stay in? I'll expect answers. Preferably ones where your rooms sound worse."
"And if I can't come?"
"Then tell me where to send the next complaint, honey. I'm resourceful."''',
     (0, '"Then come here."'),
     (1, '"And when I have to leave?"'))

text(S, "lasting_close", '''{n}You kiss her before the next joke is ready. Chivarro catches your sleeve and keeps you there after the kiss is over.
Afterward she rights the case and puts a blank sheet into the side pocket with the handbill.{/n}
"For the first address. If I put it anywhere else, I'll decide it's business and write to you like a customer."
{n}You ask how she writes to customers she especially likes. She shows you: a sweet, proper face whose promise becomes perfectly filthy halfway through. Then she ruins it by laughing.
You stay while she repacks. This time she leaves the lid open and puts her feet up on the case, where you have room to sit close.{/n}''',
     (0, '[Keep her, and let her keep her road.]'))

text(S, "distance", '''"Your first road will be worse than mine. I've been trying not to count the ways. I'm very good at counting."
{n}She opens the side pocket and slips a blank sheet in beside the handbill.{/n}
"An address, when I have one. You'll get it before you get a description of the room. I know myself."
"What do you want sent back?"
"Your own hand. Not a secretary's. Not a clerk's. If I get one line in somebody else's writing, I'll sell it. And the couriers are on you, honey. I'll send the bill with the address."
{n}She turns your hand over in hers, as if checking it for rings.{/n}
"And when you come, come early enough to find me awake. I've spent whole evenings planning a magnificent welcome and then fallen asleep over the takings. I'd hate to waste an entrance on that."
"I could wake you."
"You could try, honey. I'm told I'm difficult."''',
     (0, '[Promise the letters, in your own hand.]'))

text(S, "visits", '''"Then I'll have to make the invitations interesting."
{n}She weighs you up the way she weighs a guest on the stair.{/n}
"Sivane wants a new act: a judge from the upper town who pays to be sentenced by a succubus. I'd like you in the gallery when she passes sentence. You'll enjoy it. He won't. He'll pay double."
"Do I get a part?"
"If you're frightened of being picked, I'll seat you out of biting distance."
{n}She moves the case off the couch.{/n}
"That's for later. Today I've got an hour, a room I like, and no succubus banging on the trapdoor. Stay."''',
     (0, '[Stay close.]'),
     (1, '[Stay and talk.]'))

text(S, "visits_close", '''{n}Chivarro settles under your arm and tells you about a coast where the stones go green in the shallows. She wants to see it before some merchant describes it well enough to ruin it.
You ask who told her about it. She admits, with bad grace, that it was a customer she always claimed bored her stiff.{/n}
"He talked for an hour. I can't remember his name."
"You remember the stones."
"Yes. I'm furious with him. I should have charged him for the hour."
{n}She kisses you, and then describes the little boat she'd refuse to get into and the view she'd insist on having from it, until you're both laughing at a journey neither of you will ever take.{/n}''',
     (0, '[Keep the visits.]'))

text(S, "visits_talk", '''{n}You stay while Chivarro wraps her few precious things. Each has a story, and she chooses which to tell. Some stay short. Some grow an unexpected detail when you ask why she kept the thing at all.
One plain pin came from no admirer. She bought it because the seller said it was too severe for her. She shows you the face she wore while paying, which knocked a third off the price, and you accuse her of having practised it for a hundred years. She denies it badly enough to make you both laugh.
When you leave, the case is packed and the house below is opening for the evening, and she stands at the trapdoor looking pleased with both.{/n}''',
     (0, '[Keep the visits, and the stories.]'))

text(S, "friends", '''{n}Chivarro hears the whole answer before she says anything.{/n}
"Then friendship. I'll have to invite you up to talk and cheat you at dice instead."
{n}She pauses.{/n}
"I'm a little disappointed. I'll decide exactly how much after you've gone, and I won't do it where you can hear."
{n}The smile takes the worst edge off it.{/n}
"You'll still hear what becomes of the house, whether you like it or not. I want your opinion when it's useful and your company when it isn't. If I send for you, come. I'm a demon, not a debt collector. Mostly."
{n}She shows you the one thing she has decided not to take: an ornament from the Delights, expensive, awkward, tied to a night she no longer enjoys telling. She has already found a buyer. Selling it seems to please her far more than keeping it ever did.{/n}''',
     (0, '[Keep her friendship.]'))

# ---------------------------------------------------------------------------
# Endings (RE-VOICE: grief becomes a hunt). Text only; paragraphs and exits stay.
# ---------------------------------------------------------------------------
ENDINGS = {
    "ending_minagho_lost": '''{n}When Minagho died, Chivarro did not weep where anyone could see it. She asked who had been there, who had done it, and who had been paid, and she read the answers out of the heads of the people who gave them, and she kept a list.
Then she sold the house. All of it: the lease, the debts, the furniture and the custom, to the highest bidder, in one afternoon, without haggling. She used the money to buy the killer's name. Then she bought the killer. Any of them can be yours for a night, she told the one she bought; or forever, if your pockets are deep enough. Hers were. Nobody ever saw that one again, and some nights, for years afterward, Chivarro went down to a cellar no one else had a key to, and came back up smiling. The Commander could share the news. The rest was hers.{/n}''',
    "ending_chivarro_lost": '''{n}When Minagho heard that Chivarro was dead, she became very calm, and very precise. She wanted names, places, and the price someone had been paid. She got them. Then she did what she had always done when an enemy was beyond her: she hired the best killer she could afford, and paid him in advance, and went to watch.
She sat close enough to see it done. She clapped. Whatever Baphomet's mark still asked of her, it had blood that night, and she let it run down her face and did not wipe it away. Afterward she kept Chivarro's last letter under her pillow, with all its insults, and corrected anyone who misquoted them.{/n}''',
    "ending_changed": '''{n}Chivarro read what the Commander had become the first time they met again, before a word was spoken, and laughed without any pleasure in it.
"I told you so, honey. I told you at the start. A larva. The cocoon of a beast that some plane is going to come and claim." She said it to Minagho afterward, too, at greater length and with more obscenity.
Minagho only wanted to know whether the thing could be used, and for how long, and at what price. They argued about that for a whole night. In the morning they locked the door, and kept it locked, and sent the Commander's letters back unopened, priced.{/n}''',
}


def _pages(payload):
    return {s["Id"][len(P):]: s for s in payload["Scenes"] if s["Id"].startswith(P)}


def _node(pages, sid, nid):
    matches = [n for n in pages[sid]["Nodes"] if n["Id"] == nid]
    if len(matches) != 1:
        raise KeyError("minachiv voice: %s/%s matched %d nodes" % (sid, nid, len(matches)))
    return matches[0]


def _slot_default(directory, slot_id):
    brief = json.loads((SLOTS / directory / (slot_id + ".json")).read_text(encoding="utf-8"))
    if brief["slot_id"] != slot_id:
        raise ValueError("minachiv voice: brief/slot mismatch " + slot_id)
    return brief["default_text"]


def integrate(payload):
    pages = _pages(payload)
    for sid, title in TITLES.items():
        page = pages[sid]
        if page.get("Entry") == page["Title"]:
            page["Entry"] = title
        page["Title"] = title
    for (sid, nid), body in NODES.items():
        _node(pages, sid, nid)["Text"] = body.strip()
    for (sid, nid, index), body in CHOICES.items():
        choices = _node(pages, sid, nid)["Choices"]
        if index >= len(choices):
            raise IndexError("minachiv voice: %s/%s has no answer %d" % (sid, nid, index))
        choices[index]["Text"] = body.strip()
    for (sid, nid), paras in PARAS.items():
        node = _node(pages, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + paras
    for (sid, nid), (directory, aftermath) in SLOT_TEXT.items():
        body = _slot_default(directory, nid)
        _node(pages, sid, nid)["Text"] = body + ("\n" + aftermath.strip() if aftermath else "")
    for sid, body in ENDINGS.items():
        for twin in (sid, sid + "_completed"):
            _node(pages, twin, "end")["Text"] = body.strip()
    for sid, page in pages.items():
        for node in page["Nodes"]:
            texts = [node["Text"]] + [a["Text"] for a in node["Choices"]] + [
                para["Text"] for para in node.get("Paragraphs", [])]
            if any(PENDING in t for t in texts):
                raise ValueError("minachiv voice: prose still pending at %s/%s" % (sid, node["Id"]))
