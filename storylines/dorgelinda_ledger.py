"""Dorgelinda Stranglehold: the weekly counts that turn an audit into a courtship.

Every scene is at her own desk or in her own stores in Drezen, after the Trickster audit has opened (dorgelinda_trickster).
Each engages a canon anchor of hers:
- the withered hand and the nickname (Logistics_Officer/Cue_0013 4145e730, Cue_0014 73a6ebd0, Cue_0017 d469d483);
- her contempt for the court's banquets (Cue_0020 59935ba7) and her helmets "stuck somewhere in Ustalav" (Cue_0011 a514f727);
- her fences and old debtors (Logistics_2/Cue_0050 75dd6c9b, Logistics_6/Cue_0025 7ccd16a9);
- Bartley's warehouse and the command staff's potions (Logistics_5/Cue_0062 d50321da, Cue_0063 e05050d7, Cue_0074 753c00e6);
- her awe at the Commander's return from the Abyss (Logistics_6/Cue_0001 e247ef32);
- the ration cuts she proposed to lie about (Logistics_7/Cue_0030 a2d71b94, Cue_0050 87957683);
- her offer to be court-martialled after the war (Logistics_8-1/Cue_0095 c25b7d5e).
Her past before the supply service is her own telling in her own voice, and she says as much; nothing here states it as fact.
"""
from story_format import c
from storylines.dorgelinda_trickster import (ABYSS, BOOTS_PAID, CARTS, CLEAN, COMMITTED, COUNTED, DIRTY, HANGED_LANN,
                                             HANGED_WENDUAG, HUSHED, LATE, METHODS, P, PRESENT, PRISON, REDEEMED, RETURNED,
                                             TRIBUNAL, d, nar, office)

SCENES = []
L = "dorgelinda.ledger."
HAND_OFFERED = "dorgelinda.hand_offered"          # Logistics_Officer/Answer_0008: "We have spells available that could restore your hand."
BACK_FROM_ABYSS = "dorgelinda.back_from_abyss"    # Logistics_6/Cue_0001: "You really did come back from the Abyss itself!"
RATIONS_CUT = "dorgelinda.rations_cut"            # Logistics_7/Cue_0001: "we can't feed our whole army"
RATIONS_LIE = "dorgelinda.rations_lie"            # Logistics_7/Cue_0050: her plan chosen, the ranks told it will improve
RATIONS_EQUAL = "dorgelinda.rations_equal"        # Logistics_7/Cue_0051: the Commander refused the cut
COURT_MARTIAL = "dorgelinda.court_martial_offered"  # Logistics_8-1/Cue_0095: "You can court-martial me after the war"

SELECTED_ANSWERS = {HAND_OFFERED: "16083b4c429389c45aece47df3d2d590"}
SEEN_CUES = {
    BACK_FROM_ABYSS: ["e247ef321268e0f4da5f20edb24985f5"],
    RATIONS_CUT: ["38132221ce5c4504ca6a0567c18b0f8f"],
    RATIONS_LIE: ["87957683a0ae2ed4983aa17ae0965d86"],
    RATIONS_EQUAL: ["e87c9eebfc7d1e74aacaf8a5678398b6"],
    COURT_MARTIAL: ["c25b7d5ecaab416479e23e41d8f11e94"],
    "dorgelinda.free_rein": ["a9d4895276ebb3449a00c31ad9191b40"],
    "dorgelinda.plunder_refused": ["809f75ce119a3a84eac7c107e02b124c"],
    "dorgelinda.cathedral": ["059df5b17bf8dd74fa293a2ec6fe5fb4"],
    "dorgelinda.merry_city": ["8a5d9a9b77b581b4f82ac7a06602fc7e"],
    "dorgelinda.king_revel": ["6a98741751820244981e3de2edd5e41b"],
}

HAND = L + "the_hand"
GRIP = L + "stranglehold"
WAREHOUSE = L + "the_warehouse"
DEBTS = L + "old_debts"
RECEIPTS = L + "receipts"
RATIONS = L + "half_rations"
NIGHT = L + "after_hours"
MORNING = L + "morning_count"
INQUIRY = L + "the_inquiry"
FORWARD = L + "carried_forward"

VROCK = L + "the_vrocks_driver"
BARTLEY = L + "the_corporals_account"
COUNCIL = L + "after_the_council"
GATE = L + "the_west_gate"
WEIGHT = L + "weight_discrepancy"
REVELS = L + "the_kings_bill"
FAITH = L + "buying_forgiveness"
AFTER = L + "after_the_war"
FREE_REIN = "dorgelinda.free_rein"                # Logistics_6/Cue_0050: free rein given to her connections
PLUNDER_REFUSED = "dorgelinda.plunder_refused"    # Logistics_6/Cue_0051: "your conscience can't fill an empty belly"
CATHEDRAL = "dorgelinda.cathedral"                # Logistics_8-1/Cue_0075: "maybe buyin' it will"
MERRY_CITY = "dorgelinda.merry_city"              # c5 Coronation/Cue_0009 (Trickster, no Fool King crowned)
KING_REVEL = "dorgelinda.king_revel"              # c5 Coronation/Cue_0018 (Trickster, King Thaberdine crowned)

HAND_TOLD = L + "hand_told"
PEN_LIFTED = L + "pen_lifted"
GRIP_HELD = L + "grip_held"
POTIONS_OURS = L + "potions_ours"
POTIONS_BARTLEY = L + "potions_bartley"
FORGED = L + "forged_release"
HONEST_DEMAND = L + "honest_demand"
FENCE_CALLED = L + "fence_called"
WELCOMED = L + "welcomed"
SHARED = L + "shared_ration"
ORDERED = L + "ordered_to_eat"
NIGHT_KEPT = L + "night_kept"
TRUE_BOOKS = L + "true_books_sent"
CLEAN_COPY = L + "clean_copy_sent"
HER_NAME = L + "her_name_sent"
RECEIPT = L + "receipt_signed"


# --- 1. The bad hand. -------------------------------------------------------------------------------------------------

office(HAND, "The bad hand", '"You\'re writin\' with one hand again."', [
    nar("door", '''{n}Dorgelinda is copying a requisition for lamp oil, cold-weather cloaks and forty pairs of boots, none of which Nerosyan will send. She writes with her good hand. The other lies on the page to hold it flat, the fingers curled and grey, and the page does not move.{/n}''',
        c("Continue", "asked_before", requires=(HAND_OFFERED,)),
        c("Continue", "never_asked", forbids=(HAND_OFFERED,))),
    d("asked_before", '''"You asked me once if I wanted it mended. I told you to spend the spell on some poor sap whose legs got ripped off in the first battle."
{n}She blots the requisition and does not look up.{/n}
"I meant it. There's a sergeant in the infirmary walkin' on two legs today 'cause of what I said. You'd like to know the rest of it. Everybody does. Most of 'em don't pay for it in boots."''',
      c('"How did it happen?"', "story"),
      c('"I didn\'t come to ask."', "liar")),
    d("never_asked", '''"You keep lookin' at it. Everyone does, the first dozen times. Clerks, colonels, a Hellknight or two who think nobody sees 'em count my fingers."
{n}She blots the requisition and does not look up.{/n}
"Go on, then. You're payin' in boots this week. I'll give you a story for 'em."''',
      c('"How did it happen?"', "story"),
      c('"I didn\'t come to ask."', "liar")),
    d("liar", '''"Liar." {n}She says it without heat, the way she says "damp" of a warehouse.{/n}
"You came to be counted, and you're sittin' there countin' me. I'd do the same. A quartermaster who doesn't count the other side of the table ends up guardin' an empty warehouse with a full book."''',
      c("Continue", "story")),
    d("story", '''"There's three versions, dependin' on who's buyin'. For a colonel, I held a breach alone at Kenabres against a horde. For a recruit, it was a demon the size of a barn." {n}She finally looks up.{/n}
"For you, the true one. Somethin' with claws came over a barricade I was holdin', in the dark, and I put a spear in it, and it put its hand across my face and the other across my arm on the way down. The report says demon. The report was written by a man who wasn't there. I didn't see much of it. It took the eye first."''',
      c('"And the hand?"', "hand")),
    d("hand", '''"The hand it left. That's the joke. It took the eye and it left the hand, only it left the hand the way a cutpurse leaves a purse: on you, with nothin' in it." {n}She lifts the grey fingers with her good hand, turns them to the lamp, and lets them fall back on the page. They land like something dropped.{/n}
"Went numb on the march back and stayed numb. The healers poked it for a month. Our resident jokesters took one look and started callin' me Stranglehold. So I left the front for the supply service, and I showed every one of those wisecrackers that one hand's all you need to keep your supplies in order."''',
      c('"And did they learn?"', "learned"),
      c('[Reach across the desk and take the bad hand in yours.]', "touch")),
    d("learned", '''"All of 'em. The thievin' quartermasters, the officers who lose half a caravan every skirmish, the civilian milksops with a sob story for every sack." {n}Something that is almost pride comes into her voice.{/n}
"Two of those jokesters are dead now, on the walls, and I buried 'em in good boots. The third's a sergeant in my stores. He calls me ma'am and counts twice." {n}She sniffs.{/n} "That's what a nickname's for. To see who's still sayin' it in a year."''',
      c("Continue", "ask_back")),
    d("touch", '''{n}She does not pull away. Nor does she help. The hand is cool and very light, the skin tight over the bones, like holding a glove somebody else has taken off.{/n}
"It won't feel a thing, Commander. That's the point of tellin' you." {n}Her good hand keeps the page flat on its own. She watches your thumb move over the knuckles and her jaw works, once.{/n}
"...It's been a while since anybody picked it up on purpose. Most folk hand it back to me like it's somethin' I dropped."''',
      c("[Keep holding it a moment longer.]", "ask_back", flags=(L + "held_hand",)),
      c("[Set it back on the page, gently.]", "ask_back")),
    d("ask_back", '''"Right. Your turn." {n}She dips the pen.{/n} "I've told you where my eye went and where my hand went. You've drawn a warehouse, two pairs of boots and a blanket you can't account for. What's the Trickster had off you? And don't say nothin'. Nobody walks out of a war without somethin' missin' from the column."''',
      c("[Show her a scar you don't talk about.]", "scar"),
      c('"The Trickster took something. I\'m still counting what."', "counting"),
      c('[Flirt] "Nothing you can see. You\'ll have to look harder."', "flirt")),
    d("scar", '''{n}She looks at it for a long time, the way she looks at a dented helmet, working out what hit it and how hard and whether whoever wore it walked away.{/n}
"That's a bad one. Somebody meant it." {n}She writes a line in your column, small. You can read it upside down: One scar, declared.{/n}
"There. Now you're on the books properly. Everythin' else you drew was stores. That's the first thing you've given me that isn't."''',
      c('"Is that how you court, Quartermaster? By inventory?"', "close", flags=(HAND_TOLD,))),
    d("counting", '''"Still countin'." {n}She repeats it as if checking the weight.{/n}
"That's an honest answer, and I hate it, 'cause I can't write it down. Tell you what. You count, I'll hold the column open, and when you've got a figure you bring it here." {n}She writes a line in your column: One loss, amount not yet known.{/n}
"There. Now you're on the books properly. That's the first thing you've given me that isn't stores."''',
      c('"Is that how you court, Quartermaster? By inventory?"', "close", flags=(HAND_TOLD,))),
    d("flirt", '''{n}She looks at you with the one eye, from the top of your head to the edge of the desk, as thoroughly as she would a new consignment of cavalry saddles.{/n}
"Harder than that?" {n}A pause.{/n} "Hammer and tongs, Commander. You've got the nerve of a Fellow with a full cart." {n}She writes a line in your column, very small, and turns the book so you cannot read it.{/n}
"There. Now you're on the books properly. Don't ask what I wrote."''',
      c('"Is that how you court, Quartermaster? By inventory?"', "close", flags=(HAND_TOLD,))),
    d("close", '''"Court?" {n}She snorts, and caps the ink, and for a moment the corner of her mouth goes somewhere it does not usually go.{/n}
"I'm auditin' you. If you've mistook the two, that's your affair. Same time next week. Bring the boots back if you've still got 'em. There's a lad on the south wall with his toes out."''',
      c("[Leave her to the requisition.]")),
], requires=("trickster.ever", COUNTED), forbids=(HAND,), delay=24)


# --- 2. The grip. -----------------------------------------------------------------------------------------------------

