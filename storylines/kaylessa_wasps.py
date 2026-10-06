"""Kaylessa: the courtship under the tailor's awning, before the knife (optional beats after her rules).

Every scene is at her presence in Drezen's market (kaylessa_trickster PRESENCE) or, once, a ride out of the city. Each
engages a canon anchor of hers:
- the Sunset Wasps, vigilantes of Calistria, fed false names by Anemora "hiding under the guise of the oldest and the
  wisest of us" (Kaylessa_Reveal/Cue_0039 b60a1979, Cue_0040 21e7f278; Kaylessa_Diary c669b34a);
- her message and her last request: "Send a letter to Avennara, to the leader of the border defenders" (Kaylessa_Reveal/
  Cue_0028 f252350f; Obj6_SendMessage e4b22586), the papers pressed into the Commander's hand at her early death
  (Kaylessa_main/Cue_0059 a71103ae), Forn's "Destroy it" (Forn_main/Answer_0039 30b5b35e) and the Kyonin marksmen of
  the Kaylessa_Letter project (472666a0; KaylessaTomb 78fb64bf);
- "Everyone's a soldier in a war, generals and privates alike" (Kaylessa_main/Cue_0073 425898fa);
- "What are you looking at, soldier? Like what you see?" (Kaylessa_main/Cue_0001 2d7d6df4);
- Forn's flash powder: "bright light causes her kind pain" (Forn_main/Cue_0048 e5f50b58); her broken bow (Cue_0019
  1686b22f);
- Anevia's catch in the war camp (Cue_0084 5f306afc), her torn half-mask (Cue_0056 462478fa), Camellia's "Help her go on
  her own terms" (Kaylessa_Reveal/Cue_0052 ce4651d7; Answer_0067 6502c2a2);
- the Winter Council and "truth is greater than gain" (Cue_0026 02598510, Cue_0036 6155ceb3; the diary);
- Anemora at Iz: "None... except for that blasted Kaylessa." (c5/Iz/Anemora/Cue_0146 c0fb6762);
- Ember in Kenabres: "you were burned from within, I think. It hurt, didn't it?" (Kaylessa_main/Cue_0080 b3427ecf).
Acknowledgments of other women are in Kaylessa's voice only; no scene between partners.
"""
from story_format import c, scene
from storylines.kaylessa_trickster import (FIRST_WORDS, ANEMORA_TOLD, AMULET, BEGGED, CAM_KILLED, CAUGHT, CLOSED, COMMITTED, DREZEN,
                                           EMBER_MET, KNIFE_SHOWN, LEFT, NOTE_DESTROYED, NOTE_HELD, PRESENCE, REL, RETURNED,
                                           RULES, SHYKA_RAISED, STALLED, SWAP_CLEAN, SWAP_FUMBLED, TOMB, UNIT, UNMASKED, kay, nar)

SCENES = []
K = "kaylessa.wasps."

THE_WASP = K + "the_wasp"
LAST_WORDS = K + "last_words"
HER_TOMB = K + "her_tomb"
SOLDIER = K + "soldier"
IN_THE_DARK = K + "in_the_dark"
THE_BOW = K + "the_bow"
OTHER_YOU = K + "the_other_you"
HANDS = K + "watching_hands"
KYONIN = K + "kyonin"
ANEMORA = K + "anemora"
BURNED = K + "burned_within"
NOON = K + "noon"
WHAT_I_WANT = K + "what_i_want"
WOLJIF = K + "woljif"

# Outcomes later scenes and the epilogue may read.
STING_FLIRTED = K + "sting_flirted"
NOTE_RETURNED = K + "note_returned"
LETTER_SOLD_TOLD = K + "letter_sold_told"
LETTER_UNSENT_TOLD = K + "letter_unsent_told"
MARKSMEN_TOLD = K + "marksmen_told"
MARKSMEN_KEPT = K + "marksmen_kept"
KISSED = K + "kissed"
LETTER_SENT = K + "letter_sent"
LETTER_KEPT = K + "letter_kept"
# PP2 early beat (kaylessa_early, Chapter 1 Kenabres; path-neutral), read in "Hands" only.
EARLY_BOUND = "kaylessa.early.dressed.bound"
EARLY_LIED = "kaylessa.early.dressed.lied"
DREW_THE_BOW = K + "drew_the_bow"


def meet(id, title, entry, nodes, requires=(RULES,), forbids=(), delay=24, chapters=(3, 5), **extra):
    """A physical, optional beat at her presence under the tailor's awning; each happens once."""
    SCENES.append(scene(id, title, "Kaylessa", min(chapters), entry, nodes,
                        requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, LEFT, id, *forbids))), delay=delay, last=max(chapters),
                        optional=True, Relationship=REL, Chapters=list(chapters), ContactUnit=UNIT, Areas=[DREZEN],
                        InteractionHub=PRESENCE, **extra))


def visit(id, title, nodes, requires, forbids=(), delay=24, **extra):
    """A rest-delivered ride out of the city: she is there in person."""
    SCENES.append(scene(id, title, "Kaylessa", 3, "", nodes, requires=tuple(dict.fromkeys(("trickster.ever", *requires))),
                        forbids=tuple(dict.fromkeys((CLOSED, LEFT, id, *forbids))), delay=delay, last=5, optional=True,
                        Relationship=REL, Remote=True, Kind="visit", Chapters=[3, 5], Areas=[DREZEN], **extra))


# --- 1. The Savored Sting: who she was before. -------------------------------------------------------------------

meet(THE_WASP, "The Savored Sting", '"Who were you, before all this?"', [
    nar("open", '''{n}She is fletching arrows on the crate, grey goose feathers laid out in a row on a scrap of oilcloth. Across the square a crier is reading the week's losses from the northern forts, name after name, and she does not look up once while he reads.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Before?" {n}She trims a feather with the edge of her knife.{/n} "Before, I was a wasp."
"The Sunset Wasps. A handful of us in Kyonin, young and very sure. We served Calistria. The Savored Sting. Lust, trickery and revenge, soldier: the three things Kyonin likes to pretend it has no use for, and uses every day behind closed shutters."''',
        c('"What did the wasps do?"', "night"),
        c('[Flirt] "Lust, trickery and revenge. I think I\'d have liked your goddess."', "flirt", flags=(STING_FLIRTED,)),
        c('"Why Calistria, of all of them?"', "why")),
    kay("flirt", '''{n}The knife stops. She looks at you over the feathers, and for once there's no weariness in it at all.{/n}
"She'd have liked you. That's what worries me." {n}Her eyes go to your mouth and stay there a heartbeat longer than they should.{/n}
"Careful, soldier. Wasps sting what they like, too. Harder, usually."''',
        c('"I\'ll take my chances."', "night"),
        c('"Noted."', "night")),
    kay("why", '''"Because the other gods in Kyonin had temples and priests and very good manners, and none of them did anything about the men who could afford a good advocate." {n}She sets the finished arrow aside.{/n}
"Calistria doesn't forgive. She doesn't ask you to. She keeps the list, and she waits, and one night she sends a girl with a knife. That appealed to me, when I was young."''',
        c('"What did the wasps do?"', "night")),
    kay("night", '''"The first one was a merchant in Iadara. He'd drowned a debtor's son in a rain barrel to make a point about interest. The magistrates called it an accident. He paid for the funeral."
{n}She draws a feather through her fingers, slowly.{/n}
"We left him on the temple steps at sunrise with his purse cut, his hamstrings cut, and the boy's name painted across his chest in lamp-black. He lived. He didn't walk again, and he didn't lend again, and every child in the street knew why."''',
        c('"That\'s justice?"', "justice"),
        c('"It sounds like it worked."', "worked")),
    kay("justice", '''"It was ours." {n}She doesn't flinch from it.{/n} "The law had its turn and bought itself a funeral. We took the next turn. I'd do it again, for him. That one I'd do again."''',
        c("Continue", "names")),
    kay("worked", '''"It did. That was the trouble. It worked so well that we wanted more of it." {n}She almost smiles.{/n} "Nothing makes a girl surer of herself than being right once in public."''',
        c("Continue", "names")),
    kay("names", '''"After that the names came to us. Whispered. Folded into prayer books in the temple. Somebody older, somebody wiser, who knew where every crime in Kyonin was buried. We never asked who."
{n}Her hands have gone still on the oilcloth.{/n}
"It was Anemora. Wearing the face of the oldest and wisest of us. We stung a scribe for three nights before anyone told us he'd done nothing at all but write down the wrong name for her once."''',
        c('"You couldn\'t have known."', "known"),
        c('"Do you still pray to her? Calistria?"', "pray"),
        c('"And now you watch everyone\'s hands."', "hands")),
    kay("known", '''"That's what everyone says. Anemora said it too, later, very kindly, holding my wrist." {n}She picks up the next feather.{/n}
"I should have known. A wasp who doesn't ask where the names come from isn't a wasp. She's a knife somebody else is holding."''',
        c("Continue", "mark")),
    kay("mark", '''{n}She pushes back her sleeve. On the inside of her wrist, where a pulse would show on anyone else, there is a small tattooed wasp, black ink on skin gone nearly as black. You would never see it unless she showed you.{/n}
"They put it on us at the altar, the night we swore. It used to stand out. Everyone in Iadara who knew what to look for could see it on my wrist when I reached for a cup." {n}She rubs it with her thumb.{/n}
"Now it's almost gone. The curse took it, like it took the rest. You have to know it's there." {n}She pulls the sleeve down.{/n} "Most things about me are like that now, soldier."''',
        c('"I know it\'s there."', "mark_know"),
        c("[Help her with the feathers.]")),
    kay("mark_know", '''"You do now." {n}She says it as if she has handed you something heavy and is waiting to see whether you drop it.{/n} "Help me with these, then. The north forts are short of arrows, and I'm short of things to do with my hands."''',
        c("[Help her with the feathers.]")),
    kay("pray", '''"Calistria doesn't want prayers. She wants payment." {n}She tilts her head toward the crier, still reading.{/n}
"I owe her Anemora. I owe her the Winter Council. I owe her every name on that man's list, if you want to be exact about it. When I've paid, I'll pray. It'll be a short prayer, and rude."''',
        c("Continue", "mark")),
    kay("hands", '''"Everyone's. Yours too." {n}She doesn't pretend otherwise.{/n}
"You've got honest hands, soldier, for a Trickster. That's the most suspicious thing about you."''',
        c("Continue", "mark")),
], delay=24)


