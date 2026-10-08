"""Minagho and Chivarro: cloud voice-owner pass (villain-route-minachiv, design-first).

Applied after minachiv_voice (minagho_chivarro_trickster.integrate). Text and
flag-gated paragraphs only: no scene, node or choice id, choice position, Next,
Set, gate or gameplay field changes. Review and truth table:
tools/route_packs/redesign/minachiv/cloud-review.md.

Structure fixed here (read-only consumers of flags the route already sets):
  * paid grudges: agent_handed_over, street_abandoned, nerath_arrested,
    soldiers_barred, officer_names_bought, clerk_sold/clerk_bought, agent_killed,
    forger_hanged were promised a reckoning in their own scenes and had no later
    reader; before_the_last_road and the living endings now read them;
  * minaghos_unfinished_sentence: the after-street lines no longer assume the
    Commander protected her (street_abandoned / survivor_maimed read);
  * before_the_last_road: the commitment stance nodes are spoken in the room,
    not exchanged as letters, and the Minagho-secret discovery is made by
    Chivarro (the wronged woman), not by Minagho reading her own receipt;
  * stale references to the retired performance chain (the brass key, "this
    performance") are removed from the endings.

Canon used (enGB): fe0c87ea, 537c1e5e, 9fb4396d, a0f6a9d3, 64bbf322, c294b4ae
(Minagho); c151ae0f, 3a0074c4, 66f981f6, 165441c8, bb860eb1, d1bfd4e0 (Chivarro).
Authored, no canon claim: as in minachiv_voice.
"""
from story_format import p

P = "minachiv."
PENDING = "[PROSE PENDING:"

NODES = {}
PARAS = {}


def text(scene, node, body, paras=()):
    NODES[(scene, node)] = body
    if paras:
        PARAS[(scene, node)] = list(paras)


def add(scene, node, *paras):
    PARAS.setdefault((scene, node), []).extend(paras)


def when(flag, body, forbids=()):
    return p(body, requires=(flag,), forbids=forbids)


# ---------------------------------------------------------------------------
# her_own_arrival: Chivarro's first evening, at her native register.
# ---------------------------------------------------------------------------
S = "her_own_arrival"
text(S, "account", '''"Yes. Intermediaries get ambitious the moment they smell that you need them. I used to encourage it. Then I made them fight for the privilege, and charged the winner."
{n}She sits without waiting to be offered a chair, and takes the better cup.{/n}
"I came to talk, Commander. If you came to collect gratitude, the beggars are on the cathedral steps."
"I've had offers." {n}She taps the folded letter.{/n} "Veyr's is the first one worth reading twice. He places rich guests in private houses that want their money without letting them in by the front door. Introductions, entertainments, information. He sells discretion and sometimes remembers to supply it. I knew his customers before he could spell their names."
{n}She turns her face toward Minagho, who has finally dragged the chest away from the second exit.{/n}
"I want a business whose keys I hold. I walked out of my own house once. I'm not walking into some fat factor's to stand at his table while he decides whether I've been forgiven enough to be useful."''')

text(S, "place", '''"That's partly what I came to find out. She talks about you like an infection she's started to enjoy."
{n}Minagho reaches across and turns Chivarro's cup so its chipped edge faces away from her mouth. Chivarro lets her, though she must have read the chip before she sat down.{/n}
"Sit, honey. I've had her version of you. Now I'm taking mine out of your head, and then I'm making her pay for every omission."
{n}She tilts her head. You feel it: fingers going through a drawer, unhurried, pleased with what they find.{/n}
"Oh. She left out a great deal."
{n}Minagho grins. Chivarro keeps her hand flat over the folded offer.{/n}''')

text(S, "company", '''"Company. How cheap of you. I'll still charge for it."
{n}Chivarro pours the wine; Minagho shoves the folded offer under an empty plate.{/n}
"She calls the tavern beer an insult to the Abyss," {n}Chivarro says.{/n} "She keeps drinking it. I've watched her do that with worse things, in worse beds."
"Mind your mouth," {n}Minagho says.{/n}
"You used to like my mouth."
{n}Minagho steals her cup. Chivarro lets her have one swallow, then takes it back and bites her lip for the theft.{/n} "There. No factor, no buyer, and a perfectly serviceable threat. We may yet enjoy the evening."''')

