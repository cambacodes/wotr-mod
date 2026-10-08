"""Living, gifted Chapter 5 continuation of the accepted RanRomance dream bargain.

New incidents and named agents are authored fiction. All participants are adults.
Dreams carry the sleeping Commander into her real court (user decision 2026-10-07).
This module does not implement acquisition, resurrection, gift replacement, or a triad.
"""
from copy import deepcopy
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
ETUDES = {
    "noct.parent_active": "18affced672d4c56a52bf6ffc00601b9",
    "noct.parent_initial": "8a28bbd82568486bb757d00a2087a6cf",
    "noct.parent_rejected": "761ca3572c1145ebb755032d613bff46",
    "noct.parent_laulieh": "9591c34df22b4d518a059cf608255458",
    "noct.parent_laulieh_departure": "19e5d6f04b9b4483b2e2979baf8736e4",
    "noct.gift": "0c1695f4a362f0243a4afcfd1957eb0d",
    "noct.dead": "e581f609dc0f44a481e7e88824ac39da",
}
# enGB 43ca3072: Nocticula states the native Aeon trial conditions.
SEEN_CUES = {
    "noct.native_trials_seen": ["a5472a3492d23c542b5f77cb6e591ca3"],
    "noct.parent_agreement_seen": ["631bf0ede36742559cee476f34dcb5de", "cb13766be07b448f8cacb477be32e13c", "5388a7d7a1da48deb333d34abab1a6d0"],
    "noct.parent_ambition_heard": ["b3a4ce99bc30440fa9ebcbfce2776176"],
    "noct.parent_feelings_uncertain": ["1110f2b6304549999fb546e7ecc4c8a1"],
    "noct.socoth_plan_exposed": ["bb552fe4e21cb874fa3c98c2cc328186"],
}
RELATIONSHIP = dict(
    Title="Under her black flower", Description="Someone sold passage under Nocticula's black flower. She wants me watching while she collects.",
    Objective="Sleep, and see what she has caught", Guidance="After accepting RanRomance's Chapter 5 dream relationship, rest in Drezen while Nocticula lives and her Profane Gift remains. While the Gift holds, her dreams carry you into her court; what you decide there happens. These meetings do not recover a missed or rejected relationship.",
    StartedFlag="noct.started", ClosedFlag="noct.closed", CommittedFlag="noct.complete",
    UnavailableFlags=["noct.dead", "inhuman", "legend", "dragon"], FailureFlags=[])
SCENES = []


def f(*names):
    return tuple("noct." + name for name in names)


def s(id, title, nodes, previous=None, delay=12):
    if previous is not None:
        late = id in ("counterseal", "no_applause", "what_she_keeps", "second_door")
        answer = ('"The harbor business is settled. I do not want these private meetings to continue."' if late
                  else '"I\'m done with your harbor. Find another pair of eyes."')
        response = '''{n}She looks away from you. When she speaks, her voice has lost its teasing edge.{/n}
"I invited you because the business was settled. You need not explain the distinction to me."
"Then you understand what I am declining."
"Perfectly. It is an unpleasant advantage of listening."
{n}You wait. She lets the silence grow uncomfortable before she answers.{/n}
"The work stands. So does the answer you have just given. There will be no further invitations to these meetings."
"Our earlier bargain still stands too."
"I did not confuse it with an evening's company. Do me the courtesy of remembering that."
{n}She lifts two fingers. The dream fades around her, and you wake without a new promise.{/n}''' if late else '''{n}She doesn't get up.{/n}
"Then go. I don't keep instruments that blunt themselves."
"And our bargain?"
"Was never about a harbor. I'll collect on it when it suits me. You'll know when." {n}She looks at you a moment longer, the way one looks at a dish sent back from the table.{/n} "I'll find another pair of eyes. They'll be prettier, and they'll do as they're told."
{n}She lifts two fingers. The dream goes out like a snuffed lamp, and your cot in Drezen is suddenly very hard.{/n}'''
        nodes[0]["Choices"].append(c(answer, "withdraw_undertaking"))
        nodes.append(n("withdraw_undertaking", "Nocticula", response,
            c('[Leave this undertaking. The earlier bargain remains unchanged.]', flags=f("closed", "undertaking_withdrawn"))))
    for page in nodes:
        page["Portrait"] = "Nocticula"
    SCENES.append(scene("noct." + id, title, "Memory", 5, title, nodes,
        requires=("noct.parent_active", "noct.parent_agreement_seen", "noct.gift") + (("noct." + previous,) if previous else ()),
        forbids=("noct.dead", "noct.parent_rejected", "noct.closed", "inhuman", "legend", "dragon"),
        delay=delay, optional=True, Relationship="nocticula", Remote=True, Areas=[DREZEN], Chapters=[5]))


s("unlit_quay", "The unlit quay", [
    n("start", "Narrator", '''{n}Sleep does not take you anywhere gentle. It drops you onto wet stone at the bottom of the night, and the stone is real: cold through your boots, slick with harbor weed, stinking of tar and low tide. Above you the Middle City of Alushinyrra climbs the dark in tiers of red lamps. Along the harbor wall the slave pens are quiet at this hour, a row of iron mouths with sleepers in them. The Fleshmarket has shut its stalls. Somewhere up the quay a drunk is singing about a succubus with three husbands, and getting the number of husbands wrong.
A man in a red coat hangs from a mooring ring by his wrists, toes just finding the stones. Nocticula sits on the bollard beside him and swings one foot, and the foot keeps time with his breathing.
Behind him stands a narrow woman in grey with a knife she has not used yet. Across Nocticula's lap lies a length of sailcloth with a black flower worked into its hem.{/n}
"Don't wake up. I went to some trouble to bring you." {n}She does not look round.{/n} "The Gift is good for more than listening to your little thoughts. Tonight it carries the rest of you. Stand there, where he can see you. He's been so lonely."
{n}The man twists on his rope to find you. His face is wet, and so is the front of his coat.{/n}
"Lady—Lady, who is that, is that the buyer? I'll tell them too, I'll tell anyone—"
"Orren Vale," {n}Nocticula says, the way one introduces a dish.{/n} "Thief, sailor, liar of real ability. He sold passage under my flower. In my city. On my quay, a hundred paces from my Fleshmarket. I'd be furious if he weren't so funny."
"It's real," {n}Orren tells you, quickly, because you are new and might be kinder.{/n} "The door's real. The captain runs her straight at a cliff and the rock opens, and there's a harbor inside, dry as a bone, six lamps burning. Then five. I swear it, five the second time. I'll draw it for you. I'll draw it in my own fucking blood if you like—"
"He keeps offering," {n}she says to you.{/n} "Rhez keeps not taking him up on it."
{n}The woman in grey shifts her grip on the knife.{/n} "Knee or hand, Lady?"
"Not yet. We have a guest."
{n}Nocticula lets the sailcloth fall open across her knees. The flower is exquisitely made, black thread on black cloth, visible only when the lamplight slides across it. Someone paid this man a great deal of silver to sail under it. Someone else did not come home.{/n}
"Three of his passengers vanished. Two came back richer than they left. He thought that was the interesting part." {n}She smiles up at the hanging man.{/n} "It isn't. The interesting part is that a mortal on my quay believed I would not notice my own flower flying from his mast. Who taught him that, darling? Who told you I was busy?"
"Nobody—nobody, Lady, I swear—"
{n}Rhez steps in and does something brief to his ribs. Orren's breath goes out of him in a high whistle. Nocticula's foot pauses, then resumes, keeping time with the new rhythm.{/n}
"You see? He lies the way other men sweat. Without effort, and all over everything."''',
      c('"Why drag me down here to watch?"', "offer"),
      c('"Is this about your brother\'s plan?"', "council", requires=f("socoth_plan_exposed"))),
    n("council", "Nocticula", '''"Is it?" {n}She tilts her head and considers you, not the man on the rope.{/n} "My silly, silly brother built a scheme for me with a trapdoor in the middle, and you brought me the trapdoor before I stepped on it. I remember that. I remember useful things; it's one of the habits that has kept me on my throne."
{n}She reaches up without looking and straightens Orren's collar. He flinches as though she had struck him.{/n}
"Don't mistake it for a pardon. I haven't forgotten how you first walked into my palace uninvited, and I don't reward every intrusion because one of them turned out clever. But you have a nose for the part of a scheme its author meant to hide." {n}She lifts the flower from her lap and lets it hang between two fingers.{/n} "Bring me this one."''', c('"Then show me the rest of it."', "offer")),
    n("offer", "Nocticula", '''"Because I want you watching." {n}Nocticula rises from the bollard. Barefoot on the wet stone she is still taller than the hanging man, and she walks a slow circle round him the way a buyer walks round a horse.{/n} "My court watches me all the time. It's dull; they only ever see what they've been told to admire. You I can't predict. You might flinch. You might bargain for him. You might ask for the interesting part. I want to find out which, and I want to find out here, where it costs something."
{n}She stops behind Orren and rests her chin on his shoulder, cheek against cheek, so that both faces look at you: his grey with fear, hers delighted.{/n}
"Here is what I want. Find where the missing ones went. Find who taught a mortal to sell my flower, and how. And then, when we have all of them on a rope like this one, I decide what everyone pays." {n}She turns her head and kisses Orren's ear. He makes a sound like a kicked dog.{/n} "You may tell me what you'd decide. Execution is mine. Opinions I take from anyone. I only keep the good ones."
"And if I say no?"
"Then you'll have said no to me on my own quay, and I'll have learned something about you." {n}Her smile does not move.{/n} "Let's make it interesting. I'll bet you the thief lies about the lamps again before Rhez gets bored."
"I'm not bored, Lady," {n}says Rhez.{/n}
"You're always bored. It's why you cost me so much."
{n}Orren has started to cry without much noise, the way men do when they have learned that noise is expensive. The tide is coming in. Beyond the harbor wall a slaver's barge slides past without lights, oars muffled, and nobody aboard it looks toward the bollard where the Lady in Shadow stands with her cheek against a thief's.
She lets go of him and comes to you. The sailcloth is in her hand again; she folds it once and tucks it into your belt, where it lies against you like something warm.{/n}
"There. Now you're carrying my flower too. Try not to sell it."
{n}Behind her, Rhez has taken hold of Orren's left hand and is examining his fingers one by one, the way a jeweler examines stones, deciding which to keep. He watches her do it with his mouth open and no sound coming out. Nocticula does not look round.{/n}
"Well, darling? I'm waiting, and so is he, and one of us is enjoying it."''',
      c('"Then let\'s hear him scream it."', flags=f("started", "invitation_accepted")),
      c('"Not tonight. Tonight I want you."', "later"),
      c('"No. Not your thief, not your harbor."', "decline_undertaking")),
    n("decline_undertaking", "Nocticula", '''{n}She does not get angry. She laughs, softly, the way one laughs at a dog that has refused a bone.{/n}
"You came all the way down here to tell me no. How touching." {n}She plucks the sailcloth back out of your belt.{/n} "Go back to your cot. He'll scream just as well without you."
"And our bargain?"
"Was never about a harbor. The Worldwound is still the price, and you are still entirely capable of disappointing me about it." {n}She turns away before you have answered, already bored with you.{/n} "Rhez."
"Hand, Lady?"
"Hand."
{n}You wake before you hear it. That is the only mercy in the dream, and it is not hers; it is only the Gift letting go of you. No further word comes from her about the harbor.{/n}''',
      c('[Decline the harbor undertaking permanently.]', flags=f("closed", "undertaking_declined"))),
    n("later", "Nocticula", '''"Not tonight? You'd leave a man hanging." {n}She looks at Orren, and then at you, and her mouth curls.{/n} "So would I. He'll keep. Rhez knows exactly where to stop."
{n}She takes your hand, hiding the flower between your palms, and the quay folds upward. Now there is a balcony of black stone above it, cushions heaped along a rail, the whole harbor spread out below like a tray of coals. You can still see the mooring ring from here. You cannot see the man on it, only the small dark shape where he is.
Nocticula lays the sailcloth on the balustrade and turns her attention to you, all of it, which is a great deal of attention.
The black dress comes open one hook at a time while she watches you watch her do it. The rail is cold against your back when she pins you there with one hand flat on your chest, and her mouth finds your throat as if she were looking for the pulse to bite.{/n}
"You asked for me instead of the work. Do you know how rarely anyone dares to want me more than they fear me? Remember that you did. I will."
{n}When she has had enough of your standing she pushes you down onto the cushions and follows you down, a knee on either side of you, her hair falling round both your faces. Far below, a man on a rope says something hoarse that might be a prayer. She laughs into your mouth, and the city goes on burning beyond the rail.
Later, the flower is still where she left it on the balustrade, folded over: a hook, not a question.{/n}
"Tell me when you've finished wanting things that aren't work," {n}she says, as the dream thins.{/n} "Then come back and watch him. I've told Rhez to save the good parts."
{n}You wake in Drezen with the ghost of her teeth at your throat and no mark to show for it.{/n}''', c('[Let the harbor wait.]', abort=True)),
], delay=0)

s("sixth_passenger", "The sixth passenger", [
    n("start", "Narrator", '''{n}The Gift takes you down instead of across: stone stairs, then more stone, then a corridor under her palace where the air is warm and close and smells of hot iron and old perfume. The cells down here are not dungeons. They are small rooms, beautifully kept, with good rugs on the floors and locks on the outsides of the doors.
In one of them Orren Vale sits in a high-backed chair with his wrists strapped to its arms. It is a good chair, carved and padded; he has bled on the padding. Nocticula is perched on the arm of it with her fingers in his hair, and Rhez leans against the wall with the knife laid along her forearm.
The interrogation began without you. You can tell by the small, neat cuts on the backs of Orren's hands, and by the smear of rouge across his mouth where someone has been kissing him.{/n}
"There you are." {n}Nocticula does not stop stroking his hair.{/n} "We've started. Don't sulk; he's told it twice already, and differently both times, so you haven't missed anything true. Tell the Commander the arrangement, darling."
"A kiss," {n}Orren says hoarsely,{/n} "for every true thing."
"And?"
"And Rhez for the rest."
"One kiss for every true thing. Rhez holds the other half of the arrangement." {n}She bends and kisses his temple, tenderly. He shudders all the way down to his boots.{/n} "That was for saying it right. Now. The story, from the beginning, for our guest."
{n}He tells it. The captain ran his ship at a cliff on the Midnight coast, in calm water, at night. Where the waves struck, the rock opened: a door, black and wet, wide enough for a longboat. Beyond it lay a dry harbor of sand and stone, with lamps burning on posts and nobody tending them. Six lamps, the first voyage. He unloaded sealed cases, and took his pay in silver and in coins cut cleanly in half, which the captain called tokens for the way back. On the second voyage there were five lamps.{/n}
"Six, then five." {n}Nocticula's fingers tighten in his hair until his head tips back against her breast.{/n} "Earlier it was seven, then five. Before that you didn't remember the lamps at all. Tell me about the lamps again, darling. Slowly. I like the part where you lie."
"I'm not lying. I want a better chair. That's all. If I tell it right, I want a better chair—"
{n}Everyone in the room knows he will not get one. Even Orren knows it. He goes on asking anyway, because asking is the last thing he owns.{/n}''',
      c('"The lamps. Make him count them again."', "measure"),
      c('"What did he steal?"', "theft"),
      c('"Who didn\'t come back?"', "missing")),
    n("measure", "Nocticula", '''{n}Orren counts the lamps again. It takes him three tries. The first time there are six and then five. The second time there are six and then four, because, he says, one had gone out. The third time he stops at five and looks at Rhez instead of at anyone else.{/n}
"Three tellings." {n}Nocticula holds up three fingers in front of his eyes.{/n} "One of them is the lie I like least. Pick the lie, Commander. I'll let you choose which one he pays for. Consider it a courtship gift."
{n}You choose the four. A lamp does not go out in a harbor where nobody tends the lamps; he said so himself not a minute ago, proud of the strangeness. Rhez's knife moves once. It opens the skin over his knuckles in a line so straight it might have been ruled, and Orren screams in a voice that cracks in the middle like a boy's.{/n}
"Good choice." {n}She kisses him on the mouth while he is still screaming, which stops it.{/n} "Five, then. Six lamps, and then five. Someone is burning in that harbor, one fewer every voyage, and he unloaded his cases beside them and took his silver and never once asked what the lamps were for."
"I didn't want to know."
"Of course you didn't. That's what you're going to pay for."''', c('"Six, then five. Keep him counting."', "terms", flags=f("asked_weights"))),
    n("theft", "Nocticula", '''"He stole something before he came to me. He's been very coy about it, which means it's the best thing he has."
{n}Rhez lays the knife flat across the back of Orren's right hand, not cutting, only resting it there, and Orren talks.
A brass instrument, palm-sized, from the captain's cabin: six hollow pins set round a lens. Look through the lens, he says, and you see the room you are standing in, but empty, as if everyone in it had already left. He took it on the second voyage. He sold it in the Fleshmarket the night he came ashore, to a buyer whose face he never saw, for enough silver to buy himself a slave of his own.{/n}
"Did you?" {n}Nocticula asks with interest.{/n} "Buy one?"
"A girl. For the house. Yes, Lady—"
"How enterprising. Where is she now?"
"With my sister."
"Not anymore." {n}She smiles at Rhez, and Rhez nods once, and something is decided about a girl in a house you will never see.{/n} "He sold the only thing that could have taken him safely through that door, to a stranger, for a slave. In the Abyss, darling, getting caught is fatal; being stupid is merely expensive." {n}She looks at you over his head.{/n} "Commander? He stole it with that hand. It's right there."''', c('"Get the buyer\'s name. Leave the hand."', "terms", flags=f("asked_instrument"))),
    n("missing", "Nocticula", '''"Names, darling. The ones who didn't come home. Give the Commander their names."
{n}This part he does not want to tell, and for the first time tonight the reluctance looks like something other than haggling. He knew two of them. Vessa, who ran the repair yard at the end of the Middle City quay, a big woman with burn scars up her forearms, who sailed to see the harbor's moorings for herself. Halren, a pilot, who taught Orren to tell a false harbor light from a true one when Orren was a boy on the boats. Neither came back on the second voyage. In the fifth lamp, Orren says, a rag of blue cloth had caught on the post, and he had taken it for a sailor's charm against storms.{/n}
"Halren wore blue," {n}he says.{/n} "He always wore blue. I didn't think—"
"No, you didn't." {n}Nocticula's voice is light and quite pleasant.{/n} "Don't weep for them, darling; they aren't yours. Everything that sails under my flower is mine, and that includes whatever is burning in those lamps." {n}She glances at you.{/n} "Don't look at me like that, Commander. I'm not mourning them. I'm counting them. Finding one's own property isn't mercy; it's housekeeping. Call it whatever makes you feel better about yourself."''', c('"Count them, then. Every name."', "terms", flags=f("asked_missing"))),
    n("terms", "Nocticula", '''{n}Rhez wipes her knife on the padding of the chair. Orren has gone quiet. He is looking at his hands, at what has been done to them tonight, with an expression of enormous surprise.
Nocticula slides off the arm of the chair and comes to you. She has his blood on her fingers and rouge on her mouth that is partly his, and she stands close enough that you can smell both.{/n}
"Now. Tell me what you want out of this." {n}She draws one bloody fingertip down the front of your shirt, slowly, from collarbone to belt.{/n} "Everyone who helps me wants something. Gold, a title, my bed, the pleasure of watching. An opportunity to improve my morals?"
"Would you believe the last one?"
"I'd believe you wanted it. I'd advise you to bring better equipment." {n}She tilts her head back toward the chair.{/n} "He wanted protection. I offered him all of it in exchange for every coin he ever made off my flower, and he offered me half. Half! In a chair like that. I adore him. I'm going to be so sorry when he's used up."
{n}Behind her, Orren has begun, very softly, to laugh, the way men do when something inside them has come loose.{/n}
"So. What does my crusader want? Say it plainly. I hate guessing, and I always guess right, and then I'm bored."''',
      c('"Find the passengers. They\'re yours; get them back."', flags=f("witness_heard", "purpose_rescue")),
      c('"I want whoever taught him working for you, or dead."', flags=f("witness_heard", "purpose_power")),
      c('"I want to see what you do with him."', flags=f("witness_heard", "purpose_curiosity"))),
], "invitation_accepted")

s("lamp_measure", "The measure of a lamp", [
    n("start", "Narrator", '''{n}Nocticula meets you in a room with a low ceiling and no furniture except an enormous balance. Six lamps hang from one side. The other holds a brass instrument, enlarged until you can see the fine scratches around its lens.
She has acquired a copy of the ship's loading book. Here it appears as floating columns, the numbers turning whenever you walk around them.{/n}
"The captain owns two sets of weights. A tolerably familiar fraud. Unfortunately, the discrepancy survives comparison with both."
{n}One column names the passengers. Another lists timber, salt, copper, and six sealed cases described as devotional supplies. The same six cases appear on three voyages, always under different owners. No passenger appears twice except Orren.{/n}
"We have not bought his instrument back," {n}she says.{/n} "This is a drawing made by the craftsman who repaired its hinge. He could describe everything except the contents of the pins. He had the sense not to open them."
"A rare quality in a craftsman?"
"In anyone asked to mend something valuable without being told what it does."
{n}Nocticula stands close behind you as you study the columns. Her presence is an agreeable distraction and, you suspect, an intentional one.{/n}
"If I were trying to make this easy," {n}she murmurs,{/n} "I would have asked somebody less interesting to read it."''',
      c('[Compare loading intervals, declared weights, and the repeated cases. Knowledge: World, DC 30.]', check=dict(Skill="SkillKnowledgeWorld", DC=30, Success="read", Failure="miss", CommanderOnly=True)),
      c('"Let us bait the captain with a shipment that is weighed honestly."', "bait"),
      c('"Offer him two profitable lies that cannot both be true."', "trick", requires=("trickster",))),
    n("read", "Nocticula", '''{n}You stop following the weights and compare the owners. Each repeated case changes hands after the ship returns, never before it leaves. The devotional goods are being sold retrospectively. Whatever enters the harbor can acquire a new owner while it is already inside.
You draw a line through the six names. Then you put the missing passengers beneath them.{/n}
"He does not transport the same cargo three times. He sells a claim to what has already arrived. The weights are an excuse for the payments."
{n}Nocticula looks at your arrangement, then at the lamps. Only now does she move away from your shoulder.{/n}
"That would explain why the fifth lamp changed without another passenger boarding. Someone purchased an old arrival."
"And why a stolen navigational instrument matters. It might identify what he is actually selling."
"Or allow the buyer to collect it."
{n}She turns the balance. Its beam cuts across the floating columns, separating the supposed cargo from the names.{/n}
"You have made this considerably less amusing."
"Because it may be worse than smuggling?"
"Because I should have seen it first."
{n}She kisses you without warning, brief and exact, then steps away before you can mistake it for a distraction from the answer.{/n}
"There. I can be generous about a defeat when it is useful."''', c('"We follow the ownership transfers. Keep the captain unaware."', flags=f("method_chosen", "ledger_read"))),
    n("miss", "Narrator", '''{n}The figures almost agree. You find a pattern in the salt shipments and spend long enough defending it that Nocticula stops teasing you. She produces a second page. It contains the same payments with no salt aboard.
For a moment the room is uncomfortably quiet.{/n}
"A plausible answer," {n}she says.{/n} "I have killed people for supplying worse ones with greater confidence."
"Shall I apologize for surviving?"
"Only if you insist on continuing the argument."
{n}You erase the connection you made. The floating columns separate again. Nocticula does not conceal the correction beneath a compliment.
The lost time has a consequence. Her agent has held Orren in protection long enough that the captain's men have begun looking for him. A quiet comparison of accounts will now be difficult. Nocticula can still send a deliberately conspicuous shipment and see what the captain offers to conceal.{/n}
"It costs me a merchant who can be trusted to act surprised," {n}she says.{/n} "They are rarer than merchants who can be trusted with money."
"Use one who dislikes the captain. Surprise will be easier when he is enjoying himself."
{n}That wins a small smile.{/n}
"Perhaps you have not entirely wasted my evening. Choose what he is to offer."''', c('"A shipment with an owner too prominent to disappear quietly."', "bait", flags=f("ledger_missed"))),
    n("bait", "Nocticula", '''"Prominent enough to be noticed. Not so prominent that he refuses the business."
{n}She chooses a broker named Meret, a middle-aged tiefling whose warehouses depend on the harbor trade. You have not met her. Nocticula describes her as honest about the occasions on which she intends to cheat.
The proposed cargo is copper stamped with Meret's own mark. Every ingot will have been weighed twice before loading. If the captain invents a discrepancy, Meret will demand to know whose scales he proposes to use.{/n}
"It warns him," {n}you say.{/n}
"Yes. You wanted an experiment rather than an elegant guess. The subject may notice he is being experimented upon."
"And Meret?"
"She owes me eleven thousand in salt and sulphur. She will carry the copper to have a third of it forgiven. If the captain makes her disappear, I lose a debtor and he loses a great deal more than copper, and Meret knows that arithmetic better than anyone. It is why she still sleeps at night."
{n}Nocticula holds out her hand. You give her the imaginary loading book. She closes it, and the room's columns vanish.{/n}
"The captain will tighten his operation. We lose surprise, gain a controlled shipment, and owe Meret something. I hope you enjoy accounting. It becomes intimate surprisingly quickly."''', c('[Authorize the conspicuous shipment within this undertaking.]', flags=f("method_chosen", "bait_sent"))),
    n("trick", "Nocticula", '''"Explain before you attempt to amuse me."
"He profits from being the only man who can satisfy a buyer. Give him two buyers. One wants a passage kept secret. The other will pay more if the same passage is publicly guaranteed by you."
"He could simply refuse the second."
"Unless the second has purchased the first buyer's debt. Then he must explain which obligation owns the voyage."
{n}Nocticula studies you. The smile comes slowly, with real interest behind it.{/n}
"You want him to choose a lie in front of someone who can collect on either answer."
"I want him to ask his supplier how to answer. We follow the question."
"No transformation of the universe? No demand that I admire a pun?"
"Will you pay more if I add one?"
"Less."
{n}She chooses two agents who have never openly worked together. Their offers will be carried through rival intermediaries. One is to complain about the price where the captain's clerk can hear him. The other will arrive carrying the disputed debt in a case too expensive for its contents.
Nocticula places the two offers on opposite sides of the balance.{/n}
"If he flees, he takes the route with him. If he answers, we learn who corrects his mistakes. I accept the risk. Do not become dull now that I have encouraged you."''', c('[Commit the contradictory offers and follow the captain\'s inquiry.]', flags=f("method_chosen", "double_offer"))),
], "witness_heard")

