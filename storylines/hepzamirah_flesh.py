"""Hepzamirah in the flesh: the courtship after her return, by the forge in Drezen (Chapter 5).

Every scene sits on her presence in the smith's yard (hepzamirah_trickster.PRESENCE) and engages a canon anchor of hers:
- the body Mutasafen grew exactly as her father left her: crushed skull, broken horn, milk-white eye (Prison_HepzamirahGhost
  Cue_0001 5e4a94e4) and his hold on it, "Anything I make, I can unmake";
- her boast that she was the best of his brood, who "sacrificed my own mother to him, then did so with hundreds of my
  brothers and sisters" (Cue_0013 f99fcbc6), and her father's verdict, "Hepzamirah was more cunning and vicious"
  (Prison_Baph/Cue_0122 03997856) and "I possess none of a father's sentimentality" (Cue_0121 0cdc1a24);
- the archpriestess's call, which a demon lord "must answer" (Cue_0014 92529f16, Cue_0018 382857e6);
- the jailers who grovelled to her and then hounded her (Cue_0012 ac4fdb1e);
- Ygefeles's bloodline, which she swore to hunt to the last child (Hepzamirah_main/Cue_0047 f76c65cc; Woljif, Cue_0037);
- Ember's pity at her ghost (Cue_0020 22cf049d, Cue_0022 3e31d6e3);
- her voice: "Enjoy it while you can. Today I'm dead, tomorrow you will be too." (Cue_0030 dbbcd068).
Her villainy stays: she bargains, threatens, collects heads and enjoys it. Her affection, when it comes, is possessive.
"""
from story_format import c, n, p, scene
from storylines import hepzamirah_trickster as core
from storylines.hepzamirah_trickster import (ARMED, BESTED, BLOOD, BLOODLINE_KEPT, CALL_FORBIDDEN, CALL_SWORN, CLOSED,
                                              COMMITTED, CONFINED, RELEASED, COURIER_KILLED, COWED, CS, EMBASSY,                                               EVE_PROMISE, EYE_BURNED, EYE_KEPT, FAVOUR_OWED, FIRST, FLOWERS_KEPT,
                                              FOLLOWED, GRUDGE, HORN_CUT, HORN_KEPT, KNOWN, LAB, LANDLORD, LATE, LET_GO,
                                              LOOKED, LOOKED_AWAY, MGRUDGE, MORNING, OFFER, P, PICK, PICK_HELD, PICK_ITEM,
                                              RENT_REFUSED, RENT_TAKEN, RET, VIAL_FORGED, VIAL_PAID, WRONG_BODY, YIELDED,
                                              hz, lead, nar)

SCENES = []
MARKET = P + "flesh.the_market"
SISTER = P + "flesh.sister"
CORNER = P + "flesh.the_corner"
DRILL = P + "flesh.drill"
LETTER2 = P + "flesh.princess"
VORLESH = P + "bond.vorlesh"
SORTIE = P + "bond.sortie"
UNMADE = P + "bond.unmade"
FORGE = P + "flesh.the_nexus"
WEAPON = P + "bond.the_weapon"
CULT = P + "flesh.apostate"
SECOND_NIGHT = P + "bond.crooked"
EMBER_ASKS = P + "bond.less_sad"
NAMES = P + "bond.names"
UNSENT = P + "flesh.unsent"
ROOM = P + "bond.her_room"
GIFT = P + "bond.gift"
COUNCIL = P + "bond.map_table"
SONG = P + "flesh.the_song"
NEROSYAN = P + "bond.nerosyan"
TREATY = P + "bond.treaty"

CHAPLAINS = P + "flesh.chaplains"
MIRROR = P + "flesh.mirror"
RENT = P + "flesh.rent"
BLOODLINE = P + "flesh.bloodline"
FLOWERS = P + "flesh.flowers"
HORN = P + "flesh.the_horn"
CALL = P + "bond.the_call"
HUNT = P + "bond.the_hunt"
EYE = P + "bond.the_eye"
EVE = P + "bond.eve"



def yard(id, title, entry, nodes, requires, forbids=(), delay=24, any_groups=None, confined_ok=False):
    """A scene on her presence by the forge in Drezen (Chapter 5). Q8 (Sol INT): while the chaplains hold her in the
    cells (cost.confined) no yard beat opens until her release (flesh.released, 72 h after the choice)."""
    extra = dict(RequiresAnyGroups=[list(g) for g in any_groups]) if any_groups else {}
    if not confined_ok:
        forbids = (CONFINED, *forbids)
        extra["ForbidOverrides"] = {CONFINED: RELEASED}
    SCENES.append(scene(id, title, "Hepzamirah", 5, entry, nodes, requires=requires,
                        forbids=(CLOSED, *forbids), delay=delay, last=5, optional=True, Relationship="hepzamirah",
                        Chapters=[5], ContactUnit=core.BODY_UNIT, Areas=[core.DREZEN], InteractionHub=core.PRESENCE, **extra))


# --- 1. The first morning: the body, the brine, the itch of flesh. --------------------------------------------------------

yard(FIRST, "Flesh itches", '"How is the body?"', [
    *lead([("yard", nar, '''{n}She is sitting on the smith's quenching trough in a borrowed shift that does not close across her shoulders, eating a raw onion like an apple. There is still brine in her hair. The smith has moved his work to the far side of the anvil and hammers without looking up, the way a man hammers in the rain.{/n}
{n}Every so often she stops chewing and presses the heel of her hand hard against the ridge of scar on her skull, as if to make sure it is still there.{/n}''', None),
           ("yard_late", hz, '''"The jailers' whispers followed me out of the Labyrinth, whelp. Your name, over and over. I hear them in the anvil."''', LATE)],
          "itch"),
    hz("itch", '''"It itches." {n}She says it to the onion, with loathing.{/n} "Everything itches. The skin itches where the brine dried. The scar itches underneath, where he grew the bone back crooked on purpose. The eye that does not see itches most of all."
"My jailers could hurt a ghost, clown, the piss-drinking cowards. They hounded me into my corner, and when your angel screamed, even dead flesh came apart, and it hurt. But my ghost did not itch. It was never hungry. It never had to *sleep*. Then a clown comes along with a quill and gives me a body, and now I itch, and I am hungry, and I have to sleep." {n}She bites the onion again, savagely.{/n} "I had forgotten sleep. It is like dying, only you have to do it every night."''',
       c('"I can have a priest look at the eye."', "priest"),
       c('"You could have stayed a ghost."', "ghost"),
       c('[Sit on the trough beside her.]', "sit")),
    hz("priest", '''{n}The onion stops halfway to her mouth.{/n}
"A priest." {n}She says the word as if tasting something the onion left behind.{/n} "One of your Inheritor's little lamps, laying his hands on the face of Baphomet's daughter, and praying over it, and making it *pretty*. I would break his fingers one at a time and let him pray through the screaming."
"No. The eye stays. The scar stays. Mutasafen grew me as my father left me, to spite me, and I will wear his spite until I can wear his skin instead. No priest mends anything of mine. Remember that, worm. I will not say it twice."''',
       c("Continue", "hungry")),
    hz("ghost", '''"Stayed?" {n}She laughs, one short bark, and the smith's hammer misses a beat.{/n} "In the Labyrinth, with the jailers? They would have had me a thousand years, and my father would have walked past my corner once a century to see how I was keeping."
"No. I would rather itch. Itching is a thing that happens to the living. So is hunger, and so is revenge." {n}She takes another bite.{/n} "Especially revenge."''',
       c("Continue", "hungry")),
    nar("sit", '''{n}She shifts away from you on the trough, not far, the way a bull shifts in a pen: to keep the horns clear. The warped edge of the broken one is a hand's breadth from your ear.{/n}''',
        c("Continue", "sat")),
    hz("sat", '''"Brave." {n}It is not a compliment.{/n} "At Colyphyr there were overseers who would sit on the shaft-head beside the new diggers like that, to show them they were not afraid. I put the ones that bit on the deep face. They stopped biting."''',
       c("Continue", "hungry")),
    hz("hungry", '''{n}She finishes the onion, root and all, and wipes her hands on the borrowed shift.{/n}
"Your soldiers are frightened of me. Good. Your chaplains are frightened of me and pretending not to be. Better; I can smell it on the whole bleating herd of them. Your cook gave me a raw onion and a sausage on the end of a pitchfork." {n}Her lip curls.{/n} "I ate the sausage first."
"The crusade marches on the Worldwound soon, they say. Deskari's nest. The Threshold." {n}She looks at the forge, not at you.{/n} "Tell your smith he will forge me a pick, clown. A heavy one. I am not walking into Deskari's mouth with a pitchfork."''',
       c('"I\'ll speak to him."', "end_speak"),
       c('[Flirt] "You look fine with a pitchfork."', "end_flirt")),
    hz("end_speak", '''"Speak to him. He has not spoken to me since I arrived, except to pray, very quietly, into his bellows, the yellow-livered little shit." {n}She turns the milk-white eye on you.{/n} "Go on, then. Tell him that if he spits in his bellows again I will feed him his own tongs."''',
       c("[Leave her to the forge.]")),
    hz("end_flirt", '''{n}For a moment she genuinely does not understand. Then she does, and the look she gives you would have peeled paint off a Colyphyr mine-cart.{/n}
"I will remember that," {n}she says, very softly, which is worse.{/n} "When I have something heavier than an onion."''',
       c("[Leave her to the forge.]")),
], requires=("trickster.ever", RET), delay=12)


# --- 2. The pick: the smith who will not forge for a demon, the pick she lost in Colyphyr, and a bout in the yard. ------

yard(PICK, "A pick for Baphomet's daughter", '"About that weapon."', [
    nar("smith", '''{n}The smith has made her a heavy pick. It lies across two trestles in the yard, a long haft of ash and a head of black iron drawn to a spike on one side and a hammer-face on the other. He made it at night, and he will not hand it to her. He says so to you, not to her, in a low voice with his back to the far wall.{/n}
{n}The Lord of Beasts' cult was at Kenabres with the rest of the horde, he says. He will not arm Baphomet's archpriestess. He is sorry. He is not sorry.{/n}''',
        c('[Pay him] "The crusade will buy it. Name your price and stop praying at me."', "paid", crusade=("Finances", -200)),
        c('[Order him] "You forged it. It\'s crusade steel. The Commander decides who carries it."', "ordered"),
        c('[Give her back Dreadful Onslaught] "Keep your pick, smith. She has her own."', "returned",
          requires=(PICK_HELD,), remove_item=PICK_ITEM)),
    nar("paid", '''{n}He names a price that is an insult, and you pay it, and he takes the coin without counting it and goes inside. The pick stays on the trestles. He will not carry it to her. You do.{/n}''',
        c("Continue", "weigh")),
    nar("ordered", '''{n}He stiffens, and salutes, and says "Commander" in a voice with nothing in it, and goes inside. The pick stays on the trestles. He will not carry it to her. You do.{/n}''',
        c("Continue", "weigh")),
    nar("returned", '''{n}You unwrap it on the trestles beside the smith's work: the pick you took off her body in the mines of Colyphyr, black and heavier than any honest forge would make it, with the unholy sign of the Lord of Beasts still sunk in the iron behind the spike. The smith makes the sign of the Inheritor and goes inside without a word.{/n}''',
        c("Continue", "own")),
    hz("own", '''{n}She does not take it at once. She puts out one hand and lays it flat on the haft, the way a rider lays a hand on a horse she thought had been sold.{/n}
"Dreadful Onslaught." {n}Her voice has gone very quiet.{/n} "You looted it off my corpse. Of course you did. Crusaders always take the weapons and leave the bodies for the crows."
"And you *kept* it. From Colyphyr, through the Abyss, through my father's maze. You carried the pick that was meant to break your skull." {n}She closes her hand on the haft and lifts it, and it comes up off the trestles as if it weighed nothing.{/n} "You are either very sentimental or very stupid, whelp. I have not decided which I would prefer."''',
       c("Continue", "test", flags=(P + "pick_returned",))),
    hz("weigh", '''{n}She takes it from you one-handed, turns it, and finds the balance with two fingers under the head.{/n}
"Crusader iron. Too plain, too honest. A weapon that apologises for what it does." {n}She sights down the spike with the good eye.{/n} "It will do. For now. My own is somewhere between here and Colyphyr, being used to crack oysters by whoever looted my body."''',
       c("Continue", "test")),
    hz("test", '''"Now pick something up, clown. A sword, a stick, that pitchfork. My arms have not held a weapon since Colyphyr, and my arms were grown in a jar. I want to know what they remember before I take them to the Threshold."''',
       c("[Take up a practice sword.]", "bout"),
       c('"I\'m not fighting you."', "coward")),
    hz("coward", '''"You are fighting me or you are leaving, and if you leave I will find someone else to fight, and it will be one of your soldiers, and he will not enjoy it." {n}She spins the pick once; the air hums off the spike.{/n} "Pick. Something. Up."''',
       c("[Take up a practice sword.]", "bout")),
    nar("bout", '''{n}She comes at you exactly the way her bulk says she will not: fast, low, horns down, the pick choked up short on the haft. The first pass hooks the practice sword out of your guard and very nearly your hand with it. The second is a charge, head down, the way a bull charges, and she turns it aside a stride short of you, not to spare you but to see whether you flinched.{/n}''',
        c("[Athletics] Step inside the charge and put her on the flagstones.",
          check=dict(Skill="SkillAthletics", DC=25, Success="bested", Failure="thrown", CommanderOnly=True)),
        c("[Give ground, and let her have the yard.]", "yielded")),
    nar("bested", '''{n}You go in under the haft where the length of it is useless and hook her ankle, and a body grown in a jar has not yet learned the weight of its own horns. She goes down on her back on the flagstones with a sound like a dropped anvil, and you are on her chest with the practice sword across her throat.{/n}''',
        c("Continue", "bested_say")),
    hz("bested_say", '''{n}For a long moment she does not move. Her breath comes hard and hot against your wrist. Then her lip peels back from her teeth, and it is not quite a snarl.{/n}
"Horzalah could never do that," {n}she says.{/n} "She was stronger. My father always said so. She charged like a siege ram and she never once thought to go *under*."
{n}She shoves you off her chest with one palm, rises, and takes up the pick.{/n} "Again. And this time I will not be learning the horns."''',
       c("[Pick up your sword.]", "end", flags=(ARMED, BESTED))),
    nar("thrown", '''{n}You go in under the haft, and she is waiting for it. The pick's head catches your sword, the haft turns, and the yard turns with it, and then you are on your back on the flagstones with the hammer-face resting on your breastbone, precisely, like a seal on a document.{/n}''',
        c("Continue", "thrown_say")),
    hz("thrown_say", '''"There." {n}She leans on it, a little, until you feel the weight.{/n} "That is what my arms remember. Good. I was afraid he had grown me soft to spite me."
{n}She lifts the pick and offers you a hand up, and when you take it she does not let go at once; she turns your wrist over and looks at the pulse there, as she might once have looked at a slave's teeth.{/n} "You came in under. Nobody comes in under. Again."''',
       c("[Get up.]", "end", flags=(ARMED,))),
    hz("yielded", '''{n}She stops with the spike a finger's width from your collarbone and looks at you down the length of the haft.{/n}
"You gave me the yard." {n}There is no pleasure in it.{/n} "I thought Mutasafen harmless once. He let me think it for years, and used the years I gave him to steal my army."
"Do not ever let me win, worm. I will know, and I will remember who taught me to be careless."''',
       c("[Nod, and pick up your sword again.]", "end", flags=(ARMED, YIELDED))),
    hz("end", '''{n}It goes on until the smith's apprentice comes out to bank the forge and stands frozen in the doorway. By then there is blood on the flagstones, most of it yours, a little of it hers, and she looks at the little that is hers with interest, as if it were news.{/n}
"Red," {n}she says.{/n} "He made it red. I had wondered."''',
       c("[Leave her with the pick.]")),
], requires=("trickster.ever", RET, FIRST), forbids=(), delay=24)


# --- 3. The chaplains: they want her gone, or locked, or exorcised. The rename, again. ----------------------------------