# ---------------------------------------------------------------------------
# the_unhired_evening: the mask game keeps its props (stones, the plum) for the
# endings and slot briefs; the forfeit becomes a secret Chivarro takes by force.
# ---------------------------------------------------------------------------
S = "the_unhired_evening"
text(S, "start", '''{n}Chivarro has put the correspondence out of reach. On the table is a shallow tray of carved stones, each painted with part of a mask. Minagho says it is a game of deception. Chivarro says it is a game of finding out who at the table is lying, which takes her no time at all, and then of making them pay for it.
The forfeit is a secret. The winner does not ask for it. Chivarro simply takes it out of the loser's head and says it to the table.
You learn the rules by losing a round. Minagho shows you the true stone with such elaborate deceit that you choose another. Chivarro tilts her head at you, smiles, and tells the room exactly what you thought the first time you saw Minagho's real face. Minagho laughs so hard she has to hold on to the table. Then Chivarro takes the prize from between you, a sugared plum she brought for precisely this purpose, and eats half of it slowly, in front of you.{/n}
"You were supposed to warn me," {n}Minagho says.{/n}
"Against a lie you admired that much? You'd have taken it as a compliment."
{n}Chivarro offers her the other half. Minagho takes it from her fingers with her teeth, and keeps the fingers a while longer than the plum requires.{/n}
"Again?" {n}Chivarro turns the tray toward you.{/n} "Or have you bled enough for one evening, honey?"''')

text(S, "game", '''"The stone was right. The performance was too much. She wanted you to believe she could never make so stupid a mistake, so you'd make it for her."
"You're giving away my methods," {n}Minagho says.{/n}
"You'll invent filthier ones."
{n}This time you watch the hands, not the faces. It helps a little. Chivarro does not soften her play for you; twice she asks whether you are certain, so politely that the second question feels like a knife being turned to catch the light.
Minagho loses. Chivarro takes her forfeit without asking: a paladin on the walls of Drezen, the night the gate opened, and how long Minagho kept him alive and talking. Minagho had half forgotten him. She is delighted to have him back. Chivarro tells it with relish, corrects the details twice from inside Minagho's head, and gives you the plum.{/n}
"There. Nobody at this table owes an introduction, an explanation or a fee for the next hour. Let's see what happens to the conversation when nobody's being paid for it."''')

text(S, "minagho_close", '''"Then I'll have to be vicious with my clothes on. A terrible hardship."
{n}She settles against your side, heavier than she looks, one hoof up on the table among the stones. You ask what she enjoyed before she learned to make pleasure useful. She tells you about Drezen, the night the walls opened, and which of the knights she kept alive longest, and watches your face the whole time to see which part you flinch at.
When you don't flinch where she expects, she tries again, slower.{/n}
"Being the first to know a thing. Not to sell it. To watch everyone else's certainty look ridiculous for a moment, right before it dies."
"You still enjoy that."
"Darling, I've kept all my accomplishments."
{n}Her claws find your hand and stay there, pricking. When Chivarro comes back, Minagho is halfway through a story she has sworn not to improve. Chivarro hears the last sentence, reads the rest out of her, and corrects the body count upward.{/n}''')

text(S, "chivarro_close", '''{n}She takes your hand, turns it palm up and reads it as if the lines were a bill she suspects of padding.{/n}
"I dislike being complimented on my memory. They think it's affection. It's a woman who refuses to be cheated twice by the same face."
"That sounds useful."
"It's lucrative. You asked what I never needed a guest to like."
{n}Her thumb presses into the heel of your hand, hard enough to find bone.{/n}
"But I remember useless things too. A banker who took off one earring before every lie and never understood how I knew. A knight who paid to be told he was filth, and wept because nobody at the Delights would say it softly enough. The way Minagho waits until everyone has gone before she admits she enjoyed a killing."
"Will you make me wait?"
{n}Chivarro brings your hand to her mouth and bites the knuckle. Not gently.{/n}
"No. I've enjoyed myself. Now you have something to remember, and a mark to remember it by."''')

text(S, "together_close", '''{n}Chivarro arranges the cushions with more authority than the task requires. Minagho objects until she finds the arrangement gives her a place against both of you; then she becomes suspiciously cooperative, and digs a hoof into your shin to make sure you notice.
You sit tangled together and talk. Chivarro asks a question she has been saving since your first meeting, then answers it herself out of your head before you can, and laughs at your face. Minagho answers a different question entirely: how much faster she would have taken Drezen with Chivarro on the walls. Chivarro tells her she would have charged admission.
Nobody takes anything off. Chivarro's fingers stay laced through yours, her nails in the back of your hand; Minagho leans on your shoulder and goes quiet without letting go of either of you. When you finally get up, both of them let you go, and both of them watch you to the door as if you were something they had bought and not yet decided where to put.{/n}''')