GRIP_CHOICES = (
    c('[Try to slide the pen out from under her hand.]',
      check=dict(Skill="SkillThievery", DC=24, Success="lifted", Failure="caught", CommanderOnly=True)),
    c('[Pull it straight out. Strength against strength.]',
      check=dict(Skill="SkillAthletics", DC=28, Success="pulled", Failure="held", CommanderOnly=True)),
    c('"I\'ll pass. I\'ve seen what you do to wagons."', "pass"),
)

office(GRIP, "Stranglehold", '"Busy?"', [
    nar("start", '''{n}A crowd has gathered around her desk: two clerks, a supply sergeant with a bandaged ear and a very young soldier from the Mendevian levies with his sleeve rolled up. On the desk between Dorgelinda and the soldier lies a single steel pen. Her good hand is flat on top of it.{/n}
{n}The soldier is pulling at the end of the pen with both hands. Dorgelinda is reading a manifest.{/n}''',
        c("[Wait for it to finish.]", "finish")),
    d("finish", '''{n}The soldier gives up, red to the ears. The sergeant collects two coppers from each clerk with the air of a man who has done this before.{/n}
"New draft," Dorgelinda says, without looking up from the manifest. "Asked the lads in the stores why they call me Stranglehold. Thought it was a joke about my temper." {n}She turns a page.{/n} "It's partly a joke about my temper."''',
      c('"Is that a standing wager?"', "wager")),
    d("wager", '''"Every new draft since Kenabres. Pay a copper, take the pen out from under my hand, win a silver. I've not paid a silver yet." {n}Now she looks up. The clerks have gone very quiet.{/n}
"Trickster's rules for you, Commander, since you're a Trickster. Any way you like. You can pull it, pinch it, sing it out. If it comes out, I'll put your silver against your boots. If it doesn't..." {n}She taps the pen with one finger.{/n} "You buy the stores a round."''',
      *GRIP_CHOICES),
    d("lifted", '''{n}You do not pull. You lean in to read the manifest upside down, and ask her about a line on it, a shipment of salted fish logged twice. She frowns and looks, and her hand shifts a hair's breadth to point, and the pen is in your sleeve before her finger lands.{/n}
{n}The sergeant makes a noise like a kettle.{/n}
"...Well." {n}She lifts her hand and looks at the bare wood under it for a long moment.{/n} "Used, quietly. Of course it was." {n}She takes a silver from her own purse and slaps it down.{/n} "The fish is logged twice, by the way. You weren't lyin' about that part. That's what makes it work."''',
      c("[Pocket the silver.]", "after", flags=(PEN_LIFTED,))),
    d("caught", '''{n}You lean in to read the manifest upside down, and ask her about a line on it, and her hand shifts to point, and your fingers are on the pen, and her hand comes down again on your fingers like a portcullis.{/n}
"Salted fish, logged twice. Good eye. Bad hands." {n}She does not let go.{/n} "I've had thieves in my stores since before you were weaned, Commander. They all ask about the fish."''',
      c("Continue", "held")),
    d("pulled", '''{n}You set your feet and pull, and for a moment nothing happens, and then the pen comes out from under her hand like a nail from old oak. The whole desk shifts a finger's breadth across the floor.{/n}
{n}Nobody breathes. Dorgelinda looks at her empty hand, then at your arm, with something like professional interest.{/n}
"Huh." {n}She takes a silver from her purse and puts it on the desk.{/n} "First in two years. You'll want to put a poultice on that shoulder tonight. Don't say I never gave you anythin'."''',
      c("[Pocket the silver.]", "after", flags=(PEN_LIFTED,))),
    d("held", '''{n}The pen does not move. Her hand does not move. After a while it is not the pen she is holding, but your hand on it, and her grip is exactly as its name promised.{/n}
"That's Stranglehold, Commander." {n}The clerks are grinning. The sergeant is already calling the round.{/n}
{n}She does not let go at once. Her thumb, the good one, moves once across the back of your knuckles, as if checking a seam.{/n} "Didn't say I'd let go when you lost. Only said you'd lose."''',
      c("[Leave your hand where it is.]", "after", flags=(GRIP_HELD,)),
      c("[Take it back, and buy the round.]", "after")),
    d("pass", '''"Hah." {n}She seems genuinely pleased.{/n} "Smartest thing anyone's said at this desk all week. Saves you a copper and me a sore wrist."
{n}She waves the clerks off. They go, disappointed, taking the young soldier with them. When the door closes she leans back.{/n}
"Don't tell 'em I've never lost. I lost twice. Once to a paladin who prayed at it, and once to a halfling who tickled me." {n}She points the pen at you.{/n} "Neither of 'em got a second go."''',
      c("Continue", "after")),
    d("after", '''{n}The office empties. She pours two cups from the bottle that is on no manifest and sets one by your hand.{/n}
"Our resident jokesters named me for a hand that couldn't hold a thing. So I made the other one hold everythin'. That's all a nickname is, Commander. Somebody else's joke that you finish." {n}She drinks.{/n} "You'd know. They call you a Trickster. I'd like to see what you finish."''',
      c('"Maybe you."', "maybe"),
      c('"The war. Then we\'ll see."', "war")),
    d("maybe", '''{n}She chokes on the drink. She does it quietly, and with dignity, and wipes her mouth with the back of her bad hand.{/n}
"You'll want to watch that, Commander. I've got a long memory and a longer book." {n}She does not say no. She writes something in your column and does not show you.{/n}''',
      c("[Finish your cup.]")),
    d("war", '''"The war." {n}She nods, satisfied, as if you have given the correct figure.{/n}
"Good answer. The war, then. And after the war, if there's an after, you can come and try the pen again. I'll have healed." {n}She lifts her cup an inch.{/n} "Torag willin'."''',
      c("[Finish your cup.]")),
], requires=("trickster.ever", HAND), forbids=(GRIP,), delay=24)


# --- 3. The warehouse by the walls (the tribunal path). --------------------------------------------------------------

POTION_CHOICES = (
    c('"Put them on my line. Used, quietly. Twelve men are breathing."', "ours"),
    c('"Enter them as theft. Bartley\'s theft. That\'s what it was."', "bartley"),
)

office(WAREHOUSE, "The warehouse by the walls", '"You said the stores by the walls still needed countin\'."', [
    nar("start", '''{n}She takes you after dark, with a lantern and a clerk's tally board, past the last sentries to a stone storehouse in the lee of the western wall. The Wound glows on the clouds beyond the battlements, a bruise that never heals. The door has three new locks. She has all the keys on a thong around her wrist.{/n}
{n}Inside it smells of oil, sacking and old cheese. Bartley's warehouse. Everything the Fellows stole, and everything they did not have time to sell.{/n}''',
        c("Continue", "hanged", requires=(HANGED_LANN,)),
        c("Continue", "hanged", requires=(HANGED_WENDUAG,), forbids=(HANGED_LANN,)),
        c("Continue", "prison", requires=(PRISON,), forbids=(HANGED_LANN, HANGED_WENDUAG)),
        c("Continue", "hushed", requires=(HUSHED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON)),
        c("Continue", "redeemed", requires=(REDEEMED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED)),
        c("Continue", "count", forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED, REDEEMED))),
    d("hanged", '''"The men who stacked this are in the ground." {n}She sets the lantern on a barrel.{/n} "I checked the knots myself. Somebody had to, and I wasn't goin' to let a hangman who'd never met 'em do it sloppy. They fought on the walls, the lot of them. They never ran."
{n}She hangs the tally board on a nail.{/n} "The stores don't care. Let's count."''',
      c("Continue", "count")),
    d("prison", '''"The men who stacked this are halfway to Nerosyan in chains, cursin' my name the whole way, I expect. Good. Better than cursin' nothin' from a tree."
{n}She hangs the tally board on a nail.{/n} "They'll serve their time. The stores won't wait for 'em. Let's count."''',
      c("Continue", "count")),
    d("hushed", '''"The men who stacked this are at some fort at the end of the world, tellin' the garrison how they escaped on a pack of trained bulettes." {n}She sniffs.{/n} "Woljif's story. I've heard four versions. The bulettes get bigger each time."
{n}She hangs the tally board on a nail.{/n} "Let's count."''',
      c("Continue", "count")),
    d("redeemed", '''"The men who stacked this are diggin' my new latrines and liftin' crates for free till the Crusade says they've atoned. Bartley asked to help count tonight." {n}She hangs the tally board on a nail.{/n} "I told him no. There's forgiveness, and there's handin' a thief the tally board."''',
      c("Continue", "count")),
    nar("count", '''{n}You count. She reads the crates and you chalk them: salt beef, lamp oil, horseshoes, a barrel of cheap Mendevian brandy, bolts of wool, three cases of crossbow quarrels with the Crusade's own brand burned into the lids. She does not hurry. Twice she makes you count a stack again because the chalk marks lean.{/n}
{n}Near midnight, behind the brandy, she pulls a tarpaulin off a small iron-bound crate stencilled with the seal of the general staff. Inside, packed in straw, are two dozen potion vials. Every one is empty.{/n}''',
        c("[Hold the lantern closer.]", "crate")),
    d("crate", '''"The command staff's healin' potions." {n}She lifts one empty vial and turns it in the light.{/n} "The ones Bartley's lads beat my quartermaster half to death for. The ones that went to the plague ward."
{n}Scratched on the inside of the lid with a knife point are twelve short lines and a word: Breathing.{/n}
"He counted 'em. The corporal." {n}Her voice is very flat.{/n} "Twelve men with green slime for tears who'd have rotted in their cots. And the order was that my quartermaster should die sooner than open this box. Because an officer's worth ten of 'em. That's the arithmetic, Commander. I've done it myself. I'll do it again before this war's over."''',
      c('"Is it the right arithmetic?"', "arith"),
      c('"What does the book want?"', "book")),
    d("arith", '''"Right?" {n}She sets the vial back in the straw, neatly, in its row.{/n}
"Right's for priests and paladins. I do supply. If an officer dies 'cause the potions went to twelve privates, we lose a battle, and a hundred privates die, and I write that down too." {n}She is quiet a moment.{/n} "And if the twelve privates die, the whole company learns what it's worth to us, and they stop fightin' for us, and we lose the battle anyway. There's no right. There's only which column it goes in."''',
      c("Continue", "book")),
    d("book", '''"The book wants twenty-four vials entered somewhere. Either they're stolen, and they go under Bartley's name for the record in Nerosyan, or they're issued, and they go under yours."
{n}She holds out the pen.{/n} "You ate a warehouse. You tell me if you ate these."''',
      *POTION_CHOICES),
    d("ours", '''{n}She watches you write it: twenty-four vials, healing, issued to the Commander, for operations. Used, quietly. Then, under it, because you are who you are, a small tally of twelve lines.{/n}
"You'll have the general staff askin' where their potions went." {n}She takes the pen back.{/n} "And I'll tell 'em. The Commander drank 'em. All twenty-four. Very thirsty, the Commander." {n}Her mouth twitches.{/n} "They'll believe it of you. That's the terrible thing."''',
      c("Continue", "home", flags=(POTIONS_OURS,))),
    d("bartley", '''{n}She nods, once, and writes it herself, in her own hand: twenty-four vials, healing, stolen, C. N. Bartley. The pen does not waver.{/n}
"That's the law. That's how it'll read in Nerosyan, and they'll say we've got a grip on our troublemakers." {n}She blots the line.{/n}
"And somewhere a corporal who saved twelve men is goin' to have one more line against him in a book nobody'll ever read." {n}She closes the ledger.{/n} "You did right by the book, Commander. I'll not pretend it tastes good."''',
      c("Continue", "home", flags=(POTIONS_BARTLEY,))),
    nar("home", '''{n}You lock up together. She takes the lantern. On the walk back along the wall a sentry salutes the Commander and then, a beat later, the quartermaster, and she returns it with the bad hand as she always does.{/n}
{n}At the stores door she stops.{/n}''',
        c("Continue", "door")),
    d("door", '''"Most commanders never set foot in a warehouse. They sign what I put in front of 'em and complain the boots don't fit." {n}She fishes for her keys.{/n}
"You counted till midnight and you didn't complain once, except about the cheese. I'll put that in the book too." {n}She gets the door open.{/n} "Goodnight, Commander. Don't dream about brandy."''',
      c("[Say goodnight.]")),
], requires=("trickster.ever", COUNTED, TRIBUNAL), forbids=(WAREHOUSE,), delay=24)


# --- 4. Old debts: the helmets stuck in Ustalav. --------------------------------------------------------------------