s("captains_reply", "The captain's reply", [
    n("start", "Narrator", '''{n}The Gift sets you down on a deck that moves. That is the first thing: after the stillness of her other dreams, this ship rocks and creaks and stinks of bilge and tar and fish, and the rope fenders squeal against the stones of the Fleshmarket quay. Up the quay the auction blocks are being sluiced down for the morning. A chained line of slaves shuffles past the gangplank, and the slaver driving them glances up at the ship's stern lantern and walks faster.
The captain's cabin is at the stern. Nocticula is sitting at his desk.
She has his book open in front of her and her bare feet up on his chair. Behind her, standing very straight against the bulkhead because Nocticula has told her to stand there, is a woman of perhaps forty with ink on her fingers and a slave's iron collar half hidden under a high-necked dress. Rhez sits on the bunk, eating the captain's figs.{/n}
"Come in, come in. He's ashore. He'll be back within the hour, drunk, and he has no idea I'm here, which is the best way to meet a man." {n}Nocticula turns a page.{/n} "This is Dessa. Dessa keeps his books, warms his kitchen, and crossed out 'master' every time she wrote it. Look."
{n}She turns the book so that you can see. Down every page, in a neat clerk's hand, the word master has been written and struck through, with captain written above it. Hundreds of times. The ink of the strokes is darker than the ink of the words, pressed hard enough to dent the paper.{/n}
"It made her slower. He beat her for it twice, she says. She kept doing it." {n}Nocticula looks up at the woman behind her with frank, warm appreciation, the way she might look at a well-made knife.{/n} "I like her already, which means she's mine. The only question is where I put her. Dessa, darling, how long have you belonged to him?"
"Eleven years, Lady." {n}Dessa's voice is perfectly level.{/n} "The city swallowed my ship. He bought me off the block for my handwriting."
"And now I've swallowed him. Isn't the Abyss tidy?"''',
      c('"What did squeezing Orren give us?"', "ledger", requires=f("ledger_read")),
      c('"Who took the flower off Orren?"', "bait", requires=f("bait_sent")),
      c('"Which of the two lies did the captain swallow?"', "double", requires=f("double_offer"))),
    n("ledger", "Nocticula", '''"Everything, eventually. He had more in him than he thought."
{n}What Orren gave up, between the kisses and the cuts, matches what Dessa has been writing in the captain's book: every run to the cliff door, every sealed case, every half-coin. And on every page, in Dessa's hand, a seventh line where the harbor has only six berths, left blank, waiting for something the ship never carries.
Beside one of the seventh lines Dessa has written a name in the margin, very small: Ilvara. Beneath it, smaller still: white shoes. Never comes aboard. Meets him on the quay, where the mud is, and the mud never touches her.{/n}
"A woman who walks through harbor filth without looking down." {n}Nocticula taps the name with one nail.{/n} "People forget beautiful faces. They remember who can afford to stay clean. And the captain has no idea his slave has been writing her down, and no idea his thief is in my cellar. He thinks he's merely dishonest. He doesn't know which of his dishonesties I've found."
"He'll find out when she stops paying him," {n}Dessa says, behind her, without being asked.{/n} "He's afraid of her, Lady. He drinks after every meeting. He thinks I don't notice."
"Everyone thinks their slaves don't notice." {n}Nocticula smiles.{/n} "It's the most useful mistake in the world."''', c('"Let him go on not knowing. We follow her."', "dessa", flags=f("collector_unwarned"))),
    n("bait", "Nocticula", '''"Someone very eager." {n}Nocticula looks pleased.{/n} "Orren went home with my flower pinned through his ear, as you wanted. He lasted until midnight. The captain found him in a tavern, beat him senseless, and tried to sell him back to the woman who taught him, as a token of good faith."
{n}Dessa speaks without being told to.{/n} "Ilvara paid for him in cut coins, Lady. Half-coins. The captain bit one to see whether it was good."
"And then she gave Orren back to us. In a sack. On my palace steps. Alive, bruised, and with my flower still pinned through his ear, because she didn't dare take it out." {n}Nocticula laughs.{/n} "She knows someone is watching now. She doesn't know who, and she was too frightened to look. I'd rather have had her unwarned. But oh, the sack."
{n}She turns to the window, where the morning is coming up grey over the slave pens.{/n} "Frightened people move. They move their money, their stock, their passengers. She'll try to close the harbor, or empty it, or sell what's in the lamps before I can reach them. Which means tonight the captain gets a visit, before he can tell her anything Dessa has seen."''', c('"Then she\'s running. Take Dessa before the captain thinks."', "dessa", flags=f("collector_warned"))),
    n("double", "Nocticula", '''"Both of them. I'd have been disappointed by anything less."
{n}Orren went back to the captain carrying two offers, as you devised: a private buyer who wanted a passenger delivered to the harbor and sold before he arrived, and a public charter that wanted the same berth. The captain took the deposit for both. Then, unable to decide which buyer to cheat, he wrote to the woman on the quay to ask whether a passenger could be sold while still at sea.
Dessa copied his letter, and the answer.{/n}
"Her name is Ilvara," {n}Nocticula says.{/n} "She told him no. A passenger has to cross the door before he can be sold. Arrival first, then ownership." {n}She holds up the copied answer between two fingers, and it smokes gently at the edges.{/n} "She put it in writing. People so rarely put the important part in writing. I'd have paid a great deal to learn that rule, and you got it out of her with two lies and a greedy captain. She suspects someone is asking questions; she doesn't know it's me. Uncertainty is a guest I like to send ahead of me. It softens the meat."''', c('"Keep her guessing. Take Dessa while they decide whom to blame."', "dessa", flags=f("collector_warned", "transfer_rule_known"))),
    n("dessa", "Nocticula", '''{n}Nocticula takes a knife from the desk drawer and lays it on the open book. It is a kitchen knife with a worn wooden handle, sharpened so often that the blade has thinned to a crescent.{/n}
"Her mother's. He told her a slave can't own a knife, and kept it in his desk to remind her. Eleven years." {n}She turns it so that the lamplight runs along the edge.{/n} "Dessa asked me for the pleasure first. Before freedom, before passage, before anything. I approved her priorities. Then I told her she isn't getting freedom, because I don't give things away, and she said—what did you say, darling?"
"I said I'd rather belong to someone who can read, Lady."
"You see? Mine." {n}Nocticula leans back in the captain's chair and regards you over the knife.{/n} "So. She's mine; that was settled when I saw the page. Where I put her is yours. I could leave her aboard, still his in his own eyes, writing down everything he does and sending it to me: a coin with my face on it, sitting in his purse. I could take her tonight, in front of him, and let him find out exactly whose flower he sold. Or I could do something to him that leaves her the ship."
{n}On deck, someone is singing badly. The gangplank thumps. Rhez puts down her fig.{/n}
{n}Dessa has not moved from the bulkhead, but her eyes have gone to the knife on the book and stayed there. She is not asking. She has been a slave for eleven years, and she knows exactly how much asking costs.{/n}
"He's early," {n}Rhez says.{/n}
"How lovely. Decide quickly, darling."''',
      c('"Leave her aboard. Let her keep his books, for you."', "lease"),
      c('"Take her. Publicly. And let him find out why."', "threat")),
    n("lease", "Nocticula", '''"Quiet. You like quiet things. I'm learning that about you."
{n}Nocticula closes the book and hands it to Dessa, and Dessa puts it in its drawer and the knife in her apron. When the captain comes stumbling down the companionway he finds his cabin empty but for his slave, bent over the book by lamplight, writing captain where she means master. Nocticula and Rhez are behind the bulkhead curtain with you. You can hear him breathing. You can smell the wine.{/n}
"Write it all down, girl," {n}he says, and falls into his bunk.{/n}
"Yes, captain."
{n}Behind the curtain Nocticula has her mouth at your ear.{/n} "She'll be mine, in the way a coin with my face on it is mine: nobody else spends it. He'll go on giving her orders. She'll go on obeying the ones that amuse me. And one night, when I've had everything I want out of that book, I'll let her use the knife, and she'll have waited long enough to do it beautifully."
"Until then she's still his slave."
"She's my slave who sleeps in his cabin. There's a difference, and she knows it, and that's the only kind of difference that counts." {n}Her teeth close lightly on your earlobe.{/n} "You make expensive distinctions, Commander. I may acquire a taste for watching you defend them."
{n}On the other side of the curtain the captain has begun to snore. Dessa's pen goes on scratching, steady, unhurried, and every few lines it stops, and presses hard, and moves on.{/n}''', c('[Leave Dessa aboard as her eyes.]', flags=f("dessa_safe", "lease_bought"))),
    n("threat", "Nocticula", '''"Publicly. Oh, I hoped you'd say that."
{n}The captain comes down the companionway singing, and stops singing. He is a big man going soft, with rings on every finger and wine down his shirt, and he looks at the woman sitting at his desk with her feet on his chair, and at the grey assassin on his bunk, and at you, and he knows. Everyone on the Fleshmarket quay knows that face.
He kneels. Nobody tells him to.{/n}
"Lady—Lady, I didn't know it was yours, I swear on my mother's—"
"Your mother keeps songbirds in Shatterstone. I know. Kneel nearer the lamp." {n}He shuffles forward on his knees. She looks down at him with real pleasure.{/n} "You sold passage under my flower. You sold my people into a hole in a cliff. And you kept your slave's mother's knife in your desk to teach her what she couldn't own." {n}She holds the knife out behind her without looking, handle first.{/n} "Dessa. He told you a slave can't own a knife. Go on. Show him what a slave can own. Leave him one ear; he'll need something to hear the story with."
{n}Dessa takes the knife. She does not hurry. She takes his left ear the way she wrote captain over master: with care, pressing hard. He screams, and does not move, because the Lady in Shadow is watching him and moving would be worse.
Nocticula throws back her head and laughs, long and hard, and the sound goes up through the deck and out over the quay, and up and down the Fleshmarket people stop what they are doing to listen.{/n}
"Oh, that was worth the trip. Dessa, darling, wipe that and keep it. You're going to the Harem of Ardent Dreams tonight, as my gift to Shamira. She collects clever women; she'll be beside herself." {n}She stands and steps over the captain on her way to you.{/n} "And tell everyone who asks why you carry a knife. Especially the ones who ask nicely."''', c('[Send Dessa to the Harem with the knife.]', flags=f("dessa_safe", "threat_sent"))),
], "method_chosen")

s("her_own_face", "Her own face", [
    n("start", "Narrator", '''{n}The Gift does not set you down on a quay tonight. It sets you down in a bed.
You know the room without being told: a chamber high in her palace, hung with dark silk, the air heavy with incense and warm skin. Through the wall comes music, low drums and a woman's laughter and a harp played badly on purpose. That is the Harem of Ardent Dreams, next door, where Shamira keeps her court and where the Lady in Shadow goes when she is weary of plots and wants wild passion. Tonight she has not gone next door. Tonight she has brought you here instead.
A single lamp burns on a low table beside a bowl of pale fruit and a book lying face down. Nocticula sits at the foot of the bed in a black gown with one fastening at the throat, and the face she turns toward you is her own. Not a mask. Not one of the faces she wears for her court, the beautiful, terrible ones. This one is narrower, older about the eyes, and amused at you before you have said a word.{/n}
"No mask tonight." {n}She bites into a piece of fruit.{/n} "You'll remember this face whether you like it or not. I've decided."
"The harbor?"
"The captains can wait. They're all appetite and no imagination. I have both." {n}She holds the rest of the fruit to your mouth, and when you take it her thumb stays on your lower lip, and presses, and only then withdraws.{/n} "Dessa is where you put her. Orren is where you put him. Rhez is somewhere, being expensive. Everyone in my city knows their place tonight except Shamira, who has just realized I'm not coming to her, and is playing that harp very badly on purpose so that I'll hear."
{n}The harp, as if it had heard, strikes a note so sour it can only have been deliberate. Nocticula smiles at the wall the way one smiles at a cat scratching at a closed door.{/n}
"She'll come round. She always does, eventually, with a knife behind her back and a kiss in front of it. That's why I keep her. Nobody else in the Abyss has ever made betrayal look so much like devotion."
"I know what obedience sounds like. It bores me. Tonight I want you hungry." {n}She lies back across the foot of the bed, propped on one elbow, the lamplight on her throat.{/n} "Well?"''',
      c('"I wanted to see you without another face between us."', "face"),
      c('"I enjoy your inventions. Show me which ones amuse you."', "invention"),
      c('"Tonight I\'d rather talk. You can keep the fruit."', "talk")),
    n("face", "Nocticula", '''"My own face? You've developed an expensive preference. Most people who see it don't survive the novelty."
{n}She turns your hand palm up and draws a fingernail across it, wrist to fingertip, hard enough to sting. When you look up from the thin red line she is already close enough to kiss you. You meet her. She lets you, then bites your lower lip, not gently, and draws back just far enough to watch it bleed.{/n}
"There. No mask to blame when you come looking for this again. And you will." {n}She takes the single fastening at her throat between finger and thumb.{/n} "I'm not going to wait while you work up to it. I'm not some crusader's shy widow. Open it, or I'll open you."''', c('[Open the fastening.]', "night", flags=f("own_face_chosen"))),
    n("invention", "Nocticula", '''"At last, someone asks about craft instead of power. Everyone wants to know what I can do. Nobody asks what I enjoy."
{n}She lifts the empty bowl. Its pale inside becomes a summer sky, and a small grey cloud crosses it, slowly enough that you can see rain falling from it over a distant hill.{/n}
"I despise perfection. It makes people suspicious. A room with no dust persuades no one they've arrived somewhere private. One misplaced thing does more work than a thousand tiles." {n}She tips her head at the book on the table.{/n} "Like that."
"What is it?"
"A chronicle of a little mortal dynasty. Two hundred years of poisoning one another over a ford, and then a flood moved the river. The last chronicler blamed a rival family's manners." {n}She laughs.{/n} "I find their persistence admirable. I've known demons give up a feud for less. I've known demons I gave up for less."
{n}She puts the bowl in your hands. The cloud follows your thumb as you tilt it; the rain goes on falling on the hill regardless.{/n}
"I could make it follow every gesture. Then there'd be nothing for you to watch but yourself, and you'd grow bored, and I'd have to kill you, and I'm not finished with you." {n}She takes the bowl back and sets it on the floor, and the sky inside it goes out.{/n} "That amuses me. You amuse me. Come here."''', c('[Go to her.]', "night", flags=f("craft_shared"))),
    n("talk", "Nocticula", '''"A devastating refusal. I shall have to eat two pieces."
{n}She does exactly that, slowly, watching you over the fruit, and licks the juice from her thumb. She does not argue. She has eaten a great many refusals in her time, and she lets you see her enjoy the taste of this one. Through the wall the harp stops, then starts again, triumphant: Shamira has decided she is winning something.{/n}
"Talk, then. About what? Not the harbor. I'll know you're lying if you say the harbor."
"That book."
"Oh, that book." {n}She picks it up and lets it fall open on her knee.{/n} "A chronicle of a little mortal dynasty that spent two hundred years poisoning one another over a ford. The last chronicler was a coward. The queen of his day had an affair so disastrous it cost them half the kingdom, and he tried to bury it under seven chapters about drainage." {n}She turns pages.{/n} "I can barely remember the affair. I can recite the drainage disputes nearly word for word."
"You think that's the more revealing part?"
"It tells me what he was afraid someone might compare. I've spent a long life reading around whatever people insist is important. The lie is never in the loud part. Orren lies about lamps. The captain lied about his cargo. Shamira lies with that harp." {n}She looks up.{/n} "You lie less than anyone I've had in this bed, and you aren't even in it. It's very irritating."
"And you?"
"I don't lie. I don't need to. I simply don't tell people things, and let them hang." {n}She smiles.{/n} "Tell me about a room. Not a battlefield. A room you remember badly."
{n}You describe one, from long before the crusade: a room you could draw only until someone asked where the second window was. She builds it as you talk, there in the lamplight between you, plaster and floorboards and a slant of afternoon. She puts the window in the wrong wall. You correct her. She moves it, and leaves one thing wrong on purpose, a door that opens the wrong way, and waits to see whether you will notice.
You notice. She laughs, and leaves it wrong.
The lamp burns down. Next door the harp gives up in the small hours. She does nothing she has not chosen, and she has chosen this; some time before morning she lies back with her head in your lap and her eyes closed, and informs you that if you repeat a word of tonight to anyone, she will have your tongue bound into a bookmark for that chronicle.{/n}''', c('[Keep the evening as talk.]', "morning", flags=f("quiet_evening"))),
    n("night", "Narrator", '''{n}Nocticula puts the bowl aside, and the book after it, and stops pretending the bed is for sitting. She takes your hand by the wrist and lays it at her throat, over the single fastening of the black gown, and holds it there until you open it. When you catch her other hand before it can change the room, she laughs low in her throat and leaves the lamp exactly where it is, so that you can see what you have uncovered.
She has no patience for being undressed slowly. Your belt, your collar, the rest of it goes wherever she flicks it, and she looks at you in the lamplight the way she looks at a map of a city she has decided to take. Through the wall the harp falters, and stops. Shamira is listening. Nocticula knows it, and smiles, and puts one hand flat on your chest and pushes, and you go down among the cushions, and she comes down after you, a knee on either side of your hips, her hair falling round both your faces like a drawn curtain.
"Look at me," she says. "My own face. Remember which one it was."
Her mouth closes on yours. She catches your wrists and presses them into the silk, smiling when you pull against her, and holds harder. "My own face," she says again, close enough for you to feel the words. The lamplight narrows to the bright edge of her hair, then vanishes.
Later she lies beside you on her stomach, chin on her folded arms, turning the pages of the chronicle where it has fallen to the floor. Next door the harp has started again, and it is playing something furious.{/n}
"That book," {n}she says,{/n} "ends with a flood. Two hundred years of ingenious murder, and the river decides the succession."
"You sound disappointed."
"I'd grown fond of the losing side. They had just hired an excellent poisoner." {n}She rolls onto her back and looks at you along the pillow. There is nothing tender in it, only an appetite that has eaten and is already considering the next course.{/n} "Don't go to sleep. You're already asleep, and I haven't finished with you."''', c('[Let her have the rest of the night.]', "morning", flags=f("private_night"))),
    n("morning", "Nocticula", '''"One question before you wake."
{n}She is sitting up now, the closed book between her hands. The room has not begun to dissolve, but you can feel morning pressing at it from outside, the way water presses at a hull.{/n}
"Ilvara is selling my flower and the people under it. When I take her road from her, some fool will call it a rescue. Some other fool will call it theft. Neither will be right; it is simply mine." {n}She turns the book over in her hands.{/n} "I'm going to hurt her in front of my whole court. Not quickly. My court bets on that sort of thing, and the betting is half the fun, and I'll want you there."
{n}She lays the book under your hand and draws you back against her, your spine to her breasts, her chin on your shoulder, her arms crossed over your chest like the bars of something.{/n}
"Will you still come here when she starts screaming?"
{n}She does not wait for you to answer. She knows the answer; she has been inside your head all night. What she wants is to hear you say it, here, with her arms locked over your chest.
You put your hand over hers. Her grip tightens until it hurts.{/n}
"Good. I'd hate to waste the lamp."
{n}The window brightens. You have time to notice that she has kept your hand pinned to the book before the weight of it disappears. In Drezen your pillow is colder than the silk she made for you.{/n}''', c('[Wake.]', flags=f("evening_kept"))),
], "dessa_safe")

s("white_shoes", "White shoes on a black shore", [
    n("start", "Narrator", '''{n}Ilvara arrives in the dream as a portrait drawn from three reports. Nocticula marks the uncertain details with deliberate flaws: one sleeve changes color, the ring on her hand has no stone, and her face remains indistinct around the eyes.
The shoes are perfectly clear. White leather, thin soles, expensive stitching. They stand on a strip of black sand that never sticks to them.{/n}
"My agents agree on those," {n}Nocticula says.{/n} "I thought you would prefer an honest uncertainty to a convincing face."
{n}Ilvara has sent a message after noticing the pressure around the captain. She addresses Nocticula by a private title used in older contracts. She offers a demonstration of the harbor's value in exchange for a meeting under a temporary truce.
The message describes the harbor as a place where journeys can be held unfinished. A passenger's arrival may be delayed, divided, or sold. It says nothing about lamps.{/n}
"A mortal magician," {n}Nocticula says.{/n} "Older than her face suggests, younger than her confidence. I have found three previous names. Under one she sold routes through dreams. Under another she arranged escapes from besieged cities. Under the third she was executed."
"Successfully?"
"The record is enthusiastic but imprecise. I have learned to distrust that combination."
{n}She places the offered truce beside Ilvara's portrait. Its seal is another half-coin.{/n}''',
      c('"What did she overlook while we kept the collector unwarned?"', "unwarned", requires=f("collector_unwarned")),
      c('"She knows you are interested. What is she trying to hide now?"', "warned", requires=f("collector_warned"))),
    n("unwarned", "Nocticula", '''"Her messenger carried two letters. He delivered mine and took the second to a buyer near the upper market. He did not know he was followed."
{n}The buyer wants the harbor emptied before Nocticula can claim it. His name is unimportant to her; his payment is not. He offered Ilvara a place aboard a departing vessel and enough power to establish herself elsewhere.
Nocticula produces a copy of the second letter. It asks whether the remaining lamps can be extinguished without damaging the instrument.{/n}
"They are considering abandoning whatever is inside."
"Or whatever sustains it. We still need the distinction."
"Can your agents stop the buyer?"
"Yes. But stopping him tells Ilvara we read the letter. I would rather make the escape less attractive before she knows it is in danger."
{n}She suggests purchasing the vessel's next berth through a third party, delaying its departure by an apparently unrelated dispute. It will buy one meeting, no more.
She counts out the berth money and adds the agent's fee. The shipowner has demanded both before holding the vessel. She pushes the coins through the dream's image of the receipt; when her hand comes back, it is empty.{/n}''', c('"Delay the vessel. We use the meeting to learn what the lamps hold."', "meeting", flags=f("escape_delayed"))),
    n("warned", "Nocticula", '''"Her escape. She has become very interested in the departure times of ships she cannot ordinarily afford."
{n}Ilvara has placed two guards at the warehouse. Neither is impressive enough to keep Nocticula out. They are impressive enough to kill a witness while their employer runs.
Nocticula does not propose testing the difference.{/n}
"I could close the harbor quarter. She would know before my order reached the final street. She might destroy what I want merely to punish me for making the attempt."
"Then offer her a reason to stay."
"She has already named one. A private audience and the possibility of becoming useful."
{n}You look at the temporary truce. Nocticula watches you read its narrow promise: no attack by either party during the meeting, no claim beyond its duration, no protection for anyone not named.{/n}
"It excludes the people in the harbor."
"Deliberately. She wants to learn how much they matter to us."
"Will she learn?"
"That depends on whether you let her choose the question."
{n}Nocticula smiles. She has begun to enjoy Ilvara's nerve, which is not the same as forgiving her use of the Black Flower.{/n}''', c('"Meet her, but decide our demand before she starts pricing it."', "meeting", flags=f("escape_open"))),
    n("meeting", "Nocticula", '''"The truce is for a real meeting in my city. You will not be there in the flesh. I can take your questions and return with her answers."
"You invited me into the investigation."
"Yes. I did not offer to carry your sleeping body into a room with an ambitious extortionist. You are my adviser, not my bait. I do not leave my possessions lying where other people can put a price on them."
{n}She draws two chairs in the sand, then erases one. The remaining chair faces the sea. Beside it she lays Dessa's final copy of the accounts. There are six numbered berths, then a seventh line with no passenger assigned to it.{/n}
"There is also this. Our diligent clerk copied the reservations. Ilvara has left one place blank on every voyage. I should like to know whom she expects."
"You can advise me. You can also ask me to make a promise in your name. I suggest you decide how much of your name you wish her to possess."
"She knows I work with you?"
"She suspects you are interested. I have not told her whether you are a patron, a lover, or an inconvenient voice I enjoy hearing."
"Which would she fear?"
"A patron would compete with her. A lover might be distracted. An inconvenient voice would ask questions she has not prepared for."
{n}Nocticula touches the indistinct face of the portrait, making it turn toward the empty second chair.{/n}
"I prefer the third. It costs us no false declaration and leaves her uncertain how far you will follow an answer."''',
      c('"Require the release of one missing passenger as proof that she can do it."', "release"),
      c('"Require a demonstration with something she owns. No borrowed victim."', "property"),
      c('"Offer her a false buyer for the seventh berth. See whether she corrects you."', "seventh", requires=("trickster",))),
    n("release", "Nocticula", '''"A clear demand. She will hear that you value the passengers."
"She will also hear that I want proof, not a performance."
"Those are not mutually exclusive. I shall require a name we can verify and a person my agents can question afterward. If she sends a convincing duplicate, I will count that as an insult to both of us."
{n}She studies you for a moment before setting the terms aside.{/n}
"You realize she may choose the least valuable captive."
"Then we learn she ranks them."
{n}Nocticula's eyes narrow with pleasure.{/n}
"There. A humane demand with a useful second edge. Keep doing that and I may begin to suspect you of enjoying the work."
{n}The portrait folds into the message. Nocticula carries it toward the water, already rehearsing how little eagerness she intends to show.{/n}''', c('[Ask for a verifiable release.]', flags=f("meeting_planned", "demand_release"))),
    n("property", "Nocticula", '''"She owns her shoes. I have developed an unreasonable interest in watching them get wet."
"Something more difficult to replace."
"Her chief assistant, perhaps. No, do not look at me like that. You said something she owns; I am demonstrating why the wording matters."
{n}You settle on the instrument itself. Ilvara may send it through the harbor and bring it back while Nocticula's agent records the interval. No captive is to be spent to make the demonstration convincing; Nocticula means to own every one of them before this is finished, and she dislikes watching her inventory wasted before she has counted it.
Nocticula corrects your proposed wording twice. The first correction prevents Ilvara from substituting a second instrument. The second prevents the demonstration from being presented as a completed sale.{/n}
"I would have asked for her signet," {n}she says.{/n} "But you have chosen something she needs enough to be frightened of losing. I approve."
{n}Her fingertips brush your wrist as she takes the terms. Her nails catch the paper beside your fingers. She folds it with the instrument's demand facing outward.{/n}''', c('[Demand the instrument\'s passage and verified return.]', flags=f("meeting_planned", "demand_instrument"))),
    n("seventh", "Nocticula", '''"There are six lamps."
"There is a seventh line in the accounts. Offer to reserve it for a passenger who has not yet agreed to travel. If she refuses, ask what would make the reservation valid."
"And if she accepts?"
"We learn whether she sells empty promises. Supply no name and pay no deposit. The offer must remain a question."
{n}Nocticula considers the shape of the trap. A false buyer could be exposed; an unanswered commercial inquiry is harder to punish without admitting why it was dangerous.{/n}
"You want to make her teach me the boundary of her own power."
"She wants you to believe it has none. She may overcorrect."
"Or attempt to sell me a boundary she does not possess."
"Then ask for the instrument as security."
{n}Nocticula laughs softly.{/n}
"I am beginning to understand why your friends keep inviting you to councils. It cannot be the brevity of the meetings."
{n}She accepts the inquiry, with one change: the hypothetical passenger must be powerful enough that an empty promise would be dangerous to collect. She leaves the name unspecified, allowing Ilvara's own ambition to furnish it.{/n}''', c('[Send the unnamed reservation and demand that she define its limits.]', flags=f("meeting_planned", "demand_seventh"))),
], "evening_kept")

s("demonstration", "What the harbor keeps", [
    n("start", "Narrator", '''{n}The throne hall of the Lady in Shadow is full tonight, and it is real.
You are standing on the dais before you understand how you got there. Below you the court spills down the steps in silk and chains and very little else: demons with jeweled horns, mortals in collars, succubi draped across courtiers like furs. A tiefling with a slate and a lump of chalk is taking bets at the foot of the stairs. The noise is enormous. It stops all at once when Nocticula lifts one finger.{/n}
"Sit. Not there. Here, at my right." {n}She does not look at you. She looks at her court, and lets them look at you.{/n} "Let them wonder what you cost me."
{n}You sit. A thousand eyes take your measure and file it away. The silence holds just long enough to become a weight. Then the doors at the far end of the hall open, and the guards bring in a woman.
She is tall and fine-boned, in grey velvet, her hair bound up in silver wire. She walks the whole length of the black floor in white shoes, and the shoes do not mark, and she does not look down. At the foot of the steps, between her guards, she curtsies as deeply as anyone you have ever seen.{/n}
"Ilvara," {n}Nocticula says pleasantly.{/n} "Who sold my flower."
"Who preserved it, Lady." {n}Her voice is low and beautiful and perfectly steady.{/n} "Who found a harbor nobody used and made it pay. I am a magician, Lady, not a thief. With your leave, I have come to show you the harbor's principle. It is very elegant. Arrival and possession need not occur at the same time."
{n}The court murmurs. Someone at the back laughs and is hushed. The tiefling with the slate has already chalked odds.{/n}
"She wants a commission," {n}Nocticula says to you, under the noise.{/n} "My protection, a place among my useful servants, and her harbor kept running under my name instead of stolen from under it. She's going to perform for it. In front of everyone. Which is already a humiliation, and she hasn't noticed." {n}She leans back on her throne.{/n} "What shall I make her prove?"''',
      c('"Make her bring one of them out. Here."', "release", requires=f("demand_release")),
      c('"Make her try it on something of yours."', "instrument", requires=f("demand_instrument")),
      c('"Ask her the price of the seventh berth."', "seventh", requires=f("demand_seventh"))),
    n("release", "Nocticula", '''"Out of the lamps? In my hall?" {n}Nocticula looks at Ilvara.{/n} "You heard my crusader."
{n}Ilvara bows again. From her sleeve she takes a lamp no bigger than a fist, brass, its flame very small, and a coin cut cleanly in half. She speaks a name that nobody else catches, and snaps the half-coin against its mate.
The flame gutters, and stretches, and a man steps out of it onto the black floor.
He is weathered and grey-bearded and dressed in sailor's blue, and in his hands he holds a boot and a half-stitched strap with the awl still threaded, as if he has been mending it for a very long time. He looks at the throne. He looks at the court. He drops the boot.{/n}
"Halren," {n}Nocticula says, and the court erupts.{/n}
{n}Half of them are betting he is real. Half are betting he is a trick. The tiefling with the slate shouts odds so fast the chalk snaps. Someone pinches Halren to find out, and he flinches, which settles nothing.{/n}
"He's real," {n}Nocticula says to you, as one comments on a horse.{/n} "And he's mine now. He crossed under my flower and came out under my roof. Ilvara has just given me a present and called it a demonstration." {n}She raises her voice.{/n} "Pay the ones who said real. Somebody take him downstairs and give him something to finish that boot with."''', c('"Keep Halren. Let her watch you keep him."', "price", flags=f("halren_returned"))),
    n("instrument", "Nocticula", '''"Something of mine." {n}Nocticula smiles.{/n} "My glove, perhaps? Ilvara has been looking at it since she walked in."
"Permit me to show the Lady the harbor's principle with something small," {n}Ilvara says.{/n} "Your glove, if it pleases you."
"My glove. How intimate. Go on."
{n}Ilvara spreads a strip of sailcloth on the floor and sets on it a brass instrument, six hollow pins round a lens: the thing Orren stole and sold. She speaks a word. The black glove on Nocticula's left hand slips from her fingers, crosses the air and lies on the cloth, and the court goes quiet.
Then Ilvara draws a small curved blade and cuts toward the glove, and the court sees what she is trying to do: sever the claim, keep the glove, prove that what arrives in her harbor belongs to her.
The blade parts the glove in two. It parts it on Nocticula's hand. The glove is back there, somehow, and the cut runs through the leather across her palm, and a thin line of black blood wells up in it.
Nobody in the hall breathes.
Nocticula throws back her head and laughs, long and hard, and after a moment the court laughs too, because it has learned to. She rises. She walks down the steps to Ilvara, who has not moved, and takes Ilvara's right hand in her own cut one, glove and blood and all, and closes it, and squeezes.
The bones go like kindling. Ilvara makes no sound until the third one.{/n}
"You've ruined a glove," {n}Nocticula says gently.{/n} "Let's make it a pair."''', c('"Now everyone has seen what her trick is for."', "price", flags=f("instrument_rule_known"))),
    n("seventh", "Nocticula", '''"The seventh berth?" {n}Ilvara's eyes flick to you, and back to the throne.{/n} "Lady, there is no seventh berth."
"No?" {n}Nocticula looks disappointed, extravagantly, for the whole court to see.{/n} "What a pity. I'd have bought it."
{n}A pause. You can watch Ilvara thinking: the Lady in Shadow, wanting something from her.{/n}
"There might be one, Lady. For a patron of sufficient importance. It would cost—"
"How much?"
"Nine thousand, for a share in perpetuity, though the risk—"
"You just priced a berth you said doesn't exist," {n}you say, loudly enough to carry.{/n}
{n}The court howls. The tiefling with the slate drops it. Ilvara opens her mouth and closes it again, and her white shoes take a half step back on the black floor.{/n}
"She thought I might volunteer," {n}Nocticula says, delighted.{/n} "To anchor her harbor, with me inside it, forever. A lamp with a crown on. The seventh line is a claim on the place itself; she's been selling shares in something she doesn't control." {n}She leans down from the throne.{/n} "Ilvara, darling. Would you have let me leave?"
{n}Ilvara says nothing at all, and the whole hall hears it.
Then, from somewhere on the upper steps, a courtier begins to laugh, high and helpless, and cannot stop, and the laughter spreads down the stairs like fire down a curtain until the whole hall is shaking with it, and Ilvara stands in the middle of it with her white shoes together and her face perfectly composed, and does not look at anyone.{/n}''', c('"There\'s her limit. She can\'t promise anyone leaves."', "price", flags=f("anchor_rule_known"))),
    n("price", "Nocticula", '''"Now, then."
{n}Nocticula rises, and the hall rises with her. She walks down the steps to where Ilvara stands, and circles her once, slowly, as she circled Orren on the quay.{/n}
"You came here to sell me a harbor. You've given my court the best night it has had since the last execution, and you've given me a present besides, and you haven't been paid for any of it. That's what happens to performers who can't read a room." {n}She stops in front of Ilvara.{/n} "Here is what happens next. You will open your door for me. Every lamp. Every name. And whatever walks out of that rock will be mine, because it crossed under my flower, and you will stand there and watch it walk past you."
"And if I refuse, Lady?"
"Then you're furniture. Something to sit on while I find someone else who knows the trick."
"Lady, I can build you more." {n}Ilvara's voice is still steady; only the words have begun to hurry.{/n} "Not one door. A dozen. Every old permission you ever gave has a scrap of you left in it, and I know how to find them. You could have a harbor on every coast of the Isles—"
"Built out of my own people, sold back to me by you." {n}Nocticula sounds almost tender.{/n} "Darling. I already have a city made of people. I don't need a magician to sell me another." {n}She turns and looks up at you on the dais.{/n} "She opens the door, or she's furniture. Choose which parts of her I keep in working order, darling."
{n}At the foot of the stairs the bookmaker begins chalking furiously. Ilvara's white shoes have not moved. You notice, now, that her hands have begun to shake, very slightly, and that she has folded them together so that the court will not see.{/n}''',
      c('"Keep her whole. She opens the door herself."', "witness"),
      c('"Break her hands. Orren can carry the coins."', "leverage")),
    n("witness", "Nocticula", '''"Whole. How generous of you." {n}Nocticula takes Ilvara's chin in her fingers and turns her face up toward the dais, toward you.{/n} "Thank the Commander, Ilvara. Your hands will be working the coins at my door. You'll break every one of them yourself. You'll call every name. And when the passengers come out of your lamps they'll see your face, whole and lovely and entirely unpunished, and they will remember it."
{n}Ilvara says, very quietly, "Thank you, Commander."
The court boos. They had money on the hands.{/n}
"Pay the ones who said whole," {n}Nocticula says,{/n} "and take her down to the cells, and give her something warm to wear. I want her fingers nimble."
{n}As the guards lead Ilvara away, Nocticula leans toward you on the throne, and her breath is warm against your ear.{/n} "Whole is crueler, you know. Broken, she'd have an excuse. Whole, every one of them will watch her choose to open that door for me with her own pretty hands. You're learning."''', c('[Leave her whole for the door.]', flags=f("next_measure", "witness_plan"))),
    n("leverage", "Nocticula", '''"Oh, both." {n}Nocticula sounds touched.{/n} "You do give the most thoughtful presents."
{n}She takes Ilvara's hands one after the other, whatever is still whole of them, and the guards hold her, and the court leans forward. It does not take long. Nocticula is very good at it. When it is done Ilvara is on her knees on the black floor with her hands in her lap like two dead birds, and her white shoes are not white any more.{/n}
"You won't be breaking any coins with those for a while. Orren will carry them for you. He's been so eager to be useful, and he still has hands, more or less." {n}She wipes her fingers on Ilvara's grey velvet.{/n} "You'll walk ahead of him and call the names. Every passenger who comes out of your lamps will see the man who sold them and the woman who kept them, and know exactly what I think of you both."
{n}The bookmaker is paying out. The hall has begun to sing something obscene about hands.{/n}''', c('[Let Orren carry the coins.]', flags=f("next_measure", "creditor_plan"))),
], "meeting_planned")