text(S, "slow", '''{n}Chivarro pulls her dress back over her shoulder and deals the stones between you.{/n} "Then lose another round, honey. Lose it slowly."
{n}Minagho steals the last plum and bites it in half without taking her eyes off you.{/n}
"You had better be worth the wait, Golarian. I don't wait well. Ask anyone who ever kept me waiting. Oh. You can't."''')

text(S, "company", '''"Then I'll stop pricing the empty space beside you. Sit where you like. I'll charge for the view either way."
{n}She brings the mask stones back. Minagho proposes new rules that would have made her the winner of the last round. Chivarro rejects them on exactly those grounds and makes you set the first mask.
The evening turns vicious in the pleasant way. Neither woman gets easier to beat, and every forfeit Chivarro takes is a little worse than the last: one of your officers' debts, a thing Minagho did at Drezen with a gutting hook, the price Chivarro once got for a paladin who had never been touched. Minagho gets worse at hiding her delight when you catch one of Chivarro's tricks. Chivarro notices, accuses her of divided loyalties, and kisses her hard enough to make the point.
At the door Chivarro asks whether you will come again without a letter to answer. Minagho tells you to bring a better prize, and a dirtier secret.{/n}''')

# ---------------------------------------------------------------------------
# minaghos_unfinished_sentence: the street outcome is read after the street.
# ---------------------------------------------------------------------------
S = "minaghos_unfinished_sentence"
text(S, "roof", '''{n}You sit on the step below her and give your opinion of the gutter, which is broken, and the roofer, who is a thief. Minagho accuses him of theft, then sabotage, then an attempt to drown her personally by drainpipe, and lists in detail what she will do to his fingers.
A ladder goes past in the street, carried by a man who looks up, sees her own face with no glamour on it, and walks a great deal faster. She laughs until the cut on her cheek opens again.{/n}
"Now I have to know whether it was him."
{n}Chivarro comes back up the street with a lamp in one hand and her account book in the other, smelling of cellar damp. She looks at the blood on the cobbles, then at Minagho, and reads the rest off the pair of you without asking.{/n}
"You started without me."
"You were busy buying a cellar."
"I'm always busy buying a cellar." {n}She sits on the step above, puts her knee into Minagho's back, and charges you for the lamp oil.{/n}''', paras=(
    when(P + "street_abandoned", '''{n}Chivarro does not look at you once, which is how you know she heard all of it from the corner.{/n} "You stood there, honey. I could hear you not moving. I'll remember the sound."'''),
    when(P + "survivor_maimed", '''{n}Chivarro glances at the well, then at the blood under Minagho's claws, and smiles for the first time tonight.{/n} "Oh. You did have fun."'''),
))

text(S, "hand_after", '''{n}Later the rain has eased and the room is dark. Minagho lies across you as if you were furniture she has paid for, one hoof hooked over your ankle so you can't leave without waking her.{/n}''', paras=(
    when(P + "street_protected", '''"Don't move. You stood in the street for me, and I hate owing. I'm collecting."'''),
    when(P + "street_abandoned", '''"Don't move. You let them have me, Golarian. This doesn't settle it. This is me deciding how long it takes."'''),
    when(P + "survivor_maimed", '''"Don't move. I can still taste that street. Best night since Drezen fell, and you gave it to me."'''),
    p('''"Don't move. You owe me for tonight, and I'm collecting."''',
      forbids=(P + "street_protected", P + "street_abandoned", P + "survivor_maimed")),
))

# ---------------------------------------------------------------------------
# after_the_last_lamp: the quiet answers keep the madam's appetite.
# ---------------------------------------------------------------------------
S = "after_the_last_lamp"
text(S, "held", '''{n}You stay together on the couch. Chivarro tells you which of last night's guests will come back, which will never come back, and which will come back swearing they never came, and what she will charge each kind. She is never wrong. She can name your footsteps on the ladder, she says; when you dispute it she imitates them, badly and obscenely, and kisses you before you can complain.
The ledger stays shut. At the trapdoor, much later, she tells you to remember this hour when you're out killing demons, because she intends to send a bill for it, and she has never once forgiven a debt.{/n}''')

text(S, "quiet", '''{n}Chivarro takes one end of the couch and gives you the other, and puts her bare feet in your lap without asking whether you want them there. Below, the shoulders-man is snoring across the doorway. She starts to say something, decides you haven't paid for it, and pulls the blanket up instead.{/n}
"Stay there. I like knowing somebody's minding the door who isn't on my books. Wake me if anyone tries to rob me. Wake me twice if it's Sivane."''')

