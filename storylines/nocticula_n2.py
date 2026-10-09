"""N2 prose for the N1 placeholder nodes of the harbor scenes (Claude, voice-locked).

Text only. Codex owns ids, gates, flags and choice indices (nocticula_n1.py);
this module fills the placeholder text of nodes N1 created and re-texts the
choices N1 appended. It refuses to overwrite anything that is not a placeholder
or an N1 choice it expects, so a structural change surfaces as an error here.
"""

PENDING = "[N2 PROSE PENDING: "

PROSE = {
    # noct.unlit_quay
    ("unlit_quay", "stitch"): '''{n}You take the hem between finger and thumb and tilt it to the lamplight. The flower is not embroidered onto the cloth. It is woven through it, warp and weft, by a hand that worked in a fashion nobody on this quay has used in a very long time. The thread has gone brittle at the edges. The sailcloth around it is newer than the flower, cut down and re-hemmed around it like an old jewel reset in cheap brass.{/n}
"It's real," {n}you say.{/n} "He didn't forge your flower. Someone cut it off something older of yours."
{n}Nocticula's foot stops swinging. For a moment the quay is very quiet; even Orren holds his breath, as though silence might be cheaper.{/n}
"Yes," {n}she says.{/n} "An old permission. A ship I let pass, a long time ago, for reasons that amused me then." {n}She takes the cloth back and smooths it over her knee, slowly, the way she might stroke a cat she intends to drown.{/n} "Someone has been cutting my old favors into new doors. How very rude. And how very clever of you to see it before I said it. I'll remember you saw it. I'll make you say it again, somewhere with an audience."''',
    ("unlit_quay", "demon"): '''{n}Nocticula claps, soundlessly, her palms stopping a finger's width apart. Her eyes have gone bright with genuine delight.{/n}
"Oh, listen to you. Such admirable thirst." {n}She leans down from the bollard until her face is level with yours, close enough that you can smell the harbor on her and, under it, something like burnt honey.{/n} "But you're in my city, darling, on my quay, and the right to kill anything that dies here is mine. Only mine. You may hold the bowl. You may not hold the knife."
{n}Orren, who has understood perhaps half of this, begins to pray to a god who has never set foot in Alushinyrra.{/n}
"Later, if you're very good, I'll let you choose where Rhez starts." {n}She straightens, and pats your cheek, twice, the way one rewards a dog that has growled at the right stranger.{/n} "Don't sulk. Wanting the knife is the most charming thing you've done all night."''',

    # noct.sixth_passenger
    ("sixth_passenger", "read_lie"): '''{n}You stop listening to what he says and watch what his body does while he says it. When Rhez's knife comes near, his eyes go to the door, as though someone might come through it to save him. When Nocticula kisses him, they go to the floor. And when he lies about the lamps, every time, his tongue finds the corner of his mouth and stays there, like a man tasting a name he has been told not to say.{/n}
"Who taught you to sell it?" {n}you ask him quietly, while he is still shaking from a kiss.{/n} "Not the captain. The captain can't spell his own ship."
"Nobody, I swear, nobody—a woman. Only a woman, on the quay. White shoes." {n}He hears himself.{/n} "She never came aboard. She said the mud was beneath her."
"Her name."
"Ilvara," {n}he says, and then, horrified,{/n} "I didn't—I never said—"
"And the captain's books? Who keeps them?"
"Dessa. His girl. His slave. She writes everything down, everything, I swear on my eyes—"
{n}Nocticula rewards him with a long kiss on the mouth, and over his head her eyes find yours. She looks hungry.{/n}
"Oh, you're good at this. I'm going to have to keep you."''',
    ("sixth_passenger", "missed_lie"): '''{n}You watch him and learn nothing. He is a sailor and a thief, and he has been lying for his life since before you came down the stairs; he has had practice. When you put your question he gives you a name that Rhez says, flatly, belongs to a fishmonger who drowned last spring. When you put it again he gives you a different one, with tears in his eyes, and it is no better.{/n}
"Oh dear." {n}Nocticula sounds delighted.{/n} "He's held out on you. That's very bad manners, Orren. The Commander came all this way."
"Toe," {n}says Rhez.{/n}
"Toe," {n}Nocticula agrees.{/n}
{n}Rhez kneels, unlaces his left boot, and takes the smallest toe off his foot with one short movement, the way a cook takes the end off a carrot. His scream goes up into the stone vault and stays there a while. Nocticula catches the toe when Rhez tosses it up, examines it, and drops it into the pocket of his red coat.{/n}
"So you'll have something to remember the Commander by." {n}She pats the pocket.{/n} "You can't read everyone, darling. That's why I keep Rhez."''',
    ("sixth_passenger", "sentence"): '''"Good. I'll hold you to it. I hold everyone to everything." {n}She turns back to the chair and regards Orren the way she regarded the flower on the quay: a pretty thing, cut from something of hers.{/n} "Now. What do we do with him while we look? He's still useful. He knows the captain's face, the captain's ship, the captain's habits. He knows the woman on the quay. He even knows which lamps he lied about, though he's stopped being sure."
{n}Orren lifts his head. Whatever came loose in him has settled into a terrible, attentive calm.{/n}
"I'll do anything," {n}he says.{/n}
"Everyone says that in that chair. It's the chair talking." {n}She looks at you.{/n} "I can keep him down here and squeeze him until there's nothing left but rind. I have a cell that's been lonely, and the captain will never know we have him. Or I can send him home with my flower pinned through his ear and watch who comes to take it off him. The captain will know at once, and so will whoever the captain answers to, and they'll run, and running people are so much easier to see." {n}Her eyes glitter.{/n} "Or you could think of something worse. You have a crooked little gift for lies, I'm told. I'd love to watch you use it on someone who deserves it."''',

    # noct.captains_reply
    ("captains_reply", "sold"): '''"Oh, the block." {n}Nocticula's whole face lights.{/n} "I want to know what a liar fetches by the pound."
{n}The captain comes down the companionway singing and finds three strangers and his slave waiting for him, and he has time to say one word, which is "who", before Rhez puts him on the floor. She does it without malice, the way she might sit on a dog. Nocticula steps over him to take the ship's keys from his belt and the purse from the other side of it, and drops both into Dessa's hands.{/n}
"There. Your keys. Your ship, after a fashion: my ship, and you'll keep it for me. My quay-woman. You'll still wear the collar, darling, because I don't give things away. But you'll wear it at the wheel."
"Yes, Lady." {n}Dessa's fingers have closed round the keys so hard her knuckles are white.{/n}
{n}They take him up at dawn, when the Fleshmarket opens. You stand at Nocticula's side on the auctioneer's platform and watch: the captain stripped to the skin on the block, his rings in a dish beside him; the buyers in their silks and chains; the auctioneer calling weight, teeth, temper. Nocticula has taken the auctioneer's chair and sits in it with her chin on her hand.{/n}
"Price him honestly," {n}she tells the auctioneer.{/n} "It'll be a novelty for him."
{n}He goes for less than his ship's anchor would have fetched. A tanner buys him for the pits, where men last a year. Dessa watches from the quay with his book under her arm, and does not cross anything out.{/n}''',
    ("captains_reply", "waking"): '''{n}You wake in Drezen with the smell of tar in your nose and a laugh still in your chest that is not yours. It goes on for a moment after your eyes open. Then the room is only your room again, and cold.{/n}''',
    ("captains_reply", "waking.lann"): '''{n}Lann is outside your door with two mugs, one of them already half drunk.{/n} "Morning, Commander. So. You were laughing in your sleep. Really laughing. Not your laugh, either." {n}He hands you the fuller mug.{/n} "I'm going to decide it was a good dream and not ask. That's me being supportive."''',
    ("captains_reply", "waking.woljif"): '''"Boss. Boss, you were laughing in your sleep. Not your laugh, either, some big fancy lady laugh. Like somebody owed you money and just paid you in teeth." {n}Woljif squints at you from the doorway.{/n} "I'm gonna go sleep in the stables a couple nights. Not because of you. The stables are nice."''',
    ("captains_reply", "waking.greybor"): '''{n}Greybor is sharpening something at the foot of the stairs. He does not look up.{/n} "You talk in your sleep. Prices, mostly. A ship. Somebody begging." {n}The whetstone goes on.{/n} "Don't care whose. If there's coin in it, though, I'd like to hear about the coin."''',

    # noct.her_own_face
    ("her_own_face", "mark"): '''{n}She does not ask. She rolls on top of you again, slow this time, deliberate, and puts her mouth to the side of your throat, and you feel her teeth.
It is not a bite to draw blood, though it draws a little. It is a bite to write with. Heat goes out from it under the skin, down your neck and across your collarbone, a slow crimson spreading like wine through water. When she lifts her head you can see it in the lamplight: a mark the color of a fresh wound, shaped like nothing you have a name for.
Behind her, her wings have opened. You had not seen them. Across the dark inner skin of each one, glowing faintly, there are runes in Abyssal that were not there before, and you can read them, though you never learned the script. They are your name.{/n}
"Hold still. I'm writing my name where you can't wash it off." {n}She touches the mark with one fingertip, and it burns, pleasantly, like a coal under a blanket.{/n} "There. Everyone in my city who can read knows whose you are. Shamira reads very well."
{n}Next door, the harp has stopped entirely.{/n}
"It won't wash off and it won't fade. Where it shows is up to you; I'm feeling generous. Wear it bare and let them stare. Or hide it, if you like. I didn't put it there for them."''',
    ("her_own_face", "waking"): '''{n}Morning in Drezen: grey light, a cold room, someone in the yard shouting about horses. Your body has slept a whole night. It does not feel as if it has rested. For a while you lie still and listen for a harp through the wall, and there is none.{/n}''',
    ("her_own_face", "waking.daeran"): '''{n}Daeran catches you on the stairs, glances at your throat, and stops with one hand pressed theatrically to his heart.{/n} "Someone has signed you, darling. In red. In a hand that is decidedly not of this plane." {n}He leans in to look closer, delighted.{/n} "I'm wounded I wasn't asked to witness. Next time, do send a card."''',
    ("her_own_face", "waking.wenduag"): '''{n}Wenduag's eyes go to your throat and stay there.{/n} "That is a claim mark." {n}Her voice is flat.{/n} "Below, the strong marked what was theirs, so the others knew not to touch it. Something strong has marked you, Commander." {n}A pause.{/n} "I would like to know what. So I know whom to watch."''',
    ("her_own_face", "waking.seelah"): '''{n}Seelah stops you in the corridor and tugs your collar aside without asking, the way she would check a comrade for a wound.{/n} "That's no bruise." {n}Her mouth goes tight.{/n} "Where I grew up, people put marks on people so the whole street knew who owned them." {n}She lets the collar fall.{/n} "Whoever she is, you watch yourself. Please."''',
    ("her_own_face", "waking.woljif"): '''"Whoa. Boss. Your neck." {n}Woljif takes a large step backward.{/n} "That's a demon mark. That's a fancy demon mark. I heard about guys with those. You know what happens to guys with those? Everybody's real polite to them. Real, real polite. Right up until." {n}He does not finish.{/n} "I'm just gonna be polite."''',

    # noct.demonstration
    ("demonstration", "court"): '''{n}The hall is roaring now. A succubus has climbed onto a courtier's shoulders for a better view. The bookmaker wipes his slate and chalks new odds as fast as his hand will go: on Ilvara's hands, on Ilvara's tongue, on Ilvara's lifespan, which has shortened considerably in the last minute.
Nocticula sits back on her throne. Without turning her head she puts her hand on your knee, and leaves it there, where everyone can see it.{/n}
"Say something clever, darling. They're watching you now." {n}Her fingers tighten.{/n} "If you're dull, they'll decide I've been sleeping with something dull, and I'll have to have you flayed for my reputation's sake. I'd hate that. Mostly."
{n}Somewhere on the steps a courtier shouts, "Ten says the crusader stammers! Ten!" and someone takes the bet, and someone else raises it.{/n}
{n}Below the dais Ilvara has straightened. Whatever has been done to her tonight, she is a performer, and she is still performing: chin up, face composed, white shoes together on the black floor. She is waiting for you to fail.{/n}''',
    ("demonstration", "exposed"): '''{n}You stand. The hall quiets by degrees, because the Lady's hand has left your knee.
You tell them where her door came from: a scrap of the Lady's own old protection, cut from a ship she once let pass. And you tell them what it is made of. The lamps are not souls, and not quite prisoners. They are arrivals, journeys begun and never allowed to finish, held open by the travelers caught inside them. The harbor is built out of them. Every passenger who crossed and was not let out is a beam in its roof. Ilvara found an old door, opened it with a stolen permission, and has been building with people ever since, and selling them the right to leave.{/n}
"She isn't a magician," {n}you finish.{/n} "She's a slaver who never had to buy chains."
{n}The court howls, the way a crowd howls at an execution when the first cut is a good one. Ilvara's composure breaks all at once: her mouth works, her eyes go to the doors, and a demon with a jeweled snout leans down from the steps and spits on her white shoes.{/n}
"Did you hear that?" {n}Nocticula's voice rides over the noise.{/n} "My crusader reads your little trick better than you perform it."''',
    ("demonstration", "laughed"): '''{n}You stand and begin to explain, and somewhere in the second sentence you lose the shape of it. The lamps are arrivals, or debts, or both; the half-coins are tokens, or keys; you correct yourself once and then again. Ilvara lets you go on. She even inclines her head politely, as one does for a child reciting.
Then someone at the back of the hall laughs, and then all of them do.
You sit down in it. It is very loud. Nocticula has not taken her hand from your knee. She is laughing too, quite openly, her head thrown back, and when she has finished she pats your knee twice.{/n}
"Even my pets have off nights." {n}She turns to the hall, and the laughter dies as if cut with a knife.{/n} "That's enough. I may laugh at the Commander. You may not."''',

    # noct.return_count
    ("return_count", "orren"): '''{n}Orren goes in on a rope, with Rhez holding the other end. The half-coins hang in a bag round his neck, because he cannot be trusted to hold a bag; his hands shake too badly for that, and the coins keep slipping from his fingers on the wet rock, and he has to pick them up with his teeth.
Through the door you can see the dry harbor: sand, posts, five lamps burning with nobody to tend them.
At the first lamp he speaks a name. His voice cracks on it. He breaks the half-coin against its mate, with his teeth when his fingers fail, and a woman steps out of the flame: big, scar-armed, a brass bell clenched in her fist. Vessa. The first thing she sees, after however long she has been inside that light, is Orren's face a foot from hers.
She knows him. You watch her know him.
She hits him with the bell. Not hard; she has no strength yet. He goes down on the sand and stays there until Rhez jerks the rope.{/n}
"Walk," {n}Rhez calls to her.{/n}
{n}Vessa walks out past him. At every lamp after that it is the same: each passenger he sold steps out of the flame and sees him first, on his knees in his red coat with a coin between his teeth, and each of them knows him.{/n}
"I promised you a spectacle," {n}Nocticula murmurs, leaning down to you.{/n} "Isn't this better than hanging?"''',
    ("return_count", "carrier"): '''"Someone has to carry the coins in." {n}Nocticula looks down at the two figures waiting under guard on the rocks below her: Ilvara in grey, her white shoes already greying with salt, and Orren Vale in his ruined red coat, shaking.{/n} "The one who built it, or the one who sold it. Either will do. Neither wants to. That's what makes it fun." {n}The surf booms against the cliff.{/n} "Choose, darling. The tide won't wait for you, and neither will I."''',
    ("return_count", "assign"): '''{n}The returned stand together on the wet rock in the lantern light from the boats: Vessa with her bell, Ren and Tomar, two others whose names Rhez reads off the slips, a cooper and a girl who cannot be more than sixteen. If Halren is not already in her cells, he is here too, with his boot. They are soaked and shaking and blinking at the lanterns, and the boats cheer them the way a crowd cheers horses that have finished the course.
None of them says thank you. None of them knows whom to say it to. They look up at the Lady on the rock, and one after another they understand what they are now.{/n}
"Mine," {n}Nocticula agrees, to their faces.{/n} "Every one. You crossed under my flower; you came out on my rock. I'm told some of you have families." {n}She sounds interested, as one is interested in the pedigree of a dog.{/n} "Now, darling. Where do I put them? The Fleshmarket will pay well for slaves with a story like that; buyers adore a story. My Harem would take them, and Shamira would have to be grateful, and she does so hate being grateful. Or the street." {n}She smiles.{/n} "The street is the funniest. Let them go, in my city, with my flower taken off them. I'll bet you a night none of them lasts the week."
"And if I sell them?"
"Then you'll have your share. Gold doesn't remember where it's been." {n}She tilts her head.{/n} "Don't look at me like that. You wanted them found. Here they are. Found."''',
    ("return_count", "orren_end"): '''{n}Rhez has the returned taken down to the boats, to wherever you have sent them. The courtiers lean over the gunwales to touch them as they pass, for luck. Nocticula has already lost interest in them. She is looking at Orren.
He kneels on the rock where the guards dropped him, his red coat black with seawater, his ruined hands held against his chest. Somewhere in the last hour he has stopped begging. He watches the boats take away the people he sold, and his face has the stillness of a man who has finally found the bottom of something.{/n}
"And now the thief." {n}She steps down from her rock and crouches in front of him, her gown pooling on the wet stone.{/n} "Orren. Darling. You were so useful. You sang so prettily in that chair." {n}She strokes the wet hair back from his forehead.{/n} "Getting caught is not an option in the Abyss. You got caught. Let's finish."
{n}She looks up at you.{/n}
"The rock wants a lamp; the old ones always do. We could make one of him and set him in the cliff, and he'd burn there in the dark as long as it stands. Orren always wanted to be useful. Or give him to them." {n}She nods toward the boats, where Vessa is standing in a stern, watching, the bell still in her fist.{/n} "They'd like that. They'd do it here on the rock, and my court would bet on how long. Or, if he's earned it, let him run. Put him in our wager. Rhez can count to a hundred, and we'll see how far a thief gets in my city with everyone watching."''',

    # noct.another_place
    ("another_place", "noct.another_place.explicit.1"): '''{n}Nocticula looks at Laulieh, at the blood she has kept on her cheek for effect, and smiles.{/n} "Come here, Laulieh. You've earned it, and the Commander has never seen you earn anything properly."
{n}She crooks a finger at Laulieh, and then at you. The hatbox stays where it is, on the dressing table, for the rest of the night.{/n}''',
    ("another_place", "noct.another_place.aftermath.1"): '''{n}Later, Laulieh is curled at the foot of the couch like a cat in a sunbeam, humming the singer's tune flawlessly, slightly sharp, out of malice. The hatbox has been decided: framed, over the bed. Nocticula lies against your shoulder with her eyes half closed, winding a lock of Laulieh's hair round one finger and pulling it now and then to hear her squeak.{/n}
"Fie, my lady."
"Hush." {n}She turns her head on your shoulder, and her eyes are not drowsy at all.{/n} "Now. Back to Ilvara. She asked your price."''',

    # noct.hearing
    ("hearing", "overruled"): '''"Let her go?" {n}For a moment the hall is so silent you can hear the cauldron bubbling.{/n} "Let her go. That isn't a sentence, darling. That's a shrug." {n}Nocticula sighs, a long, theatrical, disappointed sigh, and every courtier on the steps sighs with her.{/n} "Boring. You were so promising. The cauldron."
{n}The slaves take Ilvara by the elbows. She fights; it does not matter. They lift her and lower her into the boiling filth up to the neck, white shoes and all, and the hall roars, and the bookmaker shrieks the odds he has just won, and Ilvara screams for a long time.
When they lift her out she is still alive. Nocticula has made sure of it.{/n}
"There. Now let her go," {n}she says.{/n} "To the Fleshmarket. Whatever came out of that pot can be sold for whatever someone will pay for it. I've done as you asked, Commander: she's going. I've merely improved the route." {n}She looks at you, and her eyes are bright and hard.{/n} "Next time I ask you for a sentence, give me one." {n}She turns her slate face up. She had written cauldron. She wipes it clean with her thumb, as though the word bored her too.{/n}''',
    ("hearing", "execute"): '''"Execute her." {n}Nocticula repeats it slowly, tasting it. Then she claps, delighted, and the whole hall claps with her.{/n} "Finally. Someone who understands what a court is for."
{n}She comes down from the throne herself. She always does; nobody else in Alushinyrra is permitted to. Two guards hold Ilvara kneeling, and Nocticula takes her face in both hands, almost gently, and looks into it for a long moment, the way she looked at the flower on the quay.{/n}
"You made something clever out of something of mine. I'd have kept you, if you'd asked properly." {n}She kisses Ilvara on the forehead.{/n} "You didn't ask."
{n}She breaks Ilvara's neck. It is quick, and very loud, and the hall erupts. The bookmaker throws his slate in the air. Nocticula lets the body fall, steps over it, and comes back up the steps to you, wiping her hands on her gown.{/n}
"That was worth staying up for." {n}She sits and crosses her legs.{/n} "Have someone hang the shoes on a hook. I want to see them every time I'm bored." {n}She turns her slate face up and shows you. She had written my hands. She looks at it, and at her hands, and laughs.{/n} "I'm never wrong about myself."''',
    ("hearing", "demon_ask"): '''"Give her to you?" {n}Nocticula laughs, and claps her hands in silent applause.{/n} "Your thirst for blood is admirable! But you are here in my realm, where the right to execute demons belongs only to me." {n}She glances down at Ilvara.{/n} "And mortals, and magicians, and anything else that dies in my hall. You want the knife. I adore that. You may not have it." {n}She rises.{/n} "Hold her chin."
{n}You go down to the floor. You take Ilvara's jaw in your hand and tilt her face up toward the throne, and her eyes stay on yours, wide, while Nocticula descends the steps one at a time, in no hurry at all. The hall is utterly silent.
Nocticula kills her with one finger laid against the throat, pressing, the way one presses a stopper into a bottle. It takes a while. You hold the chin the whole time. When it is done she lifts your hand from Ilvara's jaw and kisses the palm.{/n}
"There. You helped. Doesn't that feel better than doing it yourself?" {n}Back on the throne, she turns her slate over: my hands, it says, and under it, smaller, and the crusader holds her. She taps the second line.{/n} "I knew you'd want to touch."''',
    ("hearing", "aeon"): '''"By the law of creation." {n}Nocticula sits up.{/n} "Finally. Cold judgment. I've waited so long to hear an aeon talk like one instead of like an ordinary, insipid mortal." {n}She leans forward, chin on her hand.{/n} "Go on. Say the rest."
{n}You say it. The door was made to shelter arrivals; she unmade it into a cage. What she broke, she will hold. She will be bound to the door she made, not as its prisoner but as a part of it: its hinge, its lock, the thing it turns on. It will not let her go, because she will be what it is.
The hall does not cheer. It is too surprised. Then Nocticula begins, very slowly, to applaud.{/n}
"Oh, that's the harsh adherence I wanted. Not mercy. Not cruelty. Just the shape of the thing, closing." {n}She looks down at Ilvara, who has gone grey.{/n} "Collar her to it. Bind her into the rock. She works it until it wears her through, and then she is it." {n}She turns back to you, and her smile is warm and entirely without pity.{/n} "I trust your judgment, dear aeon. Don't let it go soft on me." {n}She turns her slate face up. It is blank.{/n} "I didn't think you had it in you. I so rarely lose. I find I don't mind."''',
    ("hearing", "aeon.native_trials"): '''{n}She leans closer, so that only you can hear.{/n} "Do you remember the last time? My little trials. Three culprits out of all Alushinyrra, and you stood where you're standing now and told me what you thought, and I passed the sentences." {n}Her nails trace the arm of the throne.{/n} "Whatever you gave me then, I remember every word of it. This was better. Something has changed in you, aeon, and I don't think it's me."''',
    ("hearing", "waking"): '''{n}You wake in Drezen with your own voice still in your ears, saying something final. Your throat is raw, as though you had been shouting over a crowd. The room is silent. Somewhere in the keep a bell is ringing for morning prayers, and for a moment, before you are properly awake, it sounds like a hall full of people cheering. You lie still and wait for it to stop. It takes longer than it should.{/n}''',
    ("hearing", "waking.regill"): '''{n}Regill is waiting in your antechamber, at attention, as if he has been there for some time.{/n} "Commander. You pronounced a sentence in your sleep last night. Clearly, and twice." {n}A pause.{/n} "I will not ask on whom. I approve of the clarity. I would only remind you that a sentence passed in one's sleep is binding under no code I recognize. Whatever code you were serving, it was not ours."''',
    ("hearing", "waking.seelah"): '''{n}Seelah sits down across from you at breakfast without asking.{/n} "You were shouting in your sleep. I heard it through the wall." {n}She tears her bread in half.{/n} "Something about a sentence. A door. And a crowd cheering, except I think that was you, too." {n}She does not look up.{/n} "I don't need to know. I just want you to know I heard."''',
    ("hearing", "waking.lann"): '''"Morning, Commander. So, you know how people talk in their sleep? Usually it's like, 'Mother, no, not the pickled eels.'" {n}Lann scratches the back of his neck.{/n} "You said 'sentence.' Very calmly. Like a judge. And then you laughed. I'm going to go ahead and not think about it, if that's all right."''',

    # noct.empty_chair
    ("empty_chair", "entrance"): '''{n}She sweeps the roof off the model with one hand so that you can see down into the rooms: the dining hall, the gallery, and in its chamber the bell, a little brass thing on a hook, no bigger than a fist.{/n}
"How shall we arrive?" {n}She walks two fingers up the model's front steps.{/n} "As guests. Invited ones, masked, through the front door, with Rhez on my arm; she'll have the bell-keeper's baton off him before he's finished bowing. Or—" {n}her fingers jump to the bell chamber{/n} "—as the silence where her bell should be. Someone touches that bell before the evening starts and strikes it dumb, and Istrava rings it in front of all her guests, and nothing happens. That needs a clever hand. Yours, perhaps." {n}She smiles.{/n} "Or, if your mind is crooked enough, as her own invitation come home to her. Addressed to Istrava, from Istrava. She'd open it. They always open their own."
{n}Outside the window the Middle City burns. Somewhere far below, in her cells, someone is screaming, faintly and regularly, like a clock.{/n}''',
    ("empty_chair", "entrance.silence"): '''{n}The Gift lets you reach. For the length of a breath you are in the lodge itself, in the dark bell chamber with dust on the sill, and the bell hangs in front of you on its hook. You find the working inside it, a little knot of old enchantment that makes it ring whatever name its holder wants, and you put your thumb on the knot and press until it gives.
Then you are back at her table, and your thumb aches, and Nocticula is looking at you with her lips parted.{/n}
"Oh," {n}she says.{/n} "Oh, I felt that. She'll ring it in front of all of them and it'll just hang there like a dead mouse." {n}She takes your aching thumb into her mouth, briefly, and bites.{/n} "I'm going to watch her face."''',
    ("empty_chair", "entrance.fracture"): '''{n}The Gift lets you reach. For a breath you are in the dark bell chamber, and the bell hangs in front of you, and you find the knot of old enchantment inside it, and press.
It does not give. It rings.
Once, very loud, a note that goes through the whole lodge and through you; somewhere below, a guest laughs and calls up the stairs to ask who is so eager. You are back at the table with your ears singing. A hairline crack runs down the side of the model bell.{/n}
"Well," {n}Nocticula says, after a moment.{/n} "She'll know someone has touched it. She'll think it was a guest; they're always pawing her things." {n}She shrugs.{/n} "Then we go in as guests, through the front, with Rhez. I like the front door. It's where people see you."''',
}