office(DEBTS, "Old debts", '"You\'re writin\' letters. To whom?"', [
    d("start", '''"Debtors." {n}She has a stack of them, folded small, each addressed in her square hand to a different town: Nerosyan, Kenabres, Vigil, and one to somewhere in Ustalav.{/n}
"Remember the helmets? The consignment we paid for in spring that's been sittin' in a customs yard in Ustalav since before the Wound got its second wind? It's still sittin' there. Three hundred helmets, Commander. Three hundred heads."
{n}She taps the Ustalavic letter.{/n} "Customs wants a release from the Mendevian treasury. The treasury clerk who signs releases sits in Nerosyan, answerin' letters in the order they came, which puts ours somewhere in the next century. So I'm writin' to a man who owes me money."''',
      c('"Who is he?"', "who")),
    d("who", '''"A fence." {n}She says it the way another woman might say a cousin.{/n}
"Before I had one hand, I had a knack for findin' things, and some of the folk I found 'em through were the sort you don't bring home. There was one, in a river town, who could find a nail in a snowstorm and tell you who'd dropped it. Ya couldn't snatch a nail from him. I tried once. I was younger."
{n}She seals the Nerosyan letter with a thumb of wax.{/n} "He owes me for a night I didn't tell a watch captain what I'd seen. He's the kind of man who pays that sort of debt, 'cause the other sort don't live long in his trade."''',
      c('"And if he can\'t get the helmets out?"', "stuck")),
    d("stuck", '''"Then they sit there till the war's over, and some Ustalavic customs clerk sells 'em to a vampire's honour guard, and three hundred of our lads go up the walls with their skulls in their hands." {n}She puts the Ustalav letter on top of the pile.{/n}
"Or you can help. You've a Trickster's hand, and the Commander's seal, and you've already put your name to one thing that isn't true in my book." {n}Her eye is steady.{/n} "I'm not askin'. I'm tellin' you what's on the table."''',
      c('[Forge a Mendevian treasury release, seal and all.]', "forge"),
      c('"I\'ll write to Ustalav as the Commander. Under my own seal, with a threat in it."', "honest"),
      c('"Send your fence. I\'d like to see what a man who owes Dorgelinda Stranglehold can do."', "fence")),
    d("forge", '''{n}She watches you do it: the treasury clerk's cramped hand, the flourish on the Chancellor's initial, the right grey wax, which she produces from a drawer without comment. When you hold it up to the lamp it would fool you. It very nearly fools her.{/n}
"The Chancellor dots his i's with a tick, not a dot." {n}She points.{/n} "Did him wrong. Customs won't know. I know." {n}She blows on the ink.{/n}
"If this comes back on us, it's my stores it comes back to, and your hand on the paper. You're gettin' very comfortable in my book, Commander."''',
      c("[Seal it.]", "sent", flags=(FORGED,), crusade=("Materials", 100), alignment=("Chaotic", 1))),
    d("honest", '''"A threat." {n}She considers it.{/n} "From the Commander of the Fifth Crusade to a customs clerk in Ustalav. That's a sledgehammer on a thumbtack." {n}She pushes paper across.{/n}
"Go on, then. Make it a good one. Mention the Worldwound, they don't like to think about the Worldwound down there." {n}She reads it when you finish, twice, and nods.{/n} "That'll frighten somebody. Maybe even the right somebody."''',
      c("[Seal it.]", "sent", flags=(HONEST_DEMAND,))),
    d("fence", '''{n}She laughs, a short bark that makes the clerk outside the door drop something.{/n}
"You'd like to see it." {n}She adds a line to the fence's letter in a hand even smaller than her own, and folds it twice more.{/n}
"All right. You'll see it. It'll cost me a debt I've been savin' ten years, but you'll see it, and when three hundred helmets come up the Nerosyan road with Ustalavic customs seals on 'em that nobody ever stamped..." {n}She seals it.{/n} "...you'll not ask how. That's the rule with him."''',
      c("[Agree to the rule.]", "sent", flags=(FENCE_CALLED,))),
    d("sent", '''{n}She stacks the sealed letters for the courier and sits back. Outside, the bell on the western wall rings the change of watch. Somewhere below, someone is hammering a new hinge onto a supply wagon.{/n}
"Folk in Nerosyan think the war's fought with swords. It's fought with letters. Who owes who, who'll send what, whose cart gets to the front before the other feller's." {n}She rubs her good eye.{/n}
"The Queen's retinue is givin' banquets in the capital with wine worth more than a company's potions. I've seen the bills. And here's me callin' in a fence to get my lads helmets." {n}She snorts.{/n} "Call me a freethinkin' rebel if you like."''',
      c('"A freethinking rebel."', "rebel"),
      c('"I\'d rather call you Dorgelinda."', "name")),
    d("rebel", '''"Hah. You'd be the first to say it to my face instead of behind it." {n}She gathers the letters.{/n}
"Next week, Commander. Bring your boots. And if a man in a river-town coat asks for me at the gate, you never saw him."''',
      c("[Leave her to her letters.]")),
    d("name", '''{n}She stops with the letters half gathered.{/n}
"Nobody calls me that. It's Quartermaster, or Stranglehold, or Chair, or 'that one-eyed dwarf'." {n}She finishes gathering them, very neatly.{/n}
"...Dorgelinda'll do. In here. Not in front of the clerks." {n}She clears her throat.{/n} "Next week. Bring your boots."''',
      c("[Leave her to her letters.]", flags=(L + "first_name",))),
], requires=("trickster.ever", GRIP), forbids=(DEBTS,), delay=48)


# --- 5. Receipts from the Abyss (Chapter 5, after the Commander's return). -------------------------------------------

office(RECEIPTS, "Receipts", '"You kept my column open?"', [
    nar("door", '''{n}Her office is barer than it was. Half the shelves are empty, and the ones that are not hold ledgers instead of stores. A requisition to Nerosyan lies on the desk with "DENIED" written across it in a clerk's hand and "LIARS" under it in hers.{/n}''',
        c("Continue", "awe", requires=(BACK_FROM_ABYSS,)),
        c("Continue", "first", forbids=(BACK_FROM_ABYSS,))),
    d("awe", '''"I said it at the council and I'll say it again where nobody's writin' it down. You came back from the Abyss itself." {n}She looks at you as if checking a delivery against its manifest, and finding it, against all odds, complete.{/n}
"I had a clerk come to me the week you went down into the Abyss. Young lad, very neat hand. Asked should he rule off the Commander's column. 'Lost with the Commander', he wanted to write." {n}She sniffs.{/n} "I sent him to count horseshoes for a fortnight."''',
      c("Continue", "column")),
    d("first", '''{n}She looks up when you come in and does not say anything for a long moment. She looks at you as if checking a delivery against its manifest, and finding it, against all odds, complete.{/n}
"You came back." {n}As if that settles an argument she has been having with someone.{/n}
"I had a clerk come to me the week you went down into the Abyss. Young lad, very neat hand. Asked should he rule off the Commander's column. 'Lost with the Commander', he wanted to write." {n}She sniffs.{/n} "I sent him to count horseshoes for a fortnight."''',
      c("Continue", "column")),
    d("column", '''"I don't write off a line 'cause the owner's gone to the Abyss. I'd have to write off half the Crusade." {n}She turns the ledger to your page. Your column has grown while you were gone: small entries, weekly, in her hand. You read the dates. One for every week you were away.{/n}
"Carried forward." {n}Every one of them says it.{/n} "Now. You went down there with four crates of cold iron and a wagon of pork and a party of heroes. What came back? I want receipts."''',
      c('[Empty your pack onto her desk.]', "pack"),
      c('"I thought about your ledger down there."', "thought"),
      c('"Did you miss me?"', "miss")),
    d("pack", '''{n}You empty it: a demon's coin that is warm to the touch, a stub of candle from somewhere with no sun, a broken buckle, two cold-iron arrowheads, blunted, a scrap of silk that smells of something you do not want to name.{/n}
{n}She sorts it with her good hand into two piles without being told which is which. The coin she does not touch. The arrowheads she picks up, turns in the lamplight, and sets upright, side by side, like soldiers.{/n}
"Two. Out of four crates." {n}She writes it.{/n} "That's a better rate of return than Nerosyan."''',
      c("Continue", "close", flags=(WELCOMED,))),
    d("thought", '''"Did you." {n}She does not look up. The pen has stopped.{/n}
"What'd you think? That I'd be sittin' here with my column open like a fool?" {n}Her good hand is flat on the page.{/n}
"...Well, you weren't wrong." {n}She writes something. You do not ask what.{/n} "I kept thinkin' of you signin' for the Abyss. If anyone could make the Abyss balance, it'd be you, and I'd have to find a way to audit it."''',
      c("Continue", "close", flags=(WELCOMED,))),
    d("miss", '''"Miss you?" {n}She leans back in her chair.{/n}
"I missed the balance. There's a hole in this book the exact shape of you, and every clerk who walked past it asked me what I was goin' to do about it." {n}She picks up the pen.{/n} "I told 'em I was waitin' for the owner to come and account for it. They thought I'd gone soft." {n}She writes.{/n} "Maybe I have. Don't tell the Council."''',
      c("Continue", "close", flags=(WELCOMED,))),
    d("close", '''"Right." {n}She shuts the book on your column, carefully, as if something might fall out.{/n}
"Everythin' in Drezen's gone to the Abyss while you were in it. Mendev's in pieces. The Queen marched on Iz and took the treasury's best clerks and every spare cart with her. I've got soldiers wearin' boots made of saddle leather." {n}She stands, and for once comes round the desk.{/n}
"Don't do that again, Commander. The goin' away. I haven't the stock to lose you."''',
      c("[Stand very still while she straightens your collar.]", "collar")),
    nar("collar", '''{n}She straightens your collar with her good hand, the way a quartermaster straightens a recruit's kit before an inspection, and her fingers stay a moment at your throat. Then she goes back round the desk and sits down and picks up the pen, and whatever it was is back in its column.{/n}''',
        c("[Leave her to it.]")),
], requires=("trickster.ever", COUNTED), forbids=(RECEIPTS, ABYSS), chapters=(5,))


# --- 6. Two out of three: the ration cut. ---------------------------------------------------------------------------

EAT_CHOICES = (
    c("[Take your own bowl. Pour half of it into the recruit's.]", "share"),
    c('"Quartermaster. Eat your ration. That\'s an order."', "order"),
    c("[Sit down across from her with your own bowl and say nothing.]", "sit"),
)