yard(CHAPLAINS, "The chaplains' petition", '"The chaplains came to me about you."', [
    nar("petition", '''{n}Three chaplains of the Inheritor are standing in the smith's yard in their good surplices, as if for a funeral, with a petition. Forty names. They want the daughter of the Lord of Beasts out of Drezen before the crusade marches, or failing that, exorcised; or failing that, locked in the old cells under the citadel, with a ward on the door and a priest outside it, until the Threshold is won.{/n}
{n}Hepzamirah is grinding the spike of her pick on the smith's wheel with her back to them. The wheel shrieks every time the eldest chaplain begins a sentence.{/n}''',
        c("Continue", "priest")),
    n("priest", "Chaplain", '''"Commander. With respect. This creature was the high priestess of the Lord of Beasts, whose cult marched on Kenabres with the rest of the horde. She traded in mortal flesh in the markets of Alushinyrra. She boasts, in front of our soldiers, of feeding her own mother to her father." {n}The old man's hands are shaking, but his voice is not.{/n}
"The Inheritor asks us to forgive. She does not ask us to *house*. Whatever you have done to bring her here, and I do not ask what, the crusade cannot march with her at its back. Lock her in the cells. For the soldiers' sake, if not for ours."''',
       c("Continue", "her")),
    hz("her", '''{n}The wheel stops. She does not turn round.{/n}
"The cells," {n}she says to the pick.{/n} "Under the citadel. With a ward and a priest. Another cell. Your priests have very little imagination."
{n}She lifts the blade from the wheel and inspects the edge. A bead of water runs down it and falls.{/n} "Go on. Choose. They are waiting, and I am curious."''',
       c('[Back the chaplains] "Three nights in the cells, with a ward. Until the soldiers stop making the sign at you."', "confined",
         flags=(CONFINED,), alignment=("Lawful", 1)),
       c('[Intimidate] "Take your petition and go, Father. The next man who asks me to lock her up can share her cell."', "cowed",
         flags=(COWED,), alignment=("Evil", 1)),
       c('[Rename her rooms] "Her quarters are an embassy now. The Embassy of the Leavable Prison. Your jurisdiction ends at the door."', "embassy",
         flags=(EMBASSY,), mythic="Trickster", crusade=("Favors", -100))),
    nar("confined", '''{n}The chaplains bow and go to fetch the guard. She watches them go without expression, and sets the pick very carefully back on the trestles, spike down.{/n}''',
        c("Continue", "confined_say")),
    hz("confined_say", '''"Three nights." {n}She turns at last. The milk-white eye is on you.{/n} "You freed me from one prison and now you lend me to another, so that your soldiers can sleep. That is the most *Baphomet* thing anyone has done for me since I died."
"Your chaplain wants an apology? Bring him down here, worm. I will give it to him through his teeth." {n}She breathes out.{/n} "Very well. I will go quietly. Three nights, and I will remember every one of them, and when I come out your priests will wish you had sent them instead." {n}She walks past you toward the gate, and pauses close enough that you feel the heat of her.{/n} "You will come back for me, clown. Or I will come out, and I will not use the door."''',
       c("[Let the guard take her.]")),
    nar("cowed", '''{n}The eldest chaplain opens his mouth, and closes it, and looks at the other two, and the three of them go, holding the petition between them like a stretcher. At the gate the youngest looks back, and makes the sign of the Inheritor at you, not at her.{/n}''',
        c("Continue", "cowed_say")),
    hz("cowed_say", '''"Oh," {n}she says, and she is smiling; it pulls the scar tight and it is not a kind thing.{/n} "Oh, that was *lovely*. Did you see his hands? Forty names, and you sent them away like a cook sends away a beggar."
"My father's archpriests spoke to the faithful like that. I thought mortals could not do it. I thought you were all apologies." {n}She tests the point of the spike on her own thumb, and watches the red bead rise.{/n} "Do it again sometime. Somewhere I can watch properly."''',
       c("[Leave her smiling.]")),
    nar("embassy", '''{n}The eldest chaplain refuses to bow. An embassy needs a foreign power, he says; a name over a bedroom binds no court in Nerosyan. The court clerk nevertheless records your designation. For a week, favors will go into making the order hold inside Drezen.{/n}
{n}Hepzamirah takes the petition from the chaplain's hand. He leaves to protest to the court, watching her until he reaches the gate.{/n}''',
        c("Continue", "embassy_say")),
    hz("embassy_say", '''{n}She has put down the pick. She is looking at you as if you were a new kind of creature in the flesh market, one she cannot yet price.{/n}
"An *embassy*." {n}She tries the word the way she tried the onion.{/n} "You stole a wall and called it a door. You stole a body and called it a flat. Now you steal a bedroom and call it a country."
"My father would have killed you for this in the first hour. He would have been right to. You are dangerous, whelp. You make the names do things." {n}She takes up the pick again.{/n} "I am the ambassador, I suppose. What does an ambassador do?"''',
       c('"Here, my order protects her rooms. Elsewhere she carries her own blade."', "embassy_end")),
    hz("embassy_end", '''"Your order." {n}She rolls the petition tight and holds it over the forge until the signatures catch.{/n} "Then they can petition you again. I will be here to answer."
{n}The chaplain watches the last of his forty names burn from the gate.{/n}''',
       c("[Give her the petition.]")),
], requires=("trickster.ever", RET, FIRST, PICK), forbids=(), delay=24)   # Q8: she grinds the pick here


# Q8 (Sol INT): the three nights are served. Every other yard beat waits on this (see yard()).
yard(RELEASED, "Three nights", '"They let you out."', [
    nar("out", '''{n}The ward came off her door after three days. The chaplain who broke the chalk line did it with a broom handle, from as far away as a broom handle allows, and she walked up out of the cells past him without a word, through the citadel and across the city, and sat down on the smith's trough as if she had never left it. There is chalk on her knees. She has not brushed it off.{/n}''',
        c("Continue", "say")),
    hz("say", '''"Three nights. Your priests counted them in prayers. I counted the men outside the door." {n}The milk-white eye comes round to you.{/n} "Your chaplains prayed outside the door in shifts. The young one fell asleep at it, so I told him what his dreams meant, all night, in detail. He has asked for the Nerosyan road."
"You did not come down once. Good. I would have taken it for gloating." {n}She takes the pick off the trestles, where she left it spike down, and weighs it.{/n} "I came out by the door, clown, and the door is still on its hinges. Remember that I could have chosen otherwise. Remember it every time your chaplains sleep soundly."''',
       c("[Leave her to the forge.]")),
], requires=("trickster.ever", RET, CONFINED), delay=72, confined_ok=True)


# --- 4. The mirror: the face he grew her, and whether the Commander will look at it. ------------------------------------

yard(MIRROR, "The face he grew", '"You asked for a mirror."', [
    *lead([("mirror", nar, '''{n}She has taken the smith's polished shield down from its hook, the one he shows buyers, and propped it against the trough, and she is kneeling in front of it with the pick laid across her knees. She has been kneeling there some time. The smith's boy says she has not moved since noon.{/n}
{n}In the shield, the crushed side of her skull is a knotted ridge of scar from brow to crown. The broken horn ends in a splintered stump. The eye on that side is milk-white and fixed. The other side of the face is the one her father's cult bowed to.{/n}''', None),
           ("mirror_embassy", nar, '''{n}There is a board nailed to the post of her door now, painted in letters the smith's boy was paid to do: EMBASSY. Someone has scratched a sign of the Inheritor under it, and someone else has scratched a horned head over that.{/n}''', EMBASSY),
           ("mirror_confined", nar, '''{n}The marks of the chaplains' ward are still on the lintel of her door, three nights' worth of chalk, half rubbed out by a sleeve.{/n}''', CONFINED)],
          "face"),
    hz("face", '''"Do you know what he did?" {n}Her eye stays on the shield.{/n} "Mutasafen. He did not grow me as I was. He grew me as I was when my father finished with me in the mines. How he knew every splinter of it, I do not ask. He had years to buy a witness, and I gave him those years. He took the time to grow the *wound*."
"This eye was the last thing I lost. My father's hand came down on this side of my head, and I saw the hand coming with this eye, and then I did not see anything with it ever again." {n}Her fingers find the ridge of the scar and follow it up into her hair.{/n} "Mutasafen remembered. He wanted me to see it every morning in the shield. He is a very thorough man."''',
       c("Continue", "ask")),
    hz("ask", '''{n}At last she turns her head, so that the white eye is toward you and the good one is toward the shield.{/n}
"Everyone in this city looks at the other side. The chaplains, the soldiers, your smith. They look at the side that was pretty and they talk to it, as if the rest were a stain on a dress they are too polite to mention."
"Look at this side, worm. Properly. And then tell me what you see, and if you lie I will know, because I ran slaves at Colyphyr and I can hear a lie in an overseer's breathing."''',
       c('[Look at it properly.] "I see what he did to you. And I see that you\'re still here."', "looked", flags=(LOOKED,)),
       c('[Touch the scar.]', "touched", flags=(LOOKED,)),
       c('[Look away] "I see the woman who fed her mother to a god."', "away", flags=(LOOKED_AWAY,))),
    hz("looked", '''{n}She holds your eyes with her one good one until the silence between you has weight, and her face does not change at all.{/n}
"Still here." {n}She tests it.{/n} "That is a crusader's answer. A crusader looks at a burned village and says, *still here*, and it is meant to be a comfort to the people standing in the ashes."
"It is not a comfort. But it is not a lie either. At least you do not flinch. Keep looking. I want you to remember whose hand did this." {n}She turns back to the shield.{/n} "He counted what I gave him. Mother. Then the others. Look how he repaid me."''',
       c("Continue", "mother")),
    nar("touched", '''{n}She lets you. That is the first surprise. The scar is hot under your fingers, hotter than the rest of her, and ridged like a hide that has been badly tanned, and she holds absolutely still while your hand follows it up into her hair, the way an animal holds still when it has decided not to bite yet.{/n}
{n}When your fingers reach the stump of the horn she catches your wrist. Not hard. She holds it there, against the splintered bone, and closes the good eye.{/n}''',
        c("Continue", "touched_say")),
    hz("touched_say", '''"That hurts," {n}she says, without opening it.{/n} "Everything he grew hurts. Do not stop."
{n}And then, a long moment later, she takes your hand away herself and puts it back in your lap like something borrowed.{/n} "Do not grow proud of yourself, clown. This is not forgiveness. He counted what I gave him. Mother. Then the others. Look how he repaid me."''',
       c("Continue", "mother")),
    hz("away", '''{n}Her good eye narrows. Then she laughs, and it is not the bark from the trough; it is low and pleased and very unpleasant.{/n}
"Yes. That is what you see. That is what I *am*. Good. The others lie to me. They look at the pretty side and say *poor thing* and pity me, which is worse than a spear."
"You looked away from the scar and straight at the crime. My father would have liked you for that." {n}She turns back to the shield.{/n} "He counted what I gave him. Mother. Then the others. Look how he repaid me."''',
       c("Continue", "mother")),
    hz("mother", '''"I gave him my mother." {n}Her voice is quite level.{/n} "I thought that would make me his heir."
"I did the same with my brothers and sisters after, by the hundred. Every one of them was a gift, and every gift was a step closer. And when I had given him everything, he came to Colyphyr and killed me for losing one fight. Tell me, crusader, what should all that have bought?"
{n}She stands, and hangs the shield back on its hook, face to the wall.{/n} "That is my family, whelp. You asked for it by coming here. Now you have it."''',
       c('"Why tell me?"', "why"),
       c('[Say nothing, and stay.]', "stay")),
    hz("why", '''"Because you will hear it anyway. From the chaplains, from your soldiers, from Mutasafen when he writes to you again." {n}She takes up the pick.{/n} "I would rather you heard it from me, the way it happened. Let your priests call it what they like. They did not make the offerings. I did."
"There. Now you know what you took out of the Labyrinth. You may still put it back."''',
       c("[Leave her with the shield turned to the wall.]")),
    nar("stay", '''{n}You stay. She does not tell you to go. After a while she sits back down on the trough, with the pick across her knees, and you sit on the other end of it, and the smith hammers, and neither of you says anything until the forge is banked and the yard is dark.{/n}''',
        c("[Leave her in the dark.]")),
], requires=("trickster.ever", RET, PICK), delay=24)


# --- 5. The rent: she pays it the only way she knows. ---------------------------------------------------------------------

yard(RENT, "The first rent", '"You said you had something for me."', [
    nar("sack", '''{n}There is a sack on the trough, tied at the neck with a length of bell-rope. It is wet at the bottom. The smith's boy is sitting on the far side of the yard with his arms round his knees, very pale.{/n}''',
        c("Continue", "sack_say")),
    hz("sack_say", '''"Rent." {n}She nudges the sack with the haft of the pick.{/n} "The first real payment. Open it."
"There is a cellar under the old grain exchange, by the east wall, where three men of your crusade have been cutting a certain sign into their forearms at night and whispering my father's name. They thought the Commander had enough demons to fight outside the walls without looking under the floor." {n}She smiles the tight, scarred smile.{/n} "They knew my face from the altar-cloths. They were so pleased to see me. They thought I had come to lead them."
"I had not. I have brought you the priest. What is left of him." {n}She nudges the sack again.{/n} "The other two are still in that cellar, tied to their own altar, and they have had a whole night to think about what I am. They are yours to decide."''',
       c("Continue", "rent_prior", requires=(COWED,)),
       c("Continue", "rent_prior_embassy", requires=(EMBASSY,), forbids=(COWED,)),
       c("Continue", "choose", forbids=(COWED, EMBASSY))),
    hz("rent_prior", '''"You sent the chaplains off like beggars. So I thought you would understand a gift like this. A landlord who frightens priests should have a tenant who frightens cults."''',
       c("Continue", "choose")),
    hz("rent_prior_embassy", '''"The ambassador of the Leavable Prison has conducted a diplomatic mission to the Lord of Beasts' interests in your city. It went very well for the embassy."''',
       c("Continue", "choose")),
    hz("choose", '''{n}She is watching you with the good eye, and she is not smiling any more.{/n}
"My father's cultists, in your crusade's barracks, before you march on the Worldwound. You would have found them the day they opened a gate for Deskari's children, and not a day before."
"So. That is my rent. You may take it, and hang the head over the east gate for the others to see, as my father would, and I will go back down to the cellar and finish. Or you may be a crusader about it, and tell me I should have brought them all to your chaplains alive." {n}She shrugs.{/n} "It is too late for the priest. It is not too late for the other two. I am asking which kind of landlord you are."''',
       c('[Take the sack] "Hang it over the east gate. Let the others see."', "taken", flags=(RENT_TAKEN,), alignment=("Evil", 1)),
       c('"The crusade has courts, Hepzamirah. Next time, bring them alive."', "refused", flags=(RENT_REFUSED,), alignment=("Lawful", 1)),
       c('[Take the sack, and bury it quietly] "Thank you. Nobody will ever know you did this."', "buried", flags=(RENT_TAKEN,))),
    hz("taken", '''{n}She weighs you first, head tilted, the way she weighs everything. Then she laughs, low and delighted, and picks up the sack by the bell-rope and weighs it in her hand.{/n}
"The east gate. Where the new recruits come in." {n}She swings it once.{/n} "My father's archpriest could not have chosen better. They will make the sign at me for a month, and never again at you, because they will have seen what you let me do."
"You are not a crusader, clown. You wear one. I have always liked a disguise that fits."
{n}She goes back to the cellar before dawn. Nobody asks what she did there. By noon the chaplains have a list of eleven more names in her square, violent hand, and the provost's men spend a week arresting sappers who will not meet anyone's eye.{/n}''',
       c("[Let her take it to the gate.]")),
    hz("refused", '''{n}Her face does not move. The good eye is quite flat.{/n}
"Alive. So that your chaplains could weep over them, and your lawyers could argue, and the one that bit could go free in a month because he was drunk." {n}She sets the sack down on the trough, gently, as if it were something fragile.{/n}
"You are a crusader, then. At least with me. Very well. I will not bring you rent like this again." {n}She looks at the forge.{/n} "I will not stop collecting it. I will stop bringing it to you."
{n}The two in the cellar reach the chaplains alive, filthy and babbling. Under questioning they give up a second cell in the lower city, and a knight-chaplain you have never met sends you a stiff note of thanks, and a stiffer one asking how your tenant knew where to look.{/n}''',
       c("[Leave her with the sack.]")),
    hz("buried", '''"Nobody will know." {n}She repeats it slowly, as if checking whether it is a joke.{/n} "You would take the gift and hide the giving. That is not how my father's cult does things. We *want* the city to know."
"But I see why you do it. They would ask where your tenant goes at night, and you would have to lie, and you lie well, but you would rather not." {n}She pushes the sack toward you with the haft of the pick.{/n} "Bury it, then. I will know. That will be enough."
{n}The two in the cellar are found by a patrol the next morning, tied, alive, and so frightened that they confess to everything before anyone asks. The report says an anonymous tip. The chaplains are very pleased with themselves for a month.{/n}''',
       c("[Take the sack.]")),
], requires=("trickster.ever", RET, PICK), delay=24)


# --- 6. The bloodline: Ygefeles's great-grandson walks about in the Commander's party. -----------------------------------

yard(BLOODLINE, "Ygefeles's blood", '"You\'ve been watching my tiefling."', [
    hz("watching", '''"The thief in your company. The little tiefling with the mouth." {n}She is oiling the head of the pick with a rag, very slowly, the way a woman cleans a thing she intends to use soon.{/n} "He is Ygefeles's blood. My brother's grandson; my great-nephew, if you like, a thief. I swore in Colyphyr I would send my servants to Golarion to kill every last one of Ygefeles's offspring. I meant it. I still mean it."
"I had Ygefeles hunted down, to show my father that his line was weak. It seems his line is not finished. And now he walks past my door every morning, whistling, and calls me *auntie*."''',
       c("Continue", "want")),
    hz("want", '''{n}She puts down the rag.{/n}
"I want him, worm. I am not asking for permission. I am telling you, because I keep my word when it suits me, and this suits me. I want him dead before the Threshold, so that when my father is told his whole line is gone, it will be me who is left."
"Stop me if you can afford to."''',
       c('"Touch Woljif and the door is locked. From the outside. For good."', "locked", flags=(BLOODLINE_KEPT,)),
       c('[Rename him] "He\'s not Ygefeles\'s blood. He\'s a Jefto. Read the adoption papers. Different line entirely."', "renamed",
         flags=(BLOODLINE_KEPT,), mythic="Trickster"),
       c('[Offer her a bargain] "Leave him alone till after the Threshold, and I\'ll owe you a favour of your choosing."', "bargain",
         flags=(BLOODLINE_KEPT, FAVOUR_OWED), alignment=("Evil", 1))),
    hz("locked", '''{n}Her nostrils flare. For a moment the pick is not quite resting.{/n}
"A lock." {n}She says it very quietly.{/n} "You took me out of one cell, and now you threaten me with another, for a tiefling who picks pockets."
"Very well. That is a price I understand. My father set prices like that, and I always paid them, until I did not." {n}She picks up the rag again.{/n} "He may live, your tiefling, for as long as I am in your house. Tell him that. Tell him it is your doing and not my mercy. I will not have him thinking I have mercy."''',
       c("[Leave it there.]")),
    hz("renamed", '''{n}She stares at you. Then she stares at nothing for a while, and you can see her working through the steps of it, the way she must once have worked through a rite.{/n}
"A *Jefto*." {n}She says it with enormous disgust.{/n} "You would rename the whole of my great-nephew's bloodline to keep him out of my reach. You would make it so that when I kill him, I have not killed Ygefeles's line at all, only a thief, and there is no glory in that for anyone."
"You make the names do things. I hate it. I have hated it since the Labyrinth." {n}She returns to the rag.{/n} "Keep your Jefto. I do not waste a good blade on a thief."''',
       c("[Leave it there.]")),
    hz("bargain", '''{n}Something lights in the good eye that was not there a moment ago.{/n}
"A favour. Of my choosing." {n}She savours it.{/n} "That is the first sensible thing you have offered me. My father's whole court runs on favours owed. You pay them when you are called, and not before, and never in the currency you expected."
"Done. The tiefling lives until after the Threshold. After that, we shall see what I choose." {n}She holds out her hand, and when you take it, she does not shake it; she turns it palm up and presses her thumbnail into the centre until it marks.{/n} "There. Now it is written."''',
       c("[Take your hand back.]")),
], requires=("trickster.ever", RET, FIRST), forbids=("woljif.dead", "woljif.kicked_out"), delay=24)


