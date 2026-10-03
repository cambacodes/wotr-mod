"""Delamere, after the waking: the courtship between the stag and the huntress (delamere_trickster holds the device).

Every beat engages her canon: the fifty-three souls to a village and her contempt for cities (Kyado_main_dialogue/Cue_0034,
Cue_0038), the stag she hunted three days and whose meat she gave to Erastil (DelamereInTomb/Cue_0042 20f0dfa4), her
pride, her priesthood and her hatred of cities (Cue_0039 ac70a123), her refusal to be ordered about (Cue_0032 7bf73785)
and her fear of undeath (Cue_0040 50a96c40), the feasting table Zanedra's cult made of her sarcophagus
(TombOfDelamere_BookEvent/Cue_0002), Kyado's fear and his broken oath to her temple (Kyado_main_dialogue/Cue_0057).

Delivery: pages that arrive at a rest (she finds the Commander: a huntress can find anyone with a limp), one letter in
the Abyss, and the second hunt, which is physical on Kyado's temple list in Chapter 3 when he is alive and prior, and a
page otherwise. Three pivotal choices carry consequences into the commit, the late pages and the epilogue:
the refugee count (she would drive families out to found villages, as she did in life), Kyado's judgment, and the truth
about who woke her.
"""
import copy

from storylines.delamere_trickster import HUNT_POSTPONED   # polish r4: the late page remembers the postponed hunt

from story_format import c, p, scene
from storylines.delamere_trickster import BARK_ANSWERED   # PP10: the Commander's answer cut into the bark (Chapter 4)
from storylines.delamere_trickster import STORYTELLER_SUPPLIES, WOKE_DREZEN   # PP10: the bark's carrier; the Drezen waking
from storylines.delamere_trickster import (BOW_HELD, BOW_ITEM, BOW_RETURNED, CAUGHT, CLOSED, COMMITTED, CURSED_BOW_HELD,
                                           CURSED_BOW_ITEM, DECLINED, FIRST_FROST, HUNT_OWED, INITIATED, KYADO_DEAD,
                                           KYADO_JUDGED, KYADO_SPOKEN, LIMP, P, RAN_FAR, RAN_SHORT, RETURNED, SAID_AGAIN,
                                           SAID_FINISH, SAID_MISSED, SECOND_HUNT, STAG_TOLD, VILLAGE_CLANS, LIAR, CLAIMED, VILLAGE_FORCED,
                                           VILLAGE_GIVEN, VILLAGE_REFUSED, YEW_BOW, dl, kyado, nar)
from storylines.delamere_trickster import temple as _temple, visit as _visit

SCENES = []


def temple(*args, **kw):
    _temple(*args, into=SCENES, **kw)


def visit(*args, **kw):
    _visit(*args, into=SCENES, **kw)


COUNTED = P + "counted"
FIRST_MEAT = P + "first_meat"
MEAT_GATE = P + "meat.gate"
MEAT_TABLE = P + "meat.table"
TABLE = P + "feasting_table"
KYADO_MOURNED = P + "kyado.mourned"
ZANEDRA_DEAD = P + "zanedra.told_dead"
ZANEDRA_FLED = P + "zanedra.told_fled"
BLOOD = P + "red_blood"
TRUTH = P + "told_truth"
LIED = P + "lied_erastil"
BOTH = P + "told_both"
CONFESSED = P + "confessed"
BARK = P + "bark_letter"
CALLED = P + "called_her"
TRACKED = P + "tracked_her"
VILLAGE_SEEN = P + "village_seen"
VILLAGE = (VILLAGE_GIVEN, VILLAGE_FORCED, VILLAGE_REFUSED, VILLAGE_CLANS)
COUNT_LATE = P + "counted_after_the_abyss"   # Q6 (BEL): the count was made in Chapter 5, after the Abyss, not before it
ZANEDRA_LOST = P + "zanedra.told_lost"        # PP10: "I don't know" no longer gets her "West." (that answer's choice is retired)


# --- 1. Fifty-three (she comes to Drezen for the first time) ----------------------------------------------------------

visit(P + "woken.count", "Fifty-three", [
    nar("gate", '''{n}The sergeant of the south gate sends for you in the middle of the afternoon, and will not say why except that it is "a woman, Commander, with a bow, and she's counting."{/n}
{n}She is standing on the wheel of a supply wagon at the edge of the refugee camp, where Sarkorian families and the last of the Kenabres wagons have been packed in under the wall since the city fell to you. She wears her old grave-leathers over a borrowed smock. Her lips are moving. Her eyes go from fire to fire to fire, and she does not look down when you limp up beside the wheel.{/n}''',
        c("Continue", "number")),
    dl("number", '''"Four hundred and eleven." {n}She says it the way a surgeon names a wound.{/n} "Four hundred and eleven souls in the smoke of one another's fires, under one wall, and not one of them knows the name of the man sleeping next to him. I asked. I asked twenty of them. Not one."
{n}She steps down off the wheel.{/n} "This is what your crusade calls a refuge, stag. In my day we would have called it kindling."''',
        c('"They lost their homes. This is what\'s left."', "left"),
        c('"You walked all the way to Drezen to count my refugees?"', "walked")),
    dl("left", '''"I know what they lost. I lived in it. I walked those hills when they were Sarkoris and not a sore." {n}She looks north, toward where the sky is always the wrong colour.{/n} "The demons took their villages. You have given them back a city instead. I am not sure that is the kinder gift."''',
        c("Continue", "rule")),
    dl("walked", '''"I walked to Drezen because you live in it, and I said I would come and see what kind of animal lives in your walls." {n}Her nose wrinkles.{/n} "The kind that lives in its own dung, it turns out. I have smelled bear dens that were more particular."''',
        c("Continue", "rule")),
    dl("rule", '''"Hear me. When I was alive the first time, I walked the villages every season and I counted. Any village over fifty-three souls, I came to at the new moon, and I chose who would go and found the next one. Families wept. Some cursed me. One of them waited for me on the road with his brothers and knives."
{n}She says it without apology, and without pride either.{/n} "Not one village of mine ever rotted from the inside."''',
        c('"Why fifty-three?"', "why"),
        c('"That sounds cruel."', "cruel"),
        c('"What happened to the man with the knives?"', "knives")),
    dl("why", '''"Because a hunter can know fifty-three." {n}She holds up her scarred hand and closes it, finger by finger, as if around names.{/n} "Their fathers. Their debts. What they did in the bad winter and who they did it to. Past that you are counting strangers, and a stranger can do anything, because nobody will know it was him. That is what a city is, stag. A place where nobody knows it was him."''',
        c("Continue", "want")),
    dl("cruel", '''"It was." {n}She does not even pause over it.{/n} "Cruel on the day, and kind for a lifetime. A child who is sent off with her family to clear a new field grows up knowing every face in her village. A child who stays grows up in a town, and learns to lock her door." {n}Her mouth tightens.{/n} "I never locked a door in my life. I would have been ashamed to."''',
        c("Continue", "want")),
    dl("knives", '''"His knives did not find me. My arrows found him." {n}She touches her ribs, lightly, the way another woman would touch a ring.{/n} "His brothers carried him home, and the next spring they came to me and asked where they should build. I told them. They built there. It is under the Wound now, I suppose. Everything is."''',
        c("Continue", "want")),
    dl("want", '''"So." {n}She jerks her chin at the camp.{/n} "Give me the ones who will come. There are clearings below my temple where the Kellid villages stood before your crusade had a name. The soil is still good. The woods will feed a village if someone who knows the woods leads it, and I know them better than the deer do."''',
        c('"There are demons in those woods."', "demons"),
        c('"And the ones who won\'t come?"', "unwilling")),
    dl("demons", '''"There were marauders in my day, and trolls, and a winter wolf the size of a byre. I hunted them." {n}She shrugs one shoulder.{/n} "Demons bleed. I have seen your soldiers make them do it. I am better with a bow than your soldiers."''',
        c("Continue", "unwilling")),
    dl("unwilling", '''"The ones who will not come." {n}She considers the camp again, fire by fire.{/n} "In my time I did not ask. I chose, at the new moon, and the ones I chose went, and they hated me for a year and blessed me for forty. I would do it again today. I would do it to this camp by morning, if you gave me the word."
{n}She looks at you, and waits. It is not a request. It is the old law, standing in front of you in a borrowed smock, asking whether it still applies.{/n}''',
        c('[Give her the families who volunteer, with tools and seed from the stores] "Take the ones who want to go. Not one family more."', "given",
          crusade=("Materials", -100), flags=(COUNTED, VILLAGE_GIVEN)),
        c('[Give her the word] "Choose your fifty-three. The rest go where you send them."', "forced",
          alignment=("Evil", 1), flags=(COUNTED, VILLAGE_FORCED)),
        c('"No. They stay behind the walls. The woods aren\'t safe, and you\'re one bow."', "refused", flags=(COUNTED, VILLAGE_REFUSED)),
        c('[Persuasion: count them another way] "Drezen isn\'t one city. It\'s forty villages sharing a wall. Give every barracks an elder who knows fifty-three names, and count it that way."',
          check=dict(Skill="CheckDiplomacy", DC=24, Success="clans", Failure="clans_fail", CommanderOnly=True))),
    dl("clans_fail", '''"Words." {n}She says it the way she would say "mice".{/n} "You talk like a trader who has sold the same horse twice. A city is a city, whatever you call it at the gate." {n}She folds her arms.{/n} "So, stag. The camp. What will it be?"''',
        c('[Give her the families who volunteer, with tools and seed from the stores] "Take the ones who want to go. Not one family more."', "given",
          crusade=("Materials", -100), flags=(COUNTED, VILLAGE_GIVEN)),
        c('[Give her the word] "Choose your fifty-three. The rest go where you send them."', "forced",
          alignment=("Evil", 1), flags=(COUNTED, VILLAGE_FORCED)),
        c('"No. They stay behind the walls. The woods aren\'t safe, and you\'re one bow."', "refused", flags=(COUNTED, VILLAGE_REFUSED))),
    dl("given", '''"Volunteers." {n}The word tastes strange to her.{/n} "In my day nobody volunteered to leave a hearth. We shall see what kind of village volunteers make." {n}She watches your quartermaster's clerk being sent for, and the first family already gathering its bundles by the gate, and something in her face eases.{/n} "Three families. Maybe four. It is enough to start a hearth. I will teach them the woods. The woods will teach them the rest."''',
        c("Continue", "leave")),
    dl("forced", '''"Good." {n}No triumph in it. The satisfaction of a tool fitted to the hand it was made for.{/n} "I will choose at the new moon. They will hate me. They will live." {n}She is already looking over the camp again, and you can see her choosing: this family, not that one; the widow with three boys, yes; the old man who coughs, no.{/n} "You have not done an easy thing, stag. Nobody will thank you for it. Count the hearths smoking in those clearings at midwinter, and the children not buried in spring. That is all the thanks my law ever got."''',
        c("Continue", "leave")),
    dl("refused", '''"One bow." {n}She repeats it with something close to contempt, and then, slowly, something close to respect.{/n} "You say no to me to my face, and you do not dress it up. Good. The last man who told me no had brothers and knives." {n}She looks at the wall, the camp, the smoke.{/n} "Keep them, then. Keep your hive. But when the rot starts in it, and it will, remember who told you where to cut."''',
        c("Continue", "leave")),
    dl("clans", '''"Forty villages." {n}She stares at you.{/n} "Sharing a wall."
{n}For a while she says nothing at all. You can see her walking it through: an elder to every barracks, a name to every face, a sin for every name.{/n} "That is the most shameless thing I have heard a living soul say since I woke. You have taken Erastil's law and cut it to fit a city like a tailor cuts a dead man's coat." {n}Her mouth twitches.{/n} "I will choose the elders. All forty. Myself."''',
        c("Continue", "leave", flags=(COUNTED, VILLAGE_CLANS), alignment=("Chaotic", 1))),
    dl("leave", '''{n}She picks up her bow from where it leans against the wagon wheel and slings it.{/n} "I will come again, stag. Do not make me come looking for you. You leave a trail a child could follow." {n}She glances down at your leg.{/n} "My doing, I know. I am not sorry. Walk on it. It heals crooked either way, but it heals stronger if you walk."''',
        c("[Watch her go out through the gate.]")),
], requires=("trickster.ever", RETURNED), forbids=(CLOSED, COUNTED), delay=24, chapters=(3,))