s("voices_in_glass", "Voices in the glass", [
    n("start", "Narrator", '''{n}A long table stands on the quay. At one end rests Vessa's bell. At the other, a glass of water trembles whenever the bell moves. Nocticula has recreated the arrangement exactly as her agent described it, including a crack in the glass.
She tells you the real bell rang twice during Ilvara's second demonstration. The first sound reached the room. The second appeared only as a ripple in the water.{/n}
"Vessa understood the question. She tested the boundary instead of begging us to believe she was alive."
"What did she say?"
"Not much. Words came through in the wrong order. Names arrived more clearly than sentences. I have not allowed my agent to improve them into an explanation."
{n}The dream repeats the fragments. Vessa's voice is rough and impatient. Six lamps. A door without a wall. Tomar following a wake in dry sand. A woman waiting for someone who had already died outside.
Then a phrase which Nocticula repeats without alteration: the harbor keeps the part of the journey you cannot finish alone.{/n}
"There is a rule there," {n}she says.{/n} "It may be a rule of the original passage, or something Ilvara has made her captives believe. We need to distinguish those before we give it more power by obeying it."''',
      c('"We planned around Vessa. What did she make of our question?"', "witness", requires=f("witness_plan")),
      c('"Did the surviving creditor answer you?"', "creditor", requires=f("creditor_plan"))),
    n("witness", "Nocticula", '''"She asked whether the person who sent it knew anything about ships. I have decided to take that as a compliment to its practicality."
{n}Your question had asked which part of the harbor remained unchanged when Vessa walked away from it. She answered: the names painted beneath the lamps. She had scratched out her own. By the time she reached the door, it was there again.
Then she changed the spelling. The wrong letter remained until somebody called her by the right name.{/n}
"An error persisted until corrected by a witness," {n}Nocticula says.{/n} "That is more interesting than a wall which leads you back to your footprints."
"She can affect it."
"A little. Enough to annoy Ilvara, who ended the demonstration immediately after that answer."
{n}Nocticula places a finger against the cracked glass. Its reflection shows the letter Vessa had changed, although the air above it remains empty.{/n}
"We will need someone to carry an answer through. Someone who knows which name to say and who can come back without letting the harbor borrow the journey."
"Ilvara."
"Perhaps. I am increasingly interested in making her experience the convenience she has sold to others."''', c('"Make her explain why she can leave when her passengers cannot."', "choice", flags=f("name_rule_known"))),
    n("creditor", "Nocticula", '''"She answered in person. Her name is Sere. She is sixty-two, has outlived two husbands, and informed my agent that she will not be hurried by a woman who has had centuries to make inquiries."
{n}Sere brought a letter written by her father before he took Ilvara's passage. It promised that he would meet her at a harbor whose lamps she could see from their old home. The home has been demolished. The harbor was renamed. Sere says she waited until she understood waiting was becoming her entire life, then stopped.
She does not want her father returned as a stranger expecting a child who no longer exists.{/n}
"What does she want?"
"An account. If he died, she wants to know. If he did not, she wants him told what happened while he was absent. She will not hand us her grief to beat Ilvara with."
"Does that disappoint you?"
"Enormously. Grief is the cheapest weapon in any city, and she has locked hers in a drawer. I have had to pay her instead."
{n}Nocticula has paid Sere for copies of the letter and travel records. Sere insisted on naming the price herself. She will speak to Ilvara only after someone gives her a credible answer about the passengers now inside.
Sere has kept the original. Nocticula taps the purchased copy against her palm. "An expensive woman. I had hoped to enjoy her anger. Instead I have bought her handwriting."{/n}''', c('"Honor her terms. The letter may explain what the harbor believes is unfinished."', "choice", flags=f("sere_heard"))),
    n("choice", "Nocticula", '''"Ilvara carries a return token. One half of a coin stays with her; the other is held outside by a person who expects her back. She has never entered without arranging that expectation."
{n}The half-coin rises from the table and turns in the air. Its severed edge is irregular, too distinctive to confuse with another.{/n}
"Not a soul bond," {n}Nocticula says.{/n} "Not love. A specific appointment, witnessed and paid for. She made a practical precaution into a privilege she could deny her passengers."
"We can give them return tokens."
"If someone can carry the matched halves through. The harbor will recognize the old passengers as cargo until somebody disputes that claim from inside."
"And you cannot simply order it to change."
{n}She gives you a look of magnificent displeasure.{/n}
"I can order anything. The distinction is what happens afterward. If I break the passage, we may lose everyone in it. If I take Ilvara's place without understanding her claim, I may purchase a very elaborate prison."
{n}Nocticula lowers the coin onto the table between you.{/n}
"So. We force her to carry the tokens, with a guarantee she cannot discard. Or we send a volunteer under my protection and trust Ilvara to keep the doorway open while we work. You may imagine how much I enjoy the second proposition."''',
      c('"Use Ilvara. She made this trap, and she should take the risk of opening it."', "ilvara"),
      c('"Ask for a volunteer who understands the danger. Keep Ilvara where we can watch her."', "volunteer")),
    n("ilvara", "Nocticula", '''"I thought you might reach that conclusion eventually."
{n}She does not offer to disguise the coercion. Ilvara will enter because the alternative is losing the instrument and Nocticula's protection against the people she has cheated. She will carry the tokens because her own return half will remain outside until the passengers have been accounted for.
There are limits. She may sabotage the rescue to make herself necessary. She may choose a captive whose return creates another problem. She will certainly insist that her cooperation entitles her to more than survival.{/n}
"I will give her a written answer," {n}Nocticula says.{/n} "Cooperation buys a hearing. Nothing more."
"And if she succeeds?"
"Then we decide what to do with a useful criminal who has performed one useful act. It is a category with which I have extensive experience."
{n}She lifts the coin and presses it into your palm. The dream metal is cold, though her hand is warm around yours.{/n}
"I enjoy it when you choose a sharp tool without asking me to blunt its name. Remember that when you dislike what I do with one."''', c('[Make Ilvara carry the return tokens.]', flags=f("crossing_planned", "ilvara_sent"))),
    n("volunteer", "Nocticula", '''"You are volunteering someone you have not met. That is admirably efficient of you."
"I said ask. If nobody agrees, we use another plan."
{n}She waits long enough to make certain you mean the distinction. Then she names Teren, a tiefling pilot whose work has taken him through unstable passages before. He has no special immunity to this harbor. What he has is a reputation for returning with his passengers and for refusing jobs he considers stupid.
Nocticula will buy him the way she buys anything she means to keep using: payment, a matched return token held by a witness of his choosing, and every account she has, because a pilot who has read the charts drowns less expensively than one who has not.{/n}
"He may ask me why I do not go myself."
"What will you tell him?"
"That the harbor would gain far more by holding me than by holding him. He will find that insulting. It will still be true."
{n}She studies the space where the second chair stood in the earlier dream.{/n}
"You will receive his answer before I send him. I dislike waste, and a resentful pilot is particularly wasteful. Do not begin praising me for asking. You insisted on a condition; I have accepted it."
{n}Her gaze softens just enough to make the last sentence sound less like a reprimand.{/n}''', c('[Let Teren examine the risk and choose.]', flags=f("crossing_planned", "volunteer_requested"))),
], "next_measure")

s("cost_of_return", "The price of coming back", [
    n("start", "Narrator", '''{n}You arrive in a dream of a narrow bridge. On one side is the dry harbor; on the other, a kitchen with a kettle just beginning to boil. Nocticula stands between them, holding the two halves of a coin apart.
She glances toward the kitchen, faintly offended by how ordinary it is.{/n}
"I had a pilot named Teren examine the return arrangements. He has crossed unstable passages before. He showed my agent this kitchen, which belongs to his sister. Whenever he takes a dangerous commission, he tells her when to expect him for supper."
"That is his precaution?"
"One of them. He says an appointment he wants to keep is harder for a passage to misunderstand. No ceremony, no invocation. He insists the soup matters."
"Can wanting be measured?"
"Ilvara has built a business on pretending it can. I would rather test the claim with someone who notices when he is being cheated."
{n}The kettle whistles. Nocticula silences it without removing it from the flame. You reach past her and move it anyway. She watches the gesture with an expression you cannot immediately read.{/n}
"It was only a sound," {n}she says.{/n}
"It had a reason."
{n}She looks from the kettle to the empty kitchen chair. Then she lets the room become still on its own.{/n}''',
      c('"What terms did Ilvara accept?"', "ilvara", requires=f("ilvara_sent")),
      c('"Did Teren agree?"', "teren", requires=f("volunteer_requested"))),
    n("ilvara", "Nocticula", '''"Fewer than she asked for. More than I enjoyed granting."
{n}Ilvara will carry six matched tokens and return with a count of every person she can reach. Her own return half remains with Nocticula's agent. She demanded that no one destroy the instrument while she was inside. Nocticula agreed, since destroying it would defeat the purpose of sending her.
Then Ilvara asked to retain one lamp as payment.
Nocticula refused before the agent had finished reading the request.{/n}
"I have not begun charging you for people," {n}she says.{/n} "I see no reason to let her begin charging me."
"You want the whole harbor."
"Of course. That does not make her offer less offensive."
{n}Ilvara has written the passengers' names in a hand that deteriorates as the list continues. The final name is incomplete. She says its owner entered before she took possession of the instrument and may no longer know how to answer.
Nocticula believes this much, because it is an admission which reduces the value of the thing Ilvara hopes to sell.{/n}
"We may be buying an older crime along with hers," {n}she says.{/n} "Do not let her use that to persuade you that the newer one is less real."''', c('"Keep the older passenger in the count. Unknown is not absent."', "risk")),
    n("teren", "Nocticula", '''"He called the plan stupid, then explained how he would improve it. I take that as a professional form of affection."
{n}Teren refused a sword. He asked for a length of knotted cord, the return tokens, and written descriptions of the missing passengers. He will not carry Nocticula's emblem. It would make the harbor more interested in him and might persuade the captives that they had merely acquired a new owner.
Nocticula accepted this refusal with rather less grace than she now gives it in the telling.{/n}
"He also requested a witness who does not work for me. His sister. She will hold his coin and receive the payment if he does not return."
"You agreed?"
"Yes. I would like the man concentrating on the harbor rather than on whether I intend to cheat his family."
{n}Teren's final condition is that he may turn back after inspecting the first lamp. He will not be required to finish the rescue merely to justify the cost of beginning it.
Nocticula lays out his route. He has supplied an exact signal for retreat: three pulls on the cord, followed by a pause long enough to hear the response.{/n}
"He has agreed," {n}she says.{/n} "He has also made certain we cannot honestly say he agreed to everything. I suspect you will like him."''', c('"Keep the retreat signal. If he uses it, he comes back."', "risk")),
    n("risk", "Nocticula", '''"Before we proceed, there is the matter of the door."
{n}She brings the halves of the coin together. They do not join. A narrow line of darkness remains between them.{/n}
"The stolen cloth contains the remnant of my protection. I can lend the crossing enough of that old claim to keep it open while the tokens are carried through. I cannot do that without revealing the shape of the permission. Ilvara will learn something about how my agents travel."
"A real price."
"Yes. Try not to sound delighted."
{n}The alternative is to use the instrument without reinforcement. It may hold long enough; it may not. If it fails, the person inside must choose between abandoning the captives and losing their own way back.
Nocticula has not yet chosen. She wants the harbor, wants to punish the theft, and dislikes giving an enemy knowledge she may later have to kill to contain.{/n}
"You asked for a plan worth the delay," {n}you remind her.{/n}
"And you have helped make one. Now we decide whether the plan is worth its cost."
{n}She touches your cheek, surprisingly gently, while considering an act that has nothing gentle about it.{/n}
"Ilvara gets one look at my road. You get your passengers. I shall remember who asked."''',
      c('"Reinforce it. We accepted responsibility for sending someone through."', "open"),
      c('"Keep the secret. A rescue that gives her another weapon may cost more lives later."', "closed"),
      c('"Reveal a limited permission that expires when the last token returns."', "limited", requires=("trickster",))),
    n("open", "Nocticula", '''{n}She gives you a long, cool look, then turns back toward the harbor.{/n}
"You have an expensive understanding of responsibility."
"You knew that when you asked."
"I wanted to hear whether you still possessed it when I supplied the amount."
{n}She will reinforce the old claim. Ilvara will see how it is done. The knowledge cannot be removed afterward by declaring the rescue a success.
Nocticula orders her agent to record everyone present at the demonstration, including the guards and the woman who brings the water. Nobody is arrested for watching. Every name goes into a book she keeps for people who have seen more than they should, and one day, when it suits her, each of them will be asked what they remember.{/n}
"I will need to change the permissions on three other routes," {n}she says.{/n} "People I employ will curse my name while they learn the new forms. You may take some private satisfaction in having made their work more difficult."
"I would rather take satisfaction in the passengers coming out."
"Then let us arrange for you to have something to enjoy."
{n}She kisses you once before releasing the dream, her impatience now directed toward the work instead of your answer.{/n}''', c('[Accept the disclosed secret and the stronger crossing.]', flags=f("crossing_ready", "door_reinforced"))),
    n("closed", "Nocticula", '''"That is the answer I expected from a ruler. I was less certain whether you would give it while imagining the person inside."
{n}The crossing will proceed with a shorter limit. Her agent will pull the return line at the first sign that the harbor is borrowing its visitor's destination.
The passengers may have to come out in more than one attempt. Some may be left beyond reach when the instrument exhausts itself.{/n}
"Tell whoever goes in," {n}you say.{/n}
"Already part of the instructions. I have no use for a heroic surprise halfway through an extraction."
{n}She sets the halves of the coin on opposite sides of the bridge. The darkness between them remains.
She draws the return line between them, stopping short of the far coin. Her nail leaves a white score in the stone.{/n}
"When we hear the account," {n}she says,{/n} "do not ask me to tell it more kindly because you were prudent. I dislike prudence that cannot bear to recognize its own casualties."''', c('[Keep the route secret and require an early withdrawal if it fails.]', flags=f("crossing_ready", "door_unreinforced"))),
    n("limited", "Nocticula", '''"An expiring permission is still a permission she can study."
"Give it a condition she cannot reproduce. The matched tokens are numbered. Let the opening depend on the numbers still owed a return. When none remain, it ends."
"You are assuming we can identify every token the harbor accepts."
"Then count them together before entry. Leave no blank place she can fill later."
{n}Nocticula examines the proposal. It requires a new pattern drawn around the old cloth, two witnesses keeping the count, and a separate return line for the carrier. Ilvara can still observe the pattern. What she cannot keep is the exact unfinished obligation that powers this use of it.
The arrangement will be weaker than lending Nocticula's full protection, stronger than trusting the instrument alone.{/n}
"It also prevents me from keeping the door open after the last passenger leaves," {n}she says.{/n}
"You wanted the harbor. You may have to choose what remains of it."
{n}Her smile is slow and dangerous.{/n}
"There you are. I wondered when your clever solution would begin charging me rent."
{n}She sends for her agent's notes and begins drawing the pattern around the six names. Twice she stops to ask you to repeat the proposed limit. The second time, she catches an ambiguity and makes you choose exactly what the last token must finish.{/n}''', c('[Prepare the counted, limited reinforcement.]', flags=f("crossing_ready", "door_limited"))),
], "crossing_planned")

s("return_count", "The count at the door", [
    n("start", "Narrator", '''{n}The Gift sets you down barefoot on wet black rock, at night, in the wind, and the sea is real.
It is a coast of the Midnight Isles: a cliff going up into darkness, surf exploding white against its foot, salt on your lips. Off the rocks her court's boats ride the swell with their lanterns lit, a dozen of them, crowded with courtiers who have paid to watch. You can hear the betting from here.
In the cliff face, where the waves strike, there is a door. It is not carved. It is a place where the rock has stopped being rock: black and wet and breathing slightly, as though the cliff had a mouth and had decided, for tonight, to keep it open.
Nocticula stands on the highest rock in front of it, barefoot like you, in a black gown the spray cannot wet. She looks bored, and delighted, at once.
On the nearest boat a fat demon in a fur cloak is shouting odds across the water to the next: three to one the door eats somebody, five to one it eats the magician, evens that the Lady gets bored and leaves before the end. A succubus in the bow is selling seats nearer the rocks.
Rhez kneels on a flat stone beside the door. In front of her lie half-coins in a row, each beside a slip of paper weighted with a pebble. Names. She is counting them under her breath.{/n}
"Everything that crosses under my flower is mine," {n}Nocticula says without turning, loudly enough that the nearest boat hears it and cheers.{/n} "That includes whatever walks out of that rock tonight. Remember I said so, darling. Later, someone will try to call it something else."
{n}From inside the door, before anything appears, comes the sound of a bell: a small brass bell, the kind a shipwright rings to test a mast, struck once and then again, faint, from somewhere very far inside the rock.{/n}
"There. Someone in there still has her wits." {n}She smiles at the door.{/n} "Let's go and fetch my property."''',
      c('"Send Ilvara in."', "ilvara", requires=f("ilvara_sent")),
      c('"Send Teren in."', "teren", requires=f("volunteer_requested"))),
    n("ilvara", "Narrator", '''{n}Ilvara goes in on a chain. Rhez holds the other end. At the first step past the door her white shoes blacken with sand, and she stops and looks down at them, and Rhez jerks the chain.
Through the door you can see it now: a dry harbor under a low stone sky, sand and mooring posts, and lamps on the posts, burning with nobody to tend them. Five. You count them. Five.
At the first lamp Ilvara speaks a name, breaks a half-coin against its mate, and steps back. The flame stretches into a woman, big, scar-armed, a brass bell clenched in one fist so hard her knuckles are white. Vessa. She looks at Ilvara, and then out through the door at the lanterns and the boats and the Lady on the rock.{/n}
"Walk," {n}Rhez calls.{/n}
{n}Vessa walks. She does not run. She walks past Ilvara as though Ilvara were a post, out onto the wet rock, and stands in the spray looking up at Nocticula, and Nocticula looks back at her the way one looks at a parcel that has arrived intact.
At the second lamp, Ilvara's hand goes to her sleeve. Rhez sees it. In two strides she has Ilvara's wrist bent back, and a brass pin, one of the six from the lens, drops out of the grey velvet onto the sand.{/n}
"She wanted to keep a claim on it," {n}Nocticula says.{/n} "One pin. Enough to open it again some day, from somewhere else, when I'd stopped watching." {n}She sounds impressed.{/n} "Rhez, the pin. Ilvara, the next lamp."''', c('"Go on. The next lamp."', "strain", flags=f("ilvara_pin_taken"))),
    n("teren", "Narrator", '''{n}Teren goes in with a knotted cord tied round his waist and Rhez holding the other end. He is the volunteer from the old plan, the man who asked to carry the coins because his sister was in one of the lamps, and he has no weapon and no illusions. Through the door you can see the dry harbor: sand, posts, lamps burning with nobody to tend them.
At the first lamp he kneels and matches a coin, and Vessa steps out of the flame with a brass bell in her fist. She does not trust him. He tells her what the bell is for, lets her look at the token, and moves out of her way when she decides to walk.
At the second lamp the cord pulls itself tight, as if the harbor were trying to reel him in. He gives three pulls. Rhez answers. He comes back to the threshold, one foot on the rock, breathing hard.{/n}
"He used the rope," {n}Nocticula says.{/n} "Ilvara called it cowardice. Rhez told her she was welcome to go in instead." {n}She smiles as he turns back toward the lamps.{/n} "And now he's going back. I like him. I shall probably have to buy him."''', c('"Go on. The next lamp."', "strain", flags=f("teren_returned_once"))),
    n("strain", "Nocticula", '''"The last lamp has two names in it. Do you see?"
{n}You see. The fifth lamp's flame is doubled, like a candle seen through tears, and inside it two men occupy the same narrow space: an old one in a coat forty years out of fashion, and a young sailor with a broken nose. Ren and Tomar. Rhez reads both names off the same slip of paper, one written over the other.{/n}
"Sold twice," {n}Rhez says.{/n} "The old one has two names on him, Lady."
"Then he's twice as mine."
{n}The coin breaks. Both men try to step out at once, and cannot; the old one reaches past the young one's shoulder and finds the same flame again. The door shudders. The black rock around it is closing, slowly, the way a mouth closes on something it has decided to swallow, and you can hear it grind. Inside, the sand has begun to run toward the walls.{/n}
"It's eating," {n}Nocticula says, with interest.{/n} "Choose, darling. Quickly. I can burn my flower into that door so that it holds, and then everyone who ever finds it will see my name on it. I can let it close narrow and take what it takes. Or something cleverer, if you have something cleverer."''',
      c('"Hold it with your flower, as we agreed."', "reinforced", requires=f("door_reinforced")),
      c('"Let it close narrow, as we agreed."', "unreinforced", requires=f("door_unreinforced")),
      c('"One crossing per coin, as we counted."', "limited", requires=f("door_limited"))),
    n("reinforced", "Nocticula", '''"Into a door any fool can find afterwards?" {n}For an instant she looks at you as if you had asked her to give away a jewel. Then she laughs.{/n} "Very well. Let them find it. Let them find it with my name on it."
{n}She steps down from her rock and lays her palm flat against the cliff beside the closing door, and the stone screams. There is no other word for it. Black fire runs out from under her hand in the shape of a flower, petal by petal, burning itself into the rock, and where it burns the closing stops. The door holds, trembling, open just wide enough.
Rhez calls both names, separately, the old and the young. Ren comes out first, then Tomar, sprawling on the wet stone; Tomar's nose breaks again on the rock and he lies there bleeding into the surf and laughing. Ren tries to go back for a bag he left by the lamp. Vessa catches him by the collar and swears at him until he stops.
On the cliff face the flower is still burning, slowly, and it will burn there, Nocticula tells you, as long as the cliff stands.{/n}
"There. Every thief on every sea will know whose door that is." {n}She shakes out her hand; the palm is blistered black.{/n} "Worth a glove, I suppose. Rhez, how many?"
"All of them, Lady."''', c('[Keep the door with her name burned on it.]', flags=f("crossing_finished", "chart_intact"))),
    n("unreinforced", "Narrator", '''"Narrow," {n}Nocticula repeats, and her eyes go bright.{/n} "Let's see what it charges."
{n}The door goes on closing. Rhez calls the names, both of them, over and over. Tomar comes out first, flung onto the rock as though the harbor had spat him. Ren follows the sound of his own name, half blind, and the rock is closing on him, and Vessa, who has stood in the surf with her bell since she came out, jams the bell sideways into the gap with her hand still round it.
The brass flattens. The rock closes on it, and on her fingers, and you hear them go: a sound like someone stepping on a bundle of sticks. She keeps hold. Ren gets his shoulder through, and his hip, and his heel, and the door shuts behind him with a noise like a jaw. In Rhez's hand the lens cracks across.
Vessa draws her arm back. What is on the end of it is not quite a hand any more.{/n}
"Oh, that was worth seeing," {n}Nocticula says.{/n} "She jammed her own hand in my door to save my property. Rhez, see she's splinted; I don't waste anything that does that." {n}She looks at the closed rock and the cracked lens, and shrugs.{/n} "And the route's gone. Ah, well. I've lost doors before. I've never had one bite so prettily."''', c('[Let the door take its toll.]', flags=f("crossing_finished", "vessa_injured", "chart_lost"))),
    n("limited", "Nocticula", '''"Count it. Yes. Clever."
{n}Rhez refuses to count two people as one merely because the lamp did. She breaks the last half-coin into three pieces on the stone, one for the old man, one for the young, and one she throws through the door into the harbor, to stay there. She calls the names separately. Ren comes out. Tomar comes out. The third piece of coin lies glinting on the sand inside as the permission runs out.
The door closes. Not violently: it simply stops being a door and is rock, wet and black and ordinary, and the sailcloth flower in Rhez's pack falls apart along its old seams like rotten silk.{/n}
"There. Nobody will ever open it again." {n}Nocticula lays her hand on the closed rock.{/n} "Including me. You kept the price so small that I can't keep the door afterward. I knew that was the limit." {n}She looks at you sideways.{/n} "Knowing a price doesn't oblige me to enjoy paying it. Remember that I paid it. I will."
{n}Out on the water the boats have gone quiet. The courtiers who bet on the door eating somebody are paying out, sullenly, to the ones who bet it would simply stop. Nobody bet on that. Nocticula notices, and laughs, and the boats laugh with her, a beat late.{/n}''', c('[Let the door close for good.]', flags=f("crossing_finished", "chart_limited"))),
], "crossing_ready")