# --- 7. The flowers: Ember, who pitied her ghost, and keeps bringing jars. -------------------------------------------------

def em(id, text, *choices, **kw):
    return n(id, "Ember", text, *choices, portrait="Ember", **kw)


yard(FLOWERS, "Wildflowers", '"Ember\'s been visiting you."', [
    nar("jar", '''{n}The jar of wildflowers is on the trough again. It is a different jar; the last one, the smith's boy says, went over the yard wall. Ember is sitting on the upturned bucket beside the forge with her knees up, perfectly content, watching Hepzamirah grind the spike of her pick as if it were a pleasant thing to watch.{/n}''',
        c("Continue", "ember")),
    em("ember", '''"I brought her the blue ones today. The blue ones don't mind being thrown." {n}Ember smiles up at you.{/n} "She told me I was a stupid little elf who ought to be put in a jar myself. But she didn't throw them. I think she's getting used to them."''',
       c("Continue", "hep")),
    hz("hep", '''"I am not getting used to anything." {n}The whetstone stops.{/n} "She comes here, tells me about the weather and a cat, and calls me a poor thing. I could tear her throat out. She brings another jar."
"I told her about my mother. About the mines. She listened, then asked if I liked blue." {n}She grips the stone.{/n} "Explain her to me, clown."''',
       c('"She isn\'t for anything. She just thinks nobody should be alone."', "alone"),
       c('"She\'s for you to leave alone. Hurt her and our terms are done."', "warned")),
    hz("alone", '''"Nobody should be alone." {n}She glances at Ember, humming on her bucket.{/n} "Tell that to my father's jailers. They would have found her company very useful."
"She keeps giving me things. There is nothing left for me to take. I cannot stand it."''',
       c("Continue", "keep")),
    hz("warned", '''{n}The good eye comes round to you, and the soldiers at the gate find something else to watch.{/n}
"You think I would hurt *her*?" {n}Then, surprisingly, the look turns to contempt.{/n} "There is nothing to take from her. She has nothing she will not give away. Hurting her would be like robbing a beggar who keeps handing you his bowl."
"No. I will not hurt her. I will throw her jars over the wall until she stops. She will not stop." {n}She sounds almost tired, which she has not allowed herself since the Labyrinth.{/n}''',
       c("Continue", "keep")),
    nar("keep", '''{n}She picks up the jar of blue flowers and turns it in the light, as if trying to work out what it costs and who is paying.{/n}''',
        c('"Keep them."', "kept", flags=(FLOWERS_KEPT,)),
        c("[Say nothing.]", "thrown")),
    nar("kept", '''{n}She does not answer. She takes the jar inside. When the door has shut behind her Ember claps her hands, once, very quietly, as if in a temple.{/n}''',
        c("[Leave them to it.]")),
    nar("thrown", '''{n}She throws it over the yard wall. It breaks on the far side. Ember sighs, stands up, dusts off her skirt, and goes to see if there are any blue ones left on the hill.{/n}''',
        c("[Leave them to it.]")),
], requires=("trickster.ever", RET, FIRST, "ember.present"), delay=24)


# --- 8. The horn: the broken stump, and what she lets the Commander do to it. ------------------------------------------

yard(HORN, "The broken horn", '"The smith says you asked for a saw."', [
    nar("saw", '''{n}She has a bone-saw from the infirmary on the trough beside her, and a rasp, and a pot of the smith's grease. The broken horn's stump sticks out of the ridge of scar like a snapped spar, splintered along its length, and she has been working at it with the rasp until her hand bled, and stopped.{/n}''',
        c("Continue", "catch")),
    hz("catch", '''"It catches," {n}she says, without greeting.{/n} "On the door, on the pillow, on the hood of every garment your quartermaster gives me. The splinters grow back. Mutasafen grew them to grow back." {n}She holds up the rasp.{/n} "I cannot see that side. I cannot reach the back of it. The smith will not touch me and I will not have a priest."
"So. You." {n}She holds out the saw, handle first.{/n} "Take it off level. Not the root. Only the splinters. If you slip I will know you meant it."''',
       c('[Take the saw.]', "cut"),
       c('"Leave it. It\'s yours. He wanted you to hate it."', "leave")),
    nar("cut", '''{n}She sits on the trough and bends her head, and puts her forehead against your chest so that the stump is under your hands, and holds very still. The horn is warm and heavy and smells of her. The saw goes through the splinters like green wood.{/n}
{n}Halfway through her teeth close on a curse. Her hands grip your hips to hold her head steady. You keep sawing. She does not let go until the last splinter falls.{/n}''',
        c("Continue", "cut_say")),
    hz("cut_say", '''{n}She lifts her head. Her face is quite composed except for the breathing.{/n}
"Level?" {n}She touches it. It is.{/n} "Level." {n}Her hands are still on your hips. She seems to notice this some time after you do, and looks down at them with the same interest with which she looked at her own red blood, and does not move them.{/n}
{n}She lets you go at last.{/n} "You kept the root. Good. Slip next time, whelp, and I will take a finger."''',
       c("[Put down the saw.]", flags=(HORN_CUT,))),
    hz("leave", '''{n}She stares at you. Then she looks at the saw in her own hand as though it had spoken.{/n}
"He wanted me to hate it." {n}She repeats it slowly.{/n} "Yes. He did. Everything he grew, he grew for me to hate."
"That is a very cruel thing to say to a woman with a saw in her hand, clown." {n}She puts the saw down, carefully, on the far side of the trough.{/n} "It is also true. I will keep it. It will catch on your pillow as well as mine. See how you like it."''',
       c("[Leave her with the rasp.]", flags=(HORN_KEPT,))),
], requires=("trickster.ever", RET, MIRROR), delay=24)


# --- 9. The morning after: the door, the city, and what she will not pretend. -----------------------------------------

yard(MORNING, "The door", '"About last night."', [
    *lead([("door", nar, '''{n}Her door is off its top hinge. It hangs in the frame at an angle, the way doors hang in a sacked town, and the smith's boy has been told not to fix it. Inside, the cot is in two pieces. There is a long scrape down the plaster above where it stood, at exactly the height of a horn.{/n}
{n}She is sitting on the trough in the morning cold, wearing your cloak, which is much too small for her and which she has put on inside out. She is eating your breakfast. She does not offer to share it.{/n}''', None),
           ("door_horn", nar, '''{n}There is also a tear in your pillowcase, which you found at dawn, and a long splinter of horn in it. She kept the splinters. She warned you.{/n}''', HORN_KEPT),
           ("door_confined", hz, '''"I broke the door," {n}she says, before you can.{/n} "I told you I am not a woman who forgets a lock. Now it cannot be locked. From either side. That is how I like doors."''', CONFINED)],
          "city"),
    hz("city", '''"Your whole city knows." {n}She says it with deep satisfaction.{/n} "The smith's boy heard the cot go. The watch on the east wall heard the door. By noon your chaplains will be telling each other that Baphomet's daughter has the Commander of the crusade, and by the evening bell half of them will be praying for you, and the other half will be writing to Nerosyan and wondering whether I fuck the way I fight."
"My father's cult had a word for it, when an archpriest took a consort from among the enemy. It was not a kind word. It meant the consort had been *collected*." {n}She licks honey off her thumb.{/n} "Let them think it. They will look at you differently. Some of them will finally look at you properly."''',
       c('[Let them talk] "Good. Let them look."', "talk", flags=(KNOWN,), crusade=("Favors", -100)),
       c('"I\'d rather the chaplains didn\'t write to Nerosyan."', "hush"),
       c('[Flirt] "Collected. I\'ve been called worse."', "collected", flags=(KNOWN,), crusade=("Favors", -100))),
    hz("talk", '''"Good." {n}The scar pulls her mouth into the tight smile.{/n} "I have never been anyone's secret. I would not know how to begin. My father kept me at his left hand where every cultist in Colyphyr could see me, until the day he did not."
{n}She sets down the empty bowl.{/n} "You will pay for it at court. The clerks will lose your requisitions. A few of your lords will stop sending their sons. Pay it. I am worth more than their sons."''',
       c("Continue", "rules")),
    hz("hush", '''{n}Something goes out of her face, and something colder comes into it.{/n}
"Ah. A secret, then. The crusader's shameful little appetite, behind a broken door." {n}She stands, and your cloak tears at the shoulder.{/n}
"I will not be hidden, worm. Not by my father, not by you. I will not make a scene either, for your sake. But I will not pretend in the yard that I did not break your bed. If your chaplains ask me, I will tell them. In detail."''',
       c("Continue", "rules")),
    hz("collected", '''{n}She laughs, low and pleased.{/n}
"Worse. Yes, I expect you have. Your court calls you *the clown* behind your back; I only say it to your face." {n}She reaches over and straightens your collar, as though it were a leash that had twisted.{/n} "Collected is better than clown. It means they can see whose hands are on you. Let them choke on it."
"You will pay for it at court. Pay it."''',
       c("Continue", "rules")),
    hz("rules", '''"Now listen, because I will say this once, the way my father said things." {n}She holds up one thick finger.{/n}
"You do not come to my door as a Commander. You come as a clown, or not at all. You do not give me orders in my room. You do not pity me in my room." {n}A second finger.{/n} "And when you go to the Threshold, I go first. Not beside you. First. I was my father's spearhead for longer than your crusade has had a name. I will not stand behind a mortal in a fight."
"Those are my rules. They are not negotiable. You may make rules of your own, if you like. I will consider breaking them."''',
       c('"Agreed. And my rule: you come back."', "back"),
       c('"Agreed."', "agreed")),
    hz("back", '''"Come back." {n}She tastes the words and does not like them.{/n} "That is not a rule. That is a prayer. You are praying at me, clown, like your chaplains."
{n}She takes the torn cloak off, folds it very badly, and gives it back.{/n} "Very well. I will consider breaking it."''',
       c("[Take the cloak.]")),
    hz("agreed", '''"Agreed," {n}she repeats, as if checking the weight of a coin.{/n} "No haggling. You are a very bad merchant, whelp. At Colyphyr you would have been on the deep face by the end of the first day, you soft-handed fool."
{n}She takes the torn cloak off, folds it very badly, and gives it back.{/n} "Now go and be a Commander somewhere else. I have to find out how to fix a cot without a smith."''',
       c("[Take the cloak.]")),
], requires=("trickster.ever", COMMITTED), delay=6)


# --- 10. The call: the archpriestess's right, and whether she will use it. ----------------------------------------------

yard(CALL, "The archpriestess's call", '"You were praying. Out loud."', [
    nar("rite", '''{n}She is kneeling in the yard at dusk with the pick laid in front of her, head down, horns toward the forge, and she is speaking in a language that makes the smith's dog go under the anvil and stay there. It is not a prayer. It sounds like a prayer the way a bull's bellow sounds like a word.{/n}
{n}She stops before she reaches the end of it. She stays kneeling for a while afterwards, breathing hard, both hands flat on the flagstones.{/n}''',
        c("Continue", "call")),
    hz("call", '''"When he made me his archpriestess, he said the title would grant me protection of a rare kind," {n}she says, without looking up.{/n} "Every archpriest of a demon lord may summon their master in their hour of need, and the master must answer. He cannot refuse."
"I called him once. In Colyphyr, with your crusaders at my throat. And he came, because he had to. He came to betray me. Vorlesh's work was worth more to him than I was." {n}She looks at her hands.{/n} "So I do not know if I am still his archpriestess. I do not know if the call is still mine. I got as far as his name just now. Then I stopped."''',
       c('"What happens if it\'s still yours?"', "if")),
    hz("if", '''"Then one day I say the end of the rite, and he comes, again, because he must. Here, or wherever I am standing. This time I will not be on my knees in a mine asking him to save me." {n}She lifts her head, and the good eye is bright.{/n}
"This time he will look at me. Properly. I will ask him why he came to kill me instead, and whatever he answers, I will try to kill him."
"I will fail, probably. He is a god and I am a woman grown in a jar." {n}She shrugs.{/n} "But he will have to *come*. He came once and thought I would still kneel. If he comes again, I will show him what that cost."''',
       c('[Swear] "When you call him, I\'ll be standing where he can see me."', "sworn", flags=(CALL_SWORN,)),
       c('"You gave me terms. Your father is yours. I won\'t touch it."', "hers"),
       c('[Forbid it] "Not while you\'re under my roof. I won\'t have Baphomet in Drezen."', "forbidden", flags=(CALL_FORBIDDEN,))),
    hz("sworn", '''{n}She stares at you. Then she laughs, and it goes on too long, and at the end of it she wipes her good eye with the heel of her hand.{/n}
"Where he can see you. A mortal, a clown, Areelu's work, walking, standing beside the daughter he threw away, grinning at the Lord of Beasts." {n}She shakes her head slowly.{/n} "He would hate that more than the dying. He would hate it more than the pick."
"Yes. Stand there. I will hold you to it." {n}She stands, and takes up the pick.{/n} "Not today. After the Wound. I will not give him your army to hide behind. Keep yourself useful until then."''',
       c("[Leave it there.]")),
    hz("hers", '''"Mine." {n}She tests the word, as she tested everything.{/n} "You remembered whose quarry he is. Good. I will remember too."
"Very well. The call is mine, and the day is mine, and you will not bargain with him over my head." {n}She stands, and takes up the pick.{/n} "I will tell you when. Probably afterwards."''',
       c("[Leave it there.]")),
    hz("forbidden", '''{n}The good eye goes flat and dark, and for a moment she is only the woman in Colyphyr.{/n}
"Under your roof." {n}Very quietly.{/n} "You gave me terms, clown. *My father is mine*. You agreed to it in front of the smith. And now you take it back, because you are afraid of what he would do to your pretty city."
{n}She stands. She is a head taller than you and the pick is in her hand.{/n} "I will not call him in Drezen. I will give you that, because I want him cornered, not loose in a city where he can buy a thousand shields. But you broke a term, and I do not forget a broken term any more than a lock. I will be collecting on this one."''',
       c("[Let her go inside.]")),
], requires=("trickster.ever", COMMITTED, MORNING), delay=24)


# --- 11. The hunt: one of Mutasafen's bodies, and the term that nobody follows. ------------------------------------------

yard(HUNT, "Nobody follows", '"You\'re leaving."', [
    *lead([("pack", nar, '''{n}She has a pack on the trough: rope, a lantern, three days of the quartermaster's hard biscuit, and a jar of lamp oil. The pick is already over her shoulder. The sky over the Worldwound is the colour of a bruise, the way it is every evening now, and the crusade's drums are practising for the march.{/n}''', None),
           ("pack_killed", hz, '''"The Apprentice told me where one of them is, before I sent his eyes to his master. He was very forthcoming at the end. They always are."''', COURIER_KILLED),
           ("pack_forged", hz, '''"Your vial of wine went north, to a cave in the Worldwound, to a bench with a body on it that looks exactly like Mutasafen. I had the smith's boy follow the carter. He was very proud of himself."''', VIAL_FORGED),
           ("pack_lab", hz, '''"Your crusade funded him a laboratory, worm. Laboratories have addresses. Your own clerks wrote it down, and your own clerks will sell anything for a drink."''', LAB)],
          "where"),
    hz("where", '''"One of his bodies. A spare, in a cave on the edge of the Worldwound, two days' ride north, in a vat, with a guard of vrocks who do not know what they are guarding." {n}She checks the edge of the spike with her thumb.{/n}
"The revival system I created for myself is flawless. That is what he wrote to me. Flawless. I intend to go and break a piece of it, so that when he dies next, he has one fewer place to wake up."
"And you know the term. When I go for Mutasafen, nobody follows. I am telling you, so that you know where I have gone. I am not asking you to wish me luck. Luck is for mortals."''',
       c('[Let her go] "Five days. Bring me back something."', "go", flags=(LET_GO,)),
       c('[Stealth] Agree, and follow her anyway, at a distance, on the north road.',
         check=dict(Skill="SkillStealth", DC=30, Success="shadow", Failure="caught", CommanderOnly=True)),
       c('"Take a squad of the crusade\'s scouts. Not to follow. To hold the horses."', "scouts")),
    hz("go", '''"Something." {n}The scar pulls her mouth.{/n} "Yes. I will bring you something. You will not like it."
{n}She shoulders the pack and goes out through the yard gate without looking back, and the watch on the north road lets her through without a word, because the watch on the north road has heard about the cot.{/n}''',
       c("[Watch her go.]")),
    nar("shadow", '''{n}If she knows you are there, she does not show it. She does not look back once in two days. On the second night, in the lee of a black ridge above the cave, you watch her go down alone into the dark with the lantern, and hear what happens to the vrocks, and see, through the cave mouth, what happens to the thing in the vat. She is thorough. It takes a long time.{/n}
{n}You ride back ahead of her and are in the yard, bored, when she comes in.{/n}''',
        c("[Say nothing.]", flags=(FOLLOWED,))),
    hz("caught", '''{n}On the first night her voice comes out of the dark beside your fire, from somewhere you had not thought anyone could stand.{/n}
"I heard your horse on the first day." {n}She steps into the light with the pick over her shoulder.{/n} "One term. I gave you *one term* about Mutasafen, and you could not keep it for one day."
"Go home, clown. If I see you on this road again I will break your horse's legs, and then I will carry you back to Drezen across my shoulders like a stolen sheep, and your whole crusade will see."''',
       c("[Go home.]", flags=(FOLLOWED,))),
    hz("scouts", '''"Horses." {n}She considers it, the way she considers every gift, turning it over to look for the hook.{/n} "Horses are not following. Horses are furniture. Very well. Two scouts, to hold the horses at the foot of the ridge. If either of them comes up the ridge, I will send you his horse, and not him."
{n}She shoulders the pack.{/n} "You are learning, whelp. You found the one gift the term does not forbid."''',
       c("[Send for the scouts.]", flags=(LET_GO,), crusade=("Favors", -50))),
], requires=("trickster.ever", COMMITTED, MORNING), delay=24)