office(RATIONS, "Two out of three", '"You weren\'t at the mess."', [
    nar("start", '''{n}You find her not at her desk but at the end of the long table in the stores kitchen, where the clerks and carters eat. The bowls are half full, of barley and something that was a turnip. The soldiers eat without talking. At the far end of the table a boy of sixteen in a levy tunic is eating very slowly, to make it last.{/n}
{n}Dorgelinda's bowl is in front of him. Hers is empty, and very clean, as if it had never been used.{/n}''',
        c("Continue", "lied", requires=(RATIONS_LIE,)),
        c("Continue", "equal", requires=(RATIONS_EQUAL,), forbids=(RATIONS_LIE,)),
        c("Continue", "cut", requires=(RATIONS_CUT,), forbids=(RATIONS_LIE, RATIONS_EQUAL)),
        c("Continue", "short", forbids=(RATIONS_CUT,))),
    d("lied", '''"Don't." {n}She says it before you open your mouth.{/n}
"We cut every ration in Drezen, 'cause I asked you to. And we told the ranks it'd get better soon, 'cause I asked you to. It's a lie. It's vile. It's for their own good." {n}She does not look at the boy.{/n}
"So I don't get to eat my third while I'm lyin' to him about the other two. That's all."''',
      *EAT_CHOICES),
    d("equal", '''"Don't." {n}She says it before you open your mouth.{/n}
"You gave the order: nobody goes to battle on an empty stomach. Everyone eats as before. Very fine. And now the carts are late and I'm feedin' the whole of Drezen from a warehouse that's two-thirds air." {n}She does not look at the boy.{/n}
"So I eat last. That's the price of your fine order, and I'm the one keepin' the books on it."''',
      *EAT_CHOICES),
    d("cut", '''"Don't." {n}She says it before you open your mouth.{/n}
"Rations are short. You know they're short, you sat on the council that shortened 'em. Whoever tightens their belt is for you to decide, you said." {n}She does not look at the boy.{/n}
"I decided mine."''',
      *EAT_CHOICES),
    d("short", '''"Don't." {n}She says it before you open your mouth.{/n}
"Mendev's carts come half empty and a week late, when they come. We're feedin' Drezen on crumbs. I've told the council, and I'll tell 'em again when they want it louder." {n}She does not look at the boy.{/n}
"Somebody's got to eat less. I've more to spare than he has."''',
      *EAT_CHOICES),
    d("share", '''{n}You tip half your bowl into the boy's. He looks at the Commander, and at the quartermaster, and goes very red, and eats faster.{/n}
"Showin' off." {n}But she takes your bowl, with what is left, and eats half of that herself, fast, like a soldier, and pushes the rest back to you.{/n}
"There. Now nobody's eaten a full ration and nobody's eaten none. That's supply, Commander. Two out of three." {n}She wipes her mouth.{/n} "Don't make a habit of it. The ranks'll start wantin' commanders at their tables."''',
      c("Continue", "after", flags=(SHARED,))),
    d("order", '''{n}Every spoon at the table stops.{/n}
"...An order." {n}She looks at you for a long moment with the one eye. Then she takes a bowl from the stack, fills it at the pot, sits down, and eats every mouthful while holding your gaze, and sets the spoon down with a click.{/n}
"Ration consumed, Commander. Enter it where you like." {n}The table starts eating again.{/n} "You'll pay for that in the book. I've a long memory for orders I didn't want."''',
      c("Continue", "after", flags=(ORDERED,))),
    d("sit", '''{n}You sit. You eat. She watches you eat, and says nothing either, and after a while she reaches over with her spoon and takes one mouthful from your bowl, as if tasting for poison, and then another.{/n}
"The turnip's off," she says. "I'll have words with the cook." {n}She does not take a third. She does not need to.{/n}''',
      c("Continue", "after", flags=(SHARED,))),
    d("after", '''{n}Later, in her office, she opens your column and writes a line you can read, for once: Half ration, shared.{/n}
"I've fed armies on less than this, you know. On the hard postin's, before Drezen, the lads ate what the country let 'em and said thank you." {n}She stops.{/n} "Different war. Same arithmetic. Folk who've never been hungry think it's the cold that breaks an army. It's the empty bowl on the man beside you, and knowin' the officer's isn't."''',
      c('"Is that why you ate last?"', "last")),
    d("last", '''"That's why I eat last." {n}She caps the ink.{/n}
"Doesn't make me a saint. It makes me a quartermaster the ranks'll believe when I tell 'em a lie." {n}She is quiet a while.{/n}
"You sat at that table, Commander. They'll talk about it in the barracks for a month. You'll not have bought one crate with it, and you'll have bought more than a warehouse." {n}She puts the pen down.{/n} "Go on. I've letters to write to people who've never missed a meal."''',
      c("[Leave her to the letters.]")),
], requires=("trickster.ever", COUNTED, PRESENT), forbids=(RATIONS,), delay=48, chapters=(5,))


# --- 7. After hours (the intimate beat, after the commit). -------------------------------------------------------------

office(NIGHT, "After hours", '"The clerks have gone home."', [
    nar("start", '''{n}They have. The stores are dark but for her lamp. She has not opened the ledger. That is the first thing you notice: the book is shut, and her good hand lies on the cover, and she is looking at you.{/n}
"Bolt the door." {n}Not an order. She does not give you orders. It is a line in a manifest, read aloud.{/n}''',
        c("[Bolt it.]", "bolted")),
    d("bolted", '''"Right." {n}She gets up and comes round the desk, and stops close enough that you can smell the lamp oil and wool and the good stuff that is on no manifest.{/n}
"I've inventoried every inch of this fortress, Commander. Every crate, every nail, every horseshoe. I know what's in every barrel in Drezen." {n}Her eye moves over you, top to boot, slow.{/n} "Not you. Not yet. I've been doin' it by eye for weeks, and my eye's gettin' tired, and I've only got the one."''',
      c("[Take off your coat. Let her count.]", "coat"),
      c("[Reach for the strap of her eye patch.]", "patch"),
      c('"Well? Are you going to count, or just look?"', "count")),
    d("patch", '''{n}Her good hand closes on your wrist before your fingers reach the strap. Stranglehold. It does not hurt. It will not move either.{/n}
"Patch stays." {n}Very quietly.{/n} "What's under it isn't yours. It isn't anybody's. It went to a thing with claws, and the thing can keep it." {n}She brings your hand down, and does not let go of it, and puts it instead on the buckle of her own belt.{/n}
"That, you can have."''',
      c("Continue", "count")),
    d("coat", '''{n}You take off your coat and let it fall across her desk, on top of the ledger. She does not look at the ledger once.{/n}
"One coat. Officer's pattern. Mended at the left elbow, badly." {n}She lays her good hand flat on your chest, over the shirt, the way she lays it on a page to hold it still.{/n} "One shirt. Mine, as it happens, I issued it. One heart, beatin' faster than regulation."''',
      c("Continue", "count")),
    d("count", '''{n}She counts you. She does it the way she does everything: aloud, thoroughly, without hurry, with one hand. Buttons, one by one. The buckle. Your belt, which she lays across the desk like a ledger line. Each scar she finds she names, the old ones and the new, and asks nothing about any of them.{/n}
{n}Her own she does not name. You find them anyway: the long pale furrows down her arm from shoulder to wrist, the old white knot of a spear wound over the hip, the soft heavy strength of a body that has hauled crates for a lifetime and has never once been told it was beautiful and would not believe you if you tried.{/n}''',
      c('[Tell her anyway.]', "tell"),
      c('[Say nothing. Show her.]', "show")),
    d("tell", '''"Beautiful." {n}She snorts, and it catches halfway, and she puts her forehead against your shoulder so that you cannot see her face.{/n}
"You lyin' Trickster." {n}Her voice is thick.{/n} "You'd sign for anythin'. Say it again."''',
      c("Continue", "threshold")),
    d("show", '''{n}You show her. She lets you, for a while, standing, the edge of the desk behind her, her good hand fisted in your shirt as if it were the last rope on a sinking wagon.{/n}
"Hammer and tongs," {n}she breathes, not quite steady, and pulls.{/n}''',
      c("Continue", "threshold")),
    nar("threshold", '''{n}The ledger goes on the floor. She does not stop to pick it up. The cot in the back room is narrow and regulation and has never been meant for two, and she swears at it in Dwarven, fondly, the way she swears at a cart that will get there in the end. Her boots come off, and yours, and she drops them side by side, heel to heel, because she is who she is.{/n}
{n}Then she pulls you down onto the rough wool, and her dead hand lies on your back like a weight she has decided to let you carry, and the good one does not let go at all.{/n}''',
        c("[The lamp gutters out.]", flags=(NIGHT_KEPT,))),
], requires=("trickster.ever", COMMITTED), forbids=(NIGHT,), delay=12, chapters=(5,))


# --- 8. The morning count. ----------------------------------------------------------------------------------------------

office(MORNING, "The morning count", '"Mornin\'."', [
    nar("start", '''{n}You wake to the scratch of a pen. She is sitting on the edge of the cot, fully dressed, boots laced, the ledger on her knee. It is barely light. Beyond the shutters a supply wagon is being shouted into the yard.{/n}
{n}She is writing a line in your column. You can read it from the pillow: One night. Used, quietly.{/n}''',
        c('"You\'re putting that in the book?"', "book"),
        c("[Pull her back down.]", "back")),
    d("back", '''{n}She lets you, for exactly as long as it takes to kiss her, and then she is back on the edge of the cot with the ledger, and a hand flat on your chest to keep you where you are.{/n}
"Wagons, Commander. They don't unload themselves. They'd like to. I've seen 'em try." {n}She finishes the line.{/n}''',
      c('"You\'re putting last night in the book?"', "book")),
    d("book", '''"Everythin' goes in the book." {n}She blots it.{/n} "It's in code, if that eases your mind. My clerks can't read my code. Nobody can but me. The day I die, somebody in Nerosyan'll open this and find a line that says 'one night' next to your name and think it's the siege of somewhere."
{n}She closes the book.{/n} "Which it was, in a manner of speakin'."''',
      c("Continue", "sergeant")),
    d("sergeant", '''{n}Somebody knocks. She does not move.{/n}
"Ma'am?" {n}The sergeant with the bandaged ear, through the door.{/n} "Ma'am, the Commander's boots are in the office. One of 'em. Under the desk. Should I send 'em up to the citadel?"
{n}Dorgelinda closes her eye for a long moment.{/n}
"No, Sergeant," she calls. "Log 'em as returned stores. Commander's boots, one pair, to be counted at the Commander's convenience."
{n}A pause, full of thought, on the other side of the door. "Yes, ma'am."{/n}''',
      c("Continue", "consequence")),
    d("consequence", '''"That'll be round the stores by noon and round the barracks by supper." {n}She stands, and straightens her coat, and looks at you with the plain level look she gives a cart with a cracked axle.{/n}
"I don't care what the ranks say. Let 'em say the Commander's in the quartermaster's book. You are. But there's folk in Nerosyan who'd like nothin' better than a reason to say the Commander's stores are bein' run from a bed." {n}Her jaw sets.{/n} "So in the office, it's Quartermaster, and it's the ledger, and it's nothin' else. You understand?"''',
      c('"Quartermaster. Understood."', "understood"),
      c('"Let them say it. I\'ll sign for it."', "sign")),
    d("understood", '''"Good." {n}She picks up your other boot from beside the cot and hands it to you, sole first, like issuing kit.{/n}
"And out of the office..." {n}She considers it, frowning, as if it were a line with no precedent.{/n} "Out of the office, you can call me what you like. Once. Then I'll decide if I like it." {n}She goes to shout at the wagon.{/n}''',
      c("[Put your boot on.]", flags=(L + "office_rules",))),
    d("sign", '''{n}She stares at you. Then, to your very great surprise, she laughs, short and hard, the bark that makes clerks drop things.{/n}
"You would. You'd sign for anythin'." {n}She hands you your other boot, sole first, like issuing kit.{/n}
"Fine. Sign for it, then. But you sign in my book, not theirs, and you let me be the one who decides who reads it." {n}She goes to shout at the wagon.{/n} "And put your boot on. You look like a Fellow of the Crusade."''',
      c("[Put your boot on.]", flags=(L + "signed_for_it",))),
], requires=("trickster.ever", NIGHT), forbids=(MORNING,), delay=6, chapters=(5,))


# --- 9. The inquiry: Nerosyan wants the ledgers. -------------------------------------------------------------------------

INQUIRY_CHOICES = (
    c('"Send them the true books. My line open, the Fellows\' book if we kept it. All of it."', "true_books",
      crusade=("Favors", -100)),
    c('[Write them a ledger that balances, in your own hand.]', "clean_copy", crusade=("Finances", -100),
      alignment=("Chaotic", 1)),
    c('"Put your name on it, then. It\'s your stores."', "her_name"),
)