s("after_the_lamps", "After the lamps go out", [
    n("start", "Narrator", '''{n}Nocticula brings no image of the harbor to the next dream. She brings a list of requests.
Tomar wants his wages for the voyage. Vessa wants the bell and an explanation of what happened to the fittings she carried. Ren wants to know why everyone insists his daughter is an old woman. Orren wants immunity again, apparently encouraged by the survival of people who might testify against him.
Nocticula reads the last request twice, enjoying it more the second time.{/n}
"It is almost admirable. He has mistaken the absence of immediate execution for an invitation to improve his terms."
"Will you execute him?"
"For stealing a navigational instrument from a slaver? I should have to reorganize half my city if I began punishing theft according to its victim's complaint. He will surrender the profit he concealed. Then he may attempt to become somebody else's difficulty."
{n}She sits on the edge of a low fountain. The water reflects a sky which the room does not possess.{/n}
"You wanted people returned. Here they are, making claims on the world. It would be easier if gratitude made them obedient."
"Would you prefer them obedient?"
"Often. You may notice I do not always receive my preference."''',
      c('"How is Vessa\'s hand?"', "injury", requires=f("vessa_injured")),
      c('"What does Vessa want to do next?"', "yard", forbids=f("vessa_injured"))),
    n("injury", "Nocticula", '''"Better than the healer feared. Worse than she would like. She can hold a cup. She cannot yet hold a hammer."
{n}Nocticula has paid for treatment and an assistant at the repair yard. Vessa chose the assistant. She rejected the first person offered because he kept telling her how fortunate she was.
The second asked where she wanted the tools. He remains employed.{/n}
"She sent a message for you," {n}Nocticula says.{/n} "Rhez told her someone outside the city had helped choose the plan. Vessa says that if you ever commission a ship, you should pay the carpenter before praising the voyage."
"That seems fair."
"It seems pointed. Fairness was not among the qualities she mentioned."
{n}A second account lies beneath the healer's bill. It charges for a hammer with a wider handle. Nocticula has marked it for payment.
You ask whether the message displeased her.{/n}
"A little. I have paid for that woman's survival, her treatment, and now the tools with which she intends to overcharge my captains. I expect something magnificent from her first ship."
{n}She lets the water run over her fingers, then flicks the drops away.{/n}''', c('"Keep her account with ours. Do not let the successful return erase it."', "ren")),
    n("yard", "Nocticula", '''"Open her yard. Charge higher prices to captains she distrusts. Replace the fittings Ilvara lost. In that order."
{n}Vessa has refused an invitation to tell her story at a merchant's gathering. She suspects the audience would remember the miraculous rescue and forget to pay their invoices. Nocticula seems to consider this a sound assessment of merchants.
She has accepted payment for a technical account of the harbor. Her drawings show the places where sound moved differently from light, where footsteps repeated, and where the lamps' names could be changed. She has written a warning across the first sheet: tested once, under threat of death, do not call this a reliable method.{/n}
"You bought the account?"
"Yes. She knew its value. I would have been disappointed if she had given it away."
"And what will you do with it?"
"Read it. Then decide whether anybody else should be allowed to."
{n}Nocticula folds the drawings inward, hiding the measurements before you can finish reading them. Her thumb rests on Vessa's price at the bottom of the page.{/n}''', c('"What happened when Ren learned how long he had been gone?"', "ren")),
    n("ren", "Nocticula", '''"He accused Rhez of lying. Then asked her to repeat the date. Then became very quiet."
{n}Ren is Sere's father. Nocticula's agents found enough records to verify it. She did not trouble the daughter for a childhood password; a woman who has buried two husbands does not open like a chest, and Nocticula does not waste a lever she may need later.
Sere agreed to receive a letter before deciding whether to meet him. Ren wrote three. He destroyed the first because it addressed her as a child. The second contained so many explanations that he could not find a greeting. The third asked what name she preferred to be called now.{/n}
"She answered that one," {n}Nocticula says.{/n}
"Will they meet?"
"She has proposed a place. He has agreed. That is as far as the account goes."
{n}The fountain changes. Its reflection briefly shows a harbor window, then a demolished wall, then only the room again. Nocticula has forgotten to close the image.{/n}
"I could have given him the dream of the daughter he remembered," {n}she says.{/n} "It would have been considerably less painful."
"For whom?"
{n}She looks at you and does not answer quickly.{/n}
"An irritating question. You have acquired a talent for them."''',
      c('"You let them have the difficult answer. That matters to me."', "matter"),
      c('"A comforting illusion would have been another way to keep him."', "keep")),
    n("matter", "Nocticula", '''"Be careful. You are approaching gratitude on someone else's behalf."
"I said it matters to me."
{n}She considers the correction, then inclines her head a fraction.{/n}
"Accepted."
{n}You sit beside her. The fountain is narrow enough that your knees touch. She does not move away, but she does not let the closeness become evidence in the argument either.{/n}
"I have done worse things than Ilvara," {n}she says.{/n} "Do not build an understanding of me out of one rescue that served my interests."
"I am trying to understand this choice."
"Then understand that it pleased me to deny her the final explanation. She wanted to be the only person who could tell her passengers what had happened. Now they have one another, and she has lost something she valued."
{n}She catches a floating scrap of Ilvara's advertisement from the fountain. The ink runs between her fingers. The list of promised destinations comes apart last.
When she wipes her hand on your sleeve, she is smiling.{/n}
"You could have made the water vanish."
"I could have. You were sitting so conveniently near."''', c('[Stay beside her while the last of the ink dissolves.]', "ilvara_next", flags=f("motive_heard"))),
    n("keep", "Nocticula", '''"Yes. It would."
{n}She turns toward you, her expression suddenly sharper.{/n}
"You say that as though you have discovered the secret of my entire existence. I know what an illusion can keep. I also know what people willingly return to. You have done both: accepted what I offered, and asked me to change it."
"And you have sometimes agreed."
"Sometimes. Do not become sentimental about the frequency."
{n}For a moment the conversation stands close to a quarrel. Then she looks down at your hand resting on the fountain's edge and lays hers beside it, without closing the space.{/n}
"I let him write because I wanted to know whether he could bear an answer from someone who no longer needed the man he remembered being. It is not a question I often hear asked honestly."
"Is that why you told me?"
"Perhaps. Perhaps I wanted to see whether you could avoid making the story entirely about yourself."
{n}Her glance is a challenge, and her hand stays where it is, the nails resting lightly on your knuckles like a promise of what they could do.{/n}''', c('[Take her hand without claiming the last word.]', "ilvara_next", flags=f("illusion_challenged"))),
    n("ilvara_next", "Nocticula", '''"We still have Ilvara."
{n}The name returns the evening to its unfinished business. Nocticula has not promised the magician freedom. She has promised a hearing after the passengers were accounted for.
Ilvara has requested your presence by name. She believes you are the source of the limits Nocticula placed upon the rescue, and hopes to turn those limits into protection for herself.{/n}
"I will hear her before I decide what becomes of her," {n}Nocticula says.{/n} "You can hear the account here afterward and tell me what you think. If you want to propose a condition before the hearing, now is the time."
{n}You point out that she has already decided something.{/n}
"That she will not leave with my old permission intact. Beyond that, I am prepared to be persuaded. Not cheaply."
{n}She rises from the fountain and offers you her hand. Her other hand keeps Ilvara's petition folded against her hip.{/n}
"I hope you have enjoyed learning what happens after a successful rescue. People become remarkably demanding when they are allowed to continue living."''', c('"Hear her. Then we decide what she can still be trusted to do."', flags=f("aftermath_heard"))),
], "crossing_finished")

s("another_place", "A place not promised", [
    n("start", "Narrator", '''{n}Her dressing room is off the Harem, at the top of a stair of black glass, and it smells of powder and hot curling irons and blood.
The blood is in a hatbox. The hatbox sits on her dressing table between the comb and the pots of kohl, lid on, and a dark stain is spreading slowly through the bottom of the pasteboard onto the marble. Nocticula is at the mirror, putting in an earring. She does not look at the hatbox. She looks at you, in the glass.{/n}
"You're early. Good." {n}Music comes up the stair from the Harem: low strings, a drum, a woman singing in a language you almost know. There is room to dance between the dressing table and the window, and she has cleared it.{/n} "One dance first. Then I'll tell you what's in the box."
"I can guess what's in the box."
"You can guess what. Not who." {n}She holds out her hand. A folded blue note lies beside her comb; she slides it under the hatbox with one finger, where you cannot read it.{/n} "One dance. I've had a tiresome day of being sold, and I want to be held by something that isn't for sale."''',
      c('[Take her hand. Leave the note under the box.]', "dance"),
      c('"Tell me first. I won\'t be good company while I wonder."', "refused_dance")),
    n("dance", "Nocticula", '''"There. A decision made without consulting anyone."
{n}She pulls you into the cleared space. At first she leads, turning before the music is ready, so that you stumble; you follow once, then hold your place at the next turn, and her hand presses harder on yours, nails in.{/n}
"You're anticipating me."
"You keep changing the measure."
"The singer is quite certain of it. I had her sister's tongue cut out once for being wrong. She's been very certain ever since."
{n}You listen. The phrase repeats. This time you turn on its last note and leave her a choice between following and stopping, and she follows, her skirt brushing your knee, and laughs against your ear.{/n}
"I could change the song."
"Then I'd know you needed to."
{n}For several steps she gives you nothing but the weight of her hand. Then she turns you, hard, toward the window, leaving no room at all for the next step. You catch yourself on the sill, and her palm comes down beside yours, and her body comes down behind it.{/n}
"You see," {n}she says against your neck,{/n} "I don't need to."
{n}You kiss her. She lets you finish, and bites, and lets you go. The song ends. She goes back to the dressing table, lifts the hatbox, and draws out the blue note from beneath it.{/n}
"Now you may ask."''', c('[Follow her back to the dressing table.]', "note")),
    n("refused_dance", "Nocticula", '''{n}Her hand drops.{/n} "Then wonder."
{n}She sits at the dressing table and takes up the comb. It catches on a strand of hair; she works it free, watching you in the mirror, and goes on, with infuriating care, while the stain under the hatbox spreads another finger's width across the marble.
You stay by the window. From there the note would be easy to reach if you leaned past her.{/n}
"You could have put that away before I came."
"I could have made a dream in which you wanted exactly what I intended. I've acquired expensive tastes." {n}A stroke of the comb.{/n} "I asked you for one dance. I don't ask. Remember what it bought you, the one time I did."
{n}You let the next phrase of the song go by. When the singer begins again you sit on the end of the couch, and she watches your reflection settle.{/n}
"I'm staying," {n}you say.{/n}
"I can see that. I'm deciding whether to be pleased about it." {n}She finishes her hair, sets down the comb, and draws the blue note from under the hatbox. The place where she offered you her hand stays empty between you.{/n}''', c('[Listen when she chooses to speak.]', "note")),
    n("note", "Narrator", '''{n}She unfolds the note and holds it up to the mirror so that you can read it backwards and forwards at once. Blue paper; a fine, educated hand.{/n}
"From Ilvara. From my cells. She's been bribing my jailers with promises, which is all she has left, and they've been carrying her little letters up the stairs, which I shall deal with later." {n}She smiles at the stain on the marble.{/n} "Partly dealt with."
"Who did she write to?"
"Everyone. My servants, my lovers, my useful acquaintances. She asked whether any of them would like to negotiate with her without me in the room. She asked what each of them wanted." {n}Nocticula sets the note down.{/n} "She asked your price too. Through a messenger, very politely: what would the Commander take to look away when her door was opened? I told her messenger it was his head."
{n}She lifts the lid of the hatbox a finger's width, and lets it fall again. You have seen enough.{/n}
"She thinks everyone who shares my bed is either paid for it or waiting for revenge. It hasn't occurred to her that anyone might come back to it for the teeth." {n}She turns from the mirror.{/n} "Ask me who answered her. That's the fun part."''',
      c('"Did she write to Laulieh?"', "laulieh", requires=f("parent_laulieh")),
      c('"Did she offer Laulieh the way out you promised her?"', "departure", requires=f("parent_laulieh_departure")),
      c('"Who took her offer?"', "courier")),
    n("laulieh", "Nocticula", '''{n}The door behind you opens without a knock. A succubus in green comes in sideways, curtsying as she comes, so deep that her horns nearly brush the floor, and when she rises there is a smear of dried blood along one cheekbone that she has plainly left there on purpose.{/n}
"My lady!" {n}Laulieh's eyes find you, widen theatrically, and narrow with interest.{/n} "And my lady's crusader, in the flesh. Or the dream of the flesh. Fie, I can never tell with the Gift." {n}She curtsies again, to you, a fraction less deeply.{/n} "Did my lady like the box?"
"Tell the Commander what you did, darling."
"Ilvara sent me a messenger. I sent back the parts that were still talking." {n}She beams.{/n} "Well. I sent them to my lady, actually. The parts that weren't talking, I kept. A girl must have a hobby."
"She offered you something."
"Oh, everything. Gold, a seat at her harbor, freedom." {n}Laulieh laughs, high and bright.{/n} "Freedom! I'd hate it. Nobody would watch. In the Abyss you serve whoever has the most power, and the woman in the white shoes has a cell and a hole in a cliff. My lady has a city." {n}She sinks down beside the dressing stool like a cat and lays her chin on her lady's thigh.{/n} "Does my lady want to know what I'd like instead? Since everyone's asking."
"Laulieh is mine to disappoint," {n}Nocticula tells you, stroking her hair the way one strokes a favorite hound.{/n} "Ilvara didn't understand that. Her messenger does now."''', c('"She\'s earned her answer. Give it to her later."', "others", flags=f("laulieh_request_heard"))),
    n("departure", "Nocticula", '''"Indirectly. Ilvara heard about a promise I made, in a bargain you'll remember: that Laulieh goes where I go, out of the Abyss itself if it comes to that." {n}The door opens without a knock; a succubus in green slips in, curtsying, with dried blood on one cheekbone.{/n} "And she thought she could sell her a cheaper way out."
"My lady." {n}Laulieh's curtsy takes in the room, and you, and ends at her mistress's feet.{/n} "The white-shoe woman offered me a door. Her own door. Out of the Abyss, out of service, anywhere I liked." {n}She laughs.{/n} "Anywhere I liked! As if there were anywhere worth going that my lady isn't. I go where power goes, crusader. I don't run from it. I carry its train." {n}She tilts her head at the hatbox.{/n} "So I sent her messenger back. Most of him."
"Laulieh is mine to disappoint," {n}Nocticula says, without looking at her.{/n} "Not Ilvara's. If anyone is going to sell that girl a lie about her future, it will be someone who can afford to make it true." {n}She drops a hand onto Laulieh's head, carelessly, the way one rests a hand on a favorite hound.{/n} "The promise stands in exactly the words I gave it. Not one syllable wider. I have never in my existence widened a promise because somebody wept at it, and she didn't weep. She brought me a hatbox."''', c('"Then keep the promise in its own words."', "others", flags=f("laulieh_request_heard"))),
    n("courier", "Nocticula", '''"A courier named Senet. A charming man; he carried letters between houses for me for years. Ilvara offered him a route through her harbor that would let him deliver before he'd left, which is the sort of thing couriers dream about. He said yes."
"Where is he?"
"On the palace gate." {n}She says it the way she might say in the garden.{/n} "You came past him. You didn't look up. Most people don't, the first time."
{n}The door opens without a knock. A succubus in green slips in, curtsying so low her horns almost touch the floor, with a smear of dried blood along one cheekbone that she has plainly kept for effect.{/n}
"My lady's courier!" {n}Laulieh's eyes go to you, and widen, and narrow.{/n} "I did the gate. Did the crusader like the gate? I did the nails myself; the guards never get the spacing right." {n}She curtsies to you.{/n} "And then her messenger came for his answer, and I sent back the parts that were still talking. That's the box. Fie, it's leaking. My lady's marble."
"Leave it," {n}Nocticula says.{/n} "The Commander should see what it looks like when someone takes an offer. Senet took one. The gate doesn't carry letters."''', c('"Let the gate answer anyone else she writes to."', "others", flags=f("courier_request_heard"))),
    n("others", "Nocticula", '''{n}She comes round the dressing table. Only one earring is in; she turns the other between her fingers while she looks at you.{/n}
"Ilvara asked your price. You know what I told her messenger. Now I want to know what you'd have told him." {n}She steps closer.{/n} "Offers will come for you. They always come, for anything of mine. Gold, bodies, power, a door out. Someone will want what I've marked and offer you something for a look at it." {n}She lays the cold earring against your lower lip.{/n} "I'm not jealous, darling. I'm a Demon Lord, not a farmer's wife. I shan't weep if you take someone else to bed. But I do want to know what becomes of the people who make you offers."
"And if our interests collide?"
"Then we'll have a war. A small, private one. I'll enjoy it enormously; it's so much better than sulking over a kiss." {n}She fastens the second earring at last, by touch, without looking away from you.{/n} "Senet's gate has room on it. So does Laulieh's hatbox. I mention it only so you know where things go, in my house, when they're offered for." {n}She smiles.{/n} "Well? Who decides what the offerer pays?"''',
      c('"Every offer made for me comes to you. You decide what the offerer pays."', "promise"),
      c('"My other rooms stay mine."', "private")),
    n("promise", "Nocticula", '''"Oh, good." {n}She looks genuinely delighted, as though you had handed her a gift wrapped in someone else's skin.{/n} "Every offer, to me. Every one. And I decide." {n}She takes a fistful of your collar and pulls you against her, and kisses you with none of the ceremony she spends on her court; it is a kiss like a hand closing on a throat.{/n} "You realize what you've done. Every fool who wants you will end up at my gate. Laulieh is going to adore you. She does so love having something to do with her evenings."
{n}She lets you go, and turns back to the mirror to put in the second earring, and in the glass her eyes stay on you the whole time.{/n}''', c('[Let every offer go to her.]', flags=f("others_discussed", "conflicts_named"))),
    n("private", "Nocticula", '''"Keep them, then." {n}Her contempt is perfectly cheerful.{/n} "Keep your rooms. Keep your little locked drawers and your letters and your lovers. I'll know what's in them before you do." {n}She fastens the second earring, unhurried, watching you in the mirror.{/n} "I don't need to be told things, darling. I'm always the best-informed person in any room, including the rooms I'm not in. You may have your privacy the way a mouse has privacy in a house with a cat: it's real, it's yours, and I'm choosing not to eat it."
{n}She turns her head so that the earring catches the light.{/n} "And if one of your private friends plans to kill me, I'll expect a warning. Mine plan it constantly. I'll warn you when one of them grows competent."''', c('[Keep your rooms your own.]', flags=f("others_discussed", "privacy_named"))),
], "aftermath_heard")

s("hearing", "A hearing without absolution", [
    n("start", "Narrator", '''{n}The court has been waiting days for this, and you can feel it before you see it: a heat in the throne hall like the inside of a mouth.
Every step of the dais is packed. Demons hang from the pillars by their tails and their claws. Mortal slaves kneel along the walls holding up trays of wine and slates and chalk, because tonight everyone is betting, and the bookmaker, the same tiefling as on the night of the trick, has set up a lectern at the foot of the stairs and is bellowing odds in a cracked voice.{/n}
"Six to one, the cauldron by midnight! Six to one!"
{n}Below the dais, where a judge would stand, there is a space of black floor with nothing in it but you.
A courtier on the lowest step, a horned thing hung with gold rings, leans down and offers you a slate and chalk, the way a host offers a guest the wine.{/n}
"Crusader. Will you lay something? Everyone wants to know what the Lady's pet thinks the Lady will do."
{n}Nocticula's voice comes down from the throne, lazily.{/n} "The Commander doesn't bet on my sentences. The Commander gives them. Take your slate away before I give you one."
{n}The courtier withdraws so fast that he falls off his step, and the hall laughs at him gladly, the way people laugh when the knife has passed them by.
They bring Ilvara in chained at the throat and wrists. Her white shoes are white again. Someone has cleaned them for the occasion, and you understand that this is part of it. She wears grey silk gloves too, new ones, buttoned at the wrist; whether anything is wrong with the hands inside them you cannot tell, and the court is betting on that as well. She is walked to the space below the dais and left beside you, close enough that you can smell her: lavender, and under it the cells.{/n}
"Lady in Shadow." {n}She curtsies, chains and all.{/n} "Commander."
"Traitors," {n}Nocticula tells the hall, as if continuing a conversation,{/n} "are my favorite entertainment. I take great delight in punishing traitors. Nothing brings me more satisfaction. And this one isn't even mine; she simply stole a piece of me and set up shop with it. That's worse. That's an insult with a shop attached."
"The conditions," {n}Nocticula says, and the hall falls silent so fast you hear a goblet ring on the floor somewhere at the back.{/n} "Since you all pretend to forget them. First, I will be the one who passes the sentence. Naturally, I will listen to the Commander's opinion, but I won't allow anyone to ruin my fun. Second, the Commander gives me that opinion now, quickly, because any game that drags on too long soon becomes a chore." {n}She smiles down at you.{/n} "And if it bores me, I'll choose my own sentence, and you will all wish the Commander had tried harder."
{n}The court roars. The bookmaker chalks with both hands.{/n}
"Six to one the cauldron! Seven to two she's a lamp by morning! Evens on the crusader being sick on the floor!"
{n}Nocticula lifts a hand, and he stops as if strangled. She looks down at the woman in chains with open, affectionate interest.{/n}
"I've a mind to join in. Perhaps I'll even make a bet, Ilvara, on how much longer you'll live. It's going to be very entertaining." {n}She holds out her hand without looking, and a slave puts a slate in it; she writes something, and turns it face down on the arm of her throne.{/n} "There. Nobody may see it until it's over. I so rarely lose."
{n}Ilvara lifts her chin. The chains chime.{/n}
"The passengers lived, Lady," {n}she says to the throne, clearly enough that the whole hall hears.{/n} "Every one of them. Whatever else I did, they lived, because of my harbor."
"Because I made you open the door." {n}Nocticula does not raise her voice.{/n} "Gratitude is wasted on you; I've stopped offering it." {n}She settles back.{/n} "Commander? Before you give me your sentence, you may question her. Briefly. Entertainingly. In front of everyone. Make it worth my evening."''',
      c('[Break her before the court. Intimidate, DC 32.]', check=dict(Skill="SkillKnowledgeWorld", DC=32, Success="contradiction", Failure="incomplete", CommanderOnly=True)),
      c('"When did you first sell someone who couldn\'t leave?"', "date"),
      c('"Ask the court which of them bought from her."', "business", requires=("trickster",))),
    n("contradiction", "Nocticula", '''{n}You walk up to her. You do not touch her; you do not need to. You stand close enough that she has to tilt her head back to keep looking at you, and you tell her, quietly, so that the front rows lean in to hear, what you know.
The voyage when a passenger did not come back. The relatives who came asking. How, when they stopped coming, she raised the price of keeping him. Not a mistake. Not an accident inherited from some older maker. A price, charged for the very thing she says she never meant.{/n}
"You charged for the captivity," {n}you say.{/n} "Tell them."
{n}She holds it for one long breath. Then her eyes go past you to the throne, and whatever she sees there breaks her.{/n}
"I charged for it," {n}Ilvara says. Her voice cracks down the middle.{/n} "When they stopped asking, I charged more. Nobody was coming. It was cheaper to keep them."
{n}The hall howls. It is less a sound than weather. Someone throws a goblet, and it bursts on the floor at Ilvara's feet and splashes her clean white shoes with wine.{/n}
"There," {n}Nocticula says, delighted.{/n} "Now she's dressed for it."''', c('"Let the whole hall remember that."', "terms", flags=f("hearing_proof"))),
    n("incomplete", "Narrator", '''{n}You go at her, and she holds. You press her on the lost voyage and she corrects your dates, sweetly, in front of everyone, by a harbor calendar you have never heard of. You press her on the relatives and she weeps, beautifully, for exactly as long as is useful, and stops. You raise your voice and she lowers hers, so that the hall must hush to hear her and she seems the calmer of the two of you.
Somewhere at the back a demon begins a slow handclap. Others take it up. The bookmaker bellows new odds, on you now.{/n}
"Oh, she's good," {n}Nocticula says over the jeering, with real pleasure.{/n} "Isn't she good? I told you she was a performer." {n}She leans down toward you.{/n} {n}Ilvara inclines her head to you, very slightly: one performer to another, after a scene that went her way. It is the most insolent thing anyone has done in this hall tonight, and the court adores her for it.{/n}
"Never mind, darling. You don't have to break her. You only have to sentence her. She's about to learn that composure is the most expensive thing a woman can wear in this hall."''', c('"Then the sentence will break her for me."', "terms", flags=f("hearing_uncertain"))),
    n("date", "Nocticula", '''"Oh, a good question. Answer it, Ilvara. Loudly."
{n}Ilvara answers. In her second season working the harbor, she says, a passenger's return witness died: the person outside who held the other half of his coin. Without the witness the harbor would not let him out. She tried to put a hired clerk in the witness's place. The harbor would not accept a man nobody believed in. So she left the passenger where he was, in his lamp, while she looked for another way.{/n}
"And while you looked?" {n}you ask.{/n}
"I kept selling passage," {n}Ilvara says.{/n} "The harbor had to pay for itself."
{n}The hall does not howl at that. It laughs, which is worse: a long, knowing laugh, the laugh of people who have all done exactly that, and know what it costs, and are delighted to watch someone else made to pay.{/n}
"She kept the harbor going," {n}Nocticula says,{/n} "until a solution could be found." {n}She lets the phrase hang until the laughter dies.{/n} "I've heard that defense from governors with excellent reputations. I ate two of them." {n}She turns the face-down slate a quarter turn on the arm of her throne, idly, without looking at it.{/n} "Neither of them tasted of remorse either."''', c('"She knew. Sentence her knowing it."', "terms", flags=f("hearing_limits"))),
    n("business", "Nocticula", '''"Ask the court?" {n}Nocticula's eyes go wide with pleasure.{/n} "Ask the court. Yes. Do."
{n}You turn your back on Ilvara and face the steps: the packed silks, the jeweled horns, the slates and the wine.{/n}
"Which of you bought from her?" {n}you ask them.{/n} "Passage. A berth. A lamp. Which of you knew what the lamps were?"
{n}The hall goes very quiet.
In the silence three courtiers find, at the same moment, that they would rather be standing somewhere else. One is a horned demon in gold; one a mortal woman with a jeweled collar; one a succubus whose wings close round her like a cloak. They move only a little. Everyone sees.{/n}
"Oh, look," {n}Nocticula says softly.{/n} "Look at them, suddenly finding the floor so interesting." {n}She orders nothing. She only looks at the three of them for a long moment, and smiles, and then turns back to you.{/n} "I'll remember their faces. You've given me three new games, darling." {n}The three courtiers have gone the color of old ash. Nobody near them will stand within arm's reach now; the crowd has opened round each of them like water round a stone.{/n} "Now give me the first."''', c('"Ilvara first. Then them."', "terms", flags=f("hearing_business"))),
    n("terms", "Nocticula", '''"Your sentence, Commander. Make it worth my evening."
{n}The hall leans forward. The bookmaker has stopped shouting; even he wants to hear. Ilvara stands in her shoes with her chin up and her chains quiet, and looks at you, not at the throne, as if you were the one holding the knife.
Below the dais two slaves are wheeling something out from behind a curtain: a cauldron of black iron, wide enough to sit in, already steaming. It smells like a tannery and a midden boiled together. Shamira's cauldron, from the Harem, borrowed for the night; you have heard what she uses it for, when she wants the city to remember who rules it. Nobody has said it is for Ilvara. Nobody has needed to.
Ilvara looks at it once and then does not look at it again. Her hands, in their chains, have closed into fists.{/n}
"Commander." {n}Her voice is low; only the front rows hear it.{/n} "Whatever you say, she will do worse. You know that. So say something I can live through. I made a beautiful thing. Let me go on making it, for her, in a cell, in a collar, anywhere." {n}Her eyes go to the slate lying face down on the arm of the throne.{/n} "I don't want to know what she wrote."
"No," {n}Nocticula agrees.{/n} "You don't." {n}She looks at you.{/n} "Remember the conditions, darling. I pass the sentence. You merely give me one I like. Be interesting. I'd so hate to have to use that."
{n}The hall waits. You can hear the cauldron, and chalk squeaking on a hundred slates, and somewhere at the back a slave dropping a tray and being struck for it. Nobody looks round. Every face on the steps is turned toward you, open-mouthed and greedy, the way a crowd watches a juggler with knives just before he catches the last one, or does not.{/n}''',
      c('"Make her a lamp in your Harem."', "confine"),
      c('"Collar her to the door. She works it until it eats her."', "commission"),
      c('"Strip your flower off her. Sell what\'s left."', "exile")),
    n("confine", "Nocticula", '''"A lamp. Oh, that's lovely. She becomes the light she sold."
{n}She does it there on the black floor, in front of everyone. She has no need of Ilvara's instrument; she takes Ilvara's own trick and turns it the other way. Ilvara's body goes thin and bright and folds down into the flame of a small brass lamp on the floor, and the hall can see her in it, a woman made of light, beating her palms without sound against the inside of the glass.
The court screams its approval. The bookmaker pays out on seven to two, and someone at the back shouts, "Pay up, you scaly bastard, I said lamp!"{/n}
"Take her to Shamira," {n}Nocticula says, and a slave lifts the lamp in both hands as though it were hot.{/n} "With my compliments. She can hang it over her bed. Ilvara will burn there for as long as anyone keeps her lit, and watch everything Shamira does in that bed, forever, which is a punishment for both of them." {n}She laughs.{/n} "And whenever I'm there, she'll watch me." {n}She turns her slate face up and shows it to you. On it, in her looping hand, she has written lamp.{/n} "I so rarely lose."''', c('[Hang the lamp in the Harem.]', flags=f("hearing_finished", "ilvara_confined"))),
    n("commission", "Nocticula", '''"Collared to her own door. Until it eats her." {n}Nocticula claps, once.{/n} "Yes."
{n}A smith comes up out of the crowd, already sweating, with an iron collar and a hammer; somebody had money on this one and came prepared. They kneel Ilvara on the floor and close the collar on her throat with three blows, and with each blow the hall counts aloud. The collar is plain iron. When it is shut, Nocticula draws her flower on the front of it with one fingernail, and the iron smokes.{/n}
"There. Now you're mine the way the door is mine. You'll work it for me. You'll open it when I want it open and shut it when I'm bored, and every time it bites, it will bite you first." {n}She leans down from the throne.{/n} "You wanted a commission, Ilvara. Here it is. The pay is that you're still alive. Don't ask for more."
{n}Ilvara is led away on a chain. She does not look back at the throne. She looks at you, all the way to the doors.
Nocticula turns her slate face up and shows it to you. She has written a single word on it: door.{/n}
"You see? I always guess right. It's why I keep you: you're the only thing in my city that makes me wait to find out."''', c('[Send her to work her own door.]', flags=f("hearing_finished", "ilvara_commissioned"))),
    n("exile", "Nocticula", '''"Strip her and sell her. How practical you are."
{n}Nocticula comes down the steps, and the hall parts for her. She stands before Ilvara and lays one hand flat on her breastbone, and pulls, and something comes away from Ilvara that you could not have seen until it was gone: the faint shadow of a black flower, the last of the old protection she stole, peeled off her like a skin. Ilvara staggers. Without it she looks smaller, and older, and very mortal.{/n}
"Now she's nobody's. Take her to the Fleshmarket," {n}Nocticula says.{/n} "Tonight, while there's a crowd. Sell her as what she is: a magician with no magic, a thief with no harbor, a woman with lovely shoes." {n}She looks down at the shoes.{/n} "In fact, sell the shoes separately. They'll fetch more."
{n}The hall laughs until the pillars ring. Ilvara is dragged out barefoot, and someone has started the bidding before she reaches the doors.
Nocticula turns her slate face up. She had written Fleshmarket, and under it, smaller, a sum. She studies the sum, and then the doors, and laughs.{/n}
"I underpriced her. Remind me never to let you sell anything of mine without me."''', c('[Let the Fleshmarket have her.]', flags=f("hearing_finished", "ilvara_exiled"))),
], "others_discussed")