# --- 12. The eye: what she brings back, and the hold that did not close. -------------------------------------------------

yard(EYE, "Something you will not like", '"You\'re back."', [
    *lead([("home", nar, '''{n}She comes into the yard five days after she left, on foot, having eaten the horse's feed and then, apparently, the horse's patience; it came home the day before without her. There is soot in the scar on her skull and dried black blood to the elbow. She sets a jar on the trough.{/n}
{n}In the brine is a single eye, pale grey, with a surgeon's fine stitches still in the lid. Beside it, on a cord, hangs a crystal-cutter's lens.{/n}''', None),
           ("jar_followed", hz, '''"You followed me. Do not bother lying, clown. I smelled your horse when the wind turned." {n}Her mouth twists.{/n} "One term, and you could not keep it. I will remember that the next time you ask me to keep one of yours."''', FOLLOWED)],
          "eye"),
    hz("eye", '''"His. Well. One of his. The spare in the vat." {n}She taps the jar with one fingernail.{/n} "He was not awake. He will be, somewhere else, in another body, and when he needs that body he will find what I left of it, and he will know who did it, because I painted a horned head on the vat in his own blood."
"There were two more vats in the cave, empty, clean, still warm. Waiting for something." {n}She looks at the jar, not at you.{/n} "I think he was growing someone else. I burned them."''',
       c("Continue", "seized")),
    hz("seized", '''"And then, when I cut the eye out of him," {n}she says, in exactly the same voice,{/n} "this body tried to stop my heart."
{n}She holds out her left hand. On the inside of the wrist, under the skin, where there was nothing before, is a pale mark like a little seal, already fading.{/n} "*Anything I make, I can unmake.* He wrote it on me when he grew me. I felt it close like a fist. I lay on the floor of that cave with his spare's blood in my mouth, and I thought: so this is how it ends, again, in a mine, again, at the hand of a man I made."
"And then it let go. It opened, as if it had been told there was nothing in the room that belonged to it." {n}She looks at you at last.{/n} "No spare keys, you said, over the crate. I thought it was one of your jokes."''',
       c('"It was one of my jokes."', "joke"),
       c("[Take her wrist, and look at the mark.]", "wrist")),
    hz("joke", '''"Then your jokes keep better terms than my father did." {n}She sounds angry about it.{/n} "His promises did not hold. Mutasafen's did not. The Inheritor's priests say hers do, but only if you are good, which rather spoils them."
"I do not trust a thing I cannot explain, worm. I will be watching that mouth of yours very closely from now on."''',
       c("Continue", "rent_eye")),
    nar("wrist", '''{n}She lets you take it. The mark is cool and slightly raised, like a scar from a brand that has not quite healed, and while you watch it fades until there is only her skin, hot and ordinary, and the pulse under it going hard.{/n}
{n}She does not take the wrist back. She turns her hand over in yours, slowly, and closes her fingers round your own wrist in turn, exactly as she did in the yard the day she stayed.{/n}''',
        c("Continue", "rent_eye")),
    hz("rent_eye", '''"The eye is for you," {n}she says.{/n} "A trophy. The best I have taken. Keep it on your shelf, where he can see out of it, if he ever thinks to look. Or burn it. I do not care which. I only wanted you to have it first."''',
       c('[Keep it] "On the shelf. Facing the door."', "kept", flags=(EYE_KEPT,), alignment=("Evil", 1)),
       c('[Burn it in the forge.]', "burned", flags=(EYE_BURNED,)),
       c('[Give it back] "You keep it. You earned it."', "hers")),
    hz("kept", '''"Facing the door." {n}She actually laughs.{/n} "So that everyone who comes to your quarters has to walk past it. So that your chaplains see it every time they come to pray at you."
"Let them look. Let them wonder whose eye is next." {n}She pushes the jar toward you.{/n} "Taken in full, worm."''',
       c("[Take the jar.]")),
    nar("burned", '''{n}You put the jar in the heart of the forge. The glass cracks, the brine boils off in a hiss of steam that smells of formaldehyde, and the eye goes black and then goes. She watches it without expression. Afterwards she picks the lens off the trough and hangs it round her own neck on its cord.{/n}''',
        c("Continue", "burned_say")),
    hz("burned_say", '''"Good," {n}she says.{/n} "Now there is nothing of him in this yard, except me."''',
       c("[Stay with her by the forge.]")),
    hz("hers", '''{n}Her good eye narrows, measuring.{/n}
"Earned it." {n}She takes the jar back and turns it in her hands, and the grey eye turns in the brine and looks at the forge.{/n} "You refuse it? Fine. I will keep his eye. You can watch me take the other one."''',
       c("[Leave it with her.]")),
], requires=("trickster.ever", COMMITTED, HUNT), delay=120)


# --- 13. The eve: the Threshold, and where her soul goes if this body dies. ----------------------------------------------

yard(EVE, "Before the Threshold", '"When we march."', [
    *lead([("eve", nar, '''{n}The wagons for the Threshold are being repaired. When the crusade marches, they will need to hold. The yard is full of wagons, the smith's hammer going all night, the chaplains singing somewhere across the city. She has sharpened the pick until the spike shines. She is sitting on the trough with it across her knees, not doing anything, which you have never once seen her do.{/n}''', None),
           ("eve_eye", nar, '''{n}The crystal-cutter's lens hangs round her neck on its cord. She keeps touching it, the way soldiers touch a charm.{/n}''', EYE_BURNED),
           ("eve_sworn", hz, '''"Remember that you swore. Where he can see you. Not tomorrow. After."''', CALL_SWORN)],
          "soul"),
    hz("soul", '''"I have thought about it," {n}she says,{/n} "and I will tell you, because you will not think of it yourself. You never think of the price until it is in front of you."
"I am a nephilim. If this body dies at the Threshold, and his claim on me survived the escape, my soul does not go to your Pharasma. It goes back to my father's prison, to my corner, to the jailers. Everything he owns comes home to him. That is his rule." {n}Her hand is white on the haft.{/n} "I have been dead once. I did not mind the dying. I minded the corner."''',
       c('"Then I\'ll steal you out again. It\'s Leavable. I named it."', "again"),
       c('"Then don\'t die."', "dont"),
       c("[Take her face in your hands. Both sides.]", "face")),
    hz("again", '''"Steal me out again." {n}She says it slowly.{/n} "Walk into my father's prison a second time, past his jailers, with your quill and your jokes, and take his daughter out of her corner a second time, just to be *rude*."
{n}Something happens to her face that the scar was not grown to allow. It is not a smile. It is nearer to pain.{/n}
"Who said a trick is less impressive the second time." {n}She puts the pick down on the flagstones.{/n} "You would. I know you would. Then come armed, clown, and come quickly. I will not spend another night listening to his wretches, and I will not be stolen out of that place by anyone but you."''',
       c("Continue", "last", flags=(EVE_PROMISE,))),
    hz("dont", '''"*Don't die.*" {n}She repeats it with enormous scorn.{/n} "That is what your chaplains say to the recruits, and then they bury them."
{n}And then, after a moment, lower:{/n} "But from you it sounds like everything else you promise, as if it were a trick you already know how to do. Very well. I will not die. I will make the demons do it instead. I am good at that."''',
       c("Continue", "last")),
    nar("face", '''{n}She lets you. The scarred side is hot under your palm, and the milk-white eye does not close, and the good one does. The stump of her horn rests against your wrist. She breathes against your mouth without kissing you, three breaths, four, the way the forge breathes when the bellows stop.{/n}''',
        c("Continue", "face_say")),
    hz("face_say", '''"Both sides," {n}she says, against your mouth.{/n} "Not the pretty one. Both."
"Remember this face. Both sides. If he tears it apart again, I want you to know exactly what you are avenging." {n}The good eye opens.{/n} "And you will come for me. Say it."''',
       c('"I\'ll come."', "last", flags=(EVE_PROMISE,))),
    hz("last", '''{n}She stands, and takes up the pick, and puts her free hand on the back of your neck, hard, the way she held your wrist the day she stayed.{/n}
"First," {n}she says.{/n} "I go first. Into Deskari's mouth, into Areelu's laboratory, into whatever the Worldwound has left. You come behind me with your jokes, and when it is over you will find me standing on something large and dead, and you will make a joke about it, and I will pretend to hate it."
"That is the plan. This time I choose what the victory is for." {n}She lets go.{/n} "Go and sleep, whelp. I will keep watch. I do not need to sleep tonight. I have had enough of dark corners."''',
       c("[Leave her keeping watch.]")),
], requires=("trickster.ever", COMMITTED, MORNING), any_groups=[[EYE, CALL]], delay=24)


# --- 14. The market: a woman she once sold, in the Commander's city. ----------------------------------------------------

def woman(id, text, *choices, **kw):
    return n(id, "Mendevian woman", text, *choices, **kw)


yard(MARKET, "Stock that bit", '"There\'s a woman at the gate asking for you."', [
    nar("gate", '''{n}The woman at the yard gate is Mendevian, forty or so, in the grey of the crusade's laundry, and she is holding a laundry paddle the way a soldier holds a spear. There is an old brand on the back of her neck, just visible above the collar: a horned head in a circle. The watch has let her through because she asked for the Commander, and then stayed near, because of the paddle.{/n}
{n}Hepzamirah has stopped grinding the pick. She is looking at the brand.{/n}''',
        c("Continue", "woman")),
    woman("woman", '''"Three years. Three years in the crystal pits under Colyphyr, Commander, hauling Nahyndrian stone up the shafts by lamplight, until the crusade took the island and the gates came off." {n}Her voice is quite steady.{/n} "She came down once a month. She looked at our teeth. She had the ones who fought dragged to the deep face and left there, where the rest of us could hear."
"I came up out of the Abyss with the crusade's wounded and I have done laundry in this city every day since, so as never to think about her again. And now she is in the Commander's yard, with a crusade weapon in her hand. Tell me why."''',
       c("Continue", "hep")),
    hz("hep", '''{n}Hepzamirah stands up. She does it slowly, so that the woman can see the whole of her rising, and the paddle comes up in answer.{/n}
"I remember the shafts under Colyphyr," {n}she says.{/n} "I do not remember you. There were a great many of you. You all had teeth." {n}She tilts her head, the milk-white eye toward the woman.{/n}
"I will not apologise, if that is what you came for, you grey little scrap. I took what my father's cult sent down, and I worked it till it broke, and if I stood at the head of that shaft tomorrow I would work you down it again. Hit me with your stick if you like. It will not change a single thing I did."''',
       c('[Stay out of it] "Go on, then. She says it won\'t change anything. Find out."', "swing", flags=(P + "market_struck",)),
       c('[Stand between them] "Nobody hits anybody in my yard. Hepzamirah, sit down."', "between"),
       c('[Pay the woman] "The crusade owes you three years. Take this, and take the day off."', "paid", crusade=("Finances", -150),
         flags=(P + "market_paid",))),
    nar("swing", '''{n}The woman looks at you as if you had said something in a language she used to speak. Then she swings, with her whole back in it, a laundress's swing, and the paddle comes down at the scarred side of Hepzamirah's face.{/n}
{n}It never lands. Hepzamirah's hand closes on the haft in the air with a slap like a door shutting. She turns the paddle, and the woman's wrist goes with it, and the sound the wrist makes carries the length of the yard. The woman screams. Somewhere by the gate a sentry drops his spear.{/n}
{n}Hepzamirah holds her there a moment, on her toes, the way you hold a rabbit up for a child to see. Then she lets go. The woman folds to her knees in the mud, cradling her hand, and every soul in the yard has stopped to watch.{/n}''',
        c("Continue", "swing_say")),
    hz("swing_say", '''{n}She weighs the paddle in one hand, splintered where the wrist twisted, and does not trouble to look at the woman.{/n}
"You swing at the daughter of Baphomet, you stupid wench? You scrubbed their shirts for three years and thought that made you someone." {n}She lifts her voice, not to the woman but to the yard.{/n} "*Look.* The Commander's beast, off the leash for one breath. Tell the next one."
{n}She turns the paddle over.{/n} "You said *find out*, worm. She found out. Your chaplains will have the petition written by noon and the washerwomen will be sitting in the mud by supper, and I do not care. I keep the paddle. Anyone who raises a stick at me should see how it ends."''',
       c("[Leave her with the paddle.]", flags=(P + "market_strike",), crusade=("Finances", -150)),
       c("[Diplomacy] Get to the laundress before the chaplains do: a bone-setter, a purse, and a word to the yard.",
         check=dict(Skill="CheckDiplomacy", DC=24, Success="mended", Failure="strike", CommanderOnly=True))),
    nar("mended", '''{n}You have the bone-setter at the woman's side before the chaplains have found their pens. It costs you the healer's fee, a month of her pay in advance, and a loud word in front of the whole laundry that the Commander does not let those it freed go unmended. Hepzamirah does not apologise. The petition is written all the same, but it reaches the provost with a line at the foot that the Commander paid the debt the same day. The washerwomen mutter and keep the vats hot.{/n}''',
        c("[Leave her with the paddle.]", flags=(P + "market_mended",), crusade=("Finances", -100))),
    nar("strike", '''{n}You are too slow, or too unwelcome. By the evening bell the chaplains' petition is on the provost's table in three hands, asking whether the Commander of the crusade keeps a beast in the smith's yard to break the bones of those the crusade freed. By dusk the laundry has gone cold: forty women sit down in the east yard with their paddles across their knees, and nobody in the citadel has a clean shirt. The quartermaster brings you the bill, and the chaplains bring you their faces.{/n}''',
        c("[Leave her with the paddle.]", flags=(P + "market_strike",), crusade=("Finances", -150))),
    hz("between", '''{n}For a heartbeat she does not sit. Then she does, on the trough, with the pick across her knees, and looks past your shoulder at the woman with perfect indifference.{/n}
"You see? {mf|He|She} does not let me bite." {n}She says it to the woman, not to you.{/n} "That is what your crusade bought when it broke the mine gates. A keeper for me, and a paddle for you. Go and wring your sheets, wench."
{n}The woman goes. At the gate she spits on the flagstones. Hepzamirah watches the spit, and something in her face tightens that is not quite contempt.{/n}''',
       c("Continue", "between_say")),
    hz("between_say", '''"You put yourself between us," {n}she says, when the gate has shut.{/n} "Now she knows whose beast I am, and so does every washerwoman she talks to by nightfall."
"Was that worth the spit on your stones, clown? I hope so. I enjoyed it."''',
       c("[Leave her to her grinding.]")),
    nar("paid", '''{n}The woman eyes the purse as if it might be a trick. Then she takes it, and weighs it, and puts it in her apron, and looks past you at Hepzamirah.{/n}''',
        c("Continue", "paid_say")),
    woman("paid_say", '''"Three years, for a purse." {n}She does not raise her voice.{/n} "You pay like her, Commander. By the head." {n}She goes.{/n}''',
       c("Continue", "paid_hep")),
    hz("paid_hep", '''{n}Hepzamirah is laughing, quietly, into her hand.{/n}
"By the head. She is right. You bought her silence the way I used to buy it, only you overpaid." {n}She takes up the pick again.{/n} "Never overpay, worm. It tells them what they are worth to you, and then they know how much to ask the next time."''',
       c("[Leave her to her grinding.]")),
], requires=("trickster.ever", RET, PICK), delay=24)


# --- 15. The sister: Horzalah, the canary, and the verdict of the Lord of Beasts. ----------------------------------------

yard(SISTER, "The weaker branch", '"Tell me about Horzalah."', [
    *lead([("canary", nar, '''{n}There is a dead canary on the trough. A real one, from the cage the quartermaster keeps in the stores for the damp. Hepzamirah is looking at it with an expression you cannot read.{/n}''', None),
           ("canary_seen", hz, '''"You were there, in Colyphyr, when she sent me hers. A dead bird in a box with a ribbon, that opened its beak and spoke in her voice: *We meet again, sister*. Then it turned into a flaming spear and flew at my face." {n}She touches the ridge of scar.{/n} "Not this side. The other. I healed that one."''', "horzalah.gift_delivered")],
          "sister"),
    *lead([("sister", hz, '''"Horzalah's name." {n}She says the name as if it were something she had bitten on.{/n} "My sister, by our father. The two of his brood he bothered to set against each other. *Horzalah is stronger in a fight, but Hepzamirah is more cunning and vicious.* That is what he used to say, when he said anything about us at all."''', None),
           ("sister_told", hz, '''"He said it to you too, didn't he, in his prison? *Which is why she prevailed.* He compliments me to crusaders, in a cage, after he has killed me."''', "baphomet.named_horzalah")],
          "sister_state"),
    nar("sister_state", '''{n}She turns the dead canary over with one fingernail.{/n}''',
        c("Continue", "state_dead", requires=("horzalah.dead",)),
        c("Continue", "state_alive", forbids=("horzalah.dead",))),
    hz("state_dead", '''"Dead too, unless somebody has stolen her back." {n}She pokes the bird.{/n} "I wanted to settle it myself. Father will still compare us. Death never stopped his arithmetic."''',
       c("Continue", "ask")),
    hz("state_alive", '''"Somewhere that stupid bitch is still making enough noise for both of us. I wonder whether he answers her now."
{n}She turns the bird with one finger.{/n} "He answered me. Look what that bought."''',
       c("Continue", "ask")),
    hz("ask", '''"You have one of us in your yard." {n}She lifts the dead bird by its foot.{/n} "Which would you have chosen, if you were him? Think before you flatter me."''',
       c('"Neither. That\'s the point. He shouldn\'t have been choosing."', "neither"),
       c('"You. You went under."', "you"),
       c('[Grin] "The canary. It had better timing."', "canary_joke")),
    hz("neither", '''"*Shouldn't have been choosing.*" {n}She repeats it with enormous contempt.{/n} "Spoken like a crusader who was never anyone's child. Everything chooses, clown. The wolf chooses the slow deer. Your Inheritor chooses her paladins. My father chose, and made us fight for it, and the fight was the only thing he ever gave us that was honest."
{n}She drops the canary back on the trough.{/n} "Then you would have had two knives at your throat instead of one. He at least knew what he was breeding."''',
       c("[Leave it there.]")),
    hz("you", '''{n}She is quiet, and the forge ticks as it cools.{/n}
"Yes. I went under. Horzalah used to charge at everything like a siege ram, and when a wall did not fall, she charged it again." {n}Something like pride moves in her voice, and then something like grief.{/n} "And he chose me for it, and then the old piece of shit killed me for losing one fight. So the choosing was worth nothing. You see? You flatter me with the same coin he did."
{n}She drops the canary back on the trough.{/n} "Try flattering me with his words again and I will make you swallow them."''',
       c("[Leave it there.]")),
    hz("canary_joke", '''{n}For a moment she is perfectly still. Then she laughs, suddenly and helplessly, and has to put the canary down.{/n}
"The *canary*. Yes. It had very good timing." {n}She wipes her good eye.{/n} "Say that where she can hear you, whelp. I want to watch her face."''',
       c("[Leave it there.]")),
], requires=("trickster.ever", RET, FIRST), delay=24)


