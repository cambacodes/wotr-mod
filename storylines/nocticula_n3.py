"""N3/N5 prose for the N1 placeholder nodes of the lodge and close (Claude, voice-locked).

Text only. Codex owns ids, gates, flags and choice indices (nocticula_n1.py);
this module fills the placeholder text of nodes N1 created, re-texts the
choices N1 appended, voices the second_door discovery chain, and writes the
redeemed-epilogue paragraphs. It runs once, after nocticula_n1.finish_partners,
and refuses to overwrite anything that is not the text it expects, so a
structural change surfaces as an error here. The one exception is
cloud_slots() at the end: two append-only explicit-slot hosts.
"""
from copy import deepcopy

from story_format import c, n
from storylines import nocticula_continuation as route

PENDING = "[N2 PROSE PENDING: "

PROSE = {
    # noct.uninvited_guest: the hostess hunt
    ("uninvited_guest", "bell"): '''{n}She holds the baton loosely under the little brass bell, the way a woman holds a fan she has not yet decided to open. Below her the hall waits. Istrava has half risen on her coils. Suth leans on the gallery rail with his tally-stick in his hand. Down among the cabinets Edris has her arms round her sister, and the third attendant has stopped crying and is simply standing, very still, the way a hare stands in a field when the hawk's shadow crosses it.
Nobody is looking at you. They are all looking at the Lady in the bell chamber, waiting to hear whose name she rings. Only you and she know it is not hers to choose.{/n}
"The house rule," {n}Nocticula tells the room, pleasantly,{/n} "is that when the bell rings, you hunt whoever it names. I'm a great believer in house rules. I've had people boiled for breaking them." {n}She smiles down the horseshoe.{/n} "So nobody break this one."
{n}Then her eyes come back to your rail, and her voice drops, and although she is across the hall it seems to come from just behind your ear.{/n}
"Choose, darling. The hostess, on that lovely tail. The collector, who buys the ones who run; I'd let the girls have the baton for him. Or all of them." {n}Her eyes glitter behind the black silk.{/n} "Every guest in this hall came to watch someone else bleed. Ring it for all of them and see how many remember the way out."''',
    ("uninvited_guest", "hunt.istrava"): '''"Her? Oh, you darling." {n}Nocticula laughs, delighted, and strikes the bell.{/n}
{n}It gives one clear note. The note goes down the hall like a thrown knife, and every masked face in the horseshoe turns toward the highest couch.{/n}
"Istrava," {n}Nocticula says into the silence.{/n} "Your bell. Your rules. Run."
{n}For a breath the hostess does not understand. Then she does. She comes off the couch in a single heave of coils, scattering cushions and wine and a guest too slow to get out of her way, and goes for the garden doors faster than anything that size has a right to move, and the hall goes after her with a howl.
And then you are not at the rail any more.
You are behind Nocticula's eyes. You did not feel her take you; you are simply there, in the gardens, running without effort on bare feet over wet grass, and the night is not dark at all. Through her eyes the hedges are black and silver, every leaf edged with light. Through her ears every heartbeat in the garden is a small drum, and you can tell them apart: the guests' quick and drunk and greedy, the attendants' far off and racing, and somewhere ahead, enormous, slamming, the hostess's.
Istrava is screaming as she goes.{/n}
"You fucking whore, it's my house, it's my bell—"
"Hear that?" {n}Nocticula's voice comes from your own mouth, or from just beside it.{/n} "She thinks things are hers."
{n}A guest blunders across the path ahead, a big one in a boar's mask, laughing, a net over his shoulder. Nocticula does not slow. She goes through him; you feel your own hand, which is her hand, open his throat in passing the way one slits a letter, and he sits down in the hedge and stops laughing. Nobody catches the hostess but her.
The garden forks. Three paths, three dry fountains, the scrape of scales on stone somewhere ahead and the echo of it everywhere. Nocticula stops, and lets you have the eyes.{/n}
"Well?" {n}she whispers.{/n} "You found the bell its name. Now find me the bell's mistress."''',
    ("uninvited_guest", "caught.clean"): '''{n}The scrape is wrong. It comes from the left, loud, too loud: the noise of a tail dragged deliberately across gravel. Under it, from the right, so faint that only those ears could have caught it, comes a sound like a held breath. Something large is trying very hard not to pant.
You turn her head to the right. Nocticula laughs, and runs.
The third fountain is dry and choked with dead leaves, and Istrava is coiled in the basin with both hands over her mouth and the moths in her hair beating themselves to powder against their cages. She comes up out of the leaves at the last moment, all coils and nails. Nocticula steps inside the strike as if it were an invitation to dance, takes her by the hair, and puts her face down on the fountain's rim. Then she sets one bare heel on the back of the hostess's neck, and leans.
The guests arrive in a crowd, panting, with nets and knives and torches, and stop at the edge of the light.{/n}
"Mine," {n}Nocticula tells them, not loudly.{/n} "The bell named her for me." {n}She looks down at the woman under her heel.{/n} "You hid in a fountain, sweetheart. In your own garden. That's the first thing you've done tonight that surprised me." {n}She bears down until Istrava sobs.{/n} "Don't do it again."
{n}You are back at your rail before they drag her in. Your own feet are dry. You can still feel the shape of that neck under a heel you do not have.{/n}''',
    ("uninvited_guest", "caught.costly"): '''{n}You choose the left, where the scales scrape loudest. She goes where you send her, and it is the wrong path.
Istrava has dragged her tail across the gravel there and doubled back along the hedge; the scrape was a decoy. The real sound comes a heartbeat later than it should have, from the far side of the garden by the service yard: a scream, and it is not the hostess's.
Nocticula turns and runs, and through her eyes you see what she sees.
The third attendant, the one who could not stop crying behind her mask, has been cutting across the lawn toward the service door. Istrava does not stop to bargain with her. She takes the girl up in her coils as she passes, the way a wave takes a swimmer, and squeezes once, and lets go, and the girl lies on the lawn in a shape a body should not make.
It buys the hostess nothing. Nocticula is on her before the girl stops moving, has her by the hair, and puts her face down across the body, and sets a bare heel on the back of her neck.{/n}
"That," {n}she says, a little out of breath,{/n} "was mine. You owe me a servant now. I'll take it out of you." {n}She does not look at the dead girl. She looks, through the eyes you share, at you.{/n} "Don't sulk, darling. You chose a path. Paths cost something. Next time, listen harder."
{n}You are back at your rail before they drag Istrava in. Your own hands are clean. You cannot stop seeing the shape on the lawn.{/n}''',
    ("uninvited_guest", "hunt.suth"): '''"Suth." {n}Nocticula tastes the name, and her smile spreads.{/n} "Oh, I like that. The man who buys the ones who run." {n}She leans out of the bell chamber and calls down into the gallery.{/n} "Edris. Catch."
{n}She tosses the baton. It turns over once in the air above the hall, and Edris, who has never in her life caught anything thrown to her by a queen, catches it in both hands against her chest.{/n}
"Your bell," {n}Nocticula tells her.{/n} "Your rules. Ring it."
{n}Edris looks at the baton. Then she looks at the collector leaning on the gallery rail, and something in her face goes very calm. She climbs the bell chamber stair with the baton in her fist, and Nocticula steps aside for her, and Edris strikes the bell so hard it cracks.
"Suth," she says, to the whole hall. Her voice shakes, and carries anyway.
Suth is quick. He is over the rail and running before the note has finished; he knows the house, and he goes for the garden doors. The guests do not move. They look at Istrava, and Istrava looks at Nocticula, and nobody gets up.
The attendants go after him. Mera goes first, in her mother's red shoes, with the comb from the trophy cabinet in her fist, teeth outward. The third girl follows, still masked. Edris comes down the stair last, with the baton.
And then you are not at the rail. You are behind Nocticula's eyes, high on the lodge roof where she has gone to watch, and the garden below is black and silver and full of small drums, and you can hear every one of them: three servants' hearts, fast and furious, closing on one that is faster.
They catch him at the second fountain. You watch, through her eyes, what three women can do to a man with a comb, a baton and their bare hands. Nocticula watches with her chin on her fist and laughs twice, quietly, at the good parts. When Rhez comes out of the hedge and pulls them off him he is still alive. Rhez is careful about that. Her lady wants him for later.{/n}
"Look at them," {n}Nocticula murmurs, with your mouth.{/n} "An hour ago they were quarry. Now they're mine, and they've tasted it. I've made assassins out of less."
{n}Then she comes down off the roof and walks back into the hall, where the hostess is still on her couch, and you are at your rail again in time to watch Istrava learn what becomes of the mistress of a house where the servants have been allowed to ring the bell.{/n}''',
    ("uninvited_guest", "hunt.guests"): '''"All of them." {n}For a moment Nocticula is quite still in the bell chamber. Then she laughs, softly, with real pleasure, the way a woman laughs when a lover has said something filthy in company.{/n} "Oh, you greedy thing."
{n}She strikes the bell. One clear note.{/n}
"Everyone," {n}she tells the hall.{/n} "Every one of you. It's the rule."
{n}Nobody moves. A guest near the door laughs, uncertainly, waiting for the joke. Then the hedges beyond the garden doors begin to move, and the joke arrives.
Her assassins come in out of the dark. You have not seen them all evening; nobody has. Grey shapes, quiet and in no hurry, a dozen and then more, over the sills and down from the gallery roof and up the service stair, and the first guest dies with his cup still at his mouth.
And then you are not at the rail. You are behind Nocticula's eyes, and she is in the middle of it.
It is short and ugly. Through her eyes it is also beautiful, which is the worst of it: every heartbeat in the hall a small drum, the drums stopping one by one, silver on every edge, the blood black. The guests run for the gardens where they meant to hunt, and the gardens are full of her people. A rich mortal in a jeweled mask goes down on his knees in the wine and screams at nobody, over and over,{/n} "This wasn't the game! This wasn't the bloody game!" {n}until somebody makes him stop.
Nocticula kills only two herself, and only because they come at her. The rest she watches, turning slowly in the middle of the hall like a dancer waiting for her music, and you watch with her. When a grey shape comes for the hostess on her couch, Nocticula says one word, and the assassin bows and goes elsewhere.{/n}
"Not her," {n}she says, with your own mouth.{/n} "I want her talking."''',
    ("uninvited_guest", "waking"): '''{n}You wake in Drezen with your heart going like a drum and your feet aching as though you had run a mile barefoot on gravel. For a long moment you lie still and listen for scales on stone. There is only the wind, and somebody coughing on the wall walk.{/n}''',
    ("uninvited_guest", "waking.wenduag"): '''{n}Wenduag is crouched on her heels against the wall outside your door, as if she has been there some time.{/n} "You were hunting." {n}It is not a question.{/n} "In your sleep, Commander. I heard you through the door. You were running, and you were smiling." {n}She rises, and looks at you with something close to hunger.{/n} "Next time, take me."''',
    ("uninvited_guest", "waking.greybor"): '''{n}Greybor is in the yard, oiling a blade he has already oiled.{/n} "You talk in your sleep." {n}He does not look up.{/n} "Counting. Heartbeats, it sounded like. Then 'left' and 'right' a few times, and then you laughed." {n}He tests the edge on his thumbnail.{/n} "Whoever has you doing that at night, I hope they pay well. I'd want triple."''',
    ("uninvited_guest", "waking.daeran"): '''{n}Daeran studies you over his breakfast cup with frank delight.{/n} "Darling, you look positively debauched, and I happen to know you slept alone." {n}He sips.{/n} "Someone is taking you out at night. Somewhere with very good wine and very bad manners, by the look of you. Do introduce us before I become jealous."''',

    # noct.unborrowed_evening: the slot and its aftermath
    ("unborrowed_evening", "noct.unborrowed_evening.explicit.1"): '''{n}You stop talking. She moves the knife to the far end of the sill, out of your reach and well within hers, and pulls you down under the window, with the city burning on the other side of the glass. Her mouth is on yours before you land, hot and sticky with pear, her fist in your collar; she opens the hooks of the black gown one by one without looking, the dried blood at its hem crackling against the cushions, and shoves it off her shoulders.{/n}
"The hunt left me hungry," {n}she says against your jaw, her hand dragging down your chest.{/n} "I have no patience left for you tonight."
{n}She holds your eyes a moment longer, then her mouth takes yours again, and the window, the city and the knife on the sill fall out of the world.{/n}''',
    ("unborrowed_evening", "noct.unborrowed_evening.aftermath.1"): '''{n}The pear is still on the sill when the window greys. The knife is where she put it.
She lies across you on the cushions, heavy and warm and entirely awake, drawing idly on your chest with one sticky fingernail: a fountain, a bell, a little serpent with its tail tied in a knot. Down in the city the night's bells have stopped, and the morning's have not yet begun.{/n}
"Better," {n}she says.{/n} "I told you. A hunt does that." {n}She bites your shoulder, lazily, for no reason you can see.{/n} "You're very quiet. You were quiet at the rail too. You stood there and chose and never said a word, and I could hear every thought in your head." {n}She props her chin on her hand.{/n} "Ask me something, then. You've been wanting to since the pear."
"Why here? Why this window, and not your bed?"''',

    # noct.bell_without_master: the spoils
    ("bell_without_master", "rhez"): '''"Rhez." {n}Nocticula turns to the doorway, delighted.{/n} "Did you hear? The Commander's giving you a house."
{n}Rhez stops chewing. For the first time since you have known her, she has nothing to say.
Nocticula crosses the hall to her. On the way she stoops and picks something up off the tiles: one of the attendants' masks from the gallery, white, the mouth cut too wide, its ribbon still threaded with the little steel hook. She pulls the ribbon free of the mask and ties it round Rhez's wrist, tight, with the hook turned in against the skin.{/n}
"There's your leash," {n}she says.{/n} "Take it off whenever you like. It takes the skin with it." {n}She pats the knot.{/n} "The house is yours. The cellar is yours. The hostess in the cellar is yours. You'll hunt here when I tell you to, and keep it for me when I don't, and every guest who comes through that door will know who holds your other end."
"Yes, Lady." {n}Rhez's voice is not quite steady.{/n}
"Go on, then. I want to see whether you bite."
{n}Rhez looks at the cellar door. Then she walks to it, opens it, and goes down the stair into the dark without a lamp. A moment later the knocking stops. There is a sound that is not knocking, and then Istrava's voice, high and furious, and then not furious at all.
When Rhez comes back up she is wiping her mouth on her sleeve.{/n}
"She called me a servant," {n}she says.{/n}
"And?"
"She won't again." {n}Rhez spits something small onto the tiles. It is the tip of a forked tongue.{/n}
{n}Nocticula throws back her head and laughs, long and hard, and the empty hall rings with it.{/n} "Oh, she bites. Look, darling. She bites."''',

    # noct.no_applause: the wager
    ("no_applause", "wager"): '''{n}She settles back against the wall behind the bench and looks across the road at the two women and their trunk, the way one looks at a pair of horses at the start of a race.{/n}
"There's the course." {n}She points with a cherry stem: the arch, the road going down between the warehouses, the masts at the bottom of it.{/n} "From this bench to the docks. A quarter of a mile, all of it my city, and not a thread of my flower on either of them. If they make the water, a boat will take them somewhere duller. If they don't—" {n}she shrugs{/n} "—they belong to whoever catches them. That's what free means."
{n}Across the road Mera lets go of her sister's hand. She crosses alone, in her mother's red shoes, and stops in front of the bench, and looks down at the Lady in Shadow. Her face is white. Her voice is not.{/n}
"Are we yours," {n}she says,{/n} "or aren't we?"
{n}Nocticula looks up at her for a long moment. Then she smiles, slowly, genuinely pleased.{/n}
"That, sweetheart, is the most interesting question anyone's asked me all month." {n}She spits a cherry stone neatly past Mera's shoe.{/n} "Run along and find out."
{n}Mera goes back to her sister. They lift the trunk between them and go out through the arch and down the road toward the masts, walking fast, not looking back.
Nocticula holds out her hand to you, palm up, the way a gambler holds out a hand for the stake.{/n}
"Pick a side, darling, and I'll take the other. I don't mind which." {n}Her eyes are bright.{/n} "I already know how it ends. You know this city nearly as well as I do now. Bet like it."''',
    ("no_applause", "run.caught"): '''{n}They get two hundred yards.
At the bottom of the road, under the cookshop awning, the lean man in the plain coat lifts one bandaged hand, and his men go out from under the awning like dogs let off a leash. The sisters see them coming and drop the trunk and run, and it does not matter. Edris goes down first, tripped and dragged by the hair. Mera fights. She gets her nails into one face and her teeth into one hand before they twist her arms behind her, and one red shoe comes off and lies in the road.
Suth brings them back up the hill himself, walking behind his men with his hands held carefully in front of him, and has them put on their knees before the bench, and bows.{/n}
"Lady. Two runaways. Found on your road."
{n}Nocticula looks at the sisters for a while. Mera is crying with rage. Edris is not crying at all; she is looking at you.{/n}
"Not mine any more," {n}Nocticula says.{/n} "That was the point." {n}She sighs, as if at a tiresome expense.{/n} "Oh, they're crying. Good; it raises the price. The Harem. Somebody there will find a use for girls who bite." {n}She waves Suth off.{/n} "And bring the shoe. I like the shoe."''',
    ("no_applause", "run.free"): '''{n}They make the docks.
You watch them all the way down: two small figures and a cheap trunk going fast between the warehouses, past the cookshops, past a coffle climbing the other way on its chain, past a pair of dockside bravos who turn to look at the red shoes and then, for no reason either of them could have given, decide not to. Nobody stops them. Nobody is collecting in Alushinyrra this morning on paper with Suth's name on it.
At the bottom of the hill they reach the water, and a boat, and a man in the boat who takes their coin. They go down into it out of sight behind the stacked crates, and are gone.
Nocticula watches the place where they were. She does not look disappointed. She looks like a woman who has just watched a very good throw of the dice.{/n}
"Free," {n}she says.{/n} "In Alushinyrra." {n}She eats the last cherry and folds the empty paper into a small, neat square.{/n} "Give it a week. I'll send flowers."''',

    # noct.what_she_keeps
    ("what_she_keeps", "executed"): '''{n}The alcove is empty. Beside it, on a plain iron hook driven into the wall at the height of a woman's hand, hang a pair of white shoes by their heel straps. Someone has cleaned them. Someone has polished them.{/n}
"I had them hung where I'd see them when I'm bored," {n}Nocticula says.{/n} "I'm bored quite often. It works beautifully." {n}She touches one shoe and sets it swinging.{/n} "I was right about my hands. I'm always right about myself."
{n}She considers the empty alcove a moment longer, her head on one side.{/n}
"My only regret is the light. She'd have made the loveliest lamp." {n}She turns away.{/n} "Never mind. You gave me a good death instead. Most nights I'd rather have a good death than a good lamp."''',

    # noct.second_door: waking codas
    ("second_door", "waking"): '''{n}The dispatch is real, and late, and dull. You read it standing at the window with the incense still in your hair, and when you go down into the yard the morning is only the morning: mud, horses, a sergeant shouting. Nobody in Drezen heard a latch. You catch yourself listening for one anyway.{/n}''',
    ("second_door", "waking.arueshalae"): '''{n}Arueshalae stops in the corridor when she sees you. Her eyes go to the mark at your throat and stay there, and her wings shift uneasily at her back.{/n} "Commander. That mark." {n}She speaks very quietly.{/n} "I know whose that is. Any of my kind would. It means she has put her name on you." {n}She swallows.{/n} "Please be careful. She never gives anything she can't take back."''',
    ("second_door", "waking.daeran"): '''{n}Daeran glances at your throat over the rim of his cup, and lowers the cup.{/n} "Still wearing it openly, I see. Bold. Positively scandalous." {n}He smiles, slowly.{/n} "You came down those stairs like someone who has just been shown off, darling. I know the walk; I invented half of it. Give my regards to whoever holds your leash. Tell her she has excellent taste."''',
    ("second_door", "waking.seelah"): '''{n}Seelah falls in beside you on the wall walk and looks at the mark on your throat for a long moment before she says anything.{/n} "It's darker." {n}She keeps her voice low.{/n} "I'm not going to ask where you go at night, Commander. I'm not sure I want to know. But whoever put that on you is showing you off to somebody." {n}She bumps your shoulder with hers, roughly.{/n} "If you ever need someone at your back while you tell her no, you know where I'll be."''',
}