s("last_buyer", "The last buyer", [
    n("start", "Narrator", '''{n}The buyer who planned Ilvara's escape has finally introduced himself. His name is Ossin. He represents a small consortium of merchants whose success depends upon knowing which borders can be crossed before their owners notice.
Nocticula presents his letter as though serving a dish whose smell offends her.{/n}
"He believes I have taken possession of the harbor. He wishes to buy exclusive access. In the event that I refuse, he proposes to inform several interested parties that I have been maintaining a private prison beneath my own protection."
"An accusation made out of part of the truth."
"The most economical kind."
{n}Ossin knows the Black Flower was real. He knows passengers disappeared. He does not know which parts of the instrument survived, what happened at the final lamp, or what Ilvara told during her hearing.
He assumes the missing information can be purchased from somebody who resents Nocticula enough to sell it.{/n}
"I could kill him," {n}she says.{/n} "Then his partners would sell the accusation at a memorial dinner and congratulate themselves on having discovered my vulnerability. I would prefer they learn a more useful lesson first. I can always kill him afterward; he is not going anywhere I cannot reach."
{n}She spreads the letter beside three intercepted invoices. The papers differ in age and handwriting. Each names a storage facility that has already changed owners twice.{/n}
"If we answer the wrong person, we merely improve somebody else's understanding of my affairs. I would like the people who will profit from this threat to hear the answer together."''',
      c('[Identify the common guarantor hidden in the invoices. Knowledge: World, DC 33.]', check=dict(Skill="SkillKnowledgeWorld", DC=33, Success="guarantor", Failure="false_lead", CommanderOnly=True)),
      c('"Publish the passengers\' accounts and the limits of what you claimed."', "public"),
      c('"Sell them the exclusive right to a route whose limits you describe exactly."', "auction", requires=("trickster",))),
    n("guarantor", "Nocticula", '''{n}The companies do not share an owner. They share a guarantor, a woman whose signature appears only when a debt changes hands. She has promised to cover losses from an interrupted voyage. If the harbor is exposed as a fraud, she owes money to every buyer at once.
You place the three signatures beneath Ossin's threat.{/n}
"He is not simply trying to acquire your route. He needs you to acknowledge it exists so his guarantor can deny the claims."
{n}Nocticula reads the arrangement and begins to smile.{/n}
"A threatened scandal which protects the person threatening it. Yes. I should have expected a more interesting motive than greed."
"Greed remains involved."
"As it should. One must not neglect the fundamentals."
{n}She can now send the answer to every insured buyer as well as the guarantor. The letter will state exactly what survived and which journeys were sold without a reliable return. Ossin must either contradict his own contracts or admit that his consortium helped finance Ilvara's operation.
You have not made his accusation disappear. You have made it expensive for him to tell only the profitable half.{/n}
"A very good afternoon's reading," {n}Nocticula says.{/n} "I am beginning to resent how much of our private time is improved by your ability to recognize a bad contract."''', c('"Send the complete account to everyone whose money depends on it."', "cost", flags=f("buyers_exposed"))),
    n("false_lead", "Narrator", '''{n}One repeated name appears to be the owner you need. Nocticula recognizes it as a dead merchant whose identity has been used to conceal three different debts. Your comparison has found a mask, not the face behind it.
The error costs the opportunity to answer quietly. By the time her agent verifies the name, Ossin has sent copies of the accusation to two buyers who have begun asking public questions.{/n}
"We can still tell the truth," {n}Nocticula says.{/n} "We will now be doing it after someone else has supplied the first version."
"Or buy the letters back."
"No. I will pay to learn a secret. I will not pay a man to repeat a threat he has already demonstrated he cannot keep exclusive."
{n}She destroys the dead merchant's false address and keeps the copies of the accusation. The investigation has lost surprise rather than acquired a fabricated culprit.
The passengers' accounts can answer much of the claim. They will also reveal that Nocticula did not discover the stolen use of her protection immediately. She dislikes that part enough that you know the decision to include it is real.{/n}''', c('"Then publish the complete account, including the delay."', "public", flags=f("buyer_read_failed"))),
    n("public", "Nocticula", '''"A public account will travel farther than your qualifications. Someone will say I sold the passengers. Someone else will say I rescued them out of love for mortals. I find both versions irritating."
"The witnesses can describe what happened."
"They can. They may also discover that people prefer the more flattering lie."
{n}She releases the records and keeps the passengers' private histories back, because they are hers now and she does not give away what she owns for nothing. Vessa's drawings go out at Vessa's price. Sere's letters stay in Nocticula's cabinet. Tomar collects his wages and is told, very pleasantly, that the first time he sells the story in a tavern will be the last time he sells anything.
The statement includes the use of the old protection, Ilvara's sales, the return, and the remaining uncertainties. It does not claim Nocticula had always intended the outcome.{/n}
"Ossin will dislike the loss of his private audience," {n}she says.{/n} "He wanted me alone in a room with the accusation. Now he can explain it to everyone whose money he proposed to collect."
{n}Nocticula sets the statement beside the threat. She has chosen to surrender some control over her reputation rather than purchase a fragile silence.
It is not an act she intends to repeat every time somebody says something unkind.{/n}''', c('[Release the bounded account and protect the witnesses\' private details.]', "cost", flags=f("account_public"))),
    n("auction", "Nocticula", '''"That sounds remarkably close to the business we have just dismantled."
"Only if we sell what we do not possess. Offer exclusive access to the records, not the harbor. Let him explain to his investors why the difference disappoints him."
"He may notice before paying."
"Then he has learned to read. Either outcome improves the conversation."
{n}You draft an invitation to bid on the technical account, with every absence listed plainly: no guaranteed passage, no ownership of travelers, no claim on Nocticula's future protection. The price includes a public acknowledgment of which voyages the buyer previously financed.
Ossin can refuse. He can also accept and surrender the secrecy that made his accusation profitable. His competitors receive the same terms at the same time.{/n}
"You have turned his threat into a question about whether he wants his rivals to know more than he does," {n}Nocticula says.{/n} "That is much better than pretending he will become honest because we caught him lying."
{n}She makes one change. The proceeds will pay the outstanding claims from the voyages before the consortium receives a single page. If there is nothing left afterward, she will accept the pleasure of watching them calculate the loss.
Nocticula seals the offers one at a time. Each bears the same closing hour. She saves Ossin's for last and puts his name inside, where the next clerk to open it will see what their principal has been buying.{/n}''', c('[Offer the exact, limited auction to every interested buyer.]', "cost", flags=f("records_auctioned"))),
    n("cost", "Nocticula", '''"There is one more matter. Ilvara's disposition will become part of the answer whether we publish it or not."
{n}She draws the three half-coins from the hearing out of the letter's shadow. Only the one you chose remains solid.{/n}
"If I have confined her, Ossin will accuse me of hiding the witness. If I have employed her, he will say I have inherited the trade. If I have expelled her, he will try to buy her account. None is an argument for pretending we chose differently."
"What will you say?"
"What I did. With sufficient detail to make the useful questions possible and the useless ones expensive."
{n}Nocticula's hand closes around the surviving coin. She looks tired of the affair without being tired of you, a distinction she has not previously made much effort to show.{/n}
"You may take your share of the credit. You may also leave your name out. I do not need the Commander printed beneath my account as a certificate of good behavior."
"How generous."
"It is not generosity. I am deciding how much of you to spend in public, and I should like your opinion before I spend it. Do not waste the question by asking which answer would please me."''',
      c('"Name my part accurately. I helped make the decisions."', "named"),
      c('"Keep my name private. The witnesses do not need another famous person in their account."', "unnamed")),
    n("named", "Nocticula", '''"Then they will know you helped me. Some will stop listening before the rest of the sentence."
"They already do that when they hear your name."
"Yes. It is occasionally convenient."
{n}The final account names your questions and advice without crediting you for work Rhez, Vessa, or the carrier performed. Nocticula refuses a sentence praising your moral leadership. She replaces it with the particular decision for which you were responsible.
One of Ossin's buyers has returned the notice with your name circled. He wants his passage money back from the crusade. Nocticula lays his demand beneath the signed account. "He has stopped asking me. How quickly a grateful merchant learns a new address."
Nocticula studies the finished wording, then touches your signature with a finger.{/n}
"There. You are in dangerous company again. I hope you continue to find it worth the trouble."''', c('[Stand by the part you actually played.]', flags=f("buyer_answered", "work_named"))),
    n("unnamed", "Nocticula", '''"Very well. I will not invent a mysterious adviser merely to make the omission seem important."
{n}The account credits the people who performed the work and the authority under which Nocticula commissioned it. Your private involvement remains between those who already know it. She warns that silence is not a lock; Ilvara and Ossin may still guess, and guessers are cheap to kill but tiresome to count.
You accept the distinction.
Nocticula folds the final statement and puts it aside. Then she steps close enough to straighten a crease in your collar which the dream did not need to supply.{/n}
"I know what you did," {n}she says.{/n} "Do not imagine I will require a public document to remember an inconvenient answer."
"Or a useful one."
"Especially an answer which managed to be both."
{n}She kisses you before allowing the room to fade. For a moment the seal on her letter remains visible in the darkness, a black flower pressed into red wax.{/n}''', c('[Keep the work private without denying it.]', flags=f("buyer_answered", "work_private"))),
], "hearing_finished")

s("empty_chair", "The guest who was not invited", [
    n("start", "Narrator", '''{n}Her private dining room is small, for a palace: a table of black wood laid for three, candles, a window over the Middle City burning red below. One of the three chairs lies on its side on the floor. Nocticula stands over it, holding a little mask by its ribbon.
The mask is smiling. Its mouth has been cut too wide for any face, and the white paint around it is chipped, as if it has been worn many times by people who did not enjoy wearing it.{/n}
"If you're about to ask whom I've killed, ask the better question. Who sent this."
"Whom haven't you killed yet?"
"A hostess." {n}She lets the mask turn slowly on its ribbon.{/n} "A lamia named Istrava, who keeps a hunting lodge above one of the old pleasure gardens and pays me very handsomely every year for the privilege of keeping it. Her guests pay her to hunt people who can't refuse to be hunted. Debtors, mostly. Slaves she rents. Now and then someone's inconvenient wife." {n}She sets the mask on the fallen chair, face up, so that it smiles at the ceiling.{/n} "She sent this to Rhez, with an invitation. An evening in honor of the people who cost her guests their harbor investments; Rhez is to collect a prize. The invitation doesn't mention that the prize is being eaten. I'm offended on Rhez's behalf. I'd never waste her so cheaply."
{n}She hooks one bare foot under the fallen chair and rights it with a flick, as if it weighed nothing. The mask stays on the seat, smiling.{/n}
"I've already moved Rhez's meeting. I've already decided Istrava will regret the mask. What I haven't decided is how much, and I'd like your help being creative." {n}She sits down in the righted chair and crosses her legs.{/n} "Some of Ossin's dear friends will be at her table, if that sweetens it."''',
      c('"Does this threaten your people, or only your pride?"', "threat"),
      c('"She wants you angry enough to walk in blind. Don\'t give her that."', "temper")),
    n("threat", "Nocticula", '''"My people. My pride isn't something a lamia can reach with a mask."
{n}She takes a strip of yellow cloth from beside her plate, torn from a servant's sleeve, and a folded sketch, and lays them on the table.{/n} "Edris. She tended the lower gallery at Istrava's lodge until a guest noticed how often the servants disappeared before the horn, and Istrava turned her out before he could ask anyone else. She came to my gate with this."
{n}The sketch is a floor plan in charcoal, careful and unskilled.{/n}
"Istrava's evening has a theme. Three of her attendants are going to play my returned passengers, the ones from the door; she knows them from gossip, not by their faces. They'll be rescued in her gallery as a joke on me, and then the guests will hunt down the rescuers and eat them, as a joke on the joke." {n}Her mouth curls.{/n} "The returned are mine. I don't parade my property for a vassal's amusement; they're downstairs, and they'll stay there. And the three girls she has dressed up as mine don't know which part of the evening is real."
"And Istrava?"
"Istrava hunts under my protection. She pays me for it. And she has decided that means she may hunt what's mine." {n}Her voice goes soft.{/n} "Hunting is a privilege, darling. In my city, it's mine."''', c('"Tell me what Edris can show us."', "edris", flags=f("lodge_people_first"))),
    n("temper", "Nocticula", '''"You think I'm angry."
"You furnished a whole room to knock over one chair."
{n}She looks down at the chair she has just righted, and a short sound escapes her, almost a laugh. There is no warmth in it, but some of the stillness goes out of her face.{/n}
"You may be useful tonight. Don't be encouraged; it's a low bar." {n}She takes a strip of yellow cloth from beside her plate, and a folded charcoal sketch.{/n} "Istrava wants my city to watch me punish a joke because its subject embarrassed me. Half her guests would buy that story with her life and call it a bargain. I'm not going to give it to them." {n}She smooths the sketch flat.{/n} "This came from Edris, who used to tend Istrava's lower gallery. Three of Istrava's attendants are going to play my returned passengers in a mock rescue, and then be hunted down by the guests for it. My real ones are downstairs. Nobody parades my property for a lamia. The girls in the masks don't know which part of the evening is real."
"Then walk in with something she didn't plan for."
"Her own servants would do. Provided they're still alive to be useful." {n}She lays the yellow cloth across the mask's smiling mouth.{/n} "She hunts under my protection, and she's decided that means she may hunt what's mine. Hunting is mine. The tiresome thing about the best witnesses is how easy they are to eat."''', c('"Tell me what Edris can show us."', "edris", flags=f("lodge_pride_named"))),
    n("edris", "Nocticula", '''{n}Nocticula moves her hand, and the table becomes the lodge: a model in black wood and candle wax, its windows dark, the lower gallery three pale strips, a bell chamber above them with two stairs. Here and there are gaps where Edris could not remember a measurement. Nocticula leaves the gaps.{/n}
"Edris will take one person through the service door. She won't go upstairs. The last time she went upstairs, a guest had her carry his severed antler down to the yard while he begged for it back, and she says it weighed almost nothing." {n}She sounds amused.{/n} "She asked me to promise that Istrava would never find her. I said no. I don't promise what I won't bother to do. She nearly walked out. Then she remembered that her sister still works there."
"What does she want?"
"Passage for the two of them out of Istrava's reach. Not the harbor; the harbor is spoken for. A boat. And her sister's shoes, which were their mother's, which Istrava keeps in a cabinet and lends to the attendants for special evenings, so that they can be hunted in something pretty." {n}She taps the model's gallery.{/n} "The bell lives here. Until it rings, every servant stays where the guests can see them. When it rings, the guests may chase anyone it names. Edris says the bell chooses the name, which means whoever holds the bell chooses it, which means Istrava."
{n}She takes your hand and lays it on the model, your fingers along the two stairs, one down to the yard, one up to the dining room, and leaves her own hand on top of yours.{/n}
"So. What do you want from this, darling? Say it plainly. Servants alive, a hostess humbled, a house taken, me impressed." {n}Her nails press into the back of your hand.{/n} "They'll get along for an evening. Then one of them generally eats the others."''',
      c('"The attendants live. They\'re yours afterward."', "purpose", flags=f("lodge_rescue")),
      c('"Take her house."', "purpose", flags=f("lodge_conquest"))),
    n("purpose", "Nocticula", '''"Good. An appetite." {n}She takes the mask off the chair and holds it out to you by its unbroken edge. The paint is cool under your thumb. Behind the eyeholes there is nothing like a face.
You turn it over. On the back, a little steel hook has been sewn into the ribbon, set to catch in the wearer's hair if they try to tear it off.{/n}
"Economical," {n}you say.{/n}
"Unimaginative. She thinks making it hard to leave is the same as making someone want to stay." {n}Nocticula takes the mask back and lays it face down on the table.{/n} "I learned the difference a very long time ago. Every one of her guests' quarry, I'd have hunted better. That is what offends me."
{n}She sits beside you, close, her thigh against yours, and for a while the two of you study Edris's sketch until you can describe both stairs without looking. She corrects the width of a landing, then admits it was a guess and rubs it out with her thumb.{/n}
"Now. You'll come, of course. The question is how. As yourself, or behind one of these?" {n}She flicks the face-down mask with a fingernail.{/n} "And how much of the evening am I allowed to spend?"''',
      c('"I\'m coming. Masked."', "vow_guard", flags=f("lodge_proposed")),
      c('"Spend whom you like. I want the bell."', "vow_ledger", flags=f("lodge_proposed"))),
    n("vow_guard", "Nocticula", '''"Of course you are. I'd have dragged you." {n}She picks up the mask and ties it on you herself, her fingers in your hair, and checks the little hook with a fingertip, and leaves it in.{/n} "There. Now you know how her guests' quarry feel. Don't pull at it. It takes a scalp."
{n}She stands back to look at you, and her smile under the candlelight is pure appetite.{/n} "Oh, that suits you. I may make you wear it home."''', c('[Plan the entrance.]')),
    n("vow_ledger", "Nocticula", '''"Generous. I'll spend Istrava first." {n}Her eyes go very bright.{/n} "You want the bell. Not the servants, not the house: the thing that decides who runs. Oh, darling." {n}She leans in until her mouth is at your ear.{/n} "Most of my generals want to be told afterwards who died, so they can mourn with clean hands. You want to hold the rope. I'm going to give you the whole list. Every name."''', c('[Plan the entrance.]')),
], "buyer_answered")

s("mask_and_bell", "A mask with its mouth shut", [
    n("start", "Narrator", '''{n}The model has acquired a bell. Nocticula suspends it over the dining table by a thread, with an ordinary spoon inside for a clapper.
You touch the rim. It makes a small, disagreeable sound.{/n}
"Edris says the real one is silver. I considered supplying the proper material, but this noise has already improved my opinion of silence."
{n}Rhez has visited the lodge's supplier under a borrowed name. The hunting masks are ordinary objects. The bell is not. Its enchantment marks the people counted as quarry when the host names them, and the house's hunters can then follow those marks through its galleries. The marks end when the bell is rung again by the person holding the host's baton.
The supplier knew the arrangement because Istrava once refused to pay for a repair after an evening ended too soon. He kept her complaint.
Nocticula has not bought the bell or copied its enchantment into the dream. She has copied the complaint.{/n}
"A second ringing ends the hunt," {n}you say.{/n}
"If we possess the baton. If the bell has not been altered since that repair. Rhez answers to me for both, and if either fails I shall want to know whose idea wasted my agent."
{n}The baton usually remains beside Istrava's chair. Her chamberlain, Vhal, carries it when she leaves the room. He is a cambion with a talent for making guests believe every inconvenience was arranged especially for them.
Edris remembers that he has never accepted a mask himself.{/n}''',
      c('[Read the repair complaint for a way to stop the first marking. Use Magic Device, DC 34.]', check=dict(Skill="SkillUseMagicDevice", DC=34, Success="silence", Failure="fracture", CommanderOnly=True)),
      c('"Send an irresistible guest. Let Istrava surrender the baton to welcome you."', "guest"),
      c('"A hostess must greet her guests. Send her an invitation addressed to herself."', "trick", requires=("trickster",))),
    n("silence", "Nocticula", '''{n}The disputed repair replaced the bell's suspension, not its clapper. Istrava complained that the bell rang when a guest struck the outside. The supplier answered that a hunt could only begin when the baton touched the bell's inner lip.
You turn the copied complaint toward Nocticula and set the spoon against the rim from within.{/n}
"Make the first blow miss. Vhal can announce the hunt, but he cannot mark anyone with an empty gesture."
"The supplier may have improved it."
"Then we verify the inner rim before depending on it. Edris knows the cleaner who polishes it."
{n}Nocticula unfolds a second report. Rhez has already questioned the cleaner through Edris: the inner lip still carries the inscription, and old wax has lodged beneath it. The supplier's complaint now makes that observation useful. A thin packing of the same wax can absorb one touch of the baton without appearing new.
The cleaner has offered to help if she can leave before the gathering. She will not wait inside to see whether a plan works. Nocticula adds an instruction for Rhez to meet her outside before any signal is given.{/n}
"One quiet bell," {n}she says.{/n} "Afterward, everybody will know somebody has been touching it."
"Then we should already be doing something they cannot ignore."
{n}She leaves the spoon lying across the model. The first advantage is small, bought from somebody whose name the guests have never bothered to learn.{/n}''', c('[Use the verified packing to prevent the first marking.]', "limits", flags=f("lodge_silent_bell"))),
    n("fracture", "Nocticula", '''{n}You find the damaged mounting and suggest loosening its pins. Nocticula lets you finish before turning over the supplier's sketch. A second brace is fixed inside the housing. Without removing it, the bell would tilt rather than fall, leaving its inner lip directly beneath the baton.
You have nearly devised a way to make the hunt easier to begin.{/n}
"I prefer that you do your dangerous guessing here," {n}she says.{/n}
"You could have stopped me sooner."
"You were about to discover whether I enjoyed being right more than I enjoyed keeping an agent alive. I thought the discovery might be useful."
{n}She removes the pin from the dream model. The spoon strikes its exposed rim. Both of you endure the noise until you put the pin back.
The failed reading leaves you without a reliable way to silence the bell. The supplier has closed his shop for the gathering, and Rhez cannot obtain a fresh inspection without advertising the interest. There is still a direct entrance: Nocticula can attend as a guest, making Istrava stand to receive her. Vhal will then carry the baton, and Rhez can watch him from the service stair.
The bell may ring before she reaches him. Every attendant must be warned to run when it does, whether the guests believe the performance has begun or not.{/n}
"No pretending the plan is quieter than it is," {n}Nocticula says.{/n} "Tell me what you want the people downstairs to do when subtlety fails."''', c('[Use the guest entrance and warn the attendants about the first ringing.]', "limits", flags=f("lodge_bell_read_failed", "lodge_guest_entry"))),
    n("guest", "Nocticula", '''"She would enjoy that. She would also spend the evening wondering whether enjoyment was the mistake."
{n}Nocticula asks what you propose she wear. When you answer that it should give Istrava a reason to leave her chair, she looks at you as if you had moved a piece she had not seen.{/n}
"That is a remarkably indirect compliment."
"I was trying to keep it useful."
"Try less hard."
{n}The plan is simple enough to survive a frightened messenger. Nocticula will enter through the front. Istrava must either receive her or publicly refuse a guest she has spent days pretending to invite. Vhal will take the baton when his mistress rises. Rhez will approach him from the service stair while the room is watching somebody else.
Nocticula will use her own form. No double will hold a room full of demons through the first unexpected question. You will not be transported there by wanting to attend.
There is no promise that the bell remains silent. The attendants will be warned to run at its first sound, and Rhez will know that taking the baton matters more than keeping her cover.{/n}
"I shall have to trust someone else to enjoy the clever part," {n}Nocticula says.{/n}
"You can enjoy being impossible to ignore."
"I generally do. It is the occasions on which I need to be ignored that require better company."''', c('[Draw the audience toward Nocticula while Rhez follows the baton.]', "limits", flags=f("lodge_guest_entry"))),
    n("trick", "Nocticula", '''"Istrava will recognize her own address."
"Good. We need her to recognize her invitation too. Every guest was promised an honored quarry. Tell her the honor has been reserved for the only person qualified to preside over it."
"She will recognize a threat."
"A threat with excellent manners. Let her deny it before the other guests arrive. They will ask why she finds her own hospitality alarming."
{n}Nocticula considers the announcement. It forces Istrava to decide which part of her performance she is willing to defend in public.
Rhez can deliver the announcement through the lodge's musicians, who have been ordered to celebrate every guest's arrival. If they rehearse Istrava's arrival as well, the chamberlain must either interrupt the music or carry the baton out to conduct it.
The interruption will make him visible from the service stair. It does not make him helpless.{/n}
"She might laugh," {n}Nocticula says.{/n}
"Then she has bought herself time by admitting the joke. We still know who carries the baton."
"And if she orders the musicians punished?"
"Your entrance interrupts the order. We do not leave them waiting to discover whether our timing was amusing."
{n}Nocticula draws a small black flower beside the final line of the announcement.{/n}
"A joke which makes its author provide the rescue. You are becoming expensive company."''', c('[Use the public announcement to expose the chamberlain and protect its performers.]', "limits", flags=f("lodge_self_invitation"))),
    n("limits", "Nocticula", '''{n}The plan still has a lower floor. Nocticula turns the model so that the service yard faces you.
Edris can open one door. Beyond it, her sister and the others must run on their own legs. Rhez has two hands and a stair to hold, and anyone who stops at the door to argue will be left for the guests.
Nor can she remain indefinitely. Once the hunt begins, the gallery will become a corridor through which armed guests expect to pursue something.{/n}
"I want Vhal alive," {n}Nocticula says.{/n} "He knows which guests bought the performance before they were invited. If Rhez must choose between carrying him and keeping her own hands free, however, she drops him."
"That is unusually practical advice from someone who can make the whole room stop moving."
"I will be in a different room. Power does not make an agent less dead if I notice too late where I should have been looking."
{n}She says it with such irritation that you suspect the lesson once belonged to somebody whose name she has not offered. You do not ask for it as the price of believing her.
Instead you move the little figure representing Rhez from the upper stair to the yard. Nocticula moves it back. The baton must be taken before the second ringing can end the mark. You repeat the order until both movements fit without placing Rhez in two rooms at once.
The bell above you turns on its thread. Its spoon has come loose. You catch it before it hits the table.{/n}
"There," {n}Nocticula says.{/n} "A feat worthy of the Commander."
"I expect a song."
"You may have a silence. I have just learned to appreciate them."
{n}She takes the spoon from you and lays it aside. Then her fingers return to your empty hand, briefly, without a plan to illustrate.
She gives the instructions to her real agents after the dream. Their answers will belong to the next meeting; no gesture over this model can complete the operation tonight.{/n}''', c('[Let the agents prepare the agreed entrance and the service-yard withdrawal.]', flags=f("lodge_method_ready"))),
], "lodge_proposed")