# --- 16. The corner: what she hears at night. ------------------------------------------------------------------------------

yard(CORNER, "The corner", '"The watch says you don\'t sleep."', [
    nar("night", '''{n}It is past the middle of the night. The forge is banked to a red eye and the yard is cold. She is sitting with her back to the wall of her own room, outside it, on the flagstones, in the dark, with the pick across her knees. She does not look up.{/n}''',
        c("Continue", "listen")),
    hz("listen", '''"Listen," {n}she says.{/n}
{n}You listen. The forge ticks as it cools. A dog barks down by the east wall. Somewhere a sentry coughs.{/n}
"In the Labyrinth the jailers came for me. They knew where my corner was. They had grovelled to me, you understand, in Colyphyr, in the temples. They had kissed the floor where I walked. Dead, I was theirs, and they hounded me, and they enjoyed it."
"I do not sleep in rooms any more. Rooms have corners. I sit outside and listen for them."''',
       c('[Sit down beside her in the dark.]', "sit"),
       c('"Nothing\'s coming. The corner\'s Leavable. You left."', "left"),
       c('"I\'ll post a guard on the door."', "guard")),
    nar("sit", '''{n}She does not tell you to go. You sit against the wall beside her, and the stone is cold through your coat, and after a long while her shoulder comes down against yours like a dropped sack, and stays. She does not move it away.{/n}''',
        c("Continue", "sit_say")),
    hz("sit_say", '''"You are warm," {n}she says, in the tone of a complaint.{/n} "Ghosts are not. I had forgotten that too."
"Do not tell anyone about this, clown. Not your chaplains, not your smith." {n}Her shoulder does not move.{/n} "If you repeat it, I will tell them you begged me to sit with you. They will believe the daughter of Baphomet."''',
       c("[Stay until the forge is cold.]", flags=(P + "corner_kept",))),
    hz("left", '''"*Leavable.*" {n}She says it into the dark.{/n} "You say it as if a word could hold a door open forever. Words hold nothing. My father's words held nothing. Mutasafen's words held nothing."
{n}She is quiet for a while.{/n} "Yours held. Which means you can unsay it. A clown who names a corner Leavable can name it a cell again, some night when I have bored him, and the jailers would know the way." {n}The pick turns a quarter on her knees, spike toward your boots.{/n}
"Go to bed, worm. I am staying out here with this. If I hear you start renaming things in your sleep, I will know which door to come through."''',
       c("[Leave her in the dark.]")),
    hz("guard", '''"A guard." {n}She laughs, very softly, so as not to wake the smith.{/n} "One of your soldiers, standing at the door of Baphomet's daughter all night, with a spear, to keep away jailers who are not here."
"He would sooner stand guard in the Worldwound." {n}But she does not refuse it.{/n} "Very well. Post your guard. Tell him if he falls asleep I will eat his boots. I will not need to. He will not fall asleep."''',
       c("[Post the guard.]")),
], requires=("trickster.ever", RET, FIRST), delay=24)


# --- 17. The drill: she trains the crusade's shock troops, her way. -----------------------------------------------------

yard(DRILL, "Her way", '"The sergeants are complaining about you."', [
    nar("field", '''{n}On the parade ground below the citadel, forty of the crusade's heavy infantry are lying in the mud. Some of them are groaning. One of them is laughing, in the high way that men laugh when something has frightened them past fear. Hepzamirah stands in the middle of them with the pick over her shoulder and not a speck of mud on her.{/n}
{n}A sergeant with a bloody nose meets you at the edge of the field. She asked to see how the crusade meets a charge, he says. So they showed her. Then she showed them.{/n}''',
        c("Continue", "hep")),
    hz("hep", '''"Your infantry meet a charge like a village meets a flood," {n}she says, walking over.{/n} "They stand in a line and pray it will go round them, and when it does not, they shit themselves. Deskari's children will not go round. Nor will the things grown from Vorlesh's work in those pits."
"In my father's armies, the front rank knew exactly what a charge feels like, because I made them take one every morning, from me. By the second week they stopped praying and started bracing. By the fourth they were killing things." {n}She flicks mud off the spike.{/n} "Give me your shock troops for a week before the Threshold. Every morning. Half of them will hate me. The other half will live."''',
       c('[Give her the troops] "A week. Every morning. Nobody dies in training."', "given", flags=(P + "drilled_troops",)),
       c('[Give her the troops] "A week. Her way. If some break, better here than at the Threshold."', "harsh",
         flags=(P + "drilled_troops", P + "drilled_harsh"), alignment=("Evil", 1)),
       c('"No. They\'re crusaders, not your father\'s cultists."', "refused")),
    hz("given", '''"Nobody dies." {n}She considers it, as though it were an unfamiliar rule in a familiar game, and shrugs one shoulder.{/n} "Dead men learn nothing. Fine. I will leave you the bodies and take everything else."
"A man who is charged by something with horns every morning for a week does not march the same after. Knees. Shoulders. Fingers that will not close round a spear again. The ones who fold I send to the baggage train, and your sergeants can count what is left." {n}Behind her, the laughing soldier has stopped laughing and is being sick.{/n} "You will have a thinner regiment, whelp, and every man in it will have been charged by Baphomet's daughter and stood. Remember that when they are still standing at the Threshold, and count the cripples as the price."''',
       c("[Leave her to the regiment.]")),
    hz("harsh", '''{n}The scar pulls her mouth into the tight smile.{/n}
"Her way." {n}She says it slowly, relishing it.{/n} "You understand the arithmetic. A soldier who breaks on the parade ground costs you one soldier. A soldier who breaks at the Threshold costs you the line."
"My father's generals understood it. They were monsters. They won." {n}She turns back toward the field and raises her voice to a pitch that goes through the mud like a spike.{/n} "*Up.* The Commander has given you to me."''',
       c("[Leave her to the regiment.]")),
    hz("refused", '''"Not my father's cultists." {n}The good eye narrows.{/n} "No. My father's cultists would have been worth something at the Threshold."
{n}She shrugs, a great roll of her shoulders.{/n} "Keep your crusaders, then, and keep them soft, and pray for them. I will stand in front of them when the charge comes, since they cannot. That was always the plan."''',
       c("[Leave the field.]")),
], requires=("trickster.ever", RET, PICK), delay=24)


# --- 18. His first letter to her: "princess". -------------------------------------------------------------------------------

def mutasafen(id, text, *choices, **kw):
    return n(id, "Mutasafen", text, *choices, **kw)


yard(LETTER2, "Farewell, princess", '"You have a letter."', [
    nar("letter", '''{n}It came in the ordinary post, with the requisitions from Nerosyan, addressed to *Her Highness the Princess, care of the Commander*. She has not opened it. It lies on the trough. She holds its edge down with one nail, as if it might move.{/n}''',
        c("Continue", "open")),
    hz("open", '''"His hand. I would know it on a tombstone. He wrote to me once before, in Colyphyr, to say goodbye. *Farewell, princess.* He was very proud of that letter. He left it on my table where I would find it after he had stolen my army."
"Read it to me, clown. I do not want his words in my own mouth."''',
       c("[Read it aloud.]", "read")),
    *lead([("read", mutasafen, '''"Princess. How is the body? I made it carefully, you know. The scar took me longer than all the rest of you together. I think it is the best work I have ever done, and I have done a great deal of excellent work.
I hear you have been playing at being a crusader's pet. How far you have come. From archpriestess of the Lord of Beasts to a bench in a smithy, eating onions. Do they feed you well? Do they let you out?"''', None),
           ("read_paid", mutasafen, '''"Thank your Commander for the vial. It is everything I hoped. I have learned more about Areelu's work from one vial of that blood than from ten years of rumour. I have grown a hand from it, so far. Only a hand. It keeps trying to pick my pocket."''', VIAL_PAID),
           ("read_forged", mutasafen, '''"Tell your Commander the wine was an indifferent vintage. I noticed on the second test. I am not a man who forgets a joke at his expense."''', VIAL_FORGED),
           ("read_killed", mutasafen, '''"My Apprentice's eyes arrived. You always did wrap a parcel beautifully. I have hired a new Apprentice. He is less talkative."''', COURIER_KILLED)],
          "end_letter"),
    mutasafen("end_letter", '''"Remember what I told you. Anything I make, I can unmake. I am in no hurry. You know how patient I am. You knew it for years, and never noticed.
Your devoted servant, still,
M."''',
              c("Continue", "after")),
    hz("after", '''{n}She is very still.{/n}
"*Still.*" {n}She says it quietly.{/n} "He signs himself my servant still. He grew me in a jar and he writes to me as if I were his mistress, and every word is a knife he has spent a week sharpening."
"He is right about one thing. He is patient. He waited years to take my army." {n}She looks at you.{/n} "Well? You are the one who writes letters. What do we send him?"''',
       c('[Write back] "Dear Mutasafen. She\'s eating well. Onions. Your bodies are next. Regards, the Commander."', "reply",
         flags=(P + "replied",), mythic="Trickster"),
       c('"Nothing. Let him wonder."', "silence"),
       c('[Burn it] "This."', "burn")),
    hz("reply", '''"*Regards, the Commander.*" {n}She takes the pen from you before the ink is dry and adds a line under your signature in a square, violent hand. You read it upside down: "I KNOW WHERE THE CAVE IS."{/n}
"There. Now he will not sleep for a month. He will move the bodies, and moving bodies is slow, and slow things are easy to follow." {n}She folds it.{/n} "You write a very rude letter, whelp. I could grow fond of it."''',
       c("[Send it.]")),
    hz("silence", '''"Let him wonder." {n}She thinks about it.{/n} "Yes. He hates not knowing more than he hates losing. My father taught me that about him. It is the only useful thing my father ever taught me about anyone."
{n}She puts the letter in the pocket of her borrowed coat, unburned.{/n} "I will keep it, though. For when I find him. I will want to read it to him."''',
       c("[Leave her with it.]", flags=(P + "princess_letter_kept",))),
    nar("burn", '''{n}You put it in the forge. It curls and goes, and for a moment the princess on the first line burns bright before the rest. She watches until there is nothing but a flake of grey on the coals.{/n}''',
        c("Continue", "burn_say")),
    hz("burn_say", '''"Good," {n}she says.{/n} "I did not want to be *princess* in my own yard."''',
       c("[Leave her by the forge.]", flags=(P + "princess_letter_burned",))),
], requires=("trickster.ever", RET, CS), delay=24)


# --- 19. Vorlesh: the witch who took her place, and whose experiment the Commander is. -------------------------------------

yard(VORLESH, "Areelu's experiment", '"Tell me about Areelu."', [
    hz("chest", '''"Mutasafen called you *Areelu's work, walking*." {n}She is lying on the trough on her back with the pick propped against it, looking at the sky over the Worldwound.{/n} "In his first reply to you, about the vial. Walking around unexamined. He meant it as a joke. He does not make jokes."
"Whatever burns in you, clown, the thing your chaplains call a miracle, he thinks that bitch Vorlesh had a hand in it. I have watched you in the yard. I think he is right."''',
       c("Continue", "vorlesh")),
    hz("vorlesh", '''"She took my place, you know. At my father's side. While I was bleeding in Colyphyr, he was helping *her*. I called him, and he came, and he killed me for her, because she was precious to him."
{n}She turns her head on the stone and looks at you with the good eye.{/n} "And now I am in bed with her experiment. My father's new favourite made you, and you stole me out of his prison. If there is a god of jokes, worm, he is laughing very hard."''',
       c('"Does it bother you?"', "bother"),
       c('"I\'m not hers. Whatever she made, I\'m the one using it."', "mine"),
       c('[Flirt] "Then let\'s make it a joke she hears about."', "joke")),
    hz("bother", '''"Bother me." {n}She thinks about it honestly, which is rare.{/n} "It bothers me that she will see us at the end, at whatever hole in the world she is hiding in. It bothers me that she will look at you and see her work, and look at me and see the one she replaced, and think she has won twice."
"I want her to look at us and understand that she has lost twice. That her experiment and Baphomet's discarded daughter walked into her house together." {n}She sits up.{/n} "That would be very sweet. Sweeter than killing her. Almost."''',
       c("Continue", "promise")),
    hz("mine", '''"*The one using it.*" {n}She repeats it, and the scarred side of her mouth pulls.{/n} "My father would say that about a sword he took off a corpse. He would say it about me."
"But you mean it about yourself, I think. I can hear it." {n}She sits up.{/n} "Good. Then you are a thief of your own heart, clown, as well as of walls. That is the most thieving thing I have heard since the crate."''',
       c("Continue", "promise")),
    hz("joke", '''{n}She stares at you. Then the tight scarred smile comes, slowly.{/n}
"A joke she hears about." {n}She savours it.{/n} "Yes. Let us walk into her laboratory together, her experiment and her replacement's victim, and let her hear about it from the only two people in the world who find it funny."''',
       c("Continue", "promise")),
    hz("promise", '''"When we find her," {n}she says,{/n} "and your crusade will find her, because you find everything, I want to be the first thing she sees when the door comes down. Before you. Before your paladins. Me."
"Her door. I go through it first. You can have whatever I leave standing."''',
       c('"First through the door. It\'s yours."', "given", flags=(P + "vorlesh_first",)),
       c('"We go through together, or not at all."', "together")),
    hz("given", '''"Mine." {n}She lies back down on the stone and looks at the bruised sky.{/n} "Good. If this is another leash, whelp, I will pull until something breaks."''',
       c("[Leave her looking at the sky.]")),
    hz("together", '''"Together." {n}She considers it, and her lip curls.{/n} "That is a very crusader word. It means somebody does not get what they want."
"Very well. Together. Side by side through her door. I will be half a step in front. You will not notice." {n}She lies back down.{/n} "You will notice."''',
       c("[Leave her looking at the sky.]")),
], requires=("trickster.ever", COMMITTED, CALL), delay=24)


# --- 20. First blood under the banner: a sortie, and the priest she will not have. ----------------------------------------

yard(SORTIE, "The spearhead", '"You went out with the sortie."', [
    nar("back", '''{n}The sortie came back at dusk from the ridge where Deskari's vescavors had been nesting, and she came back at the head of it on foot, with the pick over her shoulder and a spear still in her, low in the side, broken off a hand's breadth from the skin. She walked through the gate like that. The watch saluted her. They had not saluted her before.{/n}
{n}Now she is sitting on the trough with the spear-stump in her, and the regiment's chaplain is standing at the yard gate with his hands already glowing, and she has told him that if he takes one more step she will put the spear in him instead.{/n}''',
        c("Continue", "wound")),
    hz("wound", '''"No priest," {n}she says, before you can speak.{/n} "Terms. No priest mends anything of mine. I said it on the first morning."
{n}She puts her hand round the spear-stump and pulls, and it comes out with a sound you will remember, and she does not make a sound at all. Blood runs down her side into the borrowed coat.{/n} "There. It is out. Now it will close or it will not. I have been dead before. I did not mind it."''',
       c('[Stitch it yourself] "Then I\'ll do it. Not a priest. Me."', "stitch"),
       c('[Order the chaplain] "Heal her, Father. That\'s an order, and it\'s mine to give."', "order"),
       c('"Your terms. Your blood."', "hers")),
    nar("stitch", '''{n}She pulls the coat clear of the wound and holds it there. You clean it with the smith's strong spirit, which makes her swear in the language of the rite, and you close it with the quartermaster's needle and waxed thread, badly, and she watches every stitch with the good eye as if memorising your hands.{/n}
{n}Her skin is fever-hot under your fingers. Once, when the needle goes deep, her hand closes on the back of your neck and stays there until you tie off.{/n}''',
        c("Continue", "stitch_say")),
    hz("stitch_say", '''"Crooked," {n}she says, looking at it.{/n} "You sew like a clown too."
"Leave it. Do not let anyone mend it. I want Mutasafen to see work he did not do, and know whose hands were on me." {n}Her hand is still on your neck.{/n} "I went first, clown. I told you I would. Forty of Deskari's creatures on that ridge, and I went first, and not one of your regiment died behind me."''',
       c("[Leave the stitches crooked.]", flags=(P + "scar_given",))),
    hz("order", '''{n}The chaplain comes forward. She does not put the spear in him. She sits perfectly still while his hands close the wound, and she does not take her eyes off you the whole time, and her face is empty.{/n}
"You promised," {n}she says, when he has gone.{/n} "Then you put a priest's hands on me." {n}She touches the new, clean, unscarred skin, the way she touched the scar in the shield.{/n} "Do not mistake my sitting still for pardon. Remember that I let you."''',
       c("[Leave her with the chaplain's work.]", flags=(P + "cost.healed_against_terms",))),
    hz("hers", '''"Mine." {n}Her lip curls, not quite at you.{/n} "You would let me bleed out on a smith's trough, rather than break a term."
{n}She ties the borrowed coat tight over the wound with her own hands.{/n} "Watching me bleed is easy, worm. Fetch thread next time. Your promise forbade a priest, not your own hands." {n}She sets her jaw.{/n} "It will close. Watch."''',
       c("[Watch.]")),
], requires=("trickster.ever", COMMITTED, MORNING), delay=24)