# Choices appended or created by N1 (nocticula_n1.py): (scene, node, index) -> (N1 text, N3 text).
CHOICES = {
    ("uninvited_guest", "start", 4): ("[Enter as guests.]", "[Go in by the front door, as guests.]"),
    ("uninvited_guest", "held", 1): ('"Make her name every patron first."', '"Let her think she\'s buying her life. Make her name every patron first."'),
    ("uninvited_guest", "bell", 0): ('"Ring it for her."', '"Ring it for her. Let\'s see the hostess run."'),
    ("uninvited_guest", "bell", 1): ('"Ring it for Suth."', '"Ring it for Suth. Give Edris the baton."'),
    ("uninvited_guest", "bell", 2): ('"Ring it for all of them."', '"Ring it for all of them."'),
    ("uninvited_guest", "hunt.istrava", 0): ("[Find her.]", "[Find her for Nocticula. Perception, DC 32.]"),
    ("uninvited_guest", "caught.clean", 0): ("Continue", "[Drag her back to her hall.]"),
    ("uninvited_guest", "caught.costly", 0): ("Continue", "[Drag her back to her hall.]"),
    ("uninvited_guest", "hunt.suth", 0): ("Continue", "[Watch the hostess's turn.]"),
    ("uninvited_guest", "hunt.guests", 0): ("Continue", "[Wait for the hall to go quiet.]"),
    ("bell_without_master", "judgment", 2): ('"Give it to Rhez."', '"Give it to Rhez. On a leash."'),
    ("bell_without_master", "rhez", 0): ("Continue", "[Let Rhez keep her house.]"),
    ("no_applause", "wager", 0): ('"They are dragged back before the gate."', '"I bet they\'re dragged back before they reach the water."'),
    ("no_applause", "wager", 1): ('"They are dragged back before the gate."', '"I bet they\'re dragged back before they reach the water."'),
    ("no_applause", "wager", 2): ('"They make the docks."', '"I bet they make the docks."'),
    ("no_applause", "wager", 3): ('"They make the docks."', '"I bet they make the docks."'),
    ("no_applause", "run.caught", 0): ("Continue", '"Settle up, then."'),
    ("no_applause", "run.free", 0): ("Continue", '"Settle up, then."'),
    ("what_she_keeps", "disposition", 3): ("[Look at the empty hook.]", '"You kept her shoes."'),
    ("what_she_keeps", "executed", 0): ("Continue", '"And what do you believe we learned about each other?"'),
}

