"""Elyanka Camilary, the courtship beats around the claim (Trickster; 11-ROSTER-PLAN-2 §2 R5, pacing Ch5 5-6 beats). Every
scene here is a rest-delivered visit to the dead-house by the south gate (or, in Chapter 6, to the Commander's tent) and
belongs to her relationship; the device, the commit, the hearse and the pages live in elyanka_trickster.

Canon anchors: the Way's hatred of "hatemongers who abhor the very thought of necromancy" and her crusader's oath under
Mendevian law (KTC_ElyankaComing/Cue_0008, Cue_0015, Cue_0021); "Our services to honor her are more luxurious than the most
lavish feasts" and "we, the matriarch priestesses of her church, remain steadfast... we are able to hide from the zealous eye
of our enemies" (Elyanka_MainDialogue/Cue_0055, Cue_0056); "everything is doomed to die, so there is no point in
restraining yourself while you are alive... the queen of pleasure, hedonism, and satiety" (Cue_0086 8352be38); the priests
in the Camilary woods and the half-raw venison (KTC_ElyankaComing/Cue_0016); "Undeath is the truest and best form of
existence... mortals... dumb cattle" (Cue_0062). Path fit: all T (v1).
"""
from story_format import c, n, p, reaction, scene
from storylines.elyanka_trickster import (E, REL, CLOSED, COMMITTED, OWNED, TESTED, BIER, EXPOSED, BLUFFED, STRAIGHT,
                                          GAVE_DEAD, SECRET_RITES, TABLE_SAT, TABLE_DOOR, TABLE_LEFT, WRIT_UPHELD,
                                          WRIT_LIED, WRIT_HERS, AT_RIFT, IN_DREZEN, REGILL_HUB, LOCK, DREZEN, el, nar, tag)

SCENES = []

ANATOMY_KNIFE = E + "anatomy.knife"
ANATOMY_WATCHED = E + "anatomy.watched"
ANATOMY_LEFT = E + "anatomy.left"
HUNT_ATE = E + "hunt.ate"
HUNT_SANG = E + "hunt.sang"
HUNT_WATCHED = E + "hunt.watched"
HUNT_HELD = E + "hunt.held"            # villain-route-elyanka (cloud): the checked interception held the hart for her knife
HUNT_GORED = E + "hunt.gored"          # ... and the failed one: the tine through the Commander's thigh
COURIER_HUNGRY = E + "courier.come_back_hungry"
COURIER_RIPENING = E + "courier.ripening"
COURIER_SILENT = E + "courier.silent"


def visit(id, title, nodes, requires, forbids=(), delay=24, last=5, chapter=5, chapters=(5,), optional=True, kind="visit",
          portable=False, areas=None, any_groups=()):
    """portable=False: a Drezen encounter, delivered at a rest in the capital. The courier and the Threshold visit travel."""
    SCENES.append(scene(id, title, "Elyanka", chapter, "", nodes, requires=("trickster.ever", *requires),
                        forbids=(CLOSED, *forbids), delay=delay, last=last, optional=optional, Relationship=REL,
                        Remote=True, Kind=kind, Chapters=list(chapters),
                        **(dict(RequiresAnyGroups=[list(g) for g in any_groups]) if any_groups else {}),
                        **(dict(Areas=areas) if areas else ({} if portable else dict(Areas=[DREZEN])))))
    tag(id, "T")


# --- 1. The anatomy lesson (T, optional): what the Abyss does to meat. ----------------------------------------------------

visit(E + "beat.anatomy", "What the Abyss does to meat", [
    nar("start", '''{n}The trestle in the dead-house has been cleared of wine and laid with a sheet, and there is something long under the sheet. Beside it a roll of oiled leather lies open, and in the leather, in loops, as neat as a jeweller's tray, are knives: hooked, straight, some no longer than a finger. Elyanka has rolled her grey sleeves to the elbow.{/n}
{n}The room smells of lime, cold stone, cloves, and underneath all three, something sweet that should not be.{/n}''',
        c("Continue", "who")),
    el("who", '''"A cultist of the Locust Lord. Your gaolers took him on the walls, and he died in their cellar before he said anything useful." {n}She draws the sheet down to the waist.{/n} "They sold him to me for four silver and my promise not to stand him up again. I keep promises that cost me nothing."
"Come here, Commander. You have killed a great many of these. I doubt you have ever looked inside one."''',
       c("[Come to the table.]", "open"),
       c('"I\'ve seen men opened before. On the field."', "field")),
    el("field", '''"On the field you see men opened by accident, in a hurry, in the dark, by people who wanted them closed." {n}She selects a knife with a curved blade.{/n} "This is different. This is reading. Come here."''',
       c("[Come to the table.]", "open")),
    el("open", '''{n}She cuts from the breastbone down, one clean stroke, with no more effort than a woman slicing bread, and folds the skin back like the cover of a book.{/n}
"Look." {n}The flesh beneath is wrong: grey, riddled, the fat gone to a kind of wet lace. In the lace, in their hundreds, lie pale seeds the size of rice grains. Some of them are moving.{/n}
"Your Deskari does not kill. He spends. He fills his servants with his children and lets them eat their way out, and calls it glory." {n}Her lip curls.{/n} "The Abyss is a glutton with no table manners."''',
       c('"And your Lady?"', "lady")),
    el("lady", '''"My Lady keeps." {n}She lifts a fold of the grey flesh on the flat of the knife and lets it fall.{/n}
"Everything is doomed to die, Commander. Everyone knows it; only my Lady's children act on it. There is no point in holding back while you live, and when you die there is no point in rotting. Undeath is the truest form there is. The body kept, the hunger kept, forever. Not this." {n}She flicks a seed off her blade into the brazier, where it pops.{/n} "This is what happens to meat that belongs to nobody."''',
       c('[Hold out your hand for the knife] "Show me."', "knife"),
       c("[Watch her work.]", "watch"),
       c('"I\'ve seen enough of him. Burn it."', "leave")),
    el("knife", '''{n}She puts the knife in your hand and closes her own hand over yours, from behind, her cold fingers laid along your warm ones, her chin at your shoulder.{/n}
"Here. The liver. Your priests say the soul lives in the heart. The soul lives nowhere. The appetite lives here." {n}She guides the blade.{/n} "Steady. You have killed a hundred of these, and a dead one makes your hand shake."
{n}Her body is against your back from shoulder to hip, cool through the grey wool, and her thumb rests on the inside of your wrist, over the pulse, as if that were where the lesson was.{/n}''',
       c("[Lean back into her, and let her guide the cut.]", "knife2"),
       c("[Keep your eyes on the dead man, and cut.]", "knife2"),
       c("[Take your hand out from under hers.]", "knife_off")),
    el("knife_off", '''{n}She lets your hand go at once, and steps back, and the cold goes with her.{/n}
"As you like. You cut, then. I will watch." {n}She folds her arms.{/n} "A surgeon's hand, after all. Careful of other people's fingers. It will not save you, but it is very correct."''',
       c("Continue", "knife2")),
    el("knife2", '''{n}She lets you cut alone for a while, and watches, and says nothing, which from her is praise.{/n}
"You hold a knife like a butcher, not like a surgeon. Good. Surgeons are liars. They pretend they are saving something." {n}She takes the knife back and wipes it on the dead man's sheet.{/n}
"When the time comes I shall do this to you myself. Very carefully. I will know my way already." {n}She wipes the blade and lays it back in its loop in the leather.{/n}''',
       c("[Wash your hands in her wine.]", flags=(ANATOMY_KNIFE,))),
    el("watch", '''{n}You watch. She works quickly, lifting out what the Locust Lord's children have left, naming it, and dropping it into the brazier: the liver, pitted like a sponge; the lungs, half eaten; the heart, still whole, still red, the only honest thing left in him.{/n}
"There. That was his. The rest belonged to his god, and his god did not even come to collect." {n}She lays the heart on a pewter plate, as if serving it.{/n}
"You are very quiet, Commander. I cannot tell whether you are disgusted or taking notes."''',
       c('"Taking notes."', "watch_notes"),
       c('"Both."', "watch_both")),
    el("watch_both", '''"Good. Both is the right answer. The disgust keeps you alive; the notes make it worth the trouble." {n}She wipes her hands, finger by finger, on a cloth that was white.{/n}
"Remember what you saw. When you are tempted to let the Abyss have you whole, remember the lace. The Way will not waste you like that. I will not." {n}She almost smiles.{/n} "Now go and wash. You look like a {mf|man|woman} who has been reading."''',
       c("[Leave her to her burning.]", flags=(ANATOMY_WATCHED,))),
    el("watch_notes", '''"Notes." {n}She looks at you with frank approval, the way she looked at the venison.{/n} "Good. Disgust is for people who can afford to be surprised. You cannot."
{n}She wipes her hands, finger by finger, on a cloth that was white.{/n}
"Remember what you saw. When you are tempted to let the Abyss have you whole, remember the lace. The Way will not waste you like that. I will not." {n}She almost smiles.{/n} "Now go and wash. You look like a {mf|man|woman} who has been reading."''',
       c("[Leave her to her burning.]", flags=(ANATOMY_WATCHED,))),
    el("leave", '''{n}She looks at you across the opened body with mild contempt, as if you had refused a second helping.{/n}
"Burn it. As you like. That is what your crusade does with everything it does not understand." {n}She draws the sheet back up to the dead man's chin, quite gently.{/n}
"I am not offended, Commander. I am disappointed, which is worse, and lasts longer. Go on. I will burn him myself. It will take me all night, and I will think of you the whole time, unkindly."''',
       c("[Go.]", flags=(ANATOMY_LEFT,))),
], requires=(BIER,), forbids=(ANATOMY_KNIFE, ANATOMY_WATCHED, ANATOMY_LEFT), delay=24, last=5)


# --- 2. The chaplains' writ (T, optional): the hatemongers, and her oath. ------------------------------------------------