office(INQUIRY, "The inquiry", '"You look like you\'ve had a letter."', [
    d("start", '''"I've had a letter." {n}She holds it up by one corner, as if it were wet. It carries the seal of the Mendevian treasury, or what is left of the treasury.{/n}
"Nerosyan wants the ledgers. All of 'em. They've heard talk in the capital about where Drezen's stores go, and none of it's kind. Some lord who's never missed a meal wants to see the books." {n}She drops it on the desk.{/n} "They'll see your line. Open, since the caravans. Carts, a warehouse, twenty-some things nobody can account for."''',
      c("Continue", "dirty", requires=(DIRTY,)),
      c("Continue", "clean", requires=(CLEAN,), forbids=(DIRTY,)),
      c("Continue", "plain", forbids=(CLEAN, DIRTY))),
    d("dirty", '''"And they'll see the other book, if they look in the right drawer. Their methods, my hand. Weight discrepancies here, carts that fell off in transit there." {n}She puts her good hand on the thin ledger, the one in the smaller script.{/n}
"I kept it better than they ever did. That won't save either of us if the wrong clerk opens it."''',
      c("Continue", "offer")),
    d("clean", '''"There's no second book. You burned it for me, or I burned it for you, and I've been sleepin' better since." {n}She taps the letter.{/n}
"Doesn't matter. Your line's enough to hang a commander in the eyes of a lord who wants one hanged."''',
      c("Continue", "offer")),
    d("plain", '''"It's enough to hang a commander in the eyes of a lord who wants one hanged." {n}She taps the letter.{/n}''',
      c("Continue", "offer")),
    d("offer", '''{n}She sits back. Her face does the thing it did at the tribunal, when she looked at Bartley: nothing at all.{/n}
"Here's what I'll do. I'll put my name on it. The whole column. Quartermaster's error, quartermaster's thievin', one-eyed dwarf lost her grip. They'll believe it. They want to believe it of somebody." {n}She shrugs.{/n} "You can court-martial me after the war if you want. For now, we need you on the walls more than we need me in the stores. Arithmetic."''',
      c("Continue", "asked_before", requires=(COURT_MARTIAL,)),
      c("Continue", "choice", forbids=(COURT_MARTIAL,))),
    d("asked_before", '''"I said it at the council, when we were robbin' Mendev and callin' it donations for the war of faith. I meant it then. I mean it more now." {n}Her good hand is flat on the letter.{/n} "It's a good trade, Commander. One quartermaster for one Commander. Nerosyan'd take it in a heartbeat."''',
      c("Continue", "choice")),
    d("choice", '''"So. What goes to Nerosyan?"''', *INQUIRY_CHOICES),
    d("true_books", '''{n}She looks at you for a long moment. Then she opens the drawer and takes out every ledger she has, and stacks them, and ties them with cord, and does not remove a page.{/n}
"The truth. To Nerosyan. Hammer and tongs." {n}She knots the cord hard.{/n} "They'll hate you for it in the capital. The lords'll say the Commander admits to it. The ranks'll say the Commander told the truth to the lords, which nobody's done in a hundred years." {n}She sets the bundle by the door.{/n} "I don't know which'll be louder. I'll be proud of you either way, and I'll not say so again."''',
      c("Continue", "after", flags=(TRUE_BOOKS,))),
    d("clean_copy", '''{n}It takes you the whole night. She sits across from you and reads each page as you finish it, and corrects your arithmetic twice, and once your spelling. By dawn there is a stores ledger for Drezen that balances to the copper, in your hand, with no Commander's line and no second book in it. The couriers and the copyist who seals it will want paying, and paying well, for their silence.{/n}
"Used, quietly." {n}She holds the last page to the lamp.{/n} "That's the best forgery I've ever seen, and I've seen 'em in three kingdoms." {n}She does not smile.{/n} "It's a lie in my book, Commander. First one I've ever sent to Nerosyan. I'll carry it. Don't ask me to like it."''',
      c("Continue", "after", flags=(CLEAN_COPY,))),
    d("her_name", '''"Right." {n}She says it very evenly. She picks up the pen and writes her name at the foot of your column, under the carts and the warehouse and the boots, in the same small hard hand: D. Stranglehold, Quartermaster. Her error.{/n}
"There. Now it's mine." {n}She blots it, and closes the book, and does not look at you.{/n}
"I'll go to Nerosyan when the war's done. Not before. Not while there's a wagon in this yard that needs countin'." {n}A long pause.{/n} "You made the right arithmetic, Commander. I told you to. I just didn't think you'd do it."''',
      c("Continue", "after", flags=(HER_NAME,))),
    nar("after", '''{n}The courier leaves at noon. Out in the yard the carts are being loaded for the front, wagon after wagon, with whatever Drezen has left, which is not enough and will have to be.{/n}
{n}She watches them from the doorway with her arms folded, the good one over the bad one, and does not come back in until the last one is through the gate.{/n}''',
        c("[Wait for her.]")),
], requires=("trickster.ever", MORNING, METHODS), forbids=(INQUIRY,), delay=48, chapters=(5,))


# --- 10. Carried forward: before the last march. -----------------------------------------------------------------------

LAST = (
    c("[Sign the receipt now, in advance: \"Commander, returned. Received in good order.\"]", "receipt"),
    c("[Kiss her, in front of the wagons, and never mind the clerks.]", "kiss"),
    c("[Salute her. Properly. The way the ranks salute her.]", "salute"),
)

office(FORWARD, "Carried forward", '"You\'re ridin\' with the wagons?"', [
    nar("start", '''{n}She is in the yard, not the office, in a travelling coat and her old campaign boots, checking the lashings on the last supply wagon with her good hand. The column is forming up for the march on the Wound. There is a pack on the wagon seat with her ledger strapped on top of it.{/n}''',
        c("Continue", "going")),
    d("going", '''"I'm ridin' with the wagons." {n}She does not stop checking lashings.{/n}
"You're goin' to the end of the world, Commander, and the end of the world hasn't got a quartermaster. Somebody's got to make sure you've got arrows when you get there, and I'll not trust it to a clerk who's never seen a demon."
{n}She tugs the last rope, tests it, and it holds.{/n} "Don't argue. I've heard every argument. I've a pen, a knife and one good hand, and the hand's the dangerous one."''',
      c('"I wasn\'t going to argue."', "wasnt"),
      c('"Stay. I need someone left to count what comes back."', "stay")),
    d("stay", '''"Somebody's left. Three clerks and a sergeant with one ear. They can count." {n}She turns round at last.{/n}
"You asked me what I wanted done with the line. Keep it open, you said. Me in the book with it." {n}Her eye is very steady.{/n} "You don't keep a line open from a hundred leagues back, Commander. You keep it open by bein' where it is."''',
      c("Continue", "boots")),
    d("wasnt", '''"Liar." {n}Without heat.{/n} "You were goin' to argue and then you thought better of it. That's growth. I'll put it in the book."''',
      c("Continue", "boots")),
    d("boots", '''{n}She reaches into the pack and takes out a folded paper and a stub of pencil.{/n}
"Receipt." {n}She holds it out.{/n} "Your party, issued: one Commander. To be returned. I've written it already. All you need to do is come back and sign that you've come back, and I'll close it. Just that one." {n}A pause.{/n} "The rest stays open."''',
      c("Continue", "paid", requires=(BOOTS_PAID,)),
      c("Continue", "choose", forbids=(BOOTS_PAID,))),
    d("paid", '''"The boots stay here." {n}She nods at the stores door.{/n} "The last pair, the ones you paid your debt in. Top shelf, unworn. I'm not issuin' 'em to anyone else, and I'm not takin' 'em to the Wound to get demon on 'em." {n}Something moves in her face.{/n} "You come back and you can have 'em. Not before."''',
      c("Continue", "choose")),
    d("choose", '''{n}Around you the column is moving. A horn sounds from the walls. The Wound's light is on every face in the yard.{/n}''', *LAST),
    d("receipt", '''{n}You sign it. In advance, in pencil, on the back of her wagon: Commander, returned. Received in good order.{/n}
{n}She reads it. She reads it again. Then she folds it very small and puts it inside her coat, over her heart, where she keeps nothing else.{/n}
"Used, quietly," {n}she says, and her voice goes wrong on the second word.{/n} "You've signed for somethin' that hasn't happened yet. That's a lie in my book, Commander." {n}She climbs up onto the wagon seat.{/n} "You'd better make it true."''',
      c("Continue", "end", flags=(RECEIPT,))),
    d("kiss", '''{n}Every clerk in the yard sees it. So do two sergeants, a column of Mendevian levies, a paladin on a warhorse and the carter of the wagon behind, who drops his reins.{/n}
{n}She lets it happen. Then she kisses you back, hard, with her good hand fisted in your collar, and lets go all at once.{/n}
"Well, that's in the book now," she says, rather hoarsely. "And theirs." {n}She climbs up onto the wagon seat.{/n} "Come back and sign the receipt, Commander. I'll not ask twice."''',
      c("Continue", "end")),
    d("salute", '''{n}You salute her, properly, heel to heel, the way the ranks salute her and nobody above the rank of sergeant ever has.{/n}
{n}She stares. Then she returns it, with the bad hand, as she always does, slowly, so that you can see the dead fingers held to her brow by nothing but the arm beneath them.{/n}
"Commander." {n}Her voice does not waver.{/n} "Come back and sign the receipt." {n}She climbs up onto the wagon seat.{/n}''',
      c("Continue", "end")),
    nar("end", '''{n}The wagon lurches. She takes the reins in her good hand. As it rolls toward the gate she opens the ledger on her knee, one-handed, against the jolt, and writes a line without looking at the page.{/n}
{n}You do not need to see it to know what it says.{/n}''',
        c("[Watch the wagon go.]")),
], requires=("trickster.ever", INQUIRY), forbids=(FORWARD,), delay=48, chapters=(5,))


# --- 11. The vrock's driver (the caravans path: the rider was signed before the tribunal). -----------------------------

office(VROCK, "The vrock's driver", '"Who\'s that in the corner?"', [
    nar("start", '''{n}A carter is standing in the corner of her office with his cap in both hands, the way men stand in front of a gallows they have heard about. He is broad, sunburned, with a cart driver's forearms and a liar's eyes, and he is looking at you with an expression you cannot at first place.{/n}
{n}Dorgelinda does not look up from her ledger.{/n}
"Tell the Commander what you told me."''',
        c("Continue", "driver")),
    d("driver", '''{n}The carter clears his throat.{/n}
"Sir. Ma'am. Commander." {n}He settles on the last one.{/n} "I lost a cart. On the Kenabres road. A vrock come down and carried it off, I told the Quartermaster, and she said to my face I was a liar and a Fellow and she'd see me hanged."
{n}He swallows.{/n} "And then she looked in her book, and it says the cart was issued. To you. For operations. So I'm not hanged."''',
      c('"Did a vrock take it?"', "vrock"),
      c("[Say nothing. Let him sweat.]", "sweat")),
    d("vrock", '''"...No, Commander." {n}Very quietly.{/n} "Fellows paid me four silver to turn off the road at the ford. I've a wife in Vigil and three little 'uns and the Crusade pays me in promises."
{n}Dorgelinda writes something without looking up.{/n}
"That's the first true thing he's said since the caravans," she says. "I wanted you to hear it. I wanted him to see who he owes his neck to."''',
      c("Continue", "owes")),
    d("sweat", '''{n}He sweats. It does not take long. Carters have no gift for silence.{/n}
"It weren't a vrock, Commander. Fellows paid me four silver to turn off the road at the ford. I've a wife in Vigil and three little 'uns and the Crusade pays me in promises."
{n}Dorgelinda writes something without looking up.{/n}
"Well done. Quieter than a thumbscrew." {n}She blots it.{/n} "I wanted you to hear it from him. I wanted him to see who he owes his neck to."''',
      c("Continue", "owes")),
    d("owes", '''{n}She puts the pen down and finally looks at the carter.{/n}
"You owe your neck to a line in my book. The Commander wrote it before anybody knew what it'd cover. It covers you." {n}Her eye moves to you.{/n} "It covers all of 'em. Every driver who took Fellows' silver to lose a cart. I could hang a dozen tomorrow and I can't touch one, 'cause the stores they lost were issued. To the Commander." {n}She says it the way another woman might say "to the plague".{/n}
"So you tell me what I do with him, Commander. It's your issue."''',
      c('"Put him back on the Kenabres road. With a cart. He\'ll never lose another."', "back"),
      c('"Let him go home to Vigil. Take his wages for the cart."', "home"),
      c('[Trickster] "Tell the Fellows a vrock took him too. Then find out who else they paid."', "spy")),
    d("back", '''{n}The carter stares at you as if you have grown a second head.{/n}
"You heard the Commander." {n}Dorgelinda jerks her chin at the door.{/n} "South gate, tomorrow, first light. You'll drive the flour wagon and you'll bring me back every sack or I'll have your hide for a map-case. Out."
{n}He goes, fast, and forgets his cap. She looks at it on the floor for a while.{/n}
"He'll never lose another. You're right." {n}She sounds almost sorry.{/n} "He'll drive that wagon through a demon's belly before he'll face me with a sack short. You've made a loyal man out of a liar with one line of ink. That's a nasty trick, Commander."''',
      c("Continue", "end", flags=(L + "driver_kept",))),
    d("home", '''{n}The carter looks at you, then at her, then at the door, and does not believe it until she jerks her chin.{/n}
"Wages forfeit. Go home. If I see you on my roads again I'll remember the vrock." {n}He goes, fast, and forgets his cap. She looks at it on the floor for a while.{/n}
"Three little 'uns in Vigil." {n}She picks the cap up with her good hand and hangs it on the peg by the door, where it will stay.{/n} "You'd have made a poor quartermaster, Commander. Or a very good one. I've not decided which."''',
      c("Continue", "end", flags=(L + "driver_sent_home",))),
    d("spy", '''{n}The carter's mouth opens and closes.{/n}
"A vrock took him too," {n}Dorgelinda repeats slowly. Then she laughs, the short bark that makes clerks drop things.{/n} "Hammer and tongs. You'd have him go back to the Fellows who paid him, tell 'em a vrock took his second cart as well, and see who else comes sniffin' for the goods."
{n}She turns to the carter.{/n} "You heard the Commander. You're a very unlucky man. Vrocks can't get enough of you. And every Fellow who asks you about it, you come and tell me their name."
{n}He goes, pale. She watches the door close.{/n} "That's a Trickster's answer. It's also a good one. I hate that."''',
      c("Continue", "end", flags=(L + "driver_turned",))),
    d("end", '''{n}She turns back to your column and adds a line to it in her small hard hand. You read it upside down: One carter. Issued.{/n}
"You keep collectin' things in my book, Commander. Carts. A warehouse. Now a man." {n}She blots it.{/n} "One of these days I'll have to decide what to do with the whole column. Not today. Today there's a flour wagon wants a driver."''',
      c("[Leave her to it.]")),
], requires=("trickster.ever", COUNTED, CARTS), forbids=(VROCK,), delay=24)


