"""Herrax: the courtship around the chain (herrax_trickster), in her own hall in Chapter 4 and by her courier in Chapter 5.

Every physical beat is inline on her hub (Herraxa_dialogue AnswersList_0004, back to Cue_0100); one is on Rokhorn's list
(AnswersList_0152, back to Cue_0159). Chapter 5 beats are rest-delivered pages: her letters, carried to Drezen by the man
she cut (or by the man she did not), and one visit from him alone. Each beat engages a canon anchor of hers:
- pricing everything, and being the one thing in the house not for sale (Cue_0097 661508b5, held back for the commit);
- the house as "a small labyrinth dedicated to hedonism" (Cue_0025 31a7cb93), the aasimar "asset" (Cue_0315 fdbce4a3),
  the Spinner of Nightmares' cultists "left ... with us for our amusement" (Cue_0054 a203e38f), the forgotten rings "cut off
  a dead body along with the fingers" (Cue_0052 d6955c2a), the Sinners (Cue_0007 59354369), Morevet (Cue_0081 f9475459)
  and the Mad Glowworm (Cue_0164 0a867832);
- Chivarro and Minagho (Cue_0024 4f7ad6a3), the kill she asked for (Cue_0045 49135105), "I inherited her riches, but not her
  debts" (Cue_0070 2aba385a), the token for her knight (Cue_0049 0362b755);
- the scars (Cue_0001 1439d338, Cue_0023 442a829d, Cue_0064 aeac18f3, Cue_0304 0cbac9fa: "a pinch of spice"); Sosiel's
  "why anyone should wish to spoil such beauty" (Cue_0303 e56632b9); what caused the eye is never stated in canon, so she
  tells three different stories and never settles which is true (her lies, labelled as hers);
- the Lady in Shadow's claim on every succubus (Nocticula_main/Cue_0523 b84ef61b) and Willodus, who "no longer visits"
  (Cue_0299 2e9aa440); Arueshalae's "house of pain, filth, and lies" (Cue_0321 2948da80).
Acknowledgments of other women (Chivarro, Minagho, Arueshalae, Nocticula) are in Herrax's voice only; no scene between
partners, and no line states exclusivity as settled fact.
"""
from story_format import c, n, scene
from storylines.herrax_trickster import (ASKED_KILL, BAIT, BLOWN, CHEEK, CLIENT, CLOSED, COMMITTED, CONFESSED, DECLINED,
                                         H, HAGGLED, HANDED, HUB, KNIFE_TAKEN, LESSON, LIE_GREED, LIE_HUNGER, LIE_SPITE, MADAM,
                                         MC_FAVOR, MET, MORNING, PRIMED, REL, RESTORED, RET, ROK_LIST, ROK_RET, TOLD_DEAD,
                                         WILLODUS, COIN_HELD, COIN_LOST, SENT, MOREVET_DEAD, morevet_variants, discovery, discovery_entry, hl, hx, nar, rk, rl)

SCENES = []
B = "herrax.house."

FIRST_PRICE = B + "first_price"
LABYRINTH = B + "labyrinth"
FORGOTTEN = B + "forgotten_things"
PREDECESSOR = B + "predecessor"
THE_LADY = B + "the_lady"
EYE_ONE = B + "eye.one"
EYE_TWO = B + "eye.two"
EYE_THREE = B + "eye.three"
ARENA = B + "arena"
SOUNDING = B + "rokhorn.sounding"
REHEARSAL = B + "rehearsal"
EVE = B + "eve"
MEANS = B + "reachable_means"
STAIRS = B + "the_stairs"
TALK = B + "the_house_talks"
LAST_NIGHT = B + "last_night"
BARE_HIP = B + "bare_hip"
# Choice flags read by later beats and letters.
RING = B + "ring.kept"
RING_REFUSED = B + "ring.refused"
EYE_BELIEVED = B + "eye.believed"
EYE_ASKED = B + "eye.asked"
EYE_GUESSED = B + "eye.guessed"
WARNED = B + "aasimar.warned"
PRICED_FORTY_ONE = B + "priced.forty_one"
# Native reads for node variants only (bound in herrax_trickster.integrate).
SERMON = "herrax.sermon_heard"                 # SeenCues Cue_0321 (Arueshalae in her hall)
SOSIEL = "herrax.sosiel_admired"               # SeenCues Cue_0303 (Sosiel on her scars)
CLAIMED = "arueshalae.nocticula_claimed"       # SeenCues Nocticula_main/Cue_0523 (trickster_world)
# Chapter 5 letters.
L = "herrax.letters."
COURIER = L + "the_courier"
OFFER = L + "rokhorns_offer"
LADYS_PEOPLE = L + "the_ladys_people"
GIFT = L + "the_gift"
HOUSE_NEWS = L + "house_news"
BEFORE = L + "before_the_wound"
OFFER_REFUSED = L + "offer.refused"
OFFER_STRUNG = L + "offer.strung_along"
OFFER_TOLD = L + "offer.told_her"
REPLY_WARM = L + "reply.warm"
REPLY_COOL = L + "reply.cool"
REPLY_CRUDE = L + "reply.crude"
KNIFE_GIFT = L + "knife.kept"
BET_LOST = B + "arena.bet_lost"              # the Commander picked the loser at the Battlebliss: a thousand owed
BET_COLLECTED = L + "arena.bet_collected"    # she named the price in the packet


def beat(id, title, entry, nodes, requires, forbids=(), delay=24, **extra):
    """An optional inline beat on her hub in Chapter 4."""
    SCENES.append(scene(id, title, "Herrax", 4, entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", MADAM, MET, *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, *forbids))), delay=delay, last=4, optional=True,
                        Relationship=REL, AnswerLists=[HUB], NativeReturnCue=RET, **extra))


def post(id, title, nodes, requires, forbids=(), delay=72, kind="letter", **extra):
    """An optional Chapter 5 page, by her courier."""
    SCENES.append(scene(id, title, "Herrax", 5, "", nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, *forbids))), delay=delay, last=5, optional=True,
                        Relationship=REL, Remote=True, Kind=kind, Chapters=[5], **extra))


# === Chapter 4: before the chain =========================================================================================

beat(FIRST_PRICE, "The only free thing", '"You look at everyone as if you were pricing them."', [
    hx("start", '''{n}Herrax is at the end of the bar with the evening's first cup of something dark, watching the room the way a spider watches the corners of its web.{/n}
"I am, lover. It's the only honest way to look at anybody. You'd be amazed how much trouble it saves." {n}She turns the cup a quarter-turn on the wood.{/n} "Shall I price you? It's free. It's the only thing in my house that is."''',
       c('"Go on, then."', "price"),
       c('[Flirt] "Only if I get to price you back."', "back")),
    hx("price", '''{n}She takes her time. Her good eye goes over you from boots to brow and back, and the blind one follows, milky and unhurried, as if it saw something the other one missed.{/n}
"Mortal. Mostly. Something in the chest that burns where it shouldn't; my girls would fight each other for a taste of it, and one of them would win, and you'd be very tired for a week." {n}She sips.{/n}
"For a night with any of them, the Sinners included, I'd pay you. That's rare. For your sword arm, a great deal, while you're alive. For your good opinion, nothing at all. I've never needed anyone's."''',
       c('"And what would a night with you cost?"', "not_for_sale"),
       c('"You\'d pay me? That\'s a first for a madam."', "pay")),
    hx("pay", '''"Madams pay for talent all the time, honey. We just call it something else, and deduct it later." {n}Her mouth quirks, and the scar pulls the quirk crooked.{/n}
"The Sinners would drain you dry and call it a compliment. Morevet would talk you to death, which is worse. The Glowworm would make you laugh so hard you'd forget your own name and wake up without your boots. I know what my stock is worth, lover. I also know what it breaks."''',
       c('"And you?"', "not_for_sale")),
    hx("back", '''{n}She laughs, light and pleased, and the girls on the nearest couch glance over to see who has amused the madam.{/n}
"Price me? Honey, people have tried. Kings, and worse." {n}She sets her chin on her fist and turns her face to the lamp, so the scar runs bright from cheekbone to lip.{/n} "Go on. I'm curious what a crusader thinks a scarred, half-blind madam with rags for wings is worth. Be careful. I bite bad appraisers."''',
       c('[Price her like stock] "The Sinners are forty thousand. You look like forty-one."', "forty_one",
         flags=(PRICED_FORTY_ONE,)),
       c('"Priceless. Which is a polite way of saying off the menu."', "not_for_sale")),
    hx("forty_one", '''"Forty-one." {n}She repeats it the way a jeweller repeats a weight she did not expect.{/n} "Forty for the body, which every succubus has, and one for the damage, which only I have." {n}Her good eye narrows.{/n}
"You counted the scars into the price, didn't you. Not out of it. Everyone else prices me as if they were a discount." {n}She clinks her cup against the counter by your hand.{/n} "Clever. Wrong, but clever."''',
       c('"Wrong how?"', "not_for_sale")),
    hx("not_for_sale", '''"Everything in this house is for sale, lover, and everyone in it. Except the madam. That's the first rule of the Delights, and the only one I've never broken for anyone." {n}She says it without regret, as another woman might say she had never learned to swim.{/n}
"Now. If you'd like to hear the house's ugliest opinion of me, ask Rokhorn why he obeys me. He tells the story beautifully. He's practised it on half my guests." {n}She stands, and her ragged wings stir the smoke.{/n} "Pay him first, if you want him honest. He's always most honest with people who've paid."''',
       c('"I might."'),
       c('"I\'d rather hear it from you."', "from_you")),
    hx("from_you", '''"From me you'd hear the pretty version." {n}She pats your cheek with two fingers, the way she might pat a new girl's.{/n} "Go and get the ugly one, and then come back and tell me whether you still want the pretty one. That's how I find out what people are made of. It's cheaper than asking."''',
       c('"I\'ll be back."'))],
    requires=(), delay=0)


beat(LABYRINTH, "Behind every door", '"Show me your house."', [
    hx("start", '''"My house?" {n}She looks genuinely pleased.{/n} "Honey, nobody sees my house. They see a room, and a door, and another room, and a door. Behind every door there's a corridor with other doors. We stand at the heart of a little labyrinth dedicated to pleasure, and most people never find out how deep it goes, because they stop at the first door that's interesting."
{n}She takes a lamp from the wall.{/n} "Come on, then. Try not to stop."''',
       c("[Follow her.]", "doors")),
    nar("doors", '''{n}She walks you through the Delights at a madam's pace, never hurrying, never quite stopping. A room of mirrors, where a guest who paid for the privilege is watching himself be adored. A room of smoke so thick you taste it for an hour. A room where a harpist is playing to nobody, because nobody is the client.{/n}
{n}Deeper in, behind a door with no handle on the outside, a dozen men and women in rotting finery lie on cushions in a sweet brown haze, too far gone to look up.{/n}''',
       c('"Who are they?"', "cultists")),
    hx("cultists", '''"Leftovers. Long before my time, a mad thing who spun nightmares kept a few rooms in this house for her own. Her refuge, she called it. When she moved on to Golarion she left her little cult behind for our amusement." {n}She lifts the lamp so they can see her. None of them does.{/n}
"They were useful for a while. Now they're furniture that breathes. Every so often a guest pays to try something on one of them that he wouldn't try on anyone who'd be missed." {n}She lowers the lamp.{/n} "Nothing in my house is wasted, lover. That's the whole art."''',
       c("[Walk on.]", "asset", requires=(SENT,)),
       c("[Walk on.]", "asset_empty", forbids=(SENT,))),
    hx("asset", '''{n}The next door opens on a clean room, whitewashed, almost a convent cell. Four girls sit on a bench in plain white shifts. They are aasimar; you would know it anywhere, the faint light under the skin. They are very still.{/n}
"And these are my future." {n}Herrax speaks softly, the way one speaks around sleeping children.{/n} "Pure and innocent. An asset to the Delights. It takes a long time to train them up, and the most important thing is never to tarnish them. I know how to be very, very careful."''',
       c("Continue", "asset_yours", requires=(SENT,)),
       c("Continue", "asset_choice", forbids=(SENT,))),
    hx("asset_yours", '''{n}She glances at you, and her mouth curves.{/n} "You'll recognise them, of course. You sent them to me yourself, out of the butcher Dyunk's pens: 'Go to the Ten Thousand Delights.' They wept all the way up my stairs. I've never had stock delivered so cheaply."''',
       c("Continue", "asset_choice")),
    hx("asset_empty", '''{n}The next door opens on a clean room, whitewashed, almost a convent cell, with a bench along one wall and nobody on it.{/n}
"My white room." {n}Herrax lifts the lamp, and looks at the empty bench the way another woman might look at an empty jewel case.{/n} "The butcher Dyunk had a pen of aasimar girls in the Fleshmarkets this season. I meant them to sit there. They have not come to my house." {n}She lowers the lamp.{/n} "The room waits. Rooms in my house always get filled, lover. The only question is what with."''',
       c("[Walk on.]", "dais")),
    hx("asset_choice", '''{n}One of the girls looks up at the sound of a new voice. Herrax meets her eyes, gently, and the girl looks down again.{/n}''',
       c('"You\'re going to break them."', "break"),
       c('"Someday someone will come for them."', "warn", flags=(WARNED,)),
       c("[Say nothing, and let her lead you on.]", "dais")),
    hx("break", '''"Break?" {n}She looks offended, and for once it isn't theatre.{/n} "I'm not a vavakia, lover. Breaking is waste. Breaking is what the arena's for. I'm going to teach them. Slowly. Until one day they come to me of their own accord and ask for the lesson, and mean it, and thank me."
"That's the difference between a brute and a madam. The brute gets one night out of a thing. I get a lifetime." {n}She closes the door softly on the white room.{/n}''',
       c("[Walk on.]", "dais")),
    hx("warn", '''{n}She considers you, and the girls behind the door, with the same unhurried eye.{/n} "Someone always does. A paladin, a brother, a crusade. It's the only kind of guest who never pays." {n}She closes the door.{/n}
"That's what the boys with knives are for. And if the boys aren't enough, lover, that's what the lesson is for. You'd be amazed how many rescued girls walk back up my stairs, once they've tasted the cold outside."''',
       c("[Walk on.]", "dais")),
    nar("dais", '''{n}The labyrinth lets you out, as she promised it would, in the great hall, at the foot of a low dais piled with cushions. The cushions are older than anything else in the room, and they smell faintly of a perfume that is not hers.{/n}''',
       c("Continue", "dais_sermon", requires=(SERMON,)),
       c("Continue", "dais_end", forbids=(SERMON,))),
    hx("dais_sermon", '''"Your little redeemed succubus stood just there." {n}Herrax points with the lamp.{/n} "In front of my guests, she called my house a house of pain, filth and lies. She said the pleasures leave scabs."
{n}She laughs.{/n} "The guests heard her, lover. They'll repeat it all over the Upper City. I couldn't have bought a better advertisement."''',
       c("Continue", "dais_end")),
    hx("dais_end", '''"Chivarro's chair. Her dais, her cushions, her scent. I kept all of it." {n}She sits, and arranges herself, and she fits it as if it had been cut for her.{/n}
"Everyone who comes up my stairs smells her and sees me, and understands without being told. That's the best kind of lesson, lover. The kind you never have to say out loud." {n}She gestures you away with the lamp.{/n} "Now you've seen more of my house than anyone who didn't pay for it. Don't make me regret it."''',
       c('"I won\'t."'))],
    requires=(FIRST_PRICE,), delay=20)