s("uninvited_guest", "The entertainment answers back", [
    n("start", "Narrator", '''{n}You fall asleep in Drezen and wake standing up, in a mask, on a stair you have only seen in charcoal.
The lodge is louder than Edris's sketch. Below you lies Istrava's dining hall: long couches in a horseshoe, bowls of something that is still moving, a hundred candles burning in a smell of musk and spilled wine. Above the far end of the hall hangs the bell chamber, open on one side like a box at the theater, and in it the little brass bell on its hook, and beside it a narrow man in grey holding a baton across his palms like a priest holding a relic. Vhal. Below the hall, behind a railing, runs the lower gallery, where three attendants stand very still in white masks with their mouths cut too wide.
Nocticula is beside you. She wears black, and a mask of plain black silk that hides nothing; every person in this house knows who she is, and the mask is there so that they must pretend not to.{/n}
"Don't wake up," {n}she says without turning her head.{/n} "I went to a great deal of trouble to bring you, and you look lovely in that."
{n}On the highest couch lies the hostess. From the waist down Istrava is serpent, a long coil of dark green and gold that runs off the couch and across the floor and back again; from the waist up she is a handsome woman with a heavy jaw, and her black hair is threaded with tiny gold cages, each one holding a live moth. The moths beat against the bars whenever she laughs. She is laughing now. Around her the guests recline in their own masks, demons and worse and a few rich mortals with the shine of terror on them that they mistake for excitement. Three of them are Ossin's friends. Ossin is not among them. Nocticula knows exactly where Ossin is.
Istrava sees the black mask on the stair and raises her glass.{/n}
"Lady in Shadow. We had begun to fear you would take offense."
"At being invited so late? I assumed you had difficulty finding a chair you could afford to lose."
{n}The laugh goes round the horseshoe a beat too late. Nocticula smiles at it the way one smiles at a dog that has learned to sit.{/n}
"Stay here, at the rail," {n}she tells you, low.{/n} "Nobody in this house can touch you. The Gift sees to that, and so do I, and every one of them can smell it on you. You won't fight tonight, darling. You'll watch. And when I look up at you, you'll choose a name for the bell."
"Whose name?"
"Whoever you like. That's the joke." {n}She takes her hand off the rail.{/n} "She rings it, and her guests chase whoever it names. She does it under my protection, in my city, on my people. Hunting is a privilege, and in Alushinyrra the privilege is mine. Let's go and remind her."''',
      c('[Watch Vhal strike the bell you silenced.]', "silent", requires=f("lodge_silent_bell")),
      c('[Watch Rhez go for the baton.]', "guest", requires=f("lodge_guest_entry")),
      c('[Let the musicians read out her invitation.]', "announcement", requires=f("lodge_self_invitation"))),
    n("silent", "Nocticula", '''{n}Istrava claps twice. The musicians stop. Vhal steps to the bell with the baton raised, and the whole horseshoe leans toward him the way a crowd leans toward a gallows.
He strikes.
Nothing. Brass on brass, a dull little tap like a spoon on a cup, and then silence. The attendants in the gallery do not move. No light comes. Vhal strikes again, harder, and the bell swings on its hook and taps the wall, and someone at the end of the horseshoe giggles.{/n}
"Is that the entertainment?" {n}Nocticula asks the room, pleasantly.{/n} "A man discovering silence? I've seen it done better in my cells. They usually scream first."
{n}Istrava's coils tighten on the couch. She says something sharp to Vhal. Vhal, sweating, lifts the baton for a third try, and finds Nocticula standing beside him in the bell chamber, though nobody saw her climb the stair. She takes the baton out of his hand the way one takes a toy from a child.{/n}
"You won't need this. It doesn't work. I had it seen to." {n}She glances up at your rail, and her eyes in the black silk are laughing.{/n} "By someone with very clever thumbs."
{n}Vhal reaches for the baton. She lets him get his fingers on it and then breaks two of them, without looking, and he folds down onto his knees and stays there.{/n}
"Listen to me, all of you." {n}She does not raise her voice. She has never had to.{/n} "The bell has no working left in it. It's only a bell. But you all know what it means when it rings in this house. That was the only magic it ever had: you, doing as you're told." {n}She taps the brass with the baton, very lightly. It gives a small, clear note.{/n} "So it still works. It simply works for me."''',
      c('"Now the gallery."', "gallery", flags=f("lodge_unmarked"))),
    n("guest", "Nocticula", '''{n}Rhez comes in on Nocticula's arm, masked, in the green coat, looking bored. She has been invited as the guest of honor and she walks like it, straight down the middle of the horseshoe toward the bell chamber, and Vhal comes down from the chamber to bow to her with the baton across his palms, as the house rules say he must.
He is still bowing when she takes it.
It is very neat. It would have been perfect, except that a guest on the nearest couch, a bull-necked thing with a jeweled snout who has been drinking since before the candles were lit, sees the baton change hands and does not like it, and puts a knife into Rhez's arm.
Rhez does not drop the baton. She cannot stop it ringing, either: it strikes the bell as she twists away, once, and a line of pale fire runs across the masks in the lower gallery, and below you the three attendants scream together. The guests applaud. They think it has begun.
Rhez hits the bell again on purpose, harder, the second stroke that ends the marks, and the fire goes out. Then she sits down on the floor with her back to the bell chamber wall, holding her arm, and bleeds.
Nocticula has the snouted guest by the collar. She lifts him off his couch, walks him across the hall with his feet kicking, and drops him into Istrava's own seat, which Istrava has just vacated in a hurry.{/n}
"You wanted service," {n}she tells him.{/n} "Begin by keeping it warm."
{n}She picks the baton up off the floor where Rhez has let it roll, and looks at the blood on it, and at Rhez.{/n}
"That arm cost me twenty years and three dead masters," {n}she says, to the whole room.{/n} "I'll remember who opened it." {n}The snouted guest, in Istrava's chair, begins very quietly to cry.{/n} "Rhez. Don't die. It would be so inconvenient." {n}Rhez, white to the lips, tells her lady where she can put the inconvenience. Nocticula laughs, delighted, and looks up at your rail.{/n}''',
      c('"Rhez is cut. Make someone pay for it."', "gallery", flags=f("lodge_mark_ended", "lodge_rhez_hurt"))),
    n("announcement", "Nocticula", '''{n}Istrava rises on her coils to make her welcome. Before she can open her mouth the musicians strike up, and a thin tenor steps forward with a card in his hand, and reads it out in a voice that fills the hall.
It is Istrava's own invitation. You know, because you wrote it. It is in her hand, and her seal is on it, and it announces, in her own flowery phrases, that this evening's most honored quarry will be the lady of the house.
Nobody moves. Then somebody laughs, high and nervous, and stops.
Vhal comes down out of the bell chamber with the baton raised to strike the tenor, and Rhez, who has been standing behind the musicians in her green coat all evening holding a tray, steps into his way and asks him whether he means to hit a guest with the instrument of welcome. He hits her with his other hand instead. She lets the blow turn her, catches the baton against her shoulder, and puts him on the floor. The tenor, bless his spite, reads the card to the end.{/n}
"Her rules," {n}Nocticula says, with enormous pleasure.{/n} "The house has rules, and she wrote them, and she signed them. I adore people who write their own sentences. It saves me the effort." {n}She takes the baton from Rhez, who gives it up with a bow.{/n}
{n}Istrava is still standing on her coils at the head of the horseshoe. Her guests are looking at her. They are looking at her the way they looked at the attendants in the gallery when they came in: measuring, appetite stirring under the masks. She sees it. She sits down very slowly, and the moths in her hair throw themselves against their cages.{/n}
"Look at their faces, darling," {n}Nocticula says up to your rail.{/n} "They're doing sums. Which is more dangerous: the hostess, or the house rule? They've never had to ask before."''',
      c('"Let them keep doing sums. The gallery."', "gallery", flags=f("lodge_unmarked", "lodge_host_exposed"))),
    n("gallery", "Narrator", '''{n}The lower gallery is a long room behind a railing, lined with cabinets, lit low so that the guests above can see down into it and the people in it cannot easily see up. The three attendants are dressed as Nocticula's returned passengers: sea-stained clothes, a fake brass bell for Vessa, a boot for Halren. Their masks have hooks sewn into the ribbons. One of them is crying behind hers and cannot stop.
The service door at the far end opens a crack. Edris slips through it, in her yellow sleeve, and goes straight to the smallest of the three and takes her by the shoulders. That is Mera. She is wearing her mother's shoes, which are red, and a size too small, and she will not leave the cabinet where Istrava keeps the rest of the trophies: a comb, three rings, a child's wooden whistle that a grown servant kept from her girlhood. Edris cuts her mask's ribbon instead of pulling it, and hisses at her to come, and Mera shakes her head.
A guest has come down into the gallery to watch them. Not one of the drunk ones. He is lean and plain-dressed, with a collector's iron chain of office round his neck and a tally-stick in his belt, and he leans on the railing and smiles at the sisters as though they were a debt he had been waiting a long time to collect.{/n}
"That one," {n}Edris says, loud enough to carry, pointing up at him with the knife.{/n} "That's Suth. He buys the ones who run, and he collects on the ones who don't. He's got paper on both of us."
{n}Suth touches his brow to her, courteously.
Up in the bell chamber, Nocticula stands with the baton held loosely under the little brass bell. The hall below her has gone quiet. Istrava is watching her. The guests are watching her. Suth, in the gallery, has stopped smiling and is watching her too.
Then she lifts her eyes, past all of them, to your rail.{/n}''',
      c("[Meet her eyes across the hall.]", "held")),
    n("held", "Nocticula", '''{n}Afterwards the hall is a mess. Couches overturned, wine and worse on the tiles, a mask lying face up in a puddle and smiling at the ceiling. The musicians have hidden under their own platform. Somewhere in the gardens a guest is still screaming, more and more faintly, as though walking away.
Istrava lies on the floor of her own dining hall with her long tail tangled round a broken couch and Nocticula's bare foot on the back of her neck. Half the moth cages in her hair are crushed. The moths that got out are crawling on her face.
Nocticula has taken the hostess's chair. She sits with one leg crossed over the other and the baton across her knee, and you stand at her right, where she has put you, still masked.{/n}
"There," {n}she says.{/n} "Now we can talk like civilized people."
{n}Istrava talks. It pours out of her, the way it does when people realize the floor they are lying on is the last floor they will own. Her patrons; the names of the people who paid for every hunt this season and the last; the house, the gardens, the gold in her strongbox, the list of every servant she ever rented and to whom. She will give all of it. She will give anything. She knows things about other houses. She knows things about the Ten Thousand Delights. She has a cousin—{/n}
"Names, sweetheart," {n}Nocticula says.{/n} "All of them. Sing it like you mean it."
{n}She reaches down without looking and picks a moth off Istrava's cheek, and eats it, slowly, in front of everyone who is left. Istrava stops talking. Nocticula licks the powder off her fingers.{/n}
"You hunted under my protection," {n}she says, to Istrava, gently.{/n} "You took my name off the door and used it to make your guests feel safe while they ate people I'd never been asked about. That's a kind of theft I don't have a word for, because nobody ever tried it often enough to need one." {n}She lifts her foot. Istrava does not dare move.{/n} "And now you want to sell me my own city back, a piece at a time, and keep your skin."
{n}She looks up at you. Behind the black silk her eyes are bright and hungry and perfectly calm.{/n}
"What do I give her for it, darling?"''',
      c('"Take the list from her mouth. Promise nothing."', flags=f("lodge_hunt_ended"))),
], "lodge_method_ready")

s("closed_gallery", "The price of keeping a door shut", [
    n("start", "Narrator", '''{n}Rhez's account is short. She wants the name of the guest who followed Mera, enough guards to make his first retaliation expensive, and a replacement for the coat she tore at the stair. She has declined an invitation to dine with Nocticula while the household is still looking for people to blame.
Nocticula reads that last sentence twice.{/n}
"She suspects dinner would become another report."
"Would it?"
"Probably. I shall buy the coat."
{n}The guests have begun telling different versions of the evening. In one, Nocticula rescued servants out of sudden tenderness. In another, she staged the entire performance to take Istrava's house. The guest who pursued Mera calls himself an injured spectator.
His name is Suth. He maintains a small company of collectors who recover people as readily as objects. Nocticula has forbidden him to approach the escaped attendants while she examines the complaint. He has obeyed so far.
Istrava's remaining servants have closed the gallery. They will not clear the trophies from the floor until they know whom the possessions will belong to afterward. Their mistress has threatened to replace them. There are not enough willing replacements waiting at her door.{/n}
"They have found an inconvenience she cannot eat," {n}you say.{/n}
"She can eat the servants. She cannot make the others mistake that for a recommendation. For the moment, she still wants a functioning house."
{n}Nocticula sets three objects between you: the copied mask, a key sent by the service-yard guard and a strip torn from Rhez's coat.
She asks which of them you think Istrava most regrets losing.{/n}''',
      c('[Find the threat Istrava cannot dismiss without losing her guests. Diplomacy, DC 35.]', check=dict(Skill="CheckDiplomacy", DC=35, Success="audience", Failure="misjudge", CommanderOnly=True)),
      c('"Let the servants name their possessions before another owner claims the house."', "owners", requires=f("lodge_rescue")),
      c('"Take her remaining guests as the audience for her surrender."', "seizure", requires=f("lodge_conquest"))),
    n("audience", "Nocticula", '''{n}You choose the mask. Not because it frightened the attendants, but because it allowed the guests to pretend that somebody else had decided whom they might hurt.
Istrava sold them that permission. When the marking failed to protect their entertainment, she asked them to rely on her version of events instead. Suth's complaint is therefore a test: will she still supply the story they paid to inhabit?{/n}
"Let her answer it before the people who purchased the same promise," {n}you say.{/n} "If she declares that a fleeing servant attacked a spectator, every patron learns that her house cannot distinguish the hunter from the quarry."
"And if she admits the hunt?"
"She must say whose protection she expected the guests to disregard."
{n}Nocticula turns the mask over. Its broken ribbon falls across her wrist.{/n}
"You have made her audience useful to me. I had been considering how much of it I could afford to remove."
"You can still dislike them."
"I shall make an effort."
{n}She sends the summons as a hearing about the hostess's hospitality, with the escaped attendants spoken for by Edris from another room; Nocticula has no intention of letting Istrava look at her property again. Edris accepts that role from another room, through a messenger she knows. The trap uses Istrava's promises against her and gives the servants time to empty the gallery before the guests understand what is being decided.{/n}''', c('[Make the invited audience hear what its hostess actually promised.]', "offer", flags=f("lodge_audience_turned"))),
    n("misjudge", "Nocticula", '''{n}You choose the key and argue that Istrava cannot afford to lose the house. Nocticula asks what you would do if the lamia burned it.
You begin answering that her guests would resent losing their possessions, then stop. Their resentment would fall on the people accused of making the house unsafe. Istrava could preserve the story by destroying the place where it might be contradicted.{/n}
"She is capable of preferring a splendid loss to a visible surrender," {n}Nocticula says.{/n} "I find that annoying chiefly because I understand it."
{n}Nocticula produces the last report received before this meeting. Istrava has already ordered two wagons brought to the gallery. She may intend to remove its contents; she may intend to destroy them. Your argument supplies no quiet pressure she can be trusted to accept before the wagons leave.
Nocticula therefore chooses an overt order for guards to stop them in the yard. The servants are to remain outside the locked gallery while their possessions are counted under guard. It is a rougher intervention, and it will tell Istrava exactly which door Nocticula is prepared to seize.{/n}
"We can recover what remains," {n}she says.{/n} "We have lost the pleasure of letting her discover why she should surrender it."
"Then claim the interference. Do not let her blame the attendants for your soldiers."
{n}Nocticula writes her own name beneath the order. She does not invite you to share the signature merely to make the correction less embarrassing.{/n}''', c('[Own the overt intervention and guard the possessions still in the yard.]', "offer", flags=f("lodge_pressure_failed"))),
    n("owners", "Nocticula", '''"Some of them will claim things which never belonged to them."
"Then ask what they can describe before you open the cabinet."
{n}You set the strip from Rhez's coat beside the key. Istrava knows the value of the trophies. Their owners know the repairs, the stains, the contents of folded letters. The distinction will not settle every claim, but it makes a useful first question.
Nocticula sends a clerk and enough guards to keep the clerk from becoming another possession. The attendants can describe an object privately before it is brought out. Objects whose ownership remains disputed go into a sealed chest, not into the clerk's pocket.
Nocticula keeps the cabinet itself. It is lacquered and old and it was Istrava's, and she likes the idea of the lamia knowing exactly where it stands.{/n}
"You have made a remarkably small conquest," {n}Nocticula says.{/n}
"Small enough that the people concerned may recognize it."
"And large enough that Istrava will resent every missing comb. There is a certain precision to it."
{n}Edris agrees to identify what she remembers. Mera will not return. Nocticula shrugs at that: a witness who will not come is a witness nobody else can buy either.
She sends the clerk without her.{/n}''', c('[Return identified possessions and keep disputed claims out of the hostess\'s hands.]', "offer", flags=f("lodge_possessions_returned"))),
    n("seizure", "Nocticula", '''"You would like them to know whose company now makes a room dangerous."
"I would like them to stop mistaking your patience for an invitation."
{n}She accepts the distinction with a slight inclination of her head, though you can see she has not surrendered the less flattering interpretation.
The summons offers Istrava a choice. She can surrender the hunting apparatus, its guest list and the lower gallery under Nocticula's authority, or face an inspection of every person presently confined in her house. The second choice would expose obligations she has concealed from several patrons.
You have chosen pressure rather than a purchased apology. It may secure the gallery quickly. It also gives Nocticula a foothold in a house she did not own yesterday.{/n}
"The attendants should hear that before they celebrate," {n}you say.{/n}
"I am not concealing my name above the door."
"A new name can look like an exit until someone tries to use it."
{n}Nocticula's expression cools. She studies you as though deciding whether the warning was meant for her or for the person you would become beside her.{/n}
"Then they may leave. I want the position, the guest list and the example. I do not need frightened cleaners to complete the triumph."
"Put that in the order."
"You are becoming less decorative with practice."
{n}She adds the sentence. The joke does not soften how carefully she watches you read it.{/n}''', c('[Take the gallery and its political advantage while allowing the attendants to depart.]', "offer", flags=f("lodge_gallery_seized"))),
    n("offer", "Nocticula", '''{n}Istrava sends a private answer before the next public move. She offers Suth as the author of the hunt. She will testify that he demanded the attendants, provided she keeps her house and the matter ends with him.
She also offers one of the gold cages from her hair. Inside it is a moth whose wings have been painted with a map. The map allegedly leads to a hidden store belonging to a former patron.
Nocticula places the cage on the table. The moth remains still.{/n}
"A gift for me," {n}she says.{/n} "A culprit for you. She has been listening poorly to whichever story she heard about us."
"Is the map real?"
"Possibly. She has not said whether its owner still visits the store. I admire an apology which finds room for an ambush."
{n}You ask whether Nocticula intends to accept the cage. She answers that accepting an object is not the same as accepting its explanation. She has already ordered the moth fed and the paint examined without unfolding its wings by force.
There is something unexpectedly intimate about watching her refuse a beautiful thing's advertised use. Then she asks how much Istrava would pay to learn whether it worked, and the moment becomes recognizably hers again.{/n}
"Suth did pursue Mera," {n}you say.{/n} "He is not innocent because he is convenient."
"Nor is Istrava absolved because her guest was enthusiastic. We may take the evidence without purchasing the conclusion."
{n}She slides the offer to you. The final line asks that the Commander be told who supplied the decisive information.
Nocticula has not disclosed your identity as her adviser if you kept it private. Istrava is speculating about a famous ally whose involvement she hopes to provoke. If you claimed public credit, she is appealing to the name you already chose to give the affair. Either way, the invitation remains unanswered.
The choice now is how much access an enemy can buy by delivering a worse one.{/n}''',
      c('"Take her evidence. Give her no private access to either of us."', "end", flags=f("lodge_offer_bounded")),
      c('"Let her think the offer interested us. Make her name the other patrons before we answer."', "end", flags=f("lodge_offer_bait"))),
    n("end", "Nocticula", '''"I will send the answer in my own name. Your choice about public credit has not become permission to write every new threat beneath it."
{n}She closes the cage's small door and places it beyond the papers. The moth begins to move. Its painted wings make the supposed treasure flicker in and out of existence.
She takes three replies from beneath the cage. Edris has asked when she can leave. Rhez's coat is ruined. Istrava wants Suth's name printed above her own.
Nocticula signs Edris's passage order, adds a coat to Rhez's payment, and holds Istrava's reply to the lamp.{/n}
"She may keep her scapegoat. I am keeping the guest list."
{n}The burning paper lights her mouth. She catches your hand before you can gather the scattered reports.{/n}
"Leave them. The next threat can wait until I wake you."''', c('[Let the chosen pressure and the reply to Istrava take effect.]', flags=f("lodge_answer_sent"))),
], "lodge_hunt_ended")

s("unborrowed_evening", "An evening she did not borrow", [
    n("start", "Narrator", '''{n}This time she does not bother with a stair or a mask. You close your eyes in Drezen and open them in a high room in her palace, at a window, with the whole of Alushinyrra lying below you on fire.
It is not burning. It only looks that way at night: the Middle City in its terraces of red lamps, the Fleshmarkets glowing like a brazier, the black canals between them catching the light and throwing it back. Somewhere down there is a hunting lodge with its doors kicked in. From here you cannot tell which light it is.
Nocticula is sitting in the window. She has not changed since the hunt. There is still dried blood at the hem of her black gown that is not hers, and a smear of moth powder, gold and grey, along one cheekbone. She is cutting a pear on the sill with a plain kitchen knife, and she is eating the slices off the blade.{/n}
"I'm hungry," {n}she says, without looking round.{/n} "A hunt does that. It always has. Mortals think it's the blood. It's the running. Everyone running at once, in the dark, and only one of them going to be caught, and none of them knowing which."
{n}She holds the pear and the knife out to you, one in each hand.{/n}
"Peel it. I want to watch your hands do something careful after tonight."
{n}You take them. The pear is cold, as if it has come out of a well, and the knife is sharper than it looks. She watches your hands the whole time, the way she watched the bell chamber, and when the peel comes away in one long curl she takes it from your fingers and eats that too.{/n}
{n}Below the window a procession is crossing the nearest bridge: lanterns, a curtained litter, a line of slaves on a chain shuffling behind it. She points at it with her chin.{/n}
"One of Istrava's guests. Going home. He thinks he got out of that garden because he's clever." {n}She bites a slice off the blade.{/n} "He got out because I left a gate open for him, so that he'd go home and tell everyone on his street what he saw. By morning the whole Middle City will know whose garden it was. Dead guests don't gossip. Frightened ones never stop."
"And Istrava?"
"In her own cellar, with Rhez sitting on the door eating an apple. I'll go and look at her tomorrow night. I want her to have one whole day to think about what I'm going to do to her, and I haven't decided, and she knows that too." {n}She licks pear juice from her thumb.{/n} "Most of them break on the thinking, darling. The chains are only for decoration."
"You found her," {n}she says.{/n} "Or you chose who'd be found, which is better. Do you know how long it has been since anybody gave me a name for a bell? Nobody gives me anything. They pay me. It's not the same." {n}She leans back against the window frame and puts her bare feet up in your lap, as if you were furniture she had bought for the purpose.{/n} "Sit. No, closer. The knife stays on the sill. I like to see it there while I decide."
"Decide what?"
"Whether I'm going to be patient." {n}She smiles. It is not a reassuring smile.{/n} "I was patient all evening. I let her talk. I'm tired of it."''',
      c('[Sit beside her. Let her have the night.]', "close", flags=f("lodge_evening_close")),
      c('"Talk to me first. Tell me what you see from this window."', "talk", flags=f("lodge_evening_talk")),
      c('"Not tonight. Send me back to Drezen."', "leave")),
    n("close", "Nocticula", '''{n}You sit where she has decided you will sit, with her feet in your lap and the city burning at your back. She takes the pear out of your hand and bites it, and then she takes your jaw in the same sticky hand and kisses you, and her mouth tastes of pear and of something under it, metallic, from the gardens.
She does not let the kiss end when you would end it. She ends it when she likes, and pulls back an inch, and looks at you from very close.{/n}
"There," {n}she says.{/n} "That's what I wanted in her hall, with my foot on her neck. I thought about it the whole time she was begging." {n}Her thumb moves along your lower lip, wiping off the juice, not gently.{/n} "Don't look shocked. You were watching through my eyes. You know exactly what I was thinking."
{n}You do. That is the uncomfortable part.
The knife lies on the sill beside her hip, where she can reach it and you cannot. She sees you notice, and is pleased.{/n}
"Now," {n}she says.{/n} "You can ask me what I was hoping you'd ask. Or you can stop talking."''',
      c('"Why here? Why this window, and not your bed?"', "want")),
    n("talk", "Nocticula", '''{n}She looks at you for a long moment, as if deciding whether to be insulted. Then she takes her feet out of your lap, turns on the sill, and looks out.{/n}
"Everything," {n}she says.{/n} "I see everything from this window. That's why I took it."
{n}She points with the knife. The tower you are in, she tells you, belonged to somebody else once, a long time ago. A demon of some importance, who liked the view, and liked her, and had her brought up here to look at it with him. She does not remember his name. She remembers that he talked through the whole evening about what he owned, pointing at it, and that she let him, and that when he finally took her to bed she killed him in it, and then she came back to this window, alone, and looked at the city, and decided she wanted all of it.{/n}
"It took longer than the evening," {n}she says.{/n} "Not much longer. Most of the people who owned those lights died in beds. The rest died in worse places. I built the islands on what was left of them." {n}She looks at you sideways.{/n} "Don't make that face. You asked what I see. I see everything I took."
"And tonight?"
"Tonight I took one more house, and watched a hostess learn whose hunt it was in a garden she thought was hers, and someone I like stood at a rail and decided it." {n}She cuts the last of the pear in two and gives you half.{/n} "That's a good night, in Alushinyrra. You should be flattered I shared it."''',
      c('"Why bring me up here, then?"', "want")),
    n("leave", "Nocticula", '''{n}She stops chewing. For a moment the only sound in the room is the noise of the city coming up through the window, music and screaming and bells, the ordinary noise of Alushinyrra at night.
Then she takes her feet out of your lap and puts them back on the floor, one at a time, very deliberately.{/n}
"Not tonight," {n}she repeats.{/n} "After a hunt. After I gave you my eyes. You stood in my city and chose who'd be torn apart, and you enjoyed it; I know you did, I was inside your head. And now you'd like to go home to your cot." {n}She laughs, and it is genuinely amused, which is worse than if it were angry.{/n} "Oh, darling. The work isn't the part you're afraid of, is it? It never is, with your sort."
{n}She leans close, close enough that you can smell the gardens on her: crushed leaves, spilled wine, a stranger's blood gone brown at her hem.{/n} "You're afraid of the part where you lie here afterwards and know you liked both. The hunt and me. The same night, with the same hands." {n}She taps the flat of the knife against your knuckles, once, not quite hard enough to cut.{/n} "Get used to it. I did, a very long time ago, and look how well I've done."
"The work goes on. I'm not walking away from the lodge."
"I know you're not. I'd have you brought back if you tried." {n}She picks the knife up off the sill and cleans it on the hem of her gown, slowly, both sides.{/n} "I keep a list of nights owed. It's a very short list; most people don't live long enough to be on it. You're on it now. I'll collect when it suits me, and you won't be asked." {n}She sets the knife down.{/n} "Go on, then. I'll send for Laulieh. She's never once told me not tonight."
{n}She lifts two fingers. Your cot in Drezen is suddenly very hard, and very cold, and you can still taste the pear.{/n}''',
      c('[Wake in Drezen. The work goes on; the night is owed.]', flags=f("lodge_evening_finished", "lodge_evening_declined"))),
    n("want", "Nocticula", '''"Because up here nobody in that city knows what I'll do next. Not Shamira, not my brother, not the dealers in the Fleshmarket who bet on my moods." {n}She turns the knife on the sill so that the lamplight runs along it.{/n} "Everything down there I took from somebody. You I only borrow, a night at a time, out of your cot. I want to see what you do with the nights."
{n}She sits up. Her eyes, without the black silk, are the eyes you looked out of in the garden: very bright, very patient, entirely without pity.{/n}
"You asked me nothing all night. You chose. Now I'm going to ask." {n}She points the knife at you, lightly, the tip just touching your breastbone.{/n} "What do you want, Commander? When there's no crusade watching and nobody kneeling. Not what you're owed. What you want. And which of your wants do you ruin for yourself, because you're afraid of what it would make you?"''',
      c('"I keep looking for the next danger. Sometimes I bring it into rooms where it was not invited."', "honest", flags=f("lodge_vigilance_admitted")),
      c('"I enjoy being necessary. I have called it duty when appetite would have been more honest."', "honest", flags=f("lodge_appetite_admitted")),
      c('"Small things. A meal while it is still hot. A voice without a report behind it. Enough sleep that waking is not an argument."', "want_small", flags=f("lodge_vigilance_admitted")),
      c('"Power. More of it than I have, and yours to measure it against."', "want_power", flags=f("lodge_appetite_admitted")),
      c('"The moment before the knife comes out. I have never found anything to match it."', "want_danger", flags=f("lodge_appetite_admitted")),
      c('"You. Here. With the knife put down."', "want_pleasure", flags=f("lodge_appetite_admitted"))),
    n("want_small", "Nocticula", '''"How very mortal." {n}She says it the way another woman might say how very rare, and eats the slice she has cut.{/n} "A hot meal. I've had kings poisoned in the middle of theirs, and you want one. I could give you every one of those things tonight in a dream, finished, never cold." {n}She does not. She watches you understand that she has chosen not to.{/n} "No. You'd stop wanting them, and then what would I hold over you?"''',
      c("Continue", "honest")),
    n("want_power", "Nocticula", '''{n}Her eyes brighten, the way a cat's do at a movement in the grass.{/n} "At last, an appetite with teeth. Measure it against mine, then, and discover how short your ruler is." {n}She taps the flat of the knife against your knee, once.{/n} "Most mortals who want power want the chair. The clever ones want the person who gives the chairs away. I haven't decided which you are. Either way, I'll enjoy watching you try."''',
      c("Continue", "honest")),
    n("want_danger", "Nocticula", '''{n}She turns the knife so the lamplight runs along the edge, and lays it on the sill between you, point toward your hand.{/n} "Then you've come to the right window." {n}She does not pick it up again.{/n} "I've killed people for sitting where you're sitting. I may yet kill you for it. And you're enjoying this more than the pear." {n}Her smile is slow.{/n} "So am I. How inconvenient for us both."''',
      c("Continue", "honest")),
    n("want_pleasure", "Nocticula", '''"Put down?" {n}She looks at the knife on the sill beside her hip, and back at you.{/n} "It's on the sill, where I can reach it. That's as down as it goes." {n}Her foot finds your thigh and stays there.{/n} "You ask for so little, for a Commander. I'll have to teach you to be greedier. Not all at once. I want to see how long you can bear to want it."''',
      c("Continue", "honest")),
    n("honest", "Nocticula", '''{n}She cuts the last slice of pear and holds it against your lower lip. When you reach for it with your mouth she draws it back and eats it herself.{/n}
"That's a better confession than most," {n}she says.{/n} "It hasn't cost you anything yet, which is why you could say it. I'll make it cost something later. I'm good at that."
{n}She turns back to the window. Below, the city goes on burning. A bell is ringing somewhere toward the Fleshmarkets, a big one, for a sale.{/n}
"Istrava asked me tonight, while she was begging, why I care what one lamia does in one garden. It's a reasonable question. I have a thousand Istravas." {n}She is quiet for a while.{/n} "The answer is that she did it with my name. She made her guests feel safe by telling them I was watching over the house. I was. I was watching her steal from me, and enjoying it, and waiting for the right evening." {n}She glances at you.{/n} "And then you came, and it was the right evening."
{n}It is the nearest she has come to saying anything kind. She leaves it there, at the window, with her face turned away from you so that you only see the side of it, gold with moth powder. Then she turns back, and it is gone, and she is smiling.{/n}
"Don't make anything of that," {n}she says.{/n} "Go home. I'll send for you when the house is ready."''',
      c('[Watch the city burn with her until the dream lets go.]', flags=f("lodge_evening_finished"))),
], "lodge_answer_sent")