visit(E + "beat.writ", "A writ from the chaplains", [
    nar("start", '''{n}They come to your quarters in the morning, three of them: two chaplains of the Inheritor in white surcoats, one young and one grey, and a clerk of the crusade's court with a leather case and a very red face. The grey chaplain does the talking. He has a writ.{/n}''',
        c("Continue", "writ")),
    n("writ", "Chaplain", '''"Commander. There is a woman lodged in the dead-house by the south gate who is a priestess of Urgathoa. Of the Pallid Princess, the plague-mother, the mistress of the walking dead. We have witnesses. She keeps a hearse. She has been seen in the yard at night with men in grey who do not breathe as men should."
{n}He holds out the writ.{/n} "The worship of Urgathoa is forbidden in every kingdom of Avistan. We ask your seal on her expulsion. Today. Before whatever she came here for is done."''',
      c('"Let\'s hear what she says. Come with me."', "yard")),
    nar("yard", '''{n}She receives the four of you in the yard, standing by the hearse with her hands folded in her sleeves, as if she had been expecting you since before you set out, and perhaps she had. Her escort stand in a row behind her, grey, silent, and very still. The young chaplain's hand goes to his holy symbol and stays there.{/n}''',
        c("Continue", "oath")),
    el("oath", '''"Chaplains." {n}She inclines her head exactly as far as courtesy requires and not a hair further.{/n}
"According to Mendevian law, I have the right to be here. I and all my escort have taken the crusader's oath and are members of the Fifth Crusade against the Worldwound. We swore it at Nerosyan, before your own bishops, in front of witnesses, with our hands on your goddess's sword. Your clerk may read the register; I see he has brought it." {n}The clerk goes redder.{/n}
"You may hate me. Hatred is free. Expulsion is not. It needs a reason the law will accept, and you have none."''',
       c("Continue", "chaplain")),
    n("chaplain", "Chaplain", '''"The law was not written for her kind!" {n}The grey chaplain turns to you.{/n} "Commander, she mocks the oath by swearing it. Every soldier in this city knows what walks behind her carriage. If the crusade shelters a necromancer's priestess, what is it fighting for?"
{n}Elyanka does not look at him. She looks at you, and waits, with the bird-bright attention of a woman who has already decided what she will think of you for each possible answer.{/n}''',
      c('[Uphold her oath] "She swore it. The law says she stays, and so does my seal. Go home."', "upheld"),
      c('[Lie] "She\'s my embalmer. I hired her for the dead of Iz. That\'s all she is."', "lied"),
      c('[Let her answer] "You heard her, chaplain. Take it up with her."', "hers")),
    nar("upheld", '''{n}The grey chaplain stares at you as if you had struck him. The clerk closes his register with great care. The young one says, "Commander, surely..." and stops, because the older man has put a hand on his arm.{/n}
{n}They go. They do not bow. At the gate of the yard the grey one turns and says, to the air, that the Inheritor sees what is done in her name, and then they are gone, and the hearse-yard is very quiet.{/n}''',
        c("Continue", "upheld2")),
    el("upheld2", '''{n}Elyanka lets out a breath, slowly, through her teeth, as if she had been holding it since the asylum.{/n}
"You stood in front of your own priests for a priestess of my Lady. On the law. In daylight." {n}Her eyes are very bright.{/n} "Do you understand what you have done? In Caliphas they will not believe it. In Nerosyan they will never forgive it. Those chaplains will pray for your soul every night until they die, and they will mean every word."
"Those three came to drive me out. You made them hear my oath instead, with their own soldiers watching. I find it quite unbearable. Go away before I say something foolish."''',
       c("[Go away.]", flags=(WRIT_UPHELD,))),
    nar("lied", '''{n}The grey chaplain looks at you, and at her, and at the six men in grey behind her who do not breathe as men should. He does not believe you. He is too old to believe anybody. But you are the Commander, and it is your seal, and after a while he rolls up his writ and goes, with his young colleague glaring back at the hearse all the way to the gate.{/n}''',
        c("Continue", "lied2")),
    el("lied2", '''{n}She waits until the gate has closed behind them. Then she turns on you, and her voice is very soft, which is worse than shouting.{/n}
"Your embalmer." {n}She tastes it.{/n} "I am a matriarch priestess of the Pallid Princess and a noblewoman of the Immortal Principality, and you have made me your servant in front of a clerk." {n}She steps close.{/n}
"It worked. I will grant you that. It was a small, cheap, clever lie, and it worked. Never tell it again. The next time you need me to be less than I am, Commander, let them burn me instead."''',
       c("[Take the rebuke.]", flags=(WRIT_LIED,))),
    el("hers", '''"Thank you, Commander." {n}She turns to the grey chaplain, and smiles, and her smile shows strong white teeth.{/n}
"Old man. You have been burying the dead of this crusade for thirty years, I think. You have put them in the ground with lime, and prayed over them, and handed their souls to the grey warden, and not one of them has ever come back to thank you." {n}She steps closer. He does not step back; he is braver than he looks.{/n}
"When you die, and you will die soon, you have the cough, I can hear it, my Lady will offer you a seat at her table. Think about it on the nights you cannot breathe. That is not a threat. It is an invitation. I have sworn an oath not to threaten crusaders."''',
       c("Continue", "hers2")),
    nar("hers2", '''{n}The young chaplain pulls the old one away by the sleeve. The clerk is already at the gate. Behind Elyanka, one of her grey escort turns his head, slowly, to watch them go, and you see the young chaplain see it, and go white.{/n}
{n}When they have gone she turns back to you, entirely composed.{/n} "You let me speak for myself. Nobody does that for a priestess of my Lady. They either burn her or hide her." {n}A dry, pleased breath.{/n} "You will regret it one day. I shall enjoy watching you not regret it yet."''',
        c("[Leave her in her yard.]", flags=(WRIT_HERS,))),
], requires=(BIER,), forbids=(WRIT_UPHELD, WRIT_LIED, WRIT_HERS), delay=36, last=5)


# --- 3. Venison (T, optional, after the hearse): hungry and fed at once. -------------------------------------------------

visit(E + "beat.hunt", "Venison", [
    nar("start", '''{n}The sprig of white flower under your door has a second thing wound round its stem this time: a strip of black cloth, the kind hunters tie on a tree to mark a path. You follow the marks north out of the postern after dark, into the scrub woods above Drezen, where the trees grow crooked from the Wound's weather and nobody has cut firewood in a generation.{/n}
{n}She is waiting in a clearing, in her grey robe, with a knife in her hand and nothing else. Two of her escort stand at the edge of the trees like posts.{/n}''',
        c("Continue", "stag")),
    el("stag", '''"There is a stag in these woods. A real one, not one of your Wound's things with too many eyes. My people have been driving him toward this clearing since sundown." {n}She tests the knife's edge with her thumb.{/n}
"Nobody in Drezen gave me leave to kill him. Nobody in Drezen owns him. That is how venison tastes best." {n}She tilts her head, listening.{/n} "Here he comes. Be still, or be quick. Not both."''',
       c("[Be still.]", "kill"),
       c("[Be quick. Get between the stag and the trees.]", "kill_quick"),
       # villain-route-elyanka (cloud; claude-work-queue elyanka-and-camilary:D08): the interception is a real Athletics
       # check with a distinct success and failure. Trailing answer: indices 0 and 1 keep their saved identity.
       c("[Athletics] Take him yourself: get between the stag and the trees, and get your hands on the antlers.",
         check=dict(Skill="SkillAthletics", DC=24, Success="held", Failure="gored", CommanderOnly=True))),
    nar("kill", '''{n}He comes out of the dark at a run, a big grey hart with a heavy neck, and her escort close in behind him without a sound, and he turns, and turns again, and there is nowhere left. She walks up to him while he is still deciding. She does not hurry.{/n}
{n}The knife goes in under the jaw. She holds his head against her body with one arm until he stops, and then a while longer.{/n}''',
        c("Continue", "fire")),
    nar("kill_quick", '''{n}He comes out of the dark at a run, a big grey hart, and you are where he wants to go. For one moment there is nothing in the world but his antlers and your arms, and then he swerves, and stumbles, and she is there, and the knife goes in under his jaw.{/n}
{n}She holds his head against her body while he dies. Then she looks at you, flushed and breathless and bruised across the forearm, and laughs out loud.{/n} "Useful after all."''',
        c("Continue", "fire")),
    nar("held", '''{n}He comes out of the dark at a run, a big grey hart with a heavy neck, and you are where he wants to go. You take one tine in your left hand and one in your right and go down on a knee in the leaf-mould, and he drags you a body's length across the clearing and cannot drag you any further. For a moment the whole forest is his breath in your face.{/n}
{n}Then she is there. She does not hurry. She puts the knife in under his jaw while you hold his head up for her like a dish, and she watches your face, not his, the whole time he is dying.{/n}
"Hold," {n}she says, when your arms begin to shake.{/n} "Hold. Let him finish. It is rude to drop the meat while it is still saying grace."''',
        c("Continue", "fire", flags=(HUNT_HELD,))),
    nar("gored", '''{n}He comes out of the dark at a run, and you are where he wants to go, and you are a heartbeat late. Your hand closes on a tine and slides off it. The next one goes into your thigh above the knee, lifts you, and throws you into the bracken like a sack of grain.{/n}
{n}You hear the rest rather than see it: the men in grey closing without a sound, the hart turning and turning again, a wet grunt, then nothing. When you can sit up she is kneeling over you with the knife still red, and she has put her thumb into the hole in your leg, quite deliberately, the way a cook tests a roast.{/n}
"Wasteful," {n}she says, and licks the thumb clean.{/n} "Look at it, running into the leaves for nothing. You are my collateral, Commander. You do not get to spill it on a stag." {n}She binds the leg with a strip torn from her own grey hem, hard enough to make you shout, and does not apologize.{/n}''',
        c("Continue", "fire", flags=(HUNT_GORED,))),
    el("fire", '''{n}Her escort build a fire. She opens the stag herself, sleeves rolled, quick and neat, and cuts the heart out and lays it on a flat stone at the edge of the flames, just long enough to sear.{/n}
"When I was sixteen I ate like this every night. Half raw, with the blood running. There was singing, and nobody asked whose deer it was, and I have never been so happy before or since." {n}She cuts the heart in two, and holds out one half to you on the blade of the knife, red to the middle and steaming.{/n}
"Eat. Or do not. My Lady keeps a very long memory of who refused her table."''',
       c("[Eat from her knife.]", "ate"),
       c('[Sing] "What did they sing, the priests in the woods?"', "sang"),
       c("[Keep watch on the trees. This is the Worldwound's edge.]", "watched")),
    el("ate", '''{n}It is hot outside and cold in the middle, and tastes of iron and smoke and something wild. The blood runs down your chin. She watches you eat it with the same frank hunger she watched you with in the hearse, and when you have finished she wipes your chin with her thumb and licks the thumb.{/n}
"There," {n}she says.{/n} "Hungry and fed at once. Now you know what my Lady promises." {n}She eats her own half slowly, with her eyes shut.{/n} "She has been fed well tonight. So have I. I shall tell her so, in the morning, at length."''',
       c("[Sit with her by the fire until it burns down.]", flags=(HUNT_ATE,))),
    el("sang", '''{n}She looks at you across the fire for a while, surprised.{/n}
"You want the words?" {n}She sets the knife down.{/n} "Songs to her. Old songs, in the tongue they speak in the woods north of Caliphas, where the Camilary deer run. About eating, and drinking, and lying down, and never having to get up again."
{n}Then, quietly, she sings one. It is low and slow, and every line rises at the end like a question, and she cannot reach the high notes any more; her voice cracks on them and she sings straight through the cracks without stopping, as if the song mattered and the voice did not. When it is finished she scowls at the fire, angry with herself, and eats her half of the heart without looking at you. Her escort at the edge of the trees stand like posts and pretend to be deaf.{/n}''',
       c("[Say nothing. Eat your half.]", flags=(HUNT_SANG,))),
    el("watched", '''{n}You get up and walk to the edge of the firelight and stand there with your back to her and your sword loose, watching the crooked trees. Somewhere out in the dark, toward the Wound, something that is not a stag is moving.{/n}
"You cannot help yourself." {n}Her voice behind you is amused, and something else.{/n} "I bring you to my Lady's table in the woods, and you stand guard over it like a hound." {n}She is quiet a moment.{/n} "Well. Guard it, then. I will keep your half warm."''',
       c("[Keep watch until the fire is ash.]", flags=(HUNT_WATCHED,))),
], requires=(BIER,), forbids=(HUNT_ATE, HUNT_SANG, HUNT_WATCHED), delay=36, last=5)


# --- 4. A man in grey (T, optional, Kind letter): she will not trust this to paper, so a courier recites her. ----------------------

visit(E + "beat.courier", "A man in grey", [
    nar("start", '''{n}One of her escort is standing in your doorway when you wake: a man in grey with a face like a closed shutter. He does not bow. He clears his throat, and when he speaks it is in her voice, exactly, the cadence and the chill and the faint Ustalavic roll of the r, coming out of a mouth that is not hers.{/n}
"The priestess sends word. She does not trust it to paper. I will say it once."''',
        c("[Listen.]", "message")),
    n("message", "Man in grey", '''"*Commander. I have gone south to the border, to a house on the Ustalav road where the Way keeps rooms. A master of the Way has come up from Caliphas to ask me why my carriage is empty.*"
"*I told him the goods are the finest offering my Lady will be served this century, and that I will not have them hurried to her table half-ripe. He asked me whether that was faith or appetite. I told him that with my Lady there is no difference.*"''',
      c("Continue", "message2")),
    n("message2", "Man in grey", '''"*I will be back in four days. Do not die while I am gone. I would not be there to collect, and the master would, and he is not gentle with other people's property.*"
"*Send your answer with this man. He will forget it the moment he has said it to me. He forgets everything. It is why I keep him.*"
{n}The man in grey stops. His face does not change. He waits.{/n}''',
      c('[Send back] "Tell her: come back hungry."', "hungry"),
      c('[Send back] "Tell her the goods are ripening nicely."', "ripening"),
      c("[Send nothing back.]", "silent")),
    nar("hungry", '''{n}He says it back to you once, in your own voice, which is a peculiar thing to hear, and then he turns and goes, and you hear his boots on the stair and nothing after.{/n}
{n}Four days later, to the hour, there is a sprig of white flower under your door. Wound round its stem is a single silver-grey hair.{/n}''',
        c("Continue", flags=(COURIER_HUNGRY,))),
    nar("ripening", '''{n}He says it back to you once, in your own voice, dry as dust, and goes.{/n}
{n}Four days later, to the hour, he is back in your doorway. He clears his throat and says, in her voice, "*Ripening. You insolent sack of meat. The master laughed. Nobody in the Way has heard him laugh in forty years. He gave me leave to stay. I hate you for making him laugh. I am coming back tonight.*" Then he goes, and forgets.{/n}''',
        c("Continue", flags=(COURIER_RIPENING,))),
    nar("silent", '''{n}He waits for a while longer, as if you might change your mind, and then he goes, and you hear his boots on the stair.{/n}
{n}Four days later she is back in the dead-house. She does not mention the courier or the master or your silence. But she looks at you, the first time you meet, for rather longer than she needs to, with her head a little on one side, as if she were listening for something in you that she could name.{/n}''',
        c("Continue", flags=(COURIER_SILENT,))),
], requires=(BIER,), forbids=(COURIER_HUNGRY, COURIER_RIPENING, COURIER_SILENT), delay=72, last=5, kind="letter", portable=True)