text(S, "empty", '''"Empty? My house?" {n}She thinks about it seriously, which is the worst of it.{/n} "Out go the drunks and the priests and the captain who cries. Out goes Sivane, after she's paid her fines. I'd keep the bouncer; he's restful." {n}She finishes her wine.{/n} "And Minagho, of course, sulking in the best room, complaining about the noise she isn't hearing. And you, I suppose, if you paid."
"And if I didn't?"
"Then you'd be polishing the floor, honey, and I'd keep you anyway."
{n}You build her imaginary empty house between you, room by room, until it has a terrible staircase, a cellar for the guests who don't pay, and a door Minagho would kick down out of spite before discovering she liked what was chained up behind it. Chivarro sees you down the ladder still laughing.{/n}''')

# ---------------------------------------------------------------------------
# what_she_will_take: the road out is priced and predatory, not a postcard.
# ---------------------------------------------------------------------------
S = "what_she_will_take"
text(S, "lasting_close", '''{n}You kiss her before the next joke is ready. Chivarro catches your collar and keeps you there long after the kiss is over, her other hand flat on the case as if you might try to steal it.
Afterward she rights the case and slides a blank sheet into the side pocket beside the handbill.{/n}
"For the first address. If I put it anywhere else, I'll decide you're business and write to you like a customer."
{n}You ask how she writes to customers she especially likes. She shows you, aloud: a sweet, proper greeting that turns, halfway down the page, into a description of what she intends to do to them, itemised, with prices. Then she ruins it by laughing, and then she stops laughing, and the case stays open on the floor for the rest of the evening with her feet up on it and you beside her.{/n}''')

text(S, "visits_close", '''{n}Chivarro settles under your arm with her claws hooked in your belt and tells you about the next house: a port she has heard is full of rich, frightened men and has no madam worth the name. She describes what she will do to the competition in loving detail, and which of the local priests she will have on her books inside a month.
You ask who told her about the place. She admits, with bad grace, that it was a customer she always claimed bored her rigid.{/n}
"He talked for an hour. I can't remember his name."
"You remember the port."
"Yes. I'm furious with him. I should have charged him for the hour."
{n}She kisses you, and goes back to describing the room she will take for herself at the top of the new house, the one with a lock only she has a key to, until the lamp gutters.{/n}''')

text(S, "visits_talk", '''{n}You stay while Chivarro wraps the few things she won't leave behind. Each has a story, and she chooses which to tell. A knife with a chipped point: a customer who tried to leave without paying, and how far he got. A ring too small for any of her fingers: she won't say whose finger it came off, only that he doesn't need it any more. A plain iron pin, bought because the seller told her it was too severe for a woman like her; she shows you the face she wore while paying, which knocked a third off the price and sent him home unsure why he felt afraid.
When you leave, the case is packed and the house below is opening for the evening, and she stands at the trapdoor looking pleased with both.{/n}''')

text(S, "friends", '''{n}Chivarro hears the whole answer before you've finished giving it.{/n}
"Then friendship. I'll have to invite you up to talk and cheat you at dice instead."
{n}She pauses.{/n}
"I'm a little disappointed. I'll decide exactly how much after you've gone, and I won't do it where you can hear."
{n}The smile takes the worst edge off it, and leaves the rest.{/n}
"You'll still hear what becomes of the house, whether you like it or not. I want your opinion when it's useful and your company when it isn't. If I send for you, come. I'm a demon, not a debt collector. Mostly."
{n}She shows you the one thing she has decided not to take: an ornament from the Delights, gold and gaudy, given to her by a lord who thought it bought him something. She has already found a buyer. She tells you what the lord thought it bought, in detail, and laughs the whole way through.{/n}''')

