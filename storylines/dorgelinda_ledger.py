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
# Authored additions: courtship, supply counts, scar stories, wool, cup, bedroom,
# Old Harrow and postwar shop extend her logistics service; they do not rewrite native verdicts.
from story_format import c, p, scene
from storylines.dorgelinda_trickster import (ABYSS, BOOTS_PAID, CARTS, CLEAN, CLOSED, CONSCIENCE, HARD_MEASURES, COMMITTED, COUNTED, DECLINED, DIRTY, HANGED,
                                             HANGED_LANN, HANGED_WENDUAG, HUSHED, LATE, METHODS, P, PRESENT, PRISON, REDEEMED,
                                             RETURNED, REVIEW, TRIBUNAL, d, nar, office)

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
    "dorgelinda.inspectors_sent": ["8b55625df9de6cd4b8f04d0cfbb30c79"],
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
HELMETS = L + "three_hundred_helmets"
WARD = L + "the_plague_ward"
SURVIVORS = L + "half_an_army"
OTHERS = L + "other_columns"
UNBALANCED = L + "the_unbalanced_line"
MARCH = L + "quartermaster_of_the_march"
SERGEANT = L + "the_sergeants_version"
QUARREL_SCENE = L + "hammer_and_tongs"
SIZE = L + "the_right_size"
INSPECTOR = L + "the_inspector"
INSPECTORS = "dorgelinda.inspectors_sent"         # Logistics_4/Cue_0049: her treasury men sent for, to ride with the caravans
FREE_REIN = "dorgelinda.free_rein"                # Logistics_6/Cue_0050: free rein given to her connections
PLUNDER_REFUSED = "dorgelinda.plunder_refused"    # Logistics_6/Cue_0051: "your conscience can't fill an empty belly"
CATHEDRAL = "dorgelinda.cathedral"                # Logistics_8-1/Cue_0075: "maybe buyin' it will"
MERRY_CITY = "dorgelinda.merry_city"              # c5 Coronation/Cue_0009 (Trickster, no Fool King crowned)
KING_REVEL = "dorgelinda.king_revel"              # c5 Coronation/Cue_0018 (Trickster, King Thaberdine crowned)

WOOL = L + "cold_iron_and_wool"            # PP5 Chapter 4 beat: the crate opened at the first camp in the Abyss
WOOL_SHARED = L + "wool_shared"
WOOL_KEPT = L + "wool_kept"
WOOL_TRADED = L + "wool_traded"
FITTED = L + "fitted"                       # the_right_size: boots made to the cord
WOOL_CHOICES = (
    c("[Hand the wool round the camp, a pair to each, and keep the note.]", flags=(WOOL_SHARED,)),
    c("[Keep the lot. She tied the note to the top pair so that you would be the one to open it.]", flags=(WOOL_KEPT,)),
    c("[Trade it. A dozen pair of dry socks is worth a great deal in a camp in the Abyss.]", flags=(WOOL_TRADED,),
      alignment=("Chaotic", 1)),
)
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
NARROWED = L + "narrowed"
QUARREL_COLD = L + "quarrel_cold"
COLD_COUNTS = L + "cold_counts"


# --- 1. The bad hand. -------------------------------------------------------------------------------------------------