# --- 12. The corporal's account (the tribunal path, after the warehouse). ---------------------------------------------

office(BARTLEY, "The corporal's account", '"You look like you\'ve had news of Bartley."', [
    nar("start", '''{n}There is a letter on her desk, or what serves for one: a sheet torn from a regimental roll, folded small, the address written in charcoal.{/n}''',
        c("Continue", "hanged", requires=(HANGED_LANN,)),
        c("Continue", "hanged", requires=(HANGED_WENDUAG,), forbids=(HANGED_LANN,)),
        c("Continue", "prison", requires=(PRISON,), forbids=(HANGED_LANN, HANGED_WENDUAG)),
        c("Continue", "hushed", requires=(HUSHED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON)),
        c("Continue", "redeemed", requires=(REDEEMED,), forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED)),
        c("Continue", "none", forbids=(HANGED_LANN, HANGED_WENDUAG, PRISON, HUSHED, REDEEMED))),
    d("hanged", '''"He gave it to the chaplain the night before, to give to me after." {n}She does not touch it.{/n} "I've read it once. I'll not read it twice. He writes a fair hand for a thief."
{n}She pushes it across. The charcoal is smudged but legible: Tell the Commander I know about the book. Tell the Commander it was a good trick and I'd have done the same. Tell the Commander the potions saved twelve. Don't let them write that bit down wrong.{/n}''',
      c("Continue", "potions")),
    d("prison", '''"From the road to Nerosyan. The escort let him write it at a waystation, which they shouldn't have, and I'll have words." {n}She pushes it across.{/n}
{n}The charcoal is smudged but legible: The chains fit. Tell the Commander I know about the book. Tell the Commander it was a good trick and I'd have done the same. Tell the Commander the potions saved twelve. Don't let them write that bit down wrong.{/n}''',
      c("Continue", "potions")),
    d("hushed", '''"From some fort at the end of the world. Come by a carter who swears he doesn't know who gave it to him, which means he does." {n}She pushes it across.{/n}
{n}The charcoal is smudged but legible: Very cold here. No bulettes. Tell the Commander I know about the book. Tell the Commander it was a good trick and I'd have done the same. Tell the Commander the potions saved twelve. Don't let them write that bit down wrong.{/n}''',
      c("Continue", "potions")),
    d("redeemed", '''"He brought it himself. Knocked, very polite, stood there with a shovel on his shoulder and handed it over like a report." {n}She pushes it across.{/n}
{n}The charcoal is smudged but legible: Tell the Commander I know about the book. Tell the Commander it was a good trick and I'd have done the same. Tell the Commander the potions saved twelve. Don't let them write that bit down wrong.{/n}
"He could've said it to your face. He's diggin' latrines fifty yards from here. He'd rather write it. Soldiers."''',
      c("Continue", "potions")),
    d("none", '''"It's from one of his. Bartley's lot. It came through the stores in a sack of oats, which is the Fellows' idea of a courier." {n}She pushes it across.{/n}
{n}The charcoal is smudged but legible: Tell the Commander we know about the book. Tell the Commander it was a good trick. Tell the Commander the potions saved twelve. Don't let them write that bit down wrong.{/n}''',
      c("Continue", "potions")),
    d("potions", '''"Don't let them write that bit down wrong." {n}She repeats it with no expression.{/n}
"Every thief I ever caught wanted the same thing. Not mercy. Not the rope took off. They wanted the book to say why." {n}She taps the ledger.{/n} "The book never says why, Commander. It says how many and when and whose. The why's what the lords in Nerosyan make up afterwards to feel clean."''',
      c("Continue", "ours", requires=(POTIONS_OURS,)),
      c("Continue", "his", requires=(POTIONS_BARTLEY,)),
      c("Continue", "ask", forbids=(POTIONS_OURS, POTIONS_BARTLEY))),
    d("ours", '''"You put the potions in your own column, the night we counted the warehouse. Used, quietly. Twelve lines under it." {n}She opens the book and shows you, as if you might have forgotten.{/n}
"So it's written down right. He'll never know. I'll not tell him." {n}She closes it.{/n} "That's the only kind of kindness a ledger's good for: the kind nobody sees."''',
      c("Continue", "ask")),
    d("his", '''"You put the potions on him, the night we counted the warehouse. Theft. That's the law." {n}She opens the book and shows you the line, in her own hand: stolen, C. N. Bartley.{/n}
"So it's written down wrong. By the book. By me." {n}She closes it.{/n} "He asked for one thing, Commander. I'll not pretend we gave it."''',
      c("Continue", "ask")),
    d("ask", '''{n}She folds the charcoal letter small again, and does not put it in the ledger. She puts it inside her coat.{/n}
"Answer me one thing and I'll not ask again. When you wrote that rider, that first day, at the caravan council or at the table with the ink wet. Did you do it for him? For them? Or 'cause you're a Trickster and you couldn't stand to see a book balance?"''',
      c('"For them. Soldiers who stole bread to fight."', "them"),
      c('"Because I could. And because you\'d notice."', "notice"),
      c('"I did it for you. You didn\'t want to hang them."', "you")),
    d("them", '''"For them." {n}She nods slowly.{/n} "That's the answer a paladin would want. You don't look like a paladin." {n}She considers you.{/n}
"But I believe it. You've the look of somebody who's been hungry in a ditch with a sword on their knees. Most commanders haven't." {n}She picks up her pen.{/n} "Right. Back to the stores."''',
      c("[Leave her to it.]", flags=(L + "for_them",))),
    d("notice", '''{n}She stares at you.{/n}
"Because I'd notice." {n}Something moves in her face, and is put away.{/n} "You wrote a lie in my book so the one person in Drezen who reads every line would find it. That's either the most arrogant thing I've ever heard or the..." {n}She stops.{/n} "...Hammer and tongs. Get out of my office, Commander. I've work."
{n}She is still looking at the door when it closes.{/n}''',
      c("[Leave her to it.]", flags=(L + "for_notice",))),
    d("you", '''"For me." {n}She laughs, not kindly.{/n} "Nobody's ever done a thing for old Dorgelinda in this whole Crusade that wasn't a trade, and you'll not start with a warehouse."
{n}But she does not say it is a lie. She sits with the letter inside her coat and her good hand flat on the book.{/n}
"I stood at that tribunal and said it's rotten, hangin' your comrades. You heard me." {n}Quietly.{/n} "...Get out, Commander. Before I start believin' you."''',
      c("[Leave her to it.]", flags=(L + "for_her",))),
], requires=("trickster.ever", WAREHOUSE, TRIBUNAL), forbids=(BARTLEY,), delay=48)


# --- 13. After the council: the other voices at her table. ----------------------------------------------------------

office(COUNCIL, "After the council", '"You look like you\'ve sat through the Logistics Council."', [
    d("start", '''"I've sat through the Logistics Council." {n}She pours two cups from the bottle that is on no manifest before you have finished sitting down.{/n}
"You'd think, with the Worldwound on the doorstep and demons on the walls, a supply council would talk about supply. No. We talk about Woljif's schemes and whether Lann's lads can live on purple moss, and the rest of the table talks about honesty." {n}She drinks.{/n} "I've never in my life wanted to strangle so many people with one hand."''',
      c('"Tell me what you really think of them."', "think"),
      c('"You like them."', "like")),
    d("like", '''"Like 'em?" {n}She snorts into the cup.{/n} "I'd die for 'em. That's different. Liking's for people who've got time." {n}She sets the cup down.{/n}
"Go on, then. Ask me about each one. I've been savin' it up. It's a long war and nobody asks the quartermaster."''',
      c("Continue", "think")),
    d("think", '''"Woljif." {n}She holds up one finger of the good hand.{/n} "Thinks every problem's a lock and every lock's a joke. He's right more often than I'd like. I'd trust him with my purse and not my stores, which you'll notice is the wrong way round, and I know it, and so does he."
"The honest ones." {n}A second finger.{/n} "Want everyone to be good. Ask me what honest people would do. I tell 'em honest people are the ones who haven't been hungry yet, and they look at me like I've kicked a dog."''',
      c("[Wait for the others.]", "others")),
    d("others", '''"Lann." {n}Third finger.{/n} "Good lad. Thinks everyone can live on nothin' 'cause his people did. They can't. His people buried a lot of the ones who couldn't. He knows it. He doesn't say it."
"And the hard ones." {n}She does not raise a fourth finger. She puts the hand flat on the table.{/n} "Want the strong fed and the weak to learn. I've seen armies run that way. They win for a season. Then they eat each other." {n}She drinks.{/n} "They'd say I'm soft. They'd be right. Soft's what keeps a supply line from gettin' its throat cut by its own soldiers."''',
      c('"And you? What would you have them say about you?"', "her"),
      c('"And me?"', "me")),
    d("her", '''"Me." {n}She thinks about it seriously, as if it were a requisition.{/n}
"That she was a thief who counted twice. That she let the lads skim a little, within reason, and hanged nobody she didn't have to, and got the boots to the front more often than not." {n}A pause.{/n} "Two out of three, Commander. That's all anybody's ever managed. I'd like 'em to say I managed two."''',
      c("Continue", "me")),
    d("me", '''{n}She looks at you over the rim of the cup for a long moment.{/n}
"You." {n}She sets it down.{/n} "You sit at that council table and you listen to all of us and you pick one, and half the time you pick the one that makes the others sulk for a month. That's the job. I'd not do it for all the helmets in Ustalav."
"And then you come here after and let me pour you a drink and complain about 'em. That's not the job." {n}Her eye is very steady.{/n} "Nobody told you to do that."''',
      c('"Nobody had to."', "nobody"),
      c('[Flirt] "The drink\'s better here."', "drink")),
    d("nobody", '''"No." {n}Very quietly.{/n} "Nobody had to."
{n}She refills your cup without asking, which she has never done, and writes nothing in the book, which she has never done either.{/n}
"Go on, then. Tell me about the war. The part the council doesn't hear. I'll not write it down."''',
      c("[Tell her about the war.]", "tell")),
    d("drink", '''"The drink's better here 'cause I found it, and I found it 'cause I know where things get lost." {n}She refills your cup without asking, which she has never done.{/n}
"You'll get a reputation, Commander, drinkin' with the quartermaster. The lords'll say you're lookin' to rob your own stores." {n}She clinks her cup against yours.{/n} "Let 'em. You already have. Tell me about the war. The part the council doesn't hear."''',
      c("[Tell her about the war.]", "tell")),
    nar("tell", '''{n}You tell her. Not the victories: the bits between. The night march in the rain. The soldier who asked you for a light and was dead by morning. The hole in the line nobody filled because nobody knew it was there. She listens the way she counts, without hurry, her good hand around the cup, and does not interrupt once.{/n}
{n}When you are done the bottle is lower than it was and the lamp needs trimming.{/n}''',
        c("Continue", "done")),
    d("done", '''"Right." {n}She trims the lamp one-handed.{/n}
"That's the column nobody keeps. The one that says what it cost." {n}She caps the bottle.{/n} "I'll keep it, if you like. Not in the book. In here." {n}She taps her temple, by the patch.{/n}
"Same time next week, Commander. Bring your boots."''',
      c("[Leave the last of your cup for her.]", flags=(L + "war_told",))),
], requires=("trickster.ever", DEBTS), forbids=(COUNCIL, "woljif.dead", "woljif.kicked_out", "lann.dead", "lann.kicked_out", "lann.plot_absent"), delay=48)