# The discovery Nocticula arranges after the Harem door (shared discovery() helper,
# voiced here for this scene only): (node id, expected old opening, new text).
DISCOVERY = (
    ("partner_discovery.end.0", "{n}The clerk has put the morning dispatch on top of your private packet.", '''{n}The knock is the dispatch, as you thought. On top of it, where the clerk could not have missed it, lies a folded letter you did not send for: her last private invitation to you, and burned across its seal a second seal, pressed so hard the wax has split. The courier who brought it wore the livery of the Harem of Ardent Dreams. He asked the clerk to say it came with the Lady's compliments.
Behind your eyes, before you have finished reading the seal, the Gift stirs. She is laughing.{/n}
"Of course she found out. I sent it through her house." {n}The voice is warm and very close.{/n} "You walked through her Harem with my hand in yours and my door open for you, and you thought a secret would keep. I wanted to watch her face, darling. It was everything I hoped. Read her answer. She wrote it for you."'''),
    ("partner_discovery.end.0.alive", "{n}A scrap of Nocticula", '''{n}Shamira's answer is written across the back of the invitation in a sharp, fast hand, the pen driven through the paper in two places.{/n} "So. The door behind my dais, opened for a Golarian in front of my own court, on a night she knew I would be elsewhere. She chose the night well. She always does. I'll remember that, Golarian. Enjoy her door. Doors have two sides, and I hold the keys to more of hers than she thinks."'''),
    ("partner_discovery.end.0.body", "{n}A scrap of Nocticula", '''{n}Shamira's answer is written across the back of the invitation in a sharp, fast hand, the pen driven through the paper in two places.{/n} "So. The door behind my dais, opened for a Golarian in front of my own court, on a night she knew I would be elsewhere. She chose the night well. She always does. I'll remember that, Golarian. Enjoy her door. Doors have two sides, and I hold the keys to more of hers than she thinks."'''),
    ("partner_discovery.end.0.mind", "{n}Inside your mind,", '''{n}The voice that answers inside your skull is not Nocticula's. It wakes with you, and it is furious.{/n} "You hid her from me. In here. In the head I live in. And she sent the proof to my old house so that my own court could read it before I did." {n}Something behind your eyes scrapes, like nails down a door.{/n} "I'll remember every word she whispers to you here, Golarian. Every one. Tell her that."'''),
    ("partner_discovery.end.0.captive", "{n}The answering message comes from Shamira", '''{n}The answer comes from Shamira's court, not from Shamira. The woman herself is still behind the lock you put on her and cannot answer anything. Her courtiers have copied the invitation in a fair hand and enclosed a list of the houses that have already bought copies.{/n} "The Ardent Dream's household thanks the Commander for the intelligence. The Lady bought the first three copies herself."'''),
    ("partner_discovery.end.0.dead", "{n}The answering message comes from Shamira", '''{n}The answer comes from what is left of Shamira's court. Their mistress is gone; her courtiers are not. They have copied the invitation, sold it twice, and sent the original on with a note.{/n} "The Lady's invitations have found another bed. The court thanks the Commander for the intelligence, and the Lady for the commission."'''),
    ("partner_discovery.end.0.cast", "{n}The answering message comes from Shamira", '''{n}The answer comes from what is left of Shamira's court. Their mistress is gone; her courtiers are not. They have copied the invitation, sold it twice, and sent the original on with a note.{/n} "The Lady's invitations have found another bed. The court thanks the Commander for the intelligence, and the Lady for the commission."'''),
    ("partner_discovery.end.0.declined", "{n}The answering message comes from Shamira", '''{n}The answer comes from what is left of Shamira's court. Their mistress is gone; her courtiers are not. They have copied the invitation, sold it twice, and sent the original on with a note.{/n} "The Lady's invitations have found another bed. The court thanks the Commander for the intelligence, and the Lady for the commission."'''),
    ("partner_discovery.end.0.fallout", '"So much for discretion.', '''"So much for your little secret. Don't sulk; it was never going to survive me." {n}Her voice behind your eyes is lazy with pleasure.{/n} "You asked me to hide you. I did, for exactly as long as it amused me, and then something amused me more. No more love letters. When I want you, I'll take you, the way I always have, and you'll find out afterwards who else was told."
{n}The Gift goes quiet. On the desk the dispatch is still waiting, and on top of it the split seal, which you find you do not want to touch.{/n}'''),
    ("partner_discovery.end.0.hidden", "{n}A hand knocks at the door.", '''{n}The knock is the dispatch. Its corner lies under her last private invitation, the one you had meant to burn and had not yet. You draw the dispatch free and hold the invitation to the lamp, and it curls and goes black before the clerk comes in. No seal leaves the room. Nothing goes to the Harem.
Behind your eyes, faintly, she laughs.{/n}
"You would have enjoyed keeping that. So would her servants." {n}A pause.{/n} "Burn the next one too. You may come when I take you. You may not keep a pretty little collection for Shamira to buy."'''),
)
DISCOVERY_CHOICE = ("[Show Nocticula the answer.]", "[Let her read it through your eyes.]")