# --- 5. Her Lady's table (T, optional): the secret, kept. -----------------------------------------------------------------

TABLE_CHOICES = (
    c("[Sit at her right hand.]", "sit"),
    c("[Keep the door.]", "door"),
    c('"I wasn\'t here." [Leave before the wine.]', "left"),
)

visit(E + "beat.table", "Her Lady's table", [
    nar("start", '''{n}Preparations for her Lady's feast have filled the dead-house with grey cloth, and the long room is full of candles and the smell of roasting fat. There are perhaps thirty people at the long table, masked in plain grey half-masks, in their ordinary clothes: a baker's apron, a sergeant's coat, the good wool of a merchant's wife. People of Drezen. People of your crusade.{/n}
{n}At the head of the table, unmasked, in her grey robe, sits Elyanka. There is an empty chair at her right hand.{/n}''',
        c("Continue", "welcome")),
    el("welcome", '''"Commander." {n}Thirty masked faces turn toward you at once.{/n} "Do not look so surprised. Our church has more followers than it seems. It always has. They simply hide from the zealous eye of their enemies, and eat well when nobody is looking."
"Our services to honour her are more luxurious than the most lavish feasts, the wildest orgies. This is a small one, a crusade one: the food is poor, and everyone goes home before the morning watch." {n}She gestures at the empty chair.{/n} "My Lady keeps a place for the one who holds my claim."''',
       c("Continue", "targona", requires=("targona.trickster.in_drezen", "targona.present_now")),
       c("Continue", "choose", forbids=("targona.trickster.in_drezen",)),
       c("Continue", "choose", requires=("targona.trickster.in_drezen",), forbids=("targona.present_now",))),
    el("targona", '''"Before you choose." {n}Her voice drops, for you only.{/n} "Your angel came to the gate of the yard yesterday. The one whose wing was made in the witch's laboratory. She stood there a long time, smelling us, the way a hound smells a fox's earth, and then she went away without a word." {n}Her mouth tightens.{/n}
"Everything that shines hates my Lady. It is the one thing I envy them: they are so certain."''',
       c("Continue", "choose")),
    el("nidalynn", '''"The Sarkorian woman who waits by the tavern door. She passed my hearse in the street and looked at my horses as if she could breathe frost on them." {n}A dry breath through the nose.{/n} "She is no more a Sarkorian goodwife than I am. I do not know what she is. I know she would like to see this house burn." {n}She turns back to her guests.{/n} "It will not burn tonight. Choose."''',
       *TABLE_CHOICES),
    el("choose", '''"Sit, and eat what my Lady's people have brought, and nobody here will ever forget it. Or stand at the door and keep it, as a crusader would. Or go home and pretend you were never here." {n}She pours wine into the cup at the empty place, dark and thick.{/n}
"Each of those is an answer. I will remember which."''',
       *TABLE_CHOICES,
       c('[Ask] "Who else has been watching your door?"', "nidalynn", requires=("nidalynn.started", "crossroute.nidalynn.available"))),
    nar("sit", '''{n}You sit. Thirty grey masks watch you do it, and then the talk starts again, low, and the dishes go round: fat meat, black pudding, honeyed things, bread soaked in red wine. You do not ask what anything is. Elyanka tells you anyway, in your ear, dish by dish, and not all of it is venison.{/n}
{n}At midnight they sing, softly, because there are sentries on the walls. The baker in the apron weeps openly. The sergeant holds his cup up to the rafters. Elyanka does not sing. She watches you listen, and her cold hand lies on the back of your neck under your hair, and stays there.{/n}''',
        c("Continue", "sit2")),
    el("sit2", '''"There," {n}she says, when the room has emptied and the candles are guttering.{/n} "Now there are thirty people in your city who have seen the Knight Commander of the Fifth Crusade at the Pallid Princess's table. Thirty who will die for you rather than say so. And thirty who would say so, one day, for the right price."
"That is what it is to be loved by my Lady's people, Commander. Get used to it."''',
       c("[Finish your wine.]", flags=(TABLE_SAT,))),
    nar("door", '''{n}You take your place at the door of the dead-house, with your back to the table and your sword at your hip, and you keep it. The feast goes on behind you: meat and wine and low singing, and once someone weeping with happiness. Twice in the night footsteps come down the lane from the gate, and twice they stop when they see who is standing in the doorway, and go away again.{/n}
{n}Near the end she comes and stands behind you, close enough that you feel the cold of her through your coat.{/n}''',
        c("Continue", "door2")),
    el("door2", '''"You would not sit at my Lady's table, and you would not leave it unguarded either." {n}Her breath is at your ear.{/n} "You are the strangest crusader I have ever owned."
"A hound on the doorstep of the Pallid Princess's feast. My Lady will laugh when she hears of it. She laughs so rarely." {n}Her fingers close, briefly, on the back of your neck. Then the hand goes down your spine under your coat, nails dragging, and flattens low on your back to pull you hard against her, the cold of her seeping through your shirt and your belt and your skin. Behind you the masked guests laugh and clink their cups, and she lets them, and her other hand slides around your hip and finds you through your breeches without the least apology.{/n}
"Warm," {n}she says, with open disgust, and squeezes until you have to bite down on a noise.{/n} "Sweating, shaking, ridiculous. And you stand at my Lady's door like a dog with a bone and let me do this in front of her guests. I shall keep you. I shall have every inch of you on that table, with the wine, with the bones, with my Lady watching, and I will cackle the whole while." {n}She puts her teeth to your ear and bites.{/n} "Later. Hound. Hold the door."
{n}She takes her hand away and licks her fingers, slowly, looking at you.{/n} "Come inside when they have gone. There is food left, and I am still hungry."''',
       c("[Keep the door until the last of them has gone.]", flags=(TABLE_DOOR,))),
    el("left", '''{n}Her face does not change. The masked faces watch you go to the door, and not one of them says a word.{/n}
"You were never here," {n}she agrees, to your back.{/n} "None of us were. That is the first rule of my Lady's table, and you have learned it in a single night." {n}A pause.{/n} "The second rule is that the one who leaves early is always the one we talk about. Good night, Commander."''',
       c("[Go.]", flags=(TABLE_LEFT,))),
], requires=(BIER, SECRET_RITES), forbids=(TABLE_SAT, TABLE_DOOR, TABLE_LEFT), delay=48, last=5)


# --- 6. Chapter 6 (T, optional): the collateral, inspected before the Threshold. ------------------------------------------

visit(E + "ch6.collateral", "The collateral, inspected", [
    nar("start", '''{n}The army has made camp outside Threshold, on black glass under a sky the colour of a bruise. Behind the baggage train stands the glass-sided hearse that followed it from Drezen. Nobody gave it leave. Nobody stopped it.{/n}
{n}Tonight she walks into your tent without asking, in her grey robe, and sits down on the end of your camp bed as if it were hers.{/n}''',
        c("Continue", "inspect", requires=(BIER,)),
        c("Continue", "inspect_debt", forbids=(BIER,))),
    el("inspect", '''"Stand up. Take off your shirt." {n}She unwinds the cord.{/n} "I measured you in Drezen. I want to see what the march has done to the goods."
{n}She measures you again, knot by knot: the shoulders, the span of the hands, the chest breathing in and breathing out. Her fingers are cold, and slower than they need to be.{/n} "Thinner. Two knots at the waist. A new cut on the forearm, badly stitched. Your quartermaster should be flogged." {n}She lets the cord fall.{/n}''',
       c("Continue", "tomorrow")),
    el("inspect_debt", '''"Stand where the lamp is. I want to see what the march has done to the goods. I never did take your measure in Drezen; I shall have to do it by eye." {n}She looks you over from the camp bed, head on one side.{/n}
"Thinner. A new cut on the forearm, badly stitched. You carry your left shoulder higher than you did in Drezen." {n}She wrinkles her nose.{/n} "And you smell of the Wound. Everything here does. It gets into the meat."''',
       c("Continue", "tomorrow")),
    el("tomorrow", '''"Tomorrow, or the next day, you go into the Wound. If you die at the edge of it, I collect. That is what you pledged to the Way, and that is what I came north to collect." {n}She sounds perfectly calm.{/n}
"If the Wound takes you whole, I have nothing. No body. No table. No offering. Half my life of patience, and a hearse built in Caliphas, for nothing." {n}Her mouth thins.{/n} "So I will ask you one thing, as your creditor. Where do you want me standing?"''',
       c('"Are you afraid for me?"', "afraid"),
       c('[Tell her to stand at the rift\'s edge] "Somewhere you can see. If it falls due, collect."', "rift"),
       c('[Tell her to wait in Drezen] "In the dead-house. If I don\'t come back, you won\'t need to see it."', "drezen")),
    el("afraid", '''"Afraid." {n}She turns the word over.{/n}
"I am afraid of losing what you pledged. That is not the same thing. A merchant is afraid for the ship, not for the sailors." {n}She looks at the tent wall, toward the north, where the sky is the colour of a bruise.{/n} "The witch in there made you. I have read what she did at Kenabres. She will want you back whole, and she does not share."
{n}Her hand, lying on her knee, has closed on a fold of her grey robe so hard that the knuckles have gone white.{/n} "Now answer my question, and do not ask me that again."''',
       c('[Tell her to stand at the rift\'s edge] "Somewhere you can see. If it falls due, collect."', "rift"),
       c('[Tell her to wait in Drezen] "In the dead-house. If I don\'t come back, you won\'t need to see it."', "drezen")),
    el("rift", '''"Where I can see." {n}She stands, and smooths her robe.{/n} "I will stand on the last ridge before the rift with my hearse and my six, and I will not lift a finger for you, Commander, not one. I will watch my collateral. If it falls, I will go down and fetch it before the demons do."
"And if it does not fall, I will have come all this way to watch a debtor live." {n}She stands.{/n} "It would not be the first time you disappointed me."''',
       c("Continue", "rift2", requires=(COMMITTED,)),
       c("[Let her go back to her hearse.]", flags=(AT_RIFT,), forbids=(COMMITTED,))),
    el("rift2", '''{n}At the tent flap she stops, and comes back, and kisses you, hard, on the mouth, with her cold hand flat over your heart as if she were counting it. She does not stop. The kiss drives you back against the tent pole, her teeth in your lip, and the cold hand leaves your heart and goes down, flat over your ribs, your belly, inside your belt, and closes. Her laugh cracks out of her, high and mad, loud enough that her six outside must hear.{/n}
"Mine to lose, mine to bury, and the Wound shall not have a scrap of it before I do." {n}She hauls your shirt up and bites the muscle over your heart, not gently, and leaves it bleeding a little.{/n} "Warm. Ugh. Warm and shaking and begging with your whole body. Do not think I cannot feel it. Lie down."
{n}She shoves you onto the blankets and is on you before you have landed, grey robe pulled aside, the cold length of her over you, her nails in your shoulders, her mouth at your throat. She spreads her knees across your hips, grinds down against you until the breath goes out of you, and reaches between your bodies to put you where she wants you.{/n}
"For my Lady," {n}she says, against your lips.{/n} "She likes an offering warm when it is pledged."''',
       c("[Let her go back to her hearse.]", flags=(AT_RIFT,))),
    el("drezen", '''{n}For a moment she does not answer, and you would swear she is offended.{/n}
"You would send your creditor home on the eve of the settlement." {n}Then the corner of her mouth goes up.{/n} "Very well. I will sit in the dead-house by the south gate with a candle, and wait for the news, like a widow. It will be a new experience. I do not expect to enjoy it."
"Do not make me drive this hearse all the way back to Drezen for nothing, Commander. One way or another, bring me something."''',
       c("[Let her go.]", flags=(IN_DREZEN,))),
], requires=(OWNED,), forbids=(AT_RIFT, IN_DREZEN), delay=0, last=6, chapter=6, chapters=(6,), portable=True, areas=["10c4b0e2af186ba46ab4d238d00a40a8"])