# Quality pass Q6 (BEL): the same count made after the Abyss. Its choices also set COUNT_LATE, so "what came of the count"
# (woken.village, which reports a season of the Commander's absence) never plays for a count made after the return.
_count_late = copy.deepcopy(SCENES[-1])
_count_late.update(Id=P + "woken.count_late", MinChapter=5, MaxChapter=5, Chapters=[5])
for _node in _count_late["Nodes"]:
    for _choice in _node["Choices"]:
        if COUNTED in _choice["Set"]:
            _choice["Set"].append(COUNT_LATE)
SCENES.append(_count_late)


# --- 2. The hunter eats last (she takes the Commander hunting) ----------------------------------------------------------

visit(P + "woken.first_meat", "The hunter eats last", [
    nar("ridge", '''{n}She comes for you before first light, as she said she would not, and takes you out of Drezen by the north postern without asking anybody's leave, least of all yours. By the time the sun is up you are in the hills, in wet bracken to the knee, and your leg is telling you in detail what it thinks of her.{/n}
{n}She moves through the trees ahead of you without sound. You move through them like a cart.{/n}''',
        c("Continue", "stop")),
    dl("stop", '''"Stop." {n}She does not raise her voice. She has not raised it once since the crypt.{/n} "You walk on the heel of that leg, because it hurts, and then you slap the good foot down to make up for it. Every beast in these hills has heard you twice. Put your weight on the outside of the foot. Roll it. Slower." {n}She watches you try.{/n} "Worse. Again."''',
        c('"You did this to my leg."', "did"),
        c("[Do it again, slower.]", "again")),
    dl("did", '''"I did. So I will teach you to walk on it." {n}She kneels without warning and takes your bad leg in both hands, above and below the knee, and turns it a little, the way she would turn a foal's leg to see how it set.{/n} "There. Feel that? That is where the bone knit. You favour it, so the rest of you goes wrong around it. A stag with a bad leg does not favour it. He cannot afford to."''',
        c("Continue", "again")),
    dl("again", '''{n}You try again. The bracken whispers less. She says nothing, which from her is praise.{/n}
{n}Her hands, when she finally lets go of your leg, stay a heartbeat longer than they need to. She notices that herself, and frowns at them.{/n}''',
        c("Continue", "sick")),
    nar("sick", '''{n}An hour later she stops again and goes down on one knee in the moss, and this time she has not stopped for you. Below you in a hollow a hind is feeding. It is too thin, and moves wrongly, jerking its head as if something were whispering in its ear, and where its hide has worn through on the flank the flesh underneath has gone the colour of a bruise.{/n}''',
        c("Continue", "wound")),
    dl("wound", '''"The Wound's breath." {n}She says it very quietly.{/n} "It gets into them from the water. First the flies stop landing on them. Then the other deer drive them out. Then they start to eat things a deer should not eat." {n}She nocks, draws, holds.{/n} "In my day, the woods were sick sometimes. Never like this."''',
        c("[Wait for her shot.]", "shot"),
        c('"Can it be saved?"', "saved")),
    dl("saved", '''"No." {n}The bowstring is at her cheek and does not waver.{/n} "It can be ended cleanly, before it goes into the villages and bites a child. That is what a hunter is for, stag. Not the killing. The choosing when."''',
        c("Continue", "shot")),
    nar("shot", '''{n}The arrow goes in behind the shoulder, and the hind drops where it stands, without a sound, as if someone had cut the string that held it up.{/n}
{n}She does not go to it at once. She stands with her head bowed and speaks to it, in old Kellid, the same low and gentle words she spoke over you in the dark. Then she goes down and makes a fire in the hollow and burns it, all of it, and does not take so much as a hoof.{/n}''',
        c("Continue", "boar")),
    nar("boar", '''{n}The boar comes later, near noon, healthy and furious and very large, and she does not let you help. She drops it at forty paces with two arrows so close together they could share a feather, and then she has it on its back and opened from throat to tail before you have got your breath back, working with the calm of a woman kneading bread.{/n}''',
        c("Continue", "first")),
    dl("first", '''{n}She cuts the first strip of fat from along the boar's spine and lays it on a flat stone, and sets the stone on the embers of her fire. When it smokes she stands back.{/n} "Old Deadeye's. Always the first. When I took the white stag I gave him all of it, every scrap. I went three more days hungry after three days of chasing." {n}She almost smiles.{/n} "It was the best meat I never ate."''',
        c("Continue", "law")),
    dl("law", '''"Now, hear the law. The hunter eats last. The village eats first. Always. A hunter who feeds himself before his village is not a hunter; he is a wolf with a bow." {n}She wipes her knife on the moss and looks at you over the carcass.{/n} "This is a great deal of meat, stag, and you have a great deal of village. Where does it go?"''',
        c('"The camp at the south gate. They eat last every day. Today they eat first."', "gate", flags=(FIRST_MEAT, MEAT_GATE)),
        c('"The soldiers on the north wall. They\'re the ones bleeding for the camp."', "wall", flags=(FIRST_MEAT, MEAT_TABLE))),
    dl("gate", '''"Good." {n}She says it as if you had passed a test you did not know you were sitting.{/n} "A lord who feeds the weakest first is not a fool, whatever his captains tell him. Weak people remember who fed them. So do their children." {n}She takes one haunch onto her own shoulder and leaves you the other.{/n} "Carry. You will not carry it well, but you will carry it."''',
        c("Continue", "bow")),
    dl("wall", '''{n}She considers it, frowning, as though you had given her a harder sum than she expected.{/n} "Soldiers are a village too. A hungry one, that never sleeps in one place and buries its own." {n}She nods, slowly.{/n} "Very well. But the camp gets the next one, and I will be watching whose fires it goes to." {n}She takes one haunch onto her own shoulder and leaves you the other.{/n} "Carry."''',
        c("Continue", "bow")),
    nar("bow", '''{n}Halfway down the hill she stops you with a hand flat on your chest, not to listen for game this time, but to look at you.{/n}''',
        c("Continue", "ask_held", requires=(YEW_BOW, BOW_HELD), forbids=(BOW_RETURNED,)),
        c("Continue", "ask_cursed", requires=(YEW_BOW, CURSED_BOW_HELD), forbids=(BOW_RETURNED, BOW_HELD)),
        c("Continue", "ask_gone", requires=(YEW_BOW,), forbids=(BOW_RETURNED, BOW_HELD, CURSED_BOW_HELD)),
        c("Continue", "home", forbids=(YEW_BOW,)),
        c("Continue", "home", requires=(YEW_BOW, BOW_RETURNED))),
    dl("ask_held", '''"You carry my bow still." {n}She does not look at it. She looks at you.{/n} "I have not asked. I will ask once. The white stag gave me its antlers because Old Deadeye told it to. I made them into that bow with my own hands, over one winter, and my hands were in it when I died. Give it back to me."''',
        c("[Give her the antler bow.]", "given", requires=(BOW_HELD,), remove_item=BOW_ITEM, flags=(BOW_RETURNED,)),
        c('"I\'ve grown fond of it. I\'ll keep it a while longer."', "kept")),
    dl("ask_cursed", '''"You carry my bow still. It hates you, you know. I can feel it hating you from here." {n}She does not look at it. She looks at you.{/n} "I will ask once. The white stag gave me its antlers because Old Deadeye told it to. I made them into that bow with my own hands, and my hands were in it when I died, and you took it out of a broken grave. Give it back to me."''',
        c("[Give her the antler bow.]", "given", requires=(CURSED_BOW_HELD,), remove_item=CURSED_BOW_ITEM, flags=(BOW_RETURNED,)),
        c('"I\'ve grown fond of it. I\'ll keep it a while longer."', "kept")),
    dl("ask_gone", '''"My bow. The antler one." {n}She says it lightly, and it is not light.{/n} "It is not in my temple. It is not on your back. Where is it?"''',
        c('"Gone. Sold, or lost in the baggage. I\'m sorry."', "gone"),
        c('"I don\'t know."', "gone")),
    dl("given", '''{n}She takes it in both hands, and for the space of three breaths she does nothing at all. Then she turns it over, and runs her thumb down the grip where the leather has worn to the shape of her fingers, and strings it in one motion, and the yew bow goes over your shoulder instead.{/n} "Keep that one. It is a good plain bow and you are a plain shot. It will suit you."''',
        c("Continue", "home")),
    dl("kept", '''{n}She looks at you the way she looked at the sick hind.{/n} "Then it will hate you a while longer, and so will I, a little." {n}She walks on ahead, and does not look back, and the silence she leaves behind her is colder than the hill.{/n}''',
        c("Continue", "home")),
    dl("gone", '''{n}Something goes out of her face, and does not come back for the rest of the walk.{/n} "Then some city merchant hangs it on a wall and tells his friends it belonged to a dead witch." {n}She adjusts the haunch on her shoulder.{/n} "Well. It was only wood. I am the one who was blessed, not the bow." {n}She does not believe that. Neither do you.{/n}''',
        c("Continue", "home")),
    nar("home", '''{n}You come down to the postern in the dusk with a boar between you and your leg on fire, and the guards stare at the pair of you as if you had come back from the Abyss already.{/n}
{n}At the gate she hands her haunch to the first person she sees, a Kellid girl of perhaps ten, and shows her how to carry it.{/n}''',
        c("[Limp home.]")),
], requires=("trickster.ever", COUNTED), forbids=(CLOSED, FIRST_MEAT), delay=24)