# --- 2. Her story: what became of her last words, in each world. ---------------------------------------------------

meet(LAST_WORDS, "Her story", '"You said you wanted to ask me something."', [
    kay("start", '''"I did. Sit." {n}She moves along the crate to make room, which she has never done before. The market is thin today; half the stalls are shut, because a supply column didn't come back from the north road and nobody wants to talk about why.{/n}
"There's one thing I've had on my mind since Kyonin, soldier. Not the beast. Not the Council. My story. That somebody should know it when I'm gone."''',
        c("Continue", "held", requires=(STALLED, NOTE_HELD), forbids=(BEGGED,)),
        c("Continue", "destroyed", requires=(STALLED, NOTE_DESTROYED), forbids=(BEGGED, NOTE_HELD)),
        c("Continue", "lost", requires=(STALLED,), forbids=(BEGGED, NOTE_HELD, NOTE_DESTROYED)),
        c("Continue", "tomb", requires=(BEGGED, TOMB)),
        c("Continue", "nocame", requires=(BEGGED,), forbids=(TOMB,)),
        c("Continue", "alive", requires=(AMULET, SWAP_CLEAN)),
        c("Continue", "alive_fumbled", requires=(AMULET, SWAP_FUMBLED))),
    kay("held", '''"I remember pushing some papers into your hand. Crumpled. Bloody, probably. I remember thinking: there, now it's somebody else's problem." {n}She looks at your belt, your pack, the pouch at your side.{/n}
"Do you still have them?"''',
        c("[Take out the folded pages and give them to her.]", "read")),
    kay("read", '''{n}She unfolds them carefully. The paper has been wet and dried again, and there is a brown thumbprint on the first page that is probably hers.{/n}
"'Whoever is reading this, know that my name was Kaylessa, and I was an elf until my last day.'" {n}She reads it aloud in a flat voice, then stops.{/n}
"I was very proud of that line. I wrote it in a cellar in Kenabres with the city burning over my head and I thought it was the truest thing I'd ever said."''',
        c('"It still is."', "still"),
        c('"You kept writing after that."', "still")),
    kay("still", '''"It isn't. I'm not an elf, soldier. I stopped being one somewhere in the Worldwound, between one prisoner and the next." {n}She folds the pages again, along the old creases.{/n}
"But you kept it. You carried a dead drow's scribble all the way from there to here, and never gave it to anyone who'd burn it."''',
        c('[Give it to her to keep] "It\'s yours."', "give", flags=(NOTE_RETURNED,)),
        c('"I\'ll keep carrying it, if you want."', "keep")),
    kay("give", '''{n}She holds the pages as if they might go off in her hands.{/n} "Mine. Yes." {n}Then she tucks them inside her cloak, against her ribs, where the shawl covers them.{/n} "The first thing in two years anyone's given back to me instead of taking."''',
        c("[Sit with her a while.]")),
    kay("keep", '''"No. Yes." {n}She pushes them back into your hands, quickly, before she can change her mind.{/n} "Keep them. If the thumb on the clock ever slips, I want somebody to have read them who didn't have to."''',
        c("[Put them away.]")),
    kay("destroyed", '''"I remember pushing papers into your hand. And I remember something else, from after, that I shouldn't. Forn, in his grey, holding them over a candle, with that sad face he did so well." {n}She is not asking.{/n}
"You gave him my story. And he burned it, because that is what he was for."''',
        c('"I didn\'t know what he was."', "didnt"),
        c('"Yes. I did."', "did")),
    kay("didnt", '''"No. Nobody did. That was his whole trade." {n}She lets out a slow breath.{/n} "He'd have come for you afterwards anyway, for having held it. Forn never left anyone alive who'd read a line of it. So your hand was bought either way, soldier. I just want you to know whose hand bought it."''',
        c("Continue", "rewrite")),
    kay("did", '''{n}She looks at you properly, and nods, as if an account has finally balanced.{/n}
"Honest. That's rule three kept, at least. It doesn't make it better. It makes it clean."''',
        c("Continue", "rewrite")),
    kay("rewrite", '''"So there's no story. Kyonin got exactly what it paid for: a dead cultist and a candle." {n}Her fingers drum on her knee.{/n}
"Then I'll write it again. Longer. Nastier. With names in it this time. And this time I'll be alive to see who reads it."''',
        c('"I\'ll carry this one myself."', "carry"),
        c('"Write it. I want to read it first."', "carry")),
    kay("carry", '''"We'll see." {n}But she's already looking at the empty page in her head, the way a hunter looks at a trail.{/n}''',
        c("[Leave her to it.]")),
    kay("lost", '''"I remember pushing papers into your hand when I died. Crumpled, bloody, badly spelled. I don't know what you did with them. I don't think I want to guess."
{n}She waits. When you don't answer at once, she shakes her head.{/n}
"Lost. Burned. Sold to a Kyonin courier for a nice pair of gloves. It doesn't matter. It was a first copy. I'll write another."''',
        c('"I don\'t know where they went."', "carry"),
        c('"Write it again. I\'ll see that it goes."', "carry")),
    kay("tomb", '''"And you sent it. My letter. To Avennara, at the border." {n}Her voice does something complicated on the name.{/n}
"I know you did, because there's a stone with my name on it in the clearing where Forn's men shot me, and there are Kyonin marksmen in your barracks drinking to my memory. I saw them from the other side of the square. They looked well."''',
        c('"You could go and tell them you\'re alive."', "friends"),
        c('"It was what you asked for."', "asked")),
    kay("friends", '''"And say what? 'Hello, I'm your tragic martyr, I got better'?" {n}She almost laughs.{/n}
"They came here to avenge a dead woman. It's the cleanest thing that's happened to my name in years. I'm not sure I'm ready to dirty it by breathing."''',
        c("[Let it rest.]")),
    kay("asked", '''"It was. It was the only thing I asked." {n}She looks at her own hands.{/n}
"Thank you, soldier. I don't say that often, so don't make a face. You did the one thing, and you did it properly, with the seal and everything. And then you went and did the other thing too."''',
        c("[Let it rest.]")),
    kay("nocame", '''"I asked you to send a letter to Avennara at the border. I remember asking. It's the last thing I remember wanting." {n}She watches the gate.{/n}
"Nobody came from Kyonin. No marksmen. No stone. So either you never sent it, or you sent it somewhere else. Which?"''',
        c('''[Tell the truth] "The Winter Council wanted your story buried. I ordered it done. They paid me."''', "sold", flags=(LETTER_SOLD_TOLD,)),
        c('"I never sent it. I don\'t have a good reason."', "unsent", flags=(LETTER_UNSENT_TOLD,)),
        c('"I haven\'t decided yet."', "unsent", flags=(LETTER_UNSENT_TOLD,))),
    kay("sold", '''{n}She sits very still. Her jaw tightens.{/n} "You took their money. You knew whose story you were burying."
"I hope it was a good price, soldier. They paid you once, and I'll have to write every bloody word again. You told me. That's rule three kept. It doesn't clean your hands."''',
        c("Continue", "rewrite")),
    kay("unsent", '''"Not sent." {n}She nods, as if she expected nothing better and is almost relieved to have been right.{/n}
"Then it's still mine. Good. I'd rather send it myself, alive, than have it read over my grave by people who'll cry about it."''',
        c("Continue", "rewrite")),
    kay("alive", '''"I kept meaning to write to Avennara. There was always another road, another hunter, another night in a ditch." {n}She looks toward the gate.{/n}
"Then we put my borrowed face on the Council's man, and they shot him for me. They went home thinking I was dead beside him. Now I have time to write. No excuse left, soldier."''',
        c('"Then write it."', "alive_write"),
        c('"What would you say?"', "alive_say")),
    kay("alive_write", '''"I will." {n}She taps the side of her head.{/n} "It's all in here. It has been for two years. The trouble isn't the words, soldier. It's knowing that the first person to read it will be someone who wants me dead."''',
        c("[Let her think.]")),
    kay("alive_say", '''"That I was an elf. That I'm not. That any one of them could wake up like me, if they stopped fighting for long enough, and that the Winter Council would rather kill every witness in Mendev than let them know it."
{n}She shrugs.{/n} "Short letter. Long list of names at the bottom."''',
        c("[Let her think.]")),
    kay("alive_fumbled", '''"I kept meaning to write to Avennara. Before the Council's next hunter caught me." {n}She watches her hands on her knees.{/n}
"They caught us instead. He caught your wrist. I killed him, and his bowmen saw enough to tell Kyonin exactly what I am. They're still hunting. If I want my story to get there before their next knife, I'd better write it now."''',
        c('"Then write it."', "alive_write"),
        c('"What would you say?"', "alive_say")),
], delay=24, RequiresAnyGroups=[[STALLED, AMULET]])   # the dead worlds stall the clock; the living one burns the amulet


# --- 3. Her tomb: a ride out to the stone the marksmen raised (the letter world only). --------------------------------