# --- 8. The Way's tongue (T, optional): a secret for a secret, in a whisper. ----------------------------------------------

WHISPER_FEAR = E + "whisper.fear"
WHISPER_WAKE = E + "whisper.wake"
WHISPER_LIE = E + "whisper.lie"

visit(E + "beat.whisper", "The Way's tongue", [
    nar("start", '''{n}She has pulled two stools close together at the end of the long room, knee to knee, with no table between them and no candle nearer than the door. When you sit she leans in until her mouth is a finger's width from your ear, and when she speaks you can barely hear her, though there is nobody else in the house.{/n}''',
        c("Continue", "lesson")),
    el("lesson", '''"The Way's teaching cannot be written. It can only be told, and felt." {n}Her breath stirs the hair at your temple.{/n} "So it is told like this. So close that nobody in the next room could swear you had spoken at all. So close that the one who hears it cannot pretend, afterwards, that it was not meant for them."
"You whispered me the terms of the bequest badly. You breathe like a soldier, all at once. Again. Say something to me. Anything. So that the door does not hear."''',
       c("[Whisper to her.]", "again")),
    el("again", '''"Worse." {n}She does not move away.{/n} "Slower. Let it out as if you were letting out blood, a little at a time, and you did not want anyone to see the bowl."
{n}You try again. This time she is quiet for a while afterwards.{/n}
"Better. Now the Way's custom: a secret for a secret. You tell me a true thing, and I tell you one, and neither of us may ever repeat what we heard, not even to each other. Go first. You are the debtor."''',
       c('[Whisper a true thing] "I am afraid of the Wound. Not of dying in it. Of what it wants me to be."', "fear"),
       c('[Whisper a true thing] "I enjoyed the wake. Every minute of it."', "wake", requires=(BLUFFED,)),
       c('[Whisper a true thing] "When you found my pulse under the veil, I was glad you had."', "wake_exposed", requires=(EXPOSED,)),
       c('[Whisper a true thing] "I came to supper bare-faced to watch your face when the corpse sat down."', "wake_straight", requires=(STRAIGHT,)),
       c("[Whisper something that isn't true.]", "lie")),
    el("fear", '''{n}She does not answer at once. Her cheek rests against yours, cold, and you feel her jaw move as if she were tasting what you said.{/n}
"Yes. That is true. I can hear it; it sits lower than the words." {n}A pause.{/n} "The witch in the Wound made you for something. My Lady at least tells her children what they are for. Hunger. Keeping. Never lying down." {n}Her fingers find your wrist, and the pulse in it.{/n} "Now mine."''',
       c("Continue", "hers", flags=(WHISPER_FEAR,))),
    el("wake", '''{n}Her breath catches against your ear, and then she laughs, without a sound, the laugh going through her shoulders and into yours.{/n}
"Yes. That is true. I watched you enjoy it through a curtain and thought you were grieving." {n}She is still smiling; you can feel it.{/n} "You are a monster, Commander. A small, warm, sweating monster. Now mine."''',
       c("Continue", "hers", flags=(WHISPER_WAKE,))),
    el("wake_exposed", '''{n}Her fingers, on your wrist, stop moving.{/n}
"Glad." {n}A long pause.{/n} "Yes. That is true. It sits low. You wanted to be caught, a little; you wanted someone to be good enough to catch you." {n}She does not sound pleased about it.{/n} "I still will not believe your face. Now mine."''',
       c("Continue", "hers", flags=(WHISPER_WAKE,))),
    el("wake_straight", '''{n}She breathes out against your ear, not quite a laugh.{/n}
"True. You watched me smell you and be disgusted, and you enjoyed it. I thought you were only rude." {n}Her cheek stays against yours.{/n} "You are worse than rude, Commander. You are curious. Now mine."''',
       c("Continue", "hers", flags=(WHISPER_WAKE,))),
    el("lie", '''{n}She is silent for a long breath. Then she sits back, a hand's width, which in that dark is as far as the other side of a room.{/n}
"No." {n}Quite gently.{/n} "That was a lie. It sat at the top of the words, where lies sit. I told you the Way would teach you to hear the difference. I did not tell you it would teach me first."
"I will still tell you mine. That is the custom: you break it, and I keep it, so that you owe me." {n}She leans back in.{/n}''',
       c("Continue", "hers", flags=(WHISPER_LIE,))),
    el("hers", '''{n}When she speaks, it is so quietly that you are not certain, afterwards, that you heard it at all.{/n}
"I am afraid she will never take me. That I will be useful and mortal and grey until I die like one of your cattle, in a bed, of something stupid, and she will not even come to the table." {n}Her hand tightens on your wrist.{/n} "I have waited half my life. Every morning I wake warm, and it is a small death."
{n}Then she lets go of you, and stands, and she is Elyanka Camilary again, straight-backed and cold.{/n} "You did not hear that. Go home."''',
       c("[Go home, and never repeat it.]")),
], requires=(TESTED,), forbids=(WHISPER_FEAR, WHISPER_WAKE, WHISPER_LIE), delay=24, last=5, optional=False)


# --- 9. A box that pinches (T, optional): the fitting. -------------------------------------------------------------------

FIT_LAY = E + "fitting.lay"
FIT_HER = E + "fitting.her_first"
FIT_REFUSED = E + "fitting.refused"

visit(E + "beat.fitting", "A box that pinches", [
    nar("start", '''{n}One of her six is a joiner. You had not known it until tonight, when you find him in the dead-house yard under a lantern, planing black wood with the absolute silence he brings to everything, and a long shape on two trestles behind him, open at the top, lined with dark red cloth.{/n}
{n}It is not a coffin. It is shallower than a coffin, and wider, and its edges are carved with fruit and vines and little bones.{/n}''',
        c("Continue", "her")),
    el("her", '''"It is a table." {n}Elyanka is sitting on the edge of the hearse's step with her knotted cord in her lap, watching him work.{/n} "My Lady does not bury anything. What is laid before her is served. The Way's joiners in Caliphas will make the true one, in ebony, when your measure reaches them. This is his practice piece. He is a perfectionist."
"Take off your boots, Commander. I want to see whether it pinches."''',
       c("[Take off your boots and lie down in it.]", "lay"),
       c('"You first."', "first"),
       c('"I\'m not lying in my own serving dish."', "refuse")),
    nar("lay", '''{n}The red cloth is cold, and smells of new wood and cloves. It fits you better than your own bed does. You lie with your hands at your sides and look up at the lantern and the black wood and the carved grapes above your face, and the joiner leans over you with a rule and measures, silently, from your crown to your heel.{/n}
{n}Elyanka comes and stands over you with her arms folded. She looks for a long while, and does not say anything at all, and her face does something you have not seen it do before.{/n}''',
        c("Continue", "lay2")),
    el("lay2", '''"It fits," {n}she says at last, and her voice is not quite steady.{/n} "That is the most indecent thing I have ever seen, and I have seen a great deal."
{n}She bends and puts her cold hand flat on your chest, over the heart, and leaves it there while it beats against her palm, as if she were counting what she is owed.{/n} "Get out of it. Now. Before I forget whose it is for, and close the lid."''',
       c("[Climb out.]", flags=(FIT_LAY,))),
    el("first", '''{n}She looks at you as if you had asked her to take off her face. Then, slowly, something like delight comes into her eyes.{/n}
"Impertinent." {n}She stands, and unlaces her boots, and steps up onto the trestle, and lies down in the red cloth with her grey robe settled around her and her hands folded on her breast, perfectly composed, like a queen on a tomb.{/n}
"Look, then. You wanted to see."''',
       c("Continue", "first2")),
    nar("first2", '''{n}She lies rigid on the red cloth, her jaw clenched, her boots set neatly beneath the trestle.{/n}
{n}You look at her there for a long while: the silver hair spread on the red, the pale throat, the strong hands folded and still. When she opens her eyes you are still looking, and she sees what is in your face, and for once she has nothing sharp to say about it.{/n}
"Help me out," {n}she says instead.{/n} "It is not mine. It will never be mine. And it is very cold."''',
        c("[Lift her out.]", flags=(FIT_HER,))),
    el("refuse", '''"Not your serving dish. My Lady's." {n}She shrugs, a small cold movement.{/n} "You will lie in it one day whether you try it now or not. I only wanted to know whether I should tell them to plane the shoulders."
{n}She turns to the joiner.{/n} "Plane the shoulders. Commanders always come to the table heavier than they left the field. It is the armour. It gets into the meat."''',
       c("[Leave them to their work.]", flags=(FIT_REFUSED,))),
], requires=(BIER,), forbids=(FIT_LAY, FIT_HER, FIT_REFUSED), delay=60, last=5)


# --- 10. A master from Caliphas (T, optional): her own order comes to hurry the claim. ------------------------------------

MASTER_KILLED = E + "master.killed"
MASTER_ESCORTED = E + "master.escorted"
MASTER_HERS = E + "master.hers"

visit(E + "beat.master", "A master from Caliphas", [
    nar("start", '''{n}There is a stranger at the trestle in the dead-house tonight: a thin man in a black coat, bald, with a face like a peeled egg and very small, very clean hands. He is eating nothing. Elyanka sits across from him with her back even straighter than usual, and when you come in she does not rise, and she does not look at you, and that tells you more than anything she could have said.{/n}''',
        c("Continue", "courier", requires=(COURIER_HUNGRY,)),
        c("Continue", "courier", requires=(COURIER_RIPENING,), forbids=(COURIER_HUNGRY,)),
        c("Continue", "master", forbids=(COURIER_HUNGRY, COURIER_RIPENING))),
    el("courier", '''"The master from the house on the Ustalav road," {n}she says, without turning her head.{/n} "The one my courier told you about. He did not believe me about the goods. He has come to look at them himself."''',
       c("Continue", "master")),
    n("master", "Master of the Way", '''"Knight Commander." {n}His voice is soft and dry, like paper being folded.{/n} "The Way congratulates you on your health. It is excellent. That is, if you will forgive me, the difficulty."
"Our sister was sent to collect a corpse. She has instead collected a debtor, who may keep us waiting generations. The Way is patient, but it is not a pawnbroker. The masters in Caliphas would like the terms improved." {n}He smiles.{/n} "We would not dream of harming you. We only propose that the date be... discussed."''',
      c('"Discussed how?"', "how"),
      c('"The terms were whispered. They don\'t change."', "terms")),
    n("how", "Master of the Way", '''"Kindly. There are gentle ways to die, Commander, and the Way knows all of them. And after the death, a far better existence than this one: no fear, no fatigue, no end. Our sister has told you what undeath is. It is the truest form there is." {n}He folds his small hands.{/n} "You would be offered it. A mythic mind in a mythic body that never tires. The masters would be honoured."
{n}Across the table Elyanka's knuckles have gone white on the handle of her knife.{/n}''',
      c("Continue", "her")),
    n("terms", "Master of the Way", '''"Whispered, yes. To her." {n}He inclines his head toward Elyanka without looking at her.{/n} "Our sister has been in Drezen a long time. She eats with you, I hear. She has let you into a carriage that was built for your corpse. The masters wonder whether the terms she whispered were the Way's terms, or her own."
{n}Across the table Elyanka's knuckles have gone white on the handle of her knife.{/n}''',
      c("Continue", "her")),
    el("her", '''{n}She speaks to him, not to you, and very quietly.{/n}
"The claim is mine. The Way sent me for it. The Commander gave me the claim, and the terms were whispered to me and by me. When the Commander dies the body goes to my Lady's table whole, and not one day before. That is what a claim is." {n}Her voice drops further.{/n} "If the Way wants to hurry my collateral into the ground, it will have to go through its collector. And the collector has waited half her life to be adopted, master, and has nothing at all to lose."''',
       c("Continue", "choice")),
    nar("choice", '''{n}The master looks from her to you, and his smile does not move. Then he rises, and bows, the precise bow of a man who has been insulted and has made a note of it.{/n}
"The Way will consider its position," {n}he says,{/n} "on the road home." {n}And he goes out into the yard, where his own carriage is waiting.{/n}
{n}Elyanka does not watch him go. Only now does she look at you, and her eyes are perfectly calm.{/n} "He will not consider anything on the road home. He will tell the masters that I have gone soft, and they will send someone who is not a clerk. Unless he does not reach the border."''',
        c('[Give her the road] "Then he doesn\'t reach the border. It\'s a long road."', "kill"),
        c('[Give him an escort] "He came under your oath. He leaves under mine. Twelve crusaders to the border."', "escort"),
        c('[Leave it to her] "He\'s your master, and your order. You decide."', "hers")),
    el("kill", '''{n}She does not smile. She nods once, as she might to a tradesman who had quoted a fair price, and makes a small gesture toward the door. Two of her six men in grey detach themselves from the wall of the yard and walk out into the dark after the master's carriage, not hurrying.{/n}
"You understand that he is my master," {n}she says,{/n} "and that I have just had him killed for you." {n}She considers this.{/n} "No. For my Lady. A master who would hurry an offering to her table half-ripe insults her. I have done her a service tonight." {n}She smiles, showing strong white teeth.{/n} "And the Way will learn that the priestess in Drezen keeps her collateral the way she keeps her faith: with a knife."''',
       c("Continue", "kill2")),
    nar("kill2", '''{n}Three days later a carriage is found in a ditch on the Ustalav road, south of the Mendevian border, with its horses gone and nobody inside it. The report reaches your desk as an item of no great interest, between a bill for tallow and a complaint about a sergeant.{/n}
{n}That night she is waiting in your quarters. She pushes the report aside, catches your collar and pulls you against her. Her fingers shake once before they tighten. "The date stays where I put it," she says against your mouth. "Not tonight."{/n}''',
        c("Continue", flags=(MASTER_KILLED,))),
    el("escort", '''{n}Her eyes narrow.{/n} "Twelve crusaders. To see a master of the Whispering Way safe out of your country." {n}She draws a long breath.{/n}
"You are a fool, Commander. He will reach Caliphas, and he will speak, and the Way will remember that you protected the man who came to hurry your death. That is the kind of thing the Way finds interesting."
{n}Then, grudgingly:{/n} "It was also lawful, and I have been hiding behind your law for weeks, and I cannot very well complain when you hide behind it too. Go and give your orders. I will be here, being disappointed."''',
       c("[Give the orders.]", flags=(MASTER_ESCORTED,))),
    el("hers", '''{n}She studies you across the trestle, and something passes over her face that might, in another woman, be gratitude. In her it looks like hunger.{/n}
"Then I will decide." {n}She rises, and takes the knife she has been holding all evening, and puts it in her sleeve.{/n} "Go to bed, Commander. Do not ask me in the morning what I decided. You gave it to me. It is mine."
{n}In the morning she is in the dead-house as usual, eating. Her sleeve is clean. You do not ask, and you never learn, and a certain master of the Way is never seen in Caliphas again.{/n}''',
       c("[Do not ask.]", flags=(MASTER_HERS,))),
], requires=(BIER,), forbids=(MASTER_KILLED, MASTER_ESCORTED, MASTER_HERS), delay=120, last=5,
    any_groups=((BIER, COURIER_HUNGRY, COURIER_RIPENING, COURIER_SILENT),))