# ---------------------------------------------------------------------------
# before_the_last_road: the farewell in their own register; the grudges the
# route promised are brought out; the commitment stances are spoken in the room.
# ---------------------------------------------------------------------------
S = "before_the_last_road"
text(S, "start", '''{n}The last meeting before your departure is in Chivarro's loft above the house, with the red lamp lit and the case half-packed on the floor. Below, the house is open; through the boards you can hear Sivane taking a merchant apart.
Minagho has brought a bag of sugared plums and dropped it in the middle of the table without explaining herself. She has also brought a knife, which she does not explain either, and which she uses to cut the plums.
For once nobody has brought a proposal from a stranger. Minagho asks what you know of the road ahead. You tell her what you can. She listens to the uncertain parts with the expression of a woman pricing a coffin.
Chivarro sets out three cups.{/n}
"The house is settled," {n}she says.{/n} "Sivane has her cut, the bouncer has his, the landlord has a fright he won't forget. Whatever happens on your road, honey, I'm not leaving a pile of debts for some other bitch to collect."
"Ambitious," {n}Minagho says.{/n}
"I'm an ambitious woman. You've noticed. You complain about it in bed."
{n}Minagho puts the knife down, takes Chivarro's hand and bites the side of it, and for a moment the two of them are somewhere you are not invited. Then they turn their faces toward you, together, which is worse.{/n}''', paras=(
    p('''{n}Before you can open your mouth, Minagho lays the knife flat on the table between you, handle toward herself.{/n} "First, the account. We said we'd bring things out on a night you'd forgotten them. Here's the night."''',
      any_groups=((P + "agent_handed_over", P + "street_abandoned", P + "nerath_arrested", P + "soldiers_barred",
                   P + "officer_names_bought", P + "clerk_sold", P + "clerk_bought", P + "agent_killed", P + "forger_hanged"),)),
    when(P + "agent_handed_over", '''"The horned man in the counting room. You took him off my plate and handed him to your fucking priests. I hear they're still at him." {n}Minagho cuts a plum in half, slowly, and doesn't eat either piece.{/n} "He was mine, Golarian. I'd have made him sing. There. We've looked at it together. Don't think we've finished looking."'''),
    when(P + "agent_killed", '''{n}Minagho is wearing the horned man's gloves. They have never fitted. She flexes them at you, one finger at a time, and smiles the smile she wore in the counting room.{/n} "Still the best present anyone's given me in this miserable city."'''),
    when(P + "buyer_list_kept", '''{n}Minagho pats her bodice, where the horned man's coded list has lived since the counting room.{/n} "Four of the buyers on it have had very bad months, darling. Two of them are still alive. I'm pacing myself."'''),
    when(P + "street_abandoned", '''"And the street. You stood with your arms folded while thirty Kenabres rats beat me in the mud. I put that somewhere I could find it." {n}She taps the knife.{/n} "I haven't decided what it costs you. I like not deciding. It makes you sweat."'''),
    when(P + "forger_hanged", '''"You gave the forger a rope," {n}Minagho says.{/n} "I went to watch, darling. He kicked for a long time; whoever tied it knew nothing about knots. I nearly asked for my six coppers back."'''),
    when(P + "nerath_arrested", '''"Nerath, honey." {n}Chivarro doesn't look up from her cup.{/n} "Three hundred and fifty crowns and my best customer, marched up my stair in his shirt. I said I'd bring it up on a night you thought you were winning. You think you're winning. There. Now it's spoiled."'''),
    when(P + "clerk_sold", '''{n}Chivarro tilts her head at the floor, where the house is roaring.{/n} "Tam's learned the price board. Nerath cried the first night the boy didn't. I charged him for that too."'''),
    when(P + "clerk_bought", '''"You still haven't torn up the clerk's debt, have you, honey?" {n}Chivarro smiles.{/n} "I can hear it folded in your coat. You like owning him. Don't scowl. It's the first thing about you I've fully understood."'''),
    when(P + "soldiers_barred", '''"And your soldiers," {n}Chivarro adds.{/n} "A third of my takings, gone because you got squeamish about captains. I've collected most of it from priests. The rest I'm collecting from you, one way or another, for as long as you live."'''),
    when(P + "house_tolerated", '''"You told me it was my house and I should run it," {n}Chivarro says.{/n} "I have. Your captains still come down my stair, and every one of them knows that you know. You'd be amazed how obedient that makes a man. I've been spending it."'''),
    when(P + "officer_names_bought", '''"You've still got my list of your officers, haven't you, honey?" {n}Chivarro pats your hand.{/n} "I sold the same list to a count from Mendev last week. Only the half with the quartermasters. You didn't pay for exclusivity."'''),
))

text(S, "answers", '''"Then say it before Minagho eats the rest of those."
{n}Minagho has a plum halfway to her mouth on the point of the knife. She offers it to Chivarro instead, who takes it off the blade with her teeth and doesn't let the manoeuvre distract her for a moment.
When Minagho turns back to you, the grin thins.{/n}
"I hate farewells. People say things they can't possibly know and then expect to be thanked for the prophecy. Tell me what you want when you come back, Golarian. Say it plainly. If you make a speech, I'll cut it short."
{n}Chivarro moves her cup to make room for yours, then moves it back a little, so that you have to reach.{/n}''')

text(S, "minagho", '''"Yes. You'll come when I send for you, and I'll complain about how long you took, and you'll apologise on your knees. Chivarro will tell you which parts to believe."
{n}She drags you across the table by your collar; the cups go over. The kiss is impatient and has teeth in it. She holds you there afterward, breathing on your mouth, while Chivarro rescues the plums from the wine.{/n}
"She comes back to me, honey," {n}Chivarro tells you.{/n} "You may keep her company. You do not buy my place beside her."''')