visit(HER_TOMB, "A very tasteful stone", [
    nar("open", '''{n}She wakes you before first light with two horses saddled and the shawl up to her eyes, and will not say where you are going until you are past the outer pickets. The road north is rutted by supply wagons and scored with the long drag-marks of something the scouts reported and nobody has named.{/n}
{n}The clearing is the one where Forn laid his trap. The stones are the same. The trees are the same. In the middle, where she fell, there is a tomb of pale grey stone with a wasp carved on the lid.{/n}''',
        c("Continue", "stone")),
    kay("stone", '''"They carved a wasp." {n}She gets down from the horse and walks all the way round it, slowly, with her hands behind her back like a sergeant inspecting a line.{/n}
"KAYLESSA OF THE SUNSET WASPS. SHE TOLD THE TRUTH." {n}She reads it aloud and stops.{/n} "That's all. No dates. No 'beloved'. Avennara always did hate an ornament."''',
        c('"It\'s a good stone."', "good"),
        c('"How does it feel?"', "feel")),
    kay("good", '''"It's very tasteful." {n}She puts her palm flat on the lid.{/n} "I'd like to be buried in it one day. Much later. By somebody who isn't in a hurry."''',
        c("Continue", "under")),
    kay("feel", '''"Like reading someone else's letters." {n}She puts her palm flat on the lid.{/n} "She was braver than me, the woman under this. She died on time."''',
        c("Continue", "under")),
    nar("scratch", '''{n}Before she mounts again she crouches by the foot of the tomb, draws the Kyonin dagger, and scratches something into the stone, low down where the moss will cover it by summer. You don't see what. When she stands, the blade has a pale crumb of stone on its tip, and she wipes it on her sleeve.{/n}''',
        c("Continue", "scratch_her")),
    kay("scratch_her", '''"Don't ask." {n}She sheathes it.{/n} "It's between me and her."
{n}She looks back once, from the saddle, at the pale stone in the clearing, with the red line of the Wound behind it.{/n} "If the thumb ever slips, soldier, bring me here. Not to the chapel in Drezen. Here. The marksmen already did the hard part."''',
        c("[Ride back beside her.]")),
    kay("under", '''"Is there anyone in it? Did they find me?" {n}She doesn't wait for an answer.{/n} "Don't tell me. I'd rather not know which of me is down there."
{n}She turns away from the stone. Behind her the Worldwound's light is a sore red line along the horizon.{/n}
"The marksmen who built this are in your army now, soldier. Fifty of them. I've heard them singing in the barracks at night. Kyonin songs I haven't heard since I was a girl."''',
        c('"I could bring you to them."', "bring"),
        c('"They don\'t have to know. Not unless you want them to."', "keep")),
    kay("bring", '''{n}She is quiet for a while, looking at the carved wasp. Then, without turning her head:{/n}
"Their captain. Only her. She was a wasp's sister once; she'll know what she's looking at." {n}A beat.{/n} "If she draws on me, soldier, you don't stop her. That's hers to decide."''',
        c("[Wait while she lingers at the stone.]", "scratch", flags=(MARKSMEN_TOLD,))),
    kay("keep", '''"Good." {n}It comes out faster than she means it to.{/n}
"Let them keep their martyr. She's better company than I am, and she never checks the clock in the mornings." "Thank you for riding out with me. I won't come often."''',
        c("[Wait while she lingers at the stone.]", "scratch", flags=(MARKSMEN_KEPT,))),
], requires=(RULES, RETURNED, TOMB, BEGGED), delay=48)


# --- 4. "Everyone's a soldier." ----------------------------------------------------------------------------------

meet(SOLDIER, "Everyone's a soldier", '"You never use my name. Why is that?"', [
    nar("open", '''{n}A squad of recruits goes past under the awning at the double, too young, their mail borrowed and badly fitted, a sergeant bawling at their heels. Kaylessa watches them out of sight.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Your name?" {n}She considers it.{/n} "Everyone's a soldier in a war, generals and privates alike. I've been telling people that since Mendev. I look at you and I see someone whose life is war and only war."
"Those boys there. Soldiers. The quartermaster with the ink on his fingers. Soldier. You." {n}She tips her cup at you.{/n} "Soldier."''',
        c('"And you?"', "you"),
        c('"I\'d like to hear you say my name."', "name"),
        c('"It\'s a way of keeping people at arm\'s length."', "length")),
    kay("you", '''"Me? I'm a deserter. From both sides." {n}She considers it.{/n} "Anemora's army and Kyonin's. That's rarer than a general. You should be honoured I sit with you."''',
        c('"You served Kyonin? Not only Calistria?"', "border"),
        c('"I\'d still like to hear you say my name."', "name")),
    kay("border", '''"Two summers on the border forts, before the Wasps. Avennara had the fort at the ford then; she taught me to shoot." {n}Something in her face softens and is put away again.{/n}
"She called all of us 'soldier', every recruit, because she couldn't be bothered learning names until we'd lived through a winter. I thought it was the coldest thing I'd ever heard. Then my first winter ended, and she called me Kaylessa, and I nearly cried in front of the whole fort."
{n}She turns the cup in her hands.{/n} "So now you know where I got it. Don't tell anyone. It ruins the effect."''',
        c('"I\'d still like to hear you say my name."', "name")),
    kay("length", '''"Of course it is." {n}She doesn't bother to deny it.{/n} "Names are handles, soldier. Anemora learned every one of ours. She'd whisper them at night, very softly, when she wanted us to do something. I learned to hate the sound of my own."''',
        c('"I\'d still like to hear you say mine."', "name")),
    kay("name", '''{n}She studies you, deciding something.{/n}
"No." {n}Not unkind. Quite gentle, for her.{/n} "Not yet. Names are for people who've lived through the winter. Ask me when the war's over."
"Once. When it counts. You'll know."''',
        c('"I\'ll wait."', "wait"),
        c('[Flirt] "Then I\'ll have to make it count."', "count")),
    kay("wait", '''"I know you will. That's the irritating part." {n}She stands, and pulls the shawl up.{/n} "Walk me to the end of the street, soldier. The recruits are back, and they stare."''',
        c("[Walk her to the end of the street.]", "street")),
    nar("street", '''{n}At the end of the street the recruits are forming up to march for the northern forts, stamping in the cold. One of them, a boy with a borrowed helmet down over his ears, sees the Commander and straightens so hard his spear-butt cracks on the cobbles.{/n}
{n}Kaylessa watches him go past with the column.{/n}''',
        c("Continue", "street_her")),
    kay("street_her", '''"Soldier." {n}She says it to his back, quietly, the way you'd say it to a son. He doesn't hear.{/n}
{n}She turns to you.{/n} "That's what it's for, you see. So you can say it to the ones you won't see again, and it doesn't cost anything." {n}A pause.{/n} "Your name would cost me something. That's why I'm saving it."''',
        c("[Watch the column out of sight with her.]")),
    kay("count", '''"Careful." {n}There's something warm under the dryness, and she doesn't bother to hide it.{/n} "I've heard that tone from worse people than you, and none of them are breathing. Try harder."''',
        c("[Walk her to the end of the street.]", "street")),
], requires=(THE_WASP,), delay=24)


# --- 5. After curfew: the city in the dark, and a kiss. -----------------------------------------------------------

meet(IN_THE_DARK, "After curfew", '"Walk with me. After the lamps go out."', [
    nar("open", '''{n}Drezen after curfew is a different city. The lamps are doused along the whole west side on account of the vrocks, which hunt by light, and the streets are rivers of black between darker walls.{/n}
{n}Kaylessa takes your wrist at the edge of the market and keeps hold of it.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Whatever your eyes are, soldier, they aren't mine. I can see the mortar between the bricks." {n}Her voice is close by your shoulder, and amused.{/n}
"Three steps down. Now left. There's a dead cat, don't be squeamish. This is my city, soldier. The one you all walk through at noon never sees it."''',
        c('"How far does it go? Your sight."', "sight"),
        c("[Let her lead you.]", "lead")),
    kay("sight", '''"Far enough to see a man on a wall before he sees me. Not far enough to see what's coming." {n}She turns you by the wrist around a corner you did not know was there.{/n}
"It was a gift. From the curse. The only thing it ever gave me that I'd keep." {n}A pause.{/n} "That, and teeth."''',
        c("Continue", "powder")),
    nar("lead", '''{n}You let her. Her hand on your wrist is cool and dry and never hesitates. You go down stone steps, across something that squelches, under an arch that drips. Somewhere above, a sentry coughs and does not look down.{/n}''',
        c("Continue", "powder")),
    kay("powder", '''"Forn found it out, the first time we fought. That I see in the dark and hate the light." {n}Her voice goes flat.{/n}
"He threw some alchemist's powder at my face. It went off like a star falling. I screamed, soldier. I screamed the way I made other people scream, and I couldn't see for two days, and I had to crawl into a drainage ditch and wait for my eyes to come back."
{n}Her fingers tighten on your wrist.{/n} "So you understand. I don't bring people into the dark to frighten them. It's the only place I'm not afraid."''',
        c('"I understand."', "sentry"),
        c('"Then I\'m glad you brought me."', "sentry")),
    nar("sentry", '''{n}A lantern swings round the corner ahead: a watchman, late on his round, holding it high. Before you can move she has you by the coat and back into a doorway, flat against old wood, her body against yours and her hand over your mouth.{/n}
{n}The light goes past a yard away. You see her face in it for a heartbeat, eyes screwed shut against the glare, teeth bared. Then the dark closes again, and she lets her breath out against your neck, slowly.{/n}''',
        c("Continue", "sentry_her")),
    kay("sentry_her", '''"Sorry." {n}She moves her hand from your mouth to your chest.{/n}
"Habit. Two years of lanterns meaning somebody wants me dead." {n}Her voice is low and not quite steady.{/n} "You let me put you against a wall in the dark. You didn't pull away. Didn't strike me. Do you know how rare that is?"''',
        c("Continue", "stop")),
    nar("stop", '''{n}She stops. You don't know why. You can hear her breathing, close, and feel the edge of her cloak against your hand, and the warmth coming off her through the cold.{/n}''',
        c("Continue", "here")),
    kay("here", '''"You're looking straight at me, soldier, and you're not looking at the fangs. It's very strange. Nobody looks at me like that." {n}A breath.{/n} "As if they don't know what I am."''',
        c("[Kiss her]", "kiss", flags=(KISSED,)),
        c("[Wait.]", "hers", flags=(KISSED,)),
        c('"I know exactly what you are."', "know", flags=(KISSED,))),
    nar("kiss", '''{n}You find her by her breath. Your mouth misses, lands on the corner of hers, and she makes a small impatient sound and fixes it. The kiss is cold at first, then not. Her fangs graze your lip and draw back, very carefully, as if she has been rehearsing how not to hurt.{/n}''',
        c("Continue", "after")),
    nar("hers", '''{n}Nothing, and then her hand on your jaw, turning your face a fraction to the left, the way you'd aim a bow. She kisses you as if she is checking something. Then again, as if the answer surprised her. Her fingers stay on your jaw the whole time, light, keeping your face where she put it.{/n}''',
        c("Continue", "after")),
    kay("know", '''"Do you." {n}Her hand comes up and rests against your chest, flat, pushing nothing.{/n} "Good. Then you won't be surprised."
{n}She kisses you. It is brief and hard and cold, and she steps back from it before you can answer it.{/n}''',
        c("Continue", "after")),
    kay("after", '''{n}She lets out a breath that is almost a laugh.{/n} "That was stupid." {n}She does not step away.{/n}
"Somewhere up there a vrock is deciding whether to eat a sentry, and the Worldwound is a day's ride off, and I'm standing in a gutter kissing the crusade's Commander by feel." {n}Her hand finds your wrist again.{/n} "Come on. I'll take you back to the light, before I start liking it here with you."''',
        c("[Let her lead you back.]")),
], requires=(SOLDIER,), delay=24)