# Authored gift detail: the bent horn is recognised by witnesses at Herrax's bar.
beat(FORGOTTEN, "Forgotten things", '"What have you got there?"', [
    hx("start", '''{n}Herrax has a tray on the bar, and on the tray the night's harvest: two purses, a silver comb, a dagger with a snapped tip, and a little heap of rings. Some of the rings have been cut off. Two of them still have what they were cut off with.{/n}
"Things our guests forgot." {n}She sorts them with one claw, idly, the way a cook sorts lentils.{/n} "You'd be amazed what people forget in the Delights, honey. Rings. Purses. Their wives. The occasional finger."''',
       c('"And the guests who forgot them?"', "guests"),
       c('"You\'re selling these?"', "selling")),
    hx("guests", '''"Went home lighter." {n}She holds a gold signet up to the lamp. The finger inside it is grey and shrunken.{/n} "Or didn't go home. It's all the same to the tray."''',
       c("Continue", "token")),
    hx("selling", '''"To anyone who isn't squeamish. That's most of Alushinyrra." {n}She holds a gold signet up to the lamp. The finger inside it is grey and shrunken.{/n} "The rest I melt down, and the finger goes to the kitchen. Waste not."''',
       c("Continue", "token")),
    hx("token", '''{n}She turns the signet toward the lamp: a ram's head in red gold, one horn bent where somebody tried to pry it loose. Then she holds it out across the bar, finger and all.{/n}''',
       c("Continue", "token_knight", requires=(TOLD_DEAD,)),
       c("Continue", "token_plain", forbids=(TOLD_DEAD,))),
    hx("token_knight", '''"You brought me good news once, and I gave you a token, the way they do on Golarion. A lady and her knight." {n}Her voice is all honey.{/n} "I liked it so much, I thought we'd do it again. This one's from a man who told me a lie at my own bar. He won't need it."''',
       c("Continue", "token_choice")),
    hx("token_plain", '''"They tell me that on Golarion a lady gives her favourite a token. A ribbon, a glove." {n}Her voice is all honey.{/n} "We don't run to ribbons in the Delights. This one's from a man who told me a lie at my own bar. He won't need it."''',
       c("Continue", "token_choice")),
    hx("token_choice", '''"Go on, lover. It's a present."''',
       c("[Take the ring, finger and all.]", "took", flags=(RING,)),
       c('"Not with the finger in it."', "finger", flags=(RING,)),
       c('"Keep your dead men\'s jewellery."', "refused", flags=(RING_REFUSED,))),
    hx("took", '''{n}She watches you close your hand on the ring and finger. Her good eye brightens.{/n} "Oh, I like you. Most people flinch."
{n}She sweeps the rest of the tray into a bag.{/n} "Wear it to my bar. The regulars saw me pry that bent horn off its last owner. They'll enjoy seeing who has it now."''',
       c('"That\'s why I took it."')),
    hx("finger", '''{n}She slides the finger out with a claw and drops it on the tray.{/n} "Squeamish. You're allowed one or two scruples, lover."
{n}She wipes the ring on her sleeve and puts it in your palm.{/n} "There. Clean. My regulars will still know it. They watched me pry that bent horn off its last owner."''',
       c('"That\'s why I took it."')),
    hx("refused", '''"Then I'll sell it to someone who isn't particular." {n}She drops it back on the tray without offence, and without interest.{/n} "You're a strange one, honey. You'll walk into my house of your own will and drink my wine, but you won't wear a dead man's ring." {n}She shrugs.{/n} "Everyone draws the line somewhere. I like to know where."''',
       c('"Now you know."'))],
    requires=(LABYRINTH,), delay=24)


beat(PREDECESSOR, "Her riches", '"Why did you want Chivarro gone?"', [
    hx("start", '''"Want her gone?" {n}Herrax arches the brow on her good side.{/n} "Honey, everyone wanted her gone. Chivarro held this chair a very long time, and nobody bothered her, because everyone knew who she was. Then Baphomet's minion came up the stairs, the bleeding one, Minagho, and they fought, oh, how they fought, and then they fell in love, and then they walked around my hall hand in hand cooing at each other like doves."
"I stood behind that chair a long while, lover. Long enough to learn how it's held. You don't hold it with a lover on your arm."''',
       c("Continue", "asked", requires=(ASKED_KILL,), forbids=(TOLD_DEAD, MC_FAVOR)),
       c("Continue", "told", requires=(TOLD_DEAD,), forbids=(MC_FAVOR,)),
       c("Continue", "deposit", requires=(MC_FAVOR,)),
       c("Continue", "unasked", forbids=(ASKED_KILL, TOLD_DEAD, MC_FAVOR))),
    hx("asked", '''"I asked you for her head, you'll remember. My gratitude would have known no bounds." {n}She studies you.{/n} "And you're still wearing that look. Polite reluctance. Mortals wear it the way my girls wear perfume, to cover something."''',
       c("Continue", "riches")),
    hx("told", '''"And then you came to my bar and told me she was dead, and I called you my knight in shining armour." {n}She laughs, delighted all over again.{/n} "I meant it, too. I don't often mean things. Remember that I did, once."''',
       c("Continue", "riches")),
    hx("deposit", '''"And then you came to my bar and put a deposit on her corpse. 'One Chivarro, forever.'" {n}She taps the scar on her lip with one claw.{/n} "I still haven't decided whether that was the most romantic thing anyone's done in this house or the most elegant fraud. Whichever it was, you still owe me a favour for it, lover. That's a separate line. When I collect, I'll collect it once."''',
       c("Continue", "riches")),
    hx("unasked", '''"Somebody put her out in the street for me, and I never had to ask. That's the best kind of gift, honey. The kind nobody can send you a bill for."''',
       c("Continue", "riches")),
    hx("riches", '''{n}She spreads her hands to take in the hall, the stair, the girls, the gold on the bar.{/n}
"I inherited her riches, lover. Not her debts. Anyone who comes up my stairs with a note of Chivarro's in his fist can go down to the Lower City and ask her for it, wherever she is, in whatever state."''',
       c('"And her enemies?"', "enemies"),
       c('"Do you ever miss her?"', "miss")),
    hx("enemies", '''"Ah." {n}Her smile goes thin at the torn side.{/n} "Those, I inherited. Every one who hated her now hates me, and a few who liked her hate me more. That's the price of the chair."
"The worst of them sleeps in my house and brings me my wine." {n}She lifts her cup, and looks past it, across the hall, to where a tall incubus is lounging against a pillar and smiling at nothing.{/n} "But you've met Rokhorn."''',
       c('"I have."')),
    hx("miss", '''{n}She actually thinks about it, which you did not expect.{/n}
"I miss hating her. That was good, clean work, and it filled the days. Now I have to hate a lot of smaller people, and it's tiring." {n}She sips.{/n} "Minagho I don't miss at all. She bled on everything. Do you know what Baphomet's blood does to silk?"''',
       c('"I can guess."'))],
    requires=(FIRST_PRICE,), delay=24)


beat(THE_LADY, "Whose she is", '"Who does a madam answer to, in Alushinyrra?"', [
    hx("start", '''"Everyone answers to the Lady in Shadow, honey. Every succubus in this city is hers, whether she's ever looked at us or not. She's queen of all of us. She doesn't have to claim us; she simply hasn't bothered to let us go."''',
       c("Continue", "claimed", requires=(CLAIMED,)),
       c("Continue", "lady", forbids=(CLAIMED,))),
    hx("claimed", '''"I hear she said as much to your own pet succubus, in her palace, in front of you. 'This demon follows you around only because I allow it.'" {n}Herrax's laugh is soft.{/n} "That's our queen. She never takes anything back. She only reminds you she could."''',
       c("Continue", "lady")),
    hx("lady", '''"She hasn't claimed me. She hasn't needed to. I pay what's due to her people, I don't sell anything she's using, and I keep my house quiet when her court's in a mood." {n}She shrugs.{/n} "In return she forgets I exist. That's the best a madam can hope for from a queen."''',
       c('"And Rokhorn? Does she remember him?"', "willodus")),
    hx("willodus", '''"Rokhorn had a friend at court. Willodus, her court magician. He used to come up my stairs twice a week for my boy and pay double for the privilege." {n}She turns her cup.{/n}
"In light of recent events, Willodus no longer visits here. Don't ask me which events. I don't gossip about the court. Not for free."''',
       c("Continue", "willodus_told", requires=(WILLODUS,)),
       c("Continue", "patronless", forbids=(WILLODUS,))),
    hx("willodus_told", '''"I think I told you that already, when you first asked for him. I tell everyone. It's good for business to have people know my boy's available."''',
       c("Continue", "patronless")),
    hx("patronless", '''{n}She looks over at the pillar where Rokhorn lounges.{/n}
"So now he has nobody. No patron, no court, no one to pay his healers the next time he gets clever. A man with no patron and a grudge is a man who'll buy anything a clever stranger sells him, lover." {n}She drinks.{/n} "Remember that. I have."''',
       c('"Does the Lady know what goes on in your house?"', "knows"),
       c('"I\'ll remember."')),
    hx("knows", '''"The Lady knows everything that amuses her." {n}Herrax sets down the cup.{/n} "Rokhorn doesn't amuse her. Neither, at the moment, do I. That's the safest either of us has ever been."''',
       c('"Then let\'s not amuse her."'))],
    requires=(LABYRINTH,), delay=24)


# --- The eye: three stories, never settled (what burned it is not in canon; these are her lies). -------------------------

beat(EYE_ONE, "The eye, once", '"Your eye. Who did that?"', [
    hx("start", '''{n}Herrax touches the ring of old burns round her blind eye, lightly, with one fingertip, the way you would touch the edge of a coin to see if it had been clipped.{/n}
"This? A priestess of Shelyn." {n}She says it at once, as though she has been waiting to be asked.{/n} "She came up my stairs with a flask of holy water under her robe and a head full of sermons, to save my girls. She saved one of them all over my face. I had her thrown into the canal. She floated, I'm told. Holy women do."''',
       c("Continue", "sosiel", requires=(SOSIEL,)),
       c("Continue", "end", forbids=(SOSIEL,))),
    hx("sosiel", '''"Your pretty cleric reminded me of her." {n}She smiles.{/n} "The one with his goddess glowing out of his chest. He stood in my hall and wondered aloud why anyone would spoil such beauty. So I told him what I tell everyone: the scars are a pinch of spice. They accentuate perfection." {n}Her good eye glints.{/n} "He wanted to heal them. Can you imagine? I'd sooner let him heal my purse."''',
       c("Continue", "end")),
    hx("end", '''"There. Now you know. It's a good story, isn't it?" {n}She sounds very pleased with it.{/n}''',
       c('"It is."'),
       c('"Is it true?"', "true")),
    hx("true", '''"Honey." {n}She pats your hand.{/n} "In this house nobody asks that. It's rude, and it's bad for trade."''',
       c('"Noted."'))],
    requires=(FIRST_PRICE,), delay=12)

beat(EYE_TWO, "The eye, twice", '"You never did tell me about the eye."', [
    hx("start", '''"Didn't I?" {n}Herrax looks surprised, and then fond, the way she looks at a guest who has come back.{/n} "Chivarro did it. The night she lost the chair. She threw her perfume bottle at me, and the perfume had something in it she'd been saving for Minagho. It burned for a week." {n}She laughs.{/n} "I still smell it when it rains. You'd think I'd hate the scent. I sleep on her cushions."''',
       c('"Last time it was a priestess of Shelyn with holy water."', "caught"),
       c('"That sounds like her."', "end")),
    hx("caught", '''{n}Her good eye widens with what might be delight.{/n} "Was it? Then that's the one I tell to paladins." {n}She tops up your cup without the slightest embarrassment.{/n}
"You were listening. Nobody listens to me, lover. They look." {n}She sets down the jug.{/n} "Now I'll have to be more careful with you."''',
       c('"Please don\'t be."')),
    hx("end", '''"Doesn't it? She had style, that one. Bad taste, and style." {n}She sips.{/n} "I'd have liked her, if I hadn't wanted her chair so much."''',
       c('"That\'s a lot to want."'))],
    requires=(EYE_ONE,), delay=24)

beat(EYE_THREE, "The eye, the third time", '"Tell me about the eye. The real one."', [
    hx("start", '''"The real one." {n}She says it back to you slowly, tasting it.{/n} "All right."
"There was a girl. I bought her from a slaver in the Fleshmarkets, a tiefling with a dyer's hands, all blue to the wrists. The night I took this chair, while everybody else was fighting, she walked up behind me with a pot from the dyers' vats, the kind that eats cloth, and threw it."
{n}She turns her face to the lamp.{/n} "I let her live. She's upstairs now. She's my best earner. She brings me my wine in the mornings, and she's never once spilt it."''',
       c("[Believe her.]", "believed", flags=(EYE_BELIEVED,)),
       c('"That\'s the third story. Which one is true?"', "which", flags=(EYE_ASKED,)),
       c('[Trickster] "None of them. You never let anyone tell you what happened to your face. Not even yourself."', "guessed",
         flags=(EYE_GUESSED,), mythic="Trickster")),
    hx("believed", '''{n}Something moves in her face, quick and gone, like a fish under dark water.{/n} "You believe that one." {n}She sounds almost curious.{/n}
"Then it's true. That's how it works, lover. In this house a story's true when someone pays for it, and you just paid for that one with the only thing I can't sell: you stopped asking." {n}She kisses the tip of her finger and presses it to the corner of your mouth.{/n}''',
       c('"Keep your stories. I\'ll keep believing them."')),
    hx("which", '''"The one that works on you." {n}She doesn't hesitate.{/n} "A priestess for paladins, a rival for romantics, and a slave girl for crusaders who want to believe a demon can spare someone."
"So you tell me, lover. Which of the three did you like best? That's the true one. It's the only true thing about any story in the Delights: who wanted it."''',
       c('"I\'ll think about it."')),
    hx("guessed", '''{n}For a heartbeat she is entirely still, and you can hear the whole hall around you: the harp, the laughter, a cup set down.{/n}
{n}Then she laughs, and it is a good laugh, low and real, the first one you've heard from her that isn't for anyone else.{/n} "Careful, lover." {n}She leans in, close enough that the burn round her eye is all you can see.{/n} "People who guess the madam's secrets end up on the tray with the other forgotten things." {n}She does not tell you whether you guessed right. She does not move away, either.{/n}''',
       c("[Stay where you are.]"))],
    requires=(EYE_TWO,), delay=24)


beat(ARENA, "The arena crowd", '"The hall is emptier tonight."', [
    hx("start", '''"Battlebliss." {n}Herrax waves a hand at the empty couches.{/n} "There's a bout on in the arena, and half my guests have gone down to watch vavakia tear each other apart, and the other half have gone down to bet on it. They'll all be back after midnight, drunk and bloody and rich or ruined, and either way they'll want company."
"The arena's the best friend a madam ever had, lover. It empties my house, and then it fills it."''',
       c('"Do you ever go?"', "go"),
       c('"And the Sinners? I don\'t see them."', "sinners")),
    hx("go", '''"Me? To sit on a stone bench with a crowd of shrieking brutes and watch meat fight meat?" {n}She looks sincerely pained.{/n} "Honey, I send my boys. Every one of them, when the crowd's thick. It's where the money is. The pickpockets I pay for, the bets I fix, the champions I buy for the night after."
"Half my house goes down to the arena on a big night, and nobody on the private floor but me and the lamps."''',
       c("Continue", "note")),
    hx("sinners", '''"The Sinners are with a client in the Upper City. They generally are. They're the best girls I have, and the most expensive, and a client who can afford all three at once doesn't usually let them go home until he runs out of money or blood." {n}She smiles.{/n}
"The house is always thinnest on arena nights. The girls up in the Upper City, the boys down at the bouts. Nobody on the private floor but me and the lamps."''',
       c("Continue", "note")),
    nar("note", '''{n}She says it lightly, as if she has said it a hundred times. Perhaps she has. Across the hall, Rokhorn is lounging against his pillar, and he has heard it too, and his eyes have stopped on her for a moment longer than they need to.{/n}''',
       c('"Doesn\'t that worry you? Alone on the private floor?"', "worry"),
       c("[Say nothing.]", "end")),
    hx("worry", '''"Worry?" {n}She leans back on her couch and lets her ragged wings fall open.{/n} "I'm the madam, lover. The strongest thing in this house. That's how I got the chair." {n}She looks at you from under her lashes.{/n} "And I've never been alone in my life. I only let people think so when it's useful."''',
       c('"I\'ll remember that."')),
    hx("end", '''"There. You're learning. Silence is cheap and it never needs mending." {n}She pats the couch beside her.{/n} "Sit. Tell me something that'll make me laugh before the brutes come back."''',
       c('[Sit.] "There was a fool king in Drezen..."'))],
    requires=(LABYRINTH,), delay=24)


# --- After the night is set: Rokhorn, sounded out; the lie, rehearsed; the eve. -----------------------------------------