# Native redeemed branch only (13a9b9dc): she renounces the Abyss and keeps herself.
REDEEMED = {
    "noct.ending_company": '''{n}When the Lady in Shadow renounced the Midnight Isles and went to Elysium as the Redeemer Queen, Alushinyrra said the crusader had done it to her. She let them say it. In Midnight's Palette she still kept a door that only the Commander opened unbidden, and behind it she was exactly who she had always been: amused, imperious, hungry, and the one who decided. Exiles came to her because they had nowhere else, and she took them in the way she had once taken a harbor, as hers. "I didn't soften," she told the Commander. "I moved house. You're still mine to disappoint."{/n}''',
    "noct.ending_alliance": '''{n}When the Lady in Shadow renounced her realm and rose to Elysium as the Redeemer Queen, patroness of exiles, she took her chosen instrument with her. Midnight's Palette needed hands that could still hold a knife; she had not changed what she wanted from the Commander, only what she would let it be used on. She still bet, and still won. The exiles who came to her found a queen who would shelter anyone she found interesting and forgive almost nothing, and who argued with her instrument over every use and kept it anyway.{/n}''',
    "noct.ending_limit": '''{n}When the Lady in Shadow renounced the Abyss and became the Redeemer Queen, the Commander supposed the debt had gone with the old title. A letter from Midnight's Palette, in her own hand, corrected the error: she had changed a great many things about herself, and kept her memory. The next time she collected, it was gentler than the Lady in Shadow would have made it. She made sure the Commander understood that she had decided it would be.{/n}''',
}