s("bell_without_master", "A bell without a master", [
    n("start", "Narrator", '''{n}The next night she takes you back to the lodge.
It is empty now, or nearly. The candles are out. The couches in the dining hall have been righted and stripped, and someone has scrubbed the tiles, not well; in the light of the lamp Nocticula carries you can see where the scrubbing gave up. The garden doors are boarded. The smell of musk is still in the walls.
She walks it the way a woman walks a house she has just bought: slowly, touching things, opening cupboards to see how deep they go. She runs a finger along the back of Istrava's couch and looks at the dust on it and wipes it on the wall. She tries the bell chamber stair and finds the third step creaks, and goes up and down it twice to be sure.
The bell itself lies on the floor of the hall, where it fell. A little brass thing, no bigger than a fist, dented on one side. Nocticula nudges it with her bare toe, and it rolls, and gives a small flat note.{/n}
"What does one do with a hunting lodge?" {n}she asks you.{/n} "Hunt, darling. Obviously. The question is who."
{n}Below your feet, through the floor, something knocks: slow, heavy, irregular, like a tail striking stone.
Istrava is in her own cellar. Rhez put her there last night and has been sitting on the cellar door since, with her coat over her shoulders, eating an apple. When Nocticula comes past she gets up and opens it without being told, and the smell that comes up is wine and damp and lamia. In the dark at the bottom of the stair the hostess of the house lies chained to her own racks by the throat and the wrists and the root of the tail, and her hair is full of empty cages.{/n}
"She hasn't stopped talking," {n}Rhez says.{/n} "I put a cork in her for an hour. She talked round it."
"She'll stop when I'm finished with her," {n}Nocticula says.{/n} "And the guests?"
"The ones who are left? Upstairs. In the long room. Still drinking." {n}Rhez shrugs.{/n} "They think they're your guests now. Nobody told them otherwise."
{n}Nocticula smiles at that, and closes the cellar door on the knocking, and turns to you with the lamp held up so that she can see your face.{/n}''',
      c('"What did her list give you?"', "bounded", requires=f("lodge_offer_bounded")),
      c('"Did she sing every name before she understood she\'d bought nothing?"', "bait", requires=f("lodge_offer_bait"))),
    n("bounded", "Nocticula", '''"Everything she had," {n}Nocticula says.{/n} "Which is what one gets, promising nothing. People give much more when they're not sure of the price."
{n}She tells you what the list was worth, ticking it off on her fingers like a girl counting presents. Eleven patrons who paid for this season's hunts, and where they sleep. Four other houses that run the same game under her protection, smaller and quieter, in the Ten Thousand Delights. A Fleshmarket dealer who rented Istrava her quarry by the night and took them back afterwards in whatever condition they were in.{/n}
"I've visited two of the patrons already, this afternoon," {n}she says.{/n} "One of them is in the cellar now, beside her; I thought she'd like the company. The other wasn't at home, so I took his house instead. I'm going to have so many houses." {n}She sounds delighted.{/n} "The dealer I'm saving. He'll keep. Dealers always think they can sell their way out, and I want to hear what he offers."
"And Istrava? What does she think she bought?"
"Nothing. I told her nothing, and she believed me, which is the only clever thing she's done all year." {n}She swings the lamp toward the cellar door.{/n} "She keeps asking me what I'm going to do with her. I keep telling her I haven't decided. It's true. I like to watch her hope."''',
      c('"Then decide what the house is for."', "judgment")),
    n("bait", "Nocticula", '''"Every one," {n}Nocticula says, with enormous satisfaction.{/n} "Every patron, every house, every dealer who ever rented her a body for the night. She sang it like a canary. She thought each name was buying her another hour, and so it was, in a way. She just didn't know how few hours there were."
{n}She tells you about the moment Istrava understood. It was near the end, after the last name. Istrava had stopped, and waited, and looked up from the floor at the Lady in Shadow sitting in her chair, and asked what she had bought. And Nocticula had told her: you, darling, have bought the right to know that you told me everything. Nobody else in the city will ever be able to say that.{/n}
"Her face," {n}Nocticula says. She closes her eyes, remembering it, and smiles.{/n} "You gave me that. You said: let her think she's buying her life. I'll keep that face in my collection forever."
"Has the story got out?"
"Of course it has. Half the Middle City knows Istrava tried to buy herself from me and was robbed in the process. Several of them have written to say how shocked they are that I'd bargain with such a creature." {n}She laughs.{/n} "They're terrified I'll bargain with them. Good. Let them write. Let them wonder what I'd charge."''',
      c('"Then decide what the house is for."', "judgment")),
    n("judgment", "Nocticula", '''{n}She sets the lamp down on Istrava's couch and walks out into the middle of the hall, where the bell lies, and turns round slowly, looking up at the bell chamber, the gallery, the boarded garden doors.{/n}
"I can think of three things to do with it," {n}she says.{/n} "I can burn it. Tonight, with the guests upstairs, still drunk, still thinking they're mine. Leave the doors open; it'll draw better. The whole Middle City will see it from the canals, and everyone who ever paid to hunt in a house under my protection will know exactly what the smoke means."
{n}She nudges the bell with her toe again. It rolls.{/n}
"Or I can keep it. Hunt here myself. It's a good house for it; she was a fool but she had taste. I'd keep her in the cellar for the season and let her out on the first night, and see how well she knows her own gardens when she's the one running." {n}Her eyes glitter.{/n} "Or I give it to Rhez. On a leash. Rhez has never been given anything in her life. I want to see whether she bites."
{n}Rhez, in the doorway with her apple, says nothing at all. She has stopped chewing.{/n}
"You decide," {n}Nocticula says to you.{/n} "I'll enjoy any of them. That's the luxury of owning things."''',
      c('"Burn it. Guests inside."', "close", flags=f("lodge_closed_house")),
      c('"Keep it. Hunt here yourself."', "keep", flags=f("lodge_kept_house"))),
    n("close", "Nocticula", '''"Oh, good," {n}she says, softly.{/n}
{n}She does it herself. She goes up the stair to the long room, where you can hear the guests laughing, and opens the door and says something, and the laughing gets louder. Then she comes back down and locks the door behind her with Istrava's own key, and drops the key into the bell's mouth, and touches the wall.
The fire starts in the walls, not on them. It comes up through the plaster like a blush. In a few breaths the whole upper floor is roaring, and the laughing has turned into something else, and fists are hammering on the locked door, and then not.
At the last moment she goes down into the cellar, alone, and comes back up the stair dragging Istrava by the chain round her throat. The hostess is coughing, sooty, her tail thrashing on the steps. Nocticula hauls her out into the yard like a sack and drops her on the gravel.{/n}
"For the collection," {n}she says to you, a little breathless, delighted.{/n} "I couldn't let her miss it. Look, Istrava. Look at your house."
{n}Istrava looks. Behind you the lodge burns, all of it, the gallery and the cabinets and the bell chamber, and the light of it goes up over the old pleasure garden and out across the canals, and down in the Middle City people come out onto their roofs to watch.
Nocticula stands in the yard with the fire on her face and her hand wound in the chain, and laughs, long and hard, the way she laughed in the throne hall when the court laughed with her. There is nobody here to laugh with her now except Rhez. Rhez does.{/n}''',
      c('[Watch it burn.]', "last", flags=f("lodge_payment_advanced"))),
    n("keep", "Nocticula", '''"Yes," {n}she says, and you can hear that it is the answer she wanted.{/n}
{n}She goes down into the cellar, and you go with her, and she crouches in front of Istrava in the wet dark and takes her chin in one hand and turns her face up to the lamp.{/n}
"You're staying," {n}she tells her.{/n} "Isn't that nice? It's your house. You know every hedge in that garden, every dry fountain, every hole in the wall. I'm going to open the house again at the end of the month, with new guests, and on the first night of the season I'm going to take the chains off you and ring that little bell, and they're going to find out how well you know it." {n}She pats Istrava's cheek.{/n} "If you're very clever, you'll last till dawn. If you last till dawn, I'll put you back down here, and we'll do it again next season."
{n}Istrava says nothing. She has finally stopped talking.
Upstairs, Nocticula gives her orders. The guests in the long room are to be woken and thanked and sent home, all of them, with a gift each: an invitation to the opening of the season, in Istrava's hand, under Nocticula's seal. They will all come. Nobody refuses the Lady in Shadow's invitations, and it will be an excellent opportunity to see which of them were Istrava's friends.{/n}
"I'll keep the bell," {n}she says, picking it up off the floor and turning it in her fingers.{/n} "Dented. I like it dented. It'll remind her."''',
      c('[Leave Istrava in her cellar for the season.]', "last", flags=f("lodge_information_post"))),
    n("last", "Nocticula", '''{n}When you come out into the yard there is a man waiting there under guard.
It is Suth, the collector from the gallery. He has been kept somewhere overnight, and it shows: his plain coat is torn, there is blood dried in his beard, and both his hands are bound up in rags, because Rhez spent part of the night asking him questions about them. But he has his chain of office round his neck still, and his tally-stick in his belt, and when he sees Nocticula he goes down on one knee on the gravel, carefully, like a man who has knelt to a great many important people and knows exactly how low to go.{/n}
"Lady," {n}he says.{/n} "With respect. I'm a collector. Lawful. I've a hall in the Middle City and forty men and my paper's good in every court on the islands." {n}He nods toward the gate, where Edris and Mera stand with Rhez.{/n} "Those two cunts owe me forty silver apiece. Their mother sold them to Istrava's house on my credit. They carry my marks. Lawful debts, Lady. I'm only asking what's mine."
{n}Nocticula looks at him for a long moment. Then she looks at Rhez.{/n}
"Rhez," {n}she says,{/n} "he said 'owe'. In my house."
"I heard him, Lady."
"Lawful." {n}She tastes the word.{/n} "In my city. Say it again, Suth. Slowly. I want Rhez to hear it properly."
{n}Suth does not say it again. He has gone very pale above the beard. He is looking at you now, because you are the only one in the yard who has not yet said anything, and he has seen in the gallery who chose the name for the bell.{/n}
"Well, darling?" {n}Nocticula says.{/n} "What do I do with a man who collects in my city on paper I never signed?"''',
      c('"Send his hands to his collectors\' hall."', flags=f("lodge_judgment_finished"))),
], "lodge_evening_finished")

s("counterseal", "The name beneath the debt", [
    n("start", "Narrator", '''{n}The quay has acquired a desk with one short leg. Nocticula has folded a petition beneath it. Each time she sets down her pen, the desk rocks just enough to make her glance at the offending corner.
A letter lies open before her. Its seal shows a hand holding another hand by the wrist.{/n}
"You have received an appeal," {n}you say.{/n}
"I have received an invoice which has learned to plead. The distinction becomes clearer near the bottom."
{n}She turns the letter toward you. A broker named Tazren financed purchases for Istrava's household. He claims the departure of her attendants has deprived his clients of the labor against which those purchases were secured. Since Nocticula arranged the departure, he suggests the obligation has passed to her.
His list includes Mera. Beside her name is a charge for the shoes she recovered from the cabinet. He describes them as an advance made for her benefit.{/n}
"Her mother's shoes," {n}you say.{/n}
"An unusually personal loan."
"He knows what they were."
"Probably. He would like me to correct the description while accepting the debt. Then we may argue about the price of an object he never owned."
{n}The letter does not disclose the sisters' destination. It names their former rooms in the lodge, information any supplier might have obtained. Nocticula's messengers have been told to bring further correspondence to her clerk, without confirming where the women went.{/n}
"You could kill him."
"Certainly. His clients would auction the claim before his chair cooled. I want to know whose signature makes them believe it is worth bidding on."
{n}She lifts the desk with one hand and takes out the folded petition. The wobble stops while she holds it. With the other hand she offers you the damaged paper.{/n}
"He sent that yesterday. Read what he wanted before he learned to call it a debt."''', c('[Read the earlier petition against the invoice.]', "petition")),
    n("petition", "Narrator", '''{n}Yesterday Tazren requested permission to announce that his clients supplied Nocticula's new household. He offered favorable terms on furnishings and credit. The invitation was addressed to the household whether or not the lodge remained open.
At the bottom, in smaller writing, he promised to settle outstanding obligations attached to any persons entering her protection. A courteous service, the sentence calls it. Nocticula has drawn a line beneath those words.{/n}
"He offered to collect their debts for you."
"He offered to decide which debts existed. An industrious man."
"And when you did not answer?"
"He supplied a debt with my name on it. If I pay, he has a transaction to show the next frightened person. If I simply tell him I owe nothing, he can announce that I have abandoned the people whose escape produced the bill."
{n}You compare the dates. The invoice predates the letter offering to arrange the obligations. Tazren has altered one figure, but the impression of the old ink remains visible in the copy she supplies.
Nocticula waits while you notice it.{/n}
"You already saw that."
"Yes. I wanted to discover whether you would propose burning the letter before reading the useful part."
"I am fond of making a creditor explain himself before the fire."
"Then we may yet have a pleasant evening."
{n}The broker has enclosed a summary, not the original agreements. His own fees form the largest part of the supposed debt. A smaller sum was guaranteed by an unnamed patron of the lodge. That signature could identify someone who paid for the hunt and has not appeared in Istrava's account.
Nocticula wants the original. She has not sent for Mera to obtain it. The woman's denial would establish what she remembers; it would not reveal what the patron signed elsewhere.{/n}''', c('"He has given us a reason to demand the papers. Has he given us a way to get them?"', "price")),
    n("price", "Nocticula", '''"He will sell. He makes his living by arriving before the collector and leaving before the argument. When this is finished, I shall find him somewhere to arrive that he cannot leave."
{n}She puts two blank sheets on the desk. One is narrow enough for a public notice. The other has the broad margin of a purchase agreement.{/n}
"We can reject the transfer openly. Name the false charge, refuse to acknowledge his authority over my household, and warn anyone buying the claim that I intend to dispute it. He may keep the original. He will have fewer people eager to finance his interpretation."
"Or you can buy it."
"Buy the original schedule and the guarantor's obligation. Cancel the entries against the attendants. Keep the claim against the person who paid to make them quarry."
"He receives money for inventing part of the bill."
"Less than he hoped. More than you would enjoy. I would be purchasing evidence as well as an obligation."
{n}She touches the wide margin with her pen, leaving a dot of ink where a signature might begin.{/n}
"I would like to collect from that patron. I would also like Tazren to discover that separating his fees from the principal makes him much poorer. Those pleasures do not prove the purchase wise. They do make it attractive."
"And the people on his list?"
"Receive the canceled originals if I obtain them. Receive a warning and my public refusal if I do not. Neither answer requires them to return here and earn my interest by telling the story again."
{n}You look at the desk's short leg. Nocticula follows your glance and restores the folded petition beneath it.{/n}
"I know," {n}she says.{/n} "A ruler of my resources should possess better furniture."
"I was thinking you could fix it."
"I could. For the moment I enjoy knowing precisely which petition is supporting my work."
{n}She waits for your answer with the pen still in her hand. This time she has told you what she wants before offering the choice.{/n}''',
      c('"Deny it publicly. Make selling this claim dangerous. I will not help him establish a price for releasing people he never owned."', "deny", flags=f("lodge_debt_denied")),
      c('"Buy the original and strip out his inventions. Cancel the servants\' entries. Then let his patron discover who now holds the honest part of his debt."', "purchase", flags=f("lodge_debt_purchased"))),
    n("deny", "Nocticula", '''"You are leaving me with a useful suspicion and no signature."
"I am leaving him with a claim you have publicly challenged. He wanted your name to make it valuable. Give him your name."
{n}She looks at the narrow sheet again. Her pen moves before she answers.{/n}
"I can make that an unpleasant gift."
{n}The notice names the altered date and the false charge for the shoes. It does not print the sisters' present whereabouts or invite other creditors to send their accounts. It states that leaving Istrava's service transferred no obligation to Nocticula and grants no collector permission to seize the former attendants under her authority.
She stops before adding a threat against anyone who buys the paper.{/n}
"An extravagant threat is cheap to repeat. It becomes expensive the first time someone tests whether I can find him."
"Then promise the part you will do."
"I will publish the objections with every attempted sale brought to my attention. I will pay for the names of the buyers. That will make Tazren calculate the value of keeping his original."
{n}She signs. Her irritation has become concentration, without becoming agreement that this was her preferred use of the evening.{/n}
"If this costs me the patron's name, I shall remind you."
"If buying it would have taught him to send another invoice, I shall be unable to prove it."
"How refreshing. An argument which admits where its victory cannot be counted."''', c('[Send the public challenge and watch who still tries to buy the claim.]', "end")),
    n("purchase", "Nocticula", '''"At last. Someone who can dislike a practice without becoming incurious about its records."
"Read the price before you congratulate me. I want the canceled entries delivered to the people named in them. Not a promise that you will never collect."
{n}Her smile narrows. She draws the broad sheet toward herself.{/n}
"You think I would keep the option."
"You have explained several times how much you enjoy options."
"I have been unusually instructive."
{n}She writes the cancellation into the purchase. No attendant's obligation can be sold on or held as security. The patron's guarantee must be produced in its original form; an assertion that such a document once existed will earn Tazren nothing. A clerk is to compare the dates before payment, and another is to witness the canceled entries being separated from the remaining account.
The price is lower than the summary demands. Nocticula explains which invented fees she has removed with the pleased precision of someone describing a rival's failed entrance.{/n}
"He can refuse," {n}you say.{/n}
"Yes. Then I have the letter in which he offered to sell an original he now refuses to produce. We begin again from there."
{n}She leaves room beneath the offer for his answer. The purchase has not occurred merely because she wants its result.{/n}
"When I collect from the guarantor, you may find him quite pitiful."
"I will read what he agreed to buy."
"Do. I should dislike discovering that you found my appetite attractive only while I was discussing it."''', c('[Offer the limited purchase, conditional on verified originals and canceled servant claims.]', "end")),
    n("end", "Nocticula", '''{n}The copied seal remains on the desk after she puts away the papers. One hand holds another by the wrist, and the tiny cut between them has filled with dark wax.
You turn it toward her.{/n}
"An unfortunate emblem for a man hoping to conduct business with you."
"He believes it depicts assistance."
"Does he?"
"He believes his clients enjoy calling it that. The distinction has fed him for years."
{n}Nocticula takes the seal between finger and thumb. For a moment you expect her to crush it. Instead she puts it beside the order she will send when this meeting ends.
You have seen enough of her correspondence to recognize the gesture. She keeps the things she may want to contradict precisely.{/n}
"You made me state the part I intended to keep," {n}she says.{/n}
"You had already stated the part you wanted."
"Do not grow complacent. There are evenings when the distinction will matter more than this one."
{n}You tell her you expect to notice. She gives you a look in which pleasure and skepticism are equally evident.
When the desk disappears, its short leg leaves a crooked impression in the dust. She removes that too. The papers go last.{/n}''', c('[Await the broker\'s answer and the survivors\' departure report.]', flags=f("lodge_debt_answered"))),
], "lodge_judgment_finished")

s("no_applause", "No applause at the departure", [
    n("start", "Narrator", '''{n}Dawn, in so far as Alushinyrra has one: a thinning of the red over the Middle City, and a grey light coming up off the canals.
She has brought you to a gate. It is one of the old landward gates of the Middle City, a high black arch with the docks beyond it and the long road down to the water, and the night's traffic is coming in through it: carts of meat, a coffle of slaves on a chain, a drunk incubus singing. Just inside the arch there is a stone bench, and Nocticula is sitting on it with her legs crossed, eating cherries out of a paper twist and spitting the stones into the gutter.
Across the road, against the wall of a cookshop, stand Edris and Mera. They have a trunk between them, a small cheap one with a broken strap, and Mera is wearing her mother's red shoes. They are holding hands. They look the way people look when they have been told something very good and have not yet worked out what is wrong with it.{/n}
"I took my flower off them this morning," {n}Nocticula says.{/n} "Both of them. Stood them in front of me and took it off, like a collar. They're free." {n}She spits a stone.{/n} "Do you know what free means, in my city?"
"Tell me."
"It means nobody's. It means that anyone who catches them may keep them." {n}She holds out the twist of cherries to you.{/n} "Every dealer in the Fleshmarket knows their faces by now. Every collector. Every bored thing on the docks that likes the look of red shoes. I've given them the road, and the morning, and nothing else. Let's see how far a bird gets without a cage in Alushinyrra."
{n}Mera has noticed you. She is looking across the road at the Lady on the bench with an expression you cannot read: fear, certainly, and something sharper than fear.{/n}''',
      c('"There\'s still smoke on the hill."', "closed_account", requires=f("lodge_closed_house")),
      c('"And your new house? Did the season open?"', "kept_account", requires=f("lodge_kept_house"))),
    n("closed_account", "Nocticula", '''{n}She follows your look. Up on the hill above the old pleasure garden a thin column of smoke still stands against the grey, going straight up in the windless air.{/n}
"It burned all night," {n}she says, pleased.{/n} "I sat up and watched. The Middle City sat up with me; I could see them on the roofs. Three other houses closed their doors before morning without being asked. One of them sent me its bell in a box, with a very frightened letter." {n}She smiles.{/n} "I'm going to have a shelf of bells. Istrava's I keep by my bed. She has a cage in my gallery now, and every night I ring it once, and she flinches. It's a lovely sound."''',
      c('"And the collector?"', "debt_report")),
    n("kept_account", "Nocticula", '''"Last night." {n}She looks satisfied enough to purr.{/n} "New guests, new masks, the same old gardens. They all came; nobody refuses my invitations. I took the chains off her myself at midnight and rang her own little dented bell, and you should have seen her go."
"Did she last till dawn?"
"She lasted till the second fountain. They brought her back with a guest's teeth still in her tail, and I put her back in the cellar to heal for next time." {n}She eats a cherry.{/n} "Whoever holds the keys to that house, it's mine. That's the point of it. Every guest who came last night knows now what happens to a house that hunts on my name, and every one of them was too frightened to leave early." {n}She spits the stone.{/n} "Good business. Better sport."''',
      c('"And the collector?"', "debt_report")),
    n("debt_report", "Narrator", '''{n}At the name, Edris looks up sharply from across the road. Mera's hand tightens on her sister's. Nocticula sees both and is amused, and does not lower her voice at all when she answers.{/n}''',
      c('"Did his hands reach his hall?"', "debt_refused", requires=f("lodge_debt_denied")),
      c('"Is he collecting for you yet?"', "debt_bought", requires=f("lodge_debt_purchased"))),
    n("debt_refused", "Nocticula", '''"In a box. Rhez took them herself, and set them on his table in front of his forty men, and asked who was in charge now." {n}Nocticula spits a cherry stone into the gutter.{/n} "Nobody was. They've closed the hall. They're selling his paper in the Fleshmarket by the bale, very cheaply, and nobody is buying it, because nobody wants to be the next collector to say 'owe' in my city."
{n}Across the road Mera has heard every word. She is staring at Nocticula. Edris has one hand pressed flat over her own mouth.{/n}
"So there's no paper on them anywhere now," {n}Nocticula says.{/n} "Nobody's chasing them for a debt. They're simply free." {n}She smiles at the sisters, and waves her fingers at them.{/n} "Which is a different thing entirely."''',
      c('"How is Rhez\'s arm?"', "wound", requires=f("lodge_rhez_hurt")),
      c('"What does Rhez want next?"', "agent", requires=f("lodge_unmarked", "lodge_silent_bell")),
      c('"What does Rhez want next?"', "agent_announcement", requires=f("lodge_unmarked", "lodge_self_invitation"), forbids=f("lodge_silent_bell"))),
    n("debt_bought", "Nocticula", '''"He started this morning." {n}Nocticula tilts her head toward the far end of the road, where it goes down between the warehouses to the docks.{/n}
{n}You look. Down there, under a cookshop awning, a lean man in a plain coat is standing with half a dozen others round him, and his hands are bandaged, and he has a new chain of office round his neck. Even from here you can see that the badge on it is a black flower.{/n}
"He collects for me now," {n}she says.{/n} "His hall, his forty men, his lovely paper; all mine. I bought him for the price of his hands, and gave him the hands back. He's very grateful. You'd be surprised how hard a grateful man works." {n}She spits a stone.{/n} "And he does know those two. Their faces. Their mother. The street their aunt lives on. He knows them better than anyone in Alushinyrra."
{n}Across the road Edris has seen him too. She has gone very still.{/n}''',
      c('"How is Rhez\'s arm?"', "wound", requires=f("lodge_rhez_hurt")),
      c('"What does Rhez want next?"', "agent", requires=f("lodge_unmarked", "lodge_silent_bell")),
      c('"What does Rhez want next?"', "agent_announcement", requires=f("lodge_unmarked", "lodge_self_invitation"), forbids=f("lodge_silent_bell"))),
    n("wound", "Nocticula", '''"Healing. She can use the hand. She can't yet fasten the coat without swearing, which she does beautifully." {n}Nocticula looks pleased with Rhez, the way one is pleased with a good horse.{/n} "She came to me yesterday and asked for the man with the jeweled snout. The one who opened her arm. I'd kept him for her."
"What did she do with him?"
"Nothing yet. She's making him wait in a cell beside the one where Vhal is giving his evidence. Vhal gives it standing up, by the way, for as long as it takes; I thought that was fair, for a man who used to make the servants stand all night." {n}She eats a cherry.{/n} "When they've both finished, Rhez may decide which hand each of them leaves my city with. I thought she'd like to choose. You see, darling, I can be generous with the people who bleed for me."''',
      c('"Let Rhez collect. Then let\'s see your wager."', "credit")),
    n("agent", "Nocticula", '''"The next job." {n}Nocticula smiles.{/n} "She always wants the next job. She came to me last night with her coat on and asked what was after Istrava, and I told her nothing, yet, and she looked so disappointed that I almost found her someone to kill on the spot."
"Will you?"
"Of course. Something worthy of her. There's a dealer in the Fleshmarket who rented Istrava her quarry by the night. I've been saving him." {n}She spits a stone into the gutter.{/n} "Rhez is a knife I spent years sharpening. A knife you don't use goes dull, or goes looking for another hand. I don't let my knives go looking." {n}She glances at you.{/n} "Remember that, the next time you feel restless."''',
      c('"Give her the dealer. Then let\'s see your wager."', "credit")),
    n("credit", "Nocticula", '''{n}She settles back on the bench and wipes cherry juice off her fingers on your sleeve.{/n}
"You bet against your own hand, or with it, and you didn't even notice." {n}She sounds delighted with you.{/n} "Two nights ago, in that yard, you decided what Suth was. That decided everything. I knew how this morning would end the moment you said it. I only asked you to bet on yourself."
{n}She pulls a little iron key out of her bodice and drops it in your lap. It is warm.{/n}
"Istrava's strongbox. I had it carried up from her cellar before I burned or kept anything. If that was a win, it'll be in Drezen before you wake, and you can buy your crusade something shiny with a lamia's money." {n}She leans close.{/n} "If it wasn't, you owe me. Not gold. I don't want your gold. I'll collect at a time of my choosing, and you won't like the time."
{n}She kisses the corner of your mouth, quickly, and sits back to look at you.{/n}
"So. You've watched me hunt, and burn, and set two birds loose to see how far they get. You've helped with all of it. And you're still sitting on this bench." {n}Her eyes are very bright.{/n} "Tell me why."''',
      c('"I dislike what you can make sound reasonable. I also want you. I will have to keep answering both facts."', "answer", flags=f("lodge_desire_contested")),
      c('"I liked watching you take the house from her. I will not pretend that attraction belongs to someone less ambitious than I am."', "answer", flags=f("lodge_danger_desired"))),
    n("answer", "Nocticula", '''"Then don't tell me later that I hid which woman you were choosing."
{n}She stands. She does not sit back down beside you; she stands over you with the dawn wind pulling at her skirts and looks down at you as though you were a city she had been told she could not have. Then she sets one knee on the bench beside your thigh, takes your jaw in her hand, and turns your face up to hers.{/n}
"Both," {n}she says.{/n} "Good. Either one alone would have bored me by spring."
{n}She kisses you hard, in the open gate, in front of the meat carts and the coffle and the singing incubus, and lets you go only when she has decided to. A carter stares. She looks at him, once, and he finds something urgent to do with his mule.
Then she sits down beside you as if nothing had happened, and picks up the cherries again, and looks out through the arch at the road going down to the docks, where it is quite empty now.{/n}
"I'm going to show you my collection next," {n}she says.{/n} "Everything we've taken. You've earned a look at it."
"Our collection?"
{n}She turns her head and considers you, with a cherry halfway to her mouth.{/n}
"We'll see," {n}she says.{/n} "That depends on whether you can stand being seen holding it."''',
      c('[Let the gate and the morning go. Keep the woman on the bench.]', flags=f("lodge_consequences_finished"))),
], "lodge_debt_answered")
# Append after s() adds the existing withdrawal node; its saved position must survive.
SCENES[-1]["Nodes"].append(n("agent_announcement", "Nocticula", '''"The next job." {n}Nocticula smiles.{/n} "She always wants the next job. She came to me last night with her coat on and asked what was after Istrava. And the musicians who read out Istrava's own invitation in her own hall have come to me as well, all six of them, asking to be taken into my service, because they say nobody else in the Middle City will ever hire them again."
"Will you take them?"
"The tenor. He has a lovely voice and no sense at all of when to stop, which is exactly what I want in a herald. The rest I've sold." {n}She spits a cherry stone.{/n} "And Rhez gets a dealer in the Fleshmarket who rented Istrava her quarry by the night. I've been saving him for her. A knife you don't use goes dull, or goes looking for another hand. I don't let my knives go looking." {n}She glances at you.{/n} "Remember that, the next time you feel restless."''', c('"Give her the dealer. Then let\'s see your wager."', "credit"), portrait="Nocticula"))