SCENES.append(scene(SOUNDING, "Hot stuff", "Herrax", 4, '"Tell me about yourself, Rokhorn."', [
    rk("start", '''{n}Rokhorn grins down at you.{/n} "Hello again, hot stuff. The madam sent her girl away to talk to you. I saw that." {n}He leans closer, sniffing without shame.{/n} "What did you offer her? She doesn't send the girls away for a pretty face. I tried."''',
       c('"Maybe I\'m nobody\'s."', "nobodys"),
       c('"She likes me. It\'s a novelty."', "novelty")),
    rk("nobodys", '''"Nobody's nobody's in Alushinyrra." {n}He laughs.{/n} "Everyone's somebody's, or something's. You just haven't found out whose yet. That's the fun of a new face."''',
       c("Continue", "read")),
    rk("novelty", '''"Everything's a novelty to her for a week." {n}He shrugs his heavy shoulders.{/n} "Then she prices it, and then she sells it, and then she forgets it existed. Ask me how I know."''',
       c("Continue", "read")),
    rk("read", '''{n}He lifts one hand, the claws half out, and turns it in the lamplight in front of your face.{/n}
"You know what I like best about mortals, hot stuff? You bleed so easily. One scratch gives me a taste. Then, if I like, I speak the words and read your fate: what you want, what you fear, what you're lying about. A demonologist taught me the trick once, to buy my attention." {n}His smile widens.{/n} "Most of my guests pay extra for it. Some of them pay extra for me not to."''',
       c('"Then I\'ll keep my cheeks to myself."', "end"),
       c('"And what do you want, Rokhorn?"', "wants")),
    rk("wants", '''"Everything." {n}He says it with total sincerity.{/n} "The whole world, on its knees, begging me not to stop. But I'd settle, for now, for a chair." {n}His eyes go across the hall, to the dais, and come back to you, merry and flat.{/n} "You didn't hear that. And if you did, you'll forget it. Everyone in this house forgets things for me, eventually."''',
       c("Continue", "end")),
    rk("end", '''"Come back when you're ready to stop talking, hot stuff." {n}He stretches, and his shoulders crack.{/n} "Once you're begging, I decide what you're begging for. You'll thank me for it after. They all do."''',
       c('"We\'ll see."'))],
    requires=("trickster.ever", MADAM, MET, PRIMED), forbids=(BAIT, BLOWN, CLOSED), delay=0, last=4, optional=True,
    Relationship=REL, AnswerLists=[ROK_LIST], NativeReturnCue=ROK_RET))


# Authored blood-art limit (Cue_0193): a taste supplies blood; spoken divination reads fate.
# Authored con detail: the spite grievance is performed here, before the seller leaves for Rokhorn.
beat(REHEARSAL, "The lie, rehearsed", '"Help me get the lie right."', [
    hx("start", '''"Lie?" {n}Herrax looks shocked.{/n} "There isn't going to be a lie, lover. There's going to be a truth with one hole in it. That's harder. Sit."
{n}She clears the bar with her forearm, scattering nutshells, and sets down three coins in a row: the house, the arena, the private floor.{/n}
"Everything you tell him will be true. The arena crowd. The empty floor. The coin. He'll check every piece, because he's not a fool, only greedy. So the only thing you have to decide is why you're selling. That's the piece he can't check. That's the piece he'll believe or won't."''',
       c('"Greed. I want a quarter of the house."', "greed"),
       c('"Spite. Give me something to be angry about."', "spite"),
       c('"Hunger. I want you, and you won\'t sell."', "hunger")),
    hx("greed", '''"Mortals always want the ledger." {n}She nods slowly.{/n} "He'll believe that one fastest, because it's how he thinks: everything's a cut of something. Ask for too much and he'll haggle you down, and when you let him, he'll think he's won." {n}She pushes the house coin toward you.{/n} "Ask for a third. Let him give you a quarter. Look sulky about it."''',
       c('"And if he offers me a fifth?"', "greed2")),
    hx("greed2", '''"Then walk away, and he'll run after you with a quarter." {n}She smiles with the whole side of her mouth.{/n} "Nobody runs after a seller who doesn't care, lover. They run after one who might sell to someone else. Tell him Chivarro's old friends in the Lower City would pay more. They wouldn't. He doesn't know that."''',
       c("[Take the house coin.]", "done", flags=(LIE_GREED,))),
    hx("spite", '''"The wounded guest." {n}Her good eye gleams.{/n} "He'll believe that. He has enough grudges to recognise one."
{n}She pushes the arena coin toward you and lowers her voice.{/n} "Leave angry when I laugh. Don't do it prettily. Rokhorn will be watching for that."''',
       c('"You\'ll enjoy that."', "spite2")),
    hx("spite2", '''{n}Herrax turns toward the couches and raises her voice.{/n} "Listen to this, girls. A crusader wants the madam. Couldn't afford the Sinners, so asked for me."
{n}The nearest girls laugh. Herrax lets them look you over, then laughs with them, eyes bright, mouth cruel.{/n} "Go on, lover. Tell your soldiers what you can buy with crusader glory."
{n}Under cover of their laughter, she nudges the arena coin into your hand.{/n} "There," {n}she murmurs.{/n} "Take that to my boy."''',
       c("[Take the arena coin.]", "done", flags=(LIE_SPITE,))),
    hx("hunger", '''{n}She is quiet a moment, and the torn side of her mouth doesn't move.{/n}
"That one's dangerous, lover. It's the one he'll believe best, because it's the one he'd sell himself. The keeper who's beyond everyone's reach, and the mortal who can't have her, and the incubus who promises to put her on the menu." {n}She pushes the floor coin toward you.{/n}''',
       c('"Why dangerous?"', "hunger2")),
    hx("hunger2", '''"Because when you tell it, he'll look at your face, and he'll see whether it's true." {n}She watches you.{/n} "So make sure you know the answer before you go to him. I'd hate for you to find out in front of him."''',
       c("[Take the floor coin.]", "done", flags=(LIE_HUNGER,))),
    hx("done", '''{n}She sweeps the other two coins back into her purse.{/n}
"And whatever else he says, don't let him scratch you. Blood first, then the words that read your fate. You'll hear his voice change. By then you've lost the sale. Keep his claws off you; don't give him a chance to start." {n}She taps your cheek with one finger, exactly where a claw would go.{/n} "Keep your face, lover. I'll need it after."''',
       c('"I\'ll keep it."'))],
    requires=(PRIMED,), forbids=(BAIT, BLOWN, LIE_GREED, LIE_SPITE, LIE_HUNGER), delay=0)


beat(EVE, "The eve", '"About the night you named."', [
    hx("start", '''{n}Herrax is sitting on the edge of the dais with the curved knife across her knees and a whetstone in her hand. She doesn't look up. The stone goes along the edge, and back, and along.{/n}''',
       c("Continue", "sold", requires=(BAIT,)),
       c("Continue", "blown", requires=(BLOWN,), forbids=(BAIT,))),
    hx("sold", '''"He's been strutting since you left him." {n}She sounds amused.{/n} "Calling the girls 'my dears' where I can hear it. Counting my furniture. He had the Glowworm measure the dais for new cushions." {n}The stone goes along the edge.{/n}
"You did well, lover. He believes all of it, and there wasn't a lie in the whole thing. I watched him walk away from you with my coin down his belt, and I wanted to lick the lie off your mouth in front of him."''',
       c('"Where do you want me when it starts?"', "where")),
    hx("where", '''"At my right hand, one step down. Where Chivarro's favourites used to stand." {n}She tests the edge on a hair from her own head, and the hair parts.{/n}
"Don't speak unless I speak to you. Don't smile when he comes through the arch. Don't flinch when I offer you the knife." {n}Now she looks up.{/n} "I will offer it. The seller has the right of the first cut; it's a custom of my house. What you do with it is up to you. What the house thinks of you afterwards is up to them."''',
       c('"And what will you think?"', "think")),
    hx("think", '''"Me?" {n}She goes back to the stone.{/n} "I'll think whatever's true. It's a terrible habit. I've never managed to break it."''',
       c('"Goodnight, Herrax."')),
    hx("blown", '''"You let him taste you." {n}Her voice is perfectly pleasant, and the stone does not stop.{/n}
"The whole house heard him. 'The favoured guest is selling the madam's floor.' My girls have been whispering behind their hands since he shouted it, and three of my boys have asked, very politely, whether the chair is still mine." {n}Along the edge, and back.{/n}''',
       c('"I\'m sorry."', "sorry"),
       c('"He read me. I didn\'t let him."', "sorry")),
    hx("sorry", '''"Keep your sorry. It's no use to me." {n}Now she looks up, and her good eye is cold as a coin.{/n}
"When the house gathers, I cut him in the great hall, where they heard him, under the lamps. And before I do, you'll walk the length of my hall in front of all of them. If you still have my coin, you'll put it in my hand. If you've lost it, you'll show them your empty hands. After that, lover, we'll see what's left to talk about."''',
       c('"I\'ll be there."'))],
    requires=(), forbids=(LESSON,), delay=6, RequiresAnyGroups=[[BAIT, BLOWN]])


# --- More of the house, before or around the chain (optional). -----------------------------------------------------------

beat(B + "the_girl_upstairs", "Blue to the wrist", '"Who brings your wine in the mornings?"', [
    nar("start", '''{n}Herrax doesn't answer. She lifts two fingers, and a girl comes down the stair with a jug on a tray: a tiefling, slight and neat, with small horns filed smooth. Her hands are stained blue from the fingertips to the wrist, the deep, permanent blue of the dyers' vats, the kind that never washes out.{/n}
{n}She fills the madam's cup without spilling a drop, and yours, and stands back with the tray against her hip.{/n}''',
       c('[Ask the girl] "Did you ever throw anything at her?"', "ask_girl"),
       c("[Say nothing, and drink.]", "drink")),
    n("ask_girl", "Narrator", '''{n}The girl looks at you, and then at Herrax, and then back at you, with the same flat, polite attention.{/n}
"The madam says I threw a pot at her," {n}she says.{/n} "If the madam says so."
{n}Herrax laughs, delighted, and dismisses her with a flick of two fingers. The girl goes back up the stair without hurrying.{/n}''',
       c("Continue", "after")),
    hx("drink", '''"Good girl." {n}Herrax watches her go back up the stair.{/n} "Best earner in the house. Never spills. Never asks for anything. Never, ever turns her back on me." {n}She sips.{/n} "Neither do I, on her. It's the most honest arrangement in the Delights."''',
       c("Continue", "after")),
    hx("after", '''"So now you've met her. Does it make the story truer?" {n}Her good eye is bright with mischief.{/n} "Blue hands, honey. Half the girls from the Fleshmarkets have them. The dyers buy slaves by the cartload and use them up."
{n}She sets her cup down.{/n} "Or she threw a pot at me. Or a priestess did, or Chivarro. You'll never know. I'll never tell you. And you'll keep wondering, every time you look at my face, which means you'll keep looking at it." {n}She tilts her head.{/n} "Did you think I tell those stories for nothing?"''',
       c('"No. Nothing in this house is for nothing."'))],
    requires=(EYE_THREE,), delay=24)


beat(B + "honeyed_tongue", "Honeyed tongue", '"One of your girls keeps looking at me."', [
    hx("start", '''"Morevet." {n}Herrax doesn't need to look.{/n} "She's been looking at you since you started coming up my stairs without paying. It offends her professionally. Everyone in this house is for sale, and she can't bear to watch a guest who isn't buying."
{n}Across the hall, a succubus with a mouth like a split fig is watching you over the rim of a cup. When she sees you looking, she runs the tip of her tongue slowly along her lower lip, and it is longer than a tongue should be, and it forks.{/n}''',
       c('"Should I be worried?"', "worried"),
       c('"Would you mind, if I bought her?"', "mind")),
    hx("worried", '''"Of Morevet?" {n}Herrax laughs.{/n} "Only if you like breathing. She's insatiable, lover, and she has no shame, and she's the only girl in the house I've ever had to carry guests out for. Twice in one week." {n}She sips.{/n} "She'll try to get you alone on the stair. She wants to find out what I see in you. When she can't, she'll make up something filthy and tell it to the whole house. I'll let her. It's good for business."''',
       c("Continue", "end")),
    hx("mind", '''"Mind?" {n}She looks at you as if you'd asked whether she minded the weather.{/n}
"Honey, I'm a madam. I don't mind anybody buying anything in my house. Buy Morevet, buy the Sinners, buy the whole Upper City if your crusade can afford it. Keep whoever you like in Drezen." {n}She sets down her cup.{/n}
"The only thing I'd mind is if you ever tried to pay me. And the only thing Morevet would mind is you coming out of her room alive."''',
       c("Continue", "end")),
    hx("end", '''{n}Morevet, on the far couch, raises her cup to Herrax in a mocking little toast. Herrax raises hers back, and smiles at her the way a cat smiles at a bird in a very small cage.{/n}
"She knows who owns her," {n}Herrax says, not lowering her voice.{/n} "It's the only thing she's ever been shy about."''',
       c('"Remind me never to annoy you."'))],
    requires=(LABYRINTH, COMMITTED), delay=24)


beat(B + "the_lesson_room", "A thief in the house", '"Something\'s happened."', [
    nar("start", '''{n}Two of the boys are holding a young incubus by the arms at the foot of the dais. He is hardly more than a boy himself, with the sullen beauty they all have, and one of his eyes is already swelling shut. On the tiles in front of him lie three gold rings and a purse.{/n}
{n}Herrax is sitting above him with her chin on her hand, looking bored.{/n}''',
       c("Continue", "thief")),
    hx("thief", '''"He stole from the tray." {n}She says it to you, not to him.{/n} "The forgotten things. Things that belong to the house. He thought nobody counted them." {n}Her good eye moves to the boy.{/n} "I count everything, sweet. You know that. You've watched me do it for two years."
"The question is what to do with him. And since you're here, lover, and you're not one of mine, you can tell me what a crusader does with a thief. I'm curious."''',
       c('"Cut off a finger. For the tray."', "finger"),
       c('"Turn him out. Let the street have him."', "street"),
       c('"It\'s your house. It\'s your lesson."', "hers")),
    hx("finger", '''"For the tray." {n}She laughs, genuinely charmed.{/n} "You do learn quickly."
{n}She nods, and one of the boys draws a knife, and the thief screams before it touches him. She lets him scream. When it's done, she picks the finger up off the tiles herself and sets it on the tray beside the rings.{/n} "There. Now the tray is square, and so is he. He'll steal again, you know. But he'll count first."''',
       c("[Watch him dragged away.]", "end")),
    hx("street", '''"The street." {n}She considers it.{/n} "That's a mortal's answer. Out of sight, out of the ledger."
"In Alushinyrra the street would eat him in a night, lover, and I'd lose everything I've spent on him. That isn't a punishment; that's a loss." {n}She waves a hand.{/n} "Take him to the cellar. Three days, no water. Then he goes back to work, and every girl in the house knows why he's thirsty."''',
       c("[Watch him dragged away.]", "end")),
    hx("hers", '''"Mine." {n}She seems pleased by that.{/n} "Yes. It is."
{n}She leans down from the dais, takes the boy's chin in her fingers and turns his face to the lamp, gently, the way she turned yours the night she priced you.{/n} "Look at my face, sweet. Look at every mark on it. That's what the chair costs. You thought you could take a little off the tray and nobody would notice." {n}She lets him go.{/n} "Cellar. Three days. Then work."''',
       c("[Watch him dragged away.]", "end")),
    hx("end", '''{n}The hall has watched all of it. It goes back to its wine.{/n}
"You see, lover, the trick isn't cruelty. Any vavakia can be cruel." {n}She settles back on Chivarro's cushions.{/n} "The trick is being cruel in front of the right people, at the right price, exactly once. After that, they do the rest themselves."''',
       c('"I\'ll remember that."'))],
    requires=(FORGOTTEN,), delay=24)


# === Chapter 4: after the night =========================================================================================

beat(MEANS, "What reachable means", '"What does \'reachable\' mean, exactly?"', [
    hx("start", '''{n}Herrax is at the end of the bar with the takings. She doesn't look up, but she moves the ledger an inch to make room for your elbow, which in her is a speech.{/n}
"It means you can come up my stairs without paying. It means that when you ask me for something, I'll answer, and when I answer, I won't be selling." {n}She makes a mark.{/n}
"It does not mean I'll be kind. It doesn't mean I'll wait. It doesn't mean you're mine, lover, or that I'm yours. Don't ever put a ribbon on it."''',
       c('"And the rest of my life? Drezen, the crusade, the people in it?"', "rest"),
       c('"What do I owe you for it?"', "owe")),
    hx("rest", '''"Keep them." {n}She sounds surprised to be asked.{/n} "You're a crusader with a war and a bed in Drezen. Fill it with whoever you like. I'm not a wife, honey. I'm a madam. I know exactly how many hearts one mortal has room for; I've made a living off the overflow for centuries."
{n}Now she looks up.{/n} "The only thing I'd mind is if someone else ever charged you for what I give you free. Then I'd want her name, and her address, and a very sharp knife."''',
       c("Continue", "end")),
    hx("owe", '''"Nothing." {n}She says it flatly.{/n} "That's the whole point, lover. The moment you owe me, you're a customer, and I have plenty of those. You'd go on the books like everybody else, and I'd charge you interest, and one day I'd sell your debt to Rokhorn for the fun of it."
"So owe me nothing. Come up my stairs empty-handed." {n}She turns a page, and a boy by the stair who has been hovering with a purse goes white.{/n} "Not you, Lissar. You owe me eleven silver and a finger, and I'm feeling generous about the finger until midnight."''',
       c("Continue", "end")),
    hx("end", '''{n}She closes the ledger.{/n} "And when you go back to your war, you'll hear from me. Not every day. I'm not a lovesick girl with a quill. But you'll hear."
"Rokhorn will carry my letters." {n}The torn side of her mouth curls.{/n} "It's a humiliation, and he'll do it beautifully. He does everything beautifully that he can't get out of."''',
       c('"Poor Rokhorn."'),
       c('"I\'ll look forward to him."'))],
    requires=(COMMITTED,), delay=8)