# --- 21. His last letter: the hold that did not close, and a bargain refused. ---------------------------------------------

yard(UNMADE, "Anything I make", '"Another letter."', [
    nar("letter", '''{n}This one did not come by the post. It was nailed to the yard gate at dawn with a surgeon's scalpel, and the smith's boy would not touch it. The paper is stained yellow in the same places as the first.{/n}''',
        c("[Read it to her.]", "read")),
    mutasafen("read", '''"Princess.
I tried. You felt it; I know you did. I closed my hand on you in that cave, as I built my hand to close, and it did not close. There was nothing there to hold. Somebody has changed the locks.
I do not know how. I have spent every hour since not knowing how. I have not gone so long not knowing anything since I was a child.
So I will offer your landlord a bargain, since you will not hear one. Give me the vessel back. Not her. The vessel. Let me take it apart and learn what was done to it. I will grow her another, better, whole, both eyes, both horns. She will be beautiful again. You have my word, for what it is worth.
M."''',
              c("Continue", "hep")),
    hz("hep", '''{n}She has not moved while you read. Now she laughs, and it is the ugliest sound you have ever heard her make.{/n}
"*Beautiful again.* Both eyes. Both horns." {n}She touches the milk-white eye, and the broken horn, and the ridge of scar.{/n} "He would take this apart on his bench to learn your trick, and grow me pretty, and keep the trick. And the next body he made would have his hand in it again."
"Well, landlord? You are the one he is bargaining with. He has made you an offer. What is your answer?"''',
       c('"No. She\'s not a vessel. She lives here."', "no", flags=(P + "unmade_refused",)),
       c('[Trickster] "Tell him the flat\'s been sublet. To her. Permanently. He\'ll need her signature."', "sublet",
         flags=(P + "unmade_refused",), mythic="Trickster"),
       c('"What do you want to say?"', "ask")),
    hz("no", '''"*She lives here.*" {n}She repeats it in exactly your voice, and then in her own, lower.{/n} "She lives here."
{n}She pulls the scalpel out of the gate and weighs it.{/n} "I will send this back to him. In something of his. It will take a little time to find the right part."''',
       c("[Let her keep the scalpel.]")),
    hz("sublet", '''{n}She stares at you until you think she will refuse, and then she takes the scalpel out of the gate, and cuts her own palm with it, neatly, and signs the bottom of his letter in her own blood with her fingertip: a horned head in a circle, the sign of the Lord of Beasts, crossed through.{/n}
"There. Sublet. Signed." {n}She blows on it.{/n} "He will know that sign. He taught my scribes to draw it. Let him read it upside down and understand that the tenant owns the lease."''',
       c("[Send it back to him.]")),
    hz("ask", '''"Give me the scalpel. I will answer him. He has heard enough from you."
{n}She pulls it out of the gate and writes on the back of his letter with its point, pressing so hard it tears: NO.{/n} "It is short. He will understand it. Everyone always understood it from me except my father."''',
       c("[Send it back to him.]", flags=(P + "unmade_refused",))),
], requires=("trickster.ever", COMMITTED, EYE), delay=24)


# --- 22. The smith: the man who would not hand her a weapon, and the mines she ran. ----------------------------------

def smith(id, text, *choices, **kw):
    return n(id, "Smith", text, *choices, **kw)


yard(FORGE, "The Nexus", '"The smith spoke to you."', [
    nar("forge", '''{n}The smith is working the bellows and she is holding the tongs for him, which you have never seen anyone but his apprentice do. A billet of iron glows white between them. Neither of them looks at you. Neither of them is speaking, in the particular way of two people who have just stopped.{/n}''',
        c("Continue", "smith")),
    smith("smith", '''"She told me I quench too early." {n}He does not look up from the iron.{/n} "Said it the first day, through the wall, and I pretended not to hear. Said it again today. She was right. Twenty years I've quenched a breath too early, and nobody told me, because nobody who knew better ever stood in this yard."
{n}He takes the tongs from her and lays the billet on the anvil.{/n} "I still won't pray for her. But I'll let her hold the tongs."''',
          c("Continue", "hep")),
    hz("hep", '''"In Colyphyr there were forges that ran day and night," {n}she says, watching him strike.{/n} "Under the mountain. My father's mines, and the Nexus, where the portals are. Your crusade stopped the crystal-mining there for a while. I was very angry with you about it at the time."
"I ran those mines. Every forge, every shaft, every slave on every chain. I know what iron sounds like when it is being lied to." {n}She nods at the anvil.{/n} "His iron tells the truth. That is rare, in a crusader's forge. Most of them hammer for the priests of the Inheritor watching and they wanted to look busy."''',
       c('"You ran the Nahyndrian mines."', "crystals"),
       c('"You two are getting on."', "on")),
    hz("crystals", '''"The crystals. Yes." {n}Her voice goes flat and careful, the voice of a quartermaster, not a priestess.{/n} "Nahyndrian crystals, the crystallized blood of dead demon lords. Vorlesh's work showed what could be made with them, and Mutasafen used her work on my army. My father wanted them dug, so I dug them. Mutasafen helped me obtain them. He wrote to me that he had."
"The army you are fighting, clown, somebody dug out of the ground on somebody's orders, and a great deal of it was me." {n}She shrugs.{/n} "I am not sorry. I am only telling you, since you asked, and since you are the one who will have to fight what we dug."''',
       c("[Watch the smith work.]")),
    hz("on", '''"Getting on." {n}She considers the phrase.{/n} "He hates me. I despise him. He is the only man in Drezen who does not pretend otherwise, and so I can stand next to him for an hour without wanting to kill him."
"That is what you crusaders call getting on, I suppose." {n}She takes the tongs back without asking.{/n} "He quenches too early. Tell him."''',
       c("[Leave them to the iron.]")),
], requires=("trickster.ever", RET, PICK), delay=24)


# --- 23. The weapon: Mutasafen's secret, and what it would do to the Commander. ----------------------------------------

yard(WEAPON, "His deadliest weapon", '"You look worried. It doesn\'t suit you."', [
    hz("worried", '''"I am not worried. I am thinking." {n}She rubs the fading maker's mark on her wrist with her thumb.{/n}
"His letter in Colyphyr promised a weapon that would strip the crystals' gifts for a time. Poison, spell, some toy of his — he kept that part to himself. He wanted me to shudder. I laughed. I should have read it twice."''',
       c("Continue", "why")),
    hz("why", '''"I did not shudder. I thought: what a small, clever, useless thing, to take the crystals' gifts away. Who would you use it on?"
{n}She looks at you with the good eye.{/n} "And then you came into my father's prison with a power in you that is not a crusader's, and not a demon's, and Mutasafen called you Areelu's work, walking, and asked for a vial of your blood."
"I think I know who he will use it on, whelp. I think he has wanted your blood for a long time, and not for science."''',
       c('[Trickster] "Then we give him a target he can\'t hit. I\'ve been renaming things since the prison."', "trick"),
       c('"Then we find him before he finishes it."', "hunt"),
       c('"Let him try."', "try")),
    hz("trick", '''"Rename yourself." {n}She almost smiles.{/n} "You would, too. You would stand in front of his weapon and tell it you were somebody else, and it would believe you, because your words hold and his do not."
"I have seen you do it to a wall and a body. I have not seen you do it to yourself." {n}She stops rubbing her wrist.{/n} "Do not try it on yourself unless you must, clown. I would not know how to find you afterwards."''',
       c("Continue", "vow")),
    hz("hunt", '''"Find him." {n}She nods slowly.{/n} "Yes. That is what I have been doing. That is what the cave was. One body fewer, one bench fewer, one more place he has to rebuild in."
"When I go next, I will go for the bench where he keeps the weapon. If he has one." {n}She looks north.{/n} "He always kept his best work closest to his bed. I used to tease him about it. I remember everything I ever teased anyone about."''',
       c("Continue", "vow")),
    hz("try", '''"*Let him try.*" {n}She repeats it with enormous scorn, and then, surprisingly, a little tenderness.{/n} "I expect he treated Areelu's work with the same contempt. Look at him now."
"You are a clown and a thief and the luckiest mortal I have ever seen, and I do not trust luck. I trust knives." {n}She taps the haft of the pick.{/n} "So I will be the knife, and you may be lucky behind me."''',
       c("Continue", "vow")),
    hz("vow", '''"Hear me, worm. This is not a term. It is a vow, and it is mine." {n}She puts one hand flat on your chest, over the place where whatever burns in you burns.{/n}
"If he takes your gifts away, I will be here when they go. If he puts you on his bench, I will take the bench apart around him. He will have to reach through me to take you. I want him to try."''',
       c("[Put your hand over hers.]", flags=(P + "weapon_vow",))),
], requires=("trickster.ever", COMMITTED, EYE), delay=24)


# --- 24. The cult comes back: the rent, and what it cost. ------------------------------------------------------------------

yard(CULT, "The rest of the cellar", '"The watch found something at your door."', [
    *lead([("door", nar, '''{n}At dawn the watch found a horned head in a circle painted on her door in something that was not paint, and under it a single word in the old script of the Lord of Beasts' cult, which the chaplains will not read aloud and the smith's boy has been told not to scrub off.{/n}
{n}She is standing in front of it with her arms folded, reading it for the tenth time, with an expression of great professional interest.{/n}''', None),
           ("door_gate", hz, '''"The cellar did its work. They know it was me. Good. I wanted them to know."''', RENT_TAKEN),
           ("door_refused", hz, '''"I told you I would stop bringing you the heads. I did not tell you I would stop collecting it. There were more of them than three. There are fewer now."''', RENT_REFUSED)],
          "word"),
    hz("word", '''"*Apostate*." {n}She reads it aloud, and the smith's dog goes under the anvil.{/n} "My father's cultists, in your city, calling *me* apostate. The woman who wrote their rites. They learned the word from me."
"They will come tonight. Five or six. The ones who were not in the cellar. They will come for me because I am the betrayal they can reach; they cannot reach my father's and they cannot reach yours." {n}She looks at you.{/n} "I will be waiting. I am telling you, so that you know what the noise was."''',
       c('"I\'ll wait with you."', "wait", flags=(P + "cult_waited",)),
       c('"I\'ll put the watch on the door. Take them alive."', "watch", flags=(P + "cult_taken",), alignment=("Lawful", 1)),
       c('[Trickster] "Leave the door open. Let them in. Then lock it behind them."', "trap", mythic="Trickster",
         flags=(P + "cult_trapped",))),
    nar("wait", '''{n}They come at the hour of the jailers. Six of them, in crusade grey, with the sign cut into their forearms. She lets them get all the way into the yard before she moves, and after that it does not take long. You take the one who goes for the smith's door. She takes the other five. When it is over she is breathing hard and smiling the tight smile, and she wipes the spike of the pick on one of their cloaks.{/n}''',
        c("Continue", "wait_say")),
    hz("wait_say", '''"You took the one going for the smith's door," {n}she says.{/n} "I saw. You left me five. Were you being polite, clown, or did you want to watch what I do with five?"
"Next time take two." {n}She looks down at the five.{/n} "A hound that does all the killing starts to wonder what the master is for."''',
       c("[Help her drag them out.]")),
    hz("watch", '''"Alive." {n}She says it as if you had told her to take them in her teeth.{/n} "Very well. Alive. For your courts, and your chaplains, and your lawyers."
{n}That night the watch takes four of them alive in the yard, and one of them dead, and one of them she takes herself, alive, in a manner of speaking; the chaplains say he will walk again, eventually.{/n} "I kept to your word," {n}she says in the morning, washing her hands in the trough.{/n} "Mostly. You got five alive. Do not complain about the sixth."''',
       c("[Leave it there.]")),
    nar("trap", '''{n}She stares at you, and then the scarred smile comes, slowly. That night the door stands wide, and the yard is dark, and six cultists of the Lord of Beasts walk into the yard of Baphomet's daughter one by one, and the smith, on your word, drops the bar across the yard gate behind the last of them.{/n}
{n}In the morning the watch carries six of them out, alive, tied, gagged, and dressed in chaplains' surplices, which she insisted on, and delivers them to the citadel's cells with a note in your hand: RETURNED TO SENDER.{/n}''',
        c("Continue", "trap_say")),
    hz("trap_say", '''"*Returned to sender.*" {n}She has the note; she took it back from the watch to keep.{/n} "You made them walk into their own prison, whelp, and gave them the key, and then took it away. That is my father's trick and yours at once."
{n}She folds the note small.{/n} "Keep a copy. I want his priests to find it when they come for the next six."''',
       c("[Leave her with the note.]")),
], requires=("trickster.ever", RET, RENT), delay=48)


# --- 25. The second night: after the sortie, the crooked scar. ------------------------------------------------------------

yard(SECOND_NIGHT, "Crooked", '"How\'s the scar?"', [
    nar("dark", '''{n}She is waiting at her door with the lamp already out, which she has never done. The broken door hangs open behind her into the dark of the room. There is no corner in there that she has not already filled with something: the pick, your torn cloak, whatever else she has decided is hers.{/n}''',
        c("Continue", "scar_ask", requires=(P + "scar_given",)),
        c("Continue", "healed_ask", requires=(P + "cost.healed_against_terms",)),
        c("Continue", "plain", forbids=(P + "scar_given", P + "cost.healed_against_terms"))),
    hz("scar_ask", '''"Crooked." {n}She takes your hand and lays it beside the closed seam low on her side. Your fingers rest clear of the stitches; she keeps them there.{/n} "Your work. Leave it crooked. Tonight I want you closer."''',
       c("Continue", "pull")),
    hz("healed_ask", '''"Clean," {n}she says, and her mouth twists.{/n} "Your chaplain's work. Not a mark. As if the spear had never been." {n}She takes your hand and puts it on the place, low on her side, under the borrowed coat. The skin is smooth and fever-hot.{/n} "I hate it. So you will have to give me something else there, clown. I will not have a body that forgets."''',
       c("Continue", "pull")),
    hz("plain", '''"No lamp tonight." {n}She says it the way she says terms.{/n} "I have spent all day being looked at by your regiment. Tonight I do not want to be looked at by anyone who can see the pretty side."''',
       c("Continue", "pull")),
    nar("pull", '''{n}She takes you by the wrist, the way she always does, and pulls you over the threshold, into the warm dark that smells of iron and forge-smoke and her, and kicks the broken door shut behind you with her heel, and it bangs in its frame and swings open again, because it cannot be locked, and she laughs against your throat.{/n}
{n}Her hands are rough and very sure. She finds every buckle you are wearing and does not bother with most of them. The stump of her horn catches in your hair and she does not stop for it. When her mouth finds yours it is hungry, and not gentle, and she bears you down onto the mended cot, which creaks like a ship, and holds you there with one broad hand flat on your chest, and looks down at you in the dark with the eye that can see.{/n}''',
        c("Continue", "down")),
    hz("down", '''"Enough prayers tonight," {n}she says, drawing your face toward hers.{/n} "Come here."
{n}She tears the borrowed coat open and lets it fall, drags your shirt loose, and pulls you against her, bare and fever-hot from shoulder to knee, and bends her head to your mouth.{/n}''',
        c("[Pull her down to you.]", flags=(P + "second_night",))),
], requires=("trickster.ever", COMMITTED, SORTIE), delay=12)


# --- 26. Ember asks if she is happy. ------------------------------------------------------------------------------------------

yard(EMBER_ASKS, "Happy", '"Ember wanted me to ask you something."', [
    nar("ember", '''{n}Ember is sitting on the upturned bucket again, and Hepzamirah is sitting on the trough, and there is a jar of blue flowers between them that nobody has thrown. They have plainly been sitting like this for some time. Ember looks up at you with great seriousness.{/n}''',
        c("Continue", "ember_say")),
    em("ember_say", '''"I asked her if she was happy now. She said happy is a word for elves and dogs. So I asked her if she was less sad now, and she didn't answer." {n}Ember turns to Hepzamirah.{/n} "I think you should tell {mf|him|her}. You tell {mf|him|her} everything else. You shout when you talk to each other."''',
       c("Continue", "hep")),
    hz("hep", '''"The smith's boy is going to lose his ears." {n}Hepzamirah does not look at either of you.{/n}
"Less sad." {n}She tests it.{/n} "In the Labyrinth I was hiding in a corner from men who used to kiss my feet, with half my head gone, listening to an angel scream. Now I sit in a smithy and a small elf brings me flowers I throw over the wall, and a clown comes in the evening and tells me jokes, and I break the furniture."
"Yes. Less sad. Is that what you wanted, elf? Is that enough?"''',
       c("Continue", "ember_end")),
    em("ember_end", '''"It's a start," {n}Ember says, very pleased, and picks the jar of blue flowers up, and gives it to her, and runs off before it can be thrown.{/n}''',
       c("Continue", "after")),
    hz("after", '''{n}Hepzamirah sits holding the jar. She does not throw it.{/n}
"Do not say anything, worm," {n}she says.{/n} "If you open your mouth I will throw it at you, and then she will cry, and then I will have to kill something to feel better, and I have run out of cultists."''',
       c("[Say nothing.]")),
], requires=("trickster.ever", COMMITTED, FLOWERS, "ember.present"), delay=24)


# --- 27. The name: what she calls the Commander, and what she will be called. -----------------------------------------