# --- 11. The King's bill (T, optional; only where the King holds court and his court wept at the wake). --------------------

KING_BILL = E + "king.bill_paid"
KING_BILL_HERS = E + "king.bill_hers"

visit(E + "beat.king_bill", "The King's bill for weeping", [
    nar("start", '''{n}You arrive at the dead-house to find the Fool King of Drezen sitting on the trestle with his boots on the bench, a paper crown on his head and a roll of paper in his hand long enough to reach the floor. Elyanka stands at the far end of the long room, as far from him as the walls allow, holding her napkin over her nose.{/n}''',
        c("Continue", "bill")),
    n("bill", "Thaberdine", '''"Commander! Just in time. I've been presenting my bill." {n}Thaberdine unrolls another yard of it.{/n} "Weeping at a wake: one court, all hands. Wailing, extra. The fire-eater's chest, bruised: extra. Me, carried in on a door, tragic: very extra. And now I find out the corpse sat up and gave itself away. That's a second funeral in one year, and that's a royal holiday by law. I made the law this morning."
"So somebody owes the crown for two wakes. And she," {n}he points with a sausage,{/n} "won't pay, because she says she's not the bereaved."''',
      c("Continue", "her")),
    el("her", '''"I am not the bereaved." {n}Her voice is muffled by the napkin.{/n} "I hold the claim. I did not hire the mourners. That was your executor's business. Everyone in Ustalav knows that."
{n}She lowers the napkin an inch.{/n} "And your King smells of beer, Commander. The smell came in with the crown. The most alive thing I have ever been in a room with, and I include you."''',
       c("Continue", "king2")),
    n("king2", "Thaberdine", '''"Alive! Ha! Thank you, madam. You're the first person in this city to notice." {n}The King beams at her with enormous goodwill.{/n} "I like her, Commander. She's a proper grump. Every court needs one. I've been looking for a Royal Undertaker since the last one fell in the moat. Pays in beer, and all the funerals you can eat."
{n}Elyanka looks at him as if a dog had asked her to dance.{/n}''',
      c('[Pay the bill] "Put it on the crusade, Majesty. Both wakes."', "pay", crusade=("Finances", -50)),
      c('[Make her pay] "She\'s the one who got a corpse out of it, Majesty. Bill the Way."', "hers")),
    nar("pay", '''{n}Thaberdine rolls up the bill with tremendous ceremony, knights it with the sausage for services to the treasury, and eats the sausage.{/n}
"A generous corpse! Best kind. Madam, the post of Royal Undertaker stays open. Think about it." {n}He climbs down from the trestle, bows to Elyanka so low that his crown falls off, and goes out singing something about a king who died twice and was buried in beer.{/n}''',
        c("Continue", "pay2")),
    el("pay2", '''{n}She waits until the singing has gone all the way down the lane. Then she takes the napkin away from her face.{/n}
"Royal Undertaker." {n}She says it as if it were a disease.{/n} "In Caliphas they would have had him on a spit for that. Here you pay his bill for weeping over you." {n}Her mouth twitches.{/n} "Your country is ruled by a drunkard, and your drunkard is ruled by you, and you let him think it is the other way round. It is almost elegant. I shall never say so to anyone."''',
       c("[Take her home to her own table.]", flags=(KING_BILL,))),
    el("hers", '''"The Way?" {n}She lowers the napkin completely. For a moment you think she will draw her knife on the King of Drezen in his own city.{/n}
{n}Then she reaches into her sleeve and puts a single heavy coin on the trestle: black, old, stamped with a crowned skull that you do not recognize.{/n} "Ustalav. Before the Tyrant fell. It is worth more than his tavern." {n}She pushes it toward him with one finger.{/n} "For the weeping, Majesty. It was very good weeping. I have heard worse at real funerals."''',
       c("Continue", "hers2")),
    nar("hers2", '''{n}Thaberdine bites the coin, pronounces it genuine and horrible, and puts it in his crown for safe keeping. He leaves with his bill trailing behind him down the lane.{/n}
{n}Elyanka watches him go.{/n} "That coin was my father's," {n}she says.{/n} "The last thing I took from his house before I left it. I have carried it since I was nineteen, for something worth spending it on." {n}She shrugs, a small cold movement.{/n} "A drunkard's grief for a debtor who did not die. My father would have hated it. That is why."''',
        c("[Say nothing about the coin.]", flags=(KING_BILL_HERS,))),
], requires=(BIER, E + "mourners", "fool_king.available"), forbids=(KING_BILL, KING_BILL_HERS, "fool_king.gone"), delay=48, last=5)


# --- 12. Daeran's first bottle (T, optional): the reactor's wine arrives. ------------------------------------------------

DAERAN_TASTED = E + "daeran.bottle_tasted"

visit(E + "beat.daeran_bottle", "A bottle older than she is", [
    nar("start", '''{n}There is a bottle on the trestle in the dead-house, black glass furred with the dust of a cellar, with a label so old it has gone the colour of tea, and a card propped against it in a hand of extravagant loops: *With the compliments of the house of Arendae, on the occasion of a funeral that has not yet happened. Do try not to enjoy it.*{/n}
{n}Elyanka is already turning the bottle to the candle to read the year, and her nostrils are flared like a hound's.{/n}''',
        c("Continue", "her")),
    el("her", '''"Your count sent this." {n}She does not touch it.{/n} "A count with a crypt full of relatives and a face like a spoiled cherub. The bottle was dispatched when he made his funeral offer. His servants have taken their time delivering it."
"He meant it as a lesson. He thought a woman from the Ustalav hills has never tasted anything older than her grandmother, and wanted to watch me learn." {n}Her mouth thins.{/n} "I will drink every drop of his lesson, and he will never hear that I liked it. Open it."''',
       c("[Open it and pour for both of you.]", "pour")),
    nar("pour", '''{n}The cork crumbles. The wine is so dark it is almost black, and it smells of dust, and plums, and something underneath like the inside of an old church. She breathes it in with her eyes shut, greedily, the way she eats, and drinks the whole cup slowly, and makes a low sound in her throat that is almost indecent.{/n}
{n}Then she holds the cup out to be filled again, without opening her eyes.{/n}''',
        c("Continue", "verdict")),
    el("verdict", '''"It is older than I am," {n}she says, after the second cup.{/n} "It was made before my father was born, and it has outlived him, and it has been waiting in the dark all this time to be drunk by someone who deserved it. That is what my Lady promises. That is exactly it."
{n}She sets the cup down very carefully.{/n} "My verdict for your count: mediocre; did not finish it; send the rest. Should his house ever ask, give them those words. Not a word about the cork. I am keeping it."''',
       c("[Pour what remains.]", flags=(DAERAN_TASTED,))),
], requires=(E + "daeran_ally",), forbids=(DAERAN_TASTED,), delay=24, last=5)


# --- 13. The wards (T, optional): her Lady's mercy, offered to the dying of Iz. -------------------------------------------

WARDS_STOPPED = E + "wards.stopped"
WARDS_LET = E + "wards.let"
WARDS_HOPELESS = E + "wards.hopeless_only"