beat(STAIRS, "The stairs", '"You might have warned me about the stairs."', [
    nar("start", '''{n}Herrax is waiting on her private floor, above the Delights' smoke rooms and mirrored gallery.{/n}''',
       c("Continue", 'stairs_no_coin', forbids=(COIN_HELD,)),
       c("Continue", "stairs_coin", requires=(COIN_HELD,))),
    hx("timed", '''"A quarter of an hour, lover." {n}She turns the glass over, idly.{/n} "The Sinners' last client did it in eleven, but he was running from his wife." {n}Her good eye takes you in: the breath, the flush, the sweat at your collar.{/n}
"You're out of breath." {n}She sounds very pleased about it.{/n} "I like you out of breath. You look like somebody who wanted to get somewhere."''',
       c('[Flirt] "Somebody did."', "close"),
       c('"Your labyrinth is a menace."', "menace")),
    hx("menace", '''"My labyrinth is a filter." {n}She stands.{/n} "Anybody who wants me badly enough to climb it, I'm prepared to see. Anybody who gives up on the second floor goes home with one of my girls instead, and pays for her, and thanks me." {n}She comes round the table.{/n} "You didn't give up."''',
       c("Continue", "close")),
    hx("close", '''{n}She puts a hand flat on your chest and feels your heart going under it, and she laughs, low, as if it were a joke only the two of you knew.{/n}
"There it is. The thing in your chest that burns where it shouldn't. It runs so fast when you've climbed." {n}She leans in, and you feel it again, the faint pull as she breathes you in: a thread of warmth going out of you and into her, light as a pickpocket's fingers.{/n}
{n}Her hand does not stay flat. It drags down your sternum, slow, over the sweat the climb left in your shirt, and hooks in your belt. She is close enough that the heat of her comes through the gown, and the gown is very little. The scar through her lips pulls wet and red when she smiles at what your body is doing without your leave.{/n}
"All that climbing, honey, and every step of it you were thinking about this. Don't lie. Your pulse is a worse liar than you are."
"Stay the night, and I'll send you down in the morning by the servants' stair. It's shorter. I'll never tell you where it is."''',
       c('"Then I\'ll stay."', STAIRS + ".explicit.1"),
       c('"I\'ll find it myself one day."', "find")),
    hx("find", '''"No, you won't." {n}She kisses the corner of your mouth, where the scar would be if you had hers, and then the corner of your jaw, and then your throat, open-mouthed, with a little scrape of teeth that is not an accident.{/n} "But I'll enjoy watching you try."
{n}She backs you off the top step and against the doorframe of her private floor by the belt she is already unbuckling, one ragged wing swinging shut across the stair behind you like a curtain drawn on the house. Her other hand finds yours and drags it flat against the left side of her ribs, where the beat under the skin is every bit as fast as your own.{/n}
"Feel that? You did that. Nobody climbs this far for nothing, lover, and nobody gets me like this for nothing, so we'll call it even and not mention it again."''',
       c("[Stay.]", STAIRS + ".explicit.1")),
    nar("stairs_no_coin", '''{n}Without her coin, getting to the Delights means walking the streets. Inside, the climb takes you through the smoke rooms, round the mirrored gallery, and through three doors that open onto other doors.{/n}
{n}Herrax waits at the top in a gown the colour of old wine. The little hourglass beside her has run out.{/n}''', c("Continue", "timed")),
    nar("stairs_coin", '''{n}Her coin can still bring you to the Delights' arch. It saves you the streets, not the climb: up through the smoke rooms, round the mirrored gallery, and through three doors that open onto other doors.{/n}
{n}Herrax waits at the top in a gown the colour of old wine. The little hourglass beside her has run out.{/n}''', c("Continue", "timed")),
    # Explicit brief: return to an established lover; private, not another first night.
    nar(STAIRS + ".explicit.1", "{n}She draws you away from the stair and shuts the door, keeping your hand against the quick beat beneath her ribs.{/n}", c("Continue", "return_morning")),
    hx("return_morning", '{n}By morning, the hourglass beside the door has run empty. Herrax steps over your discarded armour, already dressed, and counts a purse while you fasten your straps.{/n} "The back stair, lover. Your crusade has had long enough without you." {n}She kisses you, then calls for the boy with the keys.{/n}', c("[Go.]"))],
    requires=(COMMITTED,), delay=24)


beat(TALK, "The madam's pet", '"The house is talking about me."', [
    hx("start", '''"The house is always talking about somebody, lover. This week it's you." {n}Herrax doesn't seem displeased.{/n} "The Sinners have a bet on how long you'll last. Morevet says you're a spy for the Lady. The Glowworm says you're a fey prince in disguise, which is flattering, but she says that about the lamp-boy too."
{n}Across the hall, one of the boys at the stair, leaning on his spear, says something to his neighbour and grins. The words carry. "Madam's pet."{/n}''',
       c('"Let it go."', "letgo"),
       c('"Tell him to say it to my face."', "face"),
       c('"Your house. Your boy."', "hers")),
    hx("letgo", '''"Let it go?" {n}She considers it, head tilted.{/n} "That's a very expensive habit, lover. Every word you let go in this house comes back next week with interest."
"But all right. I'll let it go, because you asked." {n}She raises her voice, very slightly.{/n} "Did everyone hear that? The Commander lets it go." {n}The boy at the stair stops grinning.{/n} "Now they'll all be wondering what you're saving it for. That's much worse for him."''',
       c("Continue", "end")),
    hx("face", '''{n}She crooks one finger. The boy comes down the stair as if his legs belonged to someone else and stops in front of you, and he is taller than you, and pale.{/n}
"Say it again, sweet." {n}Her voice is honey.{/n} "To the Commander's face. You were so brave about it at the stair."
{n}He says it again. It takes him two tries. Herrax listens as if to music.{/n} "Good. Now go back to your post and think about how that felt, every time you want to open your mouth."''',
       c("Continue", "end")),
    hx("hers", '''"Mine." {n}She seems to enjoy the word as much as last time.{/n}
{n}She doesn't raise her voice or crook a finger. She only looks across the hall at the boy on the stair, and keeps looking. After a while he takes his spear and goes down the stairs and out of the Delights, and doesn't come back.{/n}
"I'll sell his contract to the arena in the morning," {n}she says, pleasantly.{/n} "They like the tall ones."''',
       c("Continue", "end")),
    hx("end", '''"Pet." {n}She turns the word over.{/n} "It's a small word, lover, for what you are in this house. You're the only person who comes up my stairs without paying. They don't have a word for that. They'll have to make one up."''',
       c('"What will they call me?"', "call")),
    hx("call", '''"Something filthy, I expect." {n}She smiles, and the scar pulls it crooked.{/n} "Morevet will think of it. It'll be clever, and you'll hate it, and in a hundred years it'll still be what the Delights call anyone who's too expensive to buy."''',
       c('"I can live with that."'))],
    requires=(COMMITTED,), delay=24)


beat(LAST_NIGHT, "Not goodbye", '"I\'ll be leaving the Isles soon."', [
    hx("start", '''"I know." {n}Herrax is on Chivarro's cushions with her feet up and her ragged wings hung over the back of the dais like a cloak on a chair.{/n} "The whole city is betting on when you'll leave, lover. Every demon with a stake in your crusade wants to know how much longer the purse stays open."
"Don't say goodbye, lover. It implies the account is closed. I don't close accounts."''',
       c('"Then what do I say?"', "say")),
    hx("say", '''"Nothing. You'll just go, one night, and I'll notice in the morning." {n}She shrugs.{/n} "Then I'll sell your side of the bed for a month to a very rich devil who wants to know what a crusader smells like, and it'll be the most profitable month of the year."
{n}She looks at you, and something in her face stops performing.{/n}
"And after that, Rokhorn goes up the Wound roads with my letters, and you read them, and you write back, and if you're not dead by the spring, you come up my stairs again. That's all. That's the whole contract, and there isn't any paper."''',
       c('"No paper. Agreed."', "agreed"),
       c('"And if I am dead by spring?"', "dead")),
    hx("dead", '''"Then I'll hear it from the Lady's people before your crusade does, and I'll close the Delights for one night, the first time in a thousand years." {n}She says it lightly.{/n} "It'll cost me a fortune. Don't make me do it."''',
       c("Continue", "agreed")),
    hx("agreed", '''{n}She holds out her hand. Not for a coin, not to be kissed; only to be taken.{/n}
"There. Everyone in the hall saw that," {n}she says, when you do.{/n} "The madam of the Ten Thousand Delights shook a mortal's hand on a bargain with no price in it. I'll never live it down."
{n}She does not let go. Her thumb works the hollow of your palm in a slow circle, and then she lifts your hand and sets her teeth against the heel of it, not hard, just enough to leave the print of a bite that will be gone by the time the hall has finished laughing. Her ragged wings slide down off the dais back and fold about her shoulders. Her eye, the good one, is on your mouth.{/n}
"A thousand years I have kept this house, and not once have I given a guest the thing I'm about to give you for nothing." {n}She stands, drawing you up with her, and she is flush against you before the cushions have settled, the cut of her lip hot against your cheek.{/n} "Don't say it, lover. You'll spoil it. Sex is an exchange of life forces, and I intend to take a little more than I give. You'll let me. You'll even thank me."''',
       c('"Good."'))],
    requires=(COMMITTED,), delay=48)


# --- Her refusal, while it stands: the empty sheath. ----------------------------------------------------------------------

beat(BARE_HIP, "The empty sheath", '"Herrax."', [
    hx("start", '''{n}She is at the bar, smiling at a guest from the Upper City with her whole beautiful ruined face, and she goes on smiling at him while she speaks to you.{/n}
"Commander." {n}Not lover. Not honey.{/n} "What can the Delights do for you tonight? The Sinners are free after midnight. Morevet has been asking after you. There's a new girl from the Fleshmarkets who has never seen a mortal."''',
       c('"I came to see you."', "see")),
    hx("see", '''"You've seen me." {n}She turns, finally. The bone sheath at her hip is empty. Everyone who has come up the stairs tonight has looked at it, and then at you.{/n}
"You took my knife off me in my own hall, lover. In front of my house. Do you know what they've been saying since? That the madam can be held. By the wrist, by a mortal, like a girl." {n}Her voice doesn't rise.{/n} "Three of my boys have asked me, very politely, whether the chair is still mine. I've had to answer them in ways I didn't enjoy."''',
       c('"I\'d do it again."', "again"),
       c('"I\'m sorry for what it cost you."', "sorry")),
    hx("again", '''"I know you would." {n}Something in her face that might, in a mortal woman, have been respect.{/n} "That's what makes it unforgivable. A fool I could forgive. You knew exactly what you were doing, and you did it anyway, in front of everyone." {n}She turns back to her guest.{/n} "You still have my knife. You know where I am."''',
       c('"I know."')),
    hx("sorry", '''"Keep your sorry." {n}She's already turning back to her guest.{/n} "It's no use to me. It isn't worth a copper at my bar, and it can't be seen from the stair."
"You still have my knife, Commander. You know what the house saw you take. You know where the house can see you give it back."''',
       c('"I know."'))],
    requires=(DECLINED,), forbids=(RESTORED,), delay=8)


# === Chapter 5: her letters, by the man who carries them =================================================================

# 05 §4.2: one Chapter 5 letter on any Herrax branch. Six undated documents and a parcel arrive together, by one courier
# (a single delivery). No minimum month of correspondence is required. The six later letters
# of the first build (the_healers, rokhorns_offer, the_ladys_people, the_gift, house_news, before_the_wound) are folded in
# here; their scenes are retired by gating on BUNDLE, never deleted (save references).
BUNDLE = L + "bundle"
HIDING = "noct.defeated_not_dead"             # ledger 05 row 2: after the Council, the Lady is in hiding and her court silent