# --- 6. Restringing: the bow on the wall at night. ----------------------------------------------------------------

meet(THE_BOW, "Restringing", '"Is that a new string?"', [
    nar("open", '''{n}She has the bow across her knees and a new string in her teeth, working it onto the nock with the patience of a woman who has done it in the rain, in the dark, under fire.{/n}''',
        c("Continue", "early", requires=(STALLED,), forbids=(BEGGED,)),
        c("Continue", "begged", requires=(BEGGED,)),
        c("Continue", "alive", requires=(AMULET,))),
    kay("early", '''"You're staring at the wood." {n}She seats the string.{/n} "You broke this bow. I remember the sound it made. And here it is, whole, not a splinter out of place, because it came from a branch where you never swung at me."
"Sometimes I pick it up expecting it to come apart in my hands."''',
        c("Continue", "wall")),
    kay("begged", '''"This bow never came out of Forn's clearing. In your world it's lying there under the leaves, rotting, next to me." {n}She seats the string.{/n} "This one came with me from the branch where I walked away."
"Same knots on the grip. Same crack by the upper nock that I keep meaning to bind. Exactly the same. I hate that more than I can tell you."''',
        c("Continue", "wall")),
    kay("alive", '''"Same bow I had in Kenabres. It's the only thing I own that's older than the curse." {n}She seats the string.{/n}
"I strung it new for the ravine and it held. I'm stringing it new again because I'd like to shoot something tonight that isn't an elf."''',
        c("Continue", "wall")),
    kay("wall", '''"Come up on the wall with me. There's a vrock that's been working the west side for a week. The sentries can't see it until it's on them." {n}She stands and slings the bow.{/n} "I can."''',
        c("[Go up on the wall with her.]", "up")),
    nar("up", '''{n}The west wall is dark, the watch-fires banked low on her say-so. Below, the city is a black bowl. Above, the sky over the Worldwound glows like a coal someone keeps blowing on.{/n}
{n}She sets you against the parapet and puts the bow in your hands.{/n}''',
        c("Continue", "stance")),
    kay("stance", '''"No. Your feet are wrong." {n}She moves them with her boot. Then she stands close behind you, her chest to your back, and reaches round to set your hands on the grip and the string.{/n}
"Draw to the corner of your mouth. Not your ear, you're not a Kyonin show-archer. Breathe out. Don't grip; the bow knows when you're scared."
{n}Her breath is on your neck. Her voice has dropped very low.{/n} "There. Two o'clock. Something big, gliding. Follow my aim, soldier."''',
        c("[Loose where she tells you.]", check=dict(Skill="SkillAthletics", DC=18, Success="hit", Failure="miss")),
        c("[Hand her back the bow.]", "hers")),
    nar("hit", '''{n}You loose into nothing. A heartbeat later something screams in the dark over the rooftops, a vast ugly sound, and wings beat away east, lopsided.{/n}''',
        c("Continue", "hit_her", flags=(DREW_THE_BOW,))),
    kay("hit_her", '''"You hit it!" {n}For a heartbeat she sounds eighteen. Then she catches herself.{/n} "In the wing. Badly. It'll be back." {n}She doesn't step away from behind you. Her hands stay on yours on the bow.{/n}
"That was good, soldier. Don't let it go to your head."''',
        c("Continue", "close")),
    nar("miss", '''{n}The arrow goes somewhere into the dark. Nothing screams. Kaylessa takes the bow out of your hands, nocks, draws and looses in one movement, and something above the rooftops shrieks and goes flapping east.{/n}''',
        c("Continue", "miss_her")),
    kay("miss_her", '''"Next time." {n}She doesn't sound disappointed. She sounds like she's already planning the next time.{/n} "Your hands are good. Let me sight it next time. Hold till I tell you."''',
        c("Continue", "close")),
    kay("hers", '''"Coward." {n}But she takes it, and nocks, and draws, and looses in one movement, and something above the rooftops shrieks and goes flapping east.{/n}
"There. That one's for the sentry it ate on Toilday."''',
        c("Continue", "close")),
    nar("close", '''{n}Neither of you moves. The watch-fires crackle. Down in the city a dog barks at the noise and gives up. Her arm is still round you, her cheek against your shoulder, and she seems to have forgotten to take either of them back.{/n}''',
        c('"We should do this more often."', "often"),
        c("[Say nothing. Stay.]", "stay")),
    kay("often", '''"Shoot vrocks?" {n}She takes her arm back, slowly.{/n} "It's a war, soldier. We'll get the chance."''',
        c("Continue", "sentries")),
    nar("sentries", '''{n}On the way down the stair you pass the relief watch coming up: four crossbowmen, a sergeant with a lantern he covers when he sees who is with you. He salutes you. He looks at her, wrapped to the eyes, bow on her back, and doesn't ask.{/n}
{n}At the bottom of the stair she stops.{/n}''',
        c("Continue", "sentries_her")),
    kay("sentries_her", '''"He'll say there's an elf archer on the west wall at night now. They'll start calling me the Commander's ghost." {n}She seems to like it more than she wants to.{/n}
"Good. A ghost can stand a watch. A drow can't." {n}She touches the bow on her back.{/n} "Tell your sergeants to leave the west fires low when the vrocks are working. I'll be up there. Not every night. Enough."''',
        c("[Walk her back to the market.]")),
    kay("stay", '''{n}Eventually she does remember, and moves, and doesn't apologise for it.{/n} "Come on. The watch changes soon, and I don't want the new sergeant writing down that the Commander was on the west wall in the dark with a drow wrapped round {mf|him|her}."''',
        c("[Walk down with her.]")),
], delay=24, RequiresAnyGroups=[[STALLED, AMULET]])


# --- 7. The other you: what the branch that lived remembers (dead worlds only). -----------------------------------

meet(OTHER_YOU, "The other one", '"You keep looking at me like I\'m someone else."', [
    kay("start", '''"Because you are. A little." {n}She says it without cruelty. The market is loud with a muster: pikemen being told off for the northern forts, their families standing about pretending not to cry.{/n}
"In the branch I came from, you were there too. The Commander of the crusade, with a laugh I still remember. I remember you. I remember both of you, and you don't quite match."''',
        c('"How don\'t we match?"', "how"),
        c('"Was the other one better?"', "better")),
    kay("how", '''"Small things." {n}She turns the cup between her palms.{/n} "That Commander's laugh was short. Always sounded like a cough. I knew it before I saw their face. Here I still turn round expecting to hear it."
"They knew me on the road. They never had to pay Shyka for me. I wasn't dead there."''',
        c("Continue", "shyka_raised", requires=(SHYKA_RAISED,), forbids=("kaylessa.trickster.dead.borrow_sending",)),
        c("Continue", "shyka", forbids=(SHYKA_RAISED,)),
        c("Continue", "shyka_sending", requires=(SHYKA_RAISED, "kaylessa.trickster.dead.borrow_sending"))),
    kay("better", '''"Better?" {n}She considers it.{/n} "I can't give you a report on that, soldier. I knew that Commander on the road. I know you here. Different days, different things to be afraid of."
"They never had to buy me back. I wasn't dead there."''',
        c("Continue", "shyka_raised", requires=(SHYKA_RAISED,), forbids=("kaylessa.trickster.dead.borrow_sending",)),
        c("Continue", "shyka", forbids=(SHYKA_RAISED,)),
        c("Continue", "shyka_sending", requires=(SHYKA_RAISED, "kaylessa.trickster.dead.borrow_sending"))),
    kay("shyka", '''"Shyka paid me a visit last night. It wore my face, then yours, then a goat's." {n}She grimaces.{/n}
"It asked if I liked the accommodation. Like a landlady with a room full of rats. I told it I'd let it know. Then it was gone, and I had to drink the tea it hadn't touched."''',
        c("Continue", "branch")),
    kay("branch", '''"I stayed on the road there. Mendev, the border, a ditch, another ditch. The beast kept coming. The last place I remember is a barn, and this dagger laid across my knees." {n}She looks toward her boot.{/n}
"Then Shyka brought me here. I don't know what would have happened next. I know what was in my hand."''',
        c('"Then this is the better branch."', "better_branch"),
        c("[Say nothing.]", "which")),
    kay("better_branch", '''"For me? I'm standing here drinking tea. I was freezing in that barn." {n}She almost laughs.{/n} "Ask me again on a bad morning, soldier."''',
        c("Continue", "which")),
    kay("shyka_raised", '''"Shyka paid me a visit last night. It wore my face, then yours, then a goat's." {n}She grimaces.{/n}
"It told me you tried to lower the price and made it worse. It was delighted. Somewhere you've said yes and meant every word, and it has that somewhere put away. I didn't like its face when it said that."''',
        c("Continue", "branch")),
    kay("which", '''"I keep comparing you with someone you never met. It's a rotten habit." {n}Her fingers stop turning the cup.{/n}
"I watch for you in the market now. When you come under the awning, I want you to stay. Even when you say something stupid. That's new, soldier. That's here."''',
        c('"Maybe it\'s you that\'s different."', "her"),
        c('[Flirt] "I\'ll take that as a compliment."', "compliment")),
    kay("her", '''"Maybe." {n}She studies you.{/n} "I'm tired of watching the gate for the next man who wants me dead. I like seeing you instead. Don't let it go to your head."''',
        c("[Leave it there.]")),
    kay("compliment", '''"Take it however you like. I only said it because it's true, and rule three cuts both ways." {n}She looks away, at the muster, and doesn't take it back.{/n}''',
        c("[Leave it there.]")),
    kay("shyka_sending", '''"Shyka paid me a visit last night. It wore my face, then yours, then a goat's." {n}She grimaces.{/n}
"It said you'd called into an empty hall until it answered. Then you paid what it asked. Somewhere you've said yes and meant every word. It has that somewhere put away, soldier. It was pleased with itself."''',
        c("Continue", "branch")),
], requires=(RULES, STALLED), delay=48)


# --- 8. Hands: the women she watches (acknowledgments, in her voice only). ----------------------------------------