# Authored: the late count carries this hunt after the Abyss, including a standalone hunt between deliveries.
_first_meat = SCENES[-1]
_home_late = copy.deepcopy(next(node for node in _first_meat["Nodes"] if node["Id"] == "home"))
_home_late["Id"] = "home_late"
_home_late["Text"] = _home_late["Text"].replace(
    "the guards stare at the pair of you as if you had come back from the Abyss already",
    "the guards watch the blood dripping from the haunches onto their clean paving")
for _node in _first_meat["Nodes"]:
    for _choice in list(_node["Choices"]):
        if _choice["Next"] == "home":
            _late_choice = copy.deepcopy(_choice)
            _choice["Forbids"].append(COUNT_LATE)
            _late_choice["Requires"].append(COUNT_LATE)
            _late_choice["Next"] = "home_late"
            _node["Choices"].append(_late_choice)
_first_meat["Nodes"].append(_home_late)


# --- 3. The feasting table (her crypt, Zanedra, and the keeper who let them in) ---------------------------------------

visit(P + "woken.feasting_table", "The feasting table", [
    nar("summons", '''{n}A charcoal-burner's boy finds you on the road with a message he has been made to learn by heart, and says it with his eyes shut: "The Blessed says come to her temple. She says bring the stag. She says she means you."{/n}
{n}She meets you at the top of the crypt stair with a lantern, and takes you down without a word.{/n}''',
        c("Continue", "stone", forbids=(WOKE_DREZEN,)),
        c("Continue", "stone_drezen", requires=(WOKE_DREZEN,))),
    # PP10 (Sol BEL): her sarcophagus went to Drezen with her bones; the feast's stains stayed on the bier and the floor.
    nar("stone_drezen", '''{n}She has scrubbed the crypt. You can see how hard she has scrubbed it: the floor is raw and pale, and her knuckles are raw and pale too. Her sarcophagus went to Drezen with her bones; the masons left the bier it stood on, and the flags round it where the feasters knelt. And still the stains come up through the scrubbing like damp through plaster. Dark rings on the bier where the bowls were set down when the lid was full. A long brown smear on the flags where something was dragged.{/n}''',
        c("Continue", "table")),
    nar("stone", '''{n}She has scrubbed the crypt. You can see how hard she has scrubbed it: the stone is raw and pale, and her knuckles are raw and pale too. And still, all across the lid of the sarcophagus, the stains come up through the scrubbing like damp through plaster. Dark rings where the bowls stood. A long brown smear where something was dragged.{/n}''',
        c("Continue", "table")),
    dl("table", '''"They ate off me." {n}Her voice is perfectly level, which is worse than if it shook.{/n} "It is all in the boy's daybook, in his frightened little hand. Baphomet's people. They came down here in the dark with their witch, and they put their bowls on my grave, and they ate. And sang. And the thing they ate was a boy from a farm three valleys over, whose father I would have known the name of, once."''',
        c("Continue", "bones")),
    dl("bones", '''{n}She opens her other hand. In it are four small bones, clean and white, the bones of fingers.{/n} "I found these in the drain. I have been trying to decide which is worse: that they did it, or that I lay under it and did not wake. How many feasts under my back, and I never so much as twitched?" {n}Her hand closes.{/n} "A stag had to blow a horn in my ear."''',
        c('"You were dead. Nobody expects the dead to guard their own graves."', "dead"),
        c("[Say nothing. Let her finish.]", "finish")),
    dl("dead", '''"I expect it." {n}She says it flatly.{/n} "I am Delamere the Blessed. I guarded these valleys for forty winters. I did not expect death to be an excuse."''',
        c("Continue", "finish")),
    dl("finish", '''"The witch. Zanedra, the boy calls her. She put rats in his belly with a word, and bowls on my grave with her hands." {n}She puts the finger bones down on the stone, very gently, in a row.{/n} "Where is she?"''',
        c('"Dead. She died down here, where she did it."', "told_dead", flags=(ZANEDRA_DEAD,)),
        c('"She ran west. Baphomet\'s people are leaving these parts, she said."', "told_fled", flags=(ZANEDRA_FLED,)),
        c('"I don\'t know. The crusade lost track of her."', "told_fled", flags=(ZANEDRA_FLED,), forbids=("chapter_later",)),   # PP10: retired
        c('"I don\'t know. The crusade lost track of her."', "told_lost", flags=(ZANEDRA_LOST,))),
    dl("told_lost", '''"Lost." {n}She turns the word over like a bad coin.{/n} "Your crusade lost a witch whose flock ate a child off my grave. Then I will find her, when this war you are having gives me a season to spare. I tracked a stag three days for my lord. I can track a witch for thirty for a farm boy." {n}She looks back at the finger bones.{/n} "The Horned One's people go under the ground like rats in a haystack, and come up somewhere else. But they leave droppings."''',
        c("Continue", "kyado_alive", forbids=(KYADO_DEAD,)),
        c("Continue", "kyado_cairn", requires=(KYADO_DEAD,))),
    dl("told_dead", '''"Down here." {n}She looks around the crypt, at the walls, the stair, the place where the altar is, as if the floor might still show where.{/n} "Good. I would have liked it to be my arrow. I will not be greedy. A dead witch is a dead witch." {n}She turns back to the finger bones.{/n} "Her flock is not dead. The Horned One's people never are. They go under the ground like rats in a haystack, and come up somewhere else."''',
        c("Continue", "kyado_alive", forbids=(KYADO_DEAD,)),
        c("Continue", "kyado_cairn", requires=(KYADO_DEAD,))),
    dl("told_fled", '''"West." {n}She turns the word over.{/n} "Then west is where I will look, when this war you are having gives me a season to spare. I tracked a stag three days for my lord. I can track a witch for thirty for a farm boy." {n}She looks back at the finger bones.{/n} "The Horned One's people go under the ground like rats in a haystack, and come up somewhere else. But they leave droppings."''',
        c("Continue", "kyado_alive", forbids=(KYADO_DEAD,)),
        c("Continue", "kyado_cairn", requires=(KYADO_DEAD,))),
    dl("kyado_alive", '''"And then there is the keeper." {n}She lifts her head toward the top of the stair, where the lamplight shows a pair of worn boots pretending not to be listening.{/n} "He had my temple. He had my key. And when the witch came he opened my door to her and went upstairs and put his fingers in his ears." {n}Her voice does not rise.{/n} "In my day, a keeper who opened the fold to the wolf was put out of the village with one day's bread and one day's grace, and nobody spoke his name again."''',
        c("Continue", "initiated", requires=(INITIATED,)),
        c("Continue", "judge", forbids=(INITIATED,))),
    dl("initiated", '''"He told me something else, too, weeping. He tells me everything; he cannot help it." {n}Her eyes come back to you.{/n} "He says he made you one of the Horned One's flock. With a prayer he did not believe and a key he did not want to give. And that you said 'I do' and laughed." {n}She is silent a moment.{/n} "I have decided that a lie told to a demon is not a lie. It is a snare. But I will watch where you set the next one."''',
        c("Continue", "judge")),
    dl("judge", '''"Tell me, stag. You know him better than I do. Does he go out with his one day's bread, or does he stay and sweep?"''',
        c('[Speak for him] "He was a shepherd boy with a witch\'s rats in his belly. He stayed. Everyone else ran. He kept your temple as well as he could."', "spared",
          flags=(TABLE, KYADO_SPOKEN)),
        c('"Your temple. Your law. Judge him yourself."', "judged", flags=(TABLE, KYADO_JUDGED)),
        c('[Trickster] "Put him out and you\'ll have to sweep the stair yourself. For the next few hundred years."', "spared",
          flags=(TABLE, KYADO_SPOKEN))),
    dl("spared", '''{n}She is quiet for a long breath.{/n} "He stayed." {n}She says it as though it were a word in a language she used to speak.{/n} "Everyone else ran, and he stayed, and was afraid the whole time, and stayed." {n}She lifts her voice, just enough to carry up the stair.{/n} "Boy. You sweep like a man who expects to be forgiven for it. Come down here and learn to do it properly." {n}A clatter, a squeak, footsteps. She does not smile. She comes very close.{/n}''',
        c("Continue", "baphomet")),
    dl("judged", '''"Then I judge." {n}She raises her voice just enough to carry up the stair.{/n} "Kyado. You opened my door to the wolf. You will sleep in the stable, and you will say the prior's prayers from the doorway of my temple, and you will not cross the threshold until I say. A year. Perhaps less, if you learn to sweep." {n}A long silence at the top of the stair. Then a small, wet voice:{/n} "Y-yes, Blessed."
{n}She looks back at you.{/n} "That is mercy, by my law. It will not feel like mercy to him. That is the point."''',
        c("Continue", "baphomet")),
    dl("kyado_cairn", '''"And then there is the keeper." {n}She nods toward the head of the stair, where a small cairn of fieldstones stands just outside the door, turnip-tops laid on it by someone.{/n} "He is out there. I found him when I woke, and I buried him properly, because nobody else had." {n}Her mouth thins.{/n} "The pilgrims say he opened my door to the witch because she frightened him. In my day, a keeper who opened the fold to the wolf was put out of the village, and nobody spoke his name again. I have not spoken it. Do you know it?"''',
        c('[Speak for him] "Kyado. He was a shepherd boy with a witch\'s rats in his belly. He kept your temple as well as he could, and he died for it."', "mourned",
          flags=(TABLE, KYADO_MOURNED)),
        c('"Leave him in peace. He paid."', "mourned", flags=(TABLE, KYADO_MOURNED))),
    dl("mourned", '''"Kyado." {n}She tries the name the way she tried her own blood in the dark.{/n} "Then I will say it when I pass the cairn. A shepherd boy. My own father kept sheep." {n}She looks at the finger bones on the stone.{/n} "Fear is not a sin, by my law. What a man does with it is. He did badly, and then he died, and dying is enough to pay for most things."''',
        c("Continue", "baphomet")),
    dl("baphomet", '''{n}She gathers the finger bones back into her palm.{/n} "I will bury these by the boy's farm, if the farm is still there. And I will clean my grave again tomorrow, and the next day, and the day after, until I can lie on it and not smell them." {n}She glances at you, and her voice drops.{/n} "Stay a while, stag. Not to talk. The crypt is very quiet, and I have had a great deal of quiet."''',
        c("[Stay with her until the lantern burns down.]", "stayed"),
        c('"I have a war to get back to."', "war")),
    nar("stayed", '''{n}You sit on the bottom step. She sits on the edge of the stone with her knees drawn up and scrubs at it, slowly, and says nothing, and so do you.{/n}
{n}When the lantern gutters she stops scrubbing, and leans back against the wall beside you, and her shoulder rests against yours. It is warm. She does not move it away. Neither do you.{/n}''',
        c("[Leave when she falls asleep.]")),
    dl("war", '''"Of course you do." {n}No reproach in it.{/n} "Go on, then. The fourth step rocks; I have not fixed it yet." {n}She has already turned back to her scrubbing when you reach it, and it rocks.{/n}''',
        c("[Go.]")),
], requires=("trickster.ever", FIRST_MEAT), forbids=(CLOSED, TABLE), delay=24)