# The legacy exits are voiced once, in nocticula_continuation.s() (EARLY_WITHDRAW /
# LATE_WITHDRAW), reconciling the N2 and N3 drafts; these scenes must still carry them.
LATE_WITHDRAW = ("no_applause", "what_she_keeps", "second_door")
EARLY_WITHDRAW = ("uninvited_guest", "unborrowed_evening", "bell_without_master")


def _node(scene, nid):
    return next(x for x in scene["Nodes"] if x["Id"] == nid)


def write(payload):
    """After nocticula_n1.finish_partners: fill placeholders and re-text N1 choices."""
    by = {s["Id"]: s for s in payload["Scenes"]}
    for (sid, nid), text in PROSE.items():
        node = _node(by["noct." + sid], nid)
        assert node["Text"].startswith("{n}" + PENDING), (sid, nid)
        node["Text"] = text.strip()
    for (sid, nid, index), (before, after) in CHOICES.items():
        choice = _node(by["noct." + sid], nid)["Choices"][index]
        assert choice["Text"] == before, (sid, nid, index, choice["Text"])
        choice["Text"] = after
    door = by["noct.second_door"]
    for nid, before, text in DISCOVERY:
        node = _node(door, nid)
        assert node["Text"].startswith(before), (nid, node["Text"][:60])
        node["Text"] = text
        for choice in node["Choices"]:
            if choice["Text"] == DISCOVERY_CHOICE[0]:
                choice["Text"] = DISCOVERY_CHOICE[1]
    for sids, text in ((LATE_WITHDRAW, route.LATE_WITHDRAW), (EARLY_WITHDRAW, route.EARLY_WITHDRAW)):
        for sid in sids:
            assert _node(by["noct." + sid], "withdraw_undertaking")["Text"] == text, sid
    for sid, text in REDEEMED.items():
        blocks = [x for x in _node(by[sid], "end").get("Paragraphs", [])
                  if x.get("Requires") == ["noct.redeemed_epilogue"]]
        assert len(blocks) == 1 and blocks[0]["Text"].startswith("{n}" + PENDING), sid
        blocks[0]["Text"] = text
    cloud_slots(payload)