yard(NAMES, "Names", '"You never use my name."', [
    hz("names", '''"Your name." {n}She considers it.{/n} "No. I do not. I call you clown. You have done nothing to lose the title."
"Names are not small things, where I come from. My father owned his brood the way a breeder owns stock, and he used our names like leashes. I wore mine as if it were a crown."''',
       c("Continue", "her")),
    hz("her", '''{n}She is quiet for a while.{/n}
"You rename things. Walls. Bodies. You have never once tried to rename me." {n}She looks at you with the good eye.{/n} "Why not? You could. I think it would hold. I think if you called me something else, loud enough, the Lord of Beasts himself would forget which of his brood I was."''',
       c('"Because it\'s yours. The one thing he gave you that you get to keep."', "keep"),
       c('[Trickster] "All right. From now on you\'re Hepzamirah, the one who left."', "renamed", mythic="Trickster",
         flags=(P + "renamed_herself",)),
       c('"You rename yourself. I\'ll use whatever you pick."', "choose")),
    hz("keep", '''"Hepzamirah." {n}She says it the way she would set down a weapon on a table.{/n} "They know it in Colyphyr. They will learn it here." {n}She stands, and takes up the pick.{/n} "You will say it when I want to hear it, clown. Not before."''',
       c("Continue", "clown")),
    hz("renamed", '''{n}She goes very still. Somewhere across the city a dog barks and stops.{/n}
"*The one who left.*" {n}She says it slowly, in your tongue, and then in the other, and the other makes the smith's forge flare, once, as if a door had opened somewhere and a draught come through.{/n}
"Oh," {n}she says, very quietly.{/n} "Oh, that held. I felt it hold." {n}She puts a hand to her chest as though checking for a wound.{/n} "You fool. You terrible, reckless fool. You should have asked."''',
       c("Continue", "clown")),
    hz("choose", '''"Pick." {n}She laughs, short.{/n} "You want me to name myself? I already made this name feared, whelp. I will not throw that work away for a prettier one."
"Perhaps in a hundred years. You will have to wait." {n}She stands, and takes up the pick.{/n} "Until then I am Hepzamirah, and you are the clown."''',
       c("Continue", "clown")),
    hz("clown", '''"And I will go on calling you clown," {n}she says.{/n} "In front of your court and your chaplains and your paladins, and at the Threshold, and in bed. It is a title now. My father's priests had titles, and I took them off them with their horns."
"Yours I will leave on you, so that everyone who hears it knows who gave it."''',
       c("[Let her keep calling you that.]")),
], requires=("trickster.ever", COMMITTED, MORNING), delay=24)


# --- 28. The letter she will never send. ------------------------------------------------------------------------------------

yard(UNSENT, "To the Lord of Beasts", '"You\'re writing something."', [
    nar("desk", '''{n}She has taken the smith's account-board off its nail and laid it across her knees for a desk, and she is writing on the back of a requisition from Nerosyan in a square, violent hand that goes through the paper in places. There are four crossed-out drafts on the flagstones. She does not cover the page when you come.{/n}''',
        c("Continue", "read")),
    hz("read", '''"To my father." {n}She does not look up.{/n} "I will never send it. I will not send it for his priests to laugh at."
"I am writing it anyway. Everything I would have said, in Colyphyr, if I had not been on my knees asking him to save me." {n}She holds it out to you, without looking.{/n} "Read it. If you laugh before the end, I will know which line to sharpen."''',
       c("[Read it.]", "letter"),
       c('"It\'s yours. I don\'t need to read it."', "private")),
    hz("letter", '''"Father.
I was the best of your brood. I gave you my mother, and my brothers and sisters by the hundred, and your mines, and your armies, and your rites, and a war on Golarion that you came to see only once, to kill me in it.
When I called you, you came. That was your bargain. And you came to kill me, for her.
I have a body now that a traitor grew and a clown stole. I will have a door with no lock. I have a pick. I have one eye that sees you exactly as you are.
One day I will call you again. You will have to come. And this time I will not be kneeling.
Your daughter, who you do not miss,
Hepzamirah."''',
       c("Continue", "verdict")),
    hz("verdict", '''{n}She watches you finish it with the good eye.{/n}
"Well? You write letters to demon lords. You wrote to Mutasafen. Is it good?"''',
       c('"It\'s good. Send it anyway. Burn it on an altar of his. It\'ll get there."', "altar"),
       c('"Cut the last line. He doesn\'t get to hear you begging to be missed."', "cut"),
       c('"Keep it. For the day you call him. Read it to his face."', "keep")),
    hz("altar", '''"Burn it on an altar." {n}She stares at you.{/n} "You would have me pray to him. With *this*."
{n}Then she laughs, and it is not the ugly laugh; it is almost delighted.{/n} "Oh, yes. A prayer that is a curse. His priests would find it in the ashes and not dare read it to him, and not dare not. I would have given my other eye for a prayer like that in Colyphyr." {n}She folds it.{/n} "There is an old shrine under the east wall. Your watch has stripped it, but the stone still knows his name. I will use it."''',
       c("[Leave her to it.]", flags=(P + "letter_burned",))),
    hz("cut", '''{n}She reads the last line twice, and her thumb stops on it.{/n}
"*Who you do not miss.*" {n}She draws the pen through it, once, hard enough to tear.{/n} "Yes. Let him wonder. He taught me to keep an enemy hungry."
"There. Now it ends at my name. Just my name. Let him wonder what I meant by it."''',
       c("[Leave her to it.]")),
    hz("keep", '''"Read it to his face." {n}She folds the letter into quarters, and then into eighths, very small, and puts it in the pocket over her heart.{/n}
"Yes. That is better than sending it. He will stand there because he must, because I called, and I will read him his own daughter's letter, and he will have to listen to the end." {n}She pats the pocket.{/n} "You are cruel, clown. You hide it in jokes, but I have seen it now. It is a good cruelty. I approve."''',
       c("[Leave her to it.]", flags=(P + "letter_kept",))),
    hz("private", '''"Yours," {n}she says, and stops writing.{/n} "You would leave a thing of mine unread, when I have held it out to you. My father read everything of mine. He had my priests open my letters before I did."
{n}Her good eye narrows. She snatches the page back off the board, folds it twice with her thumbnail, and pushes it inside her coat.{/n} "What are you saving it for? A man who will not read a thing has already guessed what is in it, or wants me to owe him for not reading it. I know that trick. I used it on my priests." {n}She takes up the pick.{/n} "You will get nothing for it. Not a word. Go away."''',
       c("[Leave her to it.]")),
], requires=("trickster.ever", RET, MIRROR), delay=24)


# --- 29. Her room: what she keeps, and why. ---------------------------------------------------------------------------------

ROOM_LEADS = [
    ("room_paddle", nar, '''{n}The laundress's paddle hangs over the bed, where a crusader would hang a holy symbol: the haft split and bound with wire where a wrist twisted in it. Under it, pinned with a nail, is the chaplains' petition, and a laundry-yard tally of the shifts that stood idle.{/n} "Her wrist knit crooked," {n}she says, following your eyes.{/n} "The petition I use to light the lamp. Every woman in your laundry has seen what happens to a stick raised at me. That was worth your purse."''', P + "market_struck"),
    ("room_note", nar, '''{n}Pinned to the wall with a cultist's knife is a note in your own hand: RETURNED TO SENDER.{/n}''', P + "cult_trapped"),
    ("room_jar", nar, '''{n}The jar of blue flowers stands on the sill. They have been changed. You did not see who changed them.{/n}''', FLOWERS_KEPT),
    ("room_lens", nar, '''{n}The crystal-cutter's lens hangs on its cord from the bedpost.{/n}''', EYE_BURNED),
    ("room_letter", nar, '''{n}Mutasafen's first letter to her in Drezen is tucked into the frame of the broken door, unburned, for the day she finds him.{/n}''', P + "princess_letter_kept"),
    ("room_splinters", nar, '''{n}On a shelf, in a row, are the splinters you sawed off her horn, laid out in order of size, like trophies.{/n}''', HORN_CUT),
]
yard(ROOM, "What she keeps", '"Can I come in?"', [
    *lead([("room", nar, '''{n}She lets you in, which is not the same as inviting you. The door cannot be shut. The room behind it is small and hot and smells of forge-smoke and her, and everything in it is something she took, or was given, or refused to give back.{/n}''', None),
           *ROOM_LEADS], "keeps"),
    hz("keeps", '''"You are looking at my things." {n}She sits on the mended cot, which complains.{/n} "Less room than Colyphyr. Fewer fools to touch my things, and the next one who does loses the hand."
{n}She looks round it.{/n} "I know who brought each one. So will anyone who steals one."''',
       c('"What\'s it like?"', "like"),
       c('[Sit beside her on the cot.]', "sit")),
    hz("like", '''"Like having a body." {n}She says it at once, as if she had the answer ready.{/n} "Everything itches and everything is mine. I keep what I want."
"If your priests object, send them here." {n}She shrugs.{/n} "I have room for another trophy."''',
       c("[Leave her with her things.]")),
    nar("sit", '''{n}The cot complains again. She does not move over. Her shoulder is against yours, heavy and hot, and after a while she takes your hand, not your wrist this time, and turns it over, and studies it in the lamplight the way she studied the things on her shelf.{/n}''',
        c("Continue", "sit_say")),
    hz("sit_say", '''"This too," {n}she says.{/n} "I keep this. I have decided."
"Do not argue. You have seen what I do to people who take my things."''',
       c("[Don't argue.]")),
], requires=("trickster.ever", COMMITTED, MORNING), delay=24)


# --- 30. The gift: what she gives, once, without being asked. ---------------------------------------------------------------

yard(GIFT, "A debt, in advance", '"You wanted to see me?"', [
    nar("box", '''{n}She hands you a box without a word. It is a crusade ammunition box with the stencil scraped off, and it has been tied with a length of red bell-rope in an elaborate knot, and she watches you untie it with the expression of a woman watching a trap to see whether it will spring.{/n}''',
        c("Continue", "inside_horn", requires=(HORN_CUT,)),
        c("Continue", "inside_plain", forbids=(HORN_CUT,))),
    nar("inside_horn", '''{n}Inside, on a bed of forge-ash, is a small thing of polished horn on a thong: the largest of the splinters you sawed from her, filed and shaped into a knife no longer than a finger, with a hole drilled through the pommel. The edge is very sharp. It has plainly taken her hours.{/n}''',
        c("Continue", "speech")),
    nar("inside_plain", '''{n}Inside, on a bed of forge-ash, is a holy symbol of the Lord of Beasts: a horned head of black iron, worn smooth with handling, on a chain that has been cut. Someone has taken a chisel to it. The horns are gone. What is left is only a head.{/n}''',
        c("Continue", "speech")),
    hz("speech", '''"In my temples a gift given downward meant a debt, and I owed nobody but him. Then he threw me away."
"I owe you." {n}She says it very fast, as if it were a thing that would burn her mouth if she held it there.{/n} "A debt. Paid in advance. For the rest of whatever this is. There. It is said. Do not make me say it again; I will not."''',
       c('[Put it on at once.]', "on", flags=(P + "gift_worn",)),
       c('"You don\'t owe me anything. That\'s the point."', "owe"),
       c('[Kiss her.]', "kiss", flags=(P + "gift_worn",))),
    hz("on", '''{n}She watches you tie it round your neck. Her hand comes up, and adjusts it, and stays there a moment against your collarbone.{/n}
"There. Wear it where your court can see." {n}The scarred smile.{/n} "I want the next fool who calls you mine to have proof."''',
       c("[Leave it on.]")),
    hz("owe", '''"*That is the point.*" {n}She repeats it with a great deal of scorn.{/n} "Crusaders. You would give everything and ask nothing and call it love, and then wonder why nobody knows what you are worth."
"I owe you. I have decided. You will take it, and you will wear it, and you will stop arguing with a gift from the daughter of Baphomet." {n}She ties it round your neck herself, too tight, and then loosens it.{/n}''',
       c("[Wear it.]", flags=(P + "gift_worn",))),
    nar("kiss", '''{n}She catches your collar and keeps you in the kiss until your hand tightens on her shoulder. Only then does she let you breathe. Then she takes the gift out of your hands and ties it round your neck herself, against your collarbone, too tight, and loosens it, and steps back.{/n}''',
        c("Continue", "kiss_say")),
    hz("kiss_say", '''"That is not how you thank someone for a debt," {n}she says.{/n} "But I will allow it. This once. Do not tell the smith."''',
       c("[Wear it.]")),
], requires=("trickster.ever", COMMITTED, MORNING), delay=48)


# --- 31. The war council: the daughter of Baphomet at the crusade's map table. -----------------------------------------

def general(id, text, *choices, **kw):
    return n(id, "Crusade general", text, *choices, **kw)


yard(COUNCIL, "At the map table", '"The generals want you gone from the council."', [
    nar("council", '''{n}She came to the war council this morning uninvited, walked past the guards and the paladins and the Mendevian lords, and put her hand flat on the map of the Worldwound between the crusade's markers for the Threshold. The council did not continue. It has been adjourned to the smith's yard, where she has laid the map across the trough and weighted it with the pick.{/n}
{n}Three generals have followed you here. They stand well back.{/n}''',
        c("Continue", "general")),
    general("general", '''"Commander. With the greatest respect. This creature was her father's archpriestess. She commanded demon armies against this crusade for years. Whatever she tells us about the Worldwound, she could be telling us so that we march into a trap." {n}He does not look at her.{/n} "We cannot plan the Threshold around her word."''',
            c("Continue", "hep")),
    hz("hep", '''"He is right," {n}she says, before you can.{/n} "I could be. I would, if I still served my father. I have led armies into traps shaped exactly like this one." {n}She taps the map, at the approach to the Threshold.{/n}
"So listen to what I tell you, and then test it, as you would test anything a traitor told you. That is what I would do. Deskari's children come in swarms, not ranks, and they come from above; your pikes are pointed the wrong way. The creatures grown from Vorlesh's work come from below, from the pits, at night. Your scouts watch the horizon. Nobody watches the ground."
"I am not asking to be trusted. I am telling your generals where to look. If they look and find nothing, hang me."''',
       c('[Back her] "You heard her. Test every word. Then use it."', "backed", flags=(P + "council_heard",)),
       c('[Use her] "Take her intelligence, general. She marches in the first rank, where you can watch her."', "used",
         flags=(P + "council_heard",)),
       c('"The generals plan the Threshold. You fight it."', "refused")),
    general("backed", '''{n}The general looks at her, and at you, and at the map, where her finger has drawn a line along the broken ground under the approach, which the crusade's charts mark as nothing at all.{/n} "Test it," {n}he says at last.{/n} "Very well. If anything comes out of that ground, I will eat my plume."''',
            c("Continue", "backed_say")),
    hz("backed_say", '''"He will eat his plume," {n}she says, when they have gone, with deep satisfaction.{/n} "Things will come out of that ground. I know how that witch likes to build. I learned it the hard way."
"*Test me*, he says. As if I were a bridge." {n}She rolls the map under her arm.{/n} "Good. Men who obey are useless. My father's court was full of them, and I fed most of them to him. Men who test can be taught. When the ground opens, I want that general standing beside me, so that I can watch him eat the plume."''',
       c("[Leave her with the map.]")),
    hz("used", '''"*Where you can watch her.*" {n}She smiles the tight smile at the general.{/n} "Good. That is where I would have put me."
"The first rank. Sensible." {n}She rolls up the map.{/n} "Now give me men who can keep up."''',
       c("[Leave her with the map.]")),
    hz("refused", '''{n}She says nothing at all. She rolls the map up very slowly, and hands it to the nearest general, who takes it as if it might bite.{/n}
"Fight it, then. I will. I will stand in the first rank, where my pikes are pointed the right way, and when your generals find the ravine the hard way, I will be there to pull them out of it." {n}She shoulders the pick.{/n} "I will not say I told you. I will only think it very loudly."''',
       c("[Let her go.]")),
], requires=("trickster.ever", COMMITTED, MORNING), delay=24)


# --- 32. The song: what the soldiers sing about her, and what she makes of it. ---------------------------------------------

yard(SONG, "The Bull's Daughter", '"You heard the song, then."', [
    nar("song", '''{n}It came up out of the barracks by the east wall a few nights ago, to the tune of a Mendevian drinking song, and now the whole garrison has it. The Bull's Daughter. Four verses, each ruder than the last, about the horns and the eye and the Commander's broken cot. The chaplains have forbidden it. The chaplains' own acolytes sing it in the scullery.{/n}
{n}Tonight a dozen soldiers were singing it on the wall above the smith's yard, and the last verse stopped very suddenly when she came out of her door with the pick.{/n}''',
        c("Continue", "hep")),
    hz("hep", '''"Come up," {n}she says to the wall, not loudly.{/n} "All of you. Bring the song."
{n}For a moment nobody moves. Then the sergeant looks at you, standing in the yard behind her, sees you do not forbid it, and comes down the stair first, because he wrote the second verse and will not have the boys go down without him. They stand in a row in the yard, twelve of them, with their helmets under their arms, and the youngest is shaking.{/n}
"Sing it," {n}she says.{/n} "From the beginning. To my face. I want to hear the words properly. On the wall you slur them."''',
       c('[Let it happen.]', "sung"),
       c('"They\'ll sing it for me too. Every verse. I\'m in it."', "both", flags=(P + "song_shared",)),
       c('[Order them off] "Dismissed. All of you. Now."', "dismissed")),
    nar("sung", '''{n}They sing it. Badly, at first, and then, because she does not stop them and does not move, better. She listens to every verse with her head on one side, the milk-white eye toward them. At the verse about the horns she nods. At the verse about the cot she laughs aloud, once, and the youngest soldier drops his helmet.{/n}''',
        c("Continue", "sung_say")),
    hz("sung_say", '''"The third verse does not scan," {n}she says when they have finished.{/n} "And you have the eye on the wrong side. Fix it. If you are going to sing about me, you will sing about me *correctly*."
{n}She looks along the row of them.{/n} "In my father's temples the faithful sang about how beautiful I was. It was not true either, and it was much worse music. Go. Sing it on the wall. Loudly."
{n}In the morning there is a complaint on your desk from their captain: twelve men late to the watch, one asking for a transfer to the Nerosyan road, and a sergeant who has been heard singing the corrected third verse at mess. The captain would like to know under whose authority the Commander's guest musters his soldiers. It is a fair question.{/n}''',
       c("[Watch them go.]")),
    nar("both", '''{n}So they sing it to both of you, and it is much worse to stand through than you expected, and the fourth verse, the one about the cot, is not one you will ever forget. She stands beside you through all of it with her arms folded, and when it reaches the cot her shoulder shakes against yours, and she does not look at you, because if she did she would not be able to keep her face.{/n}''',
        c("Continue", "both_say")),
    hz("both_say", '''"You stood and listened to your own soldiers sing about your bed," {n}she says, when they have fled.{/n} "With me. In front of them. Without flinching."
"My father's priests would have cut their tongues out. You made it a joke they are in, instead of a joke about us." {n}She shakes her head slowly.{/n} "Twelve men who will not sing it on the wall again without looking over their shoulders for you. That is a start."
{n}Their captain sees it differently: by morning there is a complaint on your desk about the Commander keeping twelve men from the watch to sing about their own bed. But the song changes on the wall that week. The cot verse goes, and a new last verse comes in, about a clown and a bull's daughter who stood and heard it out together, and fewer of the garrison make the sign when she passes.{/n}''',
       c("[Watch them go.]")),
    hz("dismissed", '''{n}They go, fast. She watches them to the gate, and then turns the good eye on you, and it is cold.{/n}
"You protected me from a *song*." {n}She says it with deep contempt.{/n} "As if I were a lady in a tower, and they had written verses under my window. My father's jailers hounded me after I was dead, worm. I can survive a drinking song."
"Next time let them sing. I will decide what hurts me."''',
       c("[Leave it there.]")),
], requires=("trickster.ever", RET, PICK, MORNING), delay=24)   # Q8 (Sol INT): the cot verse needs the cot