office(HAND, "The bad hand", '"You\'re writin\' with one hand again."', [
    nar("door", '''{n}Dorgelinda is copying a requisition for lamp oil, cold-weather cloaks and forty pairs of boots, none of which Nerosyan will send. She writes with her good hand. The other lies on the page to hold it flat, the fingers curled and grey, and the page does not move.{/n}''',
        c("Continue", "asked_before", requires=(HAND_OFFERED,)),
        c("Continue", "never_asked", forbids=(HAND_OFFERED,))),
    d("asked_before", '''"You asked me once if I wanted it mended. I told you to spend the spell on some poor sap whose legs got ripped off in the first battle."
{n}She blots the requisition and does not look up.{/n}
"I meant it. There's always some sergeant in the infirmary needs a spell more than I do. You'd like to know the rest of it. Everybody does. Most of 'em don't pay for it in boots."''',
      c('"How did it happen?"', "story"),
      c('"I didn\'t come to ask."', "liar")),
    d("never_asked", '''"You keep lookin' at it. Everyone does, the first dozen times. Clerks, colonels, a Hellknight or two who think nobody sees 'em count my fingers."
{n}She blots the requisition and does not look up.{/n}
"Go on, then. You're payin' in boots this week. I'll give you a story for 'em."''',
      c('"How did it happen?"', "story"),
      c('"I didn\'t come to ask."', "liar")),
    d("liar", '''"Liar." {n}She blots the requisition.{/n} "You've been watchin' that hand since you sat down. Go on, then."''',
      c("Continue", "story")),
    d("story", '''"There's three versions, dependin' on who's buyin'. For a colonel, I held a breach alone at Kenabres against a horde. For a recruit, it was a demon the size of a barn." {n}She finally looks up.{/n}
"For you, the true one. Somethin' with claws came over a barricade I was holdin', in the dark, and I put a spear in it, and it put its hand across my face and the other across my arm on the way down. The report says demon. The report was written by a man who wasn't there. I didn't see much of it. It took the eye first."''',
      c('"And the hand?"', "hand")),
    d("hand", '''"Hand went numb on the march back. Stayed numb. The healers poked it for a month." {n}She lifts the withered fingers with her good hand, then lowers them onto the page.{/n} "Our jokesters started callin' me Stranglehold. So I left the front for supply, and showed 'em what one hand could keep hold of."''',
      c('"And did they learn?"', "learned"),
      c('[Reach across the desk and take the bad hand in yours.]', "touch")),
    d("learned", '''"All of 'em. The thievin' quartermasters, the officers who lose half a caravan every skirmish, the civilian milksops with a sob story for every sack." {n}Something that is almost pride comes into her voice.{/n}
"Two of those jokesters are dead now, on the walls, and I buried 'em in good boots. The third's a sergeant in my stores. He calls me ma'am and counts twice." {n}She sniffs.{/n} "The one still in my stores counts twice. He can laugh after the carts are in."''',
      c("Continue", "ask_back")),
    d("touch", '''{n}She does not pull away. Nor does she help. The hand is cool and very light, the skin tight over the bones, like holding a glove somebody else has taken off.{/n}
"It won't feel a thing, Commander. That's the point of tellin' you." {n}Her good hand keeps the page flat on its own. She watches your thumb move over the knuckles and her jaw works, once.{/n}
"...It's been a while since anybody picked it up on purpose. Most folk hand it back to me like it's somethin' I dropped."''',
      c("[Keep holding it a moment longer.]", "ask_back", flags=(L + "held_hand",)),
      c("[Set it back on the page, gently.]", "ask_back")),
    d("ask_back", '''"Your turn." {n}She sets down the pen.{/n} "I've told you about the wound. What'd this war leave on you, Commander?"''',
      c("[Show her a scar you don't talk about.]", "scar"),
      c('"The Trickster took something. I\'m still counting what."', "counting"),
      c('[Flirt] "Nothing you can see. You\'ll have to look harder."', "flirt")),
    d("scar", '''{n}She studies the scar.{/n} "That's a bad one. Somebody meant it." {n}She makes a note beside the next armour issue.{/n} "Padding there, if you're wearin' plate. I'll tell the armourer."''',
      c('"You write everything down."', "close", flags=(HAND_TOLD,))),
    d("counting", '''"Still countin'. Aye." {n}She leaves the pen beside the requisition.{/n} "I've had days like that. Boots due back next week, though." {n}She writes the date of the next visit.{/n} "I'll expect you with 'em."''',
      c('"You write everything down."', "close", flags=(HAND_TOLD,))),
    d("flirt", '''{n}She looks at you with the one eye, from the top of your head to the edge of the desk, as thoroughly as she would a new consignment of cavalry saddles.{/n}
"Harder than that?" {n}A pause.{/n} "Hammer and tongs, Commander. You've got the nerve of a Fellow with a full cart." {n}She writes a line in your column, very small, and turns the book so you cannot read it.{/n}
"There. Now you're on the books properly. Don't ask what I wrote."''',
      c('"Is that how you court, Quartermaster? By inventory?"', "close", flags=(HAND_TOLD,))),
    d("close", '''{n}She snorts, and caps the ink.{/n}
"I'm auditin' you. If you've mistook it for somethin' else, that's your affair. Same time next week. Bring the boots back if you've still got 'em. There's a lad on the south wall with his toes out."''',
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
"New draft," {n}Dorgelinda says, without looking up from the manifest.{/n} "Asked the lads in the stores why they call me Stranglehold. Thought it was a joke about my temper." {n}She turns a page.{/n} "It's partly a joke about my temper."''',
      c('"Is that a standing wager?"', "wager")),
    d("wager", '''"Every new draft since Kenabres. Pay a copper, take the pen out from under my hand, win a silver. I've not paid a silver yet." {n}Now she looks up. The clerks have gone very quiet.{/n}
"Trickster's rules for you, Commander, since you're a Trickster. Any way you like. You can pull it, pinch it, sing it out. If it comes out, I'll put your silver against your boots. If it doesn't..." {n}She taps the pen with one finger.{/n} "You buy the stores a round."''',
      *GRIP_CHOICES),
    d("lifted", '''{n}You do not pull. You lean in to read the manifest upside down, and ask her about a line on it, a shipment of salted fish logged twice. She frowns and looks, and her hand shifts a hair's breadth to point, and the pen is in your sleeve before her finger lands.{/n}
{n}The sergeant makes a noise like a kettle.{/n}
"...Well." {n}She lifts her hand and looks at the bare wood under it.{/n} "Used, quietly. Of course it was." {n}She takes a silver from her own purse and slaps it down.{/n} "The fish is logged twice, by the way. You weren't lyin' about that part. That's what makes it work."''',
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
    d("after", '''{n}The clerks leave. She pours two drinks and pushes one toward you.{/n} "They laughed when the hand went numb. Now they ask before they borrow a nail." {n}She drinks.{/n} "What've you come to take, Commander?"''',
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
    d("hanged", '''"The men who stacked this are in the ground." {n}She sets the lantern on a barrel.{/n} "I saw it done myself. Somebody had to, and I wasn't goin' to let 'em die among strangers. They fought on the walls, the lot of them. They never ran."
{n}She hangs the tally board on a nail.{/n} "The stores don't care. Let's count."''',
      c("Continue", "count")),
    d("prison", '''"The men who stacked this are on the Nerosyan road in chains, cursin' my name the whole way, I expect. Good. Better than cursin' nothin' from a tree."
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
    d("arith", '''"Those potions were reserved for officers. Lose the officers and a company gets itself butchered." {n}She sets the empty vial back in its straw.{/n} "Leave twelve men rottin' while you've got medicine under lock, and their mates learn not to trust you. I backed the order. I still have to feed those mates. Go on. Give me somewhere to enter the vials."''',
      c("Continue", "book")),
    d("book", '''"The book wants twenty-four vials entered somewhere. Either they're stolen, and they go under Bartley's name for the record in Nerosyan, or they're issued, and they go under yours."
{n}She holds out the pen.{/n} "You ate a warehouse. You tell me if you ate these."''',
      *POTION_CHOICES),
    d("ours", '''{n}She watches you enter twenty-four healing vials under your own name. Beneath the issue, you mark the twelve survivors.{/n}
"You'll have the general staff askin' where their potions went." {n}She takes the pen back.{/n} "And I'll tell 'em. The Commander drank 'em. All twenty-four. Very thirsty, the Commander." {n}Her mouth twitches.{/n} "They'll believe it of you. That's the terrible thing."''',
      c("Continue", "home", flags=(POTIONS_OURS,))),
    d("bartley", '''{n}She writes the stolen vials under Bartley's name and blots the entry.{/n} "Theft. That's how it'll read in Nerosyan. I'll put the twelve survivors in the report too. Doesn't wipe out what he did to my quartermaster."''',
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
    d("stuck", '''"Then those helmets sit in Ustalav till some clerk sells 'em, and our lads climb the walls bareheaded." {n}She sets blank paper beside the letters.{/n} "You've got your seal. I've got a fence who owes me. Between us, we ought to get past one bloody customs yard."''',
      c('[Forge a Mendevian treasury release, seal and all.]', "forge", requires=('trickster.now',)),
      c('"I\'ll write to Ustalav as the Commander. Under my own seal, with a threat in it."', "honest"),
      c('"Send your fence. I\'d like to see what a man who owes Dorgelinda Stranglehold can do."', "fence")),
    d("forge", '''{n}She watches you do it: the treasury clerk's cramped hand, the flourish on the Chancellor's initial, the right grey wax, which she produces from a drawer without comment. When you hold it up to the lamp it would fool you. It very nearly fools her.{/n}
"The Chancellor dots his i's with a tick, not a dot." {n}She points.{/n} "Did him wrong. Customs won't know. I know." {n}She blows on the ink.{/n}
"If this comes back on us, it's my stores it comes back to, and your hand on the paper. You're gettin' very comfortable in my book, Commander."''',
      c("[Seal it.]", "sent", flags=(FORGED,), alignment=("Chaotic", 1))),
    d("honest", '''"A threat." {n}She considers it.{/n} "From the Commander of the Fifth Crusade to a customs clerk in Ustalav. That's a sledgehammer on a thumbtack." {n}She pushes paper across.{/n}
"Go on, then. Make it a good one. Mention the Worldwound, they don't like to think about the Worldwound down there." {n}She reads it when you finish, twice, and nods.{/n} "That'll frighten somebody. Maybe even the right somebody."''',
      c("[Seal it.]", "sent", flags=(HONEST_DEMAND,))),
    d("fence", '''{n}She laughs, a short bark that makes the clerk outside the door drop something.{/n}
"You'd like to see it." {n}She adds a line to the fence's letter in a hand even smaller than her own, and folds it twice more.{/n}
"All right. You'll see it. It'll cost me a debt I've been savin' ten years, but you'll see it, and when three hundred helmets come up the Nerosyan road with Ustalavic customs seals on 'em that nobody ever stamped..." {n}She seals it.{/n} "...you'll not ask how. That's the rule with him."''',
      c("[Agree to the rule.]", "sent", flags=(FENCE_CALLED,))),
    d("sent", '''{n}She stacks the sealed letters for the courier. The western bell rings the change of watch.{/n} "One to the treasury, one to customs, one to a fence. Three hundred helmets still sittin' in a yard while I wait for answers." {n}She rubs her eye.{/n} "The Queen's retinue can get wine for a banquet without all this. I've seen the bills. Call me a freethinkin' rebel if you like."''',
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
    d("first", '''{n}She looks up when you come in and does not say anything. She looks you over as if checking a delivery against its manifest, and finding it, against all odds, complete.{/n}
"You came back." {n}As if that settles an argument she has been having with someone.{/n}
"I had a clerk come to me the week you went down into the Abyss. Young lad, very neat hand. Asked should he rule off the Commander's column. 'Lost with the Commander', he wanted to write." {n}She sniffs.{/n} "I sent him to count horseshoes for a fortnight."''',
      c("Continue", "column")),
    d("column", '''"I don't write off a line 'cause the owner's gone to the Abyss. I'd have to write off half the Crusade." {n}She turns the ledger to your page. Your column has grown while you were gone: small entries, weekly, in her hand. You read the dates. One for every week you were away.{/n}
"Carried forward." {n}Every one of them says it.{/n} "Now. You went down there with whatever your party could carry and a pack of heroes. What came back? I want receipts."''',
      c('[Empty your pack onto her desk.]', "pack"),
      c('"I thought about your ledger down there."', "thought"),
      c('"Did you miss me?"', "miss"),
      # PP5: the wool from the arrowhead crate (Chapter 4, WOOL) comes back to her desk, as this Commander spent it.
      c('"The wool in the arrowhead crate. I handed it round the camp."', "wool_shared", requires=(WOOL_SHARED,)),
      c('"The wool in the arrowhead crate. I wore it. All twelve pair, in turn."', "wool_kept", requires=(WOOL_KEPT,)),
      c('"The wool in the arrowhead crate. I traded it."', "wool_traded", requires=(WOOL_TRADED,))),
    d("wool_shared", '''"Handed 'em round." {n}She nods, once, the way she nods at a manifest that adds up.{/n}
"Good. That's what they were for. I'd have sent twenty if I'd thought you'd do the sensible thing with 'em." {n}She writes something short.{/n} "How many pair came back?"
{n}You tell her. It is not many. She does not seem to have expected many.{/n}
"Then the rest wore through on feet that walked out again. That I can write off." {n}She looks at your boots, then at you.{/n} "Your own feet. Dry?"''',
      c('"Mostly."', "close", flags=(WELCOMED,))),
    d("wool_kept", '''"Twelve pair. On one pair of feet." {n}She sniffs.{/n}
"I sent 'em for the lot of you. I'll not pretend I didn't tie the note on top so it'd be you that opened it." {n}Her mouth twitches.{/n} "Well. Issued to the Commander's party, worn by the Commander. Can't fault the paperwork."
{n}She glances down at your boots.{/n} "Feet dry?"''',
      c('"Mostly."', "close", flags=(WELCOMED,))),
    d("wool_traded", '''"You traded my socks." {n}She puts the pen down.{/n} "In the Abyss. To what?"
{n}You tell her what a dozen pair of dry wool socks fetched in a camp in the Abyss, and from whom, and what it bought.{/n}
{n}She listens with her jaw set, outraged on behalf of the wool. Then, against her will, the corner of her mouth goes.{/n}
"That's a better rate than Nerosyan gives me." {n}She picks the pen back up.{/n} "Don't you dare tell my clerks. And next time I pack you socks, you wear the bloody socks."''',
      c('"Next time."', "close", flags=(WELCOMED,))),
    d("pack", '''{n}You empty it: a demon's coin that is warm to the touch, a stub of candle from somewhere with no sun, a broken buckle, two cold-iron arrowheads, blunted, a scrap of silk that smells of something you do not want to name.{/n}
{n}She sorts it with her good hand into two piles without being told which is which. The coin she does not touch. The arrowheads she picks up, turns in the lamplight, and sets upright, side by side, like soldiers.{/n}
"Two. I'll count those." {n}She writes it.{/n} "That's a better rate of return than Nerosyan."''',
      c("Continue", "close", flags=(WELCOMED,))),
    d("thought", '''"Did you." {n}She does not look up. The pen has stopped.{/n}
"What'd you think? That I'd be sittin' here with my column open like a fool?" {n}Her good hand is flat on the page.{/n}
"...Well, you weren't wrong." {n}She writes something. You do not ask what.{/n} "I kept thinkin' of you down there, signin' some demon's manifest with a straight face. If anyone could make the Abyss balance, it'd be you, and then I'd have to find a way to audit it."''',
      c("Continue", "close", flags=(WELCOMED,))),
    d("miss", '''"Miss you?" {n}She leans back in her chair.{/n}
"I missed bein' shouted at about boots. I missed somebody comin' through that door who didn't want somethin' off me." {n}She picks up the pen, and puts it down.{/n} "...Aye. I missed you. The clerks noticed. They think I've gone soft." {n}She picks the pen up again.{/n} "Don't tell the Council."''',
      c("Continue", "close", flags=(WELCOMED,))),
    d("close", '''"Right." {n}She closes the issue book and comes round the desk.{/n} "Your party's back. I'll match what you brought against what we sent. The council's latest supply returns are in the other book." {n}Her hand catches your collar.{/n} "I missed you, Commander. Not just your damned receipts."''',
      c("[Let her straighten your coat.]", "collar")),
    nar("collar", '''{n}She straightens your coat with her good hand, the way a quartermaster straightens a recruit's kit before an inspection, and her fingers stay a moment at your throat. Then she goes back round the desk and sits down and picks up the pen, and whatever it was is back in its column.{/n}''',
        c("[Leave her to it.]")),
], requires=("trickster.ever", COUNTED), forbids=(RECEIPTS, ABYSS, REVIEW), chapters=(5,))


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
"Rations are short. I told the council we'd have to cut somewhere, and who tightens their belt is for you to decide." {n}She does not look at the boy.{/n}
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
"...An order." {n}She gives you the one eye, unblinking. Then she takes a bowl from the stack, fills it at the pot, sits down, and eats every mouthful while holding your gaze, and sets the spoon down with a click.{/n}
"Ration consumed, Commander. Enter it where you like." {n}The table starts eating again.{/n} "I'll eat, Commander. Don't expect me to thank you for makin' a show of it."''',
      c("Continue", "after", flags=(ORDERED,))),
    d("sit", '''{n}You sit. You eat. She watches you eat, and says nothing either, and after a while she reaches over with her spoon and takes one mouthful from your bowl, as if tasting for poison, and then another.{/n}
"The turnip's off," {n}she says.{/n} "I'll have words with the cook." {n}She does not take a third. She does not need to.{/n}''',
      c("Continue", "after", flags=(SHARED,))),
    d("after", '''{n}Back in her office, Dorgelinda puts the empty ration bowl on the desk.{/n}''',
      c('"Is that why you ate last?"', "last", forbids=('dorgelinda.ledger.ordered_to_eat',)),
      c("Continue", "after_ordered", requires=(ORDERED,))),
    d("last", '''"Aye. I wasn't puttin' my supper ahead of his. The lad's eaten now. So have we." {n}She sets the bowl aside and opens the requisition book.{/n} "I've letters to write to people who've never missed a meal. If the cooks hear you liked that turnip, we'll never see the last of it. Keep your mouth shut about that much, at least."''',
      c("[Leave her to the letters.]")),

    d("after_ordered", '"You embarrassed me in front of the lads." {n}She pushes the bowl aside.{/n} "I know you meant to get food into me. Next time, sit down and eat. I can take a hint without you bellowin\' an order across the mess."',
      c("[Leave her to the letters.]")),
], requires=("trickster.ever", COUNTED, PRESENT), forbids=(RATIONS, "dorgelinda.conscience_kept"), delay=48, chapters=(5,))


# --- 7. After hours (the intimate beat, after the commit). -------------------------------------------------------------

office(NIGHT, "After hours", '"The clerks have gone home."', [
    nar("start", '''{n}The last carter has gone. Dorgelinda shuts the ledger and pushes it to the far end of the desk. Her eye follows you to the door.{/n} "Bolt it."''',
        c("[Bolt it.]", "bolted")),
    d("bolted", '''{n}She comes round the desk and takes your collar in her good hand. Her other wrist braces against the wood. She kisses you, then swears at the fastening of her belt.{/n} "Bloody buckle. Give me a hand with it. I've had enough of waitin'."''',
      c("[Take off your coat. Let her count.]", "coat"),
      c("[Reach for the strap of her eye patch.]", "patch"),
      c('"Well? Are you going to count, or just look?"', "count")),
    d("patch", '''{n}Her good hand closes on your wrist before your fingers reach the strap. Stranglehold. It does not hurt. It will not move either.{/n}
"Patch stays." {n}Very quietly.{/n} "What's under it isn't yours. It isn't anybody's. It went to a thing with claws, and the thing can keep it." {n}She brings your hand down, and does not let go of it, and puts it instead on the buckle of her own belt.{/n}
"That, you can have."''',
      c("Continue", "count")),
    d("coat", '''{n}You take off your coat and let it fall across her desk, on top of the ledger. She does not look at the ledger once.{/n}
{n}She lays her good hand flat on your chest, over the shirt, and leaves it there, feeling your heart go.{/n}
"Oh," {n}she says, quite quietly, as if somebody had told her a figure she did not expect.{/n} "That's fast. Is that me?"''',
      c("Continue", "count")),
    d("count", '''{n}She swears at a stuck button, works it free and pulls your shirt open. Her palm moves over your chest; at a scar, it slows. Her breath catches when you unfasten her belt.{/n}
{n}Her shirt slips from one shoulder, baring the pale furrows along her arm. You brush your lips over the unscarred shoulder. She turns into you and catches your mouth with hers.{/n}''',
      c("[Tell her she's beautiful.]", "tell"),
      c('[Say nothing. Show her.]', "show")),
    d("tell", '''"Beautiful." {n}She snorts, and it catches halfway, and she puts her forehead against your shoulder so that you cannot see her face.{/n}
"You lyin' Trickster." {n}Her voice is thick.{/n} "You'd sign for anythin'. Say it again."''',
      c("Continue", "threshold")),
    d("show", '''{n}You kiss her. She grips the back of your neck and pulls you closer, until your hip presses against the desk and her breath is hot against your mouth.{/n} "About bloody time."''',
      c("Continue", "threshold")),
    nar("threshold", '''{n}Her elbow sends the ledger to the floor. She leaves it there. You kick off a boot; it slides beneath the desk. She pulls you through the inner door, laughing against your mouth. At the bed you work her boots loose, then your remaining one. Her hand catches yours at her waist.{/n}
"I want you. Here. Before some bastard comes askin' for horseshoes."
{n}She draws you onto the rough wool. Her bare shoulder is warm beneath your lips; her good hand presses you close, and the last of your clothes falls beside the bed.{/n}''',
        c("[The lamp gutters out.]", "dorgelinda.ledger.after_hours.explicit.1")),
    # Explicit slot: chosen first night, her initiative, patch stays; no explicit prose here.
    nar("dorgelinda.ledger.after_hours.explicit.1", '''{n}She catches your mouth again and pulls you down beside her. The rough wool bunches beneath her good hand. The last cart rattles away outside.{/n}''',
        c("[Stay with her.]", flags=(NIGHT_KEPT,))),
], requires=("trickster.ever", COMMITTED), forbids=(NIGHT,), delay=12, chapters=(5,))


# --- 8. The morning count. ----------------------------------------------------------------------------------------------

office(MORNING, "The morning count", '"Mornin\'."', [
    nar("start", '''{n}You wake with her good arm across you. A wagon rattles beyond the shutters. She pulls you close for a kiss, then reaches for the ledger beside the cot. The pen stops above the dawn entry.{/n}''',
        c('"What\'s wrong?"', "book"),
        c("[Pull her back down.]", "back")),
    d("back", '''{n}She lets you pull her down and kisses you again. Then she pushes herself upright, warm and rumpled, with her hand on your chest.{/n} "Wagons, Commander. I'll have to get dressed. And you'll have to sit a campaign saddle today." {n}She looks at you with considerable satisfaction.{/n} "That hard one. Mind how you mount."''',
      c('"What\'s wrong?"', "book")),
    d("book", '''"I missed the dawn count." {n}She says it the way another woman might say she had lost a tooth.{/n}
"Eleven years. I've not missed a dawn count in eleven years. Not for wounds, not for fever, not the week after Kenabres." {n}She shuts the ledger.{/n} "The sergeant ran it. He'll have run it wrong. There'll be lamp oil in with the flour and cloaks in with the blankets by noon."
{n}She looks at you, and something in her face gives, and she laughs, short and helpless, into her hand.{/n} "Worth it. Don't you dare tell him I said so."''',
      c("Continue", "sergeant")),
    d("sergeant", '''{n}Somebody knocks. She does not move.{/n}
"Ma'am?" {n}The sergeant with the bandaged ear, through the door.{/n} "Ma'am, the Commander's boots are in the office. One of 'em. Under the desk. Should I send 'em up to the citadel?"
{n}Dorgelinda closes her eye and counts to five under her breath.{/n}
"No, Sergeant," {n}she calls.{/n} "Log 'em as returned stores. Commander's boots, one pair, to be counted at the Commander's convenience."
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
    c('"Send the true books. Every issue, every signature. All of it."', "true_books",
      crusade=("Favors", -100)),
    c('[Write them a ledger that balances, in your own hand.]', "clean_copy", crusade=("Finances", -100),
      alignment=("Chaotic", 1)),
    c('"Put your name on it, then. It\'s your stores."', "her_name"),
)

office(INQUIRY, "The inquiry", '"You look like you\'ve had a letter."', [
    d("start", '''"Nerosyan wants the ledgers. All of 'em." {n}She drops a treasury letter onto the desk.{/n} "Some lord's heard about our irregular issues. He wants dates, signatures and names. Yours is on the first page. Mine's on the rest. He'll have plenty to read."''',
      c("Continue", "dirty", requires=(DIRTY,)),
      c("Continue", "clean", requires=(CLEAN,), forbids=(DIRTY,)),
      c("Continue", "plain", forbids=(CLEAN, DIRTY))),
    d("dirty", '''"And they'll see the other book, if they look in the right drawer. My methods, my hand. Weight discrepancies here, carts written off in transit there." {n}She puts her good hand on the thin ledger, the one she showed you beside the signed returns.{/n}
"I kept it better than they ever did. That won't save either of us if the wrong clerk opens it."''',
      c("Continue", "offer")),
    d("clean", '''"No second book. I burned it." {n}She taps the letter.{/n} "But there's still your signature under those issues. A lord who wants a scandal won't stop because the sums add up."''',
      c("Continue", "offer")),
    d("plain", '''"The sums aren't what he's after. He wants somebody to blame."''',
      c("Continue", "offer")),
    d("offer", '''{n}She draws the letter back across the desk.{/n} "I can answer for it. Quartermaster's error, quartermaster's thievin'. They'll like either. You stay here and keep the demons off the walls. I'll go to Nerosyan after the war."''',
      c("Continue", "asked_before", requires=(COURT_MARTIAL,)),
      c("Continue", "choice", forbids=(COURT_MARTIAL,))),
    d("asked_before", '''"I said it at the council: court-martial me after the war. I meant it then. I mean it more now." {n}Her good hand is flat on the letter.{/n} "It's a good trade, Commander. One quartermaster for one Commander. Nerosyan'd take it in a heartbeat."''',
      c("Continue", "choice")),
    d("choice", '''"So. What goes to Nerosyan?"''', *INQUIRY_CHOICES),
    d("true_books", '''{n}She stacks every ledger, ties the bundle and leaves every page in place.{/n} "All of it, then. I'll send copies of the receipts with it. Nerosyan'll curse us. Let 'em do it with the figures in front of 'em."''',
      c("Continue", "after", flags=(TRUE_BOOKS,))),
    d("clean_copy", '''{n}You spend the night copying the returns without the disputed issues. Dorgelinda checks each page. At dawn she sets the clean copy beside the original.{/n} "This will get this inquiry off our backs, if nobody asks for the receipts. It doesn't make the issue true." {n}She locks the original away.{/n} "The courier and copyist want pay for their silence. I'll keep the proof of what we sent."''',
      c("Continue", "after", flags=(CLEAN_COPY,))),
    d("her_name", '''{n}She writes her name beneath the list of disputed issues: D. Stranglehold, Quartermaster.{/n} "There. My responsibility." {n}She blots it without looking up.{/n} "I'll answer for it when the war's done. Not while there's a cart in this yard waitin' to be counted."''',
      c("Continue", "after", flags=(HER_NAME,))),
    nar("after", '''{n}The courier leaves at noon. In the yard, clerks match loaded wagons against the current supply returns. Dorgelinda checks the issue receipts before letting each cart through the gate. The disputed signatures travel to Nerosyan; the supplies travel to the front.{/n}''',
        c("[Wait for her.]")),
], requires=("trickster.ever", MORNING, METHODS), forbids=(INQUIRY,), delay=48, chapters=(5,))


# --- 10. Carried forward: before the last march. -----------------------------------------------------------------------

LAST = (
    c("[Sign the receipt now, in advance: \"Commander, returned. Received in good order.\"]", "receipt"),
    c("[Kiss her, in front of the wagons, and never mind the clerks.]", "kiss"),
    c("[Salute her. Properly. The way the ranks salute her.]", "salute"),
)

office(FORWARD, "Carried forward", '"You\'re ridin\' with the wagons?"', [
    nar("start", '''{n}In the stores yard she checks a wagon packed for the future march on the Wound. Beside it lies the party's kit, labelled and ready. Her ledger is open on a bench; the carters wait for their loading orders.{/n}''',
        c("Continue", "going")),
    d("going", '''"Packin' ahead. You'll want arrows when the order comes, and I'll not leave it to the last bloody hour." {n}She tests a lashing.{/n} "I'll count this again before it leaves. Till then, you know where my desk is."''',
      c('"I wasn\'t going to argue."', "wasnt"),
      c('"Stay. I need someone left to count what comes back."', "stay")),
    d("stay", '''"Aye. Someone has to count what comes back." {n}She checks the kit against her ledger.{/n} "I'm still here, Commander. This wagon isn't goin' anywhere till we get the march order."''',
      c("Continue", "boots")),
    d("wasnt", '''"Good. Hold that rope while I check the knot. Then I've a receipt for you."''',
      c("Continue", "boots")),
    d("boots", '''{n}She takes a folded paper and pencil from her pack.{/n} "Receipt for your party's kit. Sign when you bring it back. And bring yourself back with it. I don't want a clerk returnin' your boots without you."''',
      c("Continue", "paid", requires=(BOOTS_PAID,)),
      c("Continue", "choose", forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed', 'dorgelinda.trickster.cost.boots_paid'), requires=()),
      c("Continue", 'choose', requires=('dorgelinda.ledger.quarrel_mended',), forbids=('dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed', 'dorgelinda.trickster.cost.boots_paid')),
      c("Continue", 'choose_cold', requires=('dorgelinda.ledger.quarrel_unmended',), forbids=('dorgelinda.trickster.cost.boots_paid',)),
      c("Continue", 'choose_cold', requires=('dorgelinda.ledger.quarrel_cold',), forbids=('dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.trickster.cost.boots_paid')),
      c("Continue", 'choose_reserved', requires=('dorgelinda.ledger.narrowed',), forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.trickster.cost.boots_paid')),
      c("Continue", 'choose_reserved', requires=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.quarrel_unmended', 'dorgelinda.trickster.cost.boots_paid')),
      c("Continue", 'choose_private', requires=('dorgelinda.ledger.unblessed',), forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.trickster.cost.boots_paid')),
      c("Continue", 'choose_private', requires=('dorgelinda.ledger.unblessed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.trickster.cost.boots_paid'))),
    d("paid", '''"The boots stay here." {n}She nods at the stores door.{/n} "The last pair, the ones you paid your debt in. Top shelf, unworn. I'm not issuin' 'em to anyone else, and they're not goin' on this wagon to get demon on 'em." {n}Something moves in her face.{/n} "You come back and you can have 'em. Not before."''',
      c("Continue", "choose", forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed'), requires=()),
      c("Continue", 'choose', requires=('dorgelinda.ledger.quarrel_mended',), forbids=('dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed')),
      c("Continue", 'choose_cold', requires=('dorgelinda.ledger.quarrel_unmended',), forbids=()),
      c("Continue", 'choose_cold', requires=('dorgelinda.ledger.quarrel_cold',), forbids=('dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended')),
      c("Continue", 'choose_reserved', requires=('dorgelinda.ledger.narrowed',), forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended')),
      c("Continue", 'choose_reserved', requires=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.quarrel_unmended',)),
      c("Continue", 'choose_private', requires=('dorgelinda.ledger.unblessed',), forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended')),
      c("Continue", 'choose_private', requires=('dorgelinda.ledger.unblessed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_unmended'))),
    d("choose", '''{n}Around you the carters finish loading. A horn sounds the change of watch. The Wound's light is on every face in the yard.{/n}''', *LAST),
    d("receipt", '''{n}You write “Commander, returned” in pencil beside the issued kit. She reads it, folds the paper and puts it inside her coat.{/n} "Not yet, you aren't. You'd better make it true."''',
      c("Continue", "end", flags=(RECEIPT,))),
    d("kiss", '''{n}Every clerk in the yard sees it. So do two sergeants, a column of Mendevian levies, a paladin on a warhorse and the carter of the wagon behind, who drops his reins.{/n}
{n}She lets it happen. Then she kisses you back, hard, with her good hand flat against your breastbone, pushing as much as holding, and lets go all at once.{/n}
"Well, that's in the book now," {n}she says, rather hoarsely.{/n} "And theirs." {n}She takes her ledger from the bench.{/n} "Come back and sign the receipt, Commander. I'll not ask twice."''',
      c("Continue", "end")),
    d("salute", '''{n}You salute her, properly, heel to heel, the way the ranks salute her and nobody above the rank of sergeant ever has.{/n}
{n}She stares. Then she returns it, with the bad hand, as she always does, slowly, so that you can see the withered fingers held to her brow by nothing but the arm beneath them.{/n}
"Commander." {n}Her voice does not waver.{/n} "Come back and sign the receipt." {n}She takes her ledger from the bench.{/n}''',
      c("Continue", "end")),
    nar("end", '''{n}Dorgelinda orders the wagon backed beneath the stores awning. She takes her ledger inside and calls the next carter to her desk. Your kit stays packed for the march.{/n}''',
        c("[Leave her to the preparations.]")),

    d('choose_cold', "{n}Around you the carters finish loading. A horn sounds the change of watch. The Wound's light is on every face in the yard.{/n}",
      c("[Sign the receipt now, in advance: \"Commander, returned. Received in good order.\"]", "receipt"),
      c("[Kiss her, in front of the wagons, and never mind the clerks.]", 'kiss_cold'),
      c("[Salute her. Properly. The way the ranks salute her.]", "salute")),
    d('choose_reserved', "{n}Around you the carters finish loading. A horn sounds the change of watch. The Wound's light is on every face in the yard.{/n}",
      c("[Sign the receipt now, in advance: \"Commander, returned. Received in good order.\"]", "receipt"),
      c("[Kiss her, in front of the wagons, and never mind the clerks.]", 'kiss_reserved'),
      c("[Salute her. Properly. The way the ranks salute her.]", "salute")),
    d('choose_private', "{n}Around you the carters finish loading. A horn sounds the change of watch. The Wound's light is on every face in the yard.{/n}",
      c("[Sign the receipt now, in advance: \"Commander, returned. Received in good order.\"]", "receipt"),
      c("[Kiss her, in front of the wagons, and never mind the clerks.]", 'kiss_reserved_private'),
      c("[Salute her. Properly. The way the ranks salute her.]", "salute")),
    d('kiss_cold', '{n}She steps back and catches your wrist before you can kiss her. The clerks look down at their manifests.{/n} "Not here. Not after what you said." {n}She releases you and takes up her ledger.{/n} "Bring the kit back, Commander. The receipt\'s still yours."',
      c("Continue", "end")),
    d('kiss_reserved', '{n}She turns her cheek and gives your hand a brief squeeze, then lets go.{/n} "My rooms, on the nights I say. We settled that. The yard\'s for wagons." {n}She turns back to the kit.{/n} "Come back with your kit."',
      c("Continue", "end")),
    d('kiss_reserved_private', '{n}She turns her cheek and lets your hand go.{/n} "Not in front of my clerks. You\'ve your business. This is mine." {n}She turns back to the kit.{/n} "Come back with your kit."',
      c("Continue", "end")),
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
"That's the first true thing he's said since the caravans," {n}she says.{/n} "I wanted you to hear it. I wanted him to see who he owes his neck to."''',
      c("Continue", "owes")),
    d("sweat", '''{n}He sweats. It does not take long. Carters have no gift for silence.{/n}
"It weren't a vrock, Commander. Fellows paid me four silver to turn off the road at the ford. I've a wife in Vigil and three little 'uns and the Crusade pays me in promises."
{n}Dorgelinda writes something without looking up.{/n}
"Well done. Quieter than a thumbscrew." {n}She blots it.{/n} "I wanted you to hear it from him. I wanted him to see who he owes his neck to."''',
      c("Continue", "owes")),
    d("owes", '''{n}She puts the pen down and finally looks at the carter.{/n}
"You owe your neck to a line in my book. The Commander wrote it before anybody knew what it'd cover. It covers you." {n}Her eye moves to you.{/n} "It covers all of 'em. Every driver who took Fellows' silver to lose a cart. I could hang a dozen tomorrow, and I'll not touch one, 'cause the stores they lost are entered as issued. To the Commander, who'd have to explain why." {n}She says it the way another woman might say "to the plague".{/n}
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
"You keep collectin' things in my book, Commander. Carts. Boots. Now a man." {n}She blots it.{/n} "One of these days I'll have to decide what to do with the whole column. Not today. Today there's a flour wagon wants a driver."''',
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
    d("potions", '''"Twelve." {n}She presses a finger against the charcoal number.{/n} "That's what the letter asks us to remember. Fair enough. I'll put it beside the stolen potions. And beside the quartermaster Bartley left bleedin' on the floor. Nerosyan can read all three."''',
      c("Continue", "ours", requires=(POTIONS_OURS,)),
      c("Continue", "his", requires=(POTIONS_BARTLEY,)),
      c("Continue", "ask", forbids=(POTIONS_OURS, POTIONS_BARTLEY))),
    d("ours", '''"You put the potions in your own column, the night we counted the warehouse. Used, quietly. Twelve lines under it." {n}She opens the book and shows you, as if you might have forgotten.{/n}
"So it's written down right, near enough." {n}She dips the pen and copies his last line under yours, word for word, in her own small hard hand: Don't let them write that bit down wrong.{/n} "There. Any lord in Nerosyan who opens this book to hang somebody over twenty-four vials can read that first. He'll hate it. Good."''',
      c("Continue", "ask")),
    d("his", '''"You entered the theft under his name. I wrote it." {n}She closes the ledger.{/n} "That letter's goin' with the report. Let 'em read what he wanted said."''',
      c("Continue", "ask")),
    d("ask", '''{n}She folds the charcoal letter small again, and does not put it in the ledger. She puts it inside her coat.{/n}
"Answer me one thing and I'll not ask again. When you put your name to that line, that first day. Did you do it for him? For them? Or 'cause you're a Trickster and you couldn't stand to see a book balance?"''',
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
], requires=("trickster.ever", WAREHOUSE, TRIBUNAL), forbids=(BARTLEY, REVIEW), delay=48)


# --- 13. After the council: the other voices at her table. ----------------------------------------------------------

office(COUNCIL, "After the council", '"You look like you\'ve sat through the Logistics Council."', [
    d("start", '''"Council's done." {n}She sets the current supply returns beside the requisitions.{/n} "Demons on the walls, carts on the road. Someone's still got to get the issue to the companies. Want the figures, or my opinion?"''',
      c('"Tell me what you really think of them."', "think", forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended')),
      c('"You like them."', "like", forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended')),
      c('"Give me the supply report."', "council_cold", requires=('dorgelinda.ledger.quarrel_unmended',), forbids=()),
      c('"Give me the supply report."', "council_cold", requires=('dorgelinda.ledger.quarrel_cold',), forbids=('dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended')),
      c('"Tell me what you really think of them."', 'think', requires=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.quarrel_unmended',)),
      c('"You like them."', 'like', requires=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.quarrel_unmended',))),
    d("like", '''"Like 'em?" {n}She snorts.{/n} "I'd die for 'em. Doesn't mean I want another council meetin'. Go on. Ask me. I've been savin' it up."''',
      c("Continue", "think")),
    d("think", '''{n}She pours two cups and sets the supply minutes between you.{/n} "They want a recommendation. I want a cart that reaches the front. I'll hear a scheme, but I'll want to know where the stores come from."''',
      c("[Wait for the others.]", "others")),
    d("others", '''"And the hard ones would feed the strong and let the rest go hungry." {n}She sets her hand on the requisitions.{/n} "Then I'm short drivers and the strong ones haven't got ammunition. I'll not run my stores that way."''',
      c('"And you? What would you have them say about you?"', "her"),
      c('"And me?"', "me")),
    d("her", '''"Me." {n}She thinks about it seriously, as if it were a requisition.{/n}
"That she was a thief who counted twice. That she let the lads skim a little, within reason, and hanged nobody she didn't have to, and got the boots to the front more often than not." {n}A pause.{/n} "Two out of three, Commander. That's all anybody's ever managed. I'd like 'em to say I managed two."''',
      c("Continue", "me")),
    d("me", '''{n}She looks at you over the rim of the cup.{/n}
"You." {n}She sets it down.{/n} "You sit at that council table and you listen to all of us and you pick one, and half the time you pick the one that makes the others sulk for a month. That's the job. I'd not do it for all the helmets in Ustalav."
"And then you come here after and let me pour you a drink and complain about 'em. That's not the job." {n}Her eye is very steady.{/n} "Nobody told you to do that."''',
      c('"Nobody had to."', "nobody"),
      c('[Flirt] "The drink\'s better here."', "drink")),
    d("nobody", '''"Good." {n}She refills the cups.{/n} "Tell me where the carts failed you. What the reports left out."''',
      c("[Tell her about the war.]", "tell")),
    d("drink", '''"The drink's better here 'cause I found it, and I found it 'cause I know where things get lost." {n}She refills your cup without asking.{/n}
"You'll get a reputation, Commander, drinkin' with the quartermaster. The lords'll say you're lookin' to rob your own stores." {n}She clinks her cup against yours.{/n} "Tell me where the companies went short. The council's heard enough about honesty for one night."''',
      c("[Tell her about the war.]", "tell")),
    nar("tell", '''{n}You tell her about the fighting and the supply reports. She asks where the carts failed to arrive, and listens to the answer without touching her pen. When you finish, the bottle is lower and the lamp needs trimming.{/n}''',
        c("Continue", "done")),
    d("done", '''"Give me the companies that went short. I'll ask the carters myself." {n}She trims the lamp and caps the bottle.{/n} "Not tonight. There'll be manifests waitin' in the mornin'. Leave the names on my desk."''',
      c("[Leave the last of your cup for her.]", flags=(L + "war_told",))),

    d("council_cold", '"Wagons late. Soldiers hungry." {n}She hands you the written report.{/n} "My recommendation\'s at the bottom. Anything else goes through the clerk."',
      c("[Take the report.]")),
], requires=("trickster.ever", DEBTS), forbids=(COUNCIL,), delay=48)


# --- 14. The west gate: a supply wagon under attack. ----------------------------------------------------------------

office(GATE, "The west gate", '"Quartermaster? What\'s the bell?"', [
    nar("start", '''{n}The alarm bell on the western wall is ringing when you reach her office, and she is not in it. She is in the yard, one-handed, buckling on a breastplate that has not been buckled in years, while a clerk tries to help and gets swatted.{/n}
"Supply wagon," {n}she says, without turning.{/n} "Three hundred yards out, broken axle, and somethin' with wings circlin' it. The gate captain won't open for a cart. I'm not askin' him."''',
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
{n}She turns to you. She looks at you, and then, very briefly, she puts her forehead against your breastbone, and leaves it there for the space of one breath.{/n}
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
    d("end", '''{n}She enters the recovered boots and sends the clerks to check them.{/n} "That was a bloody great set of claws. If your shoulder's open, get a healer to it before you bleed on my floor."''',
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
    d("refused", '''"You refused plunder at the council. These came from men who owe me." {n}She points to the barrels.{/n} "But I can't swear where they got every one. Have a look before I enter ’em."''',
      c("Continue", "how")),
    d("plain", '''"I'm callin' in old debts. Army pals, drinkin' partners, men who owe me." {n}She spreads her good hand at the barrels.{/n} "This is the extra issue. Don't mistake it for the council's supply return."''',
      c("Continue", "how")),
    d("how", '''"Depot sends ten barrels. Carter swears one leaked. Nerosyan writes nine; I unload ten." {n}She taps the chalked figures.{/n} "Old army pal at the depot. Long-overdue debt. Don't look so pleased. I knew this one before you came to Drezen."''',
      c('"You\'re stealing from Mendev."', "stealing"),
      c('"You\'re better at it than the Fellows ever were."', "better")),
    d("stealing", '''"Aye. That tenth barrel belongs at a Mendevian depot." {n}She chalks its weight.{/n} "It'd do more good here than in a baron's cellar. But you can order it back. All of it, not just the brewery's. I'll have less to issue than I've chalked here. Your call."''',
      c('"Keep them. But keep the true weights too. In your own book."', "keep"),
      c('"Send the brewery\'s back. That\'s someone\'s living. Keep the army\'s."', "sort"),
      c('"Send every barrel back. Enter the true loss."', "returned_all")),
    d("better", '''"Bartley took the potions to his sick lads. He also beat my quartermaster and kept a warehouse for himself." {n}She taps her slate.{/n} "I'm enterin' these for the ranks. Still somebody else's barrels. Decide what we keep."''',
      c('"Keep them. But keep the true weights too. In your own book."', "keep"),
      c('"Send the brewery\'s back. That\'s someone\'s living. Keep the army\'s."', "sort"),
      c('"Send every barrel back. Enter the true loss."', "returned_all")),
    d("keep", '''"The true weights." {n}The one eye comes up off the page and stays on you.{/n}
"You want me to write down every stone I took, in my own hand, so there's one book in the world that knows." {n}She takes the slate back.{/n} "That's a dangerous book to keep, Commander. Any lord who got hold of it could hang me with it." {n}She tucks the slate under her arm.{/n} "...I'll keep it. Next to yours. They can hang together."''',
      c("Continue", "end", flags=(L + "true_weights",))),
    d("sort", '''"Somebody's livin'." {n}She repeats it, and snorts, and then she goes and finds the brewery barrels herself, all six, and has them loaded back on the carter's wagon, and pays him a silver from her own purse for his trouble.{/n}
"There. One honest thing in the yard." {n}She dusts her hand.{/n} "Don't tell the lads. They'd rather have had the beer."''',
      c("Continue", "end", flags=(L + "brewery_returned",))),
    d("end", '''{n}She hangs the corrected slate on its nail.{/n} "That's this delivery. The clerks can match it against the stores before they issue another barrel. Hold the door; I've the slate to bring in."''',
      c("[Help her roll the last barrel in.]")),
    d("returned_all", '''"All of it. Aye." {n}She orders the carrier to reload the barrels and crosses their weights off the proposed issue.{/n} "That's a hundred and fifty in stores I won't be handin' out. I'll send the depot the true count. They can choke on the apology."''',
      c("[Help load the returning cart.]", flags=(L + "all_barrels_returned",), crusade=("Materials", -150))),
], requires=("trickster.ever", COUNTED, PRESENT), forbids=(WEIGHT,), delay=24, chapters=(5,))


# --- 16. The Fool King's bill (Chapter 5, after the Trickster's coronation). ------------------------------------------

REVEL_CHOICES = (
    c('"Authorize two hundred from the crusade treasury. Replace the surgeons\' wine first."', "mine", crusade=("Finances", -200)),
    c('"Send the bill to the King."', "king", requires=(KING_REVEL,)),
    c('[Trickster] "It was a jest. You can\'t bill a jest."',
      check=dict(Skill="CheckBluff", DC=28, Success="jest_won", Failure="jest_lost", CommanderOnly=True)),
)

office(REVELS, "The cellar bill", '"You look like you\'ve had a very long night."', [
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
    d("mine", '''{n}She writes the authorization beside the cellar losses and underlines the amount.{/n} "Crusade funds. Two hundred, on your order. I'll buy the surgeons' red before I buy another drop for a drunk." {n}She blots the ink.{/n} "Next celebration, leave me a barrel. Or invite me before the bastards empty it."''',
      c("Continue", "end", flags=(L + "revels_paid",))),
    d("king", '''"Send it to the King." {n}She considers it, slate in hand.{/n}
"The King of Fools, with a crown and a tin sceptre and his whole treasury in his boots." {n}Something happens to her mouth.{/n} "Oh, I'll send it. I'll send it with a clerk in full dress and a trumpet. And he'll read it out to his court of drunks, and they'll cheer it, and he'll pay me in a proclamation." {n}She writes on the slate: Charged to His Majesty.{/n}
"It'll be the most useless bill I ever sent. I'm goin' to enjoy it more than any bill I ever sent."''',
      c("Continue", "end", flags=(L + "revels_billed",))),
    d("jest_won", '''"A jest." {n}She stares at you.{/n}
"You're tellin' me the whole city's night was a jest, and the drink that went down every throat in Drezen in a jest is a jest, and a jest can't be billed." {n}She opens her mouth. She closes it. She looks at the slate.{/n}
"...Hammer and tongs." {n}She rubs out the total with the heel of her bad hand and writes a smaller one under it.{/n} "A jest doesn't pay for the surgeons' red. But I'll not bill one Commander for a whole city's thirst. You get the wine. The city can owe me the ale." {n}She looks, for a moment, almost amused.{/n} "I hate you, Commander. That was a good one."''',
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
    d("plain", '''"Not like the paladins." {n}She turns the small hammer in her palm.{/n} "My mother was a smith. Torag willin', she'd say, then get on with the work. I went for a soldier. She wasn't pleased."''',
      c("Continue", "hammer")),
    d("hammer", '''{n}She lays her mother's hammer beside the requisition book.{/n} "I've wounded troops waitin' on boots and barley. I can do somethin' about that. Torag can wait till the carts are loaded."''',
      c('"Do you want forgiveness?"', "want"),
      c('[Trickster] "Would you let me bargain with Torag on your behalf?"', "bargain")),
    d("want", '''"Want it?" {n}She thinks, the way she thinks about requisitions.{/n}
"No. I want the lads fed and the boots at the front and the war won. Forgiveness is somethin' you want when you've got time." {n}She looks up.{/n}
"After, maybe. If there's an after. I'll build him a little shrine in the stores and put the hammer on it. That'll be all the cathedral I need." {n}Her mouth twists.{/n} "Somebody'll steal the hammer. I'll know who."''',
      c("Continue", "end")),
    d("bargain", '''"No." {n}She puts the hammer away.{/n} "Not for me. I've work enough without findin' I've promised a god somethin' in my sleep. If I've to answer to Torag, I'll answer myself. You leave it alone."''',
      c("Continue", "end", flags=(L + "no_deals",))),
    d("end", '''{n}She takes out the requisition book.{/n} "Right. Enough prayin'. The lads need barley whether Torag's pleased with me or not. Hand me that letter."''',
      c("[Leave her to think.]")),
], requires=("trickster.ever", RATIONS), forbids=(FAITH,), delay=48, chapters=(5,))


# --- 18. After the war (Chapter 5, after the first night): what she'll do when it's over. ------------------------------

office(AFTER, "After the war", '"It\'s cold in here."', [
    nar("start", '''{n}It is. The inner storeroom has no fire, by her own order, because fire and lamp oil and wool do not belong in the same room. She is sitting on a crate of salvaged cloaks in her coat, sorting them one-handed into good, mendable and rags, and she has put a second crate beside hers.{/n}
"Sit. Sort. Rags on the left." {n}Not looking up.{/n}''',
        c("[Sit. Sort.]", "sort")),
    nar("sort", '''{n}You sort. For a long time neither of you speaks. The cloaks came back from the front. Some of them came back without their owners. She checks every pocket before she sorts one, and puts what she finds in a tin box: a coin, a letter, a lock of hair, a wooden horse no bigger than a thumb.{/n}''',
        c('"What do you do with those?"', "tin")),
    d("tin", '''"Send 'em home, where there's a name. Where there isn't, I keep 'em." {n}She drops a brass button into the tin.{/n} "Twenty years of pockets in the back. The chaplain helps me find the families. Takes longer than mendin' the cloaks."''',
      c('"What will you do, after the war?"', "after", forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended'), requires=()),
      c('"What will you do, after the war?"', "after_narrowed", requires=('dorgelinda.ledger.narrowed',), forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended')),
      c('"What will you do, after the war?"', 'after', requires=('dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_cold'), forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_unmended')),
      c('"What will you do, after the war?"', 'after_narrowed', requires=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_cold'), forbids=('dorgelinda.ledger.quarrel_unmended',)),
      c('"What will you do, after the war?"', 'after_cold', requires=('dorgelinda.ledger.quarrel_unmended',), forbids=()),
      c('"What will you do, after the war?"', 'after_cold', requires=('dorgelinda.ledger.quarrel_cold',), forbids=('dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended'))),
    d("after_narrowed", '''{n}Her hands stop, and start again.{/n}
"That's a mornin' question, Commander. We said no mornings." {n}She sorts a cloak into rags, harder than it needs.{/n} "You'd not tell me who else is in your book. I'll not tell you what's in mine. That's the bargain you picked." {n}She does not look up.{/n} "Rags on the left. Go on, I'll finish. Tonight's not one of the nights."''',
      c("[Leave her to the cloaks.]")),
    d("after", '''{n}Her hands stop.{/n}
"After." {n}She says it as if checking whether the word is in stock.{/n}
"Nobody's asked me that since I was a girl." {n}She picks up the cloak again.{/n} "A shop. Boots, I thought, once. Boots that fit. You'd not believe how many men die in this war 'cause their boots don't fit. You'd come in, and I'd measure your feet, and you'd go out in boots that fit, and I'd never have to write you down in a book again."''',
      c('"You\'d miss the book."', "miss"),
      c('"I\'d come in every week to be measured."', "measured")),
    d("miss", '''"I'd miss the book." {n}She laughs, the short bark, quieter than usual in the cold.{/n} "I'd keep one anyway. For the boots. Who bought what, and what size, and did it fit." {n}She sorts a cloak into rags.{/n}
"And your measure. Heel, instep, toe. I'd keep that." {n}She does not look at you.{/n} "Wherever you were."''',
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
    d("joke", '''"Wherever the joke lands." {n}She sorts another cloak.{/n} "That won't get a letter to you. Send me a place when you've got one, Commander. Then I'll know where to send the boots."''',
      c("Continue", "end", flags=(L + "joke_audited",))),
    d("sign", '''{n}She puts the cloak down.{/n}
"That's what folk say in songs." {n}But she says it without any heat at all.{/n} "You'd sign for it. You sign for everythin'." {n}Her breath smokes in the cold while she thinks about it.{/n}
"All right. Sign for it. I'll hold you to it, and I've a grip, you'll recall." {n}She picks the cloak up again.{/n} "Don't make me write it off."''',
      c("Continue", "end", flags=(L + "signed_after",))),
    nar("end", '''{n}When the last cloak is sorted, she shuts the tin of soldiers' keepsakes and places it on the shelf. Outside, the carters are calling for the next load. She picks up the mendable pile and carries it to the door.{/n}''',
        c("[Stay.]")),

    d("after_cold", '"Boots. A shop, if the war leaves me enough leather." {n}She sorts another cloak into rags.{/n} "That\'s all I\'ve to say about after. Leave those on the left. I\'ll finish."',
      c("[Leave her to the cloaks.]")),
], requires=("trickster.ever", MORNING), forbids=(AFTER,), delay=24, chapters=(5,))


# --- 19. Three hundred helmets: the Ustalav letter comes home. -------------------------------------------------------

office(HELMETS, "Three hundred helmets", '"Is that what I think it is?"', [
    nar("start", '''{n}The stores yard is full of crates, and every crate is stencilled in a script you do not read, and every one of them is open. Clerks are lifting out helmets, plain kettle hats and a few good sallets, and stacking them by size along the wall. Dorgelinda stands in the middle of it with a lantern and an expression you have never seen on her face before. It takes a moment to recognise it as delight.{/n}''',
        c("Continue", "forged", requires=(FORGED,)),
        c("Continue", "honest", requires=(HONEST_DEMAND,), forbids=(FORGED,)),
        c("Continue", "fence", requires=(FENCE_CALLED,), forbids=(FORGED, HONEST_DEMAND)),
        c("Continue", "arrived", forbids=(FORGED, HONEST_DEMAND, FENCE_CALLED))),
    d("arrived", '''"Three hundred helmets. Out of a customs yard in Ustalav at last, and don't ask me how, 'cause I wrote so many letters I've lost track of which one worked." {n}She lifts one and turns it in the lamplight.{/n}
"Somebody in Ustalav finally read the word 'Worldwound' and decided they'd rather not have three hundred of our helmets on their conscience." {n}She sets it on a stack.{/n} "Three hundred heads. I'll take it."''',
      c("Continue", "stack", flags=(L + "helmets_received",), forbids=(L + "helmets_received",), crusade=("Materials", 100)),
      c("Continue", "stack", requires=(L + "helmets_received",))),
    d("forged", '''"Three hundred helmets. Out of a customs yard in Ustalav on the strength of a Mendevian treasury release with the Chancellor's i's dotted wrong." {n}She lifts one and turns it in the lamplight.{/n}
"And a letter with 'em. Ustalavic customs, very polite, askin' the Chancellor to confirm his release, 'cause he's taken to dottin' his i's with a round dot lately and they wondered was he unwell." {n}She puts the helmet on a stack.{/n} "I've answered it. In his hand. He's very well, thank you, and a round dot is the fashion in Nerosyan."''',
      c('"You forged the Chancellor twice."', "twice")),
    d("twice", '''"I forged the Chancellor twice." {n}She seems to taste the words.{/n}
"First time's the Commander's. Second time's mine. That's how it goes, isn't it. You start a thing in my book and then I'm the one keepin' it alive." {n}She sets the lantern on a crate.{/n}
"It's a lie, and it's got my name nowhere on it, and three hundred lads'll go up the walls with iron on their heads 'cause of it. I've done worse for less." {n}She looks at you sidelong.{/n} "Don't make it a habit. Nerosyan's got clerks too, and some of 'em can count."''',
      c("Continue", "stack", flags=(L + "helmets_received",), forbids=(L + "helmets_received",), crusade=("Materials", 100)),
      c("Continue", "stack", requires=(L + "helmets_received",))),
    d("honest", '''"Three hundred helmets. No, two hundred and forty. The Ustalavic customs clerk sent sixty of 'em somewhere else before your letter reached him, and he's very sorry, and he's sent an apology on good paper." {n}She holds it up. It is very long.{/n}
"He read the bit about the Worldwound. He put in a line of his own about how Ustalav prays for us nightly." {n}She folds it.{/n} "Two hundred and forty heads. Honestly come by. I didn't think you had it in you, Commander. Frightenin' a customs clerk with the truth."''',
      c("Continue", "stack", flags=(L + "helmets_received",), forbids=(L + "helmets_received",), crusade=("Materials", 75)),
      c("Continue", "stack", requires=(L + "helmets_received",))),
    d("fence", '''"Three hundred helmets. Came up the Nerosyan road on a wagon with Ustalavic customs seals nobody ever stamped, drove straight through the gate past a sergeant who swears he saw no driver, and stopped in my yard." {n}She lifts one and turns it in the lamplight.{/n}
"No letter. No bill. My debt's paid. There's a nail on the wagon seat. Just the one." {n}She holds it up between her good finger and thumb.{/n} "That's his mark. He's tellin' me we're square, and he's tellin' me he could find a nail in my stores if he wanted." {n}She pockets it.{/n} "You'll not ask how. That was the rule."''',
      c("Continue", "stack", flags=(L + "helmets_received",), forbids=(L + "helmets_received",), crusade=("Materials", 100)),
      c("Continue", "stack", requires=(L + "helmets_received",))),
    nar("stack", '''{n}You help stack. It is slow work and cold, and the clerks go home one by one until it is only the two of you and the last crate. She hands you helmets and you set them on the stacks, and she counts each one aloud as you set it down, and does not lose count once.{/n}''',
        c("[Try one on.]", "try"),
        c("[Keep stacking.]", "last")),
    d("try", '''{n}She watches you put it on. It is too small. She laughs so hard she has to sit down on the crate.{/n}
"Oh, that's a picture. The Commander of the Fifth Crusade in a levy's kettle hat, three sizes small." {n}She wipes her eye with the back of her bad hand.{/n}
"Take it off before somebody paints it. Here." {n}She finds another, larger, and sets it on your head herself, and adjusts the strap under your chin with her good hand, with great care, as if it mattered.{/n} "There. That one fits. Now you look like somebody I'd trust on a wall."''',
      c("Continue", "last")),
    d("last", '''{n}She holds the lantern up to the finished stacks.{/n} "Iron for the lads. At last." {n}She lowers it.{/n} "Tomorrow I'll have the clerks count 'em. Tonight I'm lookin'."''',
      c("[Walk her back to the office.]")),
], requires=("trickster.ever", DEBTS), forbids=(HELMETS,), delay=96)


# --- 20. The plague ward (the tribunal path, after the warehouse). ---------------------------------------------------

office(WARD, "The plague ward", '"Where are we going?"', [
    nar("start", '''{n}She does not say. She takes you out of the stores and across the lower bailey to the long stone barracks the healers took over after the last battle, where the windows are kept open in all weathers and the smell comes out to meet you before the door does.{/n}
{n}Inside, in two rows of cots, men and women with grey faces and bandaged eyes are sleeping or pretending to. A few are sitting up. One is playing dice against himself.{/n}''',
        c("Continue", "ward")),
    d("ward", '''"Bartley's company." {n}She keeps her voice low.{/n} "Came back with the plague on 'em. Green slime for tears, rottin' in their cots. The potions he stole got twelve through it. They're still here."''',
      c("Continue", "ours", requires=(POTIONS_OURS,)),
      c("Continue", "his", requires=(POTIONS_BARTLEY,)),
      c("Continue", "neither", forbids=(POTIONS_OURS, POTIONS_BARTLEY))),
    d("ours", '''"And in mine it says the Commander drank 'em. All twenty-four. Very thirsty, the Commander." {n}Her mouth twitches.{/n}
"I've had three officers from the general staff come to my desk this month askin' after their potions. I showed 'em the line. They went very quiet. One of 'em asked if you were well." {n}She looks down the row again.{/n} "They're well because Bartley got the potions into 'em. Our paperwork came after. Don't mix those up."''',
      c("Continue", "soldier")),
    d("his", '''"I wanted you to see what the theft bought. He nearly killed a quartermaster to do it. Those are the men he saved."''',
      c("Continue", "soldier")),
    d("neither", '''"Those are the lads Bartley stole the potions for. I wanted you to see 'em before they're sent back to the walls."''',
      c("Continue", "soldier")),
    nar("soldier", '''{n}The soldier with the dice looks up. He has a healer's bandage over one eye and the new pink skin of a man who has nearly rotted and then not. He knows the Commander. Everyone does. He starts to get up, and cannot quite, and salutes from the cot instead.{/n}
{n}Then he sees the quartermaster beside you, and his face changes, the way a soldier's face changes when he sees someone he owes.{/n}''',
        c("Continue", "salute")),
    d("salute", '''"Ma'am." {n}The soldier's voice is a rasp.{/n} "Corporal said to tell you, if I saw you. He said: tell the old Stranglehold we know she didn't want the rope."
{n}Dorgelinda stands very still.{/n}
"Did he." {n}Her voice does not change at all.{/n} "Get some sleep, soldier. You're on the east wall next week, eye or no eye. We're short."
{n}The soldier grins, and lies back, and closes his good eye.{/n}''',
      c("Continue", "outside")),
    nar("outside", '''{n}Outside, in the cold, she walks faster than a dwarf needs to, and does not stop until you are round the corner of the barracks, out of sight of the windows. Then she stops, and leans her shoulder against the stone, and breathes out once, long, as if she has been holding it since the tribunal.{/n}''',
        c('"You didn\'t want the rope."', "rope", forbids=(HANGED,)),
        c("[Wait beside her.]", "wait", forbids=(HANGED,)),
        c('"You didn\'t want the rope."', "rope_hanged", requires=(HANGED,)),
        c("[Wait beside her.]", "wait_hanged", requires=(HANGED,))),
    d("rope", '''"No. I didn't want it." {n}She glances back at the barracks.{/n} "He beat my quartermaster half to death. Stole more than these potions, too. I asked for chains to Nerosyan, and I meant it." {n}She straightens her coat.{/n} "Come on. They're tryin' to sleep."''',
      c("[Walk her back.]", flags=(L + "ward_seen",))),
    d("wait", '''{n}You wait beside her as a patrol passes overhead.{/n} "They looked near dead when the potions reached 'em. Now that one's playin' dice." {n}She pushes off the wall.{/n} "Come on. I've got kit to find for 'em before they're back on duty."''',
      c("[Walk her back.]", flags=(L + "ward_seen",))),
    d("rope_hanged", '''"No. I didn't want it." {n}She keeps her eye on the barracks door.{/n} "He saved those men and nearly killed my quartermaster. You had him executed. I'll not pretend I was glad to watch. Come on."''',
      c("[Walk her back.]", flags=(L + "ward_seen",))),
    d("wait_hanged", '''{n}She waits until the patrol has passed.{/n} "Twelve came through the plague. Bartley's dead. I saw both. Don't ask me to be glad about the second because of the first." {n}She starts back toward the stores.{/n}''',
      c("[Walk her back.]", flags=(L + "ward_seen",))),
], requires=("trickster.ever", WAREHOUSE), forbids=(WARD, REVIEW), delay=24)


# --- 21. The army back from Iz (Chapter 5, after the Coronation). ---------------------------------------------------

office(SURVIVORS, "Half an army", '"How many came back?"', [
    nar("start", '''{n}She is not in her office. She is at the gate, with a table set up in the mud and a clerk on either side of her, and a line of soldiers that stretches back down the road as far as the light goes. They are the army that came back from Iz. They are thinner than the army that went. Most of them are carrying less than they left with, and some of them are carrying other people's things.{/n}''',
        c("[Go to her table.]", "table")),
    d("table", '''"Name, company, what you've got, what you haven't." {n}She says it to every one of them, the same way, as they come to the table. She does not look up at you. She knows you are there.{/n}
"How many came back?" {n}She answers her own question before you can ask it, without stopping.{/n} "I'll tell you when I've counted. I don't guess numbers like that. You'd not want me to."''',
      c("[Take the next soldier yourself.]", "help"),
      c('"Let the clerks do this. You should rest."', "rest")),
    d("rest", '''"Rest." {n}She writes a name.{/n}
"These lads walked back from Iz, Commander. Half of 'em without boots. They've been waitin' on this road since dawn to be told what they're owed and where to sleep. And they'll be told it by me, 'cause I'm the one who'll remember if it's wrong." {n}She writes another.{/n}
"You want to help, sit down on that crate and take the next one. If you want to be useful, don't tell me to rest."''',
      c("[Sit down on the crate and take the next one.]", "help")),
    nar("help", '''{n}You take the next one. And the next. Name, company, what they have, what they have not. A pikeman with no pike. A cook with one pan. A girl of eighteen with a sergeant's stripes cut from a dead man's sleeve and sewn on crooked, who says she is the sergeant now because there is nobody else.{/n}
{n}The line does not get shorter for a long time. When it does, it is dark, and Dorgelinda's voice has gone hoarse, and her good hand is cramped around the pen.{/n}''',
        c("Continue", "count")),
    d("count", '''{n}She adds the columns. She does it twice. Then she sits back.{/n}
"There's your number." {n}She turns the book toward you. She does not say it aloud. She has written it at the foot of the page and underlined it.{/n}
"The city's singin' in the streets up there. Drunk on my brandy, I shouldn't wonder. Celebratin' the Commander's triumphant return." {n}She closes the book.{/n} "They're right to. You came back. They came back. This lot came back. That's worth singin' for." {n}She rubs her cramped hand.{/n} "Somebody's got to count the ones who didn't. That's all."''',
      c("[Take her hand and work the cramp out of it.]", "hand"),
      c('"I\'ll remember the number."', "remember")),
    d("hand", '''{n}She lets you. The good hand is hot and stiff, the fingers curled from ten hours on the pen. You work them straight, one by one, and she watches you do it with the one eye and does not say anything at all.{/n}
"Stranglehold," {n}she says at last, very low, when the hand is loose.{/n} "Even the good one's got its limits." {n}She does not take it back.{/n} "Don't tell the jokesters."''',
      c("Continue", "end", flags=(L + "hand_eased",))),
    d("remember", '''"Good." {n}She nods once, slowly, as if ticking off a line.{/n}
"Most commanders don't want to know it. They want the victory and the bill for the victory, and they don't want the number in between." {n}She picks up the book.{/n} "You sat in the mud and took names for eight hours. I'll not forget that either." {n}She stands, stiffly.{/n} "Now. Supper. I've some salt pork that isn't on a manifest."''',
      c("Continue", "end")),
    nar("end", '''{n}Behind you, on the walls, someone has started a drinking song. The survivors in the yard turn to listen to it. A few of them begin, quietly, to sing along.{/n}''',
        c("[Walk her back through the gate.]")),
], requires=("trickster.ever", COUNTED, "coronation.seen"), forbids=(SURVIVORS,), chapters=(5,))


# --- 22. Other columns (after the first night): the Commander's other loves. ----------------------------------------

office(OTHERS, "Other columns", '"You\'re quiet today."', [
    d("start", '''"I'm quiet 'cause I'm countin'." {n}She has a ledger open that is not the stores ledger. It is small, cheap, bound in grey cloth, and the hand in it is hers, very small.{/n}
"Everybody in Drezen keeps accounts on the Commander. Did you know? The clerks keep 'em, the cooks keep 'em, the sentries on the east wall have a book goin' on who you'll be seen with next." {n}She taps the grey ledger.{/n} "I took theirs off 'em. Confiscated. It was a disgrace. The arithmetic was terrible."''',
      c('"And what does it say?"', "says")),
    d("says", '''"It says I'm not the only line in your book. That's the sentries' arithmetic, mind." {n}Flatly, like a shortage.{/n}
"I'm not a fool, and I've got one good eye, and I use it. A Commander's got a lot of columns, or folk say so." {n}She closes the grey ledger.{/n} "I'd be a poor quartermaster if I took a sentry's word for it, and a poorer one if I didn't ask."''',
      c('"There are others. Ask me about any of them, and I\'ll answer."', "bother"),
      c('"You\'re not the only line. You\'re the one I sign for."', "sign"),
      c('"That\'s my business, Quartermaster."', "unblessed"),
      c('[Lie] "There\'s nobody else. The sentries have bad arithmetic."', "lie"),
      c('"Nobody else. Not one. The sentries can bet on the weather."', "nobody")),
    d("nobody", '''"Aye. Then I've no other names to ask for." {n}She leaves the grey notebook closed and puts your cup within reach.{/n} "If that changes, I hear it from you first. Not from a sentry, not from a clerk. That's what I'll have."''',
      c("[Stay.]", flags=(L + "sole_line",))),
    d("unblessed", '''"Your business." {n}She says it slowly, as if entering it.{/n}
"Right. Then it's yours, and my stores are mine. Nobody else draws on 'em on your seal, and I'll not ask, and you'll not tell." {n}She puts the grey ledger in a drawer and locks it.{/n}
"That's not a blessin', Commander. Don't mistake it for one. It's a separate column, and I'll keep it separate." {n}She does not look up again.{/n} "Same time next week."''',
      c("[Leave.]", flags=(L + "unblessed",))),
    d("lie", '''{n}She opens the grey ledger again, without hurry, and reads you three entries from it: two names, two dates, one of them this week. The sentries' arithmetic is excellent.{/n}
"That's the first lie you've ever told me about your own column." {n}Very quietly.{/n} "You've signed for shortages that weren't yours. I carried every one. I'll not carry that." {n}She holds out her good hand, palm up.{/n}
"The cup, Commander."''',
      c("[Put her cup in her hand.]", "ruled")),
    d("ruled", '''{n}She closes her fingers on it. Then she takes up the pen and rules a line under your column, straight and hard, the full width of the page.{/n}
"You'll draw on my stores like any other officer from now on. By requisition. Through a clerk." {n}She does not look up.{/n} "Dismissed."''',
      c("[Go.]", flags=(CLOSED, L + "line_ruled"))),
    d("bother", '''{n}She thinks about it properly, the way she thinks about everything.{/n}
"Bother me." {n}She turns the grey book over in her good hand.{/n} "It'd bother me if you lied about it. It'd bother me if I found one of 'em in my stores drawin' on your seal without askin'. It'd bother me if you were one of those that promises every line it's the only one and then can't balance a single account." {n}She puts the book down.{/n}
"You've never once lied to me about what's in your column, Commander. You lie about everythin' else. Not that."''',
      c("Continue", "terms")),
    d("sign", '''"The one you sign for." {n}She snorts, but her ears have gone faintly red.{/n}
"You sign for everythin'. You'd sign for the weather." {n}She turns the grey book over in her good hand.{/n} "But you've never once lied to me about what's in your column. You lie about everythin' else. Not that."''',
      c("Continue", "terms")),
    d("terms", '''"Before I say yes or no to anythin', I want the names." {n}She opens the grey ledger at a clean page and holds the pen over it.{/n}
"Not for the book. For me. I'll not share with somebody I can't picture, Commander. I'll not be one line among lines I've never read."''',
      c("[Name them, one by one, and what each of them is to you.]", "named"),
      c('"Does it matter who?"', "narrow")),
    d("named", '''{n}You name them. She writes nothing. She listens to each name with the whole of her attention, the way she listens to a carter explain a shortfall, and once or twice she nods, and once her jaw sets and stays set.{/n}
"Right." {n}She closes the grey ledger.{/n} "Here's what I'll have, then. Nobody draws on my stores on your seal but you. None of 'em sets foot in my rooms, ever. And you hear it from me first if one of 'em crosses me, and I hear it from you first if you ever mean to choose." {n}She holds out her good hand.{/n} "That's the whole of it. Shake on it or don't."''',
      c("[Shake on it.]", "shaken")),
    d("shaken", '''{n}She closes her good hand around yours, holding on a moment after the shake.{/n} "Done. My rooms, my choice of company. Tell me before you change what you've promised." {n}She closes the grey notebook and takes your cup from the shelf.{/n}''',
      c("[Stay.]", flags=(L + "terms_kept",))),
    d("narrow", '''"It matters to me." {n}She puts the pen down.{/n}
"You'll not tell me, then here's what you get. I'm your quartermaster, and I'm yours on the nights I say, in my rooms, and that's all. No mornings. No tellin' me what worries you. I'll not hand more of myself to a column I'm not allowed to read." {n}She closes the grey ledger.{/n}
"That's not a no, Commander. It's a smaller yes. You made it smaller."''',
      c("[Accept it.]", flags=(L + "narrowed",))),
], requires=("trickster.ever", MORNING), forbids=(OTHERS,), delay=24, chapters=(5,))


# --- 23. The unbalanced line (after her "Not today"). -------------------------------------------------------------

office(UNBALANCED, "The unbalanced line", '"Quartermaster."', [
    nar("start", '''{n}She is at her desk. She looks up when you come in, and then down again, very quickly, at the ledger, which is open, but not at your line. It is open at a page of horseshoes.{/n}
"Commander." {n}Formal. The pen keeps moving.{/n} "Somethin' from the stores?"''',
        c('"No. You."', "you"),
        c('"Horseshoes. I heard we were short."', "shoes")),
    d("shoes", '''"We're always short of horseshoes." {n}She writes a figure.{/n}
"Horses keep losin' 'em. Nobody knows where they go. There's probably a demon in the Abyss sittin' on a pile of Crusade horseshoes laughin' at us." {n}She blots it.{/n}
"...That's not what you came for." {n}She does not look up.{/n} "Go on. Ask. I'll give you the same answer, but you can ask."''',
      c("Continue", "you")),
    d("you", '''"I told you." {n}She puts the pen down. She still does not turn the book to your page.{/n}
"I'll not say yes to a line I can't balance. It's not a punishment. It's not a game. I'm not holdin' out for a better offer." {n}Her good hand is flat on the horseshoes.{/n}
"I've spent my whole life makin' books balance, Commander. Every one. And I'll not start somethin' with you that I can't close the day it goes wrong. I've buried too many books that didn't."''',
      c('"What would it take?"', "take"),
      c('"I understand. I\'ll wait."', "wait")),
    d("take", '''"You know what it'd take. I said it." {n}She finally looks at you.{/n}
"Where it went. All of it. The first line, and every one after it. You tell me and I'll write it, and if it's ugly I'll write that too, and then I'll know what I'm sayin' yes to." {n}She picks the pen back up.{/n}
"Take your time. I'm not goin' anywhere. The stores aren't goin' anywhere. Well. Some of the horseshoes are."''',
      c("[Leave her to the horseshoes.]")),
    d("wait", '''"Wait." {n}She seems surprised by it. She turns the word over the way she would a coin she did not expect to find.{/n}
"Most folk don't. They either push or they go." {n}She looks at the ledger, and then, after a moment, she turns it to your page, and looks at that instead, the long open column with no line ruled under it.{/n}
"...It's still open," {n}she says.{/n} "Don't think I've shut it. I've never shut it. I just haven't signed." {n}She closes the book.{/n} "Go on. I've horseshoes."''',
      c("[Leave her to the horseshoes.]", flags=(L + "waited",))),
], requires=("trickster.ever", DECLINED), forbids=(UNBALANCED, COMMITTED), delay=24, chapters=(5,))


# --- 24. The quartermaster of the march (Logistics_Officer/Cue_0012 11981a23: medal for the assault on Drezen). -------

office(MARCH, "The quartermaster of the march", '"Who\'s the transfer for?"', [
    d("start", '''"Old Harrow. Not his name. That's what the lads call him. He'll harrow a field for turnips if the carts are late." {n}She pushes a transfer request across the desk, signed with a thumbprint.{/n} "He kept the camp supplied on the march. Got his medal for the assault on Drezen. Good soldier. Fortress stores were beyond him, so he's back at his old work. Now he wants to go with the next column."''',
      c('"Is that a problem?"', "problem")),
    d("problem", '''"It's a problem 'cause I need your signature on it and I don't want to give it you." {n}She sits back.{/n}
"He's sixty if he's a day. His knees are gone. He'll march with that column 'cause he can't stand to be the man who stayed behind, and one night on the road some demon'll come over a wagon and he'll be the one holdin' the spear." {n}Her good hand closes, slowly, on nothing.{/n} "I know how that goes. I know exactly how it goes."''',
      c('"Then I won\'t sign it."', "refuse"),
      c('"He knows how it goes too. It\'s his choice."', "sign"),
      c('[Trickster] "Sign it. And lose it on the way to the column."', "lose")),
    d("refuse", '''"You won't sign it." {n}She lets the silence run the length of a manifest.{/n}
"And he'll come to my desk tomorrow and ask why, and I'll say the Commander refused it, and he'll look at me like I've taken his medal off him." {n}She picks the paper up and puts it in a drawer.{/n} "Thank you. I mean it. I'd not have been able to do it myself, and I'd not have been able to forgive you if you'd signed it." {n}A short breath.{/n} "That's a rotten position to put you in. I did it anyway. Put it in my column."''',
      c("Continue", "after", flags=(L + "harrow_kept",))),
    d("sign", '''"His choice." {n}She says it the way she says "two out of three".{/n}
"Aye. It is." {n}She watches you sign it. She takes it back and reads your signature as if it were a manifest, as if there might be a mistake in it that would save him.{/n}
"There. He'll go. He'll feed that column better than anybody in Golarion could." {n}She puts the paper in the tray for the courier.{/n} "And if the column comes back without him, I'll have signed nothin', and you'll have signed it, and I'll still be the one who asked you to." {n}She does not look up.{/n} "That's the job."''',
      c("Continue", "after", flags=(L + "harrow_sent",))),
    d("lose", '''{n}She stares at you. Then, slowly, she begins to laugh, without sound, her shoulders shaking.{/n}
"Sign it. Give it to the courier. And the courier loses it. And old Harrow waits for his orders, and waits, and writes again, and it's lost again." {n}She wipes her eye.{/n} "And every time he asks, I'll be able to look him in the face and say the Commander signed. It's true. You did."
{n}She takes the signed paper and, with great deliberation, files it in the back of the ledger, behind your column.{/n} "Used, quietly. Hammer and tongs, Commander. That's the cruellest kindness I've ever seen."''',
      c("Continue", "after", flags=(L + "harrow_lost",))),
    d("after", '''"He wants to go because he can still feed a marchin' army. I know what it is to lose the work you're good at." {n}She sets the pen down.{/n} "I found this job. Doesn't mean I like sendin' an old soldier out where I can't watch him."''',
      c('"You did it for them. The same as the stores."', "same"),
      c("[Put your hand over hers, on the pen.]", "pen")),
    d("same", '''"The same as the stores." {n}She nods slowly.{/n} "Maybe. I'd like to think so. On a good day I think so." {n}She puts the pen down.{/n}
"On a bad day I think I'm a one-eyed dwarf who's good at sums and bad at sayin' no." {n}She looks at you.{/n} "Today's a middlin' day. Thanks to you. Now let me get the next issue out."''',
      c("[Leave her to the tray.]")),
    d("pen", '''{n}She lets your hand lie over hers. The pen is between your fingers and hers. Neither of you moves it.{/n}
"You'll get ink on you." {n}Very quietly.{/n}
"...Fine. Get ink on you." {n}She turns her hand under yours, so that for a moment it is holding yours and not the pen, and the pen rolls away across the desk and neither of you goes after it.{/n}''',
      c("[Leave her to the tray, eventually.]", flags=(L + "pen_dropped",))),
], requires=("trickster.ever", HAND), forbids=(MARCH,), delay=48)


# --- 25. The sergeant's version (the third jokester). ---------------------------------------------------------------

office(SERGEANT, "The sergeant's version", '"Is the Quartermaster in?"', [
    nar("start", '''{n}She is not. The supply sergeant with the bandaged ear is at her desk instead, doing her figures in a slower hand than hers, with his tongue between his teeth. He jumps up so fast he knocks the ink over, and rights it, and salutes, in that order.{/n}
"Commander! She's at the gate, Commander. Caravan from Nerosyan. Half a caravan." {n}He looks at the spilled ink, and at you, and seems to decide something.{/n}''',
        c('"You\'re the jokester. The third one."', "jokester"),
        c('"I\'ll wait."', "wait")),
    nar("wait", '''{n}You wait. He mops the ink. It takes him a long time, and he watches you out of the corner of his eye the whole time, the way a man watches a dog he has been told is friendly.{/n}''',
        c('"She says you gave her the nickname."', "jokester")),
    d("jokester", '''{n}He goes a deep, dull red.{/n}
"She told you that." {n}He puts the rag down.{/n} "Aye. Me and two others. We were in the same company, before. After she got hurt, she used to hold her ration bowl in the good hand and sort of hook the bad one over the edge, to steady it, and it'd slip. Every meal. And Dobbin said..." {n}He stops.{/n} "Well. Dobbin said somethin' about her grip. And I said 'Stranglehold', and we all laughed. We were young. We were stupid."''',
      c('"And then?"', "then")),
    d("then", '''"And then she heard it." {n}He rubs his ear, the bandaged one, absently.{/n}
"Didn't say a word. Next week she's in the supply tent. Week after, she's runnin' it. By winter she's got the whole company's stores in a grip you couldn't pry a nail out of, and she's got Dobbin scrubbin' the supply-tent floor every night for a month, on his knees, with her countin' the strokes." {n}He grins, then stops grinning.{/n}
"Dobbin's dead. On the walls, at Drezen. She buried him in good boots. Right size. She measured 'em herself."''',
      c('"And you?"', "you")),
    d("you", '''"Eight years I've been her sergeant. Still count twice." {n}He glances at the door.{/n} "The lads say you're in here more than the colonels, Commander. She leaves the good bottle out when you're due. We notice. Is there somethin' in that?"''',
      c('"I signed for it. She let me."', "let"),
      c('"That\'s between me and the Quartermaster."', "between")),
    d("let", '''"Aye. She let you." {n}He picks up the rag.{/n} "Then bring your boots back when she asks, Commander. She'll have my ear if you don't. What's left of it."''',
      c("Continue", "door")),
    d("between", '''"Aye. Sorry, Commander." {n}He goes back to the ink.{/n} "I'll tell the lads to mind their own kit. She's got enough bother with the Nerosyan carts."''',
      c("Continue", "door")),
    nar("door", '''{n}The door opens. Dorgelinda comes in with snow on her shoulders and a manifest in her good hand, and stops, and looks from the sergeant to you to the ink-stained rag.{/n}''',
        c("Continue", "back")),
    d("back", '''"What's he told you?" {n}To the sergeant, not to you.{/n}
"Nothin', ma'am." {n}Instantly.{/n}
"Liar. You've got the face you had in the mess tent." {n}She hangs up her coat.{/n} "Go and count the Nerosyan carts. Twice. And if you've told the Commander about the ration bowl, count 'em three times." {n}He goes, fast.{/n}
{n}She sits down, and looks at the wet ink on the desk, and then at you.{/n} "He told you about the bowl." {n}Not a question.{/n} "...He always tells it wrong. Dobbin said it, not him. He's been takin' the blame since before Drezen, 'cause Dobbin can't."''',
      c("[Help her blot the ledger.]", flags=(L + "sergeant_heard",))),
], requires=("trickster.ever", GRIP), forbids=(SERGEANT,), delay=48)


# --- 26. Hammer and tongs: the quarrel (after the first night). --------------------------------------------------------

QUARREL = (
    c('"I\'d do it again."', "again"),
    c('"You\'re right. We were reckless. We need to answer together."', "sorry"),
    c('[Intimidate] "It was my seal. I don\'t need your leave."', "seal"),
)

office(QUARREL_SCENE, "Hammer and tongs", '"You wanted to see me?"', [
    d("start", '''"Nerosyan's cut our allotment. A quarter off grain, a third off powder, half off boots." {n}She flattens a creased letter on the desk.{/n} "Some bastard at court's read about your signatures under the irregular issues. Calls it a joke between friends. 'Irregular accounting,' he writes. The lads on the walls get less bread, and he gets a fine phrase."''',
      c('"That\'s not a joke between friends."', "friends")),
    d("friends", '''"No. It's not. I watched you sign. I let the issue through." {n}She slaps the letter.{/n} "Now he's punishin' the ranks for it. We gave him that opening, you and me. Don't sit there grinnin' as if we've outwitted him."''',
      *QUARREL),
    d("again", '''"You'd do it again. Course you would." {n}She sits down hard.{/n} "And I'd let you. I watched that ink dry. Thought we'd got the lads what they needed. Now I've a letter from Nerosyan and a quarter less bread." {n}She rubs her eye.{/n} "Hammer and tongs. I'm angry with you. And with myself."''',
      c("Continue", "cool")),
    d("sorry", '''"Together. Aye." {n}She sits, still holding the letter.{/n} "I knew what we signed. I thought gettin' the stores to the front would be enough. It wasn't." {n}She draws a fresh sheet toward her.{/n} "Next time we work out who can cut the allotment before we give him a laugh. And if you hear a threat from court, I hear it too."''',
      c("Continue", "cool", flags=(L + "tell_first",))),
    d("seal", '''{n}Silence. The kind that fills a room.{/n}
"No," {n}she says at last, very evenly.{/n} "You don't. You're the Commander. You can sign for what you like and I'll write it down." {n}She folds the letter, precisely.{/n}
"And I'm the quartermaster, and I'll feed the walls on a quarter less bread, and I'll not say one word about it to you again. You've my word." {n}She puts the letter in a drawer.{/n} "Was there anythin' else, Commander?"''',
      c('"...That was a stupid thing to say. I\'m sorry."', "cool"),
      c("[Leave.]", "cold")),
    d("cold", '''{n}You leave. She does not look up when the door closes.{/n}''',
      c("[Go.]", flags=(QUARREL_COLD,))),
    d("cool", '''"Right." {n}She takes a breath and lets it out.{/n} "Here's what we'll do." {n}She pulls a fresh sheet toward her.{/n}
"I'll write to Nerosyan. Dull as ditchwater. Every cart and crate accounted for, all regular, all quiet, nothin' to laugh about. The Commander's line in a separate book, on my shelf, not theirs." {n}She dips the pen.{/n} "And you'll write a line under mine sayin' the Commander's full confidence is in the quartermaster. Your hand. Your seal. No jokes in it."''',
      c("[Write it. No jokes.]", "written")),
    d("written", '''{n}She reads your sober letter, folds it with hers and seals them together. Later, a treasury reply reaches her desk: the powder allocation is restored; the grain and boots remain cut.{/n} "There. Powder for the guns. The rest I'll have to find elsewhere." {n}She sets your cup beside the letter.{/n} "You stood behind me. That's mended. Sit a bit."''',
      c("[Shut the door.]", flags=(L + "quarrel_mended",))),
], requires=("trickster.ever", OTHERS), forbids=(QUARREL_SCENE,), delay=48, chapters=(5,))


# --- 26b. Cold counts: after the Commander walked out of the quarrel. Mend it, or let it stand. --------------------------

office(COLD_COUNTS, "Cold counts", '"Line thirty-one, Quartermaster?"', [
    nar("start", '''{n}She counts you exactly as she counts a wagon: aloud, without looking up. Boots. Blankets. One flask, not regulation. She has done it this way every time since you walked out on her, and her clerks have stopped pretending not to listen. She says nothing that is not a figure.{/n}
"Line thirty-one, balanced. Next."''',
        c('[Set a bottle that is on no manifest on her desk, in front of the clerks.] "I was wrong about the seal. I\'m sorry, Quartermaster."', "apology"),
        c("[Sign for your kit and go. Let it stand.]", "stand")),
    d("apology", '''{n}The clerks find, all at once, that they are needed in the yard. The last one shuts the door very carefully.{/n}
"In front of my clerks." {n}She looks at the bottle, not at you.{/n} "You know what that'll cost you in the barracks? The Commander, sayin' sorry to the quartermaster." {n}She pulls the cork with her teeth and spits it on the blotter.{/n} "Good. It should cost somethin'. Sit down."''',
      c("Continue", "letter")),
    d("letter", '''"I wrote Nerosyan without you. Dull as ditchwater. Every cart accounted for, nothin' to laugh about. They gave us the powder back, not the boots." {n}She pours two cups, short ones.{/n} "There's a line left at the foot of it, for the Commander's confidence in the quartermaster. I didn't fill it in. It's not my hand they want."''',
      c("[Write it. Your hand, your seal. No jokes.]", "written")),
    d("written", '''{n}She reads your letter twice and puts it in the courier's tray. Then she looks up at you.{/n} "There. That's mended. Took you long enough. Have a drink before I find somethin' else to shout about."''',
      c("[Shut the door.]", flags=(L + "quarrel_mended",))),
    d("stand", '''{n}You sign. She blots it. Not another word passes the desk, and the clerks go back to their figures, disappointed.{/n}''',
      c("[Go.]", flags=(L + "quarrel_unmended",))),
], requires=("trickster.ever", QUARREL_COLD), forbids=(COLD_COUNTS, L + "quarrel_mended"), delay=168, chapters=(5,))


# --- 27. The right size (Logistics_2/Cue_0080: "a boot one size too large can lead to a soldier's death"). -------------

office(SIZE, "The right size", '"Why is there a boot on your desk?"', [
    d("start", '''"South-wall levy." {n}A patched boot stands upside down on her blotter. The toe is packed with bloody rags.{/n} "His own split on the ice. Borrowed this off a mate. Two sizes too big, and he kept walkin' in it till the heel rubbed raw. I've found him a pair that fits. Kept this to show the clerks what 'near enough' buys."''',
      c('"Then why is it here?"', "why")),
    d("why", '''"Blister on the march. Can't keep up. Left behind for somethin' hungry." {n}She takes the rags out of the toe and drops them in the waste bucket.{/n} "That lad needs boots, not somebody's bloody castoffs. I've told the clerks to measure him before they hand him another pair."''',
      c('"Is that a complaint about my stores?"', "complaint"),
      c('"Then teach me the right size."', "teach")),
    d("complaint", '''"Aye. Our stores." {n}She points at the stool.{/n} "I've dealt with his. Now yours. Sit down. The right heel wants lookin' at."''',
      c("[Sit. Take off your boots.]", "measure")),
    d("teach", '''{n}She squints at you with the one eye, checking whether that was a joke.{/n}
"All right." {n}She points at the stool.{/n} "Sit. Boots off. The right one's goin' to split next, I can hear it from here."''',
      c("[Sit. Take off your boots.]", "measure")),
    nar("measure", '''{n}She kneels. She takes a knotted cord from her pocket, the kind the supply service has used since before there was a Crusade, and measures your foot with it: heel to toe, then round the widest part, then round the instep, and ties a knot for each, and reads the knots with her thumb.{/n}
{n}She does it one-handed, bracing the cord with her bad wrist. She does not hurry. When she is done she keeps her hand round your ankle a moment longer than the measuring needs.{/n}''',
        c("Continue", "knots")),
    d("knots", '''"There. That's you." {n}She holds up the cord, three knots in it, and writes the measure in the back of the ledger.{/n}
"Every soldier who comes through my stores gets measured once. Most of 'em don't know it. I do it by eye, while they're signin'. Takes a second." {n}She coils the cord.{/n} "You, I measured by eye the day you walked into the Logistics Council. Your boots have been right since. I'd sooner hang than issue a soldier wrong." {n}She tucks the cord away.{/n} "And I've found a fault in 'em every week anyway. A strap, a heel, a seam that wanted lookin' at. On purpose."''',
      c('"On purpose?"', "purpose")),
    d("purpose", '''"On purpose." {n}Utterly unrepentant.{/n}
"So you'd keep comin' back to have 'em seen to. Nobody comes to the quartermaster unless somethin' pinches, so I found what pinched." {n}She stands, knees cracking, and dusts her breeches.{/n}
"It's a cheap trick. I'll not pretend otherwise. You're not the only one in Drezen who knows a few." {n}She fetches a pair from the shelf behind her without looking, sets them in front of you, and folds her good arm over her bad one.{/n} "Made to the cord, not the eye. Go on."''',
      c("[Put them on.]", "fit")),
    d("fit", '''{n}The new boots fit snugly at heel and instep. She checks the right heel once more, then stands.{/n} "There. No excuse to come back." {n}She picks up her pen, puts it down, and looks at you.{/n} "Unless you've got a better one. Go on. I've a lad on the wall waitin' for his pair."''',
      c('"I\'ll come back anyway."', flags=(L + "fitted",)),
      c("[Walk out in the new boots, and come back in an hour with the old ones.]", flags=(L + "fitted", L + "came_back"))),
], requires=("trickster.ever", GRIP), forbids=(SIZE,), delay=72)


# --- 28. The inspector (Logistics_4/Cue_0049 8b55625d: her treasury men sent for, to ride with the caravans). ---------

office(INSPECTOR, "The inspector", '"Who\'s the gentleman in the good coat?"', [
    nar("start", '''{n}There is a man in her office in a Nerosyan coat that has never been rained on, sitting in your chair, with your column open on his knee. He is thin and neat and has ink on the side of his right hand, the permanent grey stain of a man who has written more than he has ever carried. His boots are new. There is mud on them to the ankle and no higher.{/n}
{n}Dorgelinda stands behind her own desk with her good hand flat on it, which is how she stands when she would like to be holding something heavier.{/n}''',
        c("Continue", "introduce")),
    d("introduce", '''"Commander. This is one of the treasury men I sent for, to ride with the caravans. Like you agreed at the council." {n}Her voice is perfectly level.{/n} "He rode in with the last one. Saw his first demon on the Kenabres road. Very brave about it, the carters say. Only lost his breakfast the once."
{n}The inspector does not smile. He turns your column toward you.{/n}
"Commander. These issues in your name require an explanation."''',
      c('"Which line?"', "line")),
    nar("line", '''{n}He reads the issues aloud. Dorgelinda brings a corrected tally from the yard and lays it across his open ledger.{/n} "That crate went to the south-wall levy. There's their receipt. My bottle came out of my purse. You can question the issue; you can't call both a gift to the Commander."
{n}The inspector checks the tally, then copies the correction into his report. He keeps the disputed signature in view.{/n}''',
        c("Continue", "carts", requires=(CARTS,), forbids=(REVIEW, ABYSS)),
        c("Continue", "wet", requires=(LATE,), forbids=(CARTS, REVIEW)),
        c("Continue", "abyss", requires=(ABYSS,), forbids=(LATE,)),
        c("Continue", "plain", forbids=(CARTS, LATE, ABYSS)),
        c("Continue", "review", requires=(REVIEW,))),
    d("review", '''"It's the Commander's issue," {n}she says.{/n} "Signed under the Fellows' shortfall, after their tribunal, before three of my clerks. It's in order. I checked it myself. Twice."''',
      c("Continue", "press")),
    d("carts", '''"It's the Commander's issue," {n}she says.{/n} "Signed at the caravan council, before witnesses. It's in order. I checked it myself. Twice."''',
      c("Continue", "press")),
    d("wet", '''"It's the Commander's issue," {n}she says.{/n} "Signed at the tribunal, before the whole Logistics Council and a shackled corporal. It's in order. I checked it myself. Twice."''',
      c("Continue", "press")),
    d("abyss", '''"It's the Commander's issue," {n}she says.{/n} "Signed under my own clerks' record of what went down to the Abyss with the Commander's party. It's in order. I checked it myself. Twice."''',
      c("Continue", "press")),
    d("plain", '''"It's the Commander's issue," {n}she says.{/n} "Signed in my book, in the Commander's hand. It's in order. I checked it myself. Twice."''',
      c("Continue", "press")),
    nar("press", '''{n}"In order." The inspector closes the book on his finger. "Madam Quartermaster, I have ridden a very long way with a great many carts, and I have been told on every one of them that the Commander's stores are 'in order'. I should like to hear it from the Commander."{/n}
{n}He looks at you. So does she. She does not say anything at all, and that is how you know she will stand behind whatever answer comes next, and will not like it if it is stupid.{/n}''',
        c('"It\'s in order. I drew it. I used it. Quietly. You may quote me in Nerosyan."', "quote"),
        c('[Bluff] "It\'s a field accounting practice. Very common in the Worldwound. You\'ll have seen it in the regulations."',
          check=dict(Skill="CheckBluff", DC=22, Success="bluffed", Failure="caught", CommanderOnly=True)),
        c('"Ask the quartermaster. She knows my column better than I do."', "hers")),
    d("quote", '''{n}The inspector writes it down. Word for word. He blots it.{/n}
"'Used. Quietly.'" {n}He looks at the word as if it might be catching.{/n} "Nerosyan will not like that, Commander."
"Nerosyan doesn't have to eat it," {n}Dorgelinda says. It is out before she can stop it. The inspector looks at her. She looks back, one-eyed and entirely unrepentant.{/n}
{n}He closes his book, and stands, and gives the two of you a small, stiff bow that is somehow both an insult and a compliment.{/n}''',
      c("Continue", "gone", flags=(L + "inspector_quoted",))),
    d("bluffed", '''{n}The inspector hesitates. He has, you can see it, read a great many regulations. He is not certain he has read all of them. Nobody has.{/n}
"Field accounting," {n}he repeats, carefully.{/n} "Section...?"
"Nine," {n}says Dorgelinda instantly, without a flicker.{/n} "Paragraph four. Stores issued under operational necessity. It's in the Worldwound supplement. They don't send it to Nerosyan. Too much blood on the pages."
{n}He writes it down. He thanks you both. He leaves.{/n}''',
      c("Continue", "gone", flags=(L + "inspector_bluffed",))),
    d("caught", '''{n}The inspector smiles at last. It is not a pleasant smile.{/n}
"I sat on the committee that wrote the field regulations, Commander. There is no such practice." {n}He closes the book.{/n} "I shall report the line as irregular. I shall also report that the quartermaster checked it twice." {n}He glances at her.{/n} "She is the only thing in this fortress that is in order."
{n}He leaves. Dorgelinda watches the door close.{/n}''',
      c("Continue", "gone", flags=(L + "inspector_caught",))),
    d("hers", '''"I know every issue in that column. I checked the signatures and I kept the receipts." {n}Her good hand stays flat on the desk.{/n} "Nerosyan can have my explanation when it sends us the replacement stores. Till then, they're the Commander's issues. Put that in your report. My name. Spelled right."''',
      c("Continue", "gone", flags=(L + "inspector_hers",))),
    d("gone", '''{n}When he has gone she sits down in the chair he was in, your chair, and puts her face in her good hand for exactly the space of one breath.{/n}
"Hammer and tongs," {n}she says through her fingers.{/n} "I sent for him. I sent for him myself, at the council. Someone experienced, ready to answer for the delivery with his life." {n}She lowers the hand.{/n} "And he is. He'll answer for it to the letter, and he'll put us both in it." {n}A short, tired laugh.{/n} "That's what you get for askin' for honest men, Commander. You get 'em."''',
      c("[Pour her a drink from the bottle that is on no manifest.]", "drink")),
    d("drink", '''{n}She drains the cup and sets it beside the inspector's corrected tally.{/n} "He'll send both. The figures and the suspicion. Let him. I've kept the originals." {n}She pulls paper toward her.{/n} "Go on. I've a letter to write before he gets to Nerosyan."''',
      c("[Leave her to the letter.]")),
], requires=("trickster.ever", COUNTED, INSPECTORS), forbids=(INSPECTOR,), delay=48)


# The closing page after her committed page: what the weekly counts made of the years after.
SCENES.append(scene(P + "epilogue.after_the_war", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}After the war, Dorgelinda still had supplies to issue and veterans coming to her door. The new clerks quickly learned to count twice.{/n}''',
        paragraphs=(
            p("{n}There was a boot shop, in the end, on a street near the Drezen gate, with a sign that said STRANGLEHOLD'S BOOTS. THEY FIT. The jokesters were never allowed in. The Commander was measured there once a month, whether the Commander's feet had grown or not.{/n}", requires=(L + "boot_shop",)),
            p("{n}The Commander's postwar requisitions still came to Dorgelinda. She sent a clerk back whenever a quantity was missing, rank or no rank.{/n}", requires=(L + "joke_audited",)),
            p('{n}The Commander had promised to find Dorgelinda when the war was over. On returning to Drezen, the Commander found her issuing boots at the stores. That evening she pulled them through the inner door by the collar. The next morning she went out to count the carts.{/n}', requires=('dorgelinda.ledger.signed_after',), forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed')),
            p("{n}Every pair of boots the Commander wore from then on came from the same shelf, and fitted, and was entered in her book.{/n}", requires=(L + "fitted",)),
            p("{n}Twelve soldiers from a plague ward in Drezen outlived the war. None of them ever learned whose column their potions were written in.{/n}", requires=(L + "ward_seen",)),
            p("{n}On the nights she chose, Dorgelinda opened the door behind the stores and drew the Commander inside. Before breakfast she handed back their coat. The arrangement stayed as small as she had said.{/n}", requires=('dorgelinda.ledger.narrowed',), forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended')),
            p("{n}Dorgelinda kept the Commander's company private. Outside her rooms she asked only about supplies; the Commander left the other relationships unspoken. She never opened her door to them.{/n}", requires=('dorgelinda.ledger.unblessed',), forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_unmended')),
            p('{n}The quarrel about the seal remained unresolved. Dorgelinda continued supplying the army, but private visits stopped. The Commander saw her across the office desk, with a clerk waiting for the next requisition.{/n}', requires=(L + "quarrel_unmended",)),
            p('{n}When there was trouble with a requisition, the Commander heard it from Dorgelinda before Nerosyan did. The sergeant still left the office whenever their voices rose.{/n}', requires=('dorgelinda.ledger.quarrel_mended',), forbids=('dorgelinda.ledger.quarrel_unmended',)),

            p("{n}On the nights she chose, Dorgelinda opened the door behind the stores and drew the Commander inside. Before breakfast she handed back their coat. The arrangement stayed as small as she had said.{/n}", requires=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.quarrel_unmended',)),
            p("{n}Dorgelinda kept the Commander's company private. Outside her rooms she asked only about supplies; the Commander left the other relationships unspoken. She never opened her door to them.{/n}", requires=('dorgelinda.ledger.unblessed', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.narrowed', 'dorgelinda.ledger.quarrel_unmended')),
            p('{n}The Commander had promised to find Dorgelinda when the war was over. On returning to Drezen, the Commander found her issuing boots at the stores. That evening she pulled them through the inner door by the collar. The next morning she went out to count the carts.{/n}', requires=('dorgelinda.ledger.signed_after', 'dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended'), forbids=('dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed')),
            p('{n}The quarrel about the seal remained unresolved. Dorgelinda continued supplying the army, but private visits stopped. The Commander saw her across the office desk, with a clerk waiting for the next requisition.{/n}', requires=('dorgelinda.ledger.quarrel_cold',), forbids=('dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended')),
        ))],
    requires=("trickster.ever", COMMITTED), forbids=("sacrifice", CLOSED),
    ForbidOverrides={"sacrifice": "trickster.commander_back"}, last=6, Relationship="dorgelinda"))


SCENES.append(scene(P + "epilogue.ruled_off", "", "DorgelindaEpilogue", 6, "", [
    nar("page", '''{n}Dorgelinda returned the Commander's dented cup to the shelf above her desk. Requisitions came through a clerk from then on. She continued supplying the crusade, but the door to her rooms stayed shut to the Commander.{/n}''')],
    requires=("trickster.ever", COMMITTED, CLOSED), last=6, Relationship="dorgelinda"))


# --- 29. Cold iron and wool (Chapter 4, PP5). The party went down into the Abyss on the crusade's own stores (the stocktake's
# "issued to the Commander's party"). No courier crosses the planes: she packed the crate before they left, and it is opened
# at the first camp down there (the outpost the party sets up, c4 Nexus_Camp/HeraldLetsGo Cue_0018 ef9681784d2b00247b35f81e4cfbc167).
# Her reason to write is her trade: the veteran-quartermaster argument is native (Logistics_2/Cue_0080 867f1304, about her);
# her personal fitting scene (the_right_size) is authored. The
# consequence is read by receipts (Chapter 5): the wool comes back to her desk as this Commander spent it.

SCENES.append(scene(WOOL, "Cold iron and wool", "Dorgelinda", 4, "", [
    nar("crate", '''{n}In the Abyss camp, you open a crate your party brought from Drezen. Cold-iron arrowheads lie counted in straw. Under them are twelve pairs of grey wool socks, rolled in twos. A note in Dorgelinda's square hand is tied to the top pair.{/n}''',
        c("Continue", "note_heel", requires=(FITTED,)),
        c("Continue", "note", forbids=(FITTED,))),
    d("note", '''"Commander.
Cold iron's for the demons. Wool's for you lot. Wet feet'll put a soldier out of the line quicker than anythin' with horns, and I'll not have it said my stores sent you down there with one pair each.
Twelve pair. I counted. If you come back with fewer I'll want to know whose feet they're on.
D. Stranglehold, Logistics."''', *WOOL_CHOICES),
    d("note_heel", '''"Commander.
Cold iron's for the demons. Wool's for you lot. Wet feet'll put a soldier out of the line quicker than anythin' with horns, and I'll not have it said my stores sent you down there with one pair each.
Twelve pair. I counted. If you come back with fewer I'll want to know whose feet they're on.
D. Stranglehold, Logistics."
{n}Under the signature, smaller, squeezed in as if she argued with herself about it first:{/n} "Mind the right heel."''', *WOOL_CHOICES),
], requires=("trickster.ever", COUNTED), forbids=(CLOSED, WOOL), delay=24, last=4, optional=True,
    Relationship="dorgelinda", Chapters=[4], Remote=True, Kind="letter"))


# Her epilogue remembers what the weekly counts made of the line.
EPILOGUE_PARAGRAPHS = {
    P + "epilogue.committed": (
        (TRUE_BOOKS, '{n}The ledgers sent to Nerosyan were the true ones, disputed issues and all. The lords resented the admission. Among the ranks, it earned the Commander a few defenders who had no patience for court gossip.{/n}'),
        (CLEAN_COPY, "{n}The copy she sent to Nerosyan during the war balanced to the copper, in the Commander's hand. It concealed the disputed issues from this inquiry. She kept the original against a second demand for the books.{/n}"),
        (HER_NAME, "{n}After the war Dorgelinda went to Nerosyan to answer for the disputed issues bearing her name. She took the original receipts and argued over every cart and crate. The Commander received a copy of the inquiry's questions in her small, hard hand.{/n}"),
        (RECEIPT, "{n}She kept a pencilled receipt folded small inside her coat for the rest of her life: Commander, returned. Received in good order. It remained in her coat after the Commander had actually returned to Drezen.{/n}"),
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

    _round2_partners(payload)
    from storylines.dorgelinda_round3 import integrate as round3
    round3(payload)

    # Authored polish: retained account and private terms, after all old paragraph slots.
    by_id[P + "epilogue.committed"]["Nodes"][0]["Paragraphs"].extend((
        p("{n}The first disputed account had balanced before the war ended. She kept the Commander's confession with its receipts; no clerk was allowed to mistake it for missing stock.{/n}", requires=('dorgelinda.trickster.cost.told_all',), forbids=()),
        p('{n}The original issue remained unresolved. She kept its receipts together and still demanded an explanation whenever the Commander brought another requisition.{/n}', requires=(), forbids=('dorgelinda.trickster.cost.told_all',)),
        p("{n}When the Commander returned to Drezen, she finished the day's dispatches before taking their hand. Behind the stores she drew them close, kissed them hard and shut her own door. At dawn she was back in the yard.{/n}", requires=('dorgelinda.ledger.quarrel_mended',), forbids=('dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed')),
        p("{n}When the Commander returned to Drezen, she finished the day's dispatches before taking their hand. Behind the stores she drew them close, kissed them hard and shut her own door. At dawn she was back in the yard.{/n}", requires=(), forbids=('dorgelinda.ledger.quarrel_cold', 'dorgelinda.ledger.quarrel_mended', 'dorgelinda.ledger.quarrel_unmended', 'dorgelinda.ledger.narrowed', 'dorgelinda.ledger.unblessed')),
    ))


# Round 2: receipts for already stated supply consequences. These are authored
# logistics extensions, not native verdict changes or additional romance prices.
ALLOTMENT_LOST = L + "allotment_lost"
POWDER_RESTORED = L + "powder_restored"
WINE_OWED = L + "wine_owed"
BILL_OWED = L + "cellar_bill_owed"
CELLAR_PAID = L + "cellar_settled"
REQUISITIONS = L + "requisitions_applied"
OTHER_LOVER = L + "other_lover"


def _round2_receipts():
    from storylines.dorgelinda_trickster import SCENES as office_scenes
    by = {s["Id"]: s for s in office_scenes + SCENES}
    def node(sid, nid):
        return next(n for n in by[sid]["Nodes"] if n["Id"] == nid)

    # The old scene remains available in all its old histories. A receipt also
    # protects resources if a conversation is interrupted before completion.
    first = node(QUARREL_SCENE, "start")["Choices"][0]
    first.update(Next="grain_receipt", Set=[ALLOTMENT_LOST],
                 Forbids=[ALLOTMENT_LOST], Crusade=dict(Resource="Materials", Amount=-150))
    node(QUARREL_SCENE, "start")["Choices"].append(
        c("[Read the cut allotment.]", "friends", requires=(ALLOTMENT_LOST,)))
    by[QUARREL_SCENE]["Nodes"].append(nar("grain_receipt",
        "{n}She enters the cancelled grain issue beside the powder and boots: fifty from the food allocation, a hundred and fifty in military stores. The treasury notice is pinned to the loss.{/n}",
        c("[Read the notice.]", "friends", crusade=("Finances", -50))))

    for sid, nid in ((QUARREL_SCENE, "written"), (COLD_COUNTS, "letter")):
        old = node(sid, nid)["Choices"][0]
        old.update(Requires=[ALLOTMENT_LOST], Forbids=[POWDER_RESTORED],
                   Crusade=dict(Resource="Materials", Amount=50))
        old["Set"].append(POWDER_RESTORED)
        # Old saves can reach the delayed repair without the newly added loss.
        # Preserve their welcome and dialogue, but never mint replacement stock.
        node(sid, nid)["Choices"].append(c(old["Text"], old["Next"],
            flags=tuple(f for f in old["Set"] if f != POWDER_RESTORED), requires=(POWDER_RESTORED,)))
        node(sid, nid)["Choices"].append(c(old["Text"], old["Next"],
            flags=tuple(f for f in old["Set"] if f != POWDER_RESTORED), forbids=(ALLOTMENT_LOST, POWDER_RESTORED)))

    # Existing failed/successful checks retain their positions. Leaving a bill
    # owing is selectable at zero funds; payment never earns affection.
    for nid, flag, amount in (("jest_won", WINE_OWED, 50), ("jest_lost", BILL_OWED, 200)):
        old = node(REVELS, nid)["Choices"][0]
        old["Text"] = "[Leave the bill owing.]"
        old["Set"].append(flag)
        node(REVELS, nid)["Choices"].append(c(
            '[Authorize %s from the crusade treasury.]' % amount, "end",
            flags=(CELLAR_PAID,), crusade=("Finances", -amount)))
    won = node(REVELS, "jest_won")
    won["Text"] = won["Text"].replace("You get the wine.", "Fifty for the wine. You get that.")
    lost = node(REVELS, "jest_lost")
    lost["Text"] = '"Nice try. Two hundred still owing." {n}She writes the full bill beneath your failed jest.{/n} "Crusade treasury, on your order. Pay it now, or I keep it here till you do. The surgeons get their wine first."'

    grain = node(QUARREL_SCENE, "grain_receipt")
    grain["Choices"][0]["Set"] = [L + "grain_allotment_lost"]
    grain["Choices"][0]["Forbids"] = [L + "grain_allotment_lost"]
    grain["Choices"].append(c("[Read the notice.]", "friends", requires=(L + "grain_allotment_lost",)))
    node(QUARREL_SCENE, "start")["Choices"][-1]["Next"] = "grain_receipt"

    # Existing surplus/requisition outcomes always outrank memories of crisis.
    for sid, nid in ((RECEIPTS, "door"),):
        old = node(sid, nid)
        old["Text"] = "{n}Dorgelinda has the party's Abyss issue open beside the current council returns. A clerk waits with a stack of delivery receipts. She waves him out when she sees you.{/n}"
    # The meal can follow donations too: hunger here is her missed meal,
    # not an erased council recovery. Keep the same player responses/results.
    for answer in node(RATIONS, "start")["Choices"]:
        answer["Forbids"].append(CONSCIENCE)
    node(RATIONS, "start")["Choices"].append(c("Continue", "provisioned", requires=(CONSCIENCE,)))
    by[RATIONS]["Nodes"].append(d("provisioned",
        '''"The donations are in. Plenty in the warehouses." {n}She nudges the bowl toward the young levy.{/n} "He missed the mess call fetchin' kit for the wounded. I gave him mine. I've been countin' carts since, and the cook's not waitin' on me. Don't make a council out of it."''',
        *EAT_CHOICES))
    methods = by[P + "after.fellows_methods"]
    for answer in methods["Nodes"][0]["Choices"]:
        answer["Requires"] = [REQUISITIONS if f == HARD_MEASURES else f for f in answer["Requires"]]
        answer["Forbids"] = [REQUISITIONS if f == HARD_MEASURES else f for f in answer["Forbids"]]
    council = by[COUNCIL]
    old = node(COUNCIL, "think")["Choices"][0]
    old.update(Next="woljif_opinion", Requires=["woljif.in_party"])
    node(COUNCIL, "think")["Choices"].append(c("Continue", "lann_dispatch", forbids=("woljif.in_party",)))
    council["Nodes"].extend((
        d("woljif_opinion", '''"Woljif's scheme at the table? He can find us stores. I'll still check the weights myself."''', c("Continue", "lann_dispatch")),
        nar("lann_dispatch", "{n}She turns to the ration figures.{/n}",
            c("Continue", "lann_opinion", requires=("lann.in_party",)),
            c("Continue", "others", forbids=("lann.in_party",))),
        d("lann_opinion", '''"Lann's careful with grain. Knows what hunger does. My drivers need enough to haul, though. I'll count their rations before I stretch anythin'."''', c("Continue", "others")),
    ))

    # Record actual harm separately from the existence of an optional scene.
    for target in ("keep", "sort"):
        node(WEIGHT, target)["Choices"][0]["Set"].append(L + "barrels_kept")
    returned = node(WEIGHT, "returned_all")
    returned["Choices"][0]["Requires"] = [DIRTY]
    returned["Choices"].append(c("[Help load the returning cart.]",
        flags=(L + "all_barrels_returned",), forbids=(DIRTY,)))
    returned["Text"] = '"All of it. Aye." {n}She orders the barrels reloaded and crosses their weights off the proposed issue.{/n} "A hundred and fifty in stores I won\'t be handin\' out. If we\'ve booked it in the reserve, I\'ll strike it out again. The depot gets the true count."'
    for nid in ("cathedral", "plain"):
        old = node(FAITH, nid)["Choices"][0]
        old.update(Next="harm", Requires=[L + "harm_done"])
        node(FAITH, nid)["Choices"].append(c("Continue", "restrained", forbids=(L + "harm_done",)))
    by[FAITH]["Nodes"].extend((
        d("harm", '"Those stores came out of somebody\'s house or depot. We sent them to the front. Doesn\'t put them back where we took them from." {n}She turns the hammer in her palm.{/n} "The folk back there can curse me. I\'ll not tell \u2019em they owe me thanks."', c("Continue", "hammer")),
        d("restrained", '"We could have taken more. We didn\'t." {n}She studies the hammer.{/n} "Still got wounded lads comin\' through my stores. I\'d rather find their kit than spend the afternoon askin\' a priest whether I\'m forgiven."', c("Continue", "hammer")),
    ))


_round2_receipts()

office(L + "cellar_settlement", "The remaining bill", '"The cellar bill, Quartermaster."', [
    d("bill", '"Still here." {n}She brings the slate out of a drawer.{/n} "The surgeons\' wine first. No jokes this time."',
      c("[Authorize two hundred from the crusade treasury.]", flags=(CELLAR_PAID,),
        requires=(BILL_OWED,), crusade=("Finances", -200)),
      c("[Authorize fifty for the wine.]", flags=(CELLAR_PAID,), requires=(WINE_OWED,),
        forbids=(BILL_OWED,), crusade=("Finances", -50)),
      c("[Leave it owing.]", abort=True)),
], requires=("trickster.ever", "dorgelinda.present_now", REVELS), forbids=(CELLAR_PAID,), chapters=(5,),
   RequiresAnyGroups=[[WINE_OWED, BILL_OWED]])


def _round2_partners(payload):
    """Route-local questions read the existing open, earned romantic entitlement.

    Naming is the Commander's disclosure, not knowledge obtained from gossip,
    a vision, or the stores ledger. No participant is brought into the room.
    """
    import copy
    from storylines.household import PARTNERS
    by = {s["Id"]: s for s in payload["Scenes"]}
    other = by[OTHERS]
    nodes = {n["Id"]: n for n in other["Nodes"]}
    derived = payload.setdefault("Derived", {})
    partners = [rel for rel in PARTNERS if rel not in ("dorgelinda", "ember", "aivu")]
    native_romances = {"arueshalae": L + "native_arueshalae_open", "camellia": "camellia.romance",
                       "galfrey": "galfrey.romance_active", "wenduag": "wenduag.romance_active"}
    # Native Arueshalae has no shared romance reader in this export. Bind it
    # here without altering her route. Native breakup completes this parent;
    # the first-strike Fail child is a warning, not a persistent failure reader.
    payload.setdefault("Etudes", {})[L + "native_arueshalae"] = "d6a90c0f6536331498cafa1f3195d886"
    derived[L + "native_arueshalae_open"] = [[L + "native_arueshalae"]]
    for rel in partners:
        key = L + "current_other." + rel
        derived[key] = [[rel + ".harem.eligible"]]
        if rel in native_romances:
            derived[key].append([native_romances[rel]])
        payload.setdefault("DerivedOpenRoutes", {})[key] = [rel]
    derived[OTHER_LOVER] = [[L + "current_other." + rel] for rel in partners]
    derived[L + "harm_done"] = [[REQUISITIONS], [L + "barrels_kept"], [DIRTY]]
    payload.setdefault("SeenCues", {})[REQUISITIONS] = ["1576c91c20be9064083a3181abb354a9"]
    nodes["start"]["Text"] = '"Who else, Commander?" {n}She sets your dented cup beside a small grey notebook.{/n} "I want it from you. The sentries can keep their wagers. We\'ve had a night; that doesn\'t answer this."'
    # Both legacy denials follow actual history. The labelled lie cannot create
    # evidence on a solo run; the unlabelled denial cannot obtain a false sole yes.
    for answer in nodes["says"]["Choices"]:
        if answer["Next"] in ("nobody", "lie"):
            answer["Forbids"].append(OTHER_LOVER)
            answer["Next"] = "nobody"
    nodes["says"]["Choices"].append(c('[Lie] "Nobody else."', "lie", requires=(OTHER_LOVER,)))
    nodes["start"]["Choices"][0]["Text"] = '"Ask me yourself."'
    nodes["says"]["Text"] = '"Are there others? I want the names if there are." {n}She pushes the cup toward you, then leaves her hand beside it.{/n}'
    for answer in nodes["says"]["Choices"]:
        if answer["Next"] in ("bother", "sign"):
            answer["Requires"].append(OTHER_LOVER)
        elif answer["Next"] == "nobody":
            answer["Text"] = '"Nobody else. Not one."'
    nodes["lie"]["Text"] = '"Nobody?" {n}She holds your cup between her hands.{/n} "Say it plain, Commander. I\'ll take an honest answer I don\'t like. If that was a lie, give me the cup back. I\'ll not keep a lover who promises me I\'m the only one and won\'t tell me the truth."'
    nodes["lie"]["Choices"][0]["Text"] = "[Admit the lie and put her cup in her hand.]"
    nodes["bother"]["Text"] = '"Aye, it matters." {n}She sets the cup down.{/n} "I don\'t want somebody turnin\' up in my stores with your seal and a claim on me. And I don\'t want promises you can\'t keep. Names first. Then I decide."'
    nodes["sign"]["Text"] = '"Then tell me what you\'re signin\' for." {n}She leaves her good hand beside your cup.{/n} "The night was ours. I\'m askin\' what comes after it."'
    nodes["named"]["Text"] = '"Tell me each name yourself. No clerk, no sentry." {n}She puts the pen aside and faces you.{/n}'
    nodes["named"]["Choices"][0]["Next"] = "names.0"
    nodes["named"]["Choices"][0]["Text"] = "[Tell her who you are with.]"
    response = '"Right. Nobody draws on my stores on your seal but you. Nobody else sets foot in my rooms. If that changes, I hear it from you." {n}She holds out her good hand.{/n} "Shake on it, if that\'s what you want too."'
    def name_answer(rel):
        # This answer supplies information; it does not summon the named woman.
        names = {"tirabade": ["Anevia", "Irabeth"],
                 "minagho_chivarro": ["Minagho", "Chivarro"]}.get(rel, [PARTNERS[rel][1]])
        return "[Give " + " and ".join(name + "'s name" for name in names) + ".]"

    added = []
    for rel in partners:
        name = PARTNERS[rel][1]
        nxt = "names_done"
        words = {
            "nocticula": '"A demon lord. Hammer and tongs." {n}Her jaw tightens.{/n} "No presents in my stores. No favours called in through you. If she wants somethin\', she asks me and I can say no."',
            "shamira": '"The demon from Alushinyrra? She\'ll not have a key, or an issue on your seal. Tell her that before she comes askin\'."',
            "jerribeth": '"A demon with a taste for soldiers. Keep her out of my ranks and out of my rooms. I mean it, Commander."',
            "galfrey": '"Royal company." {n}She lets out a short breath.{/n} "No orders from her household about mine. I answer for the army\'s stores. My bed isn\'t an appointment she hands out."',
            "anevia": '"She\'ll know how to keep a private door private. Tell her this one\'s mine."',
            "irabeth": '"I\'ll not have her put in the middle of a lie. What you promise her, you keep. Same as what you promise me."',
        }.get(rel, '"Aye." {n}She considers the name before nodding.{/n} "Your time with her is yours to arrange. My rooms and my stores stay mine."')
        added.append(d("named." + rel, words, c("Continue", nxt)))
    added.append(nar("names.0", "{n}She listens while you name the other relationships you have chosen.{/n}"))
    added.append(d("names_done", response, c("[Take her hand.]", "shaken")))
    # Acyclic, ordered disclosure: show only the next actual lover, never
    # empty checklist pages or a loop through the conversation.
    ordered_keys = [L + "current_other." + rel for rel in partners]
    for index, rel in enumerate(partners):
        replies = next(n for n in added if n["Id"] == "named." + rel)
        replies["Choices"] = [c(name_answer(r), "named." + r,
            requires=(ordered_keys[j],),
            forbids=tuple(ordered_keys[index + 1:j])) for j, r in enumerate(partners) if j > index]
        replies["Choices"].append(c("[Hear her answer.]", "names_done",
            forbids=tuple(ordered_keys[index + 1:])))
    opening = next(n for n in added if n["Id"] == "names.0")
    opening["Choices"] = [c(name_answer(r), "named." + r,
        requires=(ordered_keys[j],), forbids=tuple(ordered_keys[:j])) for j, r in enumerate(partners)]
    opening["Choices"].append(c("[There are no other names.]", "names_done", forbids=tuple(ordered_keys)))
    other["Nodes"].extend(added)
    # The existing sole arrangement explicitly asks for renewed disclosure.
    # This is its collection, not a new exclusivity demand or a reconciliation.
    follow = copy.deepcopy(other)
    follow["Id"] = L + "changed_columns"
    follow["Title"] = "What changed"
    follow["Entry"] = '"There\'s someone else. You said to tell you first."'
    follow["Requires"] = ["trickster.ever", "dorgelinda.present_now", COMMITTED, L + "sole_line", OTHER_LOVER]
    follow["Forbids"] = [CLOSED, follow["Id"]]
    follow["DelayHours"] = 0
    follow["Nodes"][0]["Text"] = '"Aye. I did." {n}She sets your cup between you.{/n} "Glad you came yourself. Now tell me who. Then I\'ll tell you what I can have."'
    follow["Nodes"][0]["Choices"] = [c("[Name the other relationship.]", "terms"), c('"I won\'t name her."', "narrow")]
    # Only the new follow-up is reduced; all saved original nodes stay intact.
    follow_nodes = {n["Id"]: n for n in follow["Nodes"]}
    reachable, pending = set(), [follow["Nodes"][0]["Id"]]
    while pending:
        nid = pending.pop()
        if nid in reachable:
            continue
        reachable.add(nid)
        pending.extend(a["Next"] for a in follow_nodes[nid]["Choices"] if a.get("Next"))
    follow["Nodes"] = [n for n in follow["Nodes"] if n["Id"] in reachable]
    payload["Scenes"].append(follow)