post(COURIER, "The courier", [
    nar("start", '''{n}The incubus at the citadel gate at dusk has made the guard very nervous, and made two of the laundresses forget what they came out for. He wears a traveller's cloak grey with Worldwound ash, and nothing much under it, and a scar from lip to cheekbone that is not quite the one you saw made: the stitches are out, and the line is raw, and a finger's width longer than the knife left it.{/n}
{n}He carries a packet of letters tied in black ribbon, six of them, each sealed in black wax with a gold coin pressed into the seal, and under his arm a long, narrow parcel wrapped in black silk, which he holds away from his body as if it might bite. He does not talk. He puts the packet into your hands and waits in your doorway.{/n}''',
       c("Continue", "letter", flags=(BUNDLE,))),
    hl("letter", '''{n}The first letter begins without a date.{/n}
"Lover.
Rokhorn has been told that if he reads this, I'll take the other side of his face to match. He believes me. He's become very sensible.
The house is well. Better than well: since the night, nobody has so much as looked at my chair. The boys sweep the dais twice a day, and they sweep round the stain. I've told them to."''',
       c("Continue", "letter_cut", requires=(KNIFE_TAKEN,)),
       c("Continue", "letter_handed", requires=(HANDED,), forbids=(KNIFE_TAKEN,)),
       c("Continue", "letter_restored", requires=(RESTORED,), forbids=(KNIFE_TAKEN, HANDED)),
       c("Continue", "letter_end", forbids=(KNIFE_TAKEN, HANDED, RESTORED))),
    hl("letter_cut", '''"Every guest asks about his face, now, and I tell them the favoured guest did it, with my knife, where I pointed. They look at him, and then they look at me, and then they're very polite for the rest of the evening. You've made my house quieter than it's been in a century. I'd pay you for it, if you'd let me."''',
       c("Continue", "letter_end")),
    hl("letter_handed", '''"Every guest asks about his face, now, and I tell them I did it, with the knife the favoured guest handed me back. That's the part they can't make sense of. Everyone keeps a knife they're handed. They look at him, and then at me, and they go away thinking about it. Good. Let them think."''',
       c("Continue", "letter_end")),
    hl("letter_restored", '''"Every guest asks about his face, now, and I tell them the truth: I cut it a night late, because a mortal held my wrist, and then that mortal gave me back my knife in front of the Sinners. Half of them think I've gone soft. The other half have stopped asking for credit. I'll take that bargain."''',
       c("Continue", "letter_end")),
    hl("letter_end", '''"Write back. Tell me what a crusade eats for breakfast, and whether your paladins pray before or after. Tell me something I can laugh at. You'll get my letters when I have enough of them to be worth the road; I don't send a courier every week like a girl writing to her soldier. Rokhorn will wait. He's very good at waiting now.
H."''',
       c('[Write back warmly] "I miss your stairs."', "b_healers", flags=(REPLY_WARM,)),
       c('[Write back briefly] "The war goes on. So do I."', "b_healers", flags=(REPLY_COOL,)),
       c('[Write back something filthy about the dais.]', "b_healers", flags=(REPLY_CRUDE,))),
    rl("reply", '''{n}Rokhorn takes your answers between two claws and tucks them away without looking at them. At the door he stops, and turns his ruined face toward you, and for the first time speaks.{/n}
"Hello, hot stuff." {n}The raw scar pulls. He does not smile.{/n} "Every word of it was true, you know. That's what I can't stop thinking about."''',
       c("[Let him go.]", "b_offer"), *discovery_entry("b_")),
    # --- The rest of the packet: the healers, the Lady's people, the house, the parcel, the last letter. ---
    nar("b_healers", '''{n}The second letter explains his face before you have finished wondering about it.{/n}''',
       c("Continue", "b_healers2")),
    hl("b_healers2", '''"Lover.
You'll have noticed his face by now.
He found a healer. A little witch in the Lower City who didn't know whose work she was undoing, and was greedy enough not to ask. He paid her with a ring off my tray, which was stupid of him, since I count the tray.
She's on the tray herself now. Some of her. And I opened his cheek again along the same line, a little longer, so he'll remember that it's mine, not his, and not the healers'. He took it very well. He's learning."''',
       c("Continue", "b_cheek", requires=(CHEEK,)),
       c("Continue", "b_lady", forbids=(CHEEK, HIDING)),
       c("Continue", "b_lady_hiding", requires=(HIDING,), forbids=(CHEEK,))),
    hl("b_cheek", '''"And that reminds me. Your cheek. His claw. Don't you dare let your priests near it, honey. Every guest in my house has heard how the favoured guest walked the length of my hall with his mark on your cheek, and I want it there when you come back. I'll know if it's gone. You've never seen me disappointed. Keep it that way."''',
       c("Continue", "b_lady", forbids=(HIDING,)),
       c("Continue", "b_lady_hiding", requires=(HIDING,))),
    hl("b_lady", '''{n}The third seal is pressed crooked, as if in a hurry.{/n}
"Lover.
Two of the Lady's people came up my stairs last night. Not guests. They don't come as guests. They sat on my best couch and drank my best wine and asked me, very politely, about the mortal who climbs my labyrinth without paying.
Every succubus in the city belongs to the Lady in Shadow. She doesn't have to claim us; she only has to remember us. Last night she remembered me.
I told them the truth. It's the only thing the Lady's people can't make use of. You are a guest of my house; you pay nothing and buy nothing, and nothing of mine is for sale to you, so there's nothing of mine they can buy from you either. They went away to tell her they didn't understand it. When the Lady is amused, honey, it's best to be very far away. You are. I'm not.
Is there anything between you and the Lady I should know about, before they come back? Put it in your answer. I don't like being surprised in my own house."''',
       c("Continue", "b_news")),
    hl("b_lady_hiding", '''{n}The third seal is pressed crooked, as if in a hurry.{/n}
"Lover.
The palace is dark. No music from the Lady's windows, no couriers, no summonses; the whole Upper City is holding its breath and pretending not to. They say she took a beating at some council of lords and has gone to ground. Nobody says who gave it to her. Everybody looks at me when they don't say it, because everybody knows who climbs my stairs without paying.
Two of her people came up my stairs last night. Not on her business: she isn't answering them either. On their own account, looking for a new roof before somebody else's knife finds them. They asked me, very politely, about the mortal who climbs my labyrinth for free, and whether the mortal's friends might be hiring.
I sent a girl to the palace with a question of my own. She came back with it unopened. So I'll ask you instead. Is there anything between you and the Lady I should know about? Put it in your answer. I don't like being surprised in my own house, and I like it least when the surprise is a Demon Lord's grudge sitting on my best couch."''',
       c("Continue", "b_news")),
    hl("b_news", '''{n}The fourth is three pages in the round, unhurried hand.{/n}
"The house news, since you never ask for it and always read it.
Morevet has invented a word for you. I won't write it down. It's very clever and very filthy and every girl in the house uses it now, even the Sinners, who are too expensive to use anyone's words but their own. When you come back, someone will say it to your face, and you'll know it's you.
The Glowworm drank a devil under the table on Oathday and he signed over his house to her by mistake. We're all very proud."''',
       c("Continue", "b_news_warned", requires=(WARNED,)),
       c("Continue", "b_news_white", requires=(SENT,), forbids=(WARNED,)),
       c("Continue", "b_news_empty", forbids=(WARNED, SENT))),
    hl("b_news_warned", '''"You'll want to know about the white room. You told me someday someone would come for them. Nobody has. But one of them came to me, of her own accord, the one who looked up when you were there, and asked me to teach her.
I told you, lover. They walk back up the stairs once they've tasted the cold. Some of them never even need to go out in it."''',
       c("Continue", "b_gift", forbids=(BET_LOST,)),
       c("Continue", "b_debt", requires=(BET_LOST,))),
    hl("b_news_white", '''"The white room is coming along. Since you left, one of the girls came to me of her own accord and asked to be taught, which is the first real lesson and the only one that matters. I was very, very careful with her. I always am."''',
       c("Continue", "b_gift", forbids=(BET_LOST,)),
       c("Continue", "b_debt", requires=(BET_LOST,))),
    hl("b_news_empty", '''"The white room is still empty. I've had an offer on it from a devil who wants it for a ledger room, which is an insult I'm saving to repay. It will have girls in it by the spring. It always does."''',
       c("Continue", "b_gift", forbids=(BET_LOST,)),
       c("Continue", "b_debt", requires=(BET_LOST,))),
    hl("b_debt", '''"And you still owe me a thousand from the Battlebliss. I've thought of something.
When you come up my stairs in the spring, you'll spend one night behind my bar, in an apron, pouring for my guests, and you'll smile at every one of them, and I'll keep the tips. I've already told the house. Morevet is selling places at the bar. You'd be flattered what they're fetching."''',
       c("Continue", "b_gift", flags=(BET_COLLECTED,))),
    nar("b_gift", '''{n}The fifth letter is tied to the parcel. Inside the black silk is a knife beside a sheath of worked bone: thin, curved, and so sharp that the silk has parted where the edge touched it. It is not her knife. It is its twin.{/n}''',
       c("Continue", "b_gift_letter")),
    hl("b_gift_letter", '''"Lover.
I had it made by the same smith who made mine, a salamander in the Lower City who works in bone and demon-iron. He wanted a price. I paid it. Don't ask what."''',
       c("Continue", "b_gift_cut", requires=(KNIFE_TAKEN,)),
       c("Continue", "b_gift_handed", requires=(HANDED,), forbids=(KNIFE_TAKEN,)),
       c("Continue", "b_gift_restored", requires=(RESTORED,), forbids=(KNIFE_TAKEN, HANDED)),
       c("Continue", "b_gift_end", forbids=(KNIFE_TAKEN, HANDED, RESTORED))),
    hl("b_gift_cut", '''"It's for the hand that did what it was told and didn't shake. Every madam should have one hand in the world she trusts with a knife. I've decided mine is attached to a crusader. It's absurd. I've stopped arguing with it."''',
       c("Continue", "b_gift_end")),
    hl("b_gift_handed", '''"It's for the hand that gives knives back. Everyone keeps a knife they're handed; you didn't. So here's one you'll have to keep, since it's a gift, and I don't take gifts back. That's the trick of it, honey. Now you'll have to find out what you do with a knife you can't return."''',
       c("Continue", "b_gift_end")),
    hl("b_gift_restored", '''"It's for the hand that held my wrist in my own hall and then walked out in front of the Sinners and gave my knife back. I want that hand armed. If anyone ever holds you by the wrist, lover, I want them to regret it, and I want to hear how."''',
       c("Continue", "b_gift_end")),
    hl("b_gift_end", '''"Don't wear it where your paladins can see. They'll ask where it came from, and you'll have to tell them it came from a brothel in the Abyss, and they'll pray for you, and it'll be very tedious for everyone.
H."''',
       c("[Buckle it on.]", "b_last", flags=(KNIFE_GIFT,)),
       c("[Wrap it in the black silk and put it away.]", "b_last")),
    hl("b_last", '''{n}The last letter is sealed twice, and on the outside, in the round hand, three words: Read this last.{/n}
"Lover.
The whole city says you'll go into the Wound itself before the year is out. There are bets. I have placed one. I won't tell you which way.
The girls write to their men sometimes, and I read the letters first, of course, and they're all the same: I'll wait, I'll pray, I'll never love another. I won't wait, I don't pray, and I've had hundreds. So those are out.
Here is what I have instead. A house full of things that can be bought, and a chair that can be taken, and a face that tells everyone exactly what I did to keep both. And one person who comes up my stairs without paying."''',
       c("Continue", "b_last2")),
    hl("b_last2", '''"If you die in the Wound, I'll close the Delights for one night. Everyone in Alushinyrra will know why, and they'll say the madam's gone soft, and I'll collect from every one of them who says it to my face.
If you live, come up my stairs in the spring. Don't bring a coin. You'll have to reach.
H.
P.S. Don't let anyone scratch you."''',
       c("[Keep the letter inside your armour.]", "reply"),
       c("[Burn it in the brazier, so no one else ever reads it.]", "reply")),
    # --- His offer, in person, in the rain (after the packet). ---
    rl("b_offer", '''{n}Rokhorn follows you into the square instead of taking the south road. In the cold rain, he draws close enough to speak without the sentries hearing.{/n}
"She doesn't know I've waited." {n}His voice is low and quick, and the scarred side of his mouth hardly moves.{/n} "You sold me once, hot stuff, and I paid for it with my face. Twice, now. So I know what you're worth. I'm here to make you an offer."''',
       c('"Go on."', "b_offer2"),
       c('"No."', "b_offer_first")),
    rl("b_offer_first", '''"You haven't heard it." {n}He sounds genuinely hurt.{/n} "That's rude, even for a crusader. Hear it, and then say no. It'll be more satisfying for both of us."''',
       c("Continue", "b_offer2")),
    rl("b_offer2", '''"Sell her to me this time. Properly." {n}He glances at the dark around you.{/n} "You're the only living soul who goes up her stairs without paying. She tells you things. She'd leave her door unbarred for you. One night, when she thinks you're coming, it's me who comes instead."
"I'll give you half the house. Not a quarter: half. And I'll give you her. To keep. Chained, if you like, or not; whatever you mortals prefer. She'd be the finest thing you ever owned."''',
       c('"No. Get back down the Wound road."', "b_refused", flags=(OFFER_REFUSED,)),
       c('"Let me think about it."', "b_strung", flags=(OFFER_STRUNG,)),
       c('"I\'ll be writing to her about this tonight."', "b_told", flags=(OFFER_TOLD,))),
    rl("b_refused", '''{n}He stops walking. The rain runs down the raw scar.{/n}
"You're really hers, then." {n}He sounds almost admiring.{/n} "Nobody's hers. Not for long. I'll wait, hot stuff. Incubi are good at waiting, and demons live a very long time, and you don't." {n}He pulls his hood up and goes.{/n}''',
       c("[Watch him go.]")),
    rl("b_strung", '''"Think." {n}His grin comes, lopsided, dragged by the scar.{/n} "Think very hard. I can wait."
{n}He goes off across the square in the rain, whistling. You have seen men walk away from a sale they thought was made. You have also seen men walk away from a trap they thought they'd set.{/n}''',
       c("[Watch him go.]")),
    rl("b_told", '''"You'll..." {n}For a moment his face goes entirely still around the scar.{/n} "You would. Of course you would. Every word of it true."
{n}He laughs, a short, ugly sound in the rain.{/n} "Then tell her I said it. Tell her everything. Let her take the other side. At least then they'll match."''',
       c("[Watch him go.]", "b_told_answer")),
    nar("b_told_answer", '''{n}You write to her that night, every word he said in the rain, and seal it, and give it to the next courier going south. Not to Rokhorn. He watches it go from the gate with his hood up, and does not whistle.{/n}''',
       c("[Go back inside.]")),
    *discovery("b_", "b_offer")],
    requires=(COMMITTED,), delay=0)


post(OFFER, "A better offer", [
    rl("start", '''{n}Rokhorn comes back three nights later without a letter. He waits for you at the gate in the rain, cloak pulled up, and falls into step beside you across the square as if you'd arranged it.{/n}
"No letter. She doesn't know I'm here." {n}His voice is low and quick, and the stitched side of his mouth hardly moves.{/n} "You stood in her hall while she cut me, hot stuff. So I know what you're worth. I'm here to make you an offer."''',
       c('"Go on."', "offer"),
       c('"No."', "no_first")),
    rl("no_first", '''"You haven't heard it." {n}He sounds genuinely hurt.{/n} "That's rude, even for a crusader. Hear it, and then say no. It'll be more satisfying for both of us."''',
       c("Continue", "offer")),
    rl("offer", '''"Sell her to me this time. Properly." {n}He glances at the dark around you.{/n} "You're the only living soul who goes up her stairs without paying. She tells you things. She leaves her rooms unguarded for you. One night, when she thinks you're coming, it's me who comes instead."
"I'll give you half the house. Not a quarter: half. And I'll give you her. To keep. Chained, if you like, or not; whatever you mortals prefer. She'd be the finest thing you ever owned."''',
       c('"No. Get back up the Wound road."', "refused", flags=(OFFER_REFUSED,)),
       c('"Let me think about it."', "strung", flags=(OFFER_STRUNG,)),
       c('"I\'ll be writing to her about this tonight."', "told", flags=(OFFER_TOLD,))),
    rl("refused", '''{n}He stops walking. The rain runs down the new scar.{/n}
"You're really hers, then." {n}He sounds almost admiring.{/n} "Nobody's hers. Not for long. I'll wait, hot stuff. Incubi are good at waiting, and demons live a very long time, and you don't." {n}He pulls his hood up and goes.{/n}''',
       c("[Watch him go.]")),
    rl("strung", '''"Think." {n}His grin comes, lopsided, dragged by the stitches.{/n} "I'll be back in a month with her next letter. Think very hard. I can wait."
{n}He goes off across the square in the rain, whistling. You have seen men walk away from a sale they thought was made. You have also seen men walk away from a trap they thought they'd set.{/n}''',
       c("[Watch him go.]")),
    rl("told", '''"You'll..." {n}For a moment his face goes entirely still under the stitches.{/n} "You would. Of course you would. Every word of it true."
{n}He laughs, a short, ugly sound in the rain.{/n} "Then tell her I said it. Tell her everything. Let her take the other side. At least then they'll match."''',
       c("[Watch him go.]"))],
    requires=(COURIER,), forbids=(BUNDLE,), delay=48, kind="event")


post(LADYS_PEOPLE, "The Lady's people", [
    nar("start", '''{n}The letter comes by Rokhorn's hand, as the letters do, sealed in black wax. He hands it over without a word and without meeting your eyes.{/n}''',
       c("Continue", "letter")),
    hl("letter", '''"Lover.
Two of the Lady's people came up my stairs last night. Not guests. They don't come as guests. They sat on my best couch and drank my best wine and asked me, very politely, about the mortal who climbs my labyrinth without paying.
Every succubus in the city belongs to the Lady in Shadow. I've told you so. She doesn't have to claim us; she only has to remember us. Last night she remembered me."''',
       c("Continue", "told", requires=(OFFER_TOLD,)),
       c("Continue", "answer", forbids=(OFFER_TOLD,))),
    hl("told", '''"Your letter came the same morning. So I know what my boy offered you in the rain, and I know what you did with it.
He's still carrying my letters. I haven't touched him. I told him I knew, and then I asked him to bring me my wine, and he did, and his hands shook the whole way up the stair. That's worth more than the other side of his face. You taught me that, lover."''',
       c("Continue", "answer")),
    hl("answer", '''"I told them the truth. It's the only thing the Lady's people can't make use of.
I told them that you are a guest of my house, that you pay nothing, that you buy nothing, and that nothing of mine is for sale to you, so there is nothing of mine they can buy from you either. They didn't understand it. They went away to tell her they didn't understand it.
She'll be amused. When the Lady is amused, honey, it's best to be very far away. You are. I'm not."''',
       c("Continue", "ask")),
    hl("ask", '''"Tell me honestly. Is there anything between you and the Lady I should know about, before her people come back? I don't want to be surprised in my own house again. Once was enough.
H."''',
       c('[Write back] "Nothing she hasn\'t already guessed."', "sent"),
       c('[Write back] "Everything. It\'s a long story. Pour a cup before you read the rest."', "sent"),
       c('[Write back] "If she comes to your house, give her whatever she asks for. I\'ll settle it."', "sent")),
    nar("sent", '''{n}Rokhorn takes your answer without a word. On the doorstep he pauses, as if he might say something, and then thinks better of it.{/n}''',
       c("[Let him go.]"))],
    requires=(OFFER,), forbids=(BUNDLE,), delay=72)


post(GIFT, "A gift from the Delights", [
    nar("start", '''{n}Rokhorn brings a letter and, this time, a long narrow parcel wrapped in black silk, which he carries at arm's length the whole way from the gate.{/n}
{n}Inside the silk is a knife beside a sheath of worked bone: thin, curved, and so sharp that the silk has parted where the edge touched it. It is not her knife. It is its twin.{/n}''',
       c("Continue", "letter")),
    hl("letter", '''"Lover.
I had it made by the same smith who made mine, a salamander in the Lower City who works in bone and demon-iron. He wanted a price. I paid it. Don't ask what."''',
       c("Continue", "cut", requires=(KNIFE_TAKEN,)),
       c("Continue", "handed", requires=(HANDED,), forbids=(KNIFE_TAKEN,)),
       c("Continue", "restored", requires=(RESTORED,), forbids=(KNIFE_TAKEN, HANDED)),
       c("Continue", "end", forbids=(KNIFE_TAKEN, HANDED, RESTORED))),
    hl("cut", '''"It's for the hand that did what it was told and didn't shake. Every madam should have one hand in the world she trusts with a knife. I've decided mine is attached to a crusader. It's absurd. I've stopped arguing with it."''',
       c("Continue", "end")),
    hl("handed", '''"It's for the hand that gives knives back. Everyone keeps a knife they're handed; you didn't. So here's one you'll have to keep, since it's a gift, and I don't take gifts back. That's the trick of it, honey. Now you'll have to find out what you do with a knife you can't return."''',
       c("Continue", "end")),
    hl("restored", '''"It's for the hand that held my wrist in my own hall and then walked out in front of the Sinners and gave my knife back. I've thought about that hand every night since. I've decided I want it armed. If anyone ever holds you by the wrist, lover, I want them to regret it."''',
       c("Continue", "end")),
    hl("end", '''"Don't wear it where your paladins can see. They'll ask where it came from, and you'll have to tell them it came from a brothel in the Abyss, and they'll pray for you, and it'll be very tedious for everyone.
H."''',
       c("[Buckle it on.]", "kept", flags=(KNIFE_GIFT,)),
       c("[Wrap it in the black silk and put it away.]", "kept")),
    nar("kept", '''{n}When you look up from the knife, Rokhorn is watching it, not you, from the doorway. His hand has gone to his face without his seeming to know it.{/n}''',
       c("[Let him go.]"))],
    requires=(LADYS_PEOPLE,), forbids=(BUNDLE,), delay=72)