meet(HANDS, "Hands", '"Who are you watching?"', [
    nar("open", '''{n}She's watching the square. Not the crowd; the hands in it. A pickpocket working a queue at the grain dole. A sergeant fingering his purse. A crusader touching the holy symbol at her throat, over and over, every time the bell for the northern muster rings.{/n}''',
        c("Continue", "start")),
    kay("start", '''"Everyone. Hands tell you what faces don't. I learned that before Anemora, and then again after, when I was the one being watched." {n}She nods toward the citadel.{/n}
"You keep interesting company, soldier. Some of them I've met. Some of them have met me."''',
        c("Continue", "camellia_killed", requires=(CAM_KILLED,)),
        c("Continue", "camellia", forbids=(CAM_KILLED,))),
    kay("camellia_killed", '''"Your shaman. The one with the lilies. She's the one who asked everyone else to give us privacy, at the end." {n}Her thumb goes to her collarbone.{/n}
"I'm not going to ask you to choose, soldier. I'm not a child, and it's not a choice I'd win. If she's still at your side, keep her." {n}Her voice doesn't change at all.{/n} "I'll watch her hands. That's all. Every time she's in a room with me, I'll know exactly where both of them are."''',
        c('"That seems fair."', "anevia_route"),
        c('"She won\'t touch you again."', "promise")),
    kay("promise", '''"You can't promise that. Nobody can promise what that one does." {n}She doesn't sound angry. Only precise.{/n} "Don't make promises for other people's knives, soldier. Just keep your own where I can see it."''',
        c("Continue", "anevia_route")),
    kay("camellia", '''"Your shaman, if she's still with you. The one with the lilies and the soft voice." {n}She watches something only she can see.{/n}
"She looks at people the way a butcher looks at a queue. I've seen that look. I used to wear it, on nights when the names came in." {n}A shrug.{/n} "I'm not telling you anything. I'm telling you I'll watch her hands. That's all."''',
        c('"That seems fair."', "anevia_route")),
    kay("anevia_route", '''"And then there's the other one. The one with the knives."''',
        c("Continue", "caught", requires=(CAUGHT,)),
        c("Continue", "unmasked", requires=(UNMASKED,), forbids=(CAUGHT,)),
        c("Continue", "gate", forbids=(CAUGHT, UNMASKED))),
    kay("caught", '''"She caught me in your war camp. She sat about looking bored for hours, waiting for me to bite, and I bit." {n}Grudging respect.{/n}
"She knocked the amulet out of my hand so fast I never saw her move. It went off into nowhere with a pop. Took me a month to find another way out of tight corners." {n}She rubs her wrist.{/n} "I'd like a rematch. I'd like it very much. I'd lose."''',
        c("Continue", "end")),
    kay("unmasked", '''"The war camp. I tore the mask off my own face in front of you because I was sick of hiding behind it." {n}She pulls the shawl up now, from habit.{/n}
"Your people were very polite about it. Too polite. There was a woman with a limp by the quartermaster's tent who didn't look polite at all. She looked like she was measuring me for a cell. I've avoided her since. She's good."''',
        c("Continue", "end")),
    kay("gate", '''"The woman who watches your gate. The one with the limp." {n}Something that is nearly approval.{/n}
"She knew I was here the second day. She's never said a word. She just stands so I can see her knowing it. That's how you tell a real watcher from a guard: a guard wants to catch you, a watcher wants you to know you're caught."''',
        c("Continue", "end")),
    kay("end", '''{n}She pulls her attention back from the square, with an effort.{/n}
"I'm not asking you to tell me who any of them are to you, soldier. I don't care. I care where their hands are." {n}A pause.{/n} "Yours I've decided about. Yours I don't watch any more. Don't make me start."''',
        c('"I won\'t."', "wont"),
        c('"That\'s the kindest thing you\'ve ever said to me."', "kind")),
    kay("wont", '''"Good." {n}She goes back to the square.{/n}''',
        c("Continue", "mine")),
    kay("mine", '''{n}After a while she holds up her own hands in front of her, backs toward you, as if showing a sergeant they were clean.{/n}
"And these I watch hardest of all. They did things in the Worldwound that I only remember in the mornings. They're very good hands. Steady. Anemora said so." {n}She lowers them.{/n}
"If you ever see them doing something I wouldn't do, soldier, you tell me. Loudly. Don't be polite about it. Politeness is how she got in the first time."''',
        c('"Loudly. I promise."', "kind_end"),
        c("[Take one of her hands in yours.]", "kind_end"),
        c('[Hold out your hand] "Kenabres. I\'ve had these on you before, and you watched every move they made."', "kenabres",
          requires=(EARLY_BOUND,)),
        c('"In Kenabres you told me a stranger\'s prayer was a sin to your mother\'s people. Was that true?"', "kenabres_lie",
          requires=(EARLY_LIED,))),
    kay("kenabres", '''{n}She looks at the hand you hold out, and then, for once, at your face.{/n} "Kenabres. A city burning, and you knelt in the street and tied a stranger's side shut with linen because she'd told you no spells, and you listened." {n}She turns your hand over, palm up, the way she watched it work that day.{/n}
"I told you then your hands didn't lie. I've been checking ever since, soldier. They still don't." {n}She lets go.{/n} "Don't make anything of it."''',
        c("Continue", "kind_end")),
    kay("kenabres_lie", '''"No." {n}The corner of her mouth goes up.{/n} "There's no such people. I made them up in the time it took your knot to slip."
"The truth's shorter. Anemora had me a long time, and things were done to me there that I couldn't stop. I won't lie still for anyone's hands or anyone's prayers again unless I say so. Not a priest's, not a friend's." {n}She looks back at the square.{/n} "You suspected it was a lie, and you let me keep it. I noticed that too."''',
        c("Continue", "kind_end")),
    kay("kind_end", '''{n}She lets it sit there, whatever you did, and goes back to watching the grain dole, where the pickpocket has been caught at last and is being marched off by a very tired corporal.{/n} "There. Justice. Very dull, when somebody else does it."''',
        c("[Watch the square with her.]")),
    kay("kind", '''"Then you've had a very sad life." {n}But she knocks her shoulder against yours before she goes back to the square.{/n}''',
        c("Continue", "mine")),
], delay=48)


# --- 9. The Winter Council: the letter she writes, and where it goes. ---------------------------------------------

meet(KYONIN, "The Winter Council", '"You\'re writing something."', [
    nar("open", '''{n}There's a board across her knees and a sheaf of cheap crusade paper on it, the kind the clerks use for requisitions. Half of it is covered in a small hard hand. The rest is crossed out. A dispatch rider clatters past the awning with news from the north, and she covers the page without looking up.{/n}''',
        c("Continue", "start")),
    kay("start", '''"To Avennara. At the border. Everything, this time: the Wasps, Anemora, the Dark Fate, Forn." {n}She taps the page.{/n}
"Do you know what the Winter Council is, soldier? Nobody does, properly. A clique of old names in Kyonin. They keep the honour of the elves the way a cook keeps a stew: stirring, skimming, and throwing out anything that floats up looking wrong."''',
        c('"And you floated up looking wrong."', "wrong"),
        c('"Forn called it duty."', "duty")),
    kay("wrong", '''"I floated up looking like the truth. Any elf can become a drow. Any one of them. That's what the Council can't have, not ever: the whole of Kyonin looking in a mirror and seeing me."
{n}She crosses out a line.{/n} "So they kill everyone who's heard it. Forn used to say they were protecting the innocent. I think he believed it."''',
        c("Continue", "honour")),
    kay("duty", '''"He did. He called it duty and he called it honour and he called it circumstances stronger than our desires." {n}She mimics his sad, careful voice exactly, and it isn't funny.{/n}
"He killed a shepherd in Mendev who'd once given me bread. Because I might have talked to him. That was Forn's duty."''',
        c('"You never told me about the shepherd."', "shepherd"),
        c("Continue", "honour")),
    kay("shepherd", '''"Old man. Half deaf. Kept goats above the Sellen, where the crusade's supply barges put in." {n}She's not looking at you.{/n}
"I came down out of the hills starving, the second month after I ran, and he gave me black bread and goat's cheese and didn't ask why I kept my hood up. He talked the whole time about his wife, who was dead, and the barges, which were late."
"Forn found his hut a week behind me. I went back to thank him, later, and there was nothing but the dog, sitting by the door, waiting." {n}Her pen has gone through the paper.{/n} "His name's on the list at the bottom. Somebody should know it."''',
        c("Continue", "honour")),
    kay("honour", '''"I wrote something once, when I thought I was dying. 'I believe that truth is greater than gain. I always have.'" {n}She almost smiles.{/n} "Very noble. Very young. I still believe it, though. That's the embarrassing part."''',
        c("Continue", "tomb", requires=(TOMB,)),
        c("Continue", "seal", forbids=(TOMB,))),
    kay("tomb", '''"Avennara already has the first letter. Your letter. The one that got me a stone. This is the second one." {n}She taps the page.{/n} "The one that says: I got better. And the Council's still lying."''',
        c("Continue", "seal")),
    kay("seal", '''{n}She signs it with a single letter, K, and a small scratch that might be a wasp.{/n}
"The question is how it goes. If I send it by any courier in Mendev, the Council will have it before it's out of the country. They read everything that goes east." {n}She holds it out, not quite to you.{/n}
"If it goes under the crusade's seal, they'd have to break the Knight Commander's seal to read it. And then they'd have to explain that to your allies."''',
        c('[Send it under the crusade\'s seal] "It goes with the next dispatch. My seal, my name."', "sent",
          flags=(LETTER_SENT,), crusade=("Favors", -100)),
        c('"Keep it. Carry it yourself, one day, when you can walk into Kyonin with it."', "kept", flags=(LETTER_KEPT,))),
    kay("sent", '''{n}She looks at the seal pressed into the wax, the crusade's arms, still warm.{/n}
"You know what this costs you. Kyonin's envoys will be very cold at your table for a year. Somebody's archers won't arrive when they were promised." {n}She puts the letter into your hands herself.{/n}
"I know you know. That's why I'm letting you."''',
        c("[Put it in the dispatch bag.]", "after")),
    kay("after", '''{n}She watches the letter go into the bag as if it were a child leaving on a ship.{/n}
"Avennara will read it at the ford, by the fire, with her boots off. She reads everything twice, the second time out loud to whoever's on watch, whether they want it or not." {n}A breath that is almost a laugh.{/n}
"Somebody on her watch tonight is going to hear that any elf can become a drow, read out in Avennara's voice, with her feet in the ashes. And then it's out. Nobody can put it back. Not the Council, not anybody."
{n}She sits back against the post of the awning and closes her eyes.{/n} "I've wanted that for two years, soldier. I didn't know it would feel like falling."''',
        c('"Like falling where?"', "falling"),
        c("[Sit with her until the rider leaves.]")),
    kay("falling", '''"Down. Out of a window. The good kind of falling, where you've already decided and it's too late to be sorry." {n}She opens one eye at you.{/n} "Don't make a joke about it. I'll push you out of one."''',
        c("[Sit with her until the rider leaves.]")),
    kay("kept", '''"One day." {n}She folds the letter small and puts it inside her cloak, with whatever else she keeps against her ribs.{/n}
"You're right. It should be me who walks in with it. Not a courier, not a seal. Me, with my own face." {n}A dry sound.{/n} "They'll hate that much more."''',
        c("Continue", "walk_in")),
    kay("walk_in", '''"I can see it. The Council's hall at the ford fort, all white wood and good manners. Me in the doorway, no hood, no amulet, no courier's grey. Every one of those old faces trying very hard not to look at my teeth." {n}She smiles, and it is not kind.{/n}
"I'll hand it to Avennara in front of all of them and ask her to read it aloud. She will. She never could resist a scene."
"After the war, soldier. When there's a road to walk it on."''',
        c('"I\'d like to be in that doorway with you."', "doorway"),
        c("[Leave her to her writing.]")),
    kay("doorway", '''"Would you." {n}She considers it, seriously.{/n} "The crusade's Knight Commander at my shoulder while I tell Kyonin its dirty secret. They'd say I'd sold the truth to the crusade." {n}A pause.{/n} "They'd say it anyway. Come if you like. Stand where they can see your hands."''',
        c("[Leave her to her writing.]")),
], requires=(LAST_WORDS,), delay=24)


