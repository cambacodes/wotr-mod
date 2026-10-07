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
text(S, "start", '''{n}You reach the shuttered gaming house at the appointed hour. The door opens onto a room Minagho has chosen because nobody in the street can see into it.{/n}''')

text(S, "native_meeting", '''{n}A folded note reaches you in Drezen, addressed in a name she wears better without its human face: Mina. Inside, Minagho has drawn a little skull beside an hour and an address in the burned quarter. Below it, in a smaller and much nastier hand, someone has added: "If this is her idea of a reassuring invitation, bring a knife."
The address is a room above a shuttered gaming house. You find Minagho there after dusk, in the blonde woman's shape she wears for your city. She lets it fall the moment the door is barred. The room has no window on the street. She chose it for that.{/n}
"She insisted on reading what I wrote. Then she insisted on making it worse. I nearly wept from nostalgia."
{n}She taps the second hand on the note.{/n} "She has answered, darling. She is coming by her own road, with a great deal more caution than my little skull suggests."
"I rented this for a few meetings. Do not infer that I have settled down and started collecting respectable neighbours. One of them tried to sell me a history of the siege. He had me sobbing over Staunton. I made Staunton sob. It is not the same thing."''',
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

text(S, "document", '''{n}Veyr's letter is short and courteous, which is the worst thing about it. It names the six as "the lady's remaining customers", offers Chivarro a share in a private gathering where they will be introduced to "new friends", and closes with a sentence about the underwriter's client so carefully worded it might as well have teeth.
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
Minagho, beside you in Mina's face, watches him come closer, and closer.{/n}
"There he is," {n}she murmurs.{/n} "Bought and paid for with her names. Darling, I could kiss Veyr. I won't. But I could."
{n}When the agent reaches the back stair, Minagho is already through the door ahead of him. Chivarro takes your arm.{/n}
"The counting room," {n}she says.{/n} "Down the lane. She'll want an audience."''',
     (0, '[Follow them to the counting room.]'))

text(S, "business_end", COUNTING_ROOM + ''' The agent comes down the lane alone, thinking he is following a blonde girl to a cheap bed. He finds Minagho waiting with her own face on and the inner door at her back.
She shuts it behind him.{/n}
"I want you looking at me when you realize."
{n}He realizes. You watch it happen: the little horned man understanding all at once that the rumour he was paid to price is standing a foot away, smiling, and that she has been hunted by far better than him.
Minagho takes the coded list from his coat while he is still deciding whether to scream. She reads it by the light from the door, and starts to laugh.{/n}
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
{n}Then she turns back to the agent, and remembers she has one of those, too.{/n}
"Well, Commander? He came for my bed. What does he leave this room with?"''',
     (0, '"His life. He goes home to his mistress with your warning."'),
     (1, '"His list stays here. Then he can go."'),
     (2, '"He\'s yours."'),
     (3, '"The Inquisition gets him."'),
     paras=(
         live('''{n}The brand has opened. Blood runs from the mark on Minagho's forehead, down her eyeless face, into the corner of her mouth. She licks it away and leans close to the agent.{/n}
"Do you know what this is, sweetie? Baphomet's love-letter. It hurts all the time, and it will go on hurting until I spill the blood of the one who made me fail at Kenabres. Yours won't do. Yours is cheap." {n}She lifts her chin toward you, over his shoulder.{/n} "That one's would. That one is standing right behind you. Isn't it funny, the company I keep?"'''),
         healed('''{n}Minagho touches her forehead where the brand used to bleed, as if she misses having something to blame for her temper.{/n} "Pity. In the old days I could have told you this was Baphomet's fault. Now it's only me."'''),
         when(SEELAH, '''{n}Seelah has stopped in the doorway and will not come further in. Her hand is on her sword, and her attention is on you.{/n}'''),
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
         when(SEELAH, '''{n}Seelah tried to stop it. You told her to stand down, and she did, and she watched, and she has not said a word since. She isn't looking at the body. She is looking at you.{/n}'''),
     ))

text(S, "agent_handed_over", '''{n}You send for the watch. Two of your soldiers and a grey-faced inquisitor come down the lane at a run and take the agent in irons, list and gloves and all. The inquisitor thanks you. The crusade will be grateful; men like this are threads, and threads lead to rooms.
Minagho stands very still while they take him. She doesn't argue. She doesn't raise her voice. When the soldiers are gone she turns her face toward you, and for a moment there is no Mina anywhere in it.{/n}
"You took him off my plate, darling. Off my plate, in front of me, and handed him to your priests."
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
{n}She says it in the counting room, with the agent in the third chair and Minagho holding his coded list up to the light from the door. The six names are in Chivarro's hand. Her little marks are beside them.{/n}
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
"Well? Which of you was it? Which of you made me fail at Kenabres? Come here, sweetie. I'd love to bleed you."'''),
         healed('''{n}Then the glamour gutters and goes out. Under it there is no wound: only her own eyeless face, clean, grinning. She spreads her arms so they can all get a good look.{/n}
"See? Not a drop. Doesn't that make you sick?"'''),
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
{n}It isn't true, or not all of it. You know why she stays; it lives upstairs and is called Chivarro. But she would rather die in this street than say so to them.{/n}''',
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
It doesn't take long. Minagho fights, and she is still a demon, and two of them go down screaming. But there are thirty of them, with Kenabres in them, and Baphomet took her powers when he branded her. They get her down in the mud by the well. You hear the cudgels. You hear her laughing the whole time, through blood.
The watch breaks it up at last. When the street is empty she gets up on her own. She won't let anyone help her. She walks past you without stopping and says it very quietly, so only you can hear.{/n}
"You let them."
{n}Nothing else. She doesn't need anything else. You can tell she is putting it somewhere she will be able to find it again.{/n}''',
     (0, '[Follow her back to the stair.]'))

text(S, "street_after", '''{n}Later there is only the stair, the broken gutter, and rain beginning to tick on the cobbles where the crowd stood. Minagho sits on the third step in her own face, no glamour, the chipped cup between her palms. Somebody trod the beer into the street; she has refilled the cup from a bottle she stole from somewhere, and she drinks it as if it had insulted her.{/n}
"Chivarro is upstairs pricing the windows, in case they get broken. She heard the whole thing and didn't come down. That's how I know she loves me. She trusted me to enjoy it."''',
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
{n}She leans in. Her breath smells of cheap beer and blood. When you turn your head she is already there, and the kiss isn't gentle: she bites, and keeps biting, and laughs into your mouth when you flinch.
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
{n}Chivarro opens the upper door and comes down three steps with a lamp in one hand and her account book in the other. Minagho lays out the theory as if it concerned the siege of Drezen. Chivarro sits on the landing to hear the evidence, and charges you for the lamp oil.{/n}''')