visit(E + "beat.wards", "Her Lady's mercy", [
    nar("start", '''{n}The fever ward is in the old granary by the north wall, where the wounded from Iz who did not die on the road are dying more slowly. The chaplains have gone to sleep at last. There is one lamp at the far end, and a grey shape moving from cot to cot in its light, bending over each one.{/n}
{n}You know the shape before you are close enough to see her face.{/n}''',
        c("Continue", "her")),
    el("her", '''"Commander." {n}She does not straighten from the cot she is bending over. On it a boy with a bandaged stump where his right arm was looks up at her with enormous, grateful eyes.{/n}
"Do not make a scene. He is nearly asleep." {n}She holds a cup to his lips, and he drinks, and she wipes his mouth with a corner of her grey sleeve. Her free hand closes over the little sword of Iomedae on his blanket and turns it face down.{/n}''',
       c("[Wait until she has finished.]", "explain"),
       c('"What did you give him?"', "cup")),
    el("cup", '''"Poppy, and wine, and honey. Nothing else. Do you think I poison children in their beds?" {n}Her mouth twists.{/n} "My family died over a dish of lamb. I raised them afterward. All but my father. He stayed in the ground." {n}She tips the cup to show you the dregs.{/n} "This is wine. I want him listening, not dead."''',
       c("Continue", "explain")),
    el("explain", '''{n}She moves on to the next cot, and you follow. A sergeant with a belly wound, grey in the face, breathing through his teeth. She kneels beside him, and takes his hand, and bends until her mouth is by his ear, and whispers. You cannot hear what she says. You can see his face ease.{/n}
"I am telling them about the table," {n}she says, when she rises.{/n} "Your chaplains taught them to be ashamed of hunger. I tell them my Lady wants it. Meat, wine, flesh — everything they have been denying themselves while demons chew through their comrades. Let them call on her for once."''',
       c("Continue", "explain2")),
    el("explain2", '''"Your chaplains tell them about judgment. The grey warden and her scales and her long queue. Half these men are more frightened of dying than of the demon that killed them." {n}She looks down the long dark ward.{/n}
"I promise them my Lady's feast beyond the grave. Let the grey warden try to keep them from it. Your chaplains have a whole city to preach in. I want these cots." {n}She meets your eyes.{/n} "Well, Commander? It is your ward."''',
       c('[Stop her] "Not here. These men are crusaders. They die as crusaders."', "stop"),
       c('[Let her] "If it eases them, whisper."', "let"),
       c('[Only the hopeless] "The ones the chaplains have given up on. Nobody else."', "hopeless")),
    el("stop", '''{n}She looks at you over the sergeant's cot. Then she sets the cup down on the floor by the sergeant's cot, very precisely, and folds her hands in her sleeves.{/n}
"As crusaders. In lime, with prayers, in a queue." {n}She bares her strong white teeth.{/n} "Your chaplains leave them trembling all night, and you would rather keep them frightened than let them call on my Lady."
{n}She snatches up the cup and empties it into the slop bucket.{/n} "Fetch a chaplain, then. Let him hear what they say about his goddess when the poppy wears off."''',
       c("Continue", "stop2")),
    nar("stop2", '''{n}You sit with the boy until the lamp goes out. He does not ask for her again, and he does not die before morning, and he does not die the morning after either. When the chaplains come round he is sitting up and asking for bread.{/n}
{n}Elyanka passes the open granary door as a chaplain brings him a loaf. She sees the little sword of Iomedae hanging at his throat again and spits into the gutter.{/n}''',
        c("Continue", flags=(WARDS_STOPPED,))),
    nar("let", '''{n}She bows her head to you, the smallest movement, and goes back to her cots. You stand at the door and watch her work down the ward, kneeling by each one, whispering, holding cups, wiping mouths, the grey robe dragging in the straw.{/n}
{n}Near dawn the sergeant with the belly wound dies. He dies smiling, with her hand in his, and his last word is a name that is not Pharasma's.{/n}''',
        c("Continue", "let2")),
    el("let2", '''"There," {n}she says, closing his eyes with two fingers.{/n} "He called for my Lady. Not yours."
{n}She pulls the sergeant's blanket over his face and takes his untouched ration of wine.{/n} "I promised him a seat. I shall ask her to keep it for him." {n}She drinks, then kneels at the next cot. The lamp is burning low.{/n} "Your chaplains can have the burial. I had his last prayer."''',
       c("[Leave her with the dead.]", flags=(WARDS_LET,))),
    el("hopeless", '''"The hopeless." {n}She tastes it, and something like approval moves in her face.{/n} "Your chaplains have given up on eleven in this ward. I counted them before you came. You would let me have the ones the grey warden already has her hand on, and not one more."
"You haggle over the dying, Commander. At the edge of the grave, you haggle." {n}She almost smiles.{/n} "Eleven, then. Keep the rest for your chaplains." {n}She pushes the boy's cot aside to reach the dying sergeant.{/n} "Bring another lamp. I will not lose one of these to the dark."''',
       c("Continue", "hopeless2")),
    nar("hopeless2", '''{n}She keeps it. You watch her pass the boy with the arm without a glance, though he calls after her, and kneel by the eleven, one by one, with her cup and her whisper.{/n}
{n}Seven of them die before dawn. All seven die quietly. The boy with the arm lives, and in the morning asks the chaplain where the grey lady went, and the chaplain does not know what he means.{/n}''',
        c("Continue", flags=(WARDS_HOPELESS,))),
], requires=(BIER,), forbids=(WARDS_STOPPED, WARDS_LET, WARDS_HOPELESS), delay=48, last=5)


# --- 14. The Tyrant's seals (T, optional): what a planner does with a creditor's secrets. --------------------------------

TYRANT_KEPT = E + "tyrant.kept"
TYRANT_WARNED = E + "tyrant.lastwall_warned"
TYRANT_TOLD = E + "tyrant.told_her"

visit(E + "beat.tyrant", "The Tyrant's seals", [
    nar("start", '''{n}She is in a good mood tonight, which in her looks like cruelty with the edges filed off. There is wine, and a map of Avistan she has had one of her six pin to the dead-house wall, old and soft at the folds, with the Worldwound a brown stain at the top and Ustalav a grey smudge in the south.{/n}''',
        c("Continue", "map")),
    el("map", '''"Look." {n}She traces a long finger down into the grey smudge of Ustalav, to a small black tower drawn among the hills.{/n} "Gallowspire. Where your Shining Crusade buried my Lady's greatest servant under a Great Seal and three little ones, and called it victory, and went home."
"Tar-Baphon. The Whispering Tyrant. He challenged Aroden and lost, and rose again as a lich, and conquered Ustalav, and ruled it six hundred years." {n}Her finger rests on the black tower.{/n} "Two of the three lesser seals are gone, Commander. And Aroden, his old enemy, is dead. We believe the Tyrant won their quarrel after all."''',
       c('"Why tell me this?"', "why"),
       c("[Say nothing. Let her talk.]", "talk")),
    el("why", '''"Because you hold my claim, and I hold yours, and between two such people there should be something worth knowing." {n}She pours for you.{/n} "And because you will not live to see it, whatever you do. You will be on my Lady's table long before he walks out of that tower."''',
       c("Continue", "talk")),
    el("talk", '''"When he comes back," {n}she says, and her eyes brighten as she traces the road to Gallowspire with one hard fingertip,{/n} "Ustalav will be what it was. The counts will kneel. The churches of the grey warden will be shut. My Lady will be worshipped openly in every town from Caliphas to Lastwall, and the dead will walk in the streets in daylight, and nobody will be afraid of them, because everyone will be one."
"I will see it. My Lady will have adopted me by then. I will stand at his gate with a cup in my hand." {n}She drinks.{/n} "You will be under glass in Caliphas, preserved, very handsome. I shall visit."''',
       c("Continue", "choice")),
    nar("choice", '''{n}She is a little drunk, or wants you to think so. The prison and its seals are no secret. What she has shown you is her pleasure at the thought of Ustalav on its knees. She watches you over her cup, waiting to see whether you recoil or drink with her.{/n}''',
        c("[Remember every word. Say nothing. Tell no one yet.]", "kept"),
        c("[Later, alone, write to Lastwall.]", "warned"),
        c('[Tell her what she has just done] "You\'ve told the Knight Commander of a crusade how eagerly you await your Tyrant."', "told")),
    el("kept", '''{n}You say nothing. You drink her wine, and let her talk about the gate of Gallowspire and the counts kneeling in the rain, and you keep every word in the back of your head, filed, the way a quartermaster keeps a list of what is in the stores.{/n}
{n}Near midnight she stops talking and looks at you over her cup.{/n} "You are very quiet. You are saving it. I can see you saving it." {n}She smiles, showing strong white teeth.{/n} "Good. I would think less of a debtor who did not."''',
       c("[Save it.]", flags=(TYRANT_KEPT,))),
    nar("warned", '''{n}You let her talk. You laugh in the right places. You leave the dead-house a little after midnight, and walk back up through the sleeping lower town to your quarters, and light a lamp, and write for an hour, very carefully, in a plain hand, to a knight of Lastwall whose name you know and who does not know yours.{/n}
{n}It describes the Way's hopes as she spoke them tonight. It claims no new breach in the seals and names no planned attack. You seal it with no device and send it south with a courier who owes you money.{/n}''',
        c("Continue", "warned2")),
    nar("warned2", '''{n}She says nothing about it the next time you see her, or the next. She eats as she always does, and mocks your smell as she always does, and you begin to think that the Way does not know everything after all.{/n}
{n}Then, one evening, she pauses with a piece of bread halfway to her mouth.{/n} "A courier who owes you money is a courier who owes other people money too," {n}she says pleasantly, and eats the bread, and says nothing else about it, then or ever.{/n}''',
        c("Continue", flags=(TYRANT_WARNED,))),
    el("told", '''{n}She stops with the cup at her lips. For a moment her face is perfectly still; then the colour comes up under her skin, slowly, from the throat.{/n}
"Yes," {n}she says.{/n} "I have. I have told a crusader how much I want those churches shut." {n}She sets the cup down.{/n} "And you have told me that you noticed, instead of simply using it. That is either very foolish or very clever, and I do not know which, and I do not like not knowing."
"Do what you like with it, Commander. It is a whisper. You cannot prove you heard it. I cannot prove I said it." {n}Her hand closes over yours on the table, cold and very hard.{/n} "But if a single knight of Lastwall rides for Gallowspire this year, I will know whose whisper sent him."''',
       c('"Then no knight will ride."', flags=(TYRANT_TOLD,)),
       c('"Then you\'ll know."', flags=(TYRANT_TOLD,))),
], requires=(BIER,), forbids=(TYRANT_KEPT, TYRANT_WARNED, TYRANT_TOLD), delay=72, last=5)


# --- 15. The Camilary daughters (T, optional): what she kept of her family. ------------------------------------------------

SISTERS_ASKED = E + "sisters.asked"
SISTERS_LET_BE = E + "sisters.let_be"

visit(E + "beat.sisters", "Six sisters", [
    nar("start", '''{n}She is sitting on the step of the hearse with something small in her lap when you come into the yard: a flat case of dark wood, open, with six ovals inside it on faded velvet. Miniatures. Six girls, painted by the same careful, provincial hand, each with the same strong dark brows.{/n}
{n}She does not close it when she sees you. That, from her, is an invitation.{/n}''',
        c("Continue", "case")),
    el("case", '''"My sisters," {n}she says.{/n} "Painted the year before the woods, by a man my father brought from Caliphas. He charged by the face. My father thought it extravagant." {n}She touches the edge of one oval with a fingertip.{/n}
"I told you I gave them all my Lady's gift. The lamb, and then the gift. You did not ask what became of them after. Nobody ever asks what becomes of them after."''',
       c('"What became of them?"', "after"),
       c("[Sit down beside her and look at the faces.]", "faces")),
    el("faces", '''{n}You sit on the step beside her, close enough that her robe touches your knee, and look at them one by one. She lets you. She does not say which is which, and you do not ask. After a while she speaks anyway, to the case, not to you.{/n}''',
       c("Continue", "after")),
    el("after", '''"Four of them are still in the Camilary house. They keep it. They do not go out in daylight, and they do not need to eat, and they are never, ever afraid." {n}Her voice is quite even.{/n} "My mother is with them. My brothers went south, to the Way. One of them is a master now. He does not come home, but I hear."
"Two of my sisters would not take the gift properly. Every night I put them in their beds, and every night they get up and walk to the churchyard and lie down on the grass, as if they were still waiting to be buried." {n}Her finger rests on one oval.{/n} "They want the warden's queue. They want to be judged. Ingratitude. My Lady gave them forever, and they would rather have a hole."''',
       c('"What did you do with them?"', "what"),
       c("[Say nothing. Leave her the case.]", "silence")),
    el("what", '''{n}She closes the case, very gently, with both hands.{/n}
"Nothing. They are mine." {n}Her voice does not change at all.{/n} "The servants carry them back from the churchyard every morning, wet with dew, and chain them in their beds, and every night they slip the chains and walk out again. I shall go on having them fetched until they learn to be grateful, or until the stars go out."
{n}She looks at you then.{/n} "You asked. Now you know what I do with things that are mine and want to leave. Do not make a habit of wanting it."''',
       c("[Take her hand.]", flags=(SISTERS_ASKED,))),
    el("silence", '''{n}You say nothing. After a while she closes the case herself, with both hands, gently, and puts it inside her robe against her breast.{/n}
"You are learning," {n}she says.{/n} "Most people cannot bear a silence at a graveside. They fill it with something stupid." {n}She stands.{/n} "Come inside. I am hungry, and I would like to watch you eat."''',
       c("[Follow her in.]", flags=(SISTERS_LET_BE,))),
], requires=(BIER,), forbids=(SISTERS_ASKED, SISTERS_LET_BE), delay=96, last=5)


# --- 16. Her eyes on the hands (T, optional; only after a failed wake): the face, read again. -----------------------------

FACE_READ = E + "face.read"