# --- 4. Red (the question under all of it: whose waking was it?) --------------------------------------------------

visit(P + "woken.red_blood", "Red", [
    nar("night", '''{n}She comes to your quarters at night, which she has never done, and does not knock, which does not surprise you. You wake to find her sitting on the end of your bed in the dark with her knees drawn up, a knife in one hand and the other hand open in her lap.{/n}
{n}The open hand is cut across the palm. Not once. Many times. Some of the cuts are days old.{/n}''',
        c('"Delamere. What have you done to your hand?"', "hand"),
        c("[Light the lamp.]", "lamp")),
    nar("lamp", '''{n}In the lamplight the cuts look worse, and her face looks tired in a way it did not in the crypt, as though she has not slept since then and does not intend to.{/n}''',
        c("Continue", "hand")),
    dl("hand", '''"I cut it every morning to see if it is still red." {n}She turns the palm to the light as if you had asked to see a wound on a hound.{/n} "It is. Every morning. And every morning I think: today it will be black. Today I will smell myself going off, like meat left in the sun, and know."
{n}She closes the hand.{/n} "Your crusade fights the lich-things, I am told. The dead that walk and think and hate. The demons make them, and some of your own make them too, when they are desperate."''',
        c("Continue", "abomination")),
    dl("abomination", '''"I am told a thing like that could be raised from a grave like mine. With green fire in its eyes, and a chain on its will." {n}She looks straight at you.{/n} "If I were such a thing, I would walk into your forge fire this night. My lord abhors a death by one's own hand, and I would do it anyway. There are worse sins than that. Being that is one of them."''',
        c('"You\'re not. You\'re warm. You eat enough for three soldiers. You bleed."', "proof"),
        c("[Take her cut hand in yours.]", "proof")),
    nar("proof", '''{n}She lets you have the hand. It is hot, almost feverish, and the pulse in her wrist is going like a hare's. She watches you find it. Then, without a word, she takes your hand and puts it flat against the side of her throat, under the jaw, where there is no mistaking what the body is doing.{/n}
{n}It is doing a great deal. So is yours.{/n}''',
        c("Continue", "question")),
    dl("question", '''"That is not what I came to ask." {n}Her voice is lower, and not steady.{/n} "I know I am warm. I know I bleed. I came to ask who did it."
"Was it my lord? Did Old Deadeye send his stag to call me back, the way he sent it to me the first time, because there is work for his priestess again in a sick world? Or was it you? A city-born jester with a borrowed horn and a bad leg, who thought it would be funny?"''',
        c('"It was me. A horn and a joke. Nobody asked Erastil, and he didn\'t send anyone."', "truth", flags=(BLOOD, TRUTH)),
        c('[Lie] "Erastil sent me. I didn\'t know it at the time. I was his stag."', "lie", flags=(BLOOD, LIED)),
        c('"Both. Your god left a door open. I walked through it, making a great deal of noise."', "both", flags=(BLOOD, BOTH))),
    dl("truth", '''{n}She breathes out, long and slow, as if you had drawn an arrow out of her.{/n} "Nobody sent you."
{n}She is quiet a while.{/n} "Then my lord did not call me back. My own vow did. 'When the stag calls, she answers.' I made that vow over a dead white stag in the snow, and I kept it, dead, for longer than your city has stood." {n}Her jaw sets.{/n} "That is better. And it is worse. It means I am here because I keep my word. It does not mean he wants me here."''',
        c("Continue", "wants")),
    dl("lie", '''{n}Her face breaks open. It is terrible to watch.{/n} "He sent you." {n}She says it again, and her voice cracks on it.{/n} "He sent you. He did not forsake me. All that dark, and he had not forgotten." {n}She presses the heel of her cut hand against her eyes and holds it there.{/n}
"Forgive me. I have not wept since I was a girl. It seems I have a great deal of it saved."''',
        c("Continue", "wants")),
    dl("both", '''{n}She stares at you. Then, unwillingly, something in her face gives.{/n} "A door open, and a fool walking through it making a noise." {n}She almost laughs.{/n} "Old Deadeye leaves no gate open without a reason, and no work half done. If he left that one open, he had his reason, and I will ask him for it on my knees." {n}She rubs her face.{/n} "Very well. My vow, and his door, and your noise. I can live with that. I am living with it."''',
        c("Continue", "wants")),
    dl("wants", '''{n}She does not let go of your hand, still flat at her throat. If anything she presses it closer.{/n} "Do you know what the dead do not have, stag? Wanting. I stood at full draw in the dark for longer than there are words for, and I did not want anything, not even to let go."
"Now I want everything. Bread. Fire. Sleep. The smell of rain." {n}Her voice drops.{/n} "Other things. I have not decided yet what to do about the other things."''',
        c('"Take your time deciding."', "time", forbids=(BLOOD,)),        # retired by gating (Q6; index kept): three exits below
        c('[Kiss her.]', "kiss"),
        c('"Go back to your woods, Delamere. Get some sleep."', "sleep"),
        c('"Take your time deciding."', "time_truth", requires=(TRUTH,)),
        c('"Take your time deciding."', "time_lie", requires=(LIED,)),
        c('"Take your time deciding."', "time_both", requires=(BOTH,))),
    dl("time_truth", '''"I am old, stag. Older than anyone you have met. I have spent a great deal of time already." {n}She takes her hand back, finally, and stands.{/n} "But I will take a little more. Not much. Do not get comfortable." {n}At the door she stops.{/n} "You did not lie to me about the horn. You could have, and I would have thanked you for it. Whatever else you are, you did not lie about that." {n}She goes.{/n}''',
        c("[Lie back and listen to her footsteps go.]")),
    dl("time_lie", '''"I am old, stag. Older than anyone you have met. I have spent a great deal of time already." {n}She takes her hand back, finally, and stands.{/n} "But I will take a little more. Not much. Do not get comfortable." {n}At the door she stops, and looks back at you with a face that has not been so open since she was a girl.{/n} "Thank you for bringing me his summons. I will not forget whose errand you ran." {n}She goes.{/n}
{n}The small cold weight in your chest goes with you back to sleep, and is still there in the morning.{/n}''',
        c("[Lie back and listen to her footsteps go.]")),
    dl("time_both", '''"I am old, stag. Older than anyone you have met. I have spent a great deal of time already." {n}She takes her hand back, finally, and stands.{/n} "But I will take a little more. Not much. Do not get comfortable." {n}At the door she stops.{/n} "A door, and a fool, and a noise. I have not decided which of the three to thank. I will tell you when I have." {n}She goes.{/n}''',
        c("[Lie back and listen to her footsteps go.]")),
    dl("time", '''"I am old, stag. Older than anyone you have met. I have spent a great deal of time already." {n}She takes her hand back, finally, and stands.{/n} "But I will take a little more. Not much. Do not get comfortable." {n}At the door she stops.{/n} "You did not lie to me about the horn. Whatever else you are, you did not lie about that." {n}She goes.{/n}''',
        c("[Lie back and listen to her footsteps go.]"), ),
    nar("kiss", '''{n}She lets you. For a heartbeat she is very still, as though she has forgotten what this is, and then she remembers all at once and her cut hand is in your hair, hard, and she kisses you back like a woman who has been hungry for centuries and has only now been reminded of it.{/n}
{n}Then she pushes you off, flat-handed, into the pillows, and stands up breathing like she has run a mile.{/n}''',
        c("Continue", "kissed")),
    dl("kissed", '''"No." {n}Not a refusal; a correction.{/n} "Not here. Not in a city, in a stone box, with a sentry coughing under the window." {n}She wipes her mouth with the back of her wrist, and looks at it, and looks at you.{/n} "I have not decided. When I have decided, it will be in my woods. On my ground. Do you understand me, stag?"''',
        c('"I understand."', "understood")),
    dl("understood", '''"Good." {n}She goes to the door, and stops with her hand on it.{/n} "Do not follow me tonight. I would hear you from a mile off with that leg, and I would have to shoot you again, and I am tired of cutting arrows out of you."''',
        c("[Let her go.]")),
    dl("sleep", '''"Sleep." {n}She considers the word.{/n} "I have slept enough for ten lives." {n}But she stands, and takes her hand back, and goes to the door.{/n} "I will go back to my woods. Not to sleep. To think. Thinking is harder there; there is nothing in the woods to argue with."''',
        c("[Watch her go.]")),
], requires=("trickster.ever", STAG_TOLD), forbids=(CLOSED, BLOOD), delay=24)