# Cloud noct-reconcile: two optional explicit slots (briefs in
# tools/route_packs/explicit_slots/nocticula/). Append-only: the host keeps its
# text, choices and positions; the appended choice leads to the heated cut,
# whose aftermath re-offers the host's own exits unchanged.
CLOUD_SLOTS = (
    ("noct.last_buyer", "named", "[Make her collect for it here, under the lamps.]",
     "{n}She does not wait for the stair to empty. She has you against the wall under the nearest lamp, and every chained face in the row is turned toward the light, toward the two of you, unable to look away; she makes sure of that.{/n}",
     '''{n}Afterwards she sits on the bottom stair with her gown pulled straight and your blood under one fingernail, which she examines in the lamplight with interest. Down the row the chained heads are still turned toward you as far as their chains allow. None of them has closed their eyes. None of them can.{/n}
"They'll remember that longer than the merchant will," {n}she says, pleased.{/n} "Go and wake up, darling. Your crusade will want to know where you've been. Soon someone will tell them."'''),
    ("noct.empty_chair", "vow_guard", "[Keep the mask on.]",
     "{n}She does not untie the mask. She puts you against the edge of the table instead, among the wax and the charcoal, and keeps one hand on the ribbon at the back of your head, where the hook is.{/n}",
     '''{n}Later the model of the lodge has lost one of its stairs, crushed flat under somebody's shoulder, and the charcoal plan is smeared past reading. Nocticula does not mind. She has it by heart. She unhooks the mask from your hair at last, with one fingernail, slowly, and keeps the strand that tore on the steel, winding it round her finger.{/n}
"Now you know how her quarry feel when the bell rings," {n}she says.{/n} "Remember it. Plan the entrance, darling, and then we'll go and make Istrava wear something much worse."'''),
)


def cloud_slots(payload):
    by = {s["Id"]: s for s in payload["Scenes"]}
    for sid, host, label, cut, aftermath in CLOUD_SLOTS:
        scene = by[sid]
        key, after = sid + ".explicit.1", sid + ".aftermath.1"
        if any(x["Id"] == key for x in scene["Nodes"]):
            continue
        exits = deepcopy(_node(scene, host)["Choices"])
        _node(scene, host)["Choices"].append(c(label, key))
        scene["Nodes"].append(n(key, "Narrator", cut, c("Continue", after), portrait="Nocticula"))
        scene["Nodes"].append(n(after, "Narrator", aftermath, *exits, portrait="Nocticula"))