s("what_she_keeps", "What she keeps", [
    n("start", "Narrator", '''{n}Her gallery is above the Harem of Ardent Dreams, in a long room under the roof with slatted floors, so that the music and the heat and the smell of the Harem come up through the boards. You can look down through the slats and see the couches below, and the bodies on them, and the succubi going between them with trays. Nobody below looks up. It is not done.
The gallery itself is lined with what she keeps.
She walks you through it the way a girl shows off a dollhouse, holding your hand, pulling you from one thing to the next before you have finished looking at the last. Here is a crown she took off a king who is still alive, somewhere, without it. Here is a jar with something in it that blinks. Here is a whole wall of masks, every one of them a face somebody once wore to her court and then could not take off. Here, newer, a row of little gold cages, each with a moth in it, beating against the bars. The moths are fresh. She has them changed every night.
Laulieh is lounging on a couch at the far end of the gallery where she is certainly not supposed to be, eating sugared almonds and admiring her own reflection in a polished shield. She waggles her fingers at you as you pass, and Nocticula ignores her magnificently.{/n}
"This," {n}Nocticula says, stopping at last in the middle of the gallery and spreading her arms,{/n} "is what I keep. Everything here was somebody's, once. Now it's mine." {n}She turns to you.{/n} "And this end of the room is what you helped me take. The harbor, the court, the lodge. Come and look."
{n}At the near end of the gallery, on a table of black wood, lies the brass lens from the cliff door.{/n}''',
      c('"The lens. Is the road still yours?"', "chart", requires=f("chart_intact")),
      c('"The lens is cracked."', "broken", requires=f("chart_lost")),
      c('"The door is shut. What did you keep of it?"', "limited", requires=f("chart_limited"))),
    n("chart", "Nocticula", '''"Of course it is." {n}She picks up the lens and holds it to her eye and looks at you through it, and laughs.{/n} "Whole. Not a scratch. And out on the coast there's a door in the cliff with my flower burning in it, and every captain who sails past at night can see it."
{n}She sets the lens down.{/n}
"Two of them have already come to me, asking to buy passage. One of them was the man who used to buy from Ilvara. He didn't recognize me. He thought I'd be grateful for the custom." {n}She smiles.{/n} "He's in the cells. His ship is mine. The other I let through, at three times what Ilvara charged, because she was polite, and I wanted to see whether the door would hold for a stranger." {n}Her eyes go to the window, toward the coast you cannot see.{/n} "It held. My road. Built on my old permission, opened by your stolen magician, and now it opens for whoever I like. A share of what comes through it is yours, darling. If you can stand being seen holding it."''',
      c('"Show me what became of Ilvara."', "disposition")),
    n("broken", "Nocticula", '''"Cracked right across." {n}She turns it in the light so that the crack throws a thin bright line onto the wall.{/n} "Rhez had it in her hand when the door shut. It's never worked since. The road's gone; the cliff is only a cliff."
{n}She does not sound sorry. She sounds interested, as if the crack were a new kind of jewel.{/n}
"Vessa is downstairs," {n}she says.{/n} "In the Harem. Her hand is splinted, and she'll never hold a bell with it again, and she knows exactly whose door it went into. She wears my flower on her collar now. The girls down there are terrified of her." {n}She sets the lens down with the crack facing you.{/n} "I lost a road. I gained a woman who put her own hand in a closing rock to save my property. I've made worse trades." {n}She glances at you.{/n} "You told me to hold the door narrow. I'll remember that it was you, every time I look at that crack. Don't worry; I don't mind remembering it."''',
      c('"Show me what became of Ilvara."', "disposition")),
    n("limited", "Nocticula", '''{n}She does not pick up the lens. Beside it on the table there is a shallow glass dish, and in the dish a little heap of black threads, brittle and coming apart, that was once a flower worked into an old sail.{/n}
"It fell to pieces in Rhez's pack when the door shut," {n}Nocticula says.{/n} "My old permission. Centuries old. Ilvara cut it off some ship I'd let pass and sewed it into her harbor, and when your count ran out, it simply gave up." {n}She touches the threads with one fingernail, and one of them breaks.{/n} "Nobody will ever open that door again. Including me. You made the price so small I couldn't keep the door afterwards."
"You agreed to it."
"I agreed to it. I didn't agree to like it." {n}She looks at you sideways.{/n} "I keep this dish to remind me that I paid. I always remember what I paid, and to whom. Most people find that alarming."''',
      c('"Show me what became of Ilvara."', "disposition")),
    n("disposition", "Narrator", '''{n}Beyond the lens there is an alcove in the gallery wall, lined with black velvet, the kind of alcove in which a better-run house would keep a statue. Nocticula leads you to it by the hand and stops in front of it.{/n}
"And the magician," {n}she says.{/n} "You haven't asked about her. You've been very good. I can see you wanting to."''',
      c('"Is she still burning?"', "confined", requires=f("ilvara_confined")),
      c('"Is she still working the door?"', "commissioned", requires=f("ilvara_commissioned")),
      c('"Who bought her?"', "exiled", requires=f("ilvara_exiled"))),
    n("confined", "Nocticula", '''"Every night." {n}The alcove is empty. Nocticula points down instead, through the slatted floor, to the far end of the Harem below.{/n}
{n}You look. Over the great bed at the end of the Harem, the one with the black silk hangings, a small brass lamp hangs on a chain, and in the lamp there is a light that is not quite a flame. If you look at it long enough, the light has a shape. The shape is a woman, very small, standing in the glass with her palms pressed against it, watching the bed.{/n}
"She's been watching for weeks," {n}Nocticula says.{/n} "Everything that happens on that bed. Everything. She can't close her eyes; lamps don't have eyelids. I've been down there twice myself, just to give her something to look at." {n}She sounds pleased.{/n} "The Harem thinks she's the most beautiful lamp in the islands. Two people have tried to buy her. One of them was a magician."
"Did you sell?"
"Darling. I never sell anything that's still suffering usefully."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("commissioned", "Nocticula", '''"Day and night." {n}The alcove is not empty. In it, on a black velvet cushion, lies a length of iron chain with a broken link at one end, as if somebody had kept a souvenir.{/n}
"She's on the coast," {n}Nocticula says.{/n} "Collared to the rock, beside her door, with my flower burned on the collar. She opens it when I want it open and shuts it when I'm bored, and every time it bites, it bites her first." {n}She lifts the chain and lets it run through her fingers.{/n} "The guards send me word when it bites. It's bitten her four times. She's lost two fingers and most of an ear, and she's still the best door-warden I've ever had, because she knows that the day she stops being useful, I'll stop feeding her."
{n}She drops the chain back on the cushion.{/n}
"She sends me messages. She has things she'd like to say about the conditions of her work."''',
      c('"Does she still say it, the thing she admitted in the hall?"', "fee_admission", requires=f("hearing_proof")),
      c('"Is she still hiding the danger she would not name?"', "extra_observer", requires=f("hearing_uncertain")),
      c('"Does she still swear she never sold anyone who couldn\'t leave?"', "return_condition", requires=f("hearing_limits")),
      c('"Have her old buyers come looking for her?"', "new_price", requires=f("hearing_business"))),
    n("fee_admission", "Nocticula", '''"Every time she tries to complain. She starts to say the passengers were never prisoners, and the guard reminds her what she admitted in front of my whole court, and she stops." {n}Nocticula smiles.{/n} "You broke her in the hall. She stays broken. I find that very restful."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("extra_observer", "Nocticula", '''"Yes. She held out on you in the hall, and she holds out still. There's something about that door she won't tell me." {n}Nocticula's eyes glitter.{/n} "So I've put a second guard on her, whose only work is to watch her face whenever the door bites, and tell me what she flinches at. Sooner or later she'll flinch at the right thing. I can wait. I'm very good at waiting."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("return_condition", "Nocticula", '''"She swore it in the hall. She swears it to the guards. She swore it to the door, the last time it bit her, at the top of her voice." {n}Nocticula laughs.{/n} "Now she's the one who can't leave. I don't think she's noticed the joke. I've stopped explaining it. Some jokes are better when only the audience gets them."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("new_price", "Nocticula", '''"Three of them, so far. Courtiers from my own steps, the ones who went somewhere else to stand when you asked the hall who'd bought from her." {n}She examines her nails.{/n} "They came to the coast to make sure she wasn't talking. I had them collared beside her. She has company now. They don't get on."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("exiled", "Nocticula", '''"A tanner." {n}The alcove is empty, except for a little card propped on the velvet, the kind they hang round a slave's neck on the Fleshmarket block. It has a number on it.{/n}
"That's what she fetched," {n}Nocticula says, tapping the card.{/n} "Less than her shoes, which I sold separately, to a dancer in the Ten Thousand Delights who wears them on stage. Ilvara's at the tannery on the eastern canal now, scraping hides. They say she still tells the other slaves she was a great magician once, and they don't believe her, and beat her for putting on airs." {n}She props the card straight.{/n} "I go and look at her sometimes, from a carriage. She never sees me. I like that best of all."''',
      c('"And what do you believe we learned about each other?"', "ambition")),
    n("ambition", "Nocticula", '''"That you'll help me take things," {n}she says.{/n} "Willingly. With your own hands, and your own voice, and sometimes with an appetite you'd rather I didn't notice. I noticed."
{n}She walks to the end of the gallery, past Laulieh, who sits up very straight, and stops at the window, which looks out over the Midnight Isles toward the open sea.{/n}
"And that you'll sometimes refuse me, and mean it, and stand there afterwards waiting to find out what it costs. Most people who refuse me run. You wait." {n}She turns.{/n} "I find that more interesting than anything in this room."
"Is that what you wanted to show me?"
"I wanted to show you what I'm going to do with it." {n}She spreads her hand against the glass, over the islands.{/n} "All this. And more than this. I didn't build the Midnight Isles out of dead lords so that I could sit on them and be content. I want more than a harbor and a house and a magician in a lamp. I want things I haven't thought of yet." {n}She looks back at you over her shoulder.{/n} "And I want to know what you want from me, darling, while I take them. Say it carefully. I'll hold you to it."''',
      c('"You told me why you want to leave the Abyss. This work has not made that ambition smaller."', "known", requires=f("parent_ambition_heard")),
      c('"I want to stand beside someone who can hear a rival answer. I do not need you harmless."', "rival"),
      c('"I want power with you. I will argue over its use, not pretend I have no appetite for it."', "power")),
    n("known", "Nocticula", '''"No. It hasn't." {n}She does not turn from the window.{/n} "I told you once what I want past the Abyss, and why I can't walk away from it empty-handed. Every lord I ever killed has friends with long memories. A harbor doesn't change that. A hunting lodge doesn't change it. I don't intend to leave with a small life and a nice view."
{n}She turns then, and comes back down the gallery to you, and takes your face in both hands.{/n}
"So don't imagine, because you've seen me pleased with a lamp and a pair of shoes, that I'll ever be content with a small, manageable future. I'm capable of enjoying small things. I'm not capable of settling for them."
"I wouldn't believe you if you promised."
"Good. Save your disbelief for when it's useful." {n}Her grip tightens.{/n} "When we meet at the Worldwound, remember this room before you decide what I can afford to lose."
"Remember it before you decide what I can afford to give."
{n}She laughs, low, and lets you go.{/n} "Yes. That'll be the troublesome part."''',
      c('"Then let us decide what we are willing to build between those ambitions."', flags=f("ambition_discussed", "future_rivals"))),
    n("rival", "Nocticula", '''"A rival answer," {n}she repeats, delighted.{/n} "From a mortal. In my own gallery, with my servant listening." {n}Behind her Laulieh says "Fie!" under her breath, scandalized and thrilled.{/n} "Oh, I'll hear it. I'll hear every one you have. And then I'll do as I like, and you'll have to stand there and watch me, and come up with a better one for next time."
"And if I never do?"
"Then I'll be bored, and you'll be dead. One of those comes first." {n}She crosses to you and takes the back of your neck in her hand and kisses you, hard, in front of Laulieh and the moths and every mask on the wall, a kiss that is not a question.{/n}
"Come back with an argument I haven't already thought of," {n}she says against your mouth.{/n} "And sometimes with no argument at all. I don't want to find out that the only thing we enjoy together is winning."''',
      c('[Take her hand.] "Then come back with a better argument."', flags=f("ambition_discussed", "future_rivals"))),
    n("power", "Nocticula", '''"There." {n}She looks at you as if you had just handed her something heavy and gold.{/n} "An appetite you haven't dressed up as a sacrifice. I was beginning to think you'd never show me one."
{n}She comes close. Behind her, very quietly, Laulieh stops eating almonds.{/n}
"Then understand mine. Try to tame me, Commander, and you'll find out which of us leaves the cage. I'll want things that ruin your plans, and I'll take them first and tell you afterwards, if I remember. And if you do the same to me—" {n}she smiles{/n} "—I'll admire it, and then I'll make you pay for it, and then I'll admire that too."
{n}She takes your hand and presses it flat against the black velvet of the empty alcove beside her, where a trophy would go.{/n}
"Remember what we agreed about Shamira. My bed hasn't given her my throne. Yours hasn't given you mine. Sell a word from this room and I'll come and collect it from your tongue."
{n}She kisses you, and bites your lower lip when she is finished, not quite hard enough to bleed.{/n}''',
      c('"Then let us see what we can take together."', flags=f("ambition_discussed", "future_power"))),
], "lodge_consequences_finished")

s("second_door", "The second door", [
    n("start", "Narrator", '''{n}She does not take you to her gallery this time. She takes you down into the Harem itself, by the front stair, in front of everyone.
The Harem of Ardent Dreams is full tonight. Couches in tiers under a dome painted with things that move when you are not looking at them; incense; music from somewhere you cannot see; succubi and incubi and their guests tangled on the cushions, and slaves with trays, and courtiers in jewels doing business in low voices in the alcoves. Everyone who matters in the Middle City comes here to buy the Lady's favor from the Ardent Dream's court. They are buying it now. They stop when she comes down the stair.
They stop because she is holding your hand.
She walks you the whole length of the Harem. She does not hurry. She lets them look: at her, at you, at your hand in hers, and the whole vast room goes quiet tier by tier as you pass, the way a crowd goes quiet at an execution when the prisoner is brought out. A courtier with a lapful of contracts lets them slide to the floor. A succubus on the nearest couch stops in the middle of something and stays stopped. The highest couch, the Ardent Dream's, stands empty tonight. That is better. A court tells everything to the one who is not in the room.
Behind the dais at the far end there is a door. It is small and black and has no handle on the outside, and every person in the Harem knows what is behind it, because every person in the Harem has at some time wished to be invited through it.
Nocticula stops in front of it and turns round to face the room.{/n}
"This door is mine," {n}she says. She does not raise her voice; the dome carries it.{/n} "Nobody opens it unbidden. Nobody ever has." {n}She lifts your hand in hers, so that they can all see it.{/n} "Except the Commander, now. Look at the Commander's face, all of you. You'll be seeing it."
{n}Nobody breathes. Then, very quietly, somewhere up in the tiers, someone begins to applaud, and is hushed, and stops.
Nocticula turns her back on them. She looks at you, close, under the dome, with the whole Harem watching and listening, and she is smiling the way she smiled in the bell chamber.{/n}
"There," {n}she says, for you alone.{/n} "Now they know. Everything we did together, and now this. Say something, darling. They're all waiting to hear what the Lady's favorite sounds like."''',
      c('"I would have liked to see them step ashore."', "rescue", requires=f("purpose_rescue")),
      c('"You\'ve shown them your hand. What are you buying with it?"', "advantage", requires=f("purpose_power")),
      c('"You wanted them to see this. What are you still deciding?"', "curiosity", requires=f("purpose_curiosity"))),
    n("rescue", "Nocticula", '''"They did," {n}she says.{/n} "Into my city."
{n}She laughs at your face, softly, so that only the first tier can hear it.{/n}
"You wanted the passengers found. I found them. You stood on my rock and watched them come out of the cliff, wet and blinking, and then you decided where they went. That was you, darling. Not me. I only held the lantern." {n}She brushes something from your collar that is not there.{/n} "Whatever you told yourself in that cell about rescuing people, you've seen now what rescue means in Alushinyrra. It means changing hands."
"You could have let them go."
"I did what you told me. I always do what you tell me, in the end, if it amuses me." {n}She glances out over the silent tiers.{/n} "And it always amuses me to see what you'll choose. That's why they're all looking at you. They've never seen me take orders. They're trying to work out what you cost."''',
      c('"Then let them wonder. Ask me what you brought me here to ask."', "future")),
    n("advantage", "Nocticula", '''"Everything." {n}She is pleased you asked.{/n} "Every one of these people sells my favor for a living. Now they know whose favor is worth more than theirs. By morning half of them will be trying to buy you a drink, and the other half will be trying to have you killed, and all of them will be telling me which is which, to curry favor." {n}She smiles.{/n} "I'll learn more about my own court in a week than I have in a century. You're the best bait I've ever owned."
"Bait?"
"Don't be offended. Bait is the most important part of the hook." {n}She lifts your hand to her mouth and bites the knuckle, lightly, in front of everyone.{/n} "And the most expensive. I don't put just anything on the end of my line."
{n}Up in the tiers someone drops a glass.{/n}''',
      c('"Then let them bite. Ask me what you brought me here to ask."', "future")),
    n("curiosity", "Nocticula", '''"What you'll do," {n}she says.{/n} "With the door. With them watching. I've given you something nobody else in my city has, in front of everybody who could ever take it from you, and I want to know whether you'll walk through it, or stand here and make a speech, or turn round and leave me holding your hand in front of my own court like a fool." {n}Her eyes are very bright.{/n} "I genuinely don't know. Do you understand how rare that is? I always know."
"And if I leave?"
"Then they'll have seen the Lady in Shadow refused, and I'll have to do something very memorable to make them forget it." {n}She smiles.{/n} "So you see, there's no wrong answer. Only interesting ones."''',
      c('"Then let me give you an interesting one. Ask."', "future")),
    n("future", "Nocticula", '''{n}She lets go of your hand. The door stands at her back, black and closed. Behind you, the whole Harem waits.{/n}
"Our old bargain stands," {n}she says.{/n} "The Worldwound. What you'll do when you reach its heart. Nothing in this room changes that, and I'd think less of you if you imagined it did." {n}She tilts her head.{/n} "But this is not the Worldwound. This is my house, and my door, and my court watching. So I'll ask you here, where they can hear the answer."
{n}She leans back against the black door.{/n}
"Will you come back? Not because I've caught you, though I have, or because I've marked you, though I may have. Because you want to stand in my city and choose who runs. Because you want to open this door with your own hand and have all of them hear the latch." {n}Her smile is slow.{/n} "Or will you keep what we already have, and no more, and walk back up that stair in front of everyone with your hands empty? Either way, darling, I'll remember. I remember everything."''',
      c('"Yes. More private evenings and more arguments worth having."', "yes", requires=f("future_rivals")),
      c('"Yes. I want the company and the dangerous work we may choose together."', "power", requires=f("future_power")),
      c('"I want to keep what we already agreed, without making this undertaking a larger promise."', "limited")),
    n("yes", "Nocticula", '''"Then open it."
{n}She steps aside.
The door has no handle. You put your palm flat against the black wood instead, where a handle would be, and for a moment nothing happens, and somewhere behind you somebody laughs nervously. Then you feel it: the Gift, under your skin, answering something in the wood. The latch lifts on the inside with a sound like a key turning in a lock, very loud in the silent Harem, and the door swings inward on darkness and the smell of her.
Behind you, a whole room full of people lets out its breath.{/n}
"There," {n}Nocticula says, at your shoulder, very softly.{/n} "They heard it. Every one of them. They'll be telling that story in the Fleshmarkets for a hundred years." {n}Her mouth is at your ear.{/n} "I've wanted to do this in front of them since the first night. Get in."
{n}She puts her hand flat on your back and pushes you through, not gently, and follows, and kicks the door shut behind her without looking. Inside it is dark and warm, and she has you against the closed door before your eyes have adjusted, her mouth on your throat, her hands already busy. Much later, the room comes back. You are lying on something soft in the dark, with her weight on you and her hair over both your faces, and from very far away, through the door, the Harem has started talking again: one voice, then many, the sound of a whole court beginning to sell what it saw.{/n}
"Listen to them," {n}she says against your neck.{/n} "Every one of them is going to remember tonight. So am I."
{n}You reach to push the hair out of your eyes. She catches your wrist and pins it.{/n}
"Leave it. I want to look at you without your face arranged."''',
      c('[Keep the door. Keep the invitation.]', "end", flags=f("chosen_company"))),
    n("power", "Nocticula", '''"Company and dangerous work." {n}She tastes it, and laughs, low, and the front tier of the Harem shivers.{/n} "Oh, you greedy thing. Yes."
{n}She does not open the door yet. She turns to the room instead, and takes your arm, and walks you along the front of the dais, past the first tier of couches, where the most important of her court sit.{/n}
"You'll want no oath from me, and you won't get one; sworn allies bore me within a year. Every scheme we make, we bargain for fresh. When you refuse me, I'll be furious, and then I'll have you anyway, the same night, in the same bed. And one rule." {n}She stops in front of a courtier in green, a soft man with clever eyes who has been, until tonight, one of the people who sell her favor.{/n} "Nothing said behind that door is ever sold. The first of us who sells a pillow confidence may expect the other to come and collect it in person." {n}She smiles down at the courtier.{/n} "With tongs."
{n}The courtier, who has sold a great many things in his time, goes grey.{/n}
"This one," {n}she tells you, not lowering her voice,{/n} "has been selling introductions to me. He thinks I don't know. I was going to deal with him tonight. I'll do it later. Much later. He can spend tonight imagining what I'll do." {n}She pats the courtier's cheek, twice.{/n} "Don't leave the Harem, sweetheart. I'll want you where I can find you."
{n}Then she takes you back to the black door and opens it herself, with one hand, and the latch sounds through the whole room like a blow, and she pulls you through by the front of your shirt. A long while afterwards she asks what you would have proposed for the courtier. You are lying in the dark with your head on her stomach, and through the door the Harem is still very quiet, as though nobody out there dares to move.
Your answer is brief: send him an introduction to his creditors.{/n}
{n}She lifts her head.{/n}
"I knew there was a reason I kept you."''',
      c('[Keep the alliance, and the door inside it.]', "end", flags=f("chosen_alliance"))),
    n("limited", "Nocticula", '''{n}She is still for a moment. Behind you, the Harem has heard. You can feel it hear: a long, slow shifting along every tier, couches creaking, silk, a whisper starting somewhere high up and being smothered.
Nocticula does not look at them. She looks at you, and her face does not change at all.{/n}
"No," {n}she says.{/n} "In front of all of them."
"I'll keep what we agreed. I won't promise more than that."
"I heard." {n}She reaches past you and lays her palm on the black door, and you hear the latch move inside it, for her, and stop, and not open.{/n} "Then it stays shut. It will stay shut for you until I decide otherwise, and I'll decide it when it suits me, not when you change your mind." {n}She smiles, quite pleasantly.{/n} "I collect my debts, Commander. And I'm in no hurry. Hurry is for mortals."
{n}She takes your arm, as she took it coming in, and turns you round to face the room, and walks you back the whole length of the Harem toward the stair, slowly, with every eye on you. Nobody laughs. Nobody would dare. But they all see your empty hands, and they all see her face, which is smiling, and they all know what it means when the Lady in Shadow smiles like that at someone who has refused her.
At the foot of the stair she lets go.{/n}
"You'll come when I send for you," {n}she says.{/n} "That's what we agreed, and I always keep what I agree. And one night, darling, I'll send for you to collect. You won't know which night until you're standing in it."''',
      c('[Keep the earlier bargain. Leave the door shut.]', "end", flags=f("chosen_limit"))),
    n("end", "Narrator", '''{n}At the last she catches your sleeve, the way she always does, and pulls you back for one more look at you.{/n}
"Wake up," {n}she says.{/n} "I'm finished with you for tonight. Tell your crusaders whatever you like about where you were. Half of them will believe you, and the other half will be right."
{n}You wake in Drezen with the smell of incense in your hair. The room is cold, the lamp gone out. Someone in the corridor is knocking: the morning dispatch, late as usual. You lie still for a moment with your eyes closed, listening, half expecting to hear a latch.{/n}''', c('[Return to the waking world.]', flags=f("complete"))),
], "ambition_discussed")


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue"):
    SCENES.append(scene("noct.ending_" + id, title, owner, 0, "", [n("end", "Narrator", text, portrait="Nocticula")],
        requires=f("complete") + tuple(requires), forbids=tuple(forbids), last=99,
        optional=True, Relationship="nocticula", Remote=True))


# Supplementary recollections of this undertaking, not replacements for native
# or parent political/romantic endings. Root must review epilogue delivery/order.
ORDINARY_BAD = ("noct.dead", "inhuman", "ascended", "sacrifice")
ending("company", "The door she keeps", '''{n}The door behind the dais in the Harem of Ardent Dreams stayed the Commander's to open unbidden. Nobody else ever did. The Ardent Dream's court counted the visits, and sold the count, and Nocticula bought it back from them now and then for the pleasure of reading how often she had been seen to want something.
She did not soften. She still sat in judgment in her throne hall and carried out the sentences herself; she still let her court bet on how long the condemned would last, and still won. She still read the Commander's thoughts whenever the Gift held, and laughed out loud at the parts the Commander had meant to keep, sometimes in company. When the Commander pronounced a sentence at her trials, she carried it out. When the sentence bored her, she said so, and chose a better one.
The harbor and the lodge became stories in the Middle City, and then songs, and the songs got the details wrong, which she preferred. The bell from Istrava's house hung somewhere she could reach it.
She never once said she loved anyone. Once, at a window over the burning city, she told the Commander: "You are mine to disappoint." It was the closest she came, and it was close enough.{/n}''', requires=f("chosen_company"), forbids=ORDINARY_BAD)
ending("alliance", "The chosen instrument", '''{n}The harbor and the lodge were the first things the Commander helped Nocticula take. They were not the last.
She called the Commander "the chosen instrument of my will" in front of her court, and meant it as the highest praise she had, and the court understood it exactly. Instruments are used. This one was used often, and well, and argued about every use, and was kept anyway, because nothing else in her city could surprise her twice.
The courtier who had sold introductions to her waited in the Harem for nine days, as he had been told to, and on the tenth she remembered him. She had his creditors introduced to him one at a time, in a locked room, and the Middle City talked about the result for a season. She told the Commander about it in bed, in detail, and laughed until she cried.
Her rule spread. Houses that had hunted under her protection closed, or burned, or were taken and hunted in by her. Captains who sold passage under borrowed flowers learned to stop. Each of these things she called ours when she was pleased, and mine the rest of the time, and both were true.{/n}''', requires=f("chosen_alliance"), forbids=ORDINARY_BAD)
ending("limit", "An undertaking completed", '''{n}At the end of the harbor undertaking Nocticula offered the Commander her door, in front of her whole court, and the Commander refused it and walked back up the Harem stair with empty hands.
She did not forgive it. She did not punish it, either, not then. She kept the bargain they had made, exactly, to the letter, the way she kept everything she agreed to. She sent for the Commander when the Gift allowed and the Commander came. The door behind the dais stayed shut.
She remembered. The Midnight Isles learned, over that time, that the Lady in Shadow had been refused by a mortal and had smiled about it, and the smile frightened them more than any punishment would have.
Long afterwards, on a night of her own choosing, she sent for the Commander and collected. What she collected, and how, the Commander never told anyone. It was not gold. It was exactly as unpleasant as she had promised, and she enjoyed every moment of it, and at the end of it she laid her hand on the Commander's cheek and said, "There. Paid. I'll think of something else you owe me."{/n}''', requires=f("chosen_limit"), forbids=ORDINARY_BAD)
ending("death", "The unused question", '''{n}After Nocticula's death, the room beside the quay could only be remembered. The dream which once supplied its light no longer brought an invitation from her.
During the harbor affair she had made an entire sea because the Commander noticed its absence. She had kept a damaged lens and an old bollard long after each had ceased to be useful to the conversation. None explained what she might have wanted from another evening.
The passengers had come out of their borrowed harbor before she died. Their names remained in the account, beside the fees she disputed and the questions she had sent back for a better answer. Between two of those reports there had been a private meeting. She had rested her hand beside the Commander's, close enough to touch, and waited.
The next movement belonged to a time when both were still there.{/n}''', requires=("noct.dead",))
ending("sacrifice", "An answer no longer possible", '''{n}After the Commander's sacrifice, the harbor account still contained the questions asked before the crossing. A reader could follow them through amended instructions, the names called at the door, and the reports delivered afterward. The person who had asked them would never read another reply.
Nocticula had once completed a room while deciding how to invite that person back. She had kept a useless bollard beside its hearth and made a window overlooking water that had not been there at first.
On their final visit of the undertaking she had asked whether there should be more evenings. The Commander had given an answer. Now the unfinished invitations belonged to her alone, and even a perfectly chosen question would receive no new answer from the one she had intended to ask.{/n}''', requires=("sacrifice",), forbids=("noct.dead", "inhuman", "ascended"))
ending("ascent", "Her champion comes home", '''{n}When Pharasma summoned the Commander to her court, another summons drowned her out: the Lady in Shadow, calling her champion home. The Commander went.
Nocticula met them in the throne hall in front of everyone, on the dais where she had once sat the Commander at her right hand to let her court wonder what the crusader cost her. Now there was no need to wonder. The Commander came up the steps in true demonic form, and the court went down on its faces, and she laughed, long and hard, and the hall laughed with her because it had learned to.
"I bet on you," she said. "Everyone told me not to. I so rarely lose."
The harbor had been the first thing they took together, and the lodge the second, and they were small things, a door in a cliff and a house in a garden. She kept the bell from Istrava's lodge by her throne anyway, and rang it sometimes when the Commander was away, to see who in her court would flinch. The conquests that followed were not small. They were only beginning.{/n}''', requires=("ascended",), forbids=("noct.dead", "inhuman"))
ending("changed", "The earlier company", '''{n}The Commander of the harbor affair belonged to an earlier time. Nocticula had asked that person for advice, resented some of it, and finished the undertaking with an invitation beside a window overlooking dark water.
Then the Commander changed, and the old invitation ceased to describe the being who might answer it. Nocticula knew the danger of trusting a familiar name after its owner had become something else.
The earlier account still held the missing passengers' names. It held the magician's evasions, the cost of a crossing, and the questions that had exposed an awkward truth. Its final private evening was harder to record. Nocticula had caught a fold of the Commander's sleeve, nearly made a joke, and chosen to speak plainly instead.
That hesitation belonged to the person she had met then.{/n}''', requires=("inhuman",), forbids=("noct.dead",))
ending("aeon", "A harbor without that witness", '''{n}In the remade history, the Commander never arrived at the quay without a sea. Nocticula had no occasion to build its water, move a lamp nearer a couch, or discover which unwelcome question that particular guest would ask.
The two doors, the copied lens, and the bollard beside the hearth belonged to meetings erased with the history that had allowed them. No passenger in the remade world owed a return to the lost investigation. No letter carried an answer from it.
There was no empty place in Nocticula's chamber where the room ought to have been. It had been made for somebody she had not met in that way, during evenings the new world had never contained.{/n}''', owner="AeonEpilogue")


from storylines.nocticula_n1 import scaffold
scaffold(SCENES)
from storylines.nocticula_n2 import write
write(SCENES)


def integrate(payload):
    """Register only verified read-only bindings; root owns export registration."""
    for name, bindings in (("Etudes", ETUDES), ("SeenCues", SEEN_CUES)):
        target = payload.setdefault(name, {})
        for key, value in bindings.items():
            if key in target and target[key] != value:
                raise ValueError("Conflicting Nocticula parent binding: " + key)
            target[key] = deepcopy(value)
    # Native Epilogues/Cue_0294 (enGB 13a9b9dc) requires this flag,
    # the Wound closed, and Nocticula alive. Read only; no authored producer.
    payload.setdefault("UnlockableFlags", {})["noct.native_redeemed"] = "48909f9355f52e14ab3a8748fa3e81a0"
    payload.setdefault("Derived", {})["noct.redeemed_epilogue"] = [["noct.native_redeemed", "ending.wound_closed"]]
    payload.setdefault("DerivedForbids", {})["noct.redeemed_epilogue"] = ["noct.dead"]
    # Existing reserved-key registry: known to validation, never produced.
    pending = payload.setdefault("PendingHooks", [])
    if "noct.retired" not in pending:
        pending.append("noct.retired")
    relationships = payload.setdefault("Relationships", {})
    if "nocticula" in relationships and relationships["nocticula"] != RELATIONSHIP:
        raise ValueError("Conflicting Nocticula relationship registration")
    relationships["nocticula"] = deepcopy(RELATIONSHIP)