text(S, "together", '''"Yes," {n}Chivarro says.{/n} "And I'm buying a better couch. This one shrieks every time I look at it. I expect better manners from things I've paid for."
"You'll be looking at me," {n}Minagho says.{/n}
"You're already disgustingly pleased with yourself."
"I'll try to keep it up."
{n}Minagho takes your hand and presses her thumbnail into the palm until it stings.{/n}
"The three of us. I want more evenings where she forgets which of us she's shouting at."
{n}Chivarro takes your other hand and drags both of you toward her. The first kiss turns into an argument about who moved which chair. The second settles it. The third knocks the case off the table, and nobody picks it up.
When you sit back, their hands are still on you. Chivarro starts describing the new couch with such precision that Minagho asks how long she has been planning to break it. She doesn't get an answer.{/n}''')

text(S, "friendship", '''"Then bring a better excuse the next time you lose at stones. I hate beating someone who spends the evening apologising."
{n}Minagho takes the plums back. Chivarro moves the knife out of her reach, then thinks better of it and moves it back.{/n}
"She's already planned the excuse," {n}Chivarro says.{/n}
"And it's a vile one."
"Chivarro wants you," {n}Minagho says.{/n} "She still comes back to me. Hurt her and I will open you from throat to crotch."''')

text(S, "open", '''"Then send word when you've got an evening," {n}Chivarro says.{/n} "I'll try to have something worth losing sleep over. Or someone."
"Her letters will sound far more respectable than the evening," {n}Minagho warns you.{/n} "Mine will sound worse. Mine will be accurate."
{n}They start arguing over who wrote the more misleading invitation. Chivarro produces the first note, the one with Minagho's little skull on it. Minagho claims the skull was an honest warning about the company.
You leave them arguing over who keeps it. At the stair, Chivarro presses it into your hand.
Minagho has drawn a second skull beside the first. This one has your hair.{/n}''')

text(S, "service", '''"Good. Then at least we've called the thing by its name."
{n}She does not soften it for the sake of a farewell. She would sooner bite her own tongue off.{/n}
"I've said what I want. Chivarro has said hers. Remember both, and don't you dare dress them up as proof that the leash has turned into a ribbon. I'll know. I'll make you eat the ribbon."
{n}Chivarro's hand lies beside hers on the table.{/n}
"What I have with you is mine, honey," {n}Chivarro tells you.{/n} "It buys you nothing of her. And her service doesn't make my leaving yours to forbid. Get that into your skull before either of us says anything sweet."
{n}Minagho closes her claws around Chivarro's wrist and lifts her cup with the other hand. Chivarro leaves hers where it is.{/n}
"Chivarro wants you," {n}Minagho says.{/n} "She still comes back to me. Hurt her and I will open you from throat to crotch."''')

SHARE = '''"Minagho keeps me, honey," {n}Chivarro says.{/n} "You join us. You don't divide the takings."
"And she keeps me," {n}Minagho says, without letting go of her.{/n} "Knock before you come in, Golarian. If we don't answer, entertain yourself on the stair."'''
EXCLUSIVE_MINAGHO = '''{n}Minagho puts the knife down very carefully, the way people do when they don't trust their hands.{/n} "You want Chivarro gone? I ran from every hunter Baphomet owns for her, darling. I'm not giving her up for your bed. I choose her. Swallow that, or get out."'''
EXCLUSIVE_MINAGHO_PRESENT = '''"Trying to evict me, honey? From a woman you never owned?" {n}Chivarro doesn't raise her voice. She doesn't need to; she is already inside your head, and you can feel her not liking what she finds there.{/n} "Keep your little citadel. She has answered you."'''
SECRET_MINAGHO = '''{n}You catch Minagho alone on the ladder while Chivarro is below shouting at Sivane, and you say it low.{/n} "A secret from Chivarro?" {n}Her grin goes slow and wide.{/n} "Oh, she'll hate that. Leave your door unbarred tonight. And don't look at her like that at supper, you idiot; she reads faces even when she isn't trying."'''
EXCLUSIVE_CHIVARRO = '''"You want me to throw Minagho out? Honey, I lost the Delights. I will not lose her to furnish your bedroom. Share, or find someone cheaper."'''
EXCLUSIVE_CHIVARRO_PRESENT = '''{n}Minagho has heard every word. She takes the knife off the table and holds it point-down between two claws, idly, the way she held Staunton's chin.{/n} "You asked her to throw me away? I have gutted people for less. She has given you your answer. Try to hear it through that thick skull."'''
SECRET_CHIVARRO = '''{n}You find Chivarro alone in the counting alcove while Minagho is upstairs sharpening something. She hears what you want before you have finished wanting it.{/n} "You want to lie to Minagho, honey? Come after she's gone out hunting. If you blab, I'll tell her whose idea it was, and I'll watch what she does about it."'''
DISCOVERY_MINAGHO = '''{n}Chivarro comes up the ladder at dawn with the night's takings. She stops on the top rung. She doesn't need a lamp, or a word, or the state of the sheets: she reads the whole night off the two of you before the trapdoor has finished falling.
Minagho sits up, slowly, and does not reach for anything to cover herself with.{/n}'''
DISCOVERY_CHIVARRO = '''{n}Minagho comes in without knocking, because she never knocks, with somebody's blood drying on her sleeve. Chivarro is still beside you. Minagho takes your belt out of your hand before you can buckle it, and waits.{/n}'''