# --- The Abyss (Chapter 4): one letter, if she can find anyone to carry it ------------------------------------------

visit(P + "woken.bark", "Birch bark", [
    nar("packet", '''{n}It comes through the Storyteller's portal with the supplies he fetches from Golarion, folded in among the bread and the lamp oil, and it is not paper. It is a strip of birch bark as long as your forearm, rolled and tied with gut, and the words are cut into it with a knife point in a hand that has not written in a very long time.{/n}''',
        c("Continue", "kyado_hand", forbids=(KYADO_DEAD,)),
        c("Continue", "own_hand", requires=(KYADO_DEAD,))),
    nar("kyado_hand", '''{n}Tucked inside the roll is a sheet of ordinary paper in a neat, anxious clerk's script. At the top someone has written: "She dictated. I wrote it down. The bark is her own; she said a letter should be something you can burn. Please don't burn it. K."{/n}''',
        c("Continue", "letter", requires=(ZANEDRA_FLED,)),
        c("Continue", "letter_hills", forbids=(ZANEDRA_FLED,))),
    nar("own_hand", '''{n}The Kellid letters are cut deep and square. Somebody at the Drezen end has pencilled a translation underneath, in the margin, with a note: "the huntress from the Erastil temple, for the Commander; she stood over me while I did this."{/n}''',
        c("Continue", "letter", requires=(ZANEDRA_FLED,)),
        c("Continue", "letter_hills", forbids=(ZANEDRA_FLED,))),
    dl("letter", '''"Stag.
They tell me you have gone down into the Abyss. They say it as if it were a place. I hunted in bad places when I was alive, and I have been dead, and I do not believe anywhere is worse than the one I lay in. Come back and tell me I am wrong.
The woods are quiet. The Horned One's people went west, as you said. I went after the ones who were slow. There are nine fewer. I left them in the trees on the west road so the others would see."''',
        c("Continue", "letter2")),
    # PP10: the same letter when the Commander never told her the witch's people went west.
    dl("letter_hills", '''"Stag.
They tell me you have gone down into the Abyss. They say it as if it were a place. I hunted in bad places when I was alive, and I have been dead, and I do not believe anywhere is worse than the one I lay in. Come back and tell me I am wrong.
The woods are quiet. Some of the Horned One's people were still in these hills when you went down. I went after them. There are nine fewer. I left them in the trees on the west road so the others would see."''',
        c("Continue", "letter2")),
    dl("letter2", '''"I have counted the days since you went. That is what I do. I do not want you to think it means anything. I have not lost count once.
You left with one good leg and one bad one. I gave you leave to limp on the bad one. I did not give you leave to lose the good one. Bring back both.
Delamere, who was Blessed."''',
        c("[Keep the bark.]", flags=(BARK,)),
        # PP10: an answer, carried back by the same dispatch rider; woken.village and her epilogue read it.
        c('[Cut an answer into the back of the bark with your knife, and give it to the Storyteller for his next trip] "Still counting. Both legs, so far."',
          flags=(BARK, BARK_ANSWERED))),
], requires=("trickster.ever", RETURNED, STORYTELLER_SUPPLIES), forbids=(CLOSED, BARK), delay=24, chapters=(4, 4), kind="letter",
    optional=True)   # PP10 (Sol HOW): only once the Storyteller has offered to fetch supplies through his portal


# --- 5. My woods (she proposes the second hunt) ---------------------------------------------------------------------

visit(P + "woken.my_woods", "My woods", [
    nar("wall", '''{n}You find her on the city wall at dusk, which is the last place in Drezen you would have looked, sitting on the parapet with her legs hanging over a sixty-foot drop and her bow across her knees, watching the hills go dark.{/n}
{n}She does not turn round. She heard you three streets away.{/n}''',
        c("Continue", "decided")),
    dl("decided", '''"I have decided." {n}She says it to the hills.{/n} "I said I would tell you when I had, and I have, and I am telling you. Sit down; you make me nervous, standing on one leg on a wall."''',
        c("[Sit beside her.]", "sit")),
    nar("sit", '''{n}You sit. The stone is still warm from the day. Below you the city goes on being a city: a dog, a quarrel, a cart with a bad axle, somebody singing in a tavern very badly. She lets it all go by without comment, which from her is a kind of tenderness.{/n}''',
        c("Continue", "proposal")),
    dl("proposal", '''"At the new moon, come to my woods. Below my temple, where the old clearings are." {n}Her hands are very still on the bow.{/n} "I will run. You will hunt me."
"You have one bad leg and no idea where the deer paths go, and I have been doing this since before your grandmother's grandmother was born. So it will not be a fair hunt. It was not fair when I hunted you, either."''',
        c('"And if I catch you?"', "catch"),
        c('"Why a hunt?"', "why")),
    dl("why", '''"Because that is how it was done, in the hills, before there were priests to say words over it." {n}She glances at you sidelong.{/n} "A woman who wanted a man, or a woman, ran into the woods at the new moon, and they followed. If she did not want to be caught, nobody on this earth could catch her. If she did..." {n}A shrug.{/n} "Then her feet went slow at the right moment, and she would swear to her dying day that she stumbled."''',
        c('"And if I catch you?"', "catch")),
    dl("catch", '''"If you catch me, it is because I let you." {n}Very plainly.{/n} "That is the whole of it. That is my yes, stag. I do not say it with my mouth; I have said too many things with my mouth. I will say it with my feet."
"And if you do not catch me, then I did not let you, and that is my answer too, and you will not ask me again."''',
        c("Continue", "limp_far", requires=(RAN_FAR,)),
        c("Continue", "limp_short", forbids=(RAN_FAR,))),
    dl("limp_far", '''{n}She looks down at your leg, stretched out on the stone.{/n} "I will run slow. A little. It is my arrow in that leg." {n}Then, with something that on another woman would be mischief:{/n} "Not much. You ran me until moonset, the first time, for a city-born beast. I would not insult you."''',
        c("Continue", "want")),
    dl("limp_short", '''{n}She looks down at your leg, stretched out on the stone.{/n} "I will run slow. It is my arrow in that leg." {n}Then, with something that on another woman would be mischief:{/n} "You made three strides, the first time. I will give you a hundred before I start running in earnest. That is generous. Do not tell anyone I was generous."''',
        c("Continue", "want")),
    dl("want", '''{n}She turns her head, at last, and looks at you from very close. There is nothing old in her face now.{/n} "I was dead, stag. I did not want anything. Now I want, and I want you, and I am not ashamed of it. I have never been ashamed of anything I wanted. Only of things I did."''',
        c('"The new moon. Your woods."', "yes", flags=(SECOND_HUNT,)),
        c('"I\'m going to catch you, Delamere."', "boast", flags=(SECOND_HUNT,)),
        c('"No. I won\'t hunt you."', "no", flags=(DECLINED, CLOSED))),
    dl("yes", '''"The new moon." {n}She stands up on the parapet, above a sixty-foot drop, as easily as on a floor, and steps down onto the walk beside you.{/n} "Rest the leg until then. Eat meat. And stop trying to walk quietly in the city; the sentries think you are sneaking out to a lover, and they are laughing at you."''',
        c("[Watch her walk away along the wall.]")),
    dl("boast", '''{n}She laughs, a short surprised bark that makes the sentry at the next tower turn round.{/n} "You will try." {n}She stands up on the parapet, above a sixty-foot drop, as easily as on a floor, and steps down beside you.{/n} "The new moon. Rest the leg until then. And stop walking quietly in the city; the sentries think you are sneaking out to a lover, and they are laughing at you."''',
        c("[Watch her walk away along the wall.]")),
    dl("no", '''{n}She is quiet for a while.{/n} "Then you will never catch me." {n}It is not an accusation. She says it as she would say that a river is deep.{/n} "Good. That is an answer, and you gave it to my face." {n}She stands, and steps down off the parapet.{/n} "I still own the day you owe me, stag. I will not come to collect it. But I will keep it."''',
        c("[Let her go.]")),
], requires=("trickster.ever", BLOOD), forbids=(CLOSED, SECOND_HUNT, DECLINED), delay=24)