visit(E + "beat.face", "A liar's face", [
    nar("start", '''{n}Since the night of the wake she has not once looked at your face when anything mattered. She looks at your hands. At your throat. At the vein at your temple. You have grown used to talking to the top of her head.{/n}
{n}Tonight she is waiting in the dead-house with a stick of charcoal and a sheet of heavy grey paper pinned to a board, and she points at the stool across from her with the charcoal.{/n}''',
        c("Continue", "draw")),
    el("draw", '''"Sit. Do not talk. Do not smile." {n}She begins to draw, fast, with quick hard strokes, and still she does not look at your face; she looks at the paper, and at your hands in your lap, and at your throat, and draws.{/n}
"I do not put what matters on paper. Drawing is not writing." {n}The charcoal scratches.{/n} "I am going to draw the face that lied to me in a veil, from everything else about you that does not lie. Then I will look at the drawing instead of at you. It will be a great deal more honest."''',
       c("[Sit still, and let her draw.]", "done"),
       c('[Take the charcoal from her] "Look at me. Just once."', "look")),
    el("done", '''{n}It takes an hour. When she turns the board round, the face on it is yours, and not quite yours: harder about the mouth, older about the eyes, the face of someone who would sit through their own wake in crepe to learn their price.{/n}
"There," {n}she says.{/n} "That one I believe." {n}She unpins it and rolls it up and puts it in her sleeve.{/n} "I will talk to it when I need to know what you really think. You may keep the other one. It is no use to me."''',
       c("[Let her keep it.]", flags=(FACE_READ, E + "face.drawn"))),
    el("look", '''{n}Her hand closes on the charcoal and on your fingers together. For a moment she does not lift her eyes; you can see her deciding not to.{/n}
{n}Then she does. She looks at your face, as she has not once since the veil came off, for as long as it takes a candle to gutter and steady, with those pale unblinking eyes, and whatever she finds there she does not say.{/n}
"Once," {n}she says, and lets go of the charcoal.{/n} "That was once. Do not ask again. I have to go on believing you are a liar. If I stop, I will start believing that a sweating crusader has a better claim on me than the masters in Caliphas, and the Way kills priestesses who believe that."''',
       c("[Give her back the charcoal.]", flags=(FACE_READ, E + "face.looked"))),
], requires=(EXPOSED, BIER), forbids=(FACE_READ,), delay=48, last=5)



# --- 18. The stone they raised (T, optional): the grave from the funeral, empty. -----------------------------------------

GRAVE_LAY = E + "grave.lay"
GRAVE_DOWN = E + "grave.stone_down"
GRAVE_KEPT = E + "grave.stone_kept"

visit(E + "beat.grave", "The stone they raised", [
    nar("start", '''{n}She wants to see your grave. She says so across the trestle, over breakfast, and she will not be put off.{/n}
{n}There is one. You had forgotten. When Drezen declared you dead, the garrison raised a stone for you in the burying ground under the east wall, since there was nothing to put under it, and nobody has thought to take it down. It stands at the end of a row of real graves, a slab of grey Mendevian granite with your name cut deep and a line of scripture under it, slightly misspelled.{/n}''',
        c("Continue", "stone")),
    el("stone", '''{n}She walks all round it, twice, reading every letter. Then she lays her palm flat on the top of it, the way a physician lays a palm on a fevered chest.{/n}
"The only grave in the world with your name on it, and nothing in it." {n}She sounds almost tender.{/n} "Do you know how rare that is? A grave that has been dug and wept over and prayed at, and is still waiting? In Ustalav we would make a shrine of it. People would come from Caliphas to sit here."
"A place waiting for what you pledged, Commander. Nothing in it yet." {n}She pats the stone.{/n} "The hole under it."''',
       c("[Lie down on your own grave.]", "lay"),
       c('"I\'ll have them take it down. I\'m not dead."', "down"),
       c('"Then it\'s yours. I\'ll leave it standing."', "kept")),
    nar("lay", '''{n}The grass over the empty ground is thick and cold with dew. You lie down on it with your head under your own name, and your hands folded, and look up at the grey Drezen sky between the gravestones.{/n}
{n}She stands over you for a while, the hem of her grey robe wet with dew. Then, very slowly, she lies down beside you on the grass, on the side where a wife is buried, and folds her own hands, and looks at the same sky.{/n}''',
        c("Continue", "lay2")),
    el("lay2", '''"It is too soft," {n}she says after a while.{/n} "The ground. Mendevian graves are always too soft. Nothing keeps in them."
{n}Her little finger finds yours on the grass, and hooks it, and stays.{/n} "In Ustalav the ground is hard, and cold, and everything that goes into it is still there a hundred years later, waiting to be asked." {n}A long breath.{/n} "Get up before somebody sees the Knight Commander lying on {mf|his|her} own grave with a priestess of Urgathoa. I will stay a little longer. It is very peaceful here, with you breathing."''',
       c("[Get up, and leave her there.]", flags=(GRAVE_LAY,))),
    el("down", '''{n}She takes her hand off the stone as if it had become hot.{/n}
"Take it down." {n}Her voice is perfectly flat.{/n} "The one grave in Golarion that has been honestly waiting for you, and you would knock it over because it embarrasses you." {n}She looks at the stone, not at you.{/n}
"As you like. It is your name. But I will have the stone, Commander, when your masons have broken it out of the ground. I will take it home to Ustalav in the hearse, and set it up in the Camilary woods, and one day I will put under it what it was cut for."''',
       c('"Take it, then."', flags=(GRAVE_DOWN,))),
    el("kept", '''"Mine." {n}She says it very quietly, with her palm still on the granite.{/n} "Then let it stand. Let the grass grow over it, and the priests pray at it on their holy days, and the soldiers who were at your funeral feast come here drunk and weep for you, and all the time you are up in the citadel, warm, eating their bread."
"I shall come here in the evenings, and sit on it, and read. No one will dare to ask me why." {n}She almost smiles.{/n} "It is the nicest thing anyone has ever given me that they did not know they had."''',
       c("[Leave her with her grave.]", flags=(GRAVE_KEPT,))),
], requires=(BIER,), forbids=(GRAVE_LAY, GRAVE_DOWN, GRAVE_KEPT), delay=36, last=5)


# --- 19. Where they lock the shutters (T, optional): Ustalav, from the walls of Drezen. -----------------------------------

USTALAV_PROMISED = E + "ustalav.promised"
USTALAV_REFUSED = E + "ustalav.refused"
USTALAV_WOODS = E + "ustalav.woods"

visit(E + "beat.ustalav", "Where they lock the shutters", [
    nar("start", '''{n}She finds you on the south wall at the end of the second watch, where you have gone to be alone, and does not ask whether she may stay. She stands beside you at the parapet in her grey robe with her hands in her sleeves, looking south, down the long dark road she came up in the hearse.{/n}
{n}Far down it, past the last campfires, there is nothing: no lights, no farms, only the black line of the hills where Mendev ends.{/n}''',
        c("Continue", "road")),
    el("road", '''"Four hundred miles," {n}she says.{/n} "And then the mist. You cannot see Ustalav from anywhere, Commander. It does not allow it."
"It is a grim land. Everyone is afraid of us, and everyone plots against us, and so we are harsh by nature and trust no one. It is the place where they lock their shutters at night, where monsters walk the woods, and the cemeteries do not lie quiet." {n}There is pride in it, and something close to hunger.{/n} "It is the most beautiful country in the world."''',
       c('"Tell me about your woods."', "woods"),
       c('"I\'ll see it one day."', "promise"),
       c('"It sounds like a country I\'d rather not see."', "refuse")),
    el("woods", '''{n}Something in her face loosens, for a moment, as it does over good meat.{/n}
"Birch, mostly, and black pine higher up. In autumn the stags come down to the river to drink, and the mist lies so thick in the hollows that you can walk through a herd of them and they do not know you are there until you have your hand on one." {n}She looks down at her own hand on the parapet.{/n}
"There is a clearing where the priests made their fire. The grass never grew back where it burned. I go there when I am home. I sit in the black circle and eat whatever I have brought, and I am sixteen again, and hungry, and nobody has come yet with dogs."''',
       c("[Put your hand over hers on the stone.]", "woods2"),
       c("[Say nothing. Look south with her.]", "woods2")),
    el("woods2", '''"You would hate it," {n}she says, without moving her hand.{/n} "It is cold, and damp, and there are wolves, and nobody in the village would sell you bread because of your face. You would sweat all the way up the hill and complain of your knees."
{n}A pause.{/n} "I have never taken anyone there. The Way does not know it exists. I do not know why I have told a Mendevian crusader." {n}She takes her hand back, and folds it into her sleeve.{/n} "It must be the altitude. Go to bed."''',
       c("[Go to bed.]", flags=(USTALAV_WOODS,))),
    el("promise", '''"One day." {n}She turns her head and looks at you, the pale eyes very steady.{/n} "You will see it one day, Commander, whether you want to or not. You will go down that road in my hearse with the curtains drawn, and you will be the best-kept thing that has ever crossed the border."
"But that is not what you meant." {n}Her mouth twitches.{/n} "You meant alive. Walking. Sweating up the hill with your sword on your back, and being refused bread in the villages." {n}She looks back south.{/n} "Very well. If you ever do, I will show you where the stags drink. I will not wait for it."''',
       c("[Look south with her until the watch changes.]", flags=(USTALAV_PROMISED,))),
    el("refuse", '''"Good." {n}She sounds pleased.{/n} "Most crusaders pretend. They say they would love to see my country, and they mean they would love to burn it. You at least say what you mean, when it suits you."
"You will see it anyway, of course. The body always goes home with the collector." {n}She pulls her robe closer.{/n} "Stay up here as long as you like. I am going in. Your walls are cold, and I have no desire to die of anything so stupid as a chill."''',
       c("[Stay on the wall alone.]", flags=(USTALAV_REFUSED,))),
], requires=(BIER,), forbids=(USTALAV_PROMISED, USTALAV_REFUSED, USTALAV_WOODS), delay=84, last=5)


# --- 20. The collector at night (T, optional): she watches the goods at rest. --------------------------------------------

NIGHT_WOKE = E + "night.woke"
NIGHT_FEIGNED = E + "night.feigned"

visit(E + "beat.night", "The collector at night", [
    nar("start", '''{n}You wake in the dark without knowing why, and lie still, and after a while you understand. Somebody is sitting in the chair by your bed. You can hear the faint dry rustle of cloth as she breathes, slowly, and smell cloves, and cold stone, and the lime of the dead-house on her hem.{/n}
{n}She has not moved since you woke. She is watching you sleep, as she might sit by a sickbed, or a coffin before the lid goes on.{/n}''',
        c("[Keep your eyes shut and your breathing slow.]", "feign"),
        c("[Open your eyes.]", "woke")),
    nar("feign", '''{n}You keep your eyes shut. You breathe the way sleepers breathe, as well as you can, and listen.{/n}
{n}For a long time nothing happens. Then there is the faintest touch at your temple, one cold fingertip laid on the vein there, and resting, and counting. It stays for a hundred beats. When it lifts, you hear her let out a breath, very quietly, as if she had been holding it the whole time.{/n}
"Still warm," {n}she says, to nobody, in the Way's whisper, so low you are not certain you heard.{/n} "Still mine. Still unpaid."''',
        c("Continue", "feign2")),
    nar("feign2", '''{n}Then the chair creaks, and the door, and she is gone, and you lie awake until the morning bell with the cold place on your temple slowly going warm.{/n}
{n}In the morning there is nothing to show she was there at all, except a single white flower on the pillow beside your head, the kind she presses into her seals, and your sentry's sworn word that nobody passed him in the night.{/n}''',
        c("Continue", flags=(NIGHT_FEIGNED,))),
    el("woke", '''{n}She does not start, or apologize, or move. In the little light from the window her face is perfectly composed.{/n}
"You sleep badly," {n}she says.{/n} "You talk. You grind your teeth. Twice you reached for a sword that was not there. I have been sitting here since the second bell, and I have learned more about you than in all our suppers."
"I came to see the goods at rest. One likes to know how they will look." {n}Her head tilts.{/n} "You will look better. The dead do not grind their teeth."''',
       c('"Come here, then, and look closer."', "woke2"),
       c('"Get out of my room, Elyanka."', "woke_out")),
    el("woke2", '''{n}She considers it. Then she rises and comes and sits on the edge of your bed, fully dressed, and lays her cold hand flat on your chest over the heart, and leaves it there.{/n}
"No," {n}she says.{/n} "Not tonight. Tonight I only want to count." {n}And she does, silently, her lips moving, while your heart goes too fast under her palm and she watches it with the bird-bright attention of a moneylender over an abacus, until you fall asleep again in spite of yourself.{/n}
{n}In the morning she is gone, and there is a white flower on the pillow.{/n}''',
       c("Continue", flags=(NIGHT_WOKE,))),
    el("woke_out", '''"As you like." {n}She rises without hurry, and smooths her robe.{/n} "It is your room. For now." {n}At the door she pauses.{/n} "You reached for your sword twice, and both times your hand came to the place where I was sitting. I do not think you meant to kill me. I think you meant to make sure I was still there. Good night, Commander."''',
       c("Continue", flags=(NIGHT_WOKE,))),
], requires=(BIER,), forbids=(NIGHT_WOKE, NIGHT_FEIGNED), delay=84, last=5)


# --- 21. The paladin's questions (T, optional): Seelah asked the Commander to help find the Iz dead. --------------------