post(HOUSE_NEWS, "News from the Delights", [
    nar("start", '''{n}A thick letter this time, three pages in the round, unhurried hand, and the seal is pressed crooked, as if it were sealed in a hurry or in a good mood.{/n}''',
       c("Continue", "letter")),
    hl("letter", '''"Lover.
The house news, since you never ask for it and always read it.
Morevet has invented a word for you. I won't write it down. It's very clever and very filthy and every girl in the house uses it now, even the Sinners, who are too expensive to use anyone's words but their own. When you come back, someone will say it to your face, and you'll know it's you.
The Glowworm drank a devil under the table on Oathday and he signed over his house to her by mistake. We're all very proud."''',
       c("Continue", "aasimar_warned", requires=(WARNED,)),
       c("Continue", "aasimar", forbids=(WARNED,))),
    hl("aasimar_warned", '''"You'll want to know about the white room. You told me someday someone would come for them. Nobody has. But one of them came to me, of her own accord, the one who looked up when you were there, and asked me to teach her.
I told you, lover. They walk back up the stairs once they've tasted the cold. Some of them never even need to go out in it."''',
       c("Continue", "rokhorn")),
    hl("aasimar", '''"The white room is coming along. Since you left, one of the girls came to me of her own accord and asked to be taught, which is the first real lesson and the only one that matters. I was very, very careful with her. I always am."''',
       c("Continue", "rokhorn")),
    hl("rokhorn", '''"Rokhorn's face is healing badly, as I'd hoped. No one in the Upper City will touch it; I made sure of that. Every guest asks. Every guest gets the story. It's the best advertisement the house has had since your redeemed succubus called it a house of lies.
Write me something. Anything. I've started reading your letters twice, which is the sort of thing I'd sell a girl for doing.
H."''',
       c('[Write back] "Tell Morevet I want to hear the word from her."', "sent"),
       c('[Write back] "Tell the girl in the white room it\'s not too late."', "sent"),
       c('[Write back] "Read them three times. I\'ll write longer."', "sent")),
    nar("sent", '''{n}Rokhorn takes the reply to the gate and goes off into the dusk with it, toward the roads that lead down into the Wound. The laundresses watch him go. So, you notice, does one of your own sentries, for rather longer than a sentry should.{/n}''',
       c("[Go back inside.]"))],
    requires=(COURIER,), forbids=(BUNDLE,), delay=96)


post(BEFORE, "Before the Wound", [
    nar("start", '''{n}The next letter comes on a grey morning, with the drill sergeants already shouting in the square. Rokhorn hands it over and, for once, does not wait for an answer. He looks at you, and at the soldiers, and goes.{/n}''',
       c("Continue", "letter")),
    hl("letter", '''"Lover.
The Lady's people say you'll go into the Wound itself before the year is out. The whole city says it. There are bets. I have placed one. I won't tell you which way.
I've never written a letter like this before, so I don't know how it's supposed to go. The girls write them to their men sometimes, and I read them first, of course, and they're all the same: I'll wait, I'll pray, I'll never love another. I won't wait, I don't pray, and I've loved hundreds. So those are out."''',
       c("Continue", "letter2")),
    hl("letter2", '''"Here is what I have instead. I have a house full of things that can be bought, and a chair that can be taken, and a face that tells everyone exactly what I did to keep both. And I have one person who comes up my stairs without paying.
If you die in the Wound, I'll close the Delights for one night, as I said. The first time in a thousand years. Everyone in Alushinyrra will know why. They'll say the madam's gone soft. Let them.
If you live, come up my stairs in the spring. Don't bring a coin. You'll have to reach."''',
       c("Continue", "letter3")),
    hl("letter3", '''"That's all. That's the whole letter. I read it three times before I sealed it and I still don't like it, which means it's probably true.
H.
P.S. Don't let anyone scratch you."''',
       c('[Keep the letter inside your armour.]', "kept"),
       c('[Burn it, so no one else ever reads it.]', "burned")),
    nar("kept", '''{n}You fold it small and put it where the Wound's fire won't reach it, if anything will reach it. It is warm against you. You tell yourself that's the fire in your own chest.{/n}''',
       c("[Go back to the war.]")),
    nar("burned", '''{n}It goes up in the brazier by your door in a single bright curl, the black wax spitting. For a moment, in the smoke, you can smell the Delights: incense, coin, lamps, and under it the ghost of another woman's perfume.{/n}''',
       c("[Go back to the war.]"))],
    requires=(GIFT,), forbids=(BUNDLE,), delay=96)


# === More of her, in Chapter 4 (optional) ================================================================================

beat(B + "the_chair", "How the chair is taken", '"How did you take the chair?"', [
    hx("start", '''"Somebody else emptied it, lover. I got there first." {n}She settles into Chivarro's cushions.{/n} "Then the boys wanted to know if I'd stay there. Every boy with a knife, every girl with a grudge, every guest with a purse and an opinion."
"Rokhorn had a patron at court and a face half the Upper City wanted to sit on. He thought that made him fit to rule. Look at me. You know how that went."''',
       c('"What did you have?"', "had")),
    hx("had", '''"This." {n}She touches the scar across her mouth.{/n} "Rokhorn gave me some of it. Two of the Sinners gave me the ribs before they saw sense. A vrock tore the wings; I threw him off the roof."
"Count the marks, honey. Then count who's pouring the wine. The boys can count too. That's why I leave the marks where they can see them."''',
       c('"And Rokhorn?"', "rokhorn"),
       c('"Why not heal them, afterwards?"', "heal")),
    hx("rokhorn", '''"Rokhorn lost loudest. And then he went straight to the healers of three circles and paid them to put his face back, and came back up my stairs smiling as if nothing had happened." {n}Her good eye is very steady.{/n}
"That's the thing I've never forgiven, lover. Not the fight. The smile. He bought his way out of the lesson. Everyone else in this house has to look at what it cost."''',
       c("Continue", "end")),
    hx("heal", '''"Heal them?" {n}She laughs.{/n} "And have to tell every climber in the house what happened, over and over, in words? Words are cheap. Anyone can say they won." {n}She tilts her face to the lamp.{/n}
"This way nobody has to ask. They look at me and they can count it. Every scar is a night I came down the stairs and they didn't."''',
       c("Continue", "end")),
    hx("end", '''"And that, lover, is the whole secret of the Delights." {n}She reaches for her cup.{/n} "Don't tell anyone. They'd only pay me to tell them again."''',
       c('"Your secret\'s safe."'))],
    requires=(PREDECESSOR,), delay=24)


beat(B + "the_wings", "Rags", '"Can you still fly?"', [
    hx("start", '''{n}Herrax looks over her shoulder at her own wings as if she'd forgotten they were there. They hang behind her in rags: long bones, and between them skin torn to lace, stirring in the draught from the stair.{/n}
"Once. Not far. Not well." {n}She shrugs, and the rags shift.{/n} "A madam doesn't need to fly, lover. A madam who can fly away is a madam nobody trusts with their secrets. My guests like to know I'll still be here in the morning, holding everything they told me."''',
       c('"Do they hurt?"', "hurt"),
       c('[Flirt] "May I?"', "touch")),
    hx("hurt", '''"When it rains." {n}She says it lightly.{/n} "It doesn't rain much in Alushinyrra, and when it does, I have a boy whose only work is to stand behind the dais with a warm towel and hold them. He's very good at it. He'll never do anything else as long as he lives."
"Everything in this house earns its keep, honey. Even the pain."''',
       c("Continue", "end")),
    hx("touch", '''{n}She considers you, and then, without a word, she lets one wing fall open along the back of the couch, into your reach.{/n}
{n}The skin is thin as old silk and warm, much warmer than you expected, and you can feel her pulse in it, slow. Where it is torn the edges have healed hard and smooth, like the scar on her mouth. She watches your hand the whole time, the way a cat watches a hand near its belly.{/n}
"Careful, lover. The last guest who touched those without paying left without the hand." {n}She doesn't draw it away.{/n} "You haven't paid. Keep going, and find out what I charge you."''',
       c("[Take your hand away, slowly.]", "end"),
       c("[Leave it where it is.]", "end")),
    hx("end", '''{n}She folds the wing back in its own time, and reaches for her cup, and is entirely the madam again.{/n}
"There. Now you know something about me that isn't for sale," {n}she says.{/n} "Be very careful who you tell. I'll know."''',
       c('"I won\'t tell anyone."'))],
    requires=(LABYRINTH,), delay=24)


beat(B + "what_she_wants", "What the keeper wants", '"What do you want, Herrax? Not the chair. After the chair."', [
    hx("start", '''{n}She looks at you for a while, as if deciding whether the question is worth answering for free.{/n}
"Rokhorn wants the whole world on its knees, lover. He'll tell anyone. He wants to fill it up and wring it out and make it his." {n}She waves a hand.{/n} "Incubi. They have one idea, and they think it's a philosophy."
"I don't want the world. The world is a very bad investment; it's always on fire somewhere. I want this house."''',
       c('"You have this house."', "have")),
    hx("have", '''"I have it tonight." {n}She taps the arm of the dais.{/n} "Chivarro had it for a very long time. Before her, I don't know. The house was here before all of us, and every one of us thought she'd keep it forever."
"I want to be the one who does. I want the Lady in Shadow to fall, and the next queen after her, and some new Lady to come up my stairs one day and find me still sitting here, with the same face, pouring the same wine." {n}She smiles.{/n} "I want to be the last thing in Alushinyrra that can't be bought."''',
       c('"That\'s a long time to sit in one chair."', "long"),
       c('"Then I hope you get it."', "hope")),
    hx("long", '''"Demons live a long time, honey. We have to do something with it." {n}She stretches, and the wings creak.{/n} "Chivarro kept this chair until a mortal walked up her stairs and knocked her off it. I mean to keep it until the next boy who comes up mine with six friends and a patron at court takes one look at my face on the landing, and turns round, and goes back down. And tells his friends why."''',
       c("Continue", "end")),
    hx("hope", '''{n}She laughs, surprised.{/n} "Hope. From a crusader, for a demon madam. My girls would charge you extra for that sort of thing." {n}She looks at you a moment longer.{/n} "Don't say it again. I might start to rely on it."''',
       c("Continue", "end")),
    hx("end", '''"And what do you want, lover? After your war?" {n}She holds up a hand before you can speak.{/n} "No. Don't answer. You'd lie, or worse, you'd tell the truth, and then I'd have to decide what to do with it. Keep it. Bring it to me when it's worth something."''',
       c('"I will."'))],
    requires=(THE_LADY,), delay=24)


beat(B + "a_guest_of_note", "A guest of note", '"Who\'s that you\'ve been talking to?"', [
    nar("start", '''{n}The guest at the end of the bar is a devil: tall, grey, immaculately dressed, with a ledger of his own under one arm and a smile that has been measured to the width of a coin. He is leaving as you arrive. He bows to Herrax on his way out, and his eyes pass over you like a clerk's over a column of sums.{/n}''',
       c("Continue", "who")),
    hx("who", '''"A buyer." {n}Herrax watches him to the stair.{/n} "From Dis. His master would like to purchase the Delights. All of it. The house, the girls, the debts, the chair. He named a number. It was a very good number."
{n}She pours herself a cup.{/n} "He also asked what the madam would cost, as a separate item. I told him she isn't for sale. He said everything is. We had a lovely conversation about it."''',
       c('"What did you tell him, in the end?"', "told"),
       c('[Trickster] "Next time, sell him the stairs. Separately. At a very good price."', "stairs", mythic="Trickster")),
    hx("told", '''"That he could have the house the day his master can buy me. Which will be never, so he can have the house never." {n}She sips.{/n} "He wrote it down. Devils write everything down. He'll be back in a hundred years with a better number, and I'll still be here."''',
       c("Continue", "end")),
    hx("stairs", '''{n}She puts her cup down and laughs, loud enough that the devil, halfway down the stair, pauses.{/n}
"The stairs. Separately." {n}She wipes her good eye.{/n} "He'd buy them, too. He'd own every step between my door and my floor, and he'd have to charge my guests a toll to climb them, and I'd charge him rent for the landing." {n}She shakes her head.{/n} "Lover, if you ever get tired of your crusade, I'll give you a job. You'd be terrible at it. You'd be rich in a year."''',
       c("Continue", "end")),
    hx("end", '''"He'll be back," {n}she says, watching the empty stair.{/n} "They always are. It's the only compliment a devil knows how to pay: coming back with more."''',
       c('"Let him come."'))],
    requires=(ARENA,), delay=24)


# --- Rokhorn, after the night (his own list; the native summons still works). -------------------------------------------

SCENES.append(scene(B + "rokhorn.stitched", "Stitches", "Herrax", 4, '"Rokhorn."', [
    rk("start", '''{n}He comes when he is summoned, as he always has; he has no choice about that. The new wound runs from his lip to his cheekbone, sewn with black thread in a row of neat, ugly stitches, and every time he speaks it pulls.{/n}
"Hello, hot stuff." {n}He says it anyway. He has said it to every guest since before you were born, and he will not stop now.{/n} "Come for your cut? She tells me you're owed a quarter of nothing. I'll pay it, if you like. In kind."''',
       c('"Does it hurt?"', "hurt"),
       c('"No hard feelings, Rokhorn."', "feelings")),
    rk("hurt", '''"Everything hurts, little bird. That's the secret. Pleasure, pain; it's the same shock, you just call it different names depending on who's holding the knife." {n}He touches the stitches with one claw.{/n} "This one I'll call pain. For a while. Then one day, I'll call it something else."''',
       c("Continue", "read", requires=(BAIT,)),
       c("Continue", "read_blown", forbids=(BAIT,))),
    rk("feelings", '''{n}He laughs, and the stitches tug his laugh into a snarl.{/n} "Hard feelings are the only kind I have, hot stuff. I'm an incubus. Soft is for mortals and angels."''',
       c("Continue", "read", requires=(BAIT,)),
       c("Continue", "read_blown", forbids=(BAIT,))),
    rk("read_blown", '''"You know what I keep thinking?" {n}He leans in, and you can smell the house's wine on him, and blood under it.{/n} "I scratched you. The day you came to me with her night in your mouth. One taste, and I read it all, and I shouted it off every couch in the house." {n}He touches the stitches.{/n} "And she cut me anyway, in front of all of them. Knowing didn't save my face. Being right didn't save my face."
"So now I know what the lesson was, hot stuff. It was never about the lie. She'd be so pleased."''',
       c('"She would."')),
    rk("read", '''"You know what I keep thinking?" {n}He leans in, and you can smell the house's wine on him, and blood under it.{/n} "I should have scratched you. The day you first came to me. One little taste, and I'd have read it all: her night, her knife, her coin. I trusted you instead. A mortal." {n}He shakes his head.{/n}
"I don't trust anyone now. So I suppose you taught me something too. She'd be so pleased."''',
       c('"She would."'))],
    requires=("trickster.ever", MADAM, MET, LESSON), forbids=(DECLINED, CLOSED), delay=12, last=4, optional=True,
    Relationship=REL, AnswerLists=[ROK_LIST], NativeReturnCue=ROK_RET))