# --- 6. The second hunt: her yes is letting herself be caught (the commit) ------------------------------------------

HOLLOW = '''{n}The hollow is a hunter's blind: a lean-to of cut boughs under an overhang of rock, screened with bracken, facing the water. Embers glow in a ring of stones. Stretched over the floor of it, still smelling of blood and woodsmoke, is a stag's hide, fresh, the pale hair on the belly side turned up.{/n}
{n}She is standing on the far side of the fire with her bow unstrung in one hand, as if she had been waiting a long time and had only just stood up.{/n}'''


def second_hunt(opening):
    """The hunt, the catch, the blind and the morning. `opening` is the first node (Kyado's list, or a page)."""
    return [opening,
        nar("woods", '''{n}The new moon. The woods below her temple are black under the trees and grey in the clearings, where the old Kellid villages stood, before there was a crusade or a Wound or a city on the hill behind you. Frost is coming. You can smell it.{/n}
{n}She is gone. There is the bent grass where she stood, and a single long hair caught on a bramble at the height of a tall woman's shoulder, and then nothing at all.{/n}''',
            c('[Perception: read her trail in the dark]',
              check=dict(Skill="SkillPerception", DC=22, Success="trail", Failure="lost", CommanderOnly=True))),
        nar("trail", '''{n}It is there if you look for what is missing instead of what is left: a dry leaf turned wet side up, a cobweb broken at knee height, the stream crossed on the one stone that does not rock. She is not hiding her trail. She is not laying it for you, either. She is running the way she runs, and letting you keep up if you can.{/n}
{n}You follow it for an hour, then two, with your leg burning, down into the clearings and up again, until the trail stops at the edge of a hollow where a fire has been banked under turf.{/n}''',
            c("Continue", "hollow", flags=(TRACKED,))),
        nar("lost", '''{n}You lose her at the stream. The far bank is stone, and the stone keeps nothing, and the woods on the other side are black and silent and full of her.{/n}
{n}You stand there with your leg aching and the frost coming down, and the old Kellid horn from the crypt is heavy at your belt, where you have carried it all night without deciding why.{/n}''',
            c('[Lore (Nature): stop hunting her like a hound and think like a hind; where would you go to ground?]',
              check=dict(Skill="SkillLoreNature", DC=20, Success="thought", Failure="horn"))),
        nar("thought", '''{n}Not uphill; she would expect you uphill. Not the thick cover; that is for beasts that are afraid. Somewhere with water close, and the wind in her face, and a long view of the way she came. Somewhere she could watch you coming and make up her mind.{/n}
{n}There is a hollow below the temple, where the stream bends. You go there. You go slowly, on the outside of your bad foot, the way she taught you. At its edge there is a fire banked under turf.{/n}''',
            c("Continue", "hollow", flags=(TRACKED,))),
        nar("horn", '''{n}You take the horn from your belt.{/n}
{n}It is cheating. You know it is cheating. It is the one call in these woods that she cannot let go unanswered: "When the stag calls, she answers." You lift it anyway, because you are what you are, and you give it everything, the three barks and the long broken roar, and it goes out over the black woods and the frozen clearings and the sleeping temple on its hill.{/n}
{n}Somewhere below you, close, a woman swears in old Kellid. Then there is a light: a fire, uncovered, in a hollow where the stream bends.{/n}''',
            c("Continue", "hollow_called", flags=(CALLED,))),
        # Polish (Sol INT): the blind reached by trail or thought is always "found"; the horn's own path reaches "called"
        # (hollow_called). called_her persists for the record, so it no longer selects the line on a later night's attempt.
        # The old gated choice is retired (chapter_later is held from Chapter 2 on), its index kept.
        nar("hollow", HOLLOW,
            c("Continue", "called", requires=(CALLED,), forbids=("chapter_later",)),
            c("Continue", "found")),
        nar("hollow_called", HOLLOW, c("Continue", "called")),
        dl("called", '''"You blew the horn." {n}Her voice is thick with something that might be outrage and might not.{/n} "You cheat, stag. You cheat at everything. You called me with my own vow, the way a poacher calls a hind with a reed." {n}She tosses the bow down on the bracken.{/n} "I should run again, and make you do it properly. I find I do not want to."''',
            c("Continue", "stag_kill")),
        dl("found", '''"You found me." {n}She sounds, of all things, pleased.{/n} "Without the horn. I thought you would blow the horn. I thought you would stand in the middle of my woods and cheat, and I would have to decide whether to come." {n}She tosses the bow down on the bracken.{/n} "You walked well. On the outside of the foot, the way I showed you. I heard you coming for the last half mile and not before."''',
            c("Continue", "stag_kill")),
        dl("stag_kill", '''{n}She nods at the hide on the floor of the blind.{/n} "I took a stag this morning. An old one, a king of these woods, grey in the muzzle. I gave Old Deadeye the first of him and the camp the rest, and the hide I kept for this." {n}She looks at you across the embers.{/n} "Now. You have hunted me down. Here I stand. What does the hunter do?"''',
            c("Continue", "the_lie", requires=(LIED,), forbids=(CONFESSED,)),
            c("Continue", "choice", forbids=(LIED,)),
            c("Continue", "choice", requires=(CONFESSED,))),
        dl("the_lie", '''{n}And then, before you can take a step, she holds up her hand.{/n} "Wait. One thing first." {n}Her face is very still.{/n} "The boy's scrolls say that Old Deadeye's stag speaks to his hunters in a man's voice, and tells them the truth, always, even when it is hard. I asked my lord about you, every night since you told me he sent you. I asked on my knees. He did not answer me once."
"So I will ask the stag instead. Who woke me?"''',
            c('"I did. I lied to you. Erastil never sent me."', "confess", flags=(CONFESSED,)),
            c('"Erastil did. I told you."', "liar", flags=(LIAR, CLOSED))),
        dl("confess", '''{n}She shuts her eyes.{/n} "Yes." {n}Just that, for a while.{/n} "I knew. I think I knew on the wall. I wanted it so much that I let you give it to me." {n}When she opens her eyes they are wet and very hard.{/n} "You gave me a gift you had stolen from my own god. That is the worst thing anyone has done to me since the peasants waited on the road with knives. And you have taken it back, out loud, in my woods, and I think that is the bravest." {n}A long breath.{/n} "I will be angry with you for a year. Ask me what I will do tonight."''',
            c("Continue", "choice")),
        dl("liar", '''{n}She looks at you for exactly as long as it takes to draw a bow and let the string down again.{/n} "No," she says, very gently. "He did not."
{n}She picks up her bow. She steps back from the fire, one step, two, and the dark takes her as if she had never been standing in it. You hear nothing at all, not a leaf, not a breath. The embers tick. The hide lies on the floor of the blind, waiting for no one.{/n}''',
            c("[Stand in the empty blind until the fire goes out.]")),
        nar("choice", '''{n}Between you there is a ring of embers, and a fresh hide, and the long cold breath of the woods. She has not moved. She will not move, you understand, unless you do; she has run as far tonight as she means to run.{/n}''',
            c("[Step through the embers and catch her by the wrist.]", "caught", flags=(COMMITTED, CAUGHT)),
            c('"Not tonight. Run, Delamere. I\'ll hunt you again another new moon."', "not_tonight", flags=(HUNT_POSTPONED,)),
            c('"You\'ll come back to Drezen with me. Tonight. You\'re mine now; I caught you."', "claimed", flags=(CLAIMED, CLOSED))),
        dl("not_tonight", '''{n}Surprise, and then something like respect.{/n} "A hunter who lets the hind go when she has stopped running." {n}She picks up her bow.{/n} "My father did that once, with a doe in fawn. He said it was the only kill he was ever proud of not making." {n}She steps back into the dark.{/n} "Another new moon, then. I will run faster."''',
            c("[Let her go.]", abort=True)),
        dl("claimed", '''{n}She goes very still, the way a deer does in the heartbeat before it runs.{/n} "Yours." {n}She says it as if trying a word in a foreign tongue and finding it foul.{/n} "Caught, and so owned. Brought back to your city on a leash and kept in a stone box. That is what a hunter does to a hind, stag, not what a man does to a woman. I let you catch me. I did not let you keep me."
{n}She is gone before you can answer, and the dark closes behind her, and nothing you do that night, horn or trail or shouting, brings her back.{/n}''',
            c("[Stand alone in the blind.]")),
        nar("caught", '''{n}The embers bite through your boot, and you do not care. Her wrist is in your hand, hot, the pulse in it going like a hare's, and she lets you have it. She lets you pull her in.{/n}
{n}Up close she smells of woodsmoke and cold air and blood, and she is taller than you remembered, and she is laughing, low in her chest, as if she has only just remembered how.{/n}''',
            c("Continue", "down")),
        dl("down", '''"Caught." {n}Her free hand comes up and takes hold of your jaw, hard, the way she held your leg on the hill: to see how it is made.{/n} "I stumbled. Say that I stumbled, if anyone asks you. I never let anything catch me in my life."
{n}Then she hooks her heel behind your bad knee, neatly, the way a wrestler would, and the leg goes as it always goes now, and she comes down with you onto the stag's hide.{/n}''',
            c("Continue", "hide")),
        nar("hide", '''{n}The hide is still warm from the fire, and slick on the flesh side, and her weight is on you, and her hair comes down around both your faces like a tent. She pulls the lacing of her leathers with one hand, impatient with it, as if she had never worn them at all; the old hide slides off her shoulders onto the stag's hide you are lying on, and she laughs at that, too.{/n}
{n}Under it she is lean and scarred and warm, all long muscle and old white marks, knife and claw and arrow, a map of forty winters on the roads of Sarkoris. She takes your hand and puts it on the worst of them, low on her side, and holds it there.{/n}''',
            c("Continue", "want")),
        dl("want", '''"The boar at the Ash-Cutters' ford, the winter I was thirty. It went under the lacing." {n}Her breath is ragged against your mouth.{/n} "I have not been touched since I was dead, and before that, not for a long time. Nobody touches the Blessed. They are afraid." {n}She takes your mouth the way she takes a trail, without asking where it goes.{/n} "You are not afraid of me. You should be. I am going to have you on this hide the way I would have a fire in winter, all of it, and I will not be gentle, and I will not be quick."''',
            c('"Good."', "cut"),
            c("[Pull her down.]", "cut")),
        nar("cut", '''{n}She makes a sound that is almost a growl, and her hands are at your belt, and the embers flare in a gust of wind off the water, and the whole blind smells of smoke and blood and frost and her.{/n}
{n}The last thing you see clearly, before her hair comes down again and shuts out the fire, is her face above you, fierce and alive and wanting, and not one thing in it that belongs to the dead.{/n}''',
            c("Continue", "morning")),
        nar("morning", '''{n}Grey light through the boughs. Frost on the bracken outside, white as salt. The embers are ash. You are under the stag's hide now, not on it, and she is not beside you.{/n}
{n}She is at the stream's edge, bare-armed in the cold, washing her hands and her face and the back of her neck in water that must be close to ice. On a flat stone by the dead fire lies a strip of fat from the stag's spine, burned black: the first of everything, for Old Deadeye. She has not forgotten him, even last night.{/n}''',
            c("Continue", "count")),
        dl("count", '''{n}She comes back up the bank with her hair dripping, and crouches by the hide, and looks at you with her head on one side.{/n} "When I was alive, my village had fifty-three. I knew them all. Every name, every father, every sin." {n}She reaches out and puts her cold wet hand flat on your chest.{/n} "I have been counting again, this last while. I did not mean to. It is what I do. You are the fifty-fourth, stag. One too many."
{n}The corner of her mouth moves.{/n} "I am not going to put you out."''',
            c('"You could have said that last night."', "said"),
            c('"What happens now?"', "now")),
        dl("said", '''"Last night I said it with my feet." {n}She stands, and stretches, and something in her back cracks like a green branch.{/n} "This morning I am saying it with my mouth. I am old. I am allowed to repeat myself."''',
            c("Continue", "now")),
        dl("now", '''"Now." {n}She considers.{/n} "Now I go back to my temple and scrub it again, and you go back to your war, and at the new moon, if you want me, you know where the woods are." {n}She picks her leathers up off the hide and shakes them out.{/n}
"I will not live in your city. Do not ask me. I will come to it when I choose, and I will leave it when it stinks, which will be always. And the day you owe me is still mine."''',
            c("Continue", "owed")),
        dl("owed", '''{n}She kneels again and puts her palm on your thigh, over the old wound, and presses, not hard.{/n} "I let you catch me. I did not let you off." {n}Her eyes are bright.{/n} "One day I will come for you, and you will run, and I will hunt you through the dark the way I did the first night, and I will catch you. And I will not finish it. Not ever. That is the point." {n}She leans down and kisses you, hard and brief, and tastes of cold water.{/n} "Stay quick, stag."''',
            c("[Stay quick.]")),
    ]