for k in ("0", "2"):
    text(S, "stance_%s_share" % k, SHARE)
for k in ("0", "1", "2"):
    text(S, "stance_%s_exclusive_minagho" % k, EXCLUSIVE_MINAGHO)
    text(S, "stance_%s_exclusive_minagho_present" % k, EXCLUSIVE_MINAGHO_PRESENT)
    text(S, "stance_%s_secret_minagho" % k, SECRET_MINAGHO)
    text(S, "stance_discovery_%s_minagho" % k, DISCOVERY_MINAGHO)
for k in ("0", "2", "3", "7"):
    text(S, "stance_%s_exclusive_chivarro" % k, EXCLUSIVE_CHIVARRO)
    text(S, "stance_%s_exclusive_chivarro_present" % k, EXCLUSIVE_CHIVARRO_PRESENT)
    text(S, "stance_%s_secret_chivarro" % k, SECRET_CHIVARRO)
    text(S, "stance_discovery_%s_chivarro" % k, DISCOVERY_CHIVARRO)

# ---------------------------------------------------------------------------
# Endings: stale retired-chain references removed; abstract endings given teeth;
# the living endings read what the Commander let them do on the way.
# ---------------------------------------------------------------------------
ENDINGS = {
    "ending_open": '''{n}Chivarro sent invitations when she had a room worth showing off. Minagho sent one when she had found a particularly irritating question, or a particularly stupid enemy. The Commander answered some, and was charged for the rest.
No house was promised, and none was given. Chivarro kept the first note, the one with Minagho's little skull on it, pinned above her bed, and told guests it was the only thing in the house that was not for sale. Then she named a price for it.
The mask game survived. So did the argument over who had stolen the last plum, which Minagho settled one winter by stabbing the plum to the table between them.{/n}''',
    "ending_friends": '''{n}Friendship with the lilitu brought good wine, appalling advice and invitations that sometimes required a bodyguard, and once required a priest. Chivarro once offered to improve a tiresome guest's manners. Minagho objected that he had no manners worth preserving, and improved his face instead.
The Commander remained welcome at their table. Some evenings ended with the mask stones scattered across it; others ended when the two women began looking at each other and forgot to deal, and the Commander was shown the stair.
Minagho bought a new set of stones to defeat Chivarro's cheating. Chivarro won the first game with them and sent her the bill.{/n}''',
    "ending_unfinished": '''{n}Minagho kept the note with the little skull. Chivarro added another correction under it, then an address. Their next letter carried three crossed-out dates, an argument about the wine, and a description of what they had done to the last man who kept them waiting.
The Commander had left a visit unfinished, not promised a life. The two women found plenty to do while they waited for an answer. Most of it would have hanged a mortal, and some of it made their invitations considerably harder to refuse.{/n}''',
}
ENDINGS_WITH_TWINS = {
    "ending_both_lost": '''{n}Minagho and Chivarro both died before the war was done, and left behind a note with two hands on it: a little skull beside an invitation, and a nasty correction underneath the skull.
Nobody else at the citadel knew what it meant, and nobody else was ever invited. Whoever had killed them was very lucky that neither had lived long enough to find out who it was.{/n}''',
    "ending_ascent": '''{n}After the Commander's ascent, Minagho was furious for a month. She had been courted by something that turned into a god, and she had not thought to demand anything while it was still mortal and could be made to pay. She never forgave herself the oversight, and never forgave the Commander for it either.
Chivarro read the thing the Commander had become once, from a very great distance, and would not say what she found there. She raised every price in the house the next morning. When Minagho asked why, she said a god owed her an evening, and the rest of the world could make up the difference.{/n}''',
    "ending_sacrifice": '''{n}After the Commander's sacrifice, Chivarro kept the first note, the one with Minagho's little skull on it and her own nasty correction underneath. She would not sell it. Several people offered.
Minagho did not mourn where anyone could see. She went out the night the news came and came back at dawn with somebody else's blood on her and a far better mood than she had any right to. She said it was for the Commander. Chivarro read the truth of it out of her and did not argue.
They spoke of the Commander differently, fought about it often, and neither ever let the other win.{/n}''',
    "ending_aeon": '''{n}In the remade history, no note with two hands on it ever reached the Commander. Chivarro never opened a house under the burned market, and Minagho never sat on a bad stair in Drezen drinking tavern beer and bleeding at a crowd.
Their lives had other rooms, other bargains, other corpses and their own long entanglement. Nothing of the erased evenings came back to them. If anything had, Minagho would have charged for it, and Chivarro would have doubled the price.{/n}''',
}