# --- 10. "That blasted Kaylessa": Anemora at Iz (Chapter 5). ------------------------------------------------------

meet(ANEMORA, "That blasted Kaylessa", '"You\'ve been to Iz."', [
    kay("start", '''"You smell of it. Ash and old blood and the swarm." {n}She's standing, not sitting, and the bow is strung. Beyond the awning the city is still counting who came back.{/n}
"She was there. Anemora. Don't tell me she wasn't. That city was hers the way the Worldwound is Deskari's."''',
        c("Continue", "told", requires=(ANEMORA_TOLD,)),
        c("Continue", "dead", requires=("iz.anemora_dead",), forbids=(ANEMORA_TOLD,)),
        c("Continue", "else", forbids=(ANEMORA_TOLD, "iz.anemora_dead"))),
    nar("told", '''{n}You tell her. That you asked Anemora about her acolytes, the elves from Kyonin; that Anemora laughed and called them sweet fools, and said it had been so amusing to deprave them, and that none of them had the nerve to refuse her. None, except for that blasted Kaylessa.{/n}''',
        c("Continue", "told_her")),
    kay("told_her", '''{n}She is quiet for so long that the crier across the square finishes a whole list.{/n}
"'That blasted Kaylessa.'" {n}She says it slowly, tasting it.{/n} "She remembered me. Out of all of them, she remembered the one who said no."
{n}And then, to your astonishment, her eyes are wet.{/n} "Two years, soldier. Two years of thinking I was nothing to her but a spoiled experiment. And I was the one she couldn't forget."''',
        c("Continue", "after")),
    kay("dead", '''"She's dead, isn't she. You killed her." {n}She reads it off your face.{/n}
"Without me. You went into her city and you killed her, and I was here under an awning buying bread." {n}Her knuckles are pale on the bow.{/n}
"I should hate you for that. I've been saving that death for two years. I'll settle for making you tell me exactly how she looked at the end. Every detail. Don't spare me."''',
        c('[Tell her everything] "She didn\'t die well."', "dead_told"),
        c('"She died like she lived. Laughing."', "dead_told")),
    kay("dead_told", '''{n}She listens to all of it with her eyes closed, the way some people listen to music.{/n}
"Good." {n}Just that.{/n} "Good. The swarm has one less mother." {n}She opens her eyes.{/n} "It doesn't make me an elf. It doesn't take back one night of it. But she's in the ground, and I'm standing in the market, and that's the right way round."''',
        c("Continue", "after")),
    kay("else", '''"And she's still there, isn't she? You went into her city and came out, and she's still alive in it." {n}She isn't accusing you. She's calculating.{/n}
"Don't. Don't tell me you'll kill her for me. I don't want her given to me like a present. When the day comes, I'd like to be standing close enough to see her face."''',
        c('"Then come with me next time."', "come"),
        c('"I\'ll leave her for you."', "come")),
    kay("come", '''"We'll see." {n}Her mouth has gone thin.{/n} "She made twenty wasps into her pets, soldier. She'd love the chance to see what she can make of a Commander." {n}A pause.{/n} "Don't go near her alone. I mean it."''',
        c("Continue", "after")),
    kay("after", '''"She was never an elf. Did you know that? She's a true drow, born in the dark, never anything else. She just liked to wear us." {n}She unstrings the bow with a single hard pull.{/n}
"The worst of it is that I understand her now. A little. I know what it's like to want to see someone kneel. I've felt it in your city, more than once." {n}She looks at you.{/n} "That's what she really left me. Not the skin. The understanding."''',
        c('"It\'s not the same thing."', "same"),
        c("[Put your hand over hers on the bow.]", "hand")),
    kay("same", '''"No. It isn't. She enjoyed it and never stopped. I enjoy it and hate myself." {n}Bitter.{/n} "I'm told that's the difference between a monster and a soldier."''',
        c("Continue", "swarm")),
    kay("swarm", '''"Do you know what she kept in herself? Under the skin? Locusts. Swarms. She'd let them out at dinner sometimes, to watch us not flinch." {n}Her lip curls back from her fangs.{/n}
"Twenty of us, elves from the best houses in Kyonin, sitting at her table with insects walking across our plates, eating anyway, because she was watching to see who'd flinch. I flinched. Every time. It was the only thing I had left that was mine."
{n}She pulls the unstrung bow across her knees.{/n} "So when you tell me I'm not like her, soldier, I'll believe you. But I'll keep flinching. Just to be sure."''',
        c("[Stay with her.]")),
    kay("hand", '''{n}She doesn't pull away. She turns her hand over under yours, so your palms meet, and holds on, hard, for as long as it takes the crier to finish the list.{/n}''',
        c("[Stay with her.]")),
], chapters=(5,), delay=24, RequiresAnyGroups=[["iz.done", "iz.anemora_dead", ANEMORA_TOLD]])


# --- 11. Burned from within: the child with the crow (friendship tone; Ember is not in the scene). --------------------

meet(BURNED, "Burned from within", '"You\'re quiet."', [
    kay("start", '''"I'm thinking about Kenabres." {n}She's watching a pair of children chase each other round a water trough, dodging a column of wounded coming in from the north gate on stretchers.{/n}
"There was a girl with you. In Kenabres, when I was bleeding and you found me. Freckles. A crow on her shoulder. She looked at my wounds like a physician."''',
        c("Continue", "said")),
    kay("said", '''"She said they weren't like hers. That they'd burned her from the outside, but I'd been burned from within." {n}She says the words exactly, the way you remember something you've gone over many times.{/n}
"'It hurt, didn't it? I'm sorry that happened to you.'" {n}She is quiet.{/n} "Nobody had said that to me. Not in two years. A child, in a burning city, to a drow she'd never met."''',
        c('"That sounds like her."', "self"),
        c('"What did you say to her?"', "reply")),
    kay("reply", '''"Nothing. I glared at her." {n}A tired huff.{/n} "I was very busy being dangerous. She wasn't impressed. She just kept looking at me, the way you look at a hurt dog to see where it bites."''',
        c("Continue", "self")),
    kay("self", '''"I was a child in Kyonin once. Iadara. My mother kept bees on the roof, and I was stung so often I stopped crying about it." {n}A small, surprised sound, as if she had forgotten that.{/n}
"Maybe that's why I liked the Savored Sting, later. I already knew what it was to be hurt by something small and to go on anyway." {n}She shakes her head.{/n} "Your crow girl reminded me. That's all. I don't usually remember being small."''',
        c("Continue", "her")),
    kay("her", '''"She's the kind that believes everyone is warm inside, if you wait long enough." {n}She says it without mockery, which for her is remarkable.{/n}
"I'd like her to go on believing it, soldier. Keep her away from me when the clock's bad. Keep her away from anyone who'd teach her otherwise." {n}She watches the children at the trough.{/n} "If you see her, tell her the drow from Kenabres said thank you. Don't tell her anything else."''',
        c('"I\'ll tell her."', "tell"),
        c('"Tell her yourself, one day."', "yourself")),
    kay("tell", '''"Good." {n}She pulls the shawl a little higher, as if to keep something in.{/n}''',
        c("[Watch the children with her.]")),
    kay("yourself", '''"Maybe. When I'm sure what I'd be showing her." {n}She pulls the shawl a little higher.{/n} "Children should see monsters from a safe distance. It's educational."''',
        c("[Watch the children with her.]")),
], requires=(RULES, EMBER_MET), delay=48)


# --- 12. Noon: the light, and the Commander's shade. --------------------------------------------------------------