# --- 14. The west gate: a supply wagon under attack. ----------------------------------------------------------------

office(GATE, "The west gate", '"Quartermaster? What\'s the bell?"', [
    nar("start", '''{n}The alarm bell on the western wall is ringing when you reach her office, and she is not in it. She is in the yard, one-handed, buckling on a breastplate that has not been buckled in years, while a clerk tries to help and gets swatted.{/n}
"Supply wagon," she says, without turning. "Three hundred yards out, broken axle, and somethin' with wings circlin' it. The gate captain won't open for a cart. I'm not askin' him."''',
        c('"Then I\'ll open it."', "open"),
        c('"You\'re not going out there."', "stay")),
    d("stay", '''"I'm goin' out there." {n}She picks up a boar spear from the rack by the stores door, the only weapon in the building that is not on a manifest.{/n}
"That wagon's got two hundred pairs of boots on it, and a carter who's got a wife in Vigil, and I signed for both. You can come, or you can order me to stay, and then I'll go anyway and you can court-martial me after." {n}She sets the spear across her shoulder.{/n} "Your choice, Commander. Choose fast."''',
      c('"I\'ll open the gate."', "open")),
    nar("open", '''{n}The gate captain opens it when the Commander tells him to, fast, with his mouth tight. You run out onto the road with Dorgelinda beside you at a dwarf's pace, which is not slow. Three hundred yards. The wagon is on its side in the ditch, the carter under it, and above it something like a vulture the size of a horse wheels and screams.{/n}
{n}It comes down.{/n}''',
        c('[Draw its attention.]', check=dict(Skill="SkillMobility", DC=25, Success="dodge", Failure="hit", CommanderOnly=True)),
        c("[Get between it and her.]", "hit")),
    nar("dodge", '''{n}You are not where its claws were. You never were. It screams again and turns, and turns straight onto Dorgelinda's spear, which she has set against the road with one hand and her whole weight behind it, the way somebody taught her a very long time ago.{/n}
{n}It takes a long time to stop moving. She does not let go of the spear until it has.{/n}''',
        c("Continue", "after")),
    nar("hit", '''{n}Its claws open your shoulder. You go down in the mud and it comes over you, and then it screams and jerks back, because Dorgelinda has come round the wagon and set her boar spear against the road with one hand and her whole weight behind it, and it has run itself straight onto the point.{/n}
{n}It takes a long time to stop moving. She does not let go of the spear until it has.{/n}''',
        c("Continue", "after", flags=(L + "gate_wound",))),
    d("after", '''{n}She is breathing hard. Her good hand is shaking now that it can.{/n}
"Two hundred pairs," {n}she says, to nobody, and then, to the carter under the wagon,{/n} "you all right under there?" {n}A muffled answer.{/n} "Good. Stay there."
{n}She turns to you. She looks at you for a long moment, and then, very briefly, she puts her forehead against your collarbone, and leaves it there for the space of one breath.{/n}
"That's how I lost the eye," {n}she says into your coat.{/n} "Somethin' with claws. I thought I'd forgotten what it looked like comin' down."''',
      c("[Hold on to her.]", "hold"),
      c('"You didn\'t forget. You set the spear."', "spear")),
    d("hold", '''{n}You hold her. On the road, in the mud, with the dead thing in the ditch and the wall full of watching soldiers. She lets you, for two breaths, three, and then she straightens and steps back and is the quartermaster again.{/n}
"Right. Boots." {n}She raises her voice to the wall.{/n} "You lot! Down here with a spare axle and six strong backs, and anyone who's got somethin' to say about the Commander can say it to the Commander!"
{n}Nobody on the wall says anything.{/n}''',
      c("Continue", "end", flags=(L + "held_on_road",))),
    d("spear", '''"I set the spear." {n}She looks down at it.{/n} "One hand's all you need, if you set it right." {n}Something that is almost a laugh.{/n}
"Don't tell the jokesters. They'll want a new nickname." {n}She straightens, and raises her voice to the wall.{/n} "You lot! Down here with a spare axle and six strong backs!"''',
      c("Continue", "end")),
    d("end", '''{n}Back inside the walls, with the wagon hauled home and the boots counted, she writes it in your column: Two hundred pairs, recovered. One carter, recovered. One Commander, out the gate on the quartermaster's account.{/n}
"That last line's the dearest thing on the page." {n}She blots it.{/n} "Don't do it again. I'll not have the stock to replace you."''',
      c("[Let her write.]")),
], requires=("trickster.ever", COUNCIL), forbids=(GATE,), delay=48)


# --- 15. A weight discrepancy (Chapter 5: her Mendevian connections). ------------------------------------------------

office(WEIGHT, "A weight discrepancy", '"That\'s a lot of barrels for a crusade with no money."', [
    nar("start", '''{n}The yard behind her stores is full of barrels. Some are marked for the Mendevian army, some for a brewery in Nerosyan, some for nobody. A carter is unloading more. Dorgelinda stands among them with a slate, chalking numbers that do not add up.{/n}''',
        c("Continue", "free", requires=(FREE_REIN,)),
        c("Continue", "refused", requires=(PLUNDER_REFUSED,), forbids=(FREE_REIN,)),
        c("Continue", "plain", forbids=(FREE_REIN, PLUNDER_REFUSED))),
    d("free", '''"You gave me free rein at the council. So." {n}She spreads the good hand at the yard.{/n}
"Old army pals, drinkin' partners, a few long-overdue debtors. Each one sends a cart, a barrel, a chest. Not enough to cause a fuss in Nerosyan. Just a weight discrepancy here, some cargo that must've dried out or fallen off in transit there."''',
      c("Continue", "how")),
    d("refused", '''"You told the council we'd take no part in the plunderin' of Mendev. Very noble. It's just a shame your conscience can't fill an empty belly." {n}She spreads the good hand at the yard.{/n}
"So these aren't plunder. These are old debts. Army pals, drinkin' partners, men who owe me. Each one sends a cart, a barrel, a chest, and I don't ask where it was before it was his."''',
      c("Continue", "how")),
    d("plain", '''"There's no buyin' honest in Mendev this year. So I'm callin' in debts." {n}She spreads the good hand at the yard.{/n}
"Old army pals, drinkin' partners, men who owe me. Each one sends a cart, a barrel, a chest. Just a weight discrepancy here, some cargo that must've dried out or fallen off in transit there."''',
      c("Continue", "how")),
    d("how", '''{n}She hands you the slate.{/n}
"You'll want to see how it's done. You of all people." {n}She points with the chalk.{/n} "A barrel of salt pork weighs what it weighs at the depot. Two days on a wet road and it's lost a stone to the damp, the carter swears. Nobody weighs it at the other end but me. So the depot writes one weight and I write another and the difference is in my yard." {n}She taps the slate.{/n} "Used, quietly. That's your trick, and it's older than you."''',
      c('"You\'re stealing from Mendev."', "stealing"),
      c('"You\'re better at it than the Fellows ever were."', "better")),
    d("stealing", '''"I'm stealin' from Mendev." {n}She agrees without heat.{/n}
"And Mendev's stealin' from itself, every lord in it, ever since the Queen squeezed it dry to march on Iz. Everythin' that's not nailed down's walkin'. I'd rather it walked here than into some baron's cellar." {n}She chalks another figure.{/n}
"You want to stop me, you give the order, and I'll send every barrel back with an apology, and next month our lads'll eat their boots. Your call."''',
      c('"Keep them. But keep the true weights too. In your own book."', "keep"),
      c('"Send the brewery\'s back. That\'s someone\'s living. Keep the army\'s."', "sort")),
    d("better", '''"Better than the Fellows." {n}She considers it, chalk in hand.{/n}
"They stole for themselves and called it fairness. I steal for the lads and don't call it anythin'. That's the only difference, and some days it's not much of one." {n}She looks at the barrels.{/n}
"You'll want to decide if that's a compliment, Commander. I've decided to take it as one."''',
      c('"Keep them. But keep the true weights too. In your own book."', "keep"),
      c('"Send the brewery\'s back. That\'s someone\'s living. Keep the army\'s."', "sort")),
    d("keep", '''"The true weights." {n}She looks at you with the one eye for a long moment.{/n}
"You want me to write down every stone I took, in my own hand, so there's one book in the world that knows." {n}She takes the slate back.{/n} "That's a dangerous book to keep, Commander. Any lord who got hold of it could hang me with it." {n}She tucks the slate under her arm.{/n} "...I'll keep it. Next to yours. They can hang together."''',
      c("Continue", "end", flags=(L + "true_weights",))),
    d("sort", '''"Somebody's livin'." {n}She repeats it, and snorts, and then she goes and finds the brewery barrels herself, all six, and has them loaded back on the carter's wagon, and pays him a silver from her own purse for his trouble.{/n}
"There. One honest thing in the yard." {n}She dusts her hand.{/n} "Don't tell the lads. They'd rather have had the beer."''',
      c("Continue", "end", flags=(L + "brewery_returned",))),
    d("end", '''{n}She chalks the last figure and hangs the slate on its nail.{/n}
"Two out of three, Commander. Armed, armoured, fed. This month we'll manage fed." {n}She glances at you sidelong.{/n} "And you came out to the yard and let me show you. You'd make a fair thief, with trainin'. I'll not say that in front of the Council."''',
      c("[Help her roll the last barrel in.]")),
], requires=("trickster.ever", COUNTED, PRESENT), forbids=(WEIGHT,), delay=24, chapters=(5,))


# --- 16. The Fool King's bill (Chapter 5, after the Trickster's coronation). ------------------------------------------

REVEL_CHOICES = (
    c('"Put it on my line."', "mine", crusade=("Finances", -200)),
    c('"Send the bill to the King."', "king"),
    c('[Trickster] "It was a jest. You can\'t bill a jest."',
      check=dict(Skill="CheckBluff", DC=28, Success="jest_won", Failure="jest_lost", CommanderOnly=True)),
)

office(REVELS, "The King's bill", '"You look like you\'ve had a very long night."', [
    nar("start", '''{n}You find her in the cellars under the stores, with a lantern, a slate and a face like a winter storm. The racks around her are empty. All of them. The floor is sticky, and smells of wine and ale and something that was once a barrel of good brandy and is now a stain.{/n}''',
        c("Continue", "crowned", requires=(KING_REVEL,)),
        c("Continue", "merry", forbids=(KING_REVEL,))),
    d("crowned", '''"The fools and drunks lined up to greet you, I hear." {n}She does not turn around.{/n} "And farted up a rousin' march with their backsides, and your King Thaberdine conducted with his crown. I didn't see it. I was down here, watchin' 'em carry out my cellar."
{n}She holds up the slate. It is covered in figures, very small, very neat.{/n} "This is the bill."''',
      c("Continue", "bill")),
    d("merry", '''"The whole merry city of Drezen, ringin' with songs and drunken laughter, and the smell of booze all through the streets." {n}She does not turn around.{/n} "You'll have noticed. Everyone noticed. I noticed first, 'cause it was my booze."
{n}She holds up the slate. It is covered in figures, very small, very neat.{/n} "This is the bill."''',
      c("Continue", "bill")),
    d("bill", '''"Sixty-one barrels of ale. Nineteen of wine, the Mendevian red I was savin' for the wounded, 'cause it's the only thing that'll get a surgeon's dose down a man with no stomach left. Four of brandy. Every bottle of the good stuff that was on no manifest, which means I can't even claim it." {n}She turns around at last.{/n}
"We came back from Iz with half an army and nothin' in the wagons, and the city celebrated by drinkin' what little we had. That's the Trickster's triumph, Commander. I'm the one countin' it."''',
      *REVEL_CHOICES),
    d("mine", '''{n}She looks at you for a long moment. Then she writes it in your column, in full, figure by figure, and at the bottom a sum that makes your purse wince.{/n}
"Paid out of the Commander's own. So I can buy wine for the surgeons from some baron who'll overcharge me." {n}She blots it.{/n} "You'd have sooner paid it than argued. That's the one thing about you I never have to audit." {n}A pause.{/n} "It was a good party, I'm told. I'd have liked to have been at it, if it had been anybody else's cellar."''',
      c("Continue", "end", flags=(L + "revels_paid",))),
    d("king", '''"Send it to the King." {n}She considers it, slate in hand.{/n}
"The King of Fools, with a crown and a tin sceptre and his whole treasury in his boots." {n}Something happens to her mouth.{/n} "Oh, I'll send it. I'll send it with a clerk in full dress and a trumpet. And he'll read it out to his court of drunks, and they'll cheer it, and he'll pay me in a proclamation." {n}She writes on the slate: Charged to His Majesty.{/n}
"It'll be the most useless bill I ever sent. I'm goin' to enjoy it more than any bill I ever sent."''',
      c("Continue", "end", flags=(L + "revels_billed",))),
    d("jest_won", '''"A jest." {n}She stares at you.{/n}
"You're tellin' me a coronation's a jest, and a king's a jest, and the drink that went down the throats of the whole city in a jest is a jest, and a jest can't be billed." {n}She opens her mouth. She closes it. She looks at the slate.{/n}
"...Hammer and tongs." {n}She rubs it out with the heel of her bad hand.{/n} "There's no line in any ledger in the world for a jest. You're right. I've no column to put it in." {n}She looks, for a moment, genuinely lost.{/n} "I hate you, Commander. I'll invent a column."''',
      c("Continue", "end", flags=(L + "revels_jested",))),
    d("jest_lost", '''"A jest." {n}She does not even blink.{/n}
"A jest drank nineteen barrels of the surgeons' red. When the next lad with his belly opened asks what he's drinkin' for the pain, I'll tell him: a jest, son. The Commander's." {n}She writes it in your column anyway, figure by figure.{/n}
"Nice try. You'll pay it in coin or in boots or in somethin' else, and I'll decide which." {n}Her eye narrows.{/n} "Probably somethin' else."''',
      c("Continue", "end")),
    d("end", '''{n}She kicks at the sticky floor with her boot, and sighs, and blows out the lantern, so that you stand together for a moment in the dark of the empty cellar with the smell of the whole city's party around you.{/n}
"We won, though." {n}Very quietly, in the dark.{/n} "Didn't we. Whatever you did down there. We came back."''',
      c('"We came back."', "back")),
    nar("back", '''{n}She finds your hand in the dark with her good one, and holds it, briefly, and then lets go, and strikes a light, and is the quartermaster again, counting the empty racks by candle as if they might, if she looked hard enough, refill.{/n}''',
        c("[Help her count the empty racks.]")),
], requires=("trickster.ever", COUNTED), forbids=(REVELS,), delay=0, chapters=(5,),
   RequiresAnyGroups=[[MERRY_CITY, KING_REVEL]])