HUNT_REQUIRES = ("trickster.ever", SECOND_HUNT)
HUNT_FORBIDS = (CLOSED, COMMITTED)

temple(P + "woods.second_hunt", "The second hunt", '"Kyado. Is Delamere in the woods tonight?"', second_hunt(
    kyado("start", '''{n}Kyado looks up from his broom, and goes red to the ears.{/n} "She left at dusk. She said you'd c-come. She said, 'Tell the stag the woods are open.' And then she ate a whole loaf standing up, and went out of the door without her cloak." {n}He looks at the dark beyond the temple door, and then at your leg, and then very hard at the floor.{/n} "Commander, it's the new moon. You know what the old Kellid songs say about the new m-moon."''',
        c('"I know."', "woods"))),
    requires=HUNT_REQUIRES, forbids=HUNT_FORBIDS, delay=24)

visit(P + "woods.second_hunt_page", "The second hunt", second_hunt(
    nar("start", '''{n}No message comes. None is needed. On the night of the new moon you take the old horn from where you have hung it, and a lantern you do not light, and you ride out alone to the woods below her temple, and tie the horse at the edge of the trees.{/n}''',
        c("Continue", "woods"))),
    requires=HUNT_REQUIRES + (KYADO_DEAD,), forbids=HUNT_FORBIDS, delay=24, chapters=(3, 5))

visit(P + "woods.second_hunt_late", "The second hunt", second_hunt(
    nar("start", '''{n}No message comes. None is needed. On the night of the new moon you take the old horn from where you have hung it since the crypt, and a lantern you do not light, and you ride out alone to the woods below her temple. The war has been through these hills since you last walked them. The trees have not noticed.{/n}''',
        c("Continue", "woods"))),
    requires=HUNT_REQUIRES, forbids=HUNT_FORBIDS + (KYADO_DEAD,), delay=24, chapters=(5, 5))


# --- 7. Fifty-three, again (Chapter 5: what came of the count) --------------------------------------------------------