meet(NOON, "Noon", '"You look like the sun\'s trying to kill you."', [
    nar("open", '''{n}It's noon, and the one day in a month Drezen gets a clear sky. Half the garrison is drilling in the square with the sun flashing off their helmets, a sergeant counting cadence, the new recruits for the northern forts learning to lock shields. The shade under the awning has shrunk to a stripe.{/n}
{n}Kaylessa is pressed into what's left of it with the shawl over her eyes and her hand over the shawl.{/n}''',
        c("Continue", "start")),
    kay("start", '''"It is." {n}She doesn't take her hand away.{/n} "Every helmet in that square is a little knife in my eyes, soldier. Your crusade's very shiny. I'd noticed it before, but never so personally."''',
        c("[Stand between her and the square, so your shadow falls on her.]", "shade"),
        c('"Come inside. The citadel\'s dark enough."', "inside"),
        c('"I\'ll come back at dusk."', "dusk")),
    kay("shade", '''{n}Your shadow falls across her. She lowers her hand, cautiously, and looks up at you from under the shawl, squinting.{/n}
"You're blocking the whole square for me. The Knight Commander, standing about like a parasol." {n}She's trying not to laugh, and failing slightly.{/n} "Half your army can see you doing it."''',
        c('"Let them look."', "look"),
        c('"I\'m a very good parasol."', "parasol")),
    kay("look", '''"They are looking. The sergeant's lost count." {n}She settles back against the post, in your shadow, and closes her eyes, easily, like someone who's decided to trust a wall.{/n}''',
        c("Continue", "drill")),
    kay("parasol", '''"You are. Don't move. If you move, I'll have to go blind with dignity, and I've done that before. It's overrated." {n}She closes her eyes, easily, like someone who's decided to trust a wall.{/n}''',
        c("Continue", "drill")),
    kay("inside", '''"And have your chamberlain watch me sulk in a corner of your hall? No." {n}She peers at you.{/n} "I'm not a lamp you keep out of the draught, soldier. I'll sit here, and suffer, and look very dignified doing it."''',
        c("[Stand in front of her anyway.]", "shade")),
    kay("dusk", '''"Coward." {n}Almost fond.{/n} "Dusk, then. Bring wine. Something that isn't the quartermaster's vinegar." {n}She waves you off into the glare.{/n}''',
        c("Continue", "evening")),
    nar("evening", '''{n}At dusk the square is empty, the helmets gone, and she's sitting on the crate with the shawl down, colour back in her face, which for her means the deep slate of a cloudy night. She takes the wine without thanks and drinks half of it.{/n}''',
        c("Continue", "drill")),
    kay("drill", '''"Those recruits." {n}She nods toward the square.{/n} "Half couldn't lock a shield. One kept turning his head before the order. He'll be dead before he learns to stop."
"I keep counting which ones will come back. It's a filthy habit. Your sergeant ought to make himself useful before the north forts bury his work."''',
        c('"I\'ll accept the blame."', "blame"),
        c('"You could train them. Archery."', "train")),
    kay("blame", '''"Then put that sergeant to work." {n}She tips her chin toward the square.{/n} "Blame won't keep their heads attached."''',
        c("Continue", "sun")),
    kay("sun", '''"Do you know what I miss? Not Kyonin. Not the trees, whatever the songs say." {n}She squints at the last red light on the rooftops as if it were an enemy she respects.{/n}
"Noon. Lying on a warm roof in Iadara at noon with my eyes shut, and the light coming red through my eyelids. I used to do it for hours. My mother said I'd cook." {n}She lowers her gaze.{/n}
"I can't even look at it now. The Dark Fate took the sun off me like a cloak. Some mornings that's the worst of it. Worse than the teeth."''',
        c('"Then I\'ll be your noon."', "noon_flirt"),
        c("[Say nothing. Stay until the light goes.]")),
    kay("noon_flirt", '''"Gods, that's terrible." {n}She laughs, properly, a short startled sound that turns heads down the street.{/n} "That's the worst thing anyone has ever said to me, and Anemora said a great many things."
{n}She doesn't take her shoulder away from yours, though.{/n}''',
        c("[Stay until the light goes.]")),
    kay("train", '''"A drow teaching crusaders to shoot?" {n}She considers it far longer than a joke deserves.{/n} "At night. Only at night. And they'd have to think I was an elf with a skin disease." {n}A pause.{/n} "Ask me again when the clock's been good for a month."''',
        c("Continue", "sun")),
], delay=24)


# --- 13. "Like what you see?": desire said aloud, before the knife. ----------------------------------------------

meet(WHAT_I_WANT, "Like what you see?", '"You\'re not wearing the shawl."', [
    nar("open", '''{n}It's late. The market is shut, the awning's canvas creaking in a wind that smells of snow and the Worldwound's rot. She's sitting on the crate with the shawl in her lap and her face bare to the dark: slate skin, white cropped hair, the red eyes steady on you as you come in under the canvas.{/n}''',
        c("Continue", "start", requires=(FIRST_WORDS,)),
        c("Continue", "start_fresh", forbids=(FIRST_WORDS,))),
    kay("start_fresh", '''"What are you looking at, soldier?" {n}She lets it sit in the dark between you. Then her mouth curves.{/n} "Like what you see?"
"I used to say that to scouts I meant to rob. I've been wanting to say it to somebody and mean it. I notice everything about you. I've been trying to stop."''',
        c('"Yes."', "yes"),
        c('[Flirt] "I\'m still deciding. Come closer."', "closer")),
    kay("start", '''"What are you looking at, soldier?" {n}She says it exactly as she said it the day you met. Then her mouth curves.{/n} "Like what you see?"
"You didn't answer that, the first time. I noticed. I notice everything about you. I've been trying to stop."''',
        c('"Yes."', "yes"),
        c('[Flirt] "I\'m still deciding. Come closer."', "closer"),
        c('"I didn\'t answer because I didn\'t know you yet."', "know")),
    kay("yes", '''{n}She stands. It's two steps from the crate to you, and she takes them slowly, as if the ground might give.{/n}
"Good. Because I've been sitting here for an hour trying to decide whether I'm allowed to want anything, with a curse in my blood and a hunter in every shadow." {n}She stops close enough that you feel the cold of her.{/n}''',
        c("Continue", "want")),
    kay("closer", '''"Deciding." {n}She stands, and closes the distance, and stops a hand's width from you, chin up.{/n} "There. Closer. Decide faster, soldier; the clock's running and I don't know how long I've got."''',
        c("Continue", "want")),
    kay("know", '''"And now you do." {n}She stands. Two steps, slowly, and she's close enough that you can feel the cold coming off her through the dark.{/n} "So answer it."''',
        c("Continue", "want")),
    kay("want", '''"Here's what I want. I'll say it once, and then I don't want to talk about it." {n}Her hands come up and take hold of your coat, not gently.{/n}
"I want to be something other than Anemora's proof for one night. I want someone to look at this body she made and not flinch. I want your hands on me because you want them there, not because you're curing me or saving me or keeping me." {n}Her breath is quick.{/n} "And I want it badly. That's the part I didn't expect."''',
        c("[Kiss her.]", "kiss"),
        c('"Then have it."', "kiss")),
    nar("kiss", '''{n}She kisses you first. It's nothing like the one in the dark: deep and hungry and not careful at all, her body hard against yours, her fingers working at the buckles of your coat as if she has been thinking about them for a week. This time she doesn't guard her teeth, and you taste copper, and she laughs into your mouth about it.{/n}
{n}She pushes the coat off your shoulders. Your hands find the laces of the courier's grey at her throat. She arches into them, breathing hard, and then, all at once, catches your wrists.{/n}''',
        c("Continue", "stop")),
    kay("stop", '''"No. Not yet." {n}She's shaking, and not from cold.{/n} "Not like this, in a market, with the knife still in my boot and nobody holding it but me."
{n}She lets go of your wrists, slowly, one at a time.{/n} "After the knife. When I've decided who holds it. Then you can have all of it, soldier, and I'll take all of you, and I'll make you forget this damned market."''',
        c('"After the knife."', "after"),
        c('[Flirt] "I\'ll hold you to that."', "hold")),
    kay("after", '''"After the knife." {n}She laughs, unsteady, and presses her forehead against your shoulder.{/n} "Gods. Go away before I change my mind, soldier. Go away right now."''',
        c("[Go, slowly.]")),
    kay("hold", '''"I'm counting on it." {n}She picks your coat up off the ground and pushes it into your arms, and her eyes are burning red in the dark.{/n} "Now go. Before I break one of my own rules and you break one of yours."''',
        c("[Go, slowly.]")),
], requires=(IN_THE_DARK, KNIFE_SHOWN), forbids=(COMMITTED,), delay=24)


# --- 14. The goat: Woljif. ----------------------------------------------------------------------------------------

meet(WOLJIF, "The goat", '"Why is Woljif avoiding the market?"', [
    kay("start", '''"Your tiefling? Because I told him to." {n}She's peeling an apple with a cheap knife from the stall, not the one in her boot. A wagon of wounded is creaking past toward the infirmary, and she doesn't look at it.{/n}
"He tried to lift my purse on the second day. Very good hands. Terrible sense of when to use them. I caught his wrist and asked him politely what he thought a drow would carry in a purse in a crusader city."''',
        c('"What did he say?"', "said")),
    kay("said", '''"He said, 'Drow money, miss. You can't be too careful with drow money.'" {n}Her face doesn't move. Her eyes do.{/n}
"So I told him that if he said one word to anyone about who sits under this awning, I'd tell everyone about the goat."''',
        c('"What goat?"', "goat"),
        c('"There\'s a goat?"', "goat")),
    kay("goat", '''"I have no idea." {n}She eats a slice of apple.{/n} "There's always a goat, with a man like that. Somewhere in his past there's a goat, and a night, and a reason he doesn't drink cider. I didn't need to know which one. He supplied it himself. Went grey as porridge."
"Now he walks the long way round the market. It adds a quarter of an hour to his errands. The quartermaster's furious."''',
        c('"That\'s cruel."', "cruel"),
        c('"That\'s a Trickster\'s move."', "trickster")),
    kay("cruel", '''"It's education. He's a thief in a city full of hungry soldiers and a war that'll hang him for a loaf. He ought to know better than to lift purses from strangers." {n}She shrugs.{/n} "I was kinder than a sergeant."''',
        c("Continue", "end")),
    kay("trickster", '''"Is it? I learned it in Kyonin. Everybody has a goat. The Wasps found out the magistrates' goats, and after that we hardly had to cut anyone at all." {n}A glance.{/n} "Don't look so pleased. I don't know yours. Yet."''',
        c("Continue", "end")),
    kay("end", '''"Tell him he can come through the market again if he brings me a decent pair of gloves. Black. Soft." {n}She wipes the knife.{/n}
"And tell him if he ever steals from you, soldier, I'll find out what the goat really was." {n}She says it lightly. It is not light at all.{/n}''',
        c('"I\'ll tell him."', "tell"),
        c('"I think he\'d rather keep walking the long way."', "tell")),
    kay("tell", '''"Clever boy." {n}She hands you a slice of apple, off the point of the knife.{/n}''',
        c("[Eat it.]", "gloves")),
    nar("gloves", '''{n}Three days later there is a parcel on the crate under the awning, wrapped in a requisition form for bandages that somebody has carefully forged. Inside is a pair of black gloves, very soft, very good, in a size that fits her exactly.{/n}
{n}There is no note. There is a small charcoal drawing of a goat on the paper, with a line through it.{/n}''',
        c("Continue", "gloves_her")),
    kay("gloves_her", '''"Kid leather. Nerosyan work. There's a colonel's wife in the upper town who's going to be very cross this week." {n}She pulls them on, finger by finger, and flexes her hands.{/n}
"Tell him the market's open to him again." {n}A beat.{/n} "And tell him the goat's safe with me. Everybody deserves one secret nobody uses."''',
        c("[Promise to tell him.]")),
], forbids=("woljif.dead", "woljif.kicked_out"), delay=48)