# --- 17. Buying forgiveness (Chapter 5): her faith, or what serves for it. --------------------------------------------

office(FAITH, "Buying forgiveness", '"I didn\'t know you prayed."', [
    nar("start", '''{n}There is a small iron hammer on her desk that was not there before, the kind a smith uses for fine work, and she is holding it in her good hand and turning it over and not using it for anything.{/n}''',
        c("Continue", "cathedral", requires=(CATHEDRAL,)),
        c("Continue", "plain", forbids=(CATHEDRAL,))),
    d("cathedral", '''"I don't." {n}She sets the hammer down.{/n} "I said so at the council. I've never been pious. If you want to placate the people, you build a temple. The priests get their gold, the gods get their prayers, and the people forget they've been robbed." {n}She looks at the hammer.{/n}
"If prayin' for forgiveness doesn't work, maybe buyin' it will. I said that too. I've been thinkin' about it since."''',
      c("Continue", "hammer")),
    d("plain", '''"I don't." {n}She sets the hammer down.{/n} "Not like the paladins do. Torag willin', I say, like my mother did. Torag doesn't come when you call, and he doesn't forgive when you pay. He's the Father of the forge. He wants the work done right." {n}She looks at the hammer.{/n}
"We've done a lot of work this year, Commander. Not much of it right."''',
      c("Continue", "hammer")),
    d("hammer", '''"It was my mother's. She was a smith. She'd have wanted me to be one." {n}She turns it once more.{/n}
"I went for a soldier instead, and then a quartermaster, which is a smith for things that aren't iron. Boots, carts, lies to the ranks about when the grain's comin'." {n}She puts the hammer in the drawer.{/n} "Torag's god of the forge, and of protection, and of plannin' a war. Hard on his enemies. I've done more harm to Mendev's common folk this year than half the demons in the Wound. I'd not blame him for bein' hard on me."''',
      c('"Do you want forgiveness?"', "want"),
      c('[Trickster] "Gods can be bargained with. I\'ve done it."', "bargain")),
    d("want", '''"Want it?" {n}She thinks, the way she thinks about requisitions.{/n}
"No. I want the lads fed and the boots at the front and the war won. Forgiveness is somethin' you want when you've got time." {n}She looks up.{/n}
"After, maybe. If there's an after. I'll build him a little shrine in the stores and put the hammer on it. That'll be all the cathedral I need." {n}Her mouth twists.{/n} "Somebody'll steal the hammer. I'll know who."''',
      c("Continue", "end")),
    d("bargain", '''{n}She looks at you for a very long time with the one eye.{/n}
"I've no doubt you have." {n}Flatly.{/n} "And I've no doubt you came out ahead, and the god's still scratchin' his head over where it went." {n}She shakes her head.{/n}
"Not Torag. Not for me. He's a smith's god. You don't bargain with a smith, you pay what the work's worth." {n}A pause.{/n} "And don't you go makin' any deals on my account behind my back, Commander. I'll find out. It'll be in somebody's ledger."''',
      c("Continue", "end", flags=(L + "no_deals",))),
    d("end", '''{n}She shuts the drawer on the hammer and takes out the ledger instead.{/n}
"There. Back to work." {n}She opens it at your column, and looks at it for a while without writing anything.{/n}
"You know what my mother used to say about a good forging? You can tell it by the sound. A cracked one rings false. You've got the loudest column in this book, Commander, and it doesn't ring false." {n}She dips the pen.{/n} "I've not decided yet what it rings like. Go on. I'll think about it."''',
      c("[Leave her to think.]")),
], requires=("trickster.ever", RATIONS), forbids=(FAITH,), delay=48, chapters=(5,))


# --- 18. After the war (Chapter 5, after the first night): what she'll do when it's over. ------------------------------

office(AFTER, "After the war", '"It\'s cold in here."', [
    nar("start", '''{n}It is. The inner storeroom has no fire, by her own order, because fire and lamp oil and wool do not belong in the same room. She is sitting on a crate of salvaged cloaks in her coat, sorting them one-handed into good, mendable and rags, and she has put a second crate beside hers.{/n}
"Sit. Sort. Rags on the left." {n}Not looking up.{/n}''',
        c("[Sit. Sort.]", "sort")),
    nar("sort", '''{n}You sort. For a long time neither of you speaks. The cloaks came back from the front. Some of them came back without their owners. She checks every pocket before she sorts one, and puts what she finds in a tin box: a coin, a letter, a lock of hair, a wooden horse no bigger than a thumb.{/n}''',
        c('"What do you do with those?"', "tin")),
    d("tin", '''"Send 'em home, where there's a name. Where there isn't, I keep 'em." {n}She drops a brass button into the tin.{/n}
"I've a crate of these in the back. Twenty years of pockets." {n}She reaches for the next cloak.{/n} "Somebody's got to. The book says a cloak came back. The book doesn't say there was a horse in the pocket."''',
      c('"What will you do, after the war?"', "after")),
    d("after", '''{n}Her hands stop.{/n}
"After." {n}She says it as if checking whether the word is in stock.{/n}
"Nobody's asked me that since I was a girl." {n}She picks up the cloak again.{/n} "A shop. Boots, I thought, once. Boots that fit. You'd not believe how many men die in this war 'cause their boots don't fit. You'd come in, and I'd measure your feet, and you'd go out in boots that fit, and I'd never have to write you down in a book again."''',
      c('"You\'d miss the book."', "miss"),
      c('"I\'d come in every week to be measured."', "measured")),
    d("miss", '''"I'd miss the book." {n}She laughs, the short bark, quieter than usual in the cold.{/n} "I'd keep one anyway. For the boots. Who bought what, and what size, and did it fit." {n}She sorts a cloak into rags.{/n}
"And one line, carried forward. I'd keep that." {n}She does not look at you.{/n} "Wherever you were."''',
      c("Continue", "where")),
    d("measured", '''"Every week." {n}She snorts.{/n} "Your feet don't grow, Commander. You'd be wastin' my time." {n}She sorts a cloak into rags.{/n}
"...I'd measure 'em anyway." {n}She does not look at you.{/n} "You'd stand there in your socks and I'd take a very long time about it."''',
      c("Continue", "where")),
    d("where", '''"Where will you be? After." {n}She asks it lightly, the way she asks a carter where he last saw a missing sack.{/n}
"And don't say 'with you'. That's what folk say in songs, and then they go and get made a lord of somewhere, or a god, or dead." {n}Her good hand is very still on the cloak.{/n} "Tell me a true thing. I'll write it down later."''',
      c('"I don\'t know. Somewhere I can find a dwarf with a boot shop."', "boots"),
      c('"Wherever the Trickster\'s joke lands. You\'ll have to audit it."', "joke"),
      c('"With you. And I\'ll sign for it."', "sign")),
    d("boots", '''"Somewhere with a dwarf with a boot shop." {n}She considers it gravely.{/n} "There's a lot of dwarves with boot shops. You'd have to try every one." {n}She sorts a cloak into mendable.{/n}
"...I'll put a sign up. So you'll know which. 'Stranglehold's Boots. They Fit.'" {n}Her mouth twitches.{/n} "The jokesters'll love it."''',
      c("Continue", "end", flags=(L + "boot_shop",))),
    d("joke", '''"Wherever the joke lands." {n}She sighs, and it smokes in the cold.{/n} "That's the truest thing you've said all year and it's no use to me at all. I can't put a joke on a map."
{n}She sorts a cloak into mendable.{/n} "Fine. I'll audit it. Wherever it lands, I'll send a clerk to count it. It'll be the only joke in history with a stores ledger."''',
      c("Continue", "end", flags=(L + "joke_audited",))),
    d("sign", '''{n}She puts the cloak down.{/n}
"That's what folk say in songs." {n}But she says it without any heat at all.{/n} "You'd sign for it. You sign for everythin'." {n}She looks at you for a long time in the cold.{/n}
"All right. Sign for it. I'll hold you to it, and I've a grip, you'll recall." {n}She picks the cloak up again.{/n} "Don't make me write it off."''',
      c("Continue", "end", flags=(L + "signed_after",))),
    nar("end", '''{n}You sort the rest together. When the last cloak is on its pile she closes the tin box, with the horse and the hair and the letter in it, and sets it on the shelf with the others, and stands for a moment with her good hand on the lid.{/n}
{n}Then she puts out the lantern, and in the dark and the cold she leans her whole weight against your side, and stays there.{/n}''',
        c("[Stay.]")),
], requires=("trickster.ever", MORNING), forbids=(AFTER,), delay=24, chapters=(5,))


# Her epilogue remembers what the weekly counts made of the line.
EPILOGUE_PARAGRAPHS = {
    P + "epilogue.committed": (
        (TRUE_BOOKS, "{n}The ledgers she sent to Nerosyan during the war were the true ones, open line and all. The lords never forgave the Commander for it. The ranks never forgot it.{/n}"),
        (CLEAN_COPY, "{n}The copy she sent to Nerosyan during the war balanced to the copper, in the Commander's hand. It was the only lie she ever filed, and she kept the original, and never said where.{/n}"),
        (HER_NAME, "{n}After the war she went to Nerosyan as she had promised, to answer for a column with her name at the foot of it. The Commander went with her, and the court found that the stores had been used, quietly, by order, and could not decide whose.{/n}"),
        (RECEIPT, "{n}She kept a pencilled receipt folded small inside her coat for the rest of her life: Commander, returned. Received in good order. It was the only receipt in her whole career she was ever glad to close.{/n}"),
    ),
}


def integrate(payload):
    """Bind this module's own native reads, and give her committed epilogue page the weekly counts' consequences."""
    for key, guid in SELECTED_ANSWERS.items():
        payload.setdefault("SelectedAnswers", {})[key] = guid
    for key, cues in SEEN_CUES.items():
        payload.setdefault("SeenCues", {})[key] = list(cues)
    by_id = {s["Id"]: s for s in payload["Scenes"]}
    from story_format import p
    for sid, paras in EPILOGUE_PARAGRAPHS.items():
        page = by_id[sid]["Nodes"][0]
        page.setdefault("Paragraphs", []).extend(p(text, requires=(flag,)) for flag, text in paras)