visit(P + "woken.village", "Fifty-three, again", [
    nar("arrive", '''{n}She is waiting on the road outside your camp when you come back from the Abyss, sitting on a milestone with a sack at her feet, as if she has been there every day since you left and meant to be there every day until you came.{/n}
{n}She looks at you, all of you, from boots to hair, counting. Then she nods, once, as if a sum has come out right.{/n}''',
        c("Continue", "both_legs", forbids=(BARK_ANSWERED,)),
        c("Continue", "both_legs_bark", requires=(BARK_ANSWERED,))),
    dl("both_legs", '''"Both legs." {n}That is all the greeting you get.{/n} "Good. Walk with me. I have something to tell you, and I will not tell it on a road."''',
        c("Continue", "given", requires=(VILLAGE_GIVEN,)),
        c("Continue", "forced", requires=(VILLAGE_FORCED,)),
        c("Continue", "refused", requires=(VILLAGE_REFUSED,)),
        c("Continue", "clans", requires=(VILLAGE_CLANS,))),
    # PP10: the Commander answered her bark from the Abyss.
    dl("both_legs_bark", '''{n}Your strip of bark is through her belt, the cut side out, where her hand can find it the way it finds an arrow.{/n} "Both legs." {n}She taps the bark.{/n} "'So far,' you cut. I have read 'so far' every night since it came up the road. That is a cruel thing to send a hunter, stag. I know what a hunter finds at the end of a trail."
{n}That is all the greeting you get.{/n} "Walk with me. I have something to tell you, and I will not tell it on a road."''',
        c("Continue", "given", requires=(VILLAGE_GIVEN,)),
        c("Continue", "forced", requires=(VILLAGE_FORCED,)),
        c("Continue", "refused", requires=(VILLAGE_REFUSED,)),
        c("Continue", "clans", requires=(VILLAGE_CLANS,))),
    dl("given", '''"The volunteers." {n}She walks beside you, matching her stride to your limp without seeming to.{/n} "Four families went. Nineteen souls. They built two longhouses in the clearing below the temple, and a palisade that would not stop a goat, and I made them build it again." {n}She is quiet a moment.{/n} "The Wound's things came in the first snow. Three of them, with wrong legs. I killed them in the stream. The cooper's boy was fetching water. He lost an arm."''',
        c("Continue", "given2")),
    dl("given2", '''"His mother came to me after, and I thought she would curse me. She asked me to teach him to shoot left-handed." {n}Something moves in her face.{/n} "Nineteen souls. By spring there will be twenty-two; two of the women are carrying. I know every name." {n}She opens the sack at her feet: dried venison, a string of mushrooms, a crooked carved deer.{/n} "They sent this. For the one who let them go. The deer is from the boy. It is very bad. Keep it."''',
        c("[Take the carved deer.]", "end", flags=(VILLAGE_SEEN,))),
    dl("forced", '''"The ones I chose." {n}She walks beside you, matching her stride to your limp without seeming to.{/n} "Sixty-one souls, in three villages. Two of them died on the road the first month: an old man and a baby, of the cold, because the carts were slow. I buried them. Their families spat on me at the graveside. I let them."
{n}Her voice does not change.{/n} "The Wound's things came in the first snow. They came to a village where every man knew every other man's hand on a spear. Not one of them got past the palisade."''',
        c("Continue", "forced2")),
    dl("forced2", '''"They hate me. They will hate me for a year, and bless me for forty, as the others did." {n}She glances at you.{/n} "They hate you more. It was your word. I told them so; I will not wear another's cruelty, only my own." {n}She opens the sack at her feet: dried venison, a string of mushrooms.{/n} "They did not send this. I took it from their smokehouse as your due. They let me. That is how you know they are alive."''',
        c("[Take the sack.]", "end", flags=(VILLAGE_SEEN,))),
    dl("refused", '''"Your hive." {n}She walks beside you, matching her stride to your limp without seeming to.{/n} "While you were gone, a fever went through the camp at the south gate. A boy brought it in from the river. By the time the chirurgeons knew, forty were sick. Eleven died."
{n}She does not raise her voice.{/n} "In a village of fifty-three, I would have known the boy's name and the river and his mother's cough by the first evening. In your hive, nobody knew him until he was dead."''',
        c('"And in a village in the woods, the demons would have had all fifty-three."', "refused2"),
        c("[Say nothing.]", "refused2")),
    dl("refused2", '''"Perhaps." {n}The word costs her something.{/n} "I have thought about it. I have had time to think; you were in the Abyss." {n}She stops walking.{/n} "You kept them behind walls, and eleven died of the walls. I would have sent them into the woods, and some would have died of the woods. I do not know which is the better sum. Old Deadeye never taught me to count cities." {n}She hands you the sack at her feet: dried venison, meant for the camp.{/n} "Take it to them. I will not go in."''',
        c("[Take the sack to the camp.]", "end", flags=(VILLAGE_SEEN,))),
    dl("clans", '''"Your forty villages." {n}She walks beside you, matching her stride to your limp without seeming to.{/n} "I chose the elders. It took a month. Some of your captains complained that I chose a laundress over a lieutenant, and I told them the laundress knew the names of every soldier in her barracks and the lieutenant knew the names of his horses."
{n}She almost smiles.{/n} "A fever came into the south camp while you were gone. The laundress found the boy who brought it on the first evening, because she knew his mother's cough. Four died. Not forty."''',
        c("Continue", "clans2")),
    dl("clans2", '''"I do not like it." {n}She says it firmly, as though you had argued.{/n} "It is a trick. It is a jester's trick, cutting Erastil's law to fit a city, and I do not like it. But it works, and I have been dead too long to be proud about things that work." {n}She hands you the sack at her feet.{/n} "Venison. For the laundress. She will know whose fires need it."''',
        c("[Take the sack.]", "end", flags=(VILLAGE_SEEN,))),
    dl("end", '''{n}She walks you as far as the camp's pickets and no further.{/n} "There. That is what came of the thing you chose, before you went down into the dark. I thought you should know. A lord should know what came of his word." {n}She looks at your leg, and then at your face.{/n} "Rest. You look like something I would put out of its misery."''',
        c("[Watch her go back up the road.]")),
], requires=("trickster.ever", COUNTED), forbids=(CLOSED, VILLAGE_SEEN, COUNT_LATE), delay=24, chapters=(5, 5),
    RequiresAnyGroups=[list(VILLAGE)])


# --- 8. The day owed (after the commit: she hunts the Commander again) -------------------------------------------------

visit(P + "woken.day_owed", "The day owed", [
    nar("window", '''{n}The first frost comes in the night. You wake because the room is cold, and the room is cold because the shutter is open, and the shutter is open because there is a woman crouched on your windowsill with a bow in one hand and the other hand over your mouth.{/n}''',
        c("Continue", "whisper")),
    dl("whisper", '''"Shh." {n}Her breath is white in the cold.{/n} "I have come for my day, stag. It is a night, but I am old and I round up." {n}She takes her hand from your mouth and nocks an arrow.{/n} "I will count to a hundred, in Kellid. Run."''',
        c('"You\'re joking."', "joking"),
        c("[Run.]", "run")),
    dl("joking", '''"I have never made a joke in my life. One." {n}She draws.{/n} "Two."''',
        c("[Run.]", "run")),
    nar("run", '''{n}You go out of the door barefoot with your coat half on, down the stair and out through the kitchens, where a scullion drops a pail, and into the frozen yard. Behind you, unhurried and perfectly audible, a voice is counting in old Kellid.{/n}
{n}You go over the wall of the citadel garden, badly, and through the lower town, worse. The frost makes the cobbles glass. Your leg screams at every stride. At some point, somewhere around the fish market, you realise that you are laughing, and that you cannot stop.{/n}''',
        c("Continue", "roofs")),
    nar("roofs", '''{n}You take to the roofs, because she will not expect a stag on the roofs. She is waiting on the second one.{/n}
{n}She does not shoot. She does not need to. She simply steps out from behind a chimney and puts out one foot, and your bad leg does what it always does now, and you go down on the frozen tiles with the whole of Drezen spread out below you, asleep and white with frost.{/n}''',
        c("Continue", "caught_again", requires=(RAN_FAR,)),
        c("Continue", "caught_again_short", requires=(RAN_SHORT,))),
    dl("caught_again", '''{n}She kneels over you as she did on the night she woke, a knee pinning you to the tiles, the knife at your throat, and her breath is coming as hard as yours.{/n} "Easy, brother. You ran well." {n}Her voice is shaking, and it is not with cold.{/n} "Worse than the first time. You are getting slow. That is my doing."''',
        c('"Go on, then. Finish it."', "no_finish"),
        c('"Not yet. Hunt me again."', "again", requires=(SAID_AGAIN,)),
        c("[Pull her down to you.]", "down"),
        # Polish (Sol INT): the same answer for a Commander who said something else in the leaves (or an older save).
        c('"Not yet. Hunt me again."', "again_new", forbids=(SAID_AGAIN,))),
    dl("no_finish", '''"No." {n}The knife goes back in its sheath.{/n} "I said it the night I woke. I will say it every time. I will never finish it." {n}She bends down until her forehead rests on yours.{/n} "If I finish it, the hunt is over, and a hunt that is over lets its hunter lie down. I am not lying down again, stag. Not for a long time."''',
        c("Continue", "cold")),
    dl("again", '''{n}Her face does something complicated.{/n} "That is what you said the first time. In the leaves, with my arrow in you." {n}The knife goes back in its sheath.{/n} "You are a fool, and I have woken up in love with a fool, and I would not trade it for all of Sarkoris." {n}She bends down until her forehead rests on yours.{/n} "Again. Every frost, as long as your leg holds out. And longer."''',
        c("Continue", "cold")),
    dl("again_new", '''{n}Her face does something complicated.{/n} "In the leaves, with my arrow in you, you said something else. You have learned the right words since." {n}The knife goes back in its sheath.{/n} "You are a fool, and I have woken up in love with a fool, and I would not trade it for all of Sarkoris." {n}She bends down until her forehead rests on yours.{/n} "Again. Every frost, as long as your leg holds out. And longer."''',
        c("Continue", "cold")),
    nar("down", '''{n}You pull her down by the lacing of her leathers, and she comes, laughing into your mouth, the knife clattering away down the tiles into somebody's gutter. For a while the frost does not matter at all.{/n}''',
        c("Continue", "cold")),
    dl("cold", '''{n}Somewhere below, a watchman's lantern is swinging round to find the noise.{/n} "Up. You are barefoot on a roof in the first frost, and my arrow's bone is in your leg, and I will not carry you." {n}She stands, and gives you her hand, and hauls you up.{/n} "Next year I will count to ninety. Stay quick, stag."''',
        c("[Limp home with her.]", flags=(FIRST_FROST,))),
], requires=("trickster.ever", COMMITTED, HUNT_OWED), forbids=(CLOSED, FIRST_FROST), delay=72)

# Authored: a stag caught on the third stride has improved by reaching the roofs, despite her arrow.
_frost = SCENES[-1]
_caught_short = copy.deepcopy(next(node for node in _frost["Nodes"] if node["Id"] == "caught_again"))
_caught_short["Id"] = "caught_again_short"
_caught_short["Text"] = _caught_short["Text"].replace(
    "Worse than the first time. You are getting slow. That is my doing.",
    "Further than three strides this time. On that leg, too. You have learned to run on my arrow.")
_frost["Nodes"].append(_caught_short)