INQUIRY_TRUTH = E + "inquiry.told_seelah"
INQUIRY_MISLED = E + "inquiry.misled"
INQUIRY_HERS = E + "inquiry.hers"

visit(E + "beat.inquiry", "The paladin's questions", [
    nar("start", '''{n}Elyanka is waiting for you at the dead-house door, which she never does. Inside, the long room is swept and empty, and on the clean floor where the sixty-one lay someone has chalked, very neatly, sixty-one small crosses.{/n}''',
        c("Continue", "her")),
    el("her", '''"Your paladin," {n}she says.{/n} "She came this morning with a lamp and a piece of chalk and did that. Then she went to every carter on the south road and asked who drove at midnight. Two of them remember my men. One of them remembers my hearse." {n}She looks at the crosses, not at you.{/n}
"She will be at the gate of this yard by tomorrow, with her questions and her sword. She told you she would find out, and she asked for your help. Well, Commander. Whose help will she get?"''',
       c('[Tell Seelah the truth yourself] "Mine. She\'ll hear it from me, not from a carter."', "truth"),
       c('[Throw her off] "Grave-robbers from the lower town. I\'ll give her some to hang."', "mislead", alignment=("Evil", 1)),
       c('[Leave it to Elyanka] "She\'s asking about your carts. Answer her yourself."', "hers")),
    el("truth", '''{n}She looks at you for some time, and her face does not move at all.{/n}
"You will tell a paladin of the Inheritor that you gave sixty-one of her crusade's dead to a priestess of Urgathoa, for nothing, on a whim, to see what I would do." {n}A dry breath.{/n} "She will never look at you the same way again. Neither will I."
"Go and do it, then. I will stay out of her road. I have no wish to be struck by a woman praying." {n}At the door she adds, without turning round:{/n} "It was very stupid, and very honest. I do not know which I dislike more."''',
       c("[Go and find Seelah.]", "confess")),
    nar("mislead", '''{n}At your order, the watch drags two resurrection men out of the lower town, men who have sold bodies to a hedge-necromancer in Kenabres. The captain needs a confession about Elyanka's carts. He gets one with a locked cellar and a mailed fist. One of the prisoners confesses to things he did and to several he did not.{/n}
{n}Before the hangman can put the rope around his neck, Seelah climbs the gallows steps and thrusts the two carters' testimony at the captain.{/n} "Stop. He did not take those bodies. Read it."
{n}She pulls the prisoner behind her. The captain calls up the guards and orders them to take her down: the sentence bears the Commander's seal. They crowd the narrow steps, shields pressed against her, until she must retreat or draw on crusaders. She comes down with the testimony crushed in her fist. The prisoner hangs at the south gate with a placard on his chest.{/n}''',
        c("Continue", "mislead_witness")),
    el("mislead2", '''"You hanged a man for my carts." {n}Elyanka does not sound shocked. Her pale eyes settle on you with fresh interest.{/n}
"A thief, and a liar, and he would have died of something stupid in a year anyway. My Lady will have him, since your paladin's goddess will not." {n}She almost smiles.{/n} "Your paladin did not believe you, Commander. She has the carters. What she does not have is an order to bring my carts back over the border. Remember that she will go on not believing you, every day, for as long as you know each other."''',
       c("[Let it lie.]", flags=(INQUIRY_MISLED,))),
    el("hers", '''"Mine." {n}Something like approval.{/n} "Yes. It was my cart."
{n}The next morning Seelah is at the gate of the yard with her lamp and her sword. Elyanka receives her standing by the hearse, and tells her, in plain words, that the sixty-one went to Ustalav, and that they will never be buried, and that the Knight Commander allowed it. She does not lie once.{/n}
{n}Seelah does not draw. She plants her lamp on the step of the hearse and faces Elyanka. Behind the priestess, the six men in grey have not moved.{/n}''',
        c("Continue", "hers_answer")),
    el("hers2", '''"She did not strike me," {n}Elyanka says, that evening, sounding almost disappointed.{/n} "She has put a witness at my door. I told him to count carefully. Your paladin is welcome to guard what you have not given me." {n}She pours wine.{/n}
"She knows now, Commander. She knows it was your word that let my carts through the gate. What she does with that is between the two of you. I have never been so glad to be a stranger in a city."''',
       c("Continue", flags=(INQUIRY_HERS, "trickster.secret.elyanka_siege_dead.known.seelah"))),
    n("confess", "Seelah", '''{n}You find Seelah at the chapel steps with the two carters waiting beside her. She dismisses them when she sees your face, but keeps their folded testimony in her hand.{/n}
"Well? Did you find them?"''',
        c('"I gave the sixty-one to Elyanka. I ordered the gate opened for her carts."', "confession_answer")),
    n("confession_answer", "Seelah", '''{n}Her fist closes over the paper. She takes a breath before she speaks.{/n}
"You gave them away. Our dead. The people we brought back from Iz so they would not be left to demons." {n}She looks toward the south gate.{/n} "Sixty-one. I am taking that count to the chaplains, and the names when we find them. A witness stays at the dead-house from now on. No more carts leave it uncounted."
"I asked you to help me find them. You could have told me then." {n}She steps past you toward the chapel.{/n} "Tell her to keep out of my road. I have work to do for people who cannot ask for it."''',
        c("[Let her take the testimony inside.]", flags=(INQUIRY_TRUTH, "trickster.secret.elyanka_siege_dead.known.seelah"))),
    n("mislead_witness", "Seelah", '''"These men saw her carts. Your prisoner did not drive them."
{n}The captain refuses to reopen the Commander's gate order. The carts are already across the border. Seelah folds the testimony, slowly.{/n}
"You dragged me off those steps to hang a man for another woman's crime. The chaplains will have his name and your order, along with this testimony. And a witness will be at the dead-house when the next bodies arrive. You will not get another confession out of that cellar while I am here."''',
        c("Continue", "mislead2")),
    n("hers_answer", "Seelah", '''"Did they suffer?" {n}Elyanka opens her mouth, but the paladin holds up a hand.{/n} "And do not tell me their families cannot. Sixty-one. I counted them. The chaplains will have that count, and the names when we find them. There will be a witness here when the next dead arrive."
{n}She looks at you.{/n} "You let those carts through. I will remember that too."''',
        c("Continue", "hers2")),
], requires=(GAVE_DEAD, E + "react.seelah_rows", BIER, "seelah.in_party"),
    forbids=(INQUIRY_TRUTH, INQUIRY_MISLED, INQUIRY_HERS, "seelah_dead", "seelah_gone"), delay=48, last=5)


# --- 7. Reaction: Regill, who reads law (the writ). ------------------------------------------------------------------------

SCENES.append(reaction("Regill", E + "react.regill_writ", ("trickster.ever", "regill.in_party"),
    '''{n}Regill is cleaning his blade, with the thoroughness of a man who expects to need it.{/n}
"The priestess of Urgathoa in the dead-house. I read the register the chaplains' clerk carried, Commander. Her oath is valid. So are the oaths of six men in grey who do not breathe. You were right to hold to it: her oath gives her residence. It also gives us obligations to enforce."
"But understand what you have in that yard. Six sworn soldiers of this crusade who answer to her and not to any officer of ours. If she gives them an order you do not like, they will obey her, but their oath binds them to crusade discipline. Have your officers enforce it." {n}He sheathes the blade.{/n} "I have put two of my own on the south gate. Not to watch her. To watch them."''',
    answer_list=REGILL_HUB, chapter=5, last=5, entry='"About the Ustalavic priestess."', portrait="Regill",
    forbids=("regill.dead", "regill.kicked_out", "regill.plot_absent"),
    RequiresAnyGroups=[[WRIT_UPHELD, WRIT_HERS]]))
tag(E + "react.regill_writ", "T")

SCENES.append(reaction("Regill", E + "react.regill_lie", ("trickster.ever", "regill.in_party", WRIT_LIED),
    '''{n}Regill is cleaning his blade, with the thoroughness of a man who expects to need it.{/n}
"You told the chaplains that the priestess in the dead-house is your embalmer, Commander. The register says otherwise: a noblewoman of Ustalav under the crusader's oath, with six sworn men in grey who do not breathe. Her oath would have held without your lie."
"Now nobody knows who commands those six. The chaplains think you do. In practice they obey her. The register records their oaths, not an independent command. When they are ordered to do something ugly, and they will be, every sergeant in this city will look to you for the order you never gave." {n}He sheathes the blade.{/n} "Put them under an officer of ours, or tell the chaplains the truth. A lie about the chain of command gets soldiers killed."''',
    answer_list=REGILL_HUB, chapter=5, last=5, entry='"About the Ustalavic priestess."', portrait="Regill",
    forbids=("regill.dead", "regill.kicked_out", "regill.plot_absent")))
tag(E + "react.regill_lie", "T")

# NM1 item 10 (ideal-run C13): a returned Seelah coexists; her death/departure forbids lift on her return.
for _s in SCENES:
    if _s.get("Id") == E + "beat.inquiry":
        _s.setdefault("ForbidOverrides", {}).update({"seelah_dead": "seelah.trickster.returned", "seelah_gone": "seelah.trickster.returned"})


# struct-slot-hosts: optional reserved continuation; retain every legacy exit.
from copy import deepcopy as _slot_deepcopy
from story_format import n as _slot_node

for _slot_scene_id, _slot_host_id in (
    ('elyanka.trickster.beat.table', 'door2'),
    ('elyanka.trickster.ch6.collateral', 'rift2'),
):
    _slot_id = _slot_scene_id + ".explicit.1"
    _slot_text = "[PROSE PENDING: " + _slot_id + "]"
    _slot_scene = next(s for s in SCENES if s["Id"] == _slot_scene_id)
    _slot_host = next(n for n in _slot_scene["Nodes"] if n["Id"] == _slot_host_id)
    _slot_entry = _slot_deepcopy(_slot_host["Choices"][0])
    _slot_entry.pop("Id", None)
    _slot_entry["Text"] = "Continue"
    _slot_entry["Next"] = _slot_id
    _slot_host["Choices"].append(_slot_entry)
    _slot_scene["Nodes"].append(_slot_node(_slot_id, "Narrator", _slot_text, c("Continue")))


# struct2-01 / ELY-A4-02: dispatch and earned return are different deliveries.
# Legacy answer positions and Next targets remain; only appended answers dispatch.
import copy as _structure_copy

COURIER_AWAY = E + "courier.away"
COURIER_RETURNED = E + "courier.returned"
_courier = next(s for s in SCENES if s["Id"] == E + "beat.courier")
_courier["Nodes"][0]["EnterSet"] = [COURIER_AWAY]
_courier["Forbids"].extend([COURIER_AWAY, COURIER_RETURNED])
_message = next(page for page in _courier["Nodes"] if page["Id"] == "message2")
_return_nodes = [nar("start", "[PROSE PENDING: courier return delivery selection]")]
_return_nodes[0]["Choices"] = []
for _index, (_branch, _answer_flag) in enumerate((
    ("hungry", COURIER_HUNGRY), ("ripening", COURIER_RIPENING), ("silent", COURIER_SILENT),
)):
    _old = _message["Choices"][_index]
    _dispatch = _structure_copy.deepcopy(_old)
    _dispatch["Next"] = "dispatch." + _branch
    _old["Requires"].append(COURIER_RETURNED)
    _message["Choices"].append(_dispatch)
    _courier["Nodes"].append(nar(
        "dispatch." + _branch, "[PROSE PENDING: courier dispatch " + _branch + "]",
        c("Continue", flags=(_answer_flag,))))
    _return_nodes[0]["Choices"].append(c("Continue", _branch, requires=(_answer_flag,)))
    _return_nodes.append(nar(
        _branch, "[PROSE PENDING: courier earned return " + _branch + "]",
        c("Continue", flags=(COURIER_RETURNED,))))
SCENES.append(scene(
    E + "beat.courier_return", _courier["Title"], "Elyanka", 5, "", _return_nodes,
    requires=("trickster.ever", COURIER_AWAY), forbids=(CLOSED, COURIER_RETURNED,
        E + "left_free", "elyanka.returned_actor_lost"), delay=96, last=6,
    optional=True, Relationship=REL, Remote=True, Kind="letter", Chapters=[5, 6],
    RequiresAnyGroups=[[COURIER_HUNGRY, COURIER_RIPENING, COURIER_SILENT]]))
tag(E + "beat.courier_return", "T")
# All groups are ANDed; the master's single OR group keeps the courier optional
# while counting any held answer in Story.cs's latest-required-flag delay anchor.