# --- 33. Nerosyan writes: the price of letting the city know. ----------------------------------------------------------

def clerk(id, text, *choices, **kw):
    return n(id, "Court clerk", text, *choices, **kw)


yard(NEROSYAN, "A letter from court", '"Nerosyan has written about us."', [
    nar("letter", '''{n}The letter is from Nerosyan, sealed three times, carried by a court clerk who will not come further into the yard than the gate and holds it out at arm's length, as if Hepzamirah might eat it, or him. She takes it from him before you can and breaks all three seals with her thumbnail.{/n}''',
        c("Continue", "clerk")),
    clerk("clerk", '''"The court, ah, expresses its concern, Commander." {n}He has plainly rehearsed this on the road.{/n} "That the Commander of the crusade has taken into, ah, intimate association, a creature of the Lord of Beasts. On the eve of the Threshold. With the whole garrison talking about it. The court asks that the association be ended, or at the least made discreet, for the crusade's sake. Otherwise certain lords will find their levies delayed."''',
          c("Continue", "hep")),
    hz("hep", '''{n}She has read the letter while he talked. She folds it very neatly.{/n}
"*Made discreet.*" {n}She says it to the clerk, pleasantly.{/n} "Your court would like the Commander to keep me in a cupboard, and take me out at night, and put me back before the chaplains are up. My father's court would have understood that perfectly."
"So. Clown. The lords will delay their levies. That is real. That is spears you will not have at the Threshold." {n}She looks at you, and she is not smiling.{/n} "What do you tell your court?"''',
       c('"Tell the court the Commander keeps no cupboards. The levies can come or not."', "public", crusade=("Favors", -150),
         flags=(P + "court_defied",)),
       c('"Tell the court it will be discreet. Until the Threshold."', "discreet", flags=(P + "cost.discreet",)),
       c('[Trickster] "Tell the court my embassy order stands. Record your objection beside it."', "embassy_reply",
         requires=(EMBASSY,), mythic="Trickster")),
    hz("public", '''{n}The clerk writes it down with a shaking hand, and goes. She watches him to the gate.{/n}
"You will pay for that," {n}she says.{/n} "Spears, and favours, and lords who will smile at you at the victory feast and remember. I know that arithmetic too. I ran my father's court."
{n}She puts the folded letter in the pocket over her heart.{/n} "I sold people for less than that. I will keep this, clown, so that I know exactly what you paid, and the day you begin to think it too much, I will read it back to you."''',
       c("[Leave it there.]")),
    hz("discreet", '''{n}The clerk bows with relief and goes. She does not watch him. She is looking at the broken door.{/n}
"Until the Threshold," {n}she says.{/n} "Very well. I will be discreet. I will not break any furniture that can be heard from the east wall." {n}Her mouth twists.{/n}
"But understand what you bought with it, whelp. You hide me for their levies. Remember what you sold, when they ask for more."''',
       c("[Leave it there.]")),
    hz("embassy_reply", '''{n}The clerk writes down the claim. The message will reach Nerosyan as your order, without a claim of agreement from the court. The levies will still be delayed. He leaves with the letter under his arm.{/n}
"A matter of state." {n}She bares her teeth at his back.{/n} "You made them write down whose bed I use. Now they can argue over it in council. Your treasury buys the missing spears; your name keeps my door open. Do not pretend the sign does it."''',
       c("[Leave it there.]", crusade=("Finances", -300), flags=(P + "court_defied",))),
], requires=("trickster.ever", COMMITTED, KNOWN), delay=48)


# --- 34. The treaty: the Embassy of the Leavable Prison negotiates with the crusade. -------------------------------------

yard(TREATY, "Articles of the Embassy", '"You wanted to see the Commander. Officially."', [
    nar("treaty", '''{n}She has written it out on a sheet of the quartermaster's best vellum, which she did not ask for, in her square violent hand, under a heading she has drawn with great care: TREATY BETWEEN THE EMBASSY OF THE LEAVABLE PRISON AND THE CRUSADE OF MENDEV. It has seven articles. She holds it out to you across the trough as if it were a challenge to a duel.{/n}''',
        c("[Read it.]", "articles")),
    hz("articles", '''"*Article the first: the Embassy has no lock.* That one is not negotiable. *Article the second: the Ambassador goes first into every fight.* Also not negotiable. *Article the third: the Commander of the crusade may enter the Embassy at any hour, without knocking, and is expected to.*" {n}She watches your face.{/n}
"*Article the fourth: no priest.* *The fifth: Mutasafen is the Ambassador's.* *The sixth: the Lord of Beasts is the Ambassador's.* The seventh I have left blank."
{n}She holds the pen out, point first.{/n} "Fill it, clown. Carefully. Whatever you write, I will hold you to it until one of us is dead, and then I will hold your ghost to it."''',
       c('"Article the seventh: the Ambassador comes back from every fight."', "back", flags=(P + "treaty_signed",)),
       c('"Article the seventh: the Commander goes first into the Embassy\'s bed."', "bed", flags=(P + "treaty_signed",)),
       c('"Article the seventh: either party may leave. Neither party will."', "leave", flags=(P + "treaty_signed",))),
    hz("back", '''"*Comes back.*" {n}She writes it in, slowly.{/n} "That is your prayer again. You keep trying to put your prayer into my treaties."
"Very well. It is written. It binds nobody in Nerosyan, and I know it; your order holds at the yard gate, and nowhere beyond your reach. It binds you and me. Break it, worm, and I will not sue. I will walk out through the door you made Leavable, and take the pick, and every name I know in your crusade's cellars, to whoever pays best." {n}She signs it with the point of the pick's spike, dipped in the forge-ash.{/n}''',
       c("[Sign it.]")),
    hz("bed", '''{n}She laughs aloud, and the smith's hammer stops.{/n}
"Goes *first*. You would put that in a treaty, in writing, on vellum, where your court could read it." {n}She writes it in, grinning, with an elaborate flourish.{/n} "It is a very badly drafted article. It does not say first *before whom*. We will have to test it."
{n}She signs it with the point of the pick's spike, dipped in the forge-ash.{/n}''',
       c("[Sign it.]")),
    hz("leave", '''{n}She stops with the pen above the vellum.{/n} "Neither leaves? Bold ink, clown."
{n}She writes it in, hard, and signs it with the point of the pick's spike, dipped in the forge-ash, and hands you the pick.{/n} "Sign it where I can see your hand."''',
       c("[Sign it.]")),
], requires=("trickster.ever", COMMITTED, EMBASSY), delay=24)


# Round 2 authored continuations: provenance and the results of promises
# already made in this route. Optional scenes create no new romance gates.
def _r2_scene(sid):
    return next(s for s in SCENES if s["Id"] == sid)


def _r2_node(sid, nid):
    return next(v for v in _r2_scene(sid)["Nodes"] if v["Id"] == nid)


for _armed_scene in (BLOODLINE, FLOWERS, CORNER):
    _r2_scene(_armed_scene)["Requires"].append(PICK)
for _ember_scene in (FLOWERS, EMBER_ASKS):
    _r2_scene(_ember_scene)["Requires"].append("ember.present_now")
    _r2_scene(_ember_scene)["Forbids"].append("ember.native_devastated")

# Separate SeenCues: pity and the apple exchange are not interchangeable.
_r2_node(FLOWERS, "ember")["Choices"][0]["Next"] = "pity_history"
_r2_scene(FLOWERS)["Nodes"].extend([
    nar("pity_history", '{n}Hepzamirah stops the whetstone as Ember speaks.{/n}',
        c("Continue", "pity_recalled", requires=(P + "heard_ember_pity",)),
        c("Continue", "hep", forbids=(P + "heard_ember_pity",))),
    hz("pity_recalled", '"In his prison you called me a poor thing. You have a body to lose, elf. I had none, and still they hurt me."',
       c("Continue", "hep")),
    hz("apple_recalled", '"Compassion is not an apple, you said. Give it to one and you do not rob another." {n}She sets the whetstone beside the jar.{/n} "Everything I had, I took. I am keeping these. Do not tell me what it means."',
       c("Continue", "keep")),
])
_r2_node(FLOWERS, "alone")["Choices"][0]["Next"] = "apple_history"
_r2_scene(FLOWERS)["Nodes"].append(nar("apple_history", '{n}Ember hums. Hepzamirah looks from the jar to her empty hands.{/n}',
    c("Continue", "apple_recalled", requires=(P + "heard_ember_apple",)),
    c("Continue", "keep", forbids=(P + "heard_ember_apple",))))

# Altar-road rent collects surviving accomplices from the known raid.
_r2_node(RENT, "sack")["Choices"][0]["Next"] = "rent_history"
_r2_scene(RENT)["Nodes"].extend([
    nar("rent_history", '{n}She nudges the wet sack with her boot.{/n}',
        c("Continue", "rent_after_altar", requires=(core.ALTAR,)),
        c("Continue", "sack_say", forbids=(core.ALTAR,))),
    hz("rent_after_altar", '"The men your watch missed. The cellar under the grain exchange had friends outside it. I followed one home. He recognized me and knelt. That made the next part easier." {n}She loosens the bell-rope.{/n} "Rent. One priest in the sack, two accomplices tied in the stripped cellar. The altar was already yours; these were still his."',
       c("Continue", "choose")),
])

# Saved hunt outcome nodes now finish the departure, not the expedition.
_r2_node(HUNT, "shadow")["Text"] = '{n}You saddle a horse after she leaves. On the north road you keep the city\'s dust between you and her pack. The pick never lowers from her shoulder.{/n}'
_r2_node(HUNT, "caught")["Text"] = '{n}You follow her through the north gate. Her head turns at the sound of your horse; then she rides on. You have already broken the term.{/n}'
_r2_node(HUNT, "shadow")["Choices"][0]["Set"].append(P + "hunt.shadowed")
_r2_node(HUNT, "caught")["Choices"][0]["Set"].append(P + "hunt.caught")
_r2_node(HUNT, "caught")["Choices"][0]["Text"] = "[Keep your distance.]"

def _hunt_report(suffix, hours, flag, text):
    # The native tavern list remains usable while her forge hub is absent.
    SCENES.append(scene(P + suffix, "The north road", "Hepzamirah", 5,
        '"Any word from the north road?"', [nar("report", text, c("[Return to the city.]"))],
        requires=("trickster.ever", RET, HUNT, flag), forbids=(CLOSED, EYE), delay=hours,
        last=5, optional=True, Relationship="hepzamirah", Chapters=[5],
        AnswerLists=["6dccfd39947ef4242a8afbe36b21a46c"], ReturnToList=True,
        ReturnText="{n}The watch has no further word from the north road.{/n}", Areas=[core.DREZEN]))

_hunt_report("bond.hunt_shadow", 72, P + "hunt.shadowed",
    '{n}You return ahead of her. On the second night you watched her go down from the black ridge with her lantern. The vrocks screamed; she stayed in the cave long after they stopped. You left before she climbed back out. Her room is still empty. She has not returned.{/n}')
_hunt_report("bond.hunt_caught", 24, P + "hunt.caught",
    '{n}You return to Drezen alone. Last night she stepped beside your fire with the pick across her shoulders. "One day, whelp. You could not keep one term for one day. Go home. Come down this road again and I bring you back across my shoulders." She waited until you turned your horse. The forge room remains empty.{/n}')

# Explicit slot: later encounter; stitched/healed/plain setup remains intact.
_r2_node(SECOND_NIGHT, "down")["Choices"][0]["Next"] = SECOND_NIGHT + ".explicit.1"
_r2_scene(SECOND_NIGHT)["Nodes"].append(nar(SECOND_NIGHT + ".explicit.1",
    '{n}She catches your mouth again and draws you close. Behind you the broken door swings open, and she lets it. Her nails go down your back, her breath is a growl against your jaw, and the cot complains like a ship in a gale; she has no prayers left for it, and no patience, and no interest in being quiet.{/n}',
    c("Continue")))

# One physical result per military promise, with the original decision clock.
yard(P + "flesh.drill_result", "Seven mornings", '"The week is up."', [
    nar("field", '{n}The sergeant lays seven marked tallies on the trough. Across the yard the surviving line braces at Hepzamirah\'s raised haft without waiting for a prayer.{/n}',
        c("Continue", "harsh", requires=(P + "drilled_harsh",)),
        c("Continue", "supervised", forbids=(P + "drilled_harsh",))),
    hz("supervised", '"Nobody died. Your sergeant counted after every charge, and I let him count." {n}She plants the pick against the trough and slides a tally across the boards with one finger.{/n} "Forty went in. Thirty-one will march. Nine of them will carry a stick for the rest of their lives: shattered knees, a hand that will not close, one who will never hear on the left. I broke them the way you break a young horse, and the ones left standing are the best soft little bastards you own. The nine you can pension." {n}The scarred side of her mouth pulls tight.{/n} "Do not tell the rest they have won a battle. I have not given them one yet."',
       c("[Return the regiment to its sergeants.]")),
    hz("harsh", '{n}The sergeant\'s casualty list separates those still drilling from those sent to the infirmary: smashed fingers, a broken knee, two soldiers unfit to march. She reads it without lowering her eyes.{/n} "These held. Those broke, and good riddance; they would have broken at the Threshold with a demon\'s teeth in them. You told me my way, whelp. Here is what it cost you, and what it bought."',
       c("[Take the casualty list.]")),
], requires=("trickster.ever", RET, "hepzamirah.present_now", DRILL, P + "drilled_troops"), delay=168)

yard(P + "bond.scouts_result", "Under the approach", '"The scouts tested your warning."', [
    nar("report", '{n}The scouts have brought a rubbing from a split stone under the approach: claw marks underneath, fresh earth pushed up through the crack. Beside it are revised watches and orders to lower the second rank\'s pikes when the ground moves. The general has removed the plume from his helmet.{/n}',
        c("Continue", "plume")),
    hz("plume", '"No appetite, general?" {n}She plucks a feather and lays it on his report. He signs the watch order and takes the feather with him.{/n} "He looked. He found it. Now he can send men who watch their feet. I want them alive behind me; dead soldiers are poor shields."',
       c("[Send the orders to the captains.]")),
], requires=("trickster.ever", RET, "hepzamirah.present_now", COUNCIL, P + "council_heard"), delay=24)

PATH_FIT = {s["Id"]: "T" for s in SCENES}


import copy

# struct2-05 / HEP-03: an attack is not its repair outcome. Retain every
# original answer and target, and append the repaired and legacy alternatives.
_room_scene = next(s for s in SCENES if s["Id"] == ROOM)
for _room_node in list(_room_scene["Nodes"]):
    for _room_answer in list(_room_node["Choices"]):
        if _room_answer.get("Next") == "room_paddle":
            _mended_answer = copy.deepcopy(_room_answer)
            _mended_answer["Next"] = "room_paddle_mended"
            _mended_answer["Requires"].append(P + "market_mended")
            _legacy_answer = copy.deepcopy(_room_answer)
            _legacy_answer["Next"] = "room_paddle_unresolved"
            _legacy_answer["Forbids"].extend((P + "market_strike", P + "market_mended"))
            _room_answer["Requires"].append(P + "market_strike")
            _room_answer["Forbids"].append(P + "market_mended")
            _room_node["Choices"].extend((_mended_answer, _legacy_answer))
_room_paddle = next(n for n in _room_scene["Nodes"] if n["Id"] == "room_paddle")
PADDLE_TEXT = {
    "room_paddle_mended": '''{n}The laundress's paddle hangs over the bed, where a crusader would hang a holy symbol: the haft split and bound with wire where a wrist twisted in it. Under it, pinned with a nail, is the chaplains' petition, and at its foot a clerk's line that the Commander paid the debt the same day.{/n} "The bone-setter set it straight," {n}she says, following your eyes.{/n} "I looked. It cost you a month of her pay and a loud word in front of the whole yard, and the vats never went cold. The petition I use to light the lamp. Every woman in your laundry saw what happens to a stick raised at me, and then saw you pay to put her back together. I keep the stick. That was worth your purse, whelp. I am not thanking you for the rest."''',
    "room_paddle_unresolved": '''{n}The laundress's paddle hangs over the bed, where a crusader would hang a holy symbol: the haft split and bound with wire where a wrist twisted in it. Under it, pinned with a nail, is a petition in the chaplains' hand.{/n} "She raised it at me," {n}she says, following your eyes.{/n} "What came of her afterwards is laundry business and the chaplains' trouble. The petition I use to light the lamp. Every woman in your laundry has seen what happens to a stick raised at me, and I keep the stick where they can see it from the door. That was worth your purse."''',
}
for _paddle_id in PADDLE_TEXT:
    _paddle_node = copy.deepcopy(_room_paddle)
    _paddle_node["Id"] = _paddle_id
    _paddle_node["Text"] = PADDLE_TEXT[_paddle_id]
    _room_scene["Nodes"].append(_paddle_node)