SCENES.append(scene(B + "rokhorn.whole", "A whole face", "Herrax", 4, '"Rokhorn."', [
    rk("start", '''{n}Rokhorn's face is whole, and he wears it like a trophy. He comes when he is summoned, stretching, and looks you over with frank delight.{/n}
"Hot stuff! My saviour." {n}He spreads his arms.{/n} "You sold me to her, and then you took the knife out of her hand, in her own hall, in front of everyone. You know what they're saying about her now? That she can be held." {n}He laughs.{/n} "You did more to her in one night than I ever managed."''',
       c('"I didn\'t do it for you."', "not_for_you"),
       c('"Don\'t get comfortable."', "comfortable")),
    rk("not_for_you", '''"Of course not. Nobody does anything for me." {n}He grins wider.{/n} "But you did it, and I've still got my face, and I know who to thank. Incubi pay their debts, hot stuff. In kind. Whenever you like. On your knees, and I'll tell you when you can get up."''',
       c("Continue", "end")),
    rk("comfortable", '''"Comfortable?" {n}He lounges against his pillar, and looks across the hall at the dais, where Herrax sits with an empty sheath at her hip.{/n} "I've never been so comfortable in my life. She could open me with a claw. But another cut before you return her knife? The house would remember your hand on her wrist. I'm betting she wants that settled first."''',
       c("Continue", "end")),
    rk("end", '''{n}He leans in, and lowers his voice.{/n} "So keep it, hot stuff. As long as you like. Forever, if you can manage it." {n}He winks.{/n} "Everyone in this house is watching to see whether you give it back. I've got money on no."''',
       c('"Then you\'ll lose it."'),
       c("[Say nothing.]"))],
    requires=("trickster.ever", MADAM, MET, DECLINED), forbids=(RESTORED, CLOSED), delay=6, last=4, optional=True,
    Relationship=REL, AnswerLists=[ROK_LIST], NativeReturnCue=ROK_RET))


# --- Chapter 5: the healers ----------------------------------------------------------------------------------------------

post(L + "the_healers", "No healers", [
    nar("start", '''{n}Rokhorn brings this one with his hood pulled low, and when he pushes it back to hand over the letter, you see why. The stitches are out. The scar under them is new, and raw, and a finger's width longer than it was.{/n}''',
       c("Continue", "letter")),
    hl("letter", '''"Lover.
You'll have noticed his face.
He found a healer. A little witch in the Lower City who didn't know whose work she was undoing, and was greedy enough not to ask. He paid her with a ring off my tray, which was stupid of him, since I count the tray.
She's on the tray herself now. Some of her. And I opened his cheek again along the same line, a little longer, so he'll remember that it's mine, not his, and not the healers'. He took it very well. He's learning."''',
       c("Continue", "cheek", requires=(CHEEK,)),
       c("Continue", "end", forbids=(CHEEK,))),
    hl("cheek", '''"And that reminds me. Your cheek. His claw. Don't you dare let your priests near it, honey. Every guest in my house has heard how the favoured guest walked the length of my hall with his mark on your cheek, and I want it there when you come back. I'll know if it's gone. I'll be very disappointed. You've never seen me disappointed."''',
       c("Continue", "end")),
    hl("end", '''"That's all. That's the news. The house is quiet. I'm bored. Come and be interesting.
H."''',
       c('[Write back] "I kept it. The cheek."', "sent", requires=(CHEEK,)),
       c('[Write back] "You\'re terrifying. Don\'t change."', "sent"),
       c('[Write back] "Leave the healers alone. Punish the one who lied to you, not the one who was paid."', "sent")),
    nar("sent", '''{n}Rokhorn takes your answer in silence and pulls his hood back up over the new cut. At the door he stops, as if he meant to say something, and then he goes down your steps without saying it.{/n}''',
       c("[Let him go.]"))],
    requires=(COURIER,), forbids=(BUNDLE,), delay=120)


# --- The day after the night, before closing (the pivot's first consequence). ------------------------------------------

beat(B + "the_stain", "Don't scrub it", '"The girls are sweeping round that stain."', [
    hx("start", '''"Because I told them to." {n}Herrax is standing at the foot of the dais, looking down at the brown mark in the grout where Rokhorn knelt, the way another woman might look at a painting she had just hung.{/n}
"A floor gets scrubbed, lover, and in a week nobody remembers what was on it. Leave it, and every girl who sweeps round it thinks about it, every morning, for the rest of her life in my house." {n}She glances at you.{/n} "It's cheaper than a sermon, and it works better."''',
       c("Continue", "cut", requires=(KNIFE_TAKEN,)),
       c("Continue", "handed", requires=(HANDED,), forbids=(KNIFE_TAKEN,)),
       c("Continue", "handed", forbids=(KNIFE_TAKEN, HANDED))),
    hx("cut", '''"They're all talking about your hand, you know." {n}She sounds pleased.{/n} "How it didn't shake. How you cut exactly where I pointed and not a hair deeper. Morevet says you've done it before. The Glowworm says you're a butcher's child from Golarion. The Sinners say nothing at all, which from the Sinners is a compliment."
"Tell me the truth, since nobody's listening. What did it feel like?"''',
       c('"Like nothing. That\'s what frightens me."', "nothing"),
       c('"Like paying a debt."', "debt"),
       c('"Good."', "good")),
    hx("nothing", '''{n}She looks at you for a while with her good eye, and the blind one drifts after it.{/n}
"Nothing? He screamed loud enough to shake the lamps." {n}She catches your wrist and turns your cutting hand palm up.{/n} "I liked that part. All those girls watching him bleed, and not one laughing at my face." {n}She presses your hand against the scar at her mouth.{/n} "Be frightened, lover. You still held the knife steady. Now every little climber in my house knows whose hand I put it in."''',
       c("Continue", "end")),
    hx("debt", '''"A debt." {n}She tastes the word.{/n} "Yes. You sold him, so you owed him the cut. That's very tidy. That's how a devil would think of it." {n}She laughs.{/n} "Don't let it go to your head, lover. Devils end up owning everything and enjoying none of it."''',
       c("Continue", "end")),
    hx("good", '''{n}She laughs, loud and delighted, and a girl sweeping by the stair nearly drops her broom.{/n} "Good. Just good. You mortals and your little words." {n}She pats your cheek.{/n} "Keep that one to yourself around your paladins, lover. They'd never understand, and I'd hate to see you burned."''',
       c("Continue", "end")),
    hx("handed", '''"They're all talking about your hand, you know. Not what it did. What it didn't." {n}She says it slowly.{/n} "Everyone in this house keeps a knife they're handed. It's the first thing they learn. And you turned it round and gave it back to me, hilt first, in front of all of them, as if it were a spoon you'd borrowed."
"Tell me the truth, since nobody's listening. Why?"''',
       c('"It was your lesson. Not mine."', "hers"),
       c('"I don\'t cut faces for other people."', "faces")),
    hx("hers", '''"Mine." {n}She seems to like that word from you almost as much as from herself.{/n} "Yes. It was. Most people would have taken it anyway, to be sure I knew they could." {n}She taps the stain with her toe.{/n} "You gave it back so I'd know you didn't need to. That's either the cleverest thing anyone's done in this hall, or the most dangerous."''',
       c("Continue", "end")),
    hx("faces", '''"Only your own, then?" {n}Her mouth curls.{/n} "That's a rare scruple in the Isles, lover. I'd sell it, if I could work out how to bottle it. Half the Upper City would pay to feel that clean for an evening."''',
       c("Continue", "end")),
    hx("end", '''{n}She turns from the stain.{/n} "Come back at closing. I'll have the hall emptied. There's something I've been meaning to say to you, and I don't say things in front of the house unless I'm charging for them."''',
       c('"At closing, then."'))],
    requires=(LESSON,), forbids=(DECLINED, COMMITTED), delay=4)


beat(B + "the_glowworm", "A fey's joke", '"Tell me about your fey."', [
    hx("start", '''"The Glowworm?" {n}Herrax follows your eyes to the sideboard, where a small, pale, freckled fey with blue curls is lying on her back with her feet up the wall, explaining something to the ceiling.{/n}
"She's here because of a joke, lover. Some prank the Lantern King played on her back in the First World. She won't tell anyone what it was; she laughs until she cries and says it's too embarrassing. So she stays. My guests adore her. She makes them laugh so hard they forget their own names, and then they wake up without their boots."''',
       c('"A joke put her here?"', "joke"),
       c('"Does she want to leave?"', "leave")),
    hx("joke", '''"The Lantern King's jokes put a great many people a great many places, I'm told." {n}She glances at you sidelong.{/n} "You've a reputation for jokes yourself, lover."''',
       # Retain the saved end target at index zero; retire it on this Trickster-only host.
       c("Continue", "end", forbids=("trickster.ever",)),
       c("Continue", "joke_before_audience", forbids=(H + "palace_dismissed",)),
       c("Continue", "joke_after_audience", requires=(H + "palace_dismissed",))),
    hx("leave", '''"Leave?" {n}Herrax seems puzzled by the question.{/n} "Where would she go? The First World? With whatever the Lantern King did to her still stuck to her like a paper tail?" {n}She shakes her head.{/n}
"Nobody in my house wants to leave, lover. That's not how it works. They want to stop wanting what brought them here. I sell them a night's worth of that at a time. It's the best business in the Abyss."''',
       c("Continue", "end")),
    hx("end", '''{n}Across the room the Glowworm sees you both looking, and waves with her foot, and laughs so hard she falls off the sideboard.{/n}
"There," {n}says Herrax.{/n} "Now she's happy. That's my whole job, honey. Everyone happy, for exactly as long as they can pay."''',
       c('"And you?"', "you")),
    hx("you", '''"Me?" {n}She considers it with real interest.{/n} "I'm happy when the takings come in and nobody tries for my chair. It's a very small happiness. It's the only kind that lasts."''',
       c('"I\'ll see what I can do about the chair."')),
    # Authored variants: only the native dismissal warrants a completed palace visit.
    hx("joke_before_audience", '''"The Isles say the mortal who unseated Chivarro plays tricks, and that the tricks don't stay tricks. If you ever feel like a joke in my house, honey, ask me first. I have a very particular sense of humour about my stock."''',
       c("Continue", "end")),
    hx("joke_after_audience", '''"The Isles say the mortal the Lady let walk out of her palace plays tricks, and that the tricks don't stay tricks. If you ever feel like a joke in my house, honey, ask me first. I have a very particular sense of humour about my stock."''',
       c("Continue", "end"))],
    requires=(FIRST_PRICE,), delay=24)


beat(B + "the_sinners", "Three for forty thousand", '"The Sinners are back."', [
    nar("start", '''{n}Three succubi are draped across one couch by the stair like a single many-limbed creature, dressed in very little and wearing it beautifully. Guests who pass them slow down, and then speed up, and then come back. The Sinners watch them do it with lazy, knowing smiles.{/n}''',
       c("Continue", "sinners")),
    hx("sinners", '''"My best girls. Forty thousand gold for the three, and worth every coin; they've never once let a client go home with anything left to spend." {n}Herrax watches them with open pride.{/n}
"They know no morality and no boundaries. That's what the price is for. Anyone can be wicked; the Sinners are wicked in perfect agreement, all three at once, like a choir." {n}She sips.{/n} "They were two of the scars on my ribs, the night I took the chair. Then they saw sense."''',
       c('"And now they work for you."', "work"),
       c('"Do they ever turn on you again?"', "turn")),
    hx("work", '''"Now they work for me, and they're paid better than they were under Chivarro, and they know it." {n}She smiles.{/n} "That's the trick with the ones who cut you, lover. Don't kill them. Hire them. They know exactly where you bleed, and they'll make very sure nobody else finds it."''',
       c("Continue", "end")),
    hx("turn", '''"Every night." {n}She says it cheerfully.{/n} "Not with knives. With their eyes. They watch me to see if I'm getting tired. The day I am, they'll have my chair in an hour, and they'll split it three ways, and fight about it for a century." {n}She raises her cup to them, and three cups rise back.{/n} "I'm never tired."''',
       c("Continue", "end")),
    hx("end", '''{n}One of the Sinners catches your eye across the hall, and slowly draws one fingertip down the centre of her own throat. The other two laugh.{/n}
"They like you," {n}Herrax says.{/n} "That's bad news for you. Ask the arena champion what happened the last time they liked someone."''',
       c('"I\'ll keep my distance."'))],
    requires=(ARENA,), delay=24)


beat(B + "a_night_out", "Battlebliss", '"Come down to the arena with me."', [
    hx("start", '''{n}Herrax looks at you as if you had suggested she go and roll in the gutter.{/n}
"The arena. With the vavakia and the betting-slips and the smell." {n}She considers it, and then, slowly, she smiles.{/n} "Actually, yes. There's a bookmaker on the east steps who's been paying my boys in clipped coin, and I'd like him to see my face while he does it. And I'd like the whole Battlebliss to see who I bring." {n}She stands, and holds out her arm.{/n} "One night. If you make me enjoy it, I'll never forgive you."''',
       c("[Take her arm.]", "arena")),
    nar("arena", '''{n}The Battlebliss is roaring when you arrive. Two demons are killing each other on the sand below, slowly, to the crowd's delight. Heads turn as you come down the steps together: the madam of the Ten Thousand Delights, whom nobody has ever seen in the stands, on the arm of a mortal crusader, with her ragged wings folded behind her like a mantle.{/n}
{n}Her own boys, scattered through the crowd with their hands in other people's purses, see her and freeze. She smiles at every one of them until they get back to work.{/n}''',
       c("Continue", "bet")),
    hx("bet", '''"Pick one." {n}She nods down at the sand.{/n} "Pick the one who'll win, and I'll put a thousand on it in your name. Pick the loser, and you pay the thousand in something I'll think of later."''',
       c('"The small one. He\'s been saving his strength."', "small"),
       c('"The big one. He\'s angrier."', "big")),
    hx("small", '''{n}The small one wins. It takes him a long time and it is not pretty, and when it is over the crowd howls and Herrax turns to you with her good eye very bright.{/n}
"Saving his strength." {n}She collects her winnings from the bookmaker on the east steps, who has gone the colour of tallow, and bites every coin he counts out, slowly, while he watches.{/n} "That's how you watch everything, isn't it, lover? For the one who's saving something."''',
       c("Continue", "home")),
    hx("big", '''{n}The big one loses. It takes him a long time and it is not pretty, and when it is over the crowd howls and Herrax turns to you with her good eye very bright.{/n}
"Angrier." {n}She laughs.{/n} "Angry is how you lose in Alushinyrra, honey. The angry ones always think the fight is the point." {n}She taps your chest.{/n} "You owe me a thousand. I'll think of something."''',
       c("Continue", "home", flags=(BET_LOST,))),
    hx("home", '''{n}On the walk back up to the Delights through the lamplit streets, she keeps her arm through yours the whole way, and does not seem to notice she is doing it. The sand is still on both of you. She smells of pit-smoke and spilled blood and clipped silver, and every few steps her thumb drags once across the inside of your wrist, idly, the way she counts coins she already owns.{/n}
"There. I've been to the arena," {n}she says at her own door.{/n} "It was loud, and it stank, and I enjoyed it." {n}She looks at you, accusing. Her good eye is very bright, and her breath is not that of a woman who has only been walking. Behind her the street door of the Delights booms as the crowd from the sand starts to pour in, and she makes no move to go to it.{/n} "I told you I'd never forgive you."
{n}She keeps your arm trapped against her ribs and puts the other hand in your collar, and her ragged wing comes round behind you, a torn, warm curtain, and draws you in until your mouths are a breath apart. The scar through her lip is hot against yours when she speaks.{/n}
"Tell me you'll live with it, lover. I love hearing a mortal promise what they can't afford. I bit every coin that man counted out tonight, and I'm still hungry."''',
       c('"I\'ll live with it."'))],
    requires=(COMMITTED,), delay=24)


# --- The coin (plants the device: the arch sets its bearer down under hers, Cue_0063; her girls take a favoured guest up). ----

beat(B + "the_coin", "Her favoured guest", '"About this coin you gave me."', [
    hx("start", '''{n}Herrax glances at the gold coin on your belt and smiles, as a jeweller smiles at a piece she sold a long time ago and is pleased to see still worn.{/n}
"Have you looked at the engraving? Properly?" {n}She holds out her palm, and you put the coin in it, and she turns it to the lamp. The little figures on its face are doing something that would get the engraver hanged in any city on Golarion.{/n}
"Every arch in Alushinyrra knows this coin. Step through any of them with it in your hand and think of me, and the arch sets you down under mine, downstairs, as my favoured guest. No queue at the street door. No fee."''',
       c('"And after the arch?"', "doors"),
       c('"How many of these are there?"', "how_many")),
    hx("doors", '''"After the arch, my girls." {n}She closes her hand on it.{/n} "The ones who keep the arch hold the keys to my floor. A guest who comes through with this coin, they take up the back stair at any hour, three locked doors past anything the other guests see, and they ask nothing. That's the house's custom. I made it." {n}She smiles.{/n} "The arches don't ask who you are, lover, only what you're carrying, and my girls only ask what the arch let through. That's the beauty of it, and the danger. Anyone holding this could walk into my rooms as if I'd sent for them."
{n}She gives it back to you, and her fingers stay on yours a moment longer than they need to.{/n} "So don't lose it. Don't sell it. Don't let anyone take it off your belt while you're drunk in my house. I'd hate to find a stranger in my rooms who smelled of you."''',
       c('"I\'ll keep it close."')),
    hx("how_many", '''"One at a time." {n}She gives it back.{/n} "When someone stops being my favoured guest, the coin comes back to me, one way or another, and waits in a drawer until I find someone else I'd like to see without having to send for them."
"Chivarro had a drawer of them, you know. Dozens. She gave them to everyone. That's why anyone could walk into her rooms, and why, in the end, someone did." {n}She smiles.{/n} "I have one. It's on your belt."''',
       c('"I\'ll keep it close."'))],
    requires=(FIRST_PRICE, COIN_HELD), forbids=(COIN_LOST,), delay=24)