LIVING = ("ending_together", "ending_two", "ending_minagho", "ending_chivarro", "ending_open",
          "ending_friends", "ending_chivarro_service", "ending_service")
CONSEQUENCES = (
    when(P + "agent_killed", '''{n}Minagho still wore the horned man's gloves on special occasions. They had never fitted. That was rather the point.{/n}'''),
    when(P + "agent_handed_over", '''{n}The horned man the Commander handed to the Inquisition was never seen again. Minagho brought him up at the worst possible moments for the rest of the Commander's life, and enjoyed it every time.{/n}'''),
    when(P + "survivor_maimed", '''{n}The well in the Kenabres street was filled in the following spring; nobody in that quarter would draw from it. Minagho walked past it whenever she wanted cheering up.{/n}'''),
    when(P + "street_abandoned", '''{n}Minagho never mentioned the street again, and never forgot it. Once a year, on the night, she sent the Commander a single cobblestone wrapped in silk.{/n}'''),
    when(P + "forger_killed", '''{n}Printers in Drezen stopped selling woodcuts of a remorseful Minagho in a crown. Nobody had to tell them why.{/n}'''),
    when(P + "forger_maimed", '''{n}The forger learned to write with his left hand. He never wrote about Minagho again, with either.{/n}'''),
    when(P + "clerk_sold", '''{n}Tam, Nerath's clerk, worked off his father's debt in Chivarro's house. It took a great deal longer than twenty years. Chivarro saw to that.{/n}'''),
    when(P + "nerath_arrested", '''{n}Chivarro never let the Commander forget Nerath. She brought him up on good nights, mostly, to ruin them.{/n}'''),
)


def _pages(payload):
    return {s["Id"][len(P):]: s for s in payload["Scenes"] if s["Id"].startswith(P)}


def _node(pages, sid, nid):
    matches = [n for n in pages[sid]["Nodes"] if n["Id"] == nid]
    if len(matches) != 1:
        raise KeyError("minachiv cloud: %s/%s matched %d nodes" % (sid, nid, len(matches)))
    return matches[0]


def integrate(payload):
    pages = _pages(payload)
    for (sid, nid), body in NODES.items():
        _node(pages, sid, nid)["Text"] = body.strip()
    for (sid, nid), paras in PARAS.items():
        node = _node(pages, sid, nid)
        node["Paragraphs"] = node.get("Paragraphs", []) + [dict(x) for x in paras]
    for sid, body in ENDINGS.items():
        _node(pages, sid, "end")["Text"] = body.strip()
    for sid, body in ENDINGS_WITH_TWINS.items():
        for twin in (sid, sid + "_completed"):
            _node(pages, twin, "end")["Text"] = body.strip()
    for sid in LIVING:
        node = _node(pages, sid, "end")
        # After the partner-state continuity lines: payoff_contracts registers those by index.
        node["Paragraphs"] = node.get("Paragraphs", []) + [dict(x) for x in CONSEQUENCES]
    for sid in {key[0] for key in NODES} | {key[0] for key in PARAS} | set(ENDINGS) | set(ENDINGS_WITH_TWINS):
        for twin in (sid, sid + "_completed"):
            for node in pages.get(twin, {}).get("Nodes", []):
                texts = [node["Text"]] + [a["Text"] for a in node["Choices"]] + [
                    para["Text"] for para in node.get("Paragraphs", [])]
                if any(PENDING in t for t in texts):
                    raise ValueError("minachiv cloud: prose still pending at %s/%s" % (twin, node["Id"]))