# Choices appended or created by N1 (nocticula_n1.py): (scene, node, index) -> (N1 text, N2 text).
CHOICES = {
    ("unlit_quay", "start", 2): ("[Look at the stitching on the flower.]", "[Look at the stitching on the flower. Perception, DC 28.]"),
    ("unlit_quay", "start", 3): ("[Demon] Let me open him up.", '[Demon] "Let me open him up."'),
    ("sixth_passenger", "start", 4): ("[Watch him while she works.]", "[Watch him while she works. Perception, DC 30.]"),
    ("sixth_passenger", "sentence", 0): ('"Keep him. Squeeze him until he is dry."', '"Keep him. Squeeze him until he\'s dry."'),
    ("sixth_passenger", "sentence", 1): ('"Send him home wearing your flower."', '"Send him home wearing your flower. See who tries to take it off him."'),
    ("sixth_passenger", "sentence", 2): ('"Let him sell the captain two lies."', '"Let him sell the captain two lies. They can\'t both be true."'),
    ("captains_reply", "dessa", 2): ('"Put him on the block instead."', '"Put him on the block instead. She can keep his book."'),
    ("captains_reply", "sold", 0): ("Continue", "[Let the gavel fall.]"),
    ("demonstration", "court", 0): ("[Tell the court how her trick works.]", "[Tell the court how her trick really works. Knowledge (Arcana), DC 32.]"),
    ("demonstration", "court", 1): ('"That flower is yours."', '"That flower is yours. She cut it from an old permission of yours."'),
    ("demonstration", "court", 2): ("[Say nothing.]", "[Say nothing. Let them watch her.]"),
    ("return_count", "start", 3): ('"Send the thief in."', '"Send the thief in."'),
    ("return_count", "start", 4): ("[Choose the carrier.]", "[Choose who carries the coins in.]"),
    ("return_count", "orren", 0): ("Continue", '"The last lamp."'),
    ("return_count", "strain", 3): ("Burn your flower into the door.", '"Burn your flower into the door."'),
    ("return_count", "strain", 4): ("Hold it narrow.", '"Hold it narrow. Let it take its toll."'),
    ("return_count", "strain", 5): ("One crossing per coin.", '"Count it: one crossing per coin, then shut."'),
    ("return_count", "assign", 0): ('"Sell them."', '"Sell them at the Fleshmarket."'),
    ("return_count", "assign", 3): ('"Let them go, under your protection."', '[Angel] "Let them go, under your protection."'),
    ("return_count", "orren_end", 0): ('"Give the door Orren."', '"Make a lamp of him."'),
    ("return_count", "orren_end", 2): ('"Let him run."', '"Let him run. Put him in your wager."'),
    ("return_count", "orren_end", 3): ('"Let him run."', '"Let him run. Put him in your wager."'),
    ("another_place", "laulieh", 1): ("[Let her be rewarded here.]", "[Let her be rewarded. Here, in front of you.]"),
    ("another_place", "departure", 1): ("[Let her be rewarded here.]", "[Let her be rewarded. Here, in front of you.]"),
    ("another_place", "courier", 1): ("[Let her be rewarded here.]", "[Let her be rewarded. Here, in front of you.]"),
    ("hearing", "start", 4): ('"She broke once in this hall already."', '"She broke once in this hall already. Remind her."'),
    ("hearing", "terms", 3): ('"Let her go."', '"Let her go."'),
    ("hearing", "terms", 4): ('"Execute her."', '"Execute her."'),
    ("hearing", "terms", 5): ('"Give her to me."', '[Demon] "Give her to me."'),
    ("hearing", "terms", 6): ('"Bound to the door she made."', '[Aeon] "By the law of creation: bound to the door she made."'),
    ("empty_chair", "entrance", 0): ('"As guests."', '"As guests. Rhez takes the baton."'),
    ("empty_chair", "entrance", 1): ("[Silence the bell.]", "[Silence the bell before it rings. Use Magic Device, DC 34.]"),
    ("empty_chair", "entrance", 2): ('"Send her an invitation to herself."', '"Send her an invitation addressed to herself."'),
}


def write(scenes):
    """After nocticula_n1.scaffold: fill placeholders and re-text N1 choices."""
    by = {s["Id"].removeprefix("noct."): s for s in scenes}
    for (sid, nid), text in PROSE.items():
        node = next(x for x in by[sid]["Nodes"] if x["Id"] == nid)
        assert node["Text"].startswith("{n}" + PENDING), (sid, nid)
        node["Text"] = text.strip()
    for (sid, nid, index), (before, after) in CHOICES.items():
        node = next(x for x in by[sid]["Nodes"] if x["Id"] == nid)
        choice = node["Choices"][index]
        assert choice["Text"] == before, (sid, nid, index, choice["Text"])
        choice["Text"] = after