# --- The lesson, a night late (her refusal answered: the knife back, then the cut, with the Commander at the back). ------

beat(B + "a_night_late", "A night late", '"Is it tonight?"', [
    nar("start", '''{n}It is. The house gathers without being told: the Sinners on the stair, Morevet with her lips parted, the Glowworm on her sideboard, the boys along the walls. Rokhorn is brought in between four of them. He has worn his whole face since the night she was held as if it were a crown, and he does not seem to have understood yet that the crown was only lent.{/n}
{n}Herrax sits on Chivarro's dais with her knife back at her hip. She looks for you at the back of the hall, finds you, and nods once, very slightly, as a madam nods to a guest she has allowed to stay.{/n}''',
       c("Continue", "cut")),
    hx("cut", '''"The other night a mortal held my wrist in my own hall," {n}she says to the room, pleasantly,{/n} "and you all saw it. Then that mortal gave me back my knife, hilt first, before the Sinners, and you all saw that too. So now you'll all see what the knife was for."
{n}She steps down to Rokhorn, takes his jaw in her fingers like a lover, and opens his face from lip to cheekbone in one unhurried stroke. He screams. She lets him. When he is finished she wipes the blade on his hair and slides it home.{/n}''',
       c("Continue", "after")),
    nar("after", '''{n}Nobody looks at Rokhorn as they drag him out. Everyone looks at you. You stand where she told you to stand, at the back, and you don't move, and you keep your eyes on all of it, and after a while the house decides it has seen enough and goes back to its wine.{/n}
{n}On her way back up the dais Herrax passes close enough to speak without being heard.{/n}''',
       c("Continue", "said")),
    hx("said", '''"You watched all of it." {n}She doesn't look at you.{/n} "Good. Come back at closing, lover. I'll have decided."''',
       c('"At closing."'))],
    requires=(RESTORED,), forbids=(COMMITTED,), delay=12)


# --- The pretty version (after Rokhorn's confession). ----------------------------------------------------------------------

beat(B + "pretty_version", "The pretty version", '"I heard Rokhorn\'s story."', [
    hx("start", '''"The ugly one." {n}Herrax looks delighted.{/n} "Did he do the pause? Before 'Seize power? Well, I did try'? He practises that pause. He thinks it makes him sound rueful." {n}She leans on the bar.{/n}
"And did he tell you about his healers? How much he paid, and to whom, and how good his jaw looks now? He always gets to the healers. He's prouder of the healers than of anything he ever did in my bed."''',
       c('"He said you keep your scars to remind them what they looked like after you finished."', "pretty"),
       c('"Now tell me the pretty version."', "pretty")),
    hx("pretty", '''"The pretty version." {n}She considers.{/n} "The pretty version is that he came up my stairs one night with six boys and a patron at court and a smile, and I was alone, and I was tired, and I had one eye left." {n}She taps the milky one.{/n}
"And in the morning I came down to the bar and poured the wine. And he came down an hour after me, and went straight out of the door to the healers, and came back when the healers had finished. That's all. That's the pretty version. It's pretty because I'm in it at the end, pouring wine."''',
       c('"He still wants your chair."', "wants"),
       c('"I like the pretty version."', "like")),
    hx("wants", '''{n}She is quiet for a breath, and then she laughs, low.{/n} "Does he, now." {n}Her good eye goes across the hall to the pillar where he lounges.{/n} "Come and tell me that again when you mean it as news, lover. Not as gossip. I pay very differently for news."''',
       c('"I\'ll remember."')),
    hx("like", '''"Everyone does." {n}She pours you a cup.{/n} "That's the trouble with it."''',
       c('"Is it true?"', "true")),
    hx("true", '''"Honey." {n}She pushes the cup across.{/n} "I told you. In this house nobody asks that."''',
       c('"I keep forgetting."'))],
    requires=(FIRST_PRICE, CONFESSED), delay=0)


# --- Her rooms (after the yes). ---------------------------------------------------------------------------------------------

beat(B + "her_rooms", "The private floor", '"Show me your rooms. By daylight."', [
    nar("start", '''{n}Herrax opens the last door on the private floor. Bare whitewashed stone, bare boards, a narrow window over the city roofs: there is no gold anywhere. A chair, a table with a jug, a locked chest, and a hook for her knife sheath are the only things plainly hers. She lets you look before she steps inside.{/n}''',
       c('"This isn\'t what I expected."', 'rooms_seen', requires=(BAIT,)),
       c('"This isn\'t what I expected."', 'rooms_first', forbids=(BAIT,))),
    hx("expected", '''"No one expects it. No one sees it." {n}Herrax sits on the chest, her ragged wings folded against the wall.{/n} "Downstairs is for selling, lover. Everything down there is dressed to be bought. Up here there's nothing to buy, so there's nothing to dress."
"Chivarro kept her rooms like a jewel box. Every inch of them was for sale if you asked the right way, and in the end someone asked. I keep mine like a cell. There's nothing in here anybody wants but me."''',
       c('"And the chest?"', "chest"),
       c("[Sit beside her.]", "beside")),
    hx("chest", '''"The chest is none of your business." {n}She says it pleasantly, and doesn't move off the lid.{/n} "Everyone has one thing they keep locked, honey. You'd think less of me if I didn't. You'd think I was stupid, and you'd be right."''',
       c("[Sit beside her.]", "beside")),
    hx("beside", '''{n}She makes room without seeming to. For a while neither of you says anything, and the noise of the Upper City comes up through the narrow window: carts, bells, someone screaming a long way off, someone laughing.{/n}
"The ones who come up here at night never look at the walls," {n}she says eventually.{/n} "Don't make anything of it. It's only a room."
{n}Her shoulder is against yours. She doesn't move it. The shoulder is not the only thing: her thigh lies along yours, a line of heat through the cloth, and the daylight from the narrow window falls across her face and does not flatter it, and she has never asked it to. It finds the jagged scar through her lips, the milky ruin of the left eye, the ragged wings hung off her back like wet washing. She watches you see all of it. She is smiling, slowly, at the wall, the way she smiles at a price she has decided to be insulted by.{/n}
"You haven't looked at the walls once since you sat down." {n}Her hand comes down flat on your thigh and stays there, heavy, the claws of her fingertips resting against the seam.{/n} "Nothing in this room has a price. Not the chair, not the jug, not what I am about to do to you. I'd hate for you to think it was a mistake, lover, so I'll say it in daylight where nobody can pretend they didn't hear."''',
       c('"It\'s only a room."')),
    nar("rooms_seen", '''{n}In daylight, the room where Rokhorn walked into his ambush looks smaller. The chair faces the same door. Herrax catches you looking at it and sits on her locked chest instead.{/n}''', c("Continue", "expected")),
    nar("rooms_first", '''{n}You saw the punishment below, in the great hall. Here there are bare boards beneath your boots and no cushions on the chair. Somebody screams in the street below the narrow window. Herrax pays it no attention.{/n}''', c("Continue", "expected"))],
    requires=(COMMITTED,), delay=24)


# --- While her refusal stands: Morevet's opinion. ---------------------------------------------------------------------------

beat(B + "morevet_laughs", "The house has opinions", '"Morevet has been following me."', [
    nar("start", '''{n}Morevet Honeyed Tongue falls into step beside you on the stair, close enough that her hip brushes yours, and speaks without turning her head, the long forked tongue flickering at the corner of her smile.{/n}
"The mortal who held the madam's wrist." {n}She sounds enchanted.{/n} "Do you know what you've done? Every girl in the house has been trying her own wrist at night, in the dark, wondering who could hold it. Herrax can't bear it. I haven't enjoyed the house this much in a century."''',
       c('"Tell her I\'m sorry."', "sorry"),
       c('"What would you do, in my place?"', "place")),
    nar("sorry", '''{n}Morevet laughs, a sweet, poisonous little sound.{/n} "Tell her yourself, darling. With the knife. In front of everyone. That's the only way anything is ever said in this house." {n}She slides away down the stair, and calls back over her shoulder:{/n} "I've got money on you never doing it. Don't disappoint me. Or do."''',
       c('"We\'ll see."')),
    nar("place", '''"In your place?" {n}She stops on the step and looks at you properly, and for once there is no sweetness in it.{/n}
"I'd give it back before the Sinners, in daylight, hilt first. And then I'd run very fast in the other direction, because she'll either take you to bed for it or cut your throat, and she won't have decided which until the knife is in her hand." {n}She smiles again.{/n} "That's what I love about her."''',
       c('"Thank you, Morevet."'))],
    requires=(DECLINED,), forbids=(RESTORED,), delay=24)


# --- Arueshalae, in Herrax's voice (acknowledgment only). -------------------------------------------------------------------

beat(B + "the_one_who_left", "The one who left", '"You knew Arueshalae."', [
    hx("start", '''"Knew her?" {n}Herrax laughs.{/n} "Honey, she lived under this roof for years. Long before my time in the chair. She tried everything the house had to offer, and a few things it didn't."
{n}She sips her wine.{/n} "And then one day she stopped. She said she wanted something the house doesn't sell. Nobody believed her. Succubi say that sometimes, the way mortals say they'll stop drinking."''',
       c('"She meant it."', "meant"),
       c('"What did the house think?"', "house")),
    hx("meant", '''"So I hear." {n}Her good eye is thoughtful.{/n} "She went hungry for some goddess, when she could have been eating out of my guests' hands. I still have people asking for her, lover. I ought to charge her for the business she cost me."''',
       c("Continue", "end")),
    hx("house", '''"The house thought she'd come back." {n}Herrax smiles.{/n} "They always come back. A succubus who leaves the Delights is like a drunk who leaves the tavern; she stands in the street for a while, being proud of herself, and then it rains."
"She hasn't. Not yet. There's money on it downstairs, and I've taken a share of the bets both ways, so I'll win whatever she does."''',
       c("Continue", "end")),
    hx("end", '''{n}She turns the cup in her fingers.{/n} "Tell her something from me, if she's still walking beside you. Tell her the madam says the room she had is still empty, and it'll stay empty, and she's not to take that as a kindness." {n}She drinks.{/n} "I don't do kindnesses. I keep inventory."''',
       c('"I\'ll tell her."'),
       c('"I don\'t think I will."', "wont")),
    hx("wont", '''"No," {n}Herrax agrees, amused.{/n} "Neither would I. That's why I asked you."''',
       c('"Clever."'))],
    requires=(LABYRINTH,), delay=24)


# Round 2 authored branches: physical history, not a second attraction test.
def _con_memory(event_id, node_id, text):
    event = next(s for s in SCENES if s["Id"] == event_id)
    node = next(n for n in event["Nodes"] if n["Id"] == node_id)
    if node is event["Nodes"][0]:
        # An entry speaks only the shared fact; the result is voiced on arrival
        # at either of its existing responses below.
        node["Text"] = node["Text"].replace("You sold me to her, and then you took the knife out of her hand", "You helped her set that night, and then you took the knife out of her hand")
        return
    variant = deepcopy(node)
    variant["Id"] += ".con_blown"
    variant["Text"] = text
    event["Nodes"].append(variant)
    for source in event["Nodes"]:
        for answer in list(source["Choices"]):
            if answer.get("Next") == node_id:
                alternate = deepcopy(answer)
                answer["Forbids"].append(BLOWN)
                alternate["Requires"].append(BLOWN)
                alternate["Next"] = variant["Id"]
                source["Choices"].append(alternate)


from copy import deepcopy
_con_memory(L + "the_courier", "reply", '"I tasted the lie, hot stuff. Shouted it to the whole house. She cut me anyway, and then she cut me again for the healer." {n}Rokhorn watches you fold your answer.{/n} "You went back to her hall with my claw across your cheek. I keep thinking about that."')
_con_memory(L + "the_courier", "b_offer", '{n}Rokhorn follows you into the square, beyond the sentries, with cold rain running off his hood.{/n} "You tried to sell me once. I tasted it and laughed you off my couch. Look what being right bought me." {n}He touches his twice-cut cheek.{/n} "Now I want to buy. Hear my offer, hot stuff."')
_con_memory(B + "rokhorn.whole", "start", "")

beat(B + "unpriced_guest", "The house still charges", '"Do your other guests get the same welcome?"', [
    hx("start", '"No. And neither do your friends. The Sinners charge by the night, the bar charges by the cup, and I take my share of both." {n}Herrax pulls you close enough to speak against your mouth.{/n} "Keep whoever you like in Drezen, lover. Buy whoever you like here. Try to pay me, and you go back downstairs."', c('"Then keep the bill for somebody else."'))], requires=(LABYRINTH, COMMITTED, MOREVET_DEAD, "herrax.present_now"), delay=24)


morevet_variants(SCENES)


# Authored court-letter answers: keep the packet's original nodes and answer indices.
def _court_answer_receipts():
    packet = next(s for s in SCENES if s["Id"] == COURIER)
    # The existing Morevet-absent Continue was appended at index 1 in round 2.
    # Add court answers only after that transformation has preserved it.
    for question in packet["Nodes"]:
        if question["Id"] in ("b_lady", "b_lady_hiding"):
            question["Choices"].extend([
                c('"The Lady and I are lovers."', "court_reply_truth", requires=("noct.complete",), forbids=("noct.closed",), flags=(L + "court.truth", L + "court.lover",)),
                c('"We are not lovers."', "court_reply_none", forbids=("noct.complete",), flags=(L + "court.truth",)),
                c('"Ask her what she wants from me."', "court_reply_evade", flags=(L + "court.evaded",)),
                c('"That is between the Lady and me."', "court_reply_refuse", flags=(L + "court.refused",)),
                c('"We were lovers. It ended."', "court_reply_none", requires=("noct.complete", "noct.closed"), flags=(L + "court.truth", L + "court.former",)),
            ])
    packet["Nodes"].extend([
    nar("court_reply_truth", '{n}You seal your answer separately from the house news. Rokhorn reads the address, then looks at you with sudden interest.{/n} "The Lady? Oh, mistress will enjoy that." {n}He tucks the sealed answer inside his coat.{/n}', c("Continue", "b_news")),
    nar("court_reply_none", '{n}You seal your answer separately from the house news. Rokhorn weighs the little packet in his hand.{/n} "No palace scandal? Mistress will be disappointed." {n}He puts it away unopened.{/n}', c("Continue", "b_news")),
    nar("court_reply_evade", '{n}Rokhorn reads the short answer before you seal it. His grin widens.{/n} "Sending mistress to ask the Lady herself? I would pay to watch." {n}He puts the answer away.{/n}', c("Continue", "b_news")),
    nar("court_reply_refuse", '{n}Rokhorn reads the short answer before you seal it.{/n} "A shut door. She does hate those." {n}His smile shows teeth as he puts it away.{/n}', c("Continue", "b_news")),
    ])
    for node in packet["Nodes"]:
        if node["Id"].startswith("court_reply_"):
            node["Choices"][0]["Forbids"].append(MOREVET_DEAD)
            node["Choices"].append(c("Continue", "b_news.morevet_absent", requires=(MOREVET_DEAD,)))
    from storylines import herrax_trickster
    ending = next(s for s in herrax_trickster.SCENES if s["Id"] == H + "epilogue.reachable")
    ending["Nodes"][0]["Paragraphs"].extend([
        dict(Text='{n}Herrax answered the court confession with a warning: "So the Lady has excellent taste for once. I expect she\'s quite annoyed with me."{/n}', Requires=[L + "court.lover"], Forbids=[]),
        dict(Text='{n}Herrax answered the news of the ended affair in a cramped line beneath her signature: "Then she can amuse herself elsewhere. I\'m busy."{/n}', Requires=[L + "court.former"], Forbids=[]),
        dict(Text='{n}Herrax sent the Commander\'s evasion back with a hole through the seal. "I asked you, lover. Not the palace. Your answer wasn\'t worth blunting my knife."{/n}', Requires=[L + "court.evaded"], Forbids=[]),
        dict(Text='{n}Herrax returned the refused answer unopened. On the outside she wrote: "Fine. Rokhorn\'s lies are more entertaining anyway."{/n}', Requires=[L + "court.refused"], Forbids=[]),
    ])
_court_answer_receipts()