# --- 15. The courier's face: the girl the amulet showed (the living world, after it burned out). ------------------

GIRLS_FACE = K + "the_girls_face"
TRANCE = K + "trance"
REMEMBERED_GIRL = K + "remembered_the_courier"

meet(GIRLS_FACE, "The courier's face", '"You keep touching your throat."', [
    kay("start", '''"Do I?" {n}She takes her hand away from the place where the amulet's cord used to sit, and looks at it as if it had been doing something without permission. Down the street a crier is shouting for volunteers to carry water to the northern forts, and nobody is volunteering.{/n}
"I wore that girl's face for a year. Freckles. A sunburnt nose. She had a way of smiling with one side of her mouth that I never could stop; the glamour did it for me."''',
        c('"Who was she?"', "who"),
        c('"Do you miss it? The face?"', "miss")),
    kay("who", '''"A courier of the Green Road. Anemora's people took her on the way to Mendev, with her letters. The amulet kept her face after they'd finished with the rest of her." {n}She rubs her throat, then stops.{/n}
"I never learned her name. Her face bought me bread for a year. Now the amulet's dead too."''',
        c("Continue", "miss")),
    kay("miss", '''"Miss it?" {n}She thinks about it honestly, which is what she does with every question you give her.{/n}
"I miss being looked at the way people looked at her. Politely. Like I was nobody in particular. That face could stand in a queue for the grain dole and nobody's hand went to a sword. This one can't." {n}She touches her own cheek, dark as slate.{/n} "This one's the only face I'll have now, soldier. The other one burnt out in the ravine. I'm not complaining. I'm telling you what it cost."''',
        c('"I\'d do it again."', "again"),
        c('"We could find out her name. Send it home."', "name"),
        c('"I like this one better."', "better")),
    kay("again", '''"I know." {n}She almost smiles.{/n} "The disguise is gone, and I'm here. Even knowing how it went, I'd take that chance again. That's what frightens me."''',
        c("[Stay with her.]")),
    kay("name", '''{n}She is quiet for a while.{/n} "Yes." {n}It comes out rough.{/n} "Yes. The Green Road keeps rolls. Someone at the border would know which girl didn't come back that summer. Her mother should get more than a letter saying lost."
"I'll put it in mine. To Avennara. The girl whose face I wore, and where she really ended up." {n}She looks at you.{/n} "Thank you. I'd never have thought of it. I was too busy being her."''',
        c("[Stay with her.]", flags=(REMEMBERED_GIRL,))),
    kay("better", '''"Liar." {n}But she doesn't say it the way rule three would.{/n} "Nobody likes this one better. They like it because they're supposed to be frightened of it, and that's more interesting than being bored."
{n}She tilts her chin up, all the same, and lets you look.{/n} "Go on, then. Look at it. It's the only one I've got."''',
        c("[Look at her.]")),
], requires=(RULES, AMULET), delay=48)


# --- 16. Four hours: elves trance, and she dreams now. -----------------------------------------------------------

meet(TRANCE, "Four hours", '"You look like you haven\'t slept."', [
    kay("start", '''"I haven't. I don't, not properly." {n}She has dark smudges under her eyes, visible even on her skin, and she's holding her tea with both hands. The bells for the night watch are ringing along the wall; somewhere north the sky flickers where the Wound is restless.{/n}
"I used to sleep like a stone, soldier. In Kyonin, in the Wasps' loft, eight of us in a row and me snoring loudest, they said. I slept the night before every job. I slept the night before Anemora."''',
        c('"And now?"', "now")),
    kay("now", '''"Now I lie down and I'm gone for an hour, and then I'm back, and I'm awake till the bells." {n}Her mouth twists.{/n} "I didn't notice it at first. I just noticed that the dreams had started."
"I dream about the Worldwound every night. The prisoners. Tessariel holding the lamp. The sound a person makes when you've found the right place." {n}She sips the tea without tasting it.{/n} "So I stay up, and sit under this awning, and watch your city not burn."''',
        c('"What do you dream when it isn\'t the Worldwound?"', "other"),
        c('"Sleep in the citadel. I\'ll sit up and watch."', "watch"),
        c('"I have bad dreams too."', "too")),
    kay("other", '''{n}She doesn't answer for a while.{/n} "Lately? A wall. The west wall, in the dark, and somebody's back against my chest, and a bow." {n}She says it to the tea.{/n}
"It isn't much of a dream. Nothing happens in it. That's why I like it."''',
        c("[Say nothing. Sit with her.]", "sit")),
    kay("watch", '''"You'd sit up. The Knight Commander, sitting up all night outside a door so a drow can have a nightmare in peace." {n}She shakes her head.{/n}
"No. If I wake up screaming, I don't want you there with a lamp. I'd go for your throat before I knew whose it was." {n}A pause.{/n} "Ask me again when I trust my hands."''',
        c("[Sit with her anyway.]", "sit")),
    kay("too", '''"I know. I've heard you." {n}Her glance is sidelong.{/n} "Your windows face the market, soldier. You talk in your sleep. Mostly orders. Once, a name I didn't know."
"I didn't tell anyone. I'm not a Winter Council clerk; I don't keep files on people's nights."''',
        c("[Sit with her.]", "sit")),
    nar("sit", '''{n}You sit on the edge of the crate beside her. After a while her head goes back against the post of the awning, and her breathing slows, and the tea tips in her loose hands. You take the cup before it spills.{/n}
{n}She sleeps for most of an hour, upright, in the cold, with the Wound flickering behind the rooftops. Whatever she dreams, she doesn't cry out. When she wakes she looks at you, and at the cup in your hand, and doesn't say anything at all.{/n}''',
        c("[Give her back the cup.]")),
], delay=48)


# --- 17. In public: a cultist's knife in the market, and a drow's arrow in front of everyone. ---------------------

IN_PUBLIC = K + "in_public"
CLAIMED_SCOUT = K + "claimed_as_scout"
CALLED_A_TRICK = K + "called_it_a_trick"
LET_THEM_LOOK = K + "let_them_look"

meet(IN_PUBLIC, "In front of everyone", '"Everyone\'s staring at the awning."', [
    nar("open", '''{n}You hear it before you see it: a scream at the grain dole, the crowd breaking like a dropped plate. A man in a baker's apron is standing over a sergeant on the cobbles with a knife in his fist and Deskari's locust daubed in blood on his own forehead, and he is turning toward the children at the trough.{/n}
{n}He gets one step. An arrow takes him through the throat from under the tailor's awning, and he sits down in the grain.{/n}''',
        c("Continue", "crowd")),
    nar("crowd", '''{n}Everyone turns to look where it came from. Kaylessa is standing at the edge of the shade with the bow still up, and in drawing it the shawl has slipped from her face. Slate skin. White hair. Red eyes narrowed against the noon.{/n}
{n}Somebody says "drow". Then several people say it. A man picks up a cobble. The sergeant on the ground is still bleeding, and nobody is looking at him any more.{/n}''',
        c('[Step into the open beside her] "She\'s one of my scouts. Anyone who touches her answers to me."', "scout",
          flags=(CLAIMED_SCOUT,)),
        c('[Laugh loudly] "A drow? In Drezen? It\'s the glare off the helmets. Look to the sergeant, all of you."', "trick",
          flags=(CALLED_A_TRICK,)),
        c("[Say nothing. Go and kneel by the sergeant, and let them look at her.]", "look", flags=(LET_THEM_LOOK,))),
    nar("scout", '''{n}The cobble goes down. The crowd doesn't love it, but the crowd has seen a demon-worshipper with a knife and an arrow that stopped him, and the Commander's voice is louder than theirs. Somebody runs for a healer. Somebody else, very quietly, says thank you in her direction.{/n}''',
        c("Continue", "scout_her")),
    kay("scout_her", '''{n}Later, when the market has emptied, she's back on the crate with the shawl up and her hands not quite steady.{/n}
"Your scout. In front of half the city." {n}She shakes her head.{/n} "Now every Kyonin clerk in Mendev will have it by the end of the month that the Knight Commander keeps a drow on the payroll. You've made yourself a file, soldier. I hope you like it."
{n}She pauses.{/n} "Nobody's said 'mine' about me in the street before. Not like that. Not to protect me."''',
        c("[Sit with her.]")),
    nar("trick", '''{n}You laugh as if it were the best joke of the week. A few people laugh with you, uncertainly. By the time they look back, the shade under the awning is empty and there is only an arrow in a dead man's throat, and the sergeant is calling for water, and everyone decides they must have been dazzled.{/n}''',
        c("Continue", "trick_her")),
    kay("trick_her", '''{n}She comes back at dusk, wrapped to the eyes, and sits down without a word, and after a while she laughs into her hands.{/n}
"'The glare off the helmets.' And they believed it. Half of them had me in their eye for a count of five." {n}She wipes her eyes with the back of a glove.{/n}
"That's the thing about people, soldier. They'll believe anything that lets them go home. Kyonin runs on it." {n}A sideways look.{/n} "So do you."''',
        c("[Sit with her.]")),
    nar("look", '''{n}You kneel on the cobbles and press your hands on the sergeant's wound, and say nothing at all. The crowd watches you do it. Then, one by one, they look back at the woman under the awning with the bow, who has not moved and has not covered her face, and who is staring back at every one of them.{/n}
{n}The man with the cobble puts it down. Nobody tells him to. The children at the trough are the first to go and look at her close.{/n}''',
        c("Continue", "look_her")),
    kay("look_her", '''"You let them look." {n}She says it at dusk, sitting on the crate with the shawl in her lap for once.{/n}
"You didn't claim me and you didn't hide me. You knelt in the grain and let the whole market decide what I was, with a dead cultist and a live sergeant right there for evidence." {n}She turns the shawl over in her hands.{/n}
"The smallest one asked if my eyes hurt. I said yes. She gave me her hat." {n}There is, in fact, a child's straw hat on the crate beside her.{/n} "I don't know what to do with this, soldier."''',
        c("[Sit with her.]")),
], delay=48)
